"""Read a Markdown submission wrapper and prepare the team's snapshot evidence.

A team occasionally submits the Moodle wrapper as a Markdown file instead of a
PDF.  The PDF fetcher cannot read that wrapper, so this module extracts the
same facts from it: the permalink at a full SHA, the recording link, the member
table's GitHub usernames, and the real-name and email tokens the privacy scan
needs.  It writes the canonical ``pdf-info.json`` beside the fetched snapshot so
the evidence collector and the privacy scan read the same keys for either kind
of wrapper.

The wrapper is private Moodle material.  Matched values stay in the team's work
directory and never reach stdout.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT
from tools.grader_tools.submission_pdf import (
    EMAIL_PATTERN,
    OPERATOR_SOURCE,
    PDF_INFO_FILENAME,
    REPO_FULL_PATTERN,
    SNAPSHOT_DIRNAME,
    CommitCheck,
    PdfMember,
    PdfPermalink,
    SnapshotFetchError,
    SubmissionPdfError,
    check_commit,
    fetch_snapshot,
    find_permalink,
    find_recording_link,
    find_text_urls,
    parse_permalink_override,
    permalink_week,
    week_mismatch_warning,
    write_pdf_info,
)

MARKDOWN_SUFFIXES = {".md", ".markdown"}
NAME_TOKEN_MIN_LENGTH = 3
COMMON_WORDS = {
    "team",
    "week",
    "github",
    "username",
    "name",
    "email",
    "university",
    "project",
    "members",
    "member",
    "participated",
    "this",
    "with",
    "from",
    "and",
    "the",
}


@dataclass(frozen=True)
class MarkdownMetadata:
    path: Path
    text: str
    permalink: PdfPermalink | None
    recording_link: str | None
    members: tuple[PdfMember, ...]
    github_usernames: tuple[str, ...]
    name_tokens: tuple[str, ...]
    email_tokens: tuple[str, ...]


@dataclass(frozen=True)
class MarkdownFetchResult:
    assignment: str
    team_dir: str
    pdf_info: dict[str, object]
    pdf_info_path: Path
    snapshot_dir: Path
    summary_lines: tuple[str, ...]
    week_mismatch: bool
    snapshot_fetched: bool


def _dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _clean_username(value: str) -> str | None:
    username = value.strip().strip("`*_").lstrip("@").strip(".,;:()[]<>")
    if not username or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*", username):
        return None
    return username


def _name_tokens(name: str, username: str | None, seen_usernames: set[str]) -> list[str]:
    tokens: list[str] = []
    for part in re.split(r"[\s\-]+", name):
        normalized = part.strip(".,;:()'\u2019`*_").casefold()
        if len(normalized) < NAME_TOKEN_MIN_LENGTH:
            continue
        if username is not None and normalized == username.casefold():
            continue
        if normalized in seen_usernames or normalized in COMMON_WORDS or normalized in tokens:
            continue
        if not normalized.isalpha():
            continue
        tokens.append(normalized)
    return tokens


def _table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _table_header(line: str) -> tuple[int, int, int] | None:
    cells = _table_cells(line)
    lowered = [cell.casefold() for cell in cells]
    username_index = next(
        (index for index, cell in enumerate(lowered) if "github" in cell or "username" in cell),
        None,
    )
    email_index = next(
        (index for index, cell in enumerate(lowered) if "email" in cell or "mail" in cell),
        None,
    )
    name_index = next(
        (
            index
            for index, cell in enumerate(lowered)
            if "name" in cell and index != username_index and index != email_index
        ),
        None,
    )
    if username_index is None or email_index is None or name_index is None:
        return None
    return username_index, name_index, email_index


def _separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_markdown_members(
    text: str,
) -> tuple[list[PdfMember], list[str], list[str], list[str]]:
    """Return members, usernames, name tokens, and email tokens from the wrapper.

    The member table is read when it has a GitHub-username column, a name column,
    and an email column.  A line outside the table that carries an email (a
    "team change" note, for example) contributes its capitalised name words too,
    so the privacy scan catches a real name that left the table.
    """
    lines = text.splitlines()
    members: list[PdfMember] = []
    usernames: list[str] = []
    name_tokens: list[str] = []
    seen_usernames: set[str] = set()
    header: tuple[int, int, int] | None = None
    table_rows: set[int] = set()
    for index, line in enumerate(lines):
        if "|" in line and header is None:
            header = _table_header(line)
            if header is not None:
                table_rows.add(index)
                continue
        if header is not None and "|" in line and index > 0:
            cells = _table_cells(line)
            if _separator_row(cells):
                table_rows.add(index)
                continue
            if len(cells) <= max(header):
                break
            username = _clean_username(cells[header[0]])
            email_match = EMAIL_PATTERN.search(cells[header[2]])
            if username is None or email_match is None:
                continue
            table_rows.add(index)
            seen_usernames.add(username.casefold())
            usernames.append(username)
            tokens = _name_tokens(cells[header[1]], username, seen_usernames)
            name_tokens.extend(tokens)
            members.append(PdfMember(github_username=username, name_tokens=tuple(tokens)))

    for index, line in enumerate(lines):
        if index in table_rows or not EMAIL_PATTERN.search(line):
            continue
        for match in EMAIL_PATTERN.finditer(line):
            before = line[: match.start()]
            for username_match in re.finditer(r"@([A-Za-z0-9][A-Za-z0-9-]*)", before):
                username = _clean_username(username_match.group(1))
                if username is not None:
                    seen_usernames.add(username.casefold())
                    usernames.append(username)
            for phrase in re.findall(r"[A-Z][A-Za-z'-]+(?:\s+[A-Z][A-Za-z'-]+)*", before):
                name_tokens.extend(_name_tokens(phrase, None, seen_usernames))

    email_tokens = _dedupe(
        match.group(0).casefold() for match in EMAIL_PATTERN.finditer(text)
    )
    return (
        members,
        _dedupe(usernames),
        _dedupe(name_tokens),
        email_tokens,
    )


def read_markdown_metadata(path: Path, primary_index: str) -> MarkdownMetadata:
    text = path.read_text(encoding="utf-8", errors="replace")
    urls = find_text_urls(text)
    permalink = find_permalink(
        urls, text, primary_index, sources={url: "link" for url in urls}
    )
    recording_link = find_recording_link(urls, text, permalink)
    members, usernames, name_tokens, email_tokens = parse_markdown_members(text)
    return MarkdownMetadata(
        path=path,
        text=text,
        permalink=permalink,
        recording_link=recording_link,
        members=tuple(members),
        github_usernames=tuple(usernames),
        name_tokens=tuple(name_tokens),
        email_tokens=tuple(email_tokens),
    )


def select_markdown_wrapper(
    submission_dir: Path, primary_index: str
) -> MarkdownMetadata:
    candidates = sorted(
        path
        for path in submission_dir.iterdir()
        if path.is_file() and path.suffix.casefold() in MARKDOWN_SUFFIXES
    )
    if not candidates:
        raise SubmissionPdfError(f"no PDF and no Markdown in {submission_dir}")
    parsed: list[MarkdownMetadata] = []
    errors: list[str] = []
    for path in candidates:
        try:
            parsed.append(read_markdown_metadata(path, primary_index))
        except SubmissionPdfError as exc:
            errors.append(f"{path.name}: {exc}")
    if not parsed:
        raise SubmissionPdfError(
            f"no readable Markdown in {submission_dir} ({'; '.join(errors)})"
        )
    for metadata in parsed:
        if metadata.permalink is not None:
            return metadata
    return parsed[0]


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def _write_week_mismatch_summary(
    work_dir: Path, assignment: str, team_dir: str, warning: str
) -> None:
    work_dir.mkdir(parents=True, exist_ok=True)
    rerun = (
        f'uv run python scripts/fetch_markdown_snapshot.py {assignment} '
        f'"{team_dir}" --permalink "<the right full permalink>"'
    )
    (work_dir / "summary.md").write_text(
        f"# {assignment} / {team_dir}\n\n{warning}\n\n{rerun}\n", encoding="utf-8"
    )


def fetch_markdown_submission(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
    *,
    repo: str | None = None,
    permalink: str | None = None,
    check_commit_fn: Callable[[str, str], CommitCheck] = check_commit,
    fetch_snapshot_fn: Callable[[str, str, Path], None] = fetch_snapshot,
) -> MarkdownFetchResult:
    config = ASSIGNMENT_CONFIG.get(assignment)
    if config is None:
        raise SubmissionPdfError(f"unknown assignment: {assignment}")
    if repo is not None and not REPO_FULL_PATTERN.fullmatch(repo):
        raise SubmissionPdfError(f"--repo must be org/repo, got {repo!r}")
    submission_dir = root / FEEDBACK_ROOT / assignment / "submissions" / team_dir
    if not submission_dir.is_dir():
        raise SubmissionPdfError(f"submission directory not found: {submission_dir}")
    metadata = select_markdown_wrapper(submission_dir, config["primary_index"])
    work_dir = root / FEEDBACK_ROOT / assignment / "work" / team_dir
    snapshot_dir = work_dir / SNAPSHOT_DIRNAME
    pdf_info_path = work_dir / PDF_INFO_FILENAME

    if snapshot_dir.exists():
        shutil.rmtree(snapshot_dir)
    snapshot_dir.mkdir(parents=True)

    override = parse_permalink_override(permalink) if permalink is not None else None
    link = override or metadata.permalink
    expected_week = config["week"]
    found_week = permalink_week(link.path) if link is not None else None
    week_mismatch = found_week is not None and found_week != expected_week
    commit: CommitCheck | None = None
    fetched = False
    repo_full = link.repo_full if link else None
    permalink_source = OPERATOR_SOURCE if link is not None else None
    summary = [
        f"{assignment} / {team_dir}",
        f"  markdown: {metadata.path.name} (no PDF wrapper)",
    ]

    if link is None:
        summary.append("  permalink: none (no full 40-character SHA in the Markdown)")
        summary.append(
            "  commit: not checked; stopping repository-dependent checks per docs/grader-policy.md#submission-and-snapshot-rules"
        )
    else:
        if repo_full is None and repo is not None:
            repo_full = repo
            summary.append(
                f"  permalink: repo={repo} sha={link.sha} path={link.path or '(root)'} source={permalink_source} (from --repo)"
            )
        else:
            summary.append(
                f"  permalink: repo={repo_full} sha={link.sha} path={link.path or '(root)'} source={permalink_source}"
            )
        if week_mismatch:
            warning = week_mismatch_warning(assignment, found_week, expected_week, link.path)
            summary.append(warning)
            _write_week_mismatch_summary(work_dir, assignment, team_dir, warning)
        elif repo_full is not None:
            commit = check_commit_fn(repo_full, link.sha)
            state = "exists" if commit.exists else "missing"
            on_main = "unknown" if commit.on_main is None else ("yes" if commit.on_main else "no")
            summary.append(
                f"  commit: {state}; on_main={on_main} ({commit.on_main_status or 'n/a'}); "
                f"snapshot_time={commit.snapshot_time or 'n/a'}"
            )
            if not commit.exists:
                summary.append(
                    "  snapshot: not fetched; stopping repository-dependent checks per docs/grader-policy.md#submission-and-snapshot-rules"
                )
            else:
                fetch_snapshot_fn(repo_full, link.sha, snapshot_dir)
                fetched = True
                summary.append(
                    f"  snapshot: fetched {len(list(snapshot_dir.iterdir()))} top-level entries to {_relative(snapshot_dir, root)}"
                )

    summary.append(f"  recording: {'present' if metadata.recording_link else 'not found'}")
    summary.append(
        f"  member tokens: {len(metadata.github_usernames)} usernames, "
        f"{len(metadata.name_tokens)} name tokens, {len(metadata.email_tokens)} email tokens "
        f"(values only in {_relative(pdf_info_path, root)})"
    )
    summary.append(f"  pdf-info: {_relative(pdf_info_path, root)}")

    pdf_info: dict[str, object] = {
        "assignment": assignment,
        "team_dir": team_dir,
        "pdf": metadata.path.name,
        "pdf_path": _relative(metadata.path, root),
        "page_count": 0,
        "submission_format": "markdown",
        "recording_link": metadata.recording_link,
        "org": repo_full.split("/", 1)[0] if repo_full else None,
        "repo": repo_full,
        "sha": link.sha if link is not None else None,
        "permalink": link.url if link is not None else None,
        "permalink_path": link.path if link is not None else None,
        "permalink_week": found_week,
        "expected_week": expected_week,
        "permalink_week_mismatch": week_mismatch,
        "permalink_source": permalink_source,
        "snapshot_time": commit.snapshot_time if commit else None,
        "commit_exists": commit.exists if commit else None,
        "on_main": commit.on_main if commit else None,
        "on_main_status": commit.on_main_status if commit else None,
        "snapshot_fetched": fetched,
        "snapshot_dir": _relative(snapshot_dir, root),
        "github_usernames": list(metadata.github_usernames),
        "privacy_tokens": {
            "name_tokens": list(metadata.name_tokens),
            "email_tokens": list(metadata.email_tokens),
        },
    }
    write_pdf_info(pdf_info_path, pdf_info)
    return MarkdownFetchResult(
        assignment=assignment,
        team_dir=team_dir,
        pdf_info=pdf_info,
        pdf_info_path=pdf_info_path,
        snapshot_dir=snapshot_dir,
        summary_lines=tuple(summary),
        week_mismatch=week_mismatch,
        snapshot_fetched=fetched,
    )

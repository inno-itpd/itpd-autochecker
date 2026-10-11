"""Read the Moodle submission PDF and fetch the snapshot it permalinks to.

The PDF is the only per-team submission artifact.  This module extracts the
permalink to the primary index (organization, repository, and full 40-character
SHA), the recording link, the page count, and the member table from it, checks
the commit on GitHub, fetches the tarball at the permalink SHA into
``itpd-assignments-feedback/<A>/work/<team_dir>/``, and writes
``tmp/<A>/<team_dir>/pdf-info.json`` for the other grader helpers.
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT

PDF_INFO_FILENAME = "pdf-info.json"
PDF_SUFFIX = ".pdf"
PAGE_NUMBER_PATTERN = re.compile(r'<page\s+number="(\d+)"')
PDFINFO_PAGES_PATTERN = re.compile(r"^Pages:\s+(\d+)\s*$", re.MULTILINE)
HTML_LINK_PATTERN = re.compile(r'<a\s+href="([^"]+)"')
PDF_URI_STRING_PATTERN = re.compile(rb"/URI\s*\(((?:\\.|[^\\()])*)\)")
PDF_URI_HEX_PATTERN = re.compile(rb"/URI\s*<([0-9A-Fa-f\s]+)>")
URL_PATTERN = re.compile(r"https?://[^\s\"'<>()\[\]]+")
URL_TAIL_PATTERN = re.compile(r"https?://\S*$")
GITHUB_PERMALINK_PATTERN = re.compile(
    r"https?://github\.com/(?P<org>[^/\s]+)/(?P<repo>[^/\s]+)/(?:blob|tree)/(?P<sha>[0-9a-f]{40})(?P<path>/[^\s\"'<>()\[\]]*)?"
)
GITHUB_REPO_PATTERN = re.compile(r"https?://github\.com/(?P<org>[^/\s]+)/(?P<repo>[^/\s]+)")
BARE_SHA_PATTERN = re.compile(r"(?<![0-9a-fA-F])(?P<sha>[0-9a-f]{40})(?![0-9a-fA-F])")
REPO_AT_SHA_PATTERN = re.compile(r"(?P<org>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)\s+at\s+(?P<sha>[0-9a-f]{40})")
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
RECORDING_HINT_PATTERN = re.compile(r"record|kickoff|meeting|validation|drive|zoom|youtu", re.IGNORECASE)
URL_CONTINUATION_CHARS = frozenset(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._~:/?#[]@!$&'()*+,;=%-"
)


class SubmissionPdfError(RuntimeError):
    """The submission PDF is missing or cannot be read."""


class SnapshotFetchError(RuntimeError):
    """The GitHub commit check or the snapshot fetch failed."""


@dataclass(frozen=True)
class PdfPermalink:
    url: str
    org: str
    repo: str
    sha: str
    path: str
    source: str

    @property
    def repo_full(self) -> str:
        return f"{self.org}/{self.repo}"


@dataclass(frozen=True)
class PdfMember:
    github_username: str
    name_tokens: tuple[str, ...]


@dataclass(frozen=True)
class PdfMetadata:
    pdf_path: Path
    page_count: int
    text: str
    links: tuple[str, ...]
    permalink: PdfPermalink | None
    recording_link: str | None
    members: tuple[PdfMember, ...]
    email_tokens: tuple[str, ...]


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class CommitCheck:
    exists: bool
    snapshot_time: str | None
    on_main: bool | None
    on_main_status: str | None


@dataclass(frozen=True)
class SnapshotFetchResult:
    assignment: str
    team_dir: str
    pdf_info: dict[str, object]
    pdf_info_path: Path
    work_dir: Path
    summary_lines: tuple[str, ...]


def run_command(command: list[str], *, input_bytes: bytes | None = None) -> CommandResult:
    try:
        process = subprocess.run(command, capture_output=True, input=input_bytes)
    except FileNotFoundError as exc:
        raise SubmissionPdfError(f"{command[0]} is not installed") from exc
    return CommandResult(
        returncode=process.returncode,
        stdout=process.stdout.decode("utf-8", errors="replace"),
        stderr=process.stderr.decode("utf-8", errors="replace"),
    )


def run_gh(args: list[str]) -> CommandResult:
    return run_command(["gh", *args])


def parse_pdftohtml_links(xml: str) -> list[str]:
    return _dedupe(html.unescape(match.group(1)) for match in HTML_LINK_PATTERN.finditer(xml))


def _unescape_pdf_string(value: bytes) -> bytes:
    out = bytearray()
    index = 0
    escapes = {ord("n"): b"\n", ord("r"): b"\r", ord("t"): b"\t", ord("b"): b"\b", ord("f"): b"\f"}
    while index < len(value):
        byte = value[index]
        if byte == ord("\\") and index + 1 < len(value):
            following = value[index + 1]
            if following in escapes:
                out.extend(escapes[following])
                index += 2
                continue
            if following in b"()\\":
                out.append(following)
                index += 2
                continue
            if ord("0") <= following <= ord("7"):
                octal = value[index + 1 : index + 4]
                digits = bytes(character for character in octal if ord("0") <= character <= ord("7"))
                out.append(int(digits, 8) & 0xFF)
                index += 1 + len(digits)
                continue
            index += 1
            continue
        out.append(byte)
        index += 1
    return bytes(out)


def parse_pdf_uri_annotations(raw: bytes) -> list[str]:
    urls: list[str] = []
    for match in PDF_URI_STRING_PATTERN.finditer(raw):
        urls.append(_unescape_pdf_string(match.group(1)).decode("utf-8", errors="replace"))
    for match in PDF_URI_HEX_PATTERN.finditer(raw):
        digits = re.sub(rb"\s+", b"", match.group(1))
        if len(digits) % 2:
            digits += b"0"
        payload = bytes.fromhex(digits.decode("ascii", errors="ignore"))
        if payload.startswith(b"\xfe\xff"):
            urls.append(payload[2:].decode("utf-16-be", errors="replace"))
        else:
            urls.append(payload.decode("utf-8", errors="replace"))
    return _dedupe(urls)


def rejoin_wrapped_urls(text: str) -> str:
    lines = text.splitlines()
    joined: list[str] = []
    index = 0
    while index < len(lines):
        current = lines[index].rstrip()
        while True:
            tail = _trailing_url(current)
            if tail is None or index + 1 >= len(lines):
                break
            following = lines[index + 1].strip()
            if not _continues_url(tail, following):
                break
            index += 1
            current += following
        joined.append(current)
        index += 1
    return "\n".join(joined)


def _trailing_url(line: str) -> str | None:
    match = URL_TAIL_PATTERN.search(line)
    return match.group(0) if match else None


def _continues_url(tail: str, following: str) -> bool:
    if not tail or tail[-1] not in URL_CONTINUATION_CHARS:
        return False
    if not following or following.startswith("http"):
        return False
    if any(character.isspace() for character in following):
        return False
    if following.endswith(":"):
        return False
    return following[0] in URL_CONTINUATION_CHARS


def _dedupe(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def find_text_urls(text: str) -> list[str]:
    return _dedupe(match.group(0).rstrip(".,;:") for match in URL_PATTERN.finditer(rejoin_wrapped_urls(text)))


def extract_pdf_text(pdf_path: Path) -> str:
    attempts = (["pdftotext", "-q", "-raw", str(pdf_path), "-"], ["pdftotext", "-q", "-layout", str(pdf_path), "-"])
    for command in attempts:
        result = run_command(command)
        if result.stdout.strip():
            return result.stdout
        if result.returncode != 0 and result.stderr.strip():
            raise SubmissionPdfError(f"pdftotext failed for {pdf_path.name}: {result.stderr.strip()}")
    raise SubmissionPdfError(f"pdftotext produced no text for {pdf_path.name}")


def extract_pdf_links(pdf_path: Path) -> list[str]:
    try:
        xml = run_command(["pdftohtml", "-q", "-xml", "-stdout", "-i", str(pdf_path)]).stdout
    except SubmissionPdfError:
        xml = ""
    links = parse_pdftohtml_links(xml) if xml else []
    if not links:
        links = parse_pdf_uri_annotations(pdf_path.read_bytes())
    return links


def extract_pdf_page_count(pdf_path: Path, xml: str = "") -> int:
    try:
        info = run_command(["pdfinfo", str(pdf_path)])
    except SubmissionPdfError:
        info = CommandResult(returncode=1, stdout="", stderr="")
    match = PDFINFO_PAGES_PATTERN.search(info.stdout)
    if match:
        return int(match.group(1))
    if not xml:
        try:
            xml = run_command(["pdftohtml", "-q", "-xml", "-stdout", "-i", str(pdf_path)]).stdout
        except SubmissionPdfError:
            xml = ""
    numbers = [int(number) for number in PAGE_NUMBER_PATTERN.findall(xml)]
    if numbers:
        return max(numbers)
    raise SubmissionPdfError(f"cannot read the page count of {pdf_path.name}")


def find_permalink(
    urls: list[str],
    text: str,
    primary_index: str,
    sources: dict[str, str] | None = None,
) -> PdfPermalink | None:
    sources = sources or {}
    best: tuple[int, int, PdfPermalink] | None = None
    for order, url in enumerate(urls):
        match = GITHUB_PERMALINK_PATTERN.match(url)
        if not match:
            continue
        path = (match.group("path") or "").rstrip(".,;:")
        candidate = PdfPermalink(
            url=url,
            org=match.group("org"),
            repo=match.group("repo"),
            sha=match.group("sha"),
            path=path,
            source=sources.get(url, "text"),
        )
        score = _path_score(path, primary_index)
        if best is None or score > best[0]:
            best = (score, order, candidate)
    if best is not None:
        return best[2]
    return _permalink_from_bare_sha(urls, text, sources)


def _path_score(path: str, primary_index: str) -> int:
    clean = path.split("#", 1)[0].rstrip("/")
    index = f"/{primary_index}"
    if clean == index:
        return 3
    directory = index.rsplit("/", 1)[0]
    if clean == directory or clean.startswith(f"{directory}/"):
        return 2
    return 1 if clean else 0


def _permalink_from_bare_sha(urls: list[str], text: str, sources: dict[str, str]) -> PdfPermalink | None:
    for url in urls:
        match = GITHUB_REPO_PATTERN.match(url)
        if match:
            shas = {sha_match.group("sha") for sha_match in BARE_SHA_PATTERN.finditer(text)}
            if len(shas) != 1:
                return None
            sha = shas.pop()
            return PdfPermalink(
                url=f"https://github.com/{match.group('org')}/{match.group('repo')}",
                org=match.group("org"),
                repo=match.group("repo"),
                sha=sha,
                path="",
                source=sources.get(url, "text"),
            )
    match = REPO_AT_SHA_PATTERN.search(text)
    if match:
        return PdfPermalink(
            url=f"https://github.com/{match.group('org')}/{match.group('repo')}",
            org=match.group("org"),
            repo=match.group("repo"),
            sha=match.group("sha"),
            path="",
            source="text",
        )
    return None


def find_recording_link(urls: list[str], text: str, permalink: PdfPermalink | None) -> str | None:
    candidates: list[str] = []
    for url in urls:
        if url.startswith("mailto:") or GITHUB_REPO_PATTERN.match(url):
            continue
        if permalink is not None and url == permalink.url:
            continue
        candidates.append(url)
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    for url in candidates:
        position = text.find(url)
        context = text[max(0, position - 160) : position] if position >= 0 else ""
        if RECORDING_HINT_PATTERN.search(context):
            return url
    return candidates[0]


def parse_member_table(text: str) -> tuple[list[PdfMember], list[str]]:
    lines = text.splitlines()
    header = _find_table_header(lines)
    members: list[PdfMember] = []
    usernames: set[str] = set()
    if header is not None:
        header_index, username_first = header
        for line in lines[header_index + 1 :]:
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split()
            if len(EMAIL_PATTERN.findall(stripped)) != 1 or not EMAIL_PATTERN.fullmatch(parts[-1].rstrip(".,;:")):
                break
            tokens = [token.rstrip(".,;:") for token in parts[:-1]]
            if not 2 <= len(tokens) <= 5:
                break
            username = tokens[0] if username_first else tokens[-1]
            name_parts = tokens[1:] if username_first else tokens[:-1]
            member = _build_member(username, name_parts, usernames)
            if member is not None:
                members.append(member)
    else:
        for line in lines:
            stripped = line.strip()
            if len(EMAIL_PATTERN.findall(stripped)) != 1:
                continue
            tokens = [token.rstrip(".,;:") for token in stripped.split() if not EMAIL_PATTERN.fullmatch(token.rstrip(".,;:"))]
            if not 2 <= len(tokens) <= 4:
                continue
            member = _build_member(tokens[0], tokens[1:], usernames)
            if member is not None:
                members.append(member)
    email_tokens = _dedupe(token.casefold() for token in EMAIL_PATTERN.findall(text))
    return members, email_tokens


def _find_table_header(lines: list[str]) -> tuple[int, bool] | None:
    for index, line in enumerate(lines):
        lowered = line.casefold()
        if "github" in lowered and "name" in lowered and ("mail" in lowered or "email" in lowered):
            return index, lowered.find("github") < lowered.find("name")
    return None


def _build_member(username: str, name_parts: list[str], seen_usernames: set[str]) -> PdfMember | None:
    clean_username = username.strip().lstrip("@").strip(".,;:")
    if not clean_username:
        return None
    seen_usernames.add(clean_username.casefold())
    tokens: list[str] = []
    for part in name_parts:
        for token in re.split(r"[\s\-]+", part):
            normalized = token.strip(".,;:()'\u2019").casefold()
            if len(normalized) < 3 or normalized == clean_username.casefold():
                continue
            if normalized not in seen_usernames and normalized not in tokens:
                tokens.append(normalized)
    return PdfMember(github_username=clean_username, name_tokens=tuple(tokens))


def read_pdf_metadata(pdf_path: Path, primary_index: str) -> PdfMetadata:
    text = extract_pdf_text(pdf_path)
    links = extract_pdf_links(pdf_path)
    text_urls = find_text_urls(text)
    permalink_sources = {url: "link" for url in links}
    urls = _dedupe([*links, *text_urls])
    permalink = find_permalink(urls, text, primary_index, sources=permalink_sources)
    recording_link = find_recording_link(urls, text, permalink)
    members, email_tokens = parse_member_table(text)
    page_count = extract_pdf_page_count(pdf_path)
    return PdfMetadata(
        pdf_path=pdf_path,
        page_count=page_count,
        text=text,
        links=tuple(links),
        permalink=permalink,
        recording_link=recording_link,
        members=tuple(members),
        email_tokens=tuple(email_tokens),
    )


def select_submission_pdf(submission_dir: Path, primary_index: str) -> PdfMetadata:
    pdfs = sorted(
        path for path in submission_dir.iterdir() if path.is_file() and path.suffix.casefold() == PDF_SUFFIX
    )
    if not pdfs:
        raise SubmissionPdfError(f"no PDF in {submission_dir}")
    parsed: list[PdfMetadata] = []
    errors: list[str] = []
    for pdf_path in pdfs:
        try:
            parsed.append(read_pdf_metadata(pdf_path, primary_index))
        except SubmissionPdfError as exc:
            errors.append(f"{pdf_path.name}: {exc}")
    if not parsed:
        raise SubmissionPdfError(f"no readable PDF in {submission_dir} ({'; '.join(errors)})")
    for metadata in parsed:
        if metadata.permalink is not None:
            return metadata
    return parsed[0]


def check_commit(repo: str, sha: str, runner: Callable[[list[str]], CommandResult] = run_gh) -> CommitCheck:
    commit = runner(["api", f"repos/{repo}/commits/{sha}", "--jq", ".commit.committer.date"])
    if commit.returncode != 0:
        if _is_not_found(commit.stderr):
            return CommitCheck(exists=False, snapshot_time=None, on_main=None, on_main_status=None)
        raise SnapshotFetchError(f"gh api commits/{sha} failed: {commit.stderr.strip()}")
    snapshot_time = commit.stdout.strip() or None
    compare = runner(["api", f"repos/{repo}/compare/{sha}...main", "--jq", ".status"])
    if compare.returncode != 0:
        if _is_not_found(compare.stderr):
            return CommitCheck(exists=True, snapshot_time=snapshot_time, on_main=False, on_main_status="not-found")
        raise SnapshotFetchError(f"gh api compare/{sha}...main failed: {compare.stderr.strip()}")
    status = compare.stdout.strip()
    return CommitCheck(
        exists=True,
        snapshot_time=snapshot_time,
        on_main=status in {"identical", "ahead"},
        on_main_status=status or None,
    )


def _is_not_found(stderr: str) -> bool:
    lowered = stderr.casefold()
    return "404" in lowered or "not found" in lowered


def fetch_snapshot(repo: str, sha: str, work_dir: Path) -> None:
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)
    try:
        download = subprocess.run(["gh", "api", f"repos/{repo}/tarball/{sha}"], capture_output=True)
    except FileNotFoundError as exc:
        raise SnapshotFetchError("gh is not installed") from exc
    if download.returncode != 0:
        raise SnapshotFetchError(
            f"gh api tarball/{sha} failed: {download.stderr.decode('utf-8', errors='replace').strip()}"
        )
    try:
        extract = subprocess.run(
            ["tar", "-xz", "--strip-components=1", "-C", str(work_dir)],
            input=download.stdout,
            capture_output=True,
        )
    except FileNotFoundError as exc:
        raise SnapshotFetchError("tar is not installed") from exc
    if extract.returncode != 0:
        raise SnapshotFetchError(
            f"tar extraction failed: {extract.stderr.decode('utf-8', errors='replace').strip()}"
        )


def fetch_team_snapshot(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
    *,
    check_commit_fn: Callable[[str, str], CommitCheck] = check_commit,
    fetch_snapshot_fn: Callable[[str, str, Path], None] = fetch_snapshot,
) -> SnapshotFetchResult:
    config = ASSIGNMENT_CONFIG.get(assignment)
    if config is None:
        raise SubmissionPdfError(f"unknown assignment: {assignment}")
    submission_dir = root / FEEDBACK_ROOT / assignment / "submissions" / team_dir
    if not submission_dir.is_dir():
        raise SubmissionPdfError(f"submission directory not found: {submission_dir}")
    metadata = select_submission_pdf(submission_dir, config["primary_index"])
    work_dir = root / FEEDBACK_ROOT / assignment / "work" / team_dir
    pdf_info_path = root / "tmp" / assignment / team_dir / PDF_INFO_FILENAME

    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True)

    permalink = metadata.permalink
    commit: CommitCheck | None = None
    fetched = False
    summary = [f"{assignment} / {team_dir}", f"  pdf: {metadata.pdf_path.name} ({metadata.page_count} page(s))"]
    if permalink is None:
        summary.append("  permalink: none (no full 40-character SHA in the PDF)")
        summary.append("  commit: not checked; stopping repository-dependent checks per docs/grader-policy.md#submission-and-snapshot-rules")
    else:
        summary.append(
            f"  permalink: repo={permalink.repo_full} sha={permalink.sha} "
            f"path={permalink.path or '(root)'} source={permalink.source}"
        )
        commit = check_commit_fn(permalink.repo_full, permalink.sha)
        state = "exists" if commit.exists else "missing"
        on_main = "unknown" if commit.on_main is None else ("yes" if commit.on_main else "no")
        summary.append(
            f"  commit: {state}; on_main={on_main} ({commit.on_main_status or 'n/a'}); "
            f"snapshot_time={commit.snapshot_time or 'n/a'}"
        )
        if not commit.exists:
            summary.append("  snapshot: not fetched; stopping repository-dependent checks per docs/grader-policy.md#submission-and-snapshot-rules")
        else:
            fetch_snapshot_fn(permalink.repo_full, permalink.sha, work_dir)
            fetched = True
            summary.append(f"  snapshot: fetched {len(list(work_dir.iterdir()))} top-level entries to {_relative(work_dir, root)}")

    name_tokens = sorted({token for member in metadata.members for token in member.name_tokens})
    summary.append(f"  recording: {'present' if metadata.recording_link else 'not found'}")
    summary.append(
        f"  member tokens: {len(metadata.members)} usernames, {len(name_tokens)} name tokens, "
        f"{len(metadata.email_tokens)} email tokens (values only in {_relative(pdf_info_path, root)})"
    )
    summary.append(f"  pdf-info: {_relative(pdf_info_path, root)}")

    pdf_info: dict[str, object] = {
        "assignment": assignment,
        "team_dir": team_dir,
        "pdf": metadata.pdf_path.name,
        "pdf_path": _relative(metadata.pdf_path, root),
        "page_count": metadata.page_count,
        "recording_link": metadata.recording_link,
        "org": permalink.org if permalink else None,
        "repo": permalink.repo_full if permalink else None,
        "sha": permalink.sha if permalink else None,
        "permalink": permalink.url if permalink else None,
        "permalink_path": permalink.path if permalink else None,
        "snapshot_time": commit.snapshot_time if commit else None,
        "commit_exists": commit.exists if commit else None,
        "on_main": commit.on_main if commit else None,
        "on_main_status": commit.on_main_status if commit else None,
        "snapshot_fetched": fetched,
        "work_dir": _relative(work_dir, root),
        "github_usernames": [member.github_username for member in metadata.members],
        "privacy_tokens": {"name_tokens": name_tokens, "email_tokens": list(metadata.email_tokens)},
    }
    write_pdf_info(pdf_info_path, pdf_info)
    return SnapshotFetchResult(
        assignment=assignment,
        team_dir=team_dir,
        pdf_info=pdf_info,
        pdf_info_path=pdf_info_path,
        work_dir=work_dir,
        summary_lines=tuple(summary),
    )


def write_pdf_info(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    os.chmod(temporary, 0o600)
    temporary.replace(path)


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()

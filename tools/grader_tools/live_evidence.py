"""Collect the live GitHub evidence for one team into its team work directory.

The A2 grading prompt's procedure step 5 defines the gh calls, their field
lists, and the limit per call.  Those lists are constants here, so the
collector and the prompt cannot drift apart; ``tests/test_live_evidence.py``
checks them against ``A2/grading_prompt.md``.

The collector reads ``itpd-assignments-feedback/<assignment>/work/<team_dir>/pdf-info.json``
(written by ``scripts/fetch_team_snapshot.py``) for the repository and the
snapshot SHA, writes JSON dumps beside it, and returns a compact summary of
counts and paths. Raw dumps are only written to files, never printed.
"""

from __future__ import annotations

import json
import os
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT
from tools.grader_tools.submission_pdf import (
    PDF_INFO_FILENAME,
    CommandResult,
    run_gh,
)

LABEL_FIELDS = ("name", "description")
LABEL_LIMIT = 200
ISSUE_FIELDS = (
    "number",
    "title",
    "labels",
    "state",
    "stateReason",
    "createdAt",
    "closedAt",
    "body",
    "url",
    "author",
    "closedByPullRequestsReferences",
)
ISSUE_LIMIT = 1000
PR_FIELDS = (
    "number",
    "title",
    "author",
    "headRefName",
    "baseRefName",
    "state",
    "createdAt",
    "mergedAt",
    "closedAt",
    "body",
    "closingIssuesReferences",
    "reviews",
    "files",
    "url",
)
PR_LIMIT = 500
RUN_FIELDS = ("databaseId", "workflowName", "headSha", "event", "status", "conclusion", "createdAt", "url")
RUN_LIMIT = 100
RUN_SHA_FIELDS = ("name", "event", "conclusion", "html_url")
PATH_COMMIT_FIELDS = ("sha", "date", "message")
EDIT_FIELDS = ("editedAt", "diff")
USER_CONTENT_EDITS_QUERY = (
    "query($owner: String!, $name: String!, $n: Int!) {"
    " repository(owner: $owner, name: $name) {"
    " issue(number: $n) { lastEditedAt userContentEdits(first: 100) { nodes { "
    + " ".join(EDIT_FIELDS)
    + " } } } } }"
)


class LiveEvidenceError(RuntimeError):
    """The pdf-info metadata is missing or a gh call failed."""


@dataclass(frozen=True)
class EvidenceFile:
    label: str
    path: Path
    count: int


@dataclass(frozen=True)
class LiveEvidenceResult:
    assignment: str
    team_dir: str
    repo: str | None
    sha: str | None
    work_dir: Path
    files: tuple[EvidenceFile, ...]
    summary_lines: tuple[str, ...]
    skipped: bool = False


def labels_command(repo: str) -> list[str]:
    return ["label", "list", "--repo", repo, "--limit", str(LABEL_LIMIT), "--json", ",".join(LABEL_FIELDS)]


def issues_command(repo: str) -> list[str]:
    return [
        "issue",
        "list",
        "--repo",
        repo,
        "--state",
        "all",
        "--limit",
        str(ISSUE_LIMIT),
        "--json",
        ",".join(ISSUE_FIELDS),
    ]


def prs_command(repo: str) -> list[str]:
    return [
        "pr",
        "list",
        "--repo",
        repo,
        "--state",
        "all",
        "--limit",
        str(PR_LIMIT),
        "--json",
        ",".join(PR_FIELDS),
    ]


def runs_main_command(repo: str) -> list[str]:
    return [
        "run",
        "list",
        "--repo",
        repo,
        "--branch",
        "main",
        "--limit",
        str(RUN_LIMIT),
        "--json",
        ",".join(RUN_FIELDS),
    ]


def runs_sha_command(repo: str, sha: str) -> list[str]:
    return ["api", f"repos/{repo}/actions/runs?head_sha={sha}", "--paginate"]


def commits_command(repo: str, sha: str) -> list[str]:
    return ["api", f"repos/{repo}/commits?sha={sha}&per_page=100", "--paginate"]


def comments_command(repo: str, number: int) -> list[str]:
    return ["api", f"repos/{repo}/issues/{number}/comments", "--paginate"]


def timeline_command(repo: str, number: int) -> list[str]:
    return ["api", f"repos/{repo}/issues/{number}/timeline", "--paginate"]


def edits_command(repo: str, number: int) -> list[str]:
    owner, name = repo.split("/", 1)
    return [
        "api",
        "graphql",
        "-F",
        f"owner={owner}",
        "-F",
        f"name={name}",
        "-F",
        f"n={number}",
        "-f",
        f"query={USER_CONTENT_EDITS_QUERY}",
    ]


def path_commits_command(repo: str, sha: str, path: str) -> list[str]:
    encoded = quote(path, safe="/")
    return ["api", f"repos/{repo}/commits?sha={sha}&path={encoded}&per_page=100", "--paginate"]


def parse_json_stream(text: str) -> list[object]:
    decoder = json.JSONDecoder()
    values: list[object] = []
    index = 0
    length = len(text)
    while index < length:
        while index < length and text[index].isspace():
            index += 1
        if index >= length:
            break
        try:
            value, index = decoder.raw_decode(text, index)
        except json.JSONDecodeError as exc:
            raise LiveEvidenceError(f"gh returned invalid JSON: {exc}") from exc
        values.append(value)
    if not values:
        raise LiveEvidenceError("gh returned no JSON")
    return values


def merge_list_pages(text: str) -> list[object]:
    merged: list[object] = []
    for page in parse_json_stream(text):
        if not isinstance(page, list):
            raise LiveEvidenceError("expected a JSON array from gh")
        merged.extend(page)
    return merged


def merge_run_pages(text: str) -> list[object]:
    runs: list[object] = []
    for page in parse_json_stream(text):
        if not isinstance(page, dict):
            raise LiveEvidenceError("expected a JSON object from gh")
        workflow_runs = page.get("workflow_runs")
        if not isinstance(workflow_runs, list):
            raise LiveEvidenceError("gh response has no workflow_runs list")
        runs.extend(workflow_runs)
    return runs


def project_runs(text: str) -> list[object]:
    projected: list[object] = []
    for run in merge_run_pages(text):
        if not isinstance(run, dict):
            raise LiveEvidenceError("a workflow run is not a JSON object")
        projected.append({field: run.get(field) for field in RUN_SHA_FIELDS})
    return projected


def project_issue_edits(text: str) -> dict[str, object]:
    values = parse_json_stream(text)
    if len(values) != 1 or not isinstance(values[0], dict):
        raise LiveEvidenceError("gh api graphql returned no JSON object")
    payload = values[0]
    data = payload.get("data")
    repository = data.get("repository") if isinstance(data, dict) else None
    issue = repository.get("issue") if isinstance(repository, dict) else None
    if not isinstance(issue, dict):
        errors = payload.get("errors")
        detail = ""
        if isinstance(errors, list) and errors:
            detail = ": " + "; ".join(
                str(error.get("message", error)) if isinstance(error, dict) else str(error) for error in errors
            )
        raise LiveEvidenceError(f"gh api graphql returned no issue{detail}")
    return issue


def project_path_commits(text: str) -> list[object]:
    projected: list[object] = []
    for commit in merge_list_pages(text):
        if not isinstance(commit, dict):
            raise LiveEvidenceError("a commit is not a JSON object")
        info = commit.get("commit")
        info = info if isinstance(info, dict) else {}
        committer = info.get("committer")
        committer = committer if isinstance(committer, dict) else {}
        message = info.get("message")
        first_line = str(message).splitlines()[0] if message else ""
        projected.append({"sha": commit.get("sha"), "date": committer.get("date"), "message": first_line})
    return projected


def normalize_repo_path(path: str) -> str:
    candidate = Path(path.strip())
    if not path.strip() or candidate.is_absolute() or any(part in ("", "..") for part in candidate.parts):
        raise LiveEvidenceError(f"invalid repository path: {path!r}")
    return candidate.as_posix()


def load_pdf_info(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise LiveEvidenceError(
            f"missing {path}; run scripts/fetch_team_snapshot.py <assignment> <team_dir> first"
        )
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LiveEvidenceError(f"cannot parse {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise LiveEvidenceError(f"{path} does not hold a JSON object")
    return payload


def snapshot_target(payload: dict[str, object]) -> tuple[str, str] | None:
    """Return the repository and SHA, or ``None`` when the snapshot is unresolved."""
    repo = payload.get("repo")
    sha = payload.get("sha")
    if isinstance(repo, str) and repo and isinstance(sha, str) and sha:
        return repo, sha
    return None


def stop_summary(assignment: str, team_dir: str, info_path: Path, root: Path) -> tuple[str, ...]:
    """The judged outcome for a submission with no resolvable snapshot."""
    return (
        f"{assignment} / {team_dir}",
        f"  {_display(info_path, root)} has no repository and SHA; "
        "repository-dependent checks are stopped per docs/grader-policy.md#submission-and-snapshot-rules",
        "  result: skipped (no snapshot)",
        "  hint: pair the PDF's SHA by hand with scripts/fetch_team_snapshot.py <assignment> <team_dir> --repo org/repo",
    )


def write_json_dump(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    os.chmod(temporary, 0o600)
    temporary.replace(path)


def collect_github_evidence(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
    *,
    issues: Sequence[int] = (),
    paths: Sequence[str] = (),
    runner: Callable[[list[str]], CommandResult] = run_gh,
) -> LiveEvidenceResult:
    if assignment not in ASSIGNMENT_CONFIG:
        raise LiveEvidenceError(f"unknown assignment: {assignment}")
    issue_numbers = _unique_issue_numbers(issues)
    repo_paths = list(dict.fromkeys(normalize_repo_path(path) for path in paths))

    work_dir = root / FEEDBACK_ROOT / assignment / "work" / team_dir
    info_path = work_dir / PDF_INFO_FILENAME
    target = snapshot_target(load_pdf_info(info_path))
    if target is None:
        return LiveEvidenceResult(
            assignment=assignment,
            team_dir=team_dir,
            repo=None,
            sha=None,
            work_dir=work_dir,
            files=(),
            summary_lines=stop_summary(assignment, team_dir, info_path, root),
            skipped=True,
        )
    repo, sha = target

    files: list[EvidenceFile] = []
    summary = [f"{assignment} / {team_dir}", f"  repo: {repo} @ {sha}"]

    def record(label: str, path: Path, count: int) -> None:
        files.append(EvidenceFile(label=label, path=path, count=count))
        summary.append(f"  {label}: {count} -> {_display(path, root)}")

    collectors: tuple[tuple[str, str, list[str], Callable[[str], object]], ...] = (
        ("labels", "labels.json", labels_command(repo), merge_list_pages),
        ("issues", "issues.json", issues_command(repo), merge_list_pages),
        ("prs", "prs.json", prs_command(repo), merge_list_pages),
        ("runs (main)", "runs_main.json", runs_main_command(repo), merge_list_pages),
        ("runs (sha)", "runs_sha.json", runs_sha_command(repo, sha), project_runs),
        ("commits", "commits.json", commits_command(repo, sha), merge_list_pages),
    )
    for label, filename, command, shape in collectors:
        value = shape(_run_gh(command, runner))
        dump_path = work_dir / filename
        write_json_dump(dump_path, value)
        record(label, dump_path, _record_count(value))

    for number in issue_numbers:
        drilldowns: tuple[tuple[str, list[str], Callable[[str], object]], ...] = (
            ("comments", comments_command(repo, number), merge_list_pages),
            ("timeline", timeline_command(repo, number), merge_list_pages),
            ("edits", edits_command(repo, number), project_issue_edits),
        )
        for kind, command, shape in drilldowns:
            value = shape(_run_gh(command, runner))
            dump_path = work_dir / "issues" / f"{number}.{kind}.json"
            write_json_dump(dump_path, value)
            record(f"issue {number} {kind}", dump_path, _record_count(value))

    for repo_path in repo_paths:
        value = project_path_commits(_run_gh(path_commits_command(repo, sha, repo_path), runner))
        dump_path = work_dir / "paths" / f"{repo_path}.json"
        write_json_dump(dump_path, value)
        record(f"path {repo_path} commits", dump_path, len(value))

    return LiveEvidenceResult(
        assignment=assignment,
        team_dir=team_dir,
        repo=repo,
        sha=sha,
        work_dir=work_dir,
        files=tuple(files),
        summary_lines=tuple(summary),
    )


def _unique_issue_numbers(issues: Sequence[int]) -> list[int]:
    numbers: list[int] = []
    for number in issues:
        if number <= 0:
            raise LiveEvidenceError(f"invalid issue number: {number}")
        if number not in numbers:
            numbers.append(number)
    return numbers


def _run_gh(command: list[str], runner: Callable[[list[str]], CommandResult]) -> str:
    result = runner(command)
    if result.returncode != 0:
        detail = result.stderr.strip() or f"exit code {result.returncode}"
        raise LiveEvidenceError(f"{_command_label(command)} failed: {detail}")
    return result.stdout


def _command_label(command: list[str]) -> str:
    if command[0] == "api":
        return "gh api " + command[1] if len(command) > 1 else "gh api"
    return "gh " + " ".join(command[:2])


def _record_count(value: object) -> int:
    if isinstance(value, list):
        return len(value)
    if isinstance(value, dict):
        edits = value.get("userContentEdits")
        nodes = edits.get("nodes") if isinstance(edits, dict) else None
        return len(nodes) if isinstance(nodes, list) else 0
    return 0


def _display(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()

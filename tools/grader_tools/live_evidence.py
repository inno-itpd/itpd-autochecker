"""Collect the live GitHub evidence for one team into its team work directory.

The A2 grading prompt's procedure step 5 defines the gh calls, their field
lists, and the limit per call.  Those lists are constants here, so the
collector and the prompt cannot drift apart; ``tests/test_live_evidence.py``
checks them against ``A2/grading_prompt.md``.

The collector reads ``itpd-assignments-feedback/<assignment>/work/<team_dir>/pdf-info.json``
(written by ``scripts/fetch_team_snapshot.py``) for the repository and the
snapshot SHA, writes JSON dumps beside it, and returns a compact summary of
counts and paths. Raw dumps are only written to files, never printed.

It also writes ``summary.md``, a bounded digest of the process evidence:
issue counts, pull-request numbers, failing runs, tags, releases, and the
milestones with their due dates and open and closed issue counts.  The digest
is capped at ``SUMMARY_LINE_CAP`` lines, and each list is truncated visibly, so
a grader can read it before opening any dump.  ``regenerate_evidence_summary``
rebuilds it from the saved dumps without calling ``gh``.

The ``--issue-fields`` mode is a separate, one-call dump: it reads every issue
through one paginated REST list call, skips pull requests, and writes
``issue-fields.json`` with each issue's number, state, title, type, milestone,
assignees, and issue-field values.  It never rewrites the other dumps, and it
is not combined with ``--summary`` or the drill-down options.

Every mode that writes dumps also rebuilds ``evidence.sqlite`` from the saved
files through ``tools.grader_tools.evidence_sqlite``, so a grader can query the
same evidence with SQL; ``--summary`` rebuilds it without calling ``gh``.
"""

from __future__ import annotations

import json
import os
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT
from tools.grader_tools.evidence_sqlite import (
    EvidenceDatabaseError,
    write_evidence_database,
)
from tools.grader_tools.submission_pdf import (
    PDF_INFO_FILENAME,
    CommandResult,
    run_gh,
    week_mismatch_warning,
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
MILESTONE_FIELDS = ("title", "due_on", "open_issues", "closed_issues")
RELEASE_FIELDS = ("tag_name", "draft", "prerelease", "published_at")
TAG_FIELDS = ("name",)
EDIT_FIELDS = ("editedAt", "diff")
USER_CONTENT_EDITS_QUERY = (
    "query($owner: String!, $name: String!, $n: Int!) {"
    " repository(owner: $owner, name: $name) {"
    " issue(number: $n) { lastEditedAt userContentEdits(first: 100) { nodes { "
    + " ".join(EDIT_FIELDS)
    + " } } } } }"
)

SUMMARY_FILENAME = "summary.md"
SUMMARY_LINE_CAP = 60
ISSUE_FIELDS_FILENAME = "issue-fields.json"
SUMMARY_DUMP_FILES = (
    "issues.json",
    "prs.json",
    "runs_main.json",
    "runs_sha.json",
    "milestones.json",
    "releases.json",
    "tags.json",
)

# A failing run concludes with a failure-like outcome; queued, in-progress,
# neutral, skipped, and successful runs are not failing.
FAILING_RUN_CONCLUSIONS = frozenset({"failure", "cancelled", "timed_out"})
SUMMARY_MAX_TAGS = 12
SUMMARY_MAX_MILESTONES = 40
SUMMARY_MAX_FAILING_RUNS = 3


class LiveEvidenceError(RuntimeError):
    """An evidence input is missing or malformed, or a gh call failed."""


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
    summary_path: Path | None = None
    database_path: Path | None = None


def _write_database(work_dir: Path, summary: list[str], root: Path) -> Path:
    """Rebuild ``evidence.sqlite`` and record its one-line summary."""
    try:
        database = write_evidence_database(work_dir)
    except EvidenceDatabaseError as exc:
        raise LiveEvidenceError(str(exc)) from exc
    summary.append(database.summary_line(root))
    return database.path


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


def milestones_command(repo: str) -> list[str]:
    return ["api", f"repos/{repo}/milestones?state=all&per_page=100", "--paginate"]


def releases_command(repo: str) -> list[str]:
    return ["api", f"repos/{repo}/releases?per_page=100", "--paginate"]


def tags_command(repo: str) -> list[str]:
    return ["api", f"repos/{repo}/tags?per_page=100", "--paginate"]


def issue_fields_command(repo: str) -> list[str]:
    return ["api", f"repos/{repo}/issues?state=all&per_page=100", "--paginate"]


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


def project_list(text: str, fields: Sequence[str], kind: str) -> list[object]:
    """Keep only the requested fields, so a dump stays small."""
    projected: list[object] = []
    for item in merge_list_pages(text):
        if not isinstance(item, dict):
            raise LiveEvidenceError(f"a {kind} is not a JSON object")
        projected.append({field: item.get(field) for field in fields})
    return projected


def project_milestones(text: str) -> list[object]:
    return project_list(text, MILESTONE_FIELDS, "milestone")


def project_releases(text: str) -> list[object]:
    return project_list(text, RELEASE_FIELDS, "release")


def project_tags(text: str) -> list[object]:
    return project_list(text, TAG_FIELDS, "tag")


def _issue_logins(assignees: object) -> list[object]:
    """Return the assignee logins, with an absent or null array becoming ``[]``."""
    if not isinstance(assignees, list):
        return []
    return [user.get("login") for user in assignees if isinstance(user, dict) and user.get("login") is not None]


def _issue_field_value(value: Mapping[str, object]) -> object:
    """Read the human-readable option of a REST issue-field value."""
    single = value.get("single_select_option")
    if isinstance(single, Mapping) and single.get("name") is not None:
        return single.get("name")
    multiple = value.get("multi_select_options")
    if isinstance(multiple, list):
        names = [
            option.get("name")
            for option in multiple
            if isinstance(option, Mapping) and option.get("name") is not None
        ]
        if names:
            return names
    return value.get("value")


def _issue_field_values(values: object) -> list[dict[str, object]]:
    """Project ``issue_field_values``, with an absent or null array becoming ``[]``."""
    if not isinstance(values, list):
        return []
    projected: list[dict[str, object]] = []
    for value in values:
        if not isinstance(value, dict):
            continue
        projected.append(
            {
                "name": value.get("issue_field_name"),
                "data_type": value.get("data_type"),
                "value": _issue_field_value(value),
            }
        )
    return projected


def project_issue_fields(text: str) -> list[object]:
    """Project a paginated REST issue list into one row per issue, without pull requests."""
    projected: list[object] = []
    for item in merge_list_pages(text):
        if not isinstance(item, dict):
            raise LiveEvidenceError("an issue is not a JSON object")
        if "pull_request" in item:
            continue
        issue_type = item.get("type")
        issue_type = issue_type if isinstance(issue_type, dict) else {}
        milestone = item.get("milestone")
        milestone = milestone if isinstance(milestone, dict) else {}
        projected.append(
            {
                "number": item.get("number"),
                "state": item.get("state"),
                "title": item.get("title"),
                "type": issue_type.get("name"),
                "milestone": milestone.get("title"),
                "assignees": _issue_logins(item.get("assignees")),
                "field_values": _issue_field_values(item.get("issue_field_values")),
            }
        )
    return projected


def normalize_repo_path(path: str) -> str:
    candidate = Path(path.strip())
    if not path.strip() or candidate.is_absolute() or any(part in ("", "..") for part in candidate.parts):
        raise LiveEvidenceError(f"invalid repository path: {path!r}")
    return candidate.as_posix()


def load_pdf_info(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise LiveEvidenceError(
            f"missing {path}; run scripts/fetch_team_snapshot.py <assignment> \"<team_dir>\" first"
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


def _stored_int(payload: Mapping[str, object], key: str) -> int | None:
    value = payload.get(key)
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return None


def permalink_week_warning(payload: Mapping[str, object], assignment: str) -> str | None:
    """The ``warn:`` line when a saved ``pdf-info.json`` records a week mismatch."""
    if payload.get("permalink_week_mismatch") is not True:
        return None
    expected = _stored_int(payload, "expected_week")
    if expected is None:
        config_week = ASSIGNMENT_CONFIG.get(assignment, {}).get("week")
        expected = config_week if isinstance(config_week, int) else None
    path = payload.get("permalink_path")
    return week_mismatch_warning(
        assignment,
        _stored_int(payload, "permalink_week"),
        expected,
        path if isinstance(path, str) and path else None,
    )


def stop_summary(assignment: str, team_dir: str, info_path: Path, root: Path) -> tuple[str, ...]:
    """The judged outcome for a submission with no resolvable snapshot."""
    return (
        f"{assignment} / {team_dir}",
        f"  {_display(info_path, root)} has no repository and SHA; "
        "repository-dependent checks are stopped per docs/grader-policy.md#submission-and-snapshot-rules",
        "  result: skipped (no snapshot)",
        "  hint: pair the PDF's SHA by hand with scripts/fetch_team_snapshot.py <assignment> \"<team_dir>\" --repo org/repo",
    )


def build_evidence_digest(
    dumps: Mapping[str, object],
    *,
    assignment: str,
    team_dir: str,
    repo: str | None = None,
    sha: str | None = None,
    cap: int = SUMMARY_LINE_CAP,
    permalink_warning: str | None = None,
) -> str:
    """Render the bounded digest of the saved dumps, capped at ``cap`` lines."""
    lines = [f"# Evidence digest: {assignment} / {team_dir}"]
    if repo and sha:
        lines.append(f"- Repository: {repo} @ {sha}")
    if permalink_warning:
        lines.append(permalink_warning)
    lines.extend(
        [
            f"- Regenerate from the saved dumps: "
            f"`scripts/collect_github_evidence.py {assignment} \"<team_dir>\" --summary`.",
            f"- Cap: {cap} lines.",
            "- Failing run: `conclusion` is `failure`, `cancelled`, or `timed_out`.",
            "",
        ]
    )
    lines.extend(_issue_digest_lines(_dump_items(dumps, "issues.json")))
    lines.extend(_pull_request_digest_lines(_dump_items(dumps, "prs.json")))
    lines.extend(
        _failing_run_digest_lines(
            _dump_items(dumps, "runs_main.json"),
            heading="Runs (main)",
            name_field="workflowName",
            url_field="url",
            id_field="databaseId",
            event_field=None,
            source="runs_main.json",
        )
    )
    lines.extend(
        _failing_run_digest_lines(
            _dump_items(dumps, "runs_sha.json"),
            heading="Runs (snapshot SHA)",
            name_field="name",
            url_field="html_url",
            id_field=None,
            event_field="event",
            source="runs_sha.json",
        )
    )
    lines.extend(_tag_digest_lines(_dump_items(dumps, "tags.json")))
    lines.extend(_release_digest_lines(_dump_items(dumps, "releases.json")))
    lines.extend(_milestone_digest_lines(_dump_items(dumps, "milestones.json")))
    return _cap_digest_lines(lines, cap)


def _dump_items(dumps: Mapping[str, object], filename: str) -> list[dict[str, object]]:
    value = dumps.get(filename)
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _int_field(item: Mapping[str, object], field: str) -> int:
    value = item.get(field)
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _issue_digest_lines(issues: Sequence[dict[str, object]]) -> list[str]:
    if not issues:
        return ["- Issues: none."]
    open_count = sum(1 for issue in issues if str(issue.get("state") or "").lower() == "open")
    return [f"- Issues: {len(issues)} total, {open_count} open, {len(issues) - open_count} closed."]


def _pull_request_digest_lines(pull_requests: Sequence[dict[str, object]]) -> list[str]:
    if not pull_requests:
        return ["- Pull requests: none."]
    numbers = sorted({_int_field(pull_request, "number") for pull_request in pull_requests} - {0})
    if not numbers:
        return [f"- Pull requests: {len(pull_requests)} total."]
    if numbers[0] == numbers[-1]:
        return [f"- Pull requests: {len(pull_requests)} total, number #{numbers[0]}."]
    return [f"- Pull requests: {len(pull_requests)} total, numbers #{numbers[0]}-#{numbers[-1]}."]


def _failing_run_digest_lines(
    runs: Sequence[dict[str, object]],
    *,
    heading: str,
    name_field: str,
    url_field: str,
    id_field: str | None,
    event_field: str | None,
    source: str,
) -> list[str]:
    failing = [run for run in runs if str(run.get("conclusion") or "").lower() in FAILING_RUN_CONCLUSIONS]
    lines = [f"- {heading}: {len(failing)} failing of {len(runs)}."]
    failing.sort(
        key=lambda run: (
            str(run.get("createdAt") or ""),
            str(run.get(name_field) or ""),
            str(run.get(url_field) or ""),
        )
    )
    for run in failing[:SUMMARY_MAX_FAILING_RUNS]:
        name = str(run.get(name_field) or "unknown workflow")
        details: list[str] = []
        if id_field is not None and run.get(id_field) is not None:
            details.append(f"run {run.get(id_field)}")
        if event_field is not None and run.get(event_field):
            details.append(str(run.get(event_field)))
        details.append(str(run.get("conclusion") or "unknown"))
        suffix = f" — {run.get(url_field)}" if run.get(url_field) else ""
        lines.append(f"  - {name} ({', '.join(details)}){suffix}")
    hidden = len(failing) - SUMMARY_MAX_FAILING_RUNS
    if hidden > 0:
        lines.append(f"  - (+{hidden} more failing runs; see {source}.)")
    return lines


def _tag_digest_lines(tags: Sequence[dict[str, object]]) -> list[str]:
    names = sorted(str(tag.get("name")) for tag in tags if tag.get("name"))
    if not names:
        return ["- Tags: none."]
    shown = names[:SUMMARY_MAX_TAGS]
    hidden = len(names) - len(shown)
    suffix = f"; {hidden} more in tags.json" if hidden > 0 else ""
    return [f"- Tags ({len(names)}): {', '.join(shown)}{suffix}."]


def _release_digest_lines(releases: Sequence[dict[str, object]]) -> list[str]:
    if not releases:
        return ["- Releases: none."]
    published = [
        release
        for release in releases
        if release.get("published_at") and not release.get("draft") and not release.get("prerelease")
    ]
    if not published:
        return [f"- Releases: {len(releases)} total; none published."]
    latest = max(published, key=lambda release: str(release.get("published_at") or ""))
    tag = latest.get("tag_name") or "untagged"
    return [f"- Releases: {len(releases)} total; latest {tag} ({latest.get('published_at')})."]


def _milestone_digest_lines(milestones: Sequence[dict[str, object]]) -> list[str]:
    if not milestones:
        return ["- Milestones: none."]
    ordered = sorted(
        milestones,
        key=lambda milestone: (
            milestone.get("due_on") is None,
            str(milestone.get("due_on") or ""),
            str(milestone.get("title") or ""),
        ),
    )
    lines = [f"- Milestones: {len(ordered)}."]
    for milestone in ordered[:SUMMARY_MAX_MILESTONES]:
        title = str(milestone.get("title") or "untitled")
        due = _due_date_label(milestone.get("due_on"))
        due_text = f"due {due}" if due else "no due date"
        lines.append(
            f"  - {title}: {due_text}, "
            f"{_int_field(milestone, 'open_issues')} open, "
            f"{_int_field(milestone, 'closed_issues')} closed."
        )
    hidden = len(ordered) - SUMMARY_MAX_MILESTONES
    if hidden > 0:
        lines.append(f"  - (+{hidden} more milestones; see milestones.json.)")
    return lines


def _due_date_label(value: object) -> str | None:
    text = str(value) if value else ""
    return text.split("T", 1)[0] if text else None


def _cap_digest_lines(lines: list[str], cap: int) -> str:
    if cap < 1:
        raise LiveEvidenceError(f"invalid summary line cap: {cap}")
    if len(lines) > cap:
        footer = f"- Truncated at the {cap}-line cap; read a bounded projection of the JSON dumps for the rest."
        lines = [*lines[: cap - 1], footer]
    return "\n".join(lines) + "\n"


def _write_private_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    temporary.write_text(text, encoding="utf-8")
    os.chmod(temporary, 0o600)
    temporary.replace(path)


def write_json_dump(path: Path, payload: object) -> None:
    _write_private_text(path, json.dumps(payload, indent=2) + "\n")


def write_summary(work_dir: Path, digest: str) -> Path:
    path = work_dir / SUMMARY_FILENAME
    _write_private_text(path, digest)
    return path


def regenerate_evidence_summary(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
) -> tuple[Path, str]:
    """Rebuild ``summary.md`` from the saved dumps; never calls ``gh``."""
    if assignment not in ASSIGNMENT_CONFIG:
        raise LiveEvidenceError(f"unknown assignment: {assignment}")
    work_dir = root / FEEDBACK_ROOT / assignment / "work" / team_dir

    dumps: dict[str, object] = {}
    missing: list[str] = []
    for filename in SUMMARY_DUMP_FILES:
        path = work_dir / filename
        if not path.is_file():
            missing.append(filename)
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise LiveEvidenceError(f"cannot parse {path}: {exc}") from exc
        if not isinstance(payload, list):
            raise LiveEvidenceError(f"{path} does not hold a JSON array")
        dumps[filename] = payload
    if missing:
        raise LiveEvidenceError(
            f"missing {', '.join(missing)} in {work_dir}; run "
            f"scripts/collect_github_evidence.py {assignment} {team_dir} first"
        )

    repo, sha = _stored_snapshot_target(work_dir)
    warning = _stored_permalink_warning(work_dir, assignment)
    digest = build_evidence_digest(
        dumps,
        assignment=assignment,
        team_dir=team_dir,
        repo=repo,
        sha=sha,
        permalink_warning=warning,
    )
    return write_summary(work_dir, digest), digest


def _stored_pdf_info(work_dir: Path) -> dict[str, object] | None:
    try:
        payload = json.loads((work_dir / PDF_INFO_FILENAME).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _stored_snapshot_target(work_dir: Path) -> tuple[str | None, str | None]:
    payload = _stored_pdf_info(work_dir)
    if payload is None:
        return None, None
    target = snapshot_target(payload)
    return target if target is not None else (None, None)


def _stored_permalink_warning(work_dir: Path, assignment: str) -> str | None:
    payload = _stored_pdf_info(work_dir)
    if payload is None:
        return None
    return permalink_week_warning(payload, assignment)


def collect_github_evidence(
    assignment: str,
    team_dir: str,
    root: Path = Path("."),
    *,
    issues: Sequence[int] = (),
    paths: Sequence[str] = (),
    issue_fields: bool = False,
    runner: Callable[[list[str]], CommandResult] = run_gh,
) -> LiveEvidenceResult:
    if assignment not in ASSIGNMENT_CONFIG:
        raise LiveEvidenceError(f"unknown assignment: {assignment}")
    issue_numbers = _unique_issue_numbers(issues)
    repo_paths = list(dict.fromkeys(normalize_repo_path(path) for path in paths))
    if issue_fields and (issue_numbers or repo_paths):
        raise LiveEvidenceError("--issue-fields cannot be combined with --issues or --paths")

    work_dir = root / FEEDBACK_ROOT / assignment / "work" / team_dir
    info_path = work_dir / PDF_INFO_FILENAME
    pdf_info = load_pdf_info(info_path)
    target = snapshot_target(pdf_info)
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
    permalink_warning = permalink_week_warning(pdf_info, assignment)

    files: list[EvidenceFile] = []
    summary = [f"{assignment} / {team_dir}", f"  repo: {repo} @ {sha}"]

    def record(label: str, path: Path, count: int) -> None:
        files.append(EvidenceFile(label=label, path=path, count=count))
        summary.append(f"  {label}: {count} -> {_display(path, root)}")

    if issue_fields:
        value = project_issue_fields(_run_gh(issue_fields_command(repo), runner))
        dump_path = work_dir / ISSUE_FIELDS_FILENAME
        write_json_dump(dump_path, value)
        record("issue fields", dump_path, len(value))
        database_path = _write_database(work_dir, summary, root)
        return LiveEvidenceResult(
            assignment=assignment,
            team_dir=team_dir,
            repo=repo,
            sha=sha,
            work_dir=work_dir,
            files=tuple(files),
            summary_lines=tuple(summary),
            database_path=database_path,
        )

    collectors: tuple[tuple[str, str, list[str], Callable[[str], object]], ...] = (
        ("labels", "labels.json", labels_command(repo), merge_list_pages),
        ("issues", "issues.json", issues_command(repo), merge_list_pages),
        ("prs", "prs.json", prs_command(repo), merge_list_pages),
        ("runs (main)", "runs_main.json", runs_main_command(repo), merge_list_pages),
        ("runs (sha)", "runs_sha.json", runs_sha_command(repo, sha), project_runs),
        ("commits", "commits.json", commits_command(repo, sha), merge_list_pages),
        ("milestones", "milestones.json", milestones_command(repo), project_milestones),
        ("releases", "releases.json", releases_command(repo), project_releases),
        ("tags", "tags.json", tags_command(repo), project_tags),
    )
    dump_values: dict[str, object] = {}
    for label, filename, command, shape in collectors:
        value = shape(_run_gh(command, runner))
        dump_path = work_dir / filename
        write_json_dump(dump_path, value)
        dump_values[filename] = value
        record(label, dump_path, _record_count(value))

    digest = build_evidence_digest(
        dump_values,
        assignment=assignment,
        team_dir=team_dir,
        repo=repo,
        sha=sha,
        permalink_warning=permalink_warning,
    )
    digest_path = write_summary(work_dir, digest)
    summary.append(f"  summary: {len(digest.splitlines())} lines -> {_display(digest_path, root)}")
    database_path = _write_database(work_dir, summary, root)

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
        summary_path=digest_path,
        database_path=database_path,
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

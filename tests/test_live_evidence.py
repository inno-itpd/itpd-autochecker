from __future__ import annotations

import json
from pathlib import Path
import re
import sqlite3

import pytest

from scripts.collect_github_evidence import run as collect_run
from tools.grader_tools.evidence_sqlite import EVIDENCE_DB_FILENAME, SCHEMA_TABLES
from tools.grader_tools.live_evidence import (
    EDIT_FIELDS,
    ISSUE_FIELDS,
    ISSUE_FIELDS_FILENAME,
    ISSUE_LIMIT,
    LABEL_FIELDS,
    LABEL_LIMIT,
    MILESTONE_FIELDS,
    PATH_COMMIT_FIELDS,
    PR_FIELDS,
    PR_LIMIT,
    RELEASE_FIELDS,
    RUN_FIELDS,
    RUN_LIMIT,
    RUN_SHA_FIELDS,
    SUMMARY_FILENAME,
    SUMMARY_LINE_CAP,
    TAG_FIELDS,
    USER_CONTENT_EDITS_QUERY,
    LiveEvidenceError,
    LiveEvidenceResult,
    build_evidence_digest,
    collect_github_evidence,
)
from tools.grader_tools.live_evidence import (
    comments_command,
    commits_command,
    edits_command,
    issue_fields_command,
    issues_command,
    labels_command,
    milestones_command,
    path_commits_command,
    prs_command,
    releases_command,
    runs_main_command,
    runs_sha_command,
    tags_command,
    timeline_command,
)
from tools.grader_tools.submission_pdf import CommandResult

ROOT = Path(__file__).resolve().parents[1]
TEAM = "Team 1 - Absolute Cinema_10937_assignsubmission_file"
REPO = "example-org/example-repo"
SHA = "1234567890abcdef1234567890abcdef12345678"


class FakeGh:
    def __init__(self, responses: dict[tuple[str, ...], str]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, ...]] = []

    def __call__(self, args: list[str]) -> CommandResult:
        key = tuple(args)
        self.calls.append(key)
        if key not in self.responses:
            raise AssertionError(f"unexpected gh call: {key}")
        return CommandResult(returncode=0, stdout=self.responses[key], stderr="")


def write_pdf_info(tmp_path: Path, repo: object = REPO, sha: object = SHA) -> Path:
    scratch = tmp_path / "itpd-assignments-feedback" / "A2" / "work" / TEAM
    scratch.mkdir(parents=True)
    (scratch / "pdf-info.json").write_text(
        json.dumps({"assignment": "A2", "team_dir": TEAM, "repo": repo, "sha": sha}),
        encoding="utf-8",
    )
    return scratch


def base_responses() -> dict[tuple[str, ...], str]:
    return {
        tuple(labels_command(REPO)): json.dumps(
            [{"name": "task", "description": "", "ignored": "x"}],
        ),
        tuple(issues_command(REPO)): json.dumps([{"number": 50, "state": "OPEN", "title": "Edit the root README"}]),
        tuple(prs_command(REPO)): json.dumps([{"number": 51, "title": "Edit the root README"}]),
        tuple(runs_main_command(REPO)): json.dumps([{"databaseId": 1, "conclusion": "success"}]),
        tuple(runs_sha_command(REPO, SHA)): json.dumps(
            {
                "total_count": 1,
                "workflow_runs": [
                    {
                        "name": "Markdown check",
                        "event": "push",
                        "conclusion": "success",
                        "html_url": "https://example.com/run/1",
                        "ignored": "x",
                    }
                ],
            }
        ),
        tuple(commits_command(REPO, SHA)): json.dumps([{"sha": "a" * 40, "commit": {"message": "one"}}]),
        tuple(milestones_command(REPO)): json.dumps(
            [
                {
                    "title": "Sprint 1",
                    "due_on": "2026-10-01T00:00:00Z",
                    "open_issues": 2,
                    "closed_issues": 3,
                    "ignored": "x",
                }
            ]
        ),
        tuple(releases_command(REPO)): json.dumps(
            [
                {
                    "tag_name": "v1.0.0",
                    "draft": False,
                    "prerelease": False,
                    "published_at": "2026-10-05T12:00:00Z",
                    "ignored": "x",
                }
            ]
        ),
        tuple(tags_command(REPO)): json.dumps([{"name": "v1.0.0", "commit": {"sha": "a" * 40}, "ignored": "x"}]),
    }


def issue_fields_responses() -> dict[tuple[str, ...], str]:
    return {
        tuple(issue_fields_command(REPO)): json.dumps(
            [
                {
                    "number": 50,
                    "state": "open",
                    "title": "Ship the slice",
                    "type": {"name": "User story"},
                    "milestone": {"title": "SPRINT-03"},
                    "assignees": [{"login": "alice"}, {"login": "bob"}],
                    "issue_field_values": [
                        {
                            "data_type": "single_select",
                            "issue_field_id": 1,
                            "issue_field_name": "Responsible",
                            "single_select_option": {"name": "alice"},
                            "value": 101,
                        },
                        {
                            "data_type": "single_select",
                            "issue_field_id": 2,
                            "issue_field_name": "Accountable",
                            "single_select_option": {"name": "bob"},
                            "value": 102,
                        },
                    ],
                },
                {
                    "number": 51,
                    "state": "closed",
                    "title": "Null-safe task",
                    "type": None,
                    "milestone": None,
                    "assignees": None,
                    "issue_field_values": None,
                },
                {"number": 52, "state": "open", "title": "Absent keys"},
                {
                    "number": 53,
                    "state": "open",
                    "title": "A pull request",
                    "pull_request": {"url": "https://example.com/pull/53"},
                    "issue_field_values": [
                        {
                            "data_type": "single_select",
                            "issue_field_name": "Responsible",
                            "single_select_option": {"name": "alice"},
                        }
                    ],
                },
            ]
        )
    }


EXPECTED_ISSUE_FIELDS = [
    {
        "number": 50,
        "state": "open",
        "title": "Ship the slice",
        "type": "User story",
        "milestone": "SPRINT-03",
        "assignees": ["alice", "bob"],
        "field_values": [
            {"name": "Responsible", "data_type": "single_select", "value": "alice"},
            {"name": "Accountable", "data_type": "single_select", "value": "bob"},
        ],
    },
    {
        "number": 51,
        "state": "closed",
        "title": "Null-safe task",
        "type": None,
        "milestone": None,
        "assignees": [],
        "field_values": [],
    },
    {
        "number": 52,
        "state": "open",
        "title": "Absent keys",
        "type": None,
        "milestone": None,
        "assignees": [],
        "field_values": [],
    },
]


def test_collect_writes_the_base_dumps_and_a_compact_summary(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(base_responses()))

    assert json.loads((scratch / "labels.json").read_text(encoding="utf-8")) == [
        {"name": "task", "description": "", "ignored": "x"}
    ]
    assert json.loads((scratch / "issues.json").read_text(encoding="utf-8")) == [
        {"number": 50, "state": "OPEN", "title": "Edit the root README"}
    ]
    assert json.loads((scratch / "prs.json").read_text(encoding="utf-8")) == [
        {"number": 51, "title": "Edit the root README"}
    ]
    assert json.loads((scratch / "runs_main.json").read_text(encoding="utf-8")) == [
        {"databaseId": 1, "conclusion": "success"}
    ]
    assert json.loads((scratch / "commits.json").read_text(encoding="utf-8")) == [
        {"sha": "a" * 40, "commit": {"message": "one"}}
    ]
    assert (scratch / "labels.json").stat().st_mode & 0o777 == 0o600

    runs_sha = json.loads((scratch / "runs_sha.json").read_text(encoding="utf-8"))
    assert runs_sha == [
        {
            "name": "Markdown check",
            "event": "push",
            "conclusion": "success",
            "html_url": "https://example.com/run/1",
        }
    ]
    assert list(runs_sha[0]) == list(RUN_SHA_FIELDS)

    milestones = json.loads((scratch / "milestones.json").read_text(encoding="utf-8"))
    assert milestones == [
        {"title": "Sprint 1", "due_on": "2026-10-01T00:00:00Z", "open_issues": 2, "closed_issues": 3}
    ]
    assert list(milestones[0]) == list(MILESTONE_FIELDS)
    releases = json.loads((scratch / "releases.json").read_text(encoding="utf-8"))
    assert releases == [
        {"tag_name": "v1.0.0", "draft": False, "prerelease": False, "published_at": "2026-10-05T12:00:00Z"}
    ]
    assert list(releases[0]) == list(RELEASE_FIELDS)
    tags = json.loads((scratch / "tags.json").read_text(encoding="utf-8"))
    assert tags == [{"name": "v1.0.0"}]
    assert list(tags[0]) == list(TAG_FIELDS)

    assert [file.label for file in result.files] == [
        "labels",
        "issues",
        "prs",
        "runs (main)",
        "runs (sha)",
        "commits",
        "milestones",
        "releases",
        "tags",
    ]
    assert [file.count for file in result.files] == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    summary = "\n".join(result.summary_lines)
    assert "itpd-assignments-feedback/A2/work/" in summary
    assert "labels: 1 -> itpd-assignments-feedback/A2/work/" in summary
    assert f"repo: {REPO} @ {SHA}" in summary
    assert '{"name"' not in summary
    assert '"workflow_runs"' not in summary

    digest_path = scratch / SUMMARY_FILENAME
    assert result.summary_path == digest_path
    assert digest_path.stat().st_mode & 0o777 == 0o600
    digest = digest_path.read_text(encoding="utf-8")
    assert digest.count("\n") <= SUMMARY_LINE_CAP
    assert f"summary: {len(digest.splitlines())} lines -> itpd-assignments-feedback/A2/work/" in summary
    assert "# Evidence digest: A2 / " + TEAM in digest
    assert f"- Repository: {REPO} @ {SHA}" in digest
    assert "- Issues: 1 total, 1 open, 0 closed." in digest
    assert "- Pull requests: 1 total, number #51." in digest
    assert "- Runs (main): 0 failing of 1." in digest
    assert "- Runs (snapshot SHA): 0 failing of 1." in digest
    assert "- Tags (1): v1.0.0." in digest
    assert "- Releases: 1 total; latest v1.0.0 (2026-10-05T12:00:00Z)." in digest
    assert "- Milestones: 1." in digest
    assert "  - Sprint 1: due 2026-10-01, 2 open, 3 closed." in digest


def test_collect_writes_the_sqlite_projection(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(base_responses()))

    database = scratch / EVIDENCE_DB_FILENAME
    assert result.database_path == database
    assert database.is_file()
    assert database.stat().st_mode & 0o777 == 0o600
    summary = "\n".join(result.summary_lines)
    assert (
        f"  evidence.sqlite: {len(SCHEMA_TABLES)} tables, 1 issue, 1 pull request -> "
        f"itpd-assignments-feedback/A2/work/{TEAM}/{EVIDENCE_DB_FILENAME}"
    ) in summary
    with sqlite3.connect(database) as connection:
        rows = connection.execute(
            "SELECT number, state, title, type, milestone, assignees, closing_pull_requests "
            "FROM issue_projection ORDER BY number"
        ).fetchall()
    assert rows == [(50, "open", "Edit the root README", None, None, "", "")]


def test_collect_uses_the_encoded_field_lists(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    runner = FakeGh(base_responses())
    collect_github_evidence("A2", TEAM, tmp_path, runner=runner)

    json_fields = {call[call.index("--json") + 1] for call in runner.calls if "--json" in call}
    assert json_fields == {
        ",".join(LABEL_FIELDS),
        ",".join(ISSUE_FIELDS),
        ",".join(PR_FIELDS),
        ",".join(RUN_FIELDS),
    }
    limits = {call[call.index("--limit") + 1] for call in runner.calls if "--limit" in call}
    assert limits == {str(LABEL_LIMIT), str(ISSUE_LIMIT), str(PR_LIMIT), str(RUN_LIMIT)}


def test_collect_merges_paginated_commit_pages(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(commits_command(REPO, SHA))] = json.dumps([{"sha": "1" * 40}]) + "\n" + json.dumps(
        [{"sha": "2" * 40}, {"sha": "3" * 40}]
    )
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))

    commits = json.loads((scratch / "commits.json").read_text(encoding="utf-8"))
    assert [commit["sha"] for commit in commits] == ["1" * 40, "2" * 40, "3" * 40]
    assert next(file for file in result.files if file.label == "commits").count == 3


def test_collect_merges_paginated_run_pages(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(runs_sha_command(REPO, SHA))] = json.dumps(
        {"total_count": 2, "workflow_runs": [{"name": "Markdown check", "conclusion": "success"}]}
    ) + json.dumps({"total_count": 2, "workflow_runs": [{"name": "Link check", "conclusion": "failure"}]})
    collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))

    runs = json.loads((scratch / "runs_sha.json").read_text(encoding="utf-8"))
    assert [run["name"] for run in runs] == ["Markdown check", "Link check"]


def test_collect_issue_drilldowns(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(comments_command(REPO, 11))] = json.dumps([{"body": "first"}]) + json.dumps([{"body": "second"}])
    responses[tuple(timeline_command(REPO, 11))] = json.dumps([{"event": "labeled", "label": {"name": "task"}}])
    responses[tuple(edits_command(REPO, 11))] = json.dumps(
        {
            "data": {
                "repository": {
                    "issue": {
                        "lastEditedAt": "2026-10-10T20:00:00Z",
                        "userContentEdits": {"nodes": [{"editedAt": "2026-10-10T20:00:00Z", "diff": "-a\n+b"}]},
                    }
                }
            }
        }
    )
    result = collect_github_evidence("A2", TEAM, tmp_path, issues=[11, 11], runner=FakeGh(responses))

    assert json.loads((scratch / "issues" / "11.comments.json").read_text(encoding="utf-8")) == [
        {"body": "first"},
        {"body": "second"},
    ]
    assert json.loads((scratch / "issues" / "11.timeline.json").read_text(encoding="utf-8")) == [
        {"event": "labeled", "label": {"name": "task"}}
    ]
    assert json.loads((scratch / "issues" / "11.edits.json").read_text(encoding="utf-8")) == {
        "lastEditedAt": "2026-10-10T20:00:00Z",
        "userContentEdits": {"nodes": [{"editedAt": "2026-10-10T20:00:00Z", "diff": "-a\n+b"}]},
    }
    assert [file.label for file in result.files] == [
        "labels",
        "issues",
        "prs",
        "runs (main)",
        "runs (sha)",
        "commits",
        "milestones",
        "releases",
        "tags",
        "issue 11 comments",
        "issue 11 timeline",
        "issue 11 edits",
    ]
    assert [file.count for file in result.files[-3:]] == [2, 1, 1]
    assert "issue 11 comments: 2 -> itpd-assignments-feedback/A2/work/" in "\n".join(result.summary_lines)


def test_collect_issue_edits_reports_graphql_errors(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(comments_command(REPO, 11))] = json.dumps([])
    responses[tuple(timeline_command(REPO, 11))] = json.dumps([])
    responses[tuple(edits_command(REPO, 11))] = json.dumps(
        {"data": None, "errors": [{"message": "Could not resolve to an issue"}]}
    )
    with pytest.raises(LiveEvidenceError, match="Could not resolve to an issue"):
        collect_github_evidence("A2", TEAM, tmp_path, issues=[11], runner=FakeGh(responses))


def test_collect_path_history_projects_sha_date_and_subject(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(path_commits_command(REPO, SHA, "reports/week-02/README.md"))] = json.dumps(
        [
            {
                "sha": "b" * 40,
                "commit": {
                    "committer": {"date": "2026-10-09T10:00:00Z"},
                    "message": "Write the week report\n\nDetails in the body.",
                },
            }
        ]
    )
    result = collect_github_evidence(
        "A2", TEAM, tmp_path, paths=["reports/week-02/README.md"], runner=FakeGh(responses)
    )

    payload = json.loads(
        (scratch / "paths" / "reports" / "week-02" / "README.md.json").read_text(encoding="utf-8")
    )
    assert payload == [{"sha": "b" * 40, "date": "2026-10-09T10:00:00Z", "message": "Write the week report"}]
    assert list(payload[0]) == list(PATH_COMMIT_FIELDS)
    assert result.files[-1].label == "path reports/week-02/README.md commits"
    assert result.files[-1].count == 1


def test_collect_rejects_path_traversal(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="invalid repository path"):
        collect_github_evidence("A2", TEAM, tmp_path, paths=["../outside.md"], runner=FakeGh(base_responses()))


def test_collect_rejects_non_positive_issue_numbers(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="invalid issue number"):
        collect_github_evidence("A2", TEAM, tmp_path, issues=[0], runner=FakeGh(base_responses()))


def test_collect_requires_the_scratch_metadata(tmp_path: Path) -> None:
    with pytest.raises(LiveEvidenceError, match="fetch_team_snapshot"):
        collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh({}))


def test_collect_stops_without_a_snapshot_repo(tmp_path: Path) -> None:
    write_pdf_info(tmp_path, repo=None, sha=None)
    result = collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh({}))

    assert result.skipped is True
    assert result.files == ()
    assert result.repo is None
    assert result.sha is None
    summary = "\n".join(result.summary_lines)
    assert "pdf-info.json has no repository and SHA" in summary
    assert "result: skipped (no snapshot)" in summary
    assert "--repo org/repo" in summary


def test_issue_fields_projects_the_expected_rows(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    runner = FakeGh(issue_fields_responses())
    result = collect_github_evidence("A2", TEAM, tmp_path, issue_fields=True, runner=runner)

    assert runner.calls == [tuple(issue_fields_command(REPO))]
    path = scratch / ISSUE_FIELDS_FILENAME
    assert json.loads(path.read_text(encoding="utf-8")) == EXPECTED_ISSUE_FIELDS
    assert list(EXPECTED_ISSUE_FIELDS[0]) == [
        "number",
        "state",
        "title",
        "type",
        "milestone",
        "assignees",
        "field_values",
    ]
    assert list(EXPECTED_ISSUE_FIELDS[0]["field_values"][0]) == ["name", "data_type", "value"]
    assert path.stat().st_mode & 0o777 == 0o600
    assert [file.label for file in result.files] == ["issue fields"]
    assert [file.count for file in result.files] == [3]
    assert result.summary_path is None
    summary = "\n".join(result.summary_lines)
    assert f"issue fields: 3 -> itpd-assignments-feedback/A2/work/{TEAM}/{ISSUE_FIELDS_FILENAME}" in summary
    assert '{"number"' not in summary


def test_issue_fields_is_null_safe_for_missing_arrays_and_objects(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    collect_github_evidence("A2", TEAM, tmp_path, issue_fields=True, runner=FakeGh(issue_fields_responses()))

    rows = json.loads((scratch / ISSUE_FIELDS_FILENAME).read_text(encoding="utf-8"))
    for number in (51, 52):
        row = next(item for item in rows if item["number"] == number)
        assert row["type"] is None
        assert row["milestone"] is None
        assert row["assignees"] == []
        assert row["field_values"] == []


def test_issue_fields_skips_pull_requests(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    collect_github_evidence("A2", TEAM, tmp_path, issue_fields=True, runner=FakeGh(issue_fields_responses()))

    rows = json.loads((scratch / ISSUE_FIELDS_FILENAME).read_text(encoding="utf-8"))
    assert [row["number"] for row in rows] == [50, 51, 52]


def test_issue_fields_leaves_the_existing_dumps_unchanged(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(base_responses()))
    before = {
        path.name: path.read_bytes()
        for path in scratch.iterdir()
        if path.is_file() and path.name != EVIDENCE_DB_FILENAME
    }

    collect_github_evidence("A2", TEAM, tmp_path, issue_fields=True, runner=FakeGh(issue_fields_responses()))

    after = {
        path.name: path.read_bytes()
        for path in scratch.iterdir()
        if path.is_file() and path.name != EVIDENCE_DB_FILENAME
    }
    assert set(after) == set(before) | {ISSUE_FIELDS_FILENAME}
    for name, content in before.items():
        assert after[name] == content


def test_issue_fields_cli_writes_the_dump_and_prints_its_path(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = issue_fields_responses()

    def fake_collect(assignment: str, team_dir: str, *, root: Path, **kwargs: object) -> LiveEvidenceResult:
        return collect_github_evidence(assignment, team_dir, root, runner=FakeGh(responses), **kwargs)

    lines: list[str] = []
    status = collect_run(
        ["A2", TEAM, "--issue-fields"], root=tmp_path, out=lines.append, collect=fake_collect
    )

    assert status == 0
    assert (scratch / ISSUE_FIELDS_FILENAME).is_file()
    assert lines == [
        f"A2 / {TEAM}",
        f"  repo: {REPO} @ {SHA}",
        f"  issue fields: 3 -> itpd-assignments-feedback/A2/work/{TEAM}/{ISSUE_FIELDS_FILENAME}",
        f"  evidence.sqlite: {len(SCHEMA_TABLES)} tables, 3 issues, 0 pull requests -> "
        f"itpd-assignments-feedback/A2/work/{TEAM}/{EVIDENCE_DB_FILENAME}",
    ]


def test_issue_fields_rejects_summary_and_drilldowns(tmp_path: Path) -> None:
    with pytest.raises(SystemExit):
        collect_run(["A2", TEAM, "--issue-fields", "--summary"], root=tmp_path, out=lambda _: None)

    lines: list[str] = []
    status = collect_run(["A2", TEAM, "--issue-fields", "--issues", "12"], root=tmp_path, out=lines.append)

    assert status == 2
    assert lines == ["ERROR: --issue-fields cannot be combined with --issues or --paths"]


def test_collect_cli_exits_zero_on_a_skipped_snapshot() -> None:
    skipped = LiveEvidenceResult(
        assignment="A2",
        team_dir=TEAM,
        repo=None,
        sha=None,
        work_dir=Path("work"),
        files=(),
        summary_lines=("result: skipped (no snapshot)",),
        skipped=True,
    )
    lines: list[str] = []
    status = collect_run(["A2", TEAM], out=lines.append, collect=lambda *args, **kwargs: skipped)

    assert status == 0
    assert lines == ["result: skipped (no snapshot)"]


def test_collect_rejects_unknown_assignment(tmp_path: Path) -> None:
    with pytest.raises(LiveEvidenceError, match="unknown assignment"):
        collect_github_evidence("A9", TEAM, tmp_path, runner=FakeGh({}))


def test_collect_raises_on_gh_failures_and_invalid_json(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    responses = base_responses()
    responses[tuple(labels_command(REPO))] = "not json"
    with pytest.raises(LiveEvidenceError, match="invalid JSON"):
        collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(responses))
    assert not (scratch / "labels.json").exists()


def test_collect_reports_gh_exit_codes(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)
    with pytest.raises(LiveEvidenceError, match="gh label list failed: HTTP 403"):
        collect_github_evidence(
            "A2",
            TEAM,
            tmp_path,
            runner=lambda command: CommandResult(returncode=1, stdout="", stderr="HTTP 403"),
        )


def test_digest_lists_counts_failing_runs_tags_and_milestones() -> None:
    dumps = {
        "issues.json": [
            {"number": 1, "state": "OPEN"},
            {"number": 2, "state": "CLOSED"},
            {"number": 3, "state": "OPEN"},
        ],
        "prs.json": [{"number": 30}, {"number": 12}, {"number": 21}],
        "runs_main.json": [
            {
                "databaseId": 1,
                "workflowName": "Markdown check",
                "conclusion": "success",
                "createdAt": "2026-10-10T09:00:00Z",
                "url": "https://example.com/run/1",
            },
            {
                "databaseId": 2,
                "workflowName": "Link check",
                "conclusion": "failure",
                "createdAt": "2026-10-10T10:00:00Z",
                "url": "https://example.com/run/2",
            },
            {
                "databaseId": 3,
                "workflowName": "Tests",
                "conclusion": "cancelled",
                "createdAt": "2026-10-10T11:00:00Z",
                "url": "https://example.com/run/3",
            },
            {
                "databaseId": 4,
                "workflowName": "Build",
                "conclusion": "timed_out",
                "createdAt": "2026-10-10T12:00:00Z",
                "url": "https://example.com/run/4",
            },
            {
                "databaseId": 5,
                "workflowName": "Deploy",
                "conclusion": "skipped",
                "createdAt": "2026-10-10T13:00:00Z",
                "url": "https://example.com/run/5",
            },
        ],
        "runs_sha.json": [
            {
                "name": "Markdown check",
                "event": "push",
                "conclusion": "failure",
                "html_url": "https://example.com/run/9",
            },
            {
                "name": "Markdown check",
                "event": "push",
                "conclusion": "success",
                "html_url": "https://example.com/run/10",
            },
        ],
        "milestones.json": [
            {"title": "Sprint 2", "due_on": "2026-10-15T00:00:00Z", "open_issues": 5, "closed_issues": 1},
            {"title": "Sprint 1", "due_on": "2026-10-01T00:00:00Z", "open_issues": 0, "closed_issues": 7},
            {"title": "Unscheduled", "due_on": None, "open_issues": 1, "closed_issues": 0},
        ],
        "releases.json": [
            {
                "tag_name": "v1.0.0",
                "draft": False,
                "prerelease": False,
                "published_at": "2026-10-05T12:00:00Z",
            },
            {"tag_name": "v1.1.0", "draft": False, "prerelease": False, "published_at": None},
        ],
        "tags.json": [{"name": "v1.1.0"}, {"name": "v1.0.0"}],
    }
    digest = build_evidence_digest(dumps, assignment="A3", team_dir="Team 1", repo=REPO, sha=SHA)

    assert "# Evidence digest: A3 / Team 1" in digest
    assert f"- Repository: {REPO} @ {SHA}" in digest
    assert f"- Cap: {SUMMARY_LINE_CAP} lines." in digest
    assert "- Issues: 3 total, 2 open, 1 closed." in digest
    assert "- Pull requests: 3 total, numbers #12-#30." in digest
    assert "- Runs (main): 3 failing of 5." in digest
    assert "  - Link check (run 2, failure) — https://example.com/run/2" in digest
    assert "  - Tests (run 3, cancelled) — https://example.com/run/3" in digest
    assert "  - Build (run 4, timed_out) — https://example.com/run/4" in digest
    assert "Deploy" not in digest
    assert "- Runs (snapshot SHA): 1 failing of 2." in digest
    assert "  - Markdown check (push, failure) — https://example.com/run/9" in digest
    assert "- Tags (2): v1.0.0, v1.1.0." in digest
    assert "- Releases: 2 total; latest v1.0.0 (2026-10-05T12:00:00Z)." in digest
    assert "- Milestones: 3." in digest
    assert "  - Sprint 1: due 2026-10-01, 0 open, 7 closed." in digest
    assert "  - Sprint 2: due 2026-10-15, 5 open, 1 closed." in digest
    assert "  - Unscheduled: no due date, 1 open, 0 closed." in digest
    assert digest.index("Sprint 1") < digest.index("Sprint 2") < digest.index("Unscheduled")
    assert len(digest.splitlines()) <= SUMMARY_LINE_CAP


def test_digest_caps_lines_and_makes_truncation_visible() -> None:
    failing = [
        {
            "databaseId": number,
            "workflowName": f"Workflow {number}",
            "conclusion": "failure",
            "createdAt": f"2026-10-{number + 1:02d}T00:00:00Z",
            "url": f"https://example.com/run/{number}",
        }
        for number in range(10)
    ]
    dumps = {
        "issues.json": [{"number": number, "state": "OPEN"} for number in range(1, 101)],
        "prs.json": [{"number": number} for number in range(1, 51)],
        "runs_main.json": failing,
        "runs_sha.json": [
            {**run, "name": run["workflowName"], "html_url": run["url"], "event": "push"} for run in failing
        ],
        "milestones.json": [
            {
                "title": f"Sprint {number}",
                "due_on": f"2026-{number % 12 + 1:02d}-01T00:00:00Z",
                "open_issues": number,
                "closed_issues": number,
            }
            for number in range(100)
        ],
        "releases.json": [],
        "tags.json": [{"name": f"v0.{number}.0"} for number in range(40)],
    }
    digest = build_evidence_digest(dumps, assignment="A3", team_dir="Team 1")

    lines = digest.splitlines()
    assert len(lines) == SUMMARY_LINE_CAP
    assert lines[-1] == (
        f"- Truncated at the {SUMMARY_LINE_CAP}-line cap; "
        "read a bounded projection of the JSON dumps for the rest."
    )
    assert "- Tags (40): " in digest
    assert "; 28 more in tags.json." in digest
    assert "- Issues: 100 total, 100 open, 0 closed." in digest

    milestone_only = build_evidence_digest(
        {**dumps, "runs_main.json": [], "runs_sha.json": [], "tags.json": []},
        assignment="A3",
        team_dir="Team 1",
    )
    assert "  - (+60 more milestones; see milestones.json.)" in milestone_only
    assert len(milestone_only.splitlines()) <= SUMMARY_LINE_CAP


def test_summary_cli_regenerates_from_the_saved_dumps_without_gh(tmp_path: Path) -> None:
    scratch = write_pdf_info(tmp_path)
    collect_github_evidence("A2", TEAM, tmp_path, runner=FakeGh(base_responses()))
    expected = (scratch / SUMMARY_FILENAME).read_text(encoding="utf-8")
    (scratch / SUMMARY_FILENAME).unlink()
    (scratch / EVIDENCE_DB_FILENAME).unlink()

    def forbidden_collect(*args: object, **kwargs: object) -> LiveEvidenceResult:
        raise AssertionError("--summary must reuse the saved dumps instead of calling gh")

    lines: list[str] = []
    status = collect_run(["A2", TEAM, "--summary"], root=tmp_path, out=lines.append, collect=forbidden_collect)

    assert status == 0
    assert lines == expected.splitlines() + [
        f"  evidence.sqlite: {len(SCHEMA_TABLES)} tables, 1 issue, 1 pull request -> "
        f"itpd-assignments-feedback/A2/work/{TEAM}/{EVIDENCE_DB_FILENAME}"
    ]
    assert (scratch / SUMMARY_FILENAME).read_text(encoding="utf-8") == expected
    assert (scratch / SUMMARY_FILENAME).stat().st_mode & 0o777 == 0o600
    assert (scratch / EVIDENCE_DB_FILENAME).is_file()
    assert (scratch / EVIDENCE_DB_FILENAME).stat().st_mode & 0o777 == 0o600


def test_summary_cli_fails_cleanly_when_the_dumps_are_missing(tmp_path: Path) -> None:
    write_pdf_info(tmp_path)

    def forbidden_collect(*args: object, **kwargs: object) -> LiveEvidenceResult:
        raise AssertionError("--summary must not call gh")

    lines: list[str] = []
    status = collect_run(["A2", TEAM, "--summary"], root=tmp_path, out=lines.append, collect=forbidden_collect)

    assert status == 2
    assert len(lines) == 1
    assert lines[0].startswith("ERROR: missing ")
    for filename in (
        "issues.json",
        "prs.json",
        "runs_main.json",
        "runs_sha.json",
        "milestones.json",
        "releases.json",
        "tags.json",
    ):
        assert filename in lines[0]
    assert f"scripts/collect_github_evidence.py A2 {TEAM}" in lines[0]
    assert "Traceback" not in lines[0]


def _a2_step5() -> str:
    text = (ROOT / "A2" / "grading_prompt.md").read_text(encoding="utf-8")
    section = text.split("## Assignment-specific procedure deltas", 1)[1]
    step = section.split("5. Collect the live evidence", 1)[1].split("6. Judge every issue", 1)[0]
    return re.sub(r" +", " ", re.sub(r"\\\n\s+", " ", step))


def test_a2_step5_field_lists_match_the_collector() -> None:
    step5 = _a2_step5()
    assert f'gh label list --repo "$REPO" --limit {LABEL_LIMIT} --json {",".join(LABEL_FIELDS)}' in step5
    assert f'gh issue list --repo "$REPO" --state all --limit {ISSUE_LIMIT} --json {",".join(ISSUE_FIELDS)}' in step5
    assert f'gh pr list --repo "$REPO" --state all --limit {PR_LIMIT} --json {",".join(PR_FIELDS)}' in step5
    assert f'gh run list --repo "$REPO" --branch main --limit {RUN_LIMIT} --json {",".join(RUN_FIELDS)}' in step5
    sha_fields = ", ".join("." + field for field in RUN_SHA_FIELDS)
    assert f"--jq '.workflow_runs[] | [{sha_fields}] | @tsv'" in step5
    assert f".[] | [.{PATH_COMMIT_FIELDS[0]}, .commit.committer.date, (.commit.message | split(\"\\n\")[0])] | @tsv" in step5
    assert f"userContentEdits(first: 100) {{ nodes {{ {' '.join(EDIT_FIELDS)} }} }}" in USER_CONTENT_EDITS_QUERY
    assert f"userContentEdits(first: 100) {{ nodes {{ {' '.join(EDIT_FIELDS)} }} }}" in step5

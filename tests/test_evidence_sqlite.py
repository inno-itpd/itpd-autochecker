from __future__ import annotations

import json
from pathlib import Path
import sqlite3
import subprocess
import sys

import pytest

from scripts.collect_github_evidence import run as collect_run
from tools.grader_tools.evidence_sqlite import (
    EVIDENCE_DB_FILENAME,
    ISSUE_DUMP_KEYS,
    ISSUE_FIELDS_DUMP_KEYS,
    PR_DUMP_KEYS,
    SCHEMA_TABLES,
    EvidenceDatabaseError,
    write_evidence_database,
)
from tools.grader_tools.live_evidence import (
    ISSUE_FIELDS,
    PR_FIELDS,
    SUMMARY_FILENAME,
    LiveEvidenceResult,
    project_issue_fields,
)

TEAM = "Team 1 - Absolute Cinema_10937_assignsubmission_file"
REPO = "example-org/example-repo"
SHA = "1234567890abcdef1234567890abcdef12345678"


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def write_pdf_info(work_dir: Path, repo: object = REPO, sha: object = SHA) -> None:
    write_json(
        work_dir / "pdf-info.json",
        {"assignment": "A3", "team_dir": TEAM, "repo": repo, "sha": sha},
    )


def write_saved_dumps(work_dir: Path, *, issue_fields: bool = True) -> None:
    """Write dumps whose optional arrays are null, as the real collector sometimes sees."""
    write_json(
        work_dir / "labels.json",
        [
            {"name": "task", "description": "One unit of work"},
            {"name": "user-story", "description": "A checkable story"},
        ],
    )
    write_json(
        work_dir / "milestones.json",
        [
            {
                "title": "SPRINT-03",
                "due_on": "2026-10-17T00:00:00Z",
                "open_issues": 1,
                "closed_issues": 1,
            }
        ],
    )
    write_json(
        work_dir / "issues.json",
        [
            {
                "number": 10,
                "state": "CLOSED",
                "stateReason": "COMPLETED",
                "title": "Task: add the slice",
                "body": "Closes when the slice runs.",
                "url": "https://example.com/issues/10",
                "author": {"login": "alice"},
                "createdAt": "2026-10-09T10:00:00Z",
                "closedAt": "2026-10-15T10:00:00Z",
                "labels": [{"name": "task", "description": "One unit of work"}],
                "closedByPullRequestsReferences": [
                    {
                        "number": 20,
                        "url": "https://example.com/pull/20",
                        "repository": {"name": "example-repo", "owner": {"login": "example-org"}},
                    }
                ],
            },
            {
                "number": 11,
                "state": "OPEN",
                "title": "Story with nulls",
                "labels": None,
                "closedByPullRequestsReferences": None,
                "author": None,
            },
        ],
    )
    write_json(
        work_dir / "prs.json",
        [
            {
                "number": 20,
                "title": "Close 10",
                "state": "MERGED",
                "author": {"login": "bob"},
                "headRefName": "10-add-slice",
                "baseRefName": "main",
                "createdAt": "2026-10-10T10:00:00Z",
                "mergedAt": "2026-10-15T09:00:00Z",
                "closedAt": "2026-10-15T09:00:00Z",
                "url": "https://example.com/pull/20",
                "body": "Closes #10",
                "closingIssuesReferences": [
                    {
                        "number": 10,
                        "url": "https://example.com/issues/10",
                        "repository": {"name": "example-repo", "owner": {"login": "example-org"}},
                    }
                ],
                "reviews": [
                    {
                        "author": {"login": "carol"},
                        "state": "APPROVED",
                        "submittedAt": "2026-10-15T08:00:00Z",
                        "body": "LGTM",
                    }
                ],
                "files": [
                    {"path": "app/main.py", "additions": 5, "deletions": 0, "changeType": "MODIFIED"},
                    {"path": "docs/setup.md", "additions": 2, "deletions": 1, "changeType": "MODIFIED"},
                ],
            },
            {
                "number": 21,
                "title": "Pull request with nulls",
                "state": "OPEN",
                "closingIssuesReferences": None,
                "reviews": None,
                "files": None,
                "author": None,
            },
        ],
    )
    if issue_fields:
        write_json(
            work_dir / "issue-fields.json",
            [
                {
                    "number": 10,
                    "state": "closed",
                    "title": "Task: add the slice",
                    "type": "Task",
                    "milestone": "SPRINT-03",
                    "assignees": ["alice", "bob"],
                    "field_values": [
                        {"name": "Responsible", "data_type": "single_select", "value": "alice"},
                        {"name": "Accountable", "data_type": "single_select", "value": "bob"},
                    ],
                },
                {
                    "number": 11,
                    "state": "open",
                    "title": "Story with nulls",
                    "type": None,
                    "milestone": None,
                    "assignees": None,
                    "field_values": None,
                },
            ],
        )


@pytest.fixture
def work_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "itpd-assignments-feedback" / "A3" / "work" / TEAM
    directory.mkdir(parents=True)
    return directory


@pytest.fixture
def null_dumps(work_dir: Path) -> Path:
    """A team work directory whose dumps carry the null arrays the real API returns."""
    write_saved_dumps(work_dir)
    return work_dir


def projection_rows(database: Path) -> list[tuple[object, ...]]:
    with sqlite3.connect(database) as connection:
        return connection.execute(
            "SELECT number, state, title, type, milestone, milestone_due_on, labels, assignees, "
            "closing_pull_requests FROM issue_projection ORDER BY number"
        ).fetchall()


def test_projection_answers_the_s6_issue_questions(null_dumps: Path) -> None:
    database = write_evidence_database(null_dumps)

    assert database.path == null_dumps / EVIDENCE_DB_FILENAME
    assert database.path.stat().st_mode & 0o777 == 0o600
    assert projection_rows(database.path) == [
        (
            10,
            "closed",
            "Task: add the slice",
            "Task",
            "SPRINT-03",
            "2026-10-17T00:00:00Z",
            "task",
            "alice, bob",
            "20",
        ),
        (11, "open", "Story with nulls", None, None, None, "", "", ""),
    ]
    assert database.counts == {
        "issues": 2,
        "labels": 2,
        "issue_labels": 1,
        "milestones": 1,
        "issue_assignees": 2,
        "issue_closing_references": 1,
        "issue_field_values": 2,
        "pull_requests": 2,
        "pr_reviews": 1,
        "pr_files": 2,
        "pr_closing_references": 1,
    }


def test_sql_answers_the_s7_questions(null_dumps: Path) -> None:
    database = write_evidence_database(null_dumps)

    with sqlite3.connect(database.path) as connection:
        field_values = connection.execute(
            "SELECT issue_number, name, value FROM issue_field_values ORDER BY issue_number, name"
        ).fetchall()
        milestones = connection.execute(
            "SELECT title, due_on, open_issues, closed_issues FROM milestones"
        ).fetchall()
        reviews = connection.execute(
            "SELECT pull_request_number, author_login, state, submitted_at FROM pr_reviews"
        ).fetchall()
        closes = connection.execute(
            "SELECT pull_request_number, issue_number FROM pr_closing_references ORDER BY issue_number"
        ).fetchall()
        unclosed = connection.execute(
            "SELECT p.number FROM pull_requests AS p "
            "LEFT JOIN pr_closing_references AS c ON c.pull_request_number = p.number "
            "WHERE c.issue_number IS NULL ORDER BY p.number"
        ).fetchall()

    assert field_values == [
        (10, "Accountable", "bob"),
        (10, "Responsible", "alice"),
    ]
    assert milestones == [("SPRINT-03", "2026-10-17T00:00:00Z", 1, 1)]
    assert reviews == [(20, "carol", "approved", "2026-10-15T08:00:00Z")]
    assert closes == [(20, 10)]
    assert unclosed == [(21,)]


def test_missing_issue_fields_is_not_an_error(work_dir: Path) -> None:
    write_saved_dumps(work_dir, issue_fields=False)
    database = write_evidence_database(work_dir)

    assert database.counts["issues"] == 2
    assert database.counts["issue_assignees"] == 0
    assert database.counts["issue_field_values"] == 0
    assert projection_rows(database.path) == [
        (10, "closed", "Task: add the slice", None, None, None, "task", "", "20"),
        (11, "open", "Story with nulls", None, None, None, "", "", ""),
    ]


def test_issue_fields_alone_builds_the_issue_rows(work_dir: Path) -> None:
    write_json(
        work_dir / "issue-fields.json",
        [
            {
                "number": 10,
                "state": "closed",
                "title": "Task: add the slice",
                "type": "Task",
                "milestone": None,
                "assignees": ["alice"],
                "field_values": None,
            }
        ],
    )
    database = write_evidence_database(work_dir)

    assert database.counts["issues"] == 1
    assert database.counts["pull_requests"] == 0
    assert projection_rows(database.path) == [
        (10, "closed", "Task: add the slice", "Task", None, None, "", "alice", "")
    ]


def test_null_top_level_dumps_become_empty_tables(work_dir: Path) -> None:
    write_json(work_dir / "issues.json", None)
    write_json(work_dir / "prs.json", None)
    write_json(work_dir / "issue-fields.json", {"unexpected": "object"})
    database = write_evidence_database(work_dir)

    assert database.counts["issues"] == 0
    assert database.counts["pull_requests"] == 0
    assert projection_rows(database.path) == []


def test_malformed_dump_raises_a_clear_error(work_dir: Path) -> None:
    (work_dir / "issues.json").write_text("{", encoding="utf-8")

    with pytest.raises(EvidenceDatabaseError, match="cannot parse"):
        write_evidence_database(work_dir)


def test_summary_mode_rebuilds_the_database_without_gh(work_dir: Path) -> None:
    write_pdf_info(work_dir)
    write_saved_dumps(work_dir)
    for name in ("runs_main.json", "runs_sha.json", "releases.json", "tags.json"):
        write_json(work_dir / name, [])
    root = work_dir.parents[3]

    def forbidden_collect(*args: object, **kwargs: object) -> LiveEvidenceResult:
        raise AssertionError("--summary must reuse the saved dumps instead of calling gh")

    lines: list[str] = []
    status = collect_run(["A3", TEAM, "--summary"], root=root, out=lines.append, collect=forbidden_collect)

    assert status == 0
    digest_path = work_dir / SUMMARY_FILENAME
    digest = digest_path.read_text(encoding="utf-8")
    assert lines == digest.splitlines() + [
        f"  evidence.sqlite: {len(SCHEMA_TABLES)} tables, 2 issues, 2 pull requests -> "
        f"itpd-assignments-feedback/A3/work/{TEAM}/{EVIDENCE_DB_FILENAME}"
    ]
    assert projection_rows(work_dir / EVIDENCE_DB_FILENAME)[0][3] == "Task"

    # A later dump change is picked up by another --summary, which proves a rebuild.
    issues = json.loads((work_dir / "issues.json").read_text(encoding="utf-8"))
    issues.append({"number": 12, "state": "OPEN", "title": "Added after the first rebuild"})
    write_json(work_dir / "issues.json", issues)
    status = collect_run(["A3", TEAM, "--summary"], root=root, out=lines.append, collect=forbidden_collect)

    assert status == 0
    assert projection_rows(work_dir / EVIDENCE_DB_FILENAME)[-1][:3] == (
        12,
        "open",
        "Added after the first rebuild",
    )


def test_stdlib_sqlite_cli_opens_the_database(null_dumps: Path) -> None:
    database = write_evidence_database(null_dumps)

    listing = subprocess.run(
        [sys.executable, "-m", "sqlite3", str(database.path), "PRAGMA table_list;"],
        capture_output=True,
        text=True,
        check=False,
    )
    query = subprocess.run(
        [
            sys.executable,
            "-m",
            "sqlite3",
            str(database.path),
            "SELECT number, assignees FROM issue_projection ORDER BY number;",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert listing.returncode == 0, listing.stderr
    for table in SCHEMA_TABLES:
        assert table in listing.stdout
    assert "issue_projection" in listing.stdout
    assert query.returncode == 0, query.stderr
    assert "(10, 'alice, bob')" in query.stdout
    assert "(11, '')" in query.stdout


def test_dump_keys_match_the_collector() -> None:
    assert ISSUE_DUMP_KEYS == ISSUE_FIELDS
    assert PR_DUMP_KEYS == PR_FIELDS

    row = project_issue_fields(
        json.dumps(
            [
                {
                    "number": 1,
                    "state": "open",
                    "title": "An issue",
                    "type": None,
                    "milestone": None,
                    "assignees": None,
                    "issue_field_values": None,
                }
            ]
        )
    )[0]
    assert tuple(row) == ISSUE_FIELDS_DUMP_KEYS

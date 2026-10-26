from __future__ import annotations

import json
from pathlib import Path
import stat

import pytest

from tools.grader_tools.markdown_submission import (
    fetch_markdown_submission,
    parse_markdown_members,
    read_markdown_metadata,
    select_markdown_wrapper,
)
from tools.grader_tools.submission_pdf import CommitCheck, SubmissionPdfError

SHA = "1234567890abcdef1234567890abcdef12345678"
WRONG_WEEK_SHA = "abcdefabcdefabcdefabcdefabcdefabcdefabcd"
TEAM_DIR = "Team 4 - Markdown Test_10940_assignsubmission_file"

WRAPPER = f"""# Running Coach App — Team 04 submission

## Project

Running Coach App, team 4.

## Team

| GitHub username | Real name | University email | This week |
| --- | --- | --- | --- |
| @alice | Alice Smith | alice@innopolis.university | Participated |
| @bob | Bob Jones | bob@innopolis.university | Participated |

## Team change

@carol (Carol White, carol@innopolis.university) has taken academic leave.

## Week 04 report

Permalink: https://github.com/example/running-coach/blob/{SHA}/reports/week-04/README.md

## Validation meeting recording

Share link: https://us06web.zoom.us/rec/share/example
"""


def _write_wrapper(root: Path, text: str = WRAPPER, name: str = "wrapper.md") -> Path:
    submission = root / "itpd-assignments-feedback" / "A4" / "submissions" / TEAM_DIR
    submission.mkdir(parents=True)
    path = submission / name
    path.write_text(text, encoding="utf-8")
    return path


def test_parse_markdown_members_reads_table_and_team_change() -> None:
    members, usernames, name_tokens, email_tokens = parse_markdown_members(WRAPPER)
    assert [member.github_username for member in members] == ["alice", "bob"]
    assert usernames == ["alice", "bob", "carol"]
    assert "smith" in name_tokens and "jones" in name_tokens and "white" in name_tokens
    assert email_tokens == [
        "alice@innopolis.university",
        "bob@innopolis.university",
        "carol@innopolis.university",
    ]


def test_read_markdown_metadata_finds_the_permalink_and_recording(tmp_path: Path) -> None:
    wrapper = tmp_path / "wrapper.md"
    wrapper.write_text(WRAPPER, encoding="utf-8")
    metadata = read_markdown_metadata(wrapper, "reports/week-04/README.md")
    assert metadata.permalink is not None
    assert metadata.permalink.repo_full == "example/running-coach"
    assert metadata.permalink.sha == SHA
    assert metadata.permalink.path == "/reports/week-04/README.md"
    assert metadata.recording_link == "https://us06web.zoom.us/rec/share/example"
    assert metadata.github_usernames == ("alice", "bob", "carol")


def test_select_markdown_wrapper_prefers_the_file_with_a_permalink(tmp_path: Path) -> None:
    submission = tmp_path / "itpd-assignments-feedback" / "A4" / "submissions" / TEAM_DIR
    submission.mkdir(parents=True)
    (submission / "a.md").write_text("# Notes\n\nNo permalink here.\n", encoding="utf-8")
    (submission / "b.md").write_text(WRAPPER, encoding="utf-8")
    metadata = select_markdown_wrapper(submission, "reports/week-04/README.md")
    assert metadata.path.name == "b.md"


def test_fetch_markdown_submission_writes_pdf_info_and_fetches(tmp_path: Path) -> None:
    _write_wrapper(tmp_path)
    fetched: list[tuple[str, str, Path]] = []

    def fake_check(repo: str, sha: str) -> CommitCheck:
        return CommitCheck(exists=True, snapshot_time="2026-10-25T10:00:00Z", on_main=True, on_main_status="ahead")

    def fake_fetch(repo: str, sha: str, snapshot_dir: Path) -> None:
        fetched.append((repo, sha, snapshot_dir))
        (snapshot_dir / "README.md").write_text("# snapshot\n", encoding="utf-8")

    result = fetch_markdown_submission(
        "A4",
        TEAM_DIR,
        root=tmp_path,
        check_commit_fn=fake_check,
        fetch_snapshot_fn=fake_fetch,
    )
    assert result.week_mismatch is False
    assert result.snapshot_fetched is True
    assert fetched and fetched[0][0] == "example/running-coach"
    payload = json.loads(result.pdf_info_path.read_text(encoding="utf-8"))
    assert payload["assignment"] == "A4"
    assert payload["team_dir"] == TEAM_DIR
    assert payload["pdf"] == "wrapper.md"
    assert payload["page_count"] == 0
    assert payload["submission_format"] == "markdown"
    assert payload["sha"] == SHA
    assert payload["permalink_source"] == "operator"
    assert payload["snapshot_time"] == "2026-10-25T10:00:00Z"
    assert payload["on_main"] is True
    assert payload["snapshot_fetched"] is True
    assert payload["github_usernames"] == ["alice", "bob", "carol"]
    assert "smith" in payload["privacy_tokens"]["name_tokens"]
    assert "alice@innopolis.university" in payload["privacy_tokens"]["email_tokens"]
    assert stat.S_IMODE(result.pdf_info_path.stat().st_mode) == 0o600


def test_fetch_markdown_submission_stops_on_a_wrong_week(tmp_path: Path) -> None:
    wrapper = WRAPPER.replace(SHA, WRONG_WEEK_SHA).replace(
        "reports/week-04/README.md", "reports/week-03/README.md"
    )
    _write_wrapper(tmp_path, wrapper)
    called: list[object] = []

    def fake_fetch(repo: str, sha: str, snapshot_dir: Path) -> None:
        called.append((repo, sha, snapshot_dir))

    result = fetch_markdown_submission(
        "A4",
        TEAM_DIR,
        root=tmp_path,
        check_commit_fn=lambda repo, sha: pytest.fail("the wrong-week stop must not check the commit"),
        fetch_snapshot_fn=fake_fetch,
    )
    assert result.week_mismatch is True
    assert result.snapshot_fetched is False
    assert called == []
    payload = json.loads(result.pdf_info_path.read_text(encoding="utf-8"))
    assert payload["permalink_week"] == 3
    assert payload["expected_week"] == 4
    assert payload["permalink_week_mismatch"] is True
    assert payload["snapshot_fetched"] is False
    summary = result.pdf_info_path.parent / "summary.md"
    assert summary.exists()
    assert "warn:" in summary.read_text(encoding="utf-8")


def test_fetch_markdown_submission_rejects_an_empty_submission(tmp_path: Path) -> None:
    submission = tmp_path / "itpd-assignments-feedback" / "A4" / "submissions" / TEAM_DIR
    submission.mkdir(parents=True)
    with pytest.raises(SubmissionPdfError, match="no PDF and no Markdown"):
        fetch_markdown_submission("A4", TEAM_DIR, root=tmp_path)

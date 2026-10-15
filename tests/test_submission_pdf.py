from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import pytest

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.submission_pdf import (
    CommandResult,
    CommitCheck,
    SnapshotFetchError,
    SubmissionPdfError,
    check_commit,
    extract_pdf_page_count,
    fetch_team_snapshot,
    find_permalink,
    find_recording_link,
    parse_member_table,
    parse_pdf_uri_annotations,
    parse_pdftohtml_links,
    read_pdf_metadata,
    rejoin_wrapped_urls,
    select_submission_pdf,
)

FIXTURES = Path(__file__).parent / "fixtures"
SHA = "1234567890abcdef1234567890abcdef12345678"
WRAPPED_SHA = "abcdefabcdefabcdefabcdefabcdefabcdefabcd"

requires_poppler = pytest.mark.skipif(
    shutil.which("pdftotext") is None or shutil.which("pdftohtml") is None or shutil.which("pdfinfo") is None,
    reason="poppler tools (pdftotext, pdftohtml, pdfinfo) are required",
)


def test_parse_pdftohtml_links_decodes_entities() -> None:
    xml = '<text><a href="https://example.com/a&amp;b">x</a></text><text><a href="https://example.com/c">y</a></text>'
    assert parse_pdftohtml_links(xml) == ["https://example.com/a&b", "https://example.com/c"]


def test_parse_pdf_uri_annotations_handles_escapes_and_hex() -> None:
    raw = (
        rb"/URI (https://example.com/a\(b\)c) /URI (https://example.com/two) "
        rb"/URI <68747470733A2F2F6578616D706C652E636F6D2F686578>"
    )
    assert parse_pdf_uri_annotations(raw) == [
        "https://example.com/a(b)c",
        "https://example.com/two",
        "https://example.com/hex",
    ]


def test_rejoin_wrapped_urls_joins_continuations_only() -> None:
    text = (
        "https://github.com/example-org/example-repo/blob/"
        f"{WRAPPED_SHA}/reports/we\nek-01/README.md\n"
        "Meet recording:\n"
        "https://drive.google.com/drive/folders/Example-Wrapped-\n"
        "RecordingLink?usp=sharing\n"
        "Transcript: not published.\n"
    )
    joined = rejoin_wrapped_urls(text)
    assert f"reports/week-01/README.md" in joined
    assert "https://drive.google.com/drive/folders/Example-Wrapped-RecordingLink?usp=sharing" in joined
    assert "RecordingLink?usp=sharingTranscript" not in joined


def test_find_permalink_prefers_primary_index_over_other_paths() -> None:
    urls = [
        f"https://github.com/example-org/example-repo/blob/{SHA}/reports/week-02/meeting-notes.md",
        f"https://github.com/example-org/example-repo/blob/{SHA}/reports/week-02/README.md",
    ]
    permalink = find_permalink(urls, "Commit: " + SHA, "reports/week-02/README.md")
    assert permalink is not None
    assert permalink.path == "/reports/week-02/README.md"
    assert permalink.repo_full == "example-org/example-repo"


def test_find_permalink_accepts_tree_directory_link() -> None:
    urls = [f"https://github.com/example-org/example-repo/tree/{SHA}/reports/week-01"]
    permalink = find_permalink(urls, "", "reports/week-01/README.md")
    assert permalink is not None
    assert permalink.path == "/reports/week-01"


def test_find_permalink_requires_full_sha() -> None:
    urls = ["https://github.com/example-org/example-repo/blob/abc1234/reports/week-01/README.md"]
    assert find_permalink(urls, "Commit: abc1234", "reports/week-01/README.md") is None


def test_find_permalink_combines_repo_url_with_bare_sha() -> None:
    text = f"Commit: {SHA}"
    urls = ["https://github.com/example-org/example-repo"]
    permalink = find_permalink(urls, text, "reports/week-01/README.md")
    assert permalink is not None
    assert (permalink.org, permalink.repo, permalink.sha) == ("example-org", "example-repo", SHA)


def test_find_permalink_from_repo_at_sha_text() -> None:
    text = f"Repository link: example-org/example-repo at\n{SHA}"
    permalink = find_permalink([], text, "reports/week-01/README.md")
    assert permalink is not None
    assert permalink.repo_full == "example-org/example-repo"


def test_find_recording_link_prefers_record_context() -> None:
    first = "https://example.com/unrelated"
    second = "https://drive.google.com/drive/folders/example"
    text = f"Some unrelated link: {first}\nKickoff meeting recording: {second}"
    assert find_recording_link([first, second], text, None) == second


def test_parse_member_table_username_first_and_name_first() -> None:
    username_first = (
        "GitHub username Real name University email\n"
        "octo-user Mira Sample m.sample@example.edu\n"
    )
    members, emails = parse_member_table(username_first)
    assert [member.github_username for member in members] == ["octo-user"]
    assert members[0].name_tokens == ("mira", "sample")
    assert emails == ["m.sample@example.edu"]

    name_first = "Name GitHub Innopolis mail\nMira Sample MiraSample m.sample@example.edu\n"
    members, emails = parse_member_table(name_first)
    assert [member.github_username for member in members] == ["MiraSample"]
    assert members[0].name_tokens == ("mira", "sample")


def test_parse_member_table_stops_at_prose() -> None:
    text = (
        "GitHub username Real name University email\n"
        "@dev Mira Sample m.sample@example.edu\n"
        "Contact the Customer at customer@example.edu for questions.\n"
    )
    members, emails = parse_member_table(text)
    assert [member.github_username for member in members] == ["dev"]
    assert "customer@example.edu" in emails


@requires_poppler
def test_extract_text_only_fixture() -> None:
    metadata = read_pdf_metadata(FIXTURES / "submission-text-only.pdf", "reports/week-01/README.md")
    assert metadata.page_count == 2
    assert metadata.permalink is not None
    assert metadata.permalink.sha == WRAPPED_SHA
    assert metadata.permalink.path == "/reports/week-01/README.md"
    assert metadata.permalink.source == "text"
    assert metadata.recording_link == "https://drive.google.com/drive/folders/Example-Wrapped-RecordingLink?usp=sharing"
    assert [member.github_username for member in metadata.members] == ["MiraSample"]
    assert metadata.members[0].name_tokens == ("mira", "sample")


@requires_poppler
def test_extract_link_fixture() -> None:
    metadata = read_pdf_metadata(FIXTURES / "submission-with-links.pdf", "reports/week-02/README.md")
    assert metadata.page_count == 1
    assert metadata.permalink is not None
    assert metadata.permalink.sha == SHA
    assert metadata.permalink.path == "/reports/week-02/README.md"
    assert metadata.permalink.source == "link"
    assert metadata.recording_link == "https://drive.google.com/file/d/ExampleRecordingLink/view?usp=sharing"
    assert [member.github_username for member in metadata.members] == ["octo-user", "second-dev"]
    assert metadata.email_tokens == ("m.sample@example.edu", "j.doe@example.edu")


@requires_poppler
def test_extract_short_sha_fixture_has_no_permalink() -> None:
    metadata = read_pdf_metadata(FIXTURES / "submission-short-sha.pdf", "reports/week-01/README.md")
    assert metadata.permalink is None
    assert metadata.recording_link is None


@requires_poppler
def test_extract_pdf_page_count_falls_back_to_xml_page_numbers() -> None:
    xml = '<pdf2xml><page number="1"></page><page number="2"></page></pdf2xml>'
    try:
        count = extract_pdf_page_count(FIXTURES / "submission-with-links.pdf", xml)
    except SubmissionPdfError:
        pytest.skip("pdfinfo is not available")
    assert count == 1


@requires_poppler
def test_select_submission_pdf_picks_the_pdf_with_a_full_sha(tmp_path: Path) -> None:
    shutil.copyfile(FIXTURES / "submission-short-sha.pdf", tmp_path / "a-short.pdf")
    shutil.copyfile(FIXTURES / "submission-with-links.pdf", tmp_path / "b-full.pdf")
    metadata = select_submission_pdf(tmp_path, "reports/week-02/README.md")
    assert metadata.pdf_path.name == "b-full.pdf"
    assert metadata.permalink is not None


@requires_poppler
def test_select_submission_pdf_returns_first_without_sha(tmp_path: Path) -> None:
    shutil.copyfile(FIXTURES / "submission-short-sha.pdf", tmp_path / "only.pdf")
    metadata = select_submission_pdf(tmp_path, "reports/week-01/README.md")
    assert metadata.pdf_path.name == "only.pdf"
    assert metadata.permalink is None


def test_select_submission_pdf_requires_a_pdf(tmp_path: Path) -> None:
    with pytest.raises(SubmissionPdfError):
        select_submission_pdf(tmp_path, "reports/week-01/README.md")


def test_check_commit_reports_missing_commit() -> None:
    result = check_commit("org/repo", SHA, runner=lambda args: CommandResult(1, "", "HTTP 404: Not Found"))
    assert result == CommitCheck(exists=False, snapshot_time=None, on_main=None, on_main_status=None)


def test_check_commit_reads_on_main_status() -> None:
    outputs = {
        ("api", f"repos/org/repo/commits/{SHA}", "--jq", ".commit.committer.date"): CommandResult(
            0, "2026-10-02T20:21:43Z\n", ""
        ),
        ("api", f"repos/org/repo/compare/{SHA}...main", "--jq", ".status"): CommandResult(0, "ahead\n", ""),
    }
    result = check_commit("org/repo", SHA, runner=lambda args: outputs[tuple(args)])
    assert result == CommitCheck(True, "2026-10-02T20:21:43Z", True, "ahead")


def test_check_commit_missing_main_is_not_on_main() -> None:
    outputs = {
        ("api", f"repos/org/repo/commits/{SHA}", "--jq", ".commit.committer.date"): CommandResult(0, "2026-10-02T20:21:43Z\n", ""),
        ("api", f"repos/org/repo/compare/{SHA}...main", "--jq", ".status"): CommandResult(1, "", "HTTP 404"),
    }
    result = check_commit("org/repo", SHA, runner=lambda args: outputs[tuple(args)])
    assert result.exists is True
    assert result.on_main is False
    assert result.on_main_status == "not-found"


def test_check_commit_raises_on_transport_errors() -> None:
    with pytest.raises(SnapshotFetchError):
        check_commit("org/repo", SHA, runner=lambda args: CommandResult(1, "", "authentication failed"))


def build_assignment_root(tmp_path: Path, assignment: str, fixture: str) -> Path:
    team_dir = tmp_path / "itpd-assignments-feedback" / assignment / "submissions" / "Team 1_x_assignsubmission_file"
    team_dir.mkdir(parents=True)
    shutil.copyfile(FIXTURES / fixture, team_dir / fixture)
    return tmp_path


def test_fetch_team_snapshot_stops_cleanly_without_a_full_sha(tmp_path: Path) -> None:
    root = build_assignment_root(tmp_path, "A1", "submission-short-sha.pdf")

    def fail(*args, **kwargs):  # pragma: no cover - must not be called
        raise AssertionError("repository-dependent checks must not run without a full SHA")

    result = fetch_team_snapshot("A1", "Team 1_x_assignsubmission_file", root, check_commit_fn=fail, fetch_snapshot_fn=fail)
    assert result.pdf_info["sha"] is None
    assert result.pdf_info["commit_exists"] is None
    assert result.pdf_info["snapshot_fetched"] is False
    assert result.snapshot_dir.exists()
    assert list(result.snapshot_dir.iterdir()) == []
    payload = json.loads(result.pdf_info_path.read_text(encoding="utf-8"))
    assert payload["privacy_tokens"]["email_tokens"] == ["d.example@example.edu"]
    summary = "\n".join(result.summary_lines)
    assert "stopping repository-dependent checks" in summary
    assert "Dana" not in summary
    assert "d.example@example.edu" not in summary
    assert os.stat(result.pdf_info_path).st_mode & 0o777 == 0o600


def test_fetch_team_snapshot_fetches_the_tarball(tmp_path: Path) -> None:
    root = build_assignment_root(tmp_path, "A1", "submission-with-links.pdf")
    calls: list[tuple[str, str]] = []

    def fake_check(repo: str, sha: str) -> CommitCheck:
        calls.append(("check", repo))
        return CommitCheck(exists=True, snapshot_time="2026-10-02T20:21:43Z", on_main=True, on_main_status="ahead")

    def fake_fetch(repo: str, sha: str, snapshot_dir: Path) -> None:
        calls.append(("fetch", repo))
        (snapshot_dir / "README.md").write_text("snapshot", encoding="utf-8")

    result = fetch_team_snapshot(
        "A1",
        "Team 1_x_assignsubmission_file",
        root,
        check_commit_fn=fake_check,
        fetch_snapshot_fn=fake_fetch,
    )
    assert calls == [("check", "example-org/example-repo"), ("fetch", "example-org/example-repo")]
    assert result.pdf_info["repo"] == "example-org/example-repo"
    assert result.pdf_info["sha"] == SHA
    assert result.pdf_info["snapshot_time"] == "2026-10-02T20:21:43Z"
    assert result.pdf_info["on_main"] is True
    assert result.pdf_info["snapshot_fetched"] is True
    work_dir = root / "itpd-assignments-feedback" / "A1" / "work" / "Team 1_x_assignsubmission_file"
    assert result.snapshot_dir == work_dir / "snapshot"
    assert result.pdf_info_path == work_dir / "pdf-info.json"
    assert result.pdf_info["snapshot_dir"] == "itpd-assignments-feedback/A1/work/Team 1_x_assignsubmission_file/snapshot"
    assert (result.snapshot_dir / "README.md").read_text(encoding="utf-8") == "snapshot"
    summary = "\n".join(result.summary_lines)
    assert "commit: exists; on_main=yes (ahead)" in summary
    assert "Mira" not in summary
    assert "m.sample@example.edu" not in summary


def test_fetch_team_snapshot_skips_fetch_when_commit_is_missing(tmp_path: Path) -> None:
    root = build_assignment_root(tmp_path, "A1", "submission-with-links.pdf")

    def fail_fetch(*args, **kwargs):  # pragma: no cover - must not be called
        raise AssertionError("the tarball must not be fetched when the commit does not exist")

    result = fetch_team_snapshot(
        "A1",
        "Team 1_x_assignsubmission_file",
        root,
        check_commit_fn=lambda repo, sha: CommitCheck(False, None, None, None),
        fetch_snapshot_fn=fail_fetch,
    )
    assert result.pdf_info["commit_exists"] is False
    assert result.pdf_info["snapshot_fetched"] is False
    assert list(result.snapshot_dir.iterdir()) == []
    assert "commit: missing" in "\n".join(result.summary_lines)


def test_fetch_team_snapshot_rejects_unknown_assignment(tmp_path: Path) -> None:
    with pytest.raises(SubmissionPdfError):
        fetch_team_snapshot("A9", "Team 1_x_assignsubmission_file", tmp_path)


def test_fetch_team_snapshot_rejects_missing_submission_dir(tmp_path: Path) -> None:
    with pytest.raises(SubmissionPdfError):
        fetch_team_snapshot("A1", "Team 99_x_assignsubmission_file", tmp_path)

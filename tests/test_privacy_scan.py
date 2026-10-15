from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.scan_privacy import run
from tools.grader_tools import privacy_scan
from tools.grader_tools.privacy_scan import (
    PrivacyScanError,
    classify_secret_file,
    is_meeting_artifact,
    scan_privacy,
)

TEAM = "Team 1_12345_assignsubmission_file"


def make_snapshot(
    tmp_path: Path,
    files: dict[str, str | bytes],
    *,
    name_tokens: tuple[str, ...] = (),
    email_tokens: tuple[str, ...] = (),
    recording_link: str | None = None,
    snapshot_fetched: bool = True,
) -> Path:
    work = tmp_path / "itpd-assignments-feedback" / "A1" / "work" / TEAM
    work.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        target = work / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            target.write_bytes(content)
        else:
            target.write_text(content, encoding="utf-8")
    scratch = tmp_path / "tmp" / "A1" / TEAM
    scratch.mkdir(parents=True, exist_ok=True)
    payload = {
        "assignment": "A1",
        "team_dir": TEAM,
        "recording_link": recording_link,
        "snapshot_fetched": snapshot_fetched,
        "work_dir": f"itpd-assignments-feedback/A1/work/{TEAM}",
        "privacy_tokens": {"name_tokens": list(name_tokens), "email_tokens": list(email_tokens)},
    }
    (scratch / "pdf-info.json").write_text(json.dumps(payload), encoding="utf-8")
    return work


def test_email_rule_flags_personal_but_not_placeholders(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {
            "docs/notes.md": (
                "Write to secret.person@university.edu\n"
                "Placeholder: contact@example.com\n"
                "GitHub: 12345+octo@users.noreply.github.com\n"
            )
        },
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [(finding.rule, finding.kind, finding.line) for finding in result.findings] == [
        ("email", "email address", 1)
    ]
    assert result.findings[0].path.endswith("/docs/notes.md")
    report = "\n".join(result.summary_lines)
    assert "secret.person" not in report
    assert "example.com" not in report


def test_email_rule_keeps_a_member_email_on_a_placeholder_domain(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {"docs/notes.md": "Mail: m.sample@example.edu\n"},
        email_tokens=("m.sample@example.edu",),
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [finding.rule for finding in result.findings] == ["email"]


def test_phone_rule_flags_common_formats_and_ignores_dates_and_ids(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {
            "docs/contacts.md": (
                "Phone +7 (912) 345-67-89\n"
                "Phone 8 812 555 11 22\n"
                "Phone (495) 123-45-67\n"
                "Date 2026-10-02\n"
                "Version v1.2.3\n"
                "ID 1234567890123456789\n"
            )
        },
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [(finding.rule, finding.kind, finding.line) for finding in result.findings] == [
        ("phone", "phone number", 1),
        ("phone", "phone number", 2),
        ("phone", "phone number", 3),
    ]
    assert "912" not in "\n".join(result.summary_lines)


def test_secret_file_rule_flags_env_and_key_files_but_not_examples(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {
            ".env": "TOKEN=abc\n",
            ".env.local": "TOKEN=abc\n",
            ".env.example": "TOKEN={{access_token}}\n",
            "app.key": "key material\n",
            "certs/server.pem": "pem material\n",
            "deploy/id_ed25519": "key material\n",
        },
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [(Path(finding.path).name, finding.kind, finding.line) for finding in result.findings] == [
        (".env", "env file", None),
        (".env.local", "env file", None),
        ("app.key", "key file", None),
        ("server.pem", "key file", None),
        ("id_ed25519", "key file", None),
    ]


def test_recording_rule_flags_links_outside_meeting_artifacts(tmp_path: Path) -> None:
    recording = "https://files.example.org/team-1-recording"
    make_snapshot(
        tmp_path,
        {
            "docs/sources.md": "Recording: https://us02web.zoom.us/j/123456789\n",
            "docs/archive.md": f"PDF recording: {recording}\nBoard: https://docs.google.com/document/d/board\n",
            "reports/week-02/meeting-report.md": (
                f"Recording: https://drive.google.com/file/d/abc/view\nDiff: {recording}\n"
            ),
        },
        recording_link=recording,
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [(finding.rule, finding.path.rsplit("/", 1)[-1], finding.line) for finding in result.findings] == [
        ("recording", "archive.md", 1),
        ("recording", "sources.md", 1),
    ]


@pytest.mark.parametrize(
    ("relative_path", "expected"),
    [
        ("reports/week-02/meeting-report.md", True),
        ("reports/week-01/meeting-script.md", True),
        ("reports/week-01/kickoff-report.md", True),
        ("docs/meeting-notes/2026-10-02.md", True),
        ("docs/customer-meeting.md", True),
        ("reports/week-01/README.md", False),
        ("docs/notes.md", False),
    ],
)
def test_is_meeting_artifact(relative_path: str, expected: bool) -> None:
    assert is_meeting_artifact(relative_path) is expected


def test_member_name_rule_matches_whole_words_case_insensitively(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {
            "reports/week-01/README.md": (
                "Ivanov drafted the vision.\n" "subivanovsky is not a match.\n" "Petrova reviewed it.\n"
            )
        },
        name_tokens=("ivanov", "petrova"),
    )
    result = scan_privacy("A1", TEAM, tmp_path)
    assert [(finding.rule, finding.kind, finding.line) for finding in result.findings] == [
        ("member-name", "member name token", 1),
        ("member-name", "member name token", 3),
    ]
    report = "\n".join(result.summary_lines)
    assert "Ivanov" not in report
    assert "Petrova" not in report
    assert "subivanovsky" not in report


def test_binary_oversized_and_symlink_files_are_skipped(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    work = make_snapshot(
        tmp_path,
        {
            "img.bin": b"\x00secret.person@university.edu",
            "big.md": "x" * 100 + " secret.person@university.edu\n",
        },
    )
    (work / "link.md").symlink_to(work / "big.md")
    monkeypatch.setattr(privacy_scan, "MAX_TEXT_BYTES", 40)
    result = scan_privacy("A1", TEAM, tmp_path)
    assert result.findings == ()
    assert result.skipped_binary == 1
    assert result.skipped_large == 1
    assert result.skipped_symlinks == 1


def test_feedback_mode_scans_the_report_instead_of_the_snapshot(tmp_path: Path) -> None:
    make_snapshot(
        tmp_path,
        {"docs/notes.md": "secret.person@university.edu\n"},
        name_tokens=("ivanov",),
    )
    report = tmp_path / "report" / "agent-feedback.md"
    report.parent.mkdir()
    report.write_text("Contact secret.person@university.edu about Ivanov.\n", encoding="utf-8")
    result = scan_privacy("A1", TEAM, tmp_path, feedback_path=report)
    assert result.mode == "feedback"
    assert [(finding.rule, finding.line) for finding in result.findings] == [("email", 1), ("member-name", 1)]
    assert all(finding.path == "report/agent-feedback.md" for finding in result.findings)
    assert "secret.person" not in "\n".join(result.summary_lines)


def test_run_reports_clean_and_finding_exit_codes(tmp_path: Path) -> None:
    work = make_snapshot(tmp_path, {"README.md": "A clean report.\n"})
    lines: list[str] = []
    assert run(["A1", TEAM], root=tmp_path, out=lines.append) == 0
    assert lines[-1].endswith("no findings")

    (work / "docs").mkdir()
    (work / "docs" / "contacts.md").write_text("Mail secret.person@university.edu\n", encoding="utf-8")
    lines = []
    assert run(["A1", TEAM], root=tmp_path, out=lines.append) == 1
    assert any("email address: 1 finding(s)" in line for line in lines)
    assert all("secret.person" not in line for line in lines)


def test_run_missing_metadata_exits_2_without_traceback(tmp_path: Path) -> None:
    lines: list[str] = []
    assert run(["A1", "missing-team"], root=tmp_path, out=lines.append) == 2
    assert lines[0].startswith("ERROR:")
    assert "fetch_team_snapshot.py" in lines[0]


def test_scan_refuses_when_snapshot_was_not_fetched(tmp_path: Path) -> None:
    make_snapshot(tmp_path, {}, snapshot_fetched=False)
    with pytest.raises(PrivacyScanError, match="snapshot_fetched=false"):
        scan_privacy("A1", TEAM, tmp_path)


def test_classify_secret_file_ignores_envrc_and_samples() -> None:
    assert classify_secret_file(".envrc") is None
    assert classify_secret_file(".env.sample") is None
    assert classify_secret_file(".env.production") == "env file"

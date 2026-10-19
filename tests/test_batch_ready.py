from __future__ import annotations

import os
from pathlib import Path

import pytest

from scripts.check_batch_ready import run
from tools.grader_tools.batch_ready import (
    ACTIVE_REASON,
    BatchReadyError,
    check_batch_ready,
    format_mtime,
)

ASSIGNMENT = "A3"
BASE_NS = 1_760_000_000_000_000_000
ONE_SECOND_NS = 1_000_000_000

TEAM = "Team 1 - Absolute Cinema_10937_assignsubmission_file"
SEVEN_TEAMS = (
    "Team 1 - Absolute Cinema_10937_assignsubmission_file",
    "Team 2 - OK_10938_assignsubmission_file",
    "Team 3 - WellMadeTeam_10939_assignsubmission_file",
    "Team 4_10940_assignsubmission_file",
    "Team 5 - TmpTeam_10941_assignsubmission_file",
    "Team 6_10942_assignsubmission_file",
    "Team 9 - almo_10945_assignsubmission_file",
)


def make_root(tmp_path: Path) -> Path:
    base = tmp_path / "itpd-assignments-feedback" / ASSIGNMENT
    (base / "feedback").mkdir(parents=True)
    (base / "work").mkdir()
    return tmp_path


def team_paths(root: Path, team: str) -> tuple[Path, Path]:
    base = root / "itpd-assignments-feedback" / ASSIGNMENT
    return base / "feedback" / team, base / "work" / team


def write_file(path: Path, mtime_ns: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("x\n", encoding="utf-8")
    os.utime(path, ns=(mtime_ns, mtime_ns))


def add_team(
    root: Path,
    team: str,
    *,
    report_ns: int | None = None,
    payload_ns: int | None = None,
    work_files: tuple[str, ...] = (),
    create_work: bool = True,
) -> None:
    feedback_dir, work_dir = team_paths(root, team)
    if report_ns is not None:
        write_file(feedback_dir / "agent-feedback.md", report_ns)
    if create_work:
        work_dir.mkdir(parents=True, exist_ok=True)
        if payload_ns is not None:
            write_file(work_dir / "payload.json", payload_ns)
        for name in work_files:
            write_file(work_dir / name, BASE_NS)


def test_report_equal_to_payload_is_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS, payload_ns=BASE_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    assert result.has_refusals is False
    assert result.teams[0].ok is True
    assert result.summary_lines[0] == (
        f"{TEAM}: ok - report {format_mtime(BASE_NS)}, payload {format_mtime(BASE_NS)}"
    )
    assert result.summary_lines[-1] == "result: ready - 1 team(s) checked, no refusals"


def test_report_newer_than_payload_is_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS + ONE_SECOND_NS, payload_ns=BASE_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    assert result.has_refusals is False
    assert result.teams[0].reason is None


def test_payload_newer_than_report_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS, payload_ns=BASE_NS + ONE_SECOND_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    status = result.teams[0]
    assert result.has_refusals is True
    assert status.ok is False
    assert "payload.json is newer than the report" in status.reason
    assert "not rendered after the last payload update" in status.reason
    assert result.summary_lines[0] == f"{TEAM}: refused - {status.reason}"
    assert result.summary_lines[-1] == "result: not ready - 1 of 1 team(s) refused"


def test_active_team_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS + ONE_SECOND_NS, payload_ns=BASE_NS)

    result = check_batch_ready(ASSIGNMENT, root, active=[f"{TEAM}/"])

    assert result.teams[0].reason == ACTIVE_REASON
    assert result.summary_lines[0] == f"{TEAM}: refused - grader still registered or running"


def test_active_team_outside_the_batch_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, SEVEN_TEAMS[0], report_ns=BASE_NS, payload_ns=BASE_NS)
    add_team(root, SEVEN_TEAMS[1], report_ns=BASE_NS, payload_ns=BASE_NS, create_work=False)

    result = check_batch_ready(ASSIGNMENT, root, active=[SEVEN_TEAMS[1], ""])

    assert [status.team for status in result.teams] == [SEVEN_TEAMS[0], SEVEN_TEAMS[1]]
    assert result.teams[0].ok is True
    assert result.teams[1].reason == ACTIVE_REASON
    assert result.summary_lines[-1] == "result: not ready - 1 of 2 team(s) refused"


def test_work_directory_without_a_report_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, work_files=("pdf-info.json",))

    result = check_batch_ready(ASSIGNMENT, root)

    status = result.teams[0]
    assert status.report_mtime_ns is None
    assert "agent-feedback.md is missing" in status.reason
    assert "a writer started and never wrote a report" in status.reason
    assert result.has_refusals is True


def test_work_directory_with_a_payload_but_no_report_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, payload_ns=BASE_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    assert [status.team for status in result.teams] == [TEAM]
    assert "agent-feedback.md is missing" in result.teams[0].reason
    assert result.summary_lines[-1] == "result: not ready - 1 of 1 team(s) refused"


def test_empty_work_directory_without_a_report_is_skipped(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM)

    result = check_batch_ready(ASSIGNMENT, root)

    assert result.teams == ()
    assert result.summary_lines == ("result: ready - 0 team(s) checked, no refusals",)


def test_report_without_a_payload_is_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    assert result.has_refusals is False
    assert result.summary_lines[0] == (
        f"{TEAM}: ok - report {format_mtime(BASE_NS)}, payload missing"
    )


def test_report_without_a_work_directory_is_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS, create_work=False)

    result = check_batch_ready(ASSIGNMENT, root)

    assert [status.team for status in result.teams] == [TEAM]
    assert result.has_refusals is False


def test_mixed_batch_counts_only_refused_teams(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, SEVEN_TEAMS[0], report_ns=BASE_NS, payload_ns=BASE_NS)
    add_team(root, SEVEN_TEAMS[1], report_ns=BASE_NS, payload_ns=BASE_NS + ONE_SECOND_NS)
    add_team(root, SEVEN_TEAMS[2], work_files=("summary.md",))

    result = check_batch_ready(ASSIGNMENT, root, active=[SEVEN_TEAMS[0]])

    assert [status.team for status in result.teams] == list(SEVEN_TEAMS[:3])
    assert [status.ok for status in result.teams] == [False, False, False]
    assert result.teams[0].reason == ACTIVE_REASON
    assert "payload.json is newer than the report" in result.teams[1].reason
    assert "agent-feedback.md is missing" in result.teams[2].reason
    assert result.summary_lines[-1] == "result: not ready - 3 of 3 team(s) refused"


def test_seven_team_ready_batch_is_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    for index, team in enumerate(SEVEN_TEAMS):
        report_ns = BASE_NS + index * 10 * ONE_SECOND_NS
        add_team(root, team, report_ns=report_ns, payload_ns=report_ns - ONE_SECOND_NS)

    result = check_batch_ready(ASSIGNMENT, root)

    assert [status.team for status in result.teams] == sorted(SEVEN_TEAMS)
    assert len(result.teams) == 7
    assert all(status.ok for status in result.teams)
    assert result.has_refusals is False
    assert len(result.summary_lines) == 8
    assert result.summary_lines[-1] == "result: ready - 7 team(s) checked, no refusals"


def test_cli_exits_zero_when_ready(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS + ONE_SECOND_NS, payload_ns=BASE_NS)
    lines: list[str] = []

    exit_code = run([ASSIGNMENT], root=root, out=lines.append)

    assert exit_code == 0
    assert lines[0].startswith(f"{TEAM}: ok - report ")
    assert lines[-1] == "result: ready - 1 team(s) checked, no refusals"


def test_cli_exits_one_when_a_team_is_refused(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, TEAM, report_ns=BASE_NS, payload_ns=BASE_NS + ONE_SECOND_NS)
    lines: list[str] = []

    exit_code = run([ASSIGNMENT], root=root, out=lines.append)

    assert exit_code == 1
    assert lines[0].startswith(f"{TEAM}: refused - ")
    assert lines[-1] == "result: not ready - 1 of 1 team(s) refused"


def test_cli_exits_two_for_an_unknown_assignment(tmp_path: Path) -> None:
    lines: list[str] = []

    exit_code = run(["A9"], root=make_root(tmp_path), out=lines.append)

    assert exit_code == 2
    assert lines == ["ERROR: unknown assignment: A9; known: A1, A2, A3"]


def test_cli_exits_two_for_a_missing_feedback_directory(tmp_path: Path) -> None:
    lines: list[str] = []

    exit_code = run([ASSIGNMENT], root=tmp_path, out=lines.append)

    assert exit_code == 2
    assert lines[0].startswith("ERROR: missing feedback directory: ")
    assert lines[0].endswith(f"itpd-assignments-feedback/{ASSIGNMENT}/feedback")


def test_cli_passes_each_active_team_to_the_gate(tmp_path: Path) -> None:
    root = make_root(tmp_path)
    add_team(root, SEVEN_TEAMS[0], report_ns=BASE_NS + ONE_SECOND_NS, payload_ns=BASE_NS)
    add_team(root, SEVEN_TEAMS[1], report_ns=BASE_NS + ONE_SECOND_NS, payload_ns=BASE_NS)
    lines: list[str] = []

    exit_code = run(
        [ASSIGNMENT, "--active", SEVEN_TEAMS[0], "--active", SEVEN_TEAMS[1]],
        root=root,
        out=lines.append,
    )

    assert exit_code == 1
    assert lines[0] == f"{SEVEN_TEAMS[0]}: refused - grader still registered or running"
    assert lines[1] == f"{SEVEN_TEAMS[1]}: refused - grader still registered or running"
    assert lines[-1] == "result: not ready - 2 of 2 team(s) refused"


def test_cli_requires_an_assignment_argument() -> None:
    with pytest.raises(SystemExit):
        run([])


def test_unknown_assignment_raises_the_tool_error(tmp_path: Path) -> None:
    with pytest.raises(BatchReadyError, match="unknown assignment"):
        check_batch_ready("A9", make_root(tmp_path))

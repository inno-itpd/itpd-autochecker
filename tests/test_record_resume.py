from __future__ import annotations

from pathlib import Path

import pytest

from scripts.record_resume import BLOCKED_HINT, run
from tools.autochecker.grading_config import load_grading_config
from tools.autochecker.resume_state import FILENAME, read_state

TEAM = "Team 5 - TmpTeam_12345_assignsubmission_file"
CAP = load_grading_config().max_agent_resumes


def calls() -> tuple[list[str], list[str], dict]:
    out: list[str] = []
    err: list[str] = []
    return out, err, {"out": out.append, "err": err.append}


def test_first_attempt_is_recorded_and_resumable(tmp_path: Path) -> None:
    out, err, streams = calls()
    assert run(["A3", TEAM, "--work-root", str(tmp_path)], **streams) == 0
    assert out == [f"{TEAM}: resumes 1/{CAP} - resumable"]
    assert err == []
    assert (tmp_path / TEAM / FILENAME).exists()


def test_the_last_allowed_attempt_blocks_and_exits_one(tmp_path: Path) -> None:
    out, err, streams = calls()
    for attempt in range(1, CAP + 1):
        code = run(["A3", TEAM, "--work-root", str(tmp_path)], **streams)
        if attempt < CAP:
            assert code == 0
            assert out[-1] == f"{TEAM}: resumes {attempt}/{CAP} - resumable"
        else:
            assert code == 1
            assert out[-2:] == [f"{TEAM}: resumes {CAP}/{CAP} - blocked", f"{TEAM}: {BLOCKED_HINT}"]


def test_show_reads_without_writing(tmp_path: Path) -> None:
    out, _, streams = calls()
    assert run(["A3", TEAM, "--work-root", str(tmp_path), "--show"], **streams) == 0
    assert out == [f"{TEAM}: resumes 0/{CAP} - resumable"]
    assert not (tmp_path / TEAM / FILENAME).exists()


def test_done_clears_the_block_after_a_final_report(tmp_path: Path) -> None:
    for _ in range(CAP):
        run(["A3", TEAM, "--work-root", str(tmp_path)], out=lambda line: None)
    out, _, streams = calls()
    assert run(["A3", TEAM, "--work-root", str(tmp_path), "--done"], **streams) == 0
    assert out == [f"{TEAM}: resumes {CAP}/{CAP} - finished"]
    assert read_state(tmp_path / TEAM, CAP).blocked is False


def test_unknown_assignment_is_a_usage_error(tmp_path: Path) -> None:
    out, err, streams = calls()
    assert run(["A9", TEAM, "--work-root", str(tmp_path)], **streams) == 2
    assert out == []
    assert err == ["Error: unknown assignment A9"]


def test_show_and_done_are_mutually_exclusive(tmp_path: Path) -> None:
    with pytest.raises(SystemExit):
        run(["A3", TEAM, "--work-root", str(tmp_path), "--show", "--done"])

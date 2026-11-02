from __future__ import annotations

import json
from pathlib import Path

from tools.grader_tools.resume_state import (
    FILENAME,
    ResumeState,
    load_resume_states,
    mark_finished,
    read_state,
    record_attempt,
)

CAP = 4


def test_missing_count_file_reads_as_zero_and_resumable(tmp_path: Path) -> None:
    state = read_state(tmp_path, 4)
    assert state == ResumeState(0, 4, False)
    assert state.blocked is False
    assert state.line == "resumes 0/4 - resumable"


def test_broken_or_negative_counts_read_as_zero(tmp_path: Path) -> None:
    (tmp_path / "resume-count.json").write_text("{nope", encoding="utf-8")
    assert read_state(tmp_path, 4).attempts == 0
    (tmp_path / "resume-count.json").write_text('{"attempts": -2}', encoding="utf-8")
    assert read_state(tmp_path, 4).attempts == 0
    (tmp_path / "resume-count.json").write_text('{"attempts": "3"}', encoding="utf-8")
    assert read_state(tmp_path, 4).attempts == 0


def test_each_attempt_is_persisted(tmp_path: Path) -> None:
    assert record_attempt(tmp_path, 4).attempts == 1
    assert record_attempt(tmp_path, 4).attempts == 2
    assert read_state(tmp_path, 4).attempts == 2
    payload = json.loads((tmp_path / "resume-count.json").read_text(encoding="utf-8"))
    assert payload["finished"] is False
    assert payload["attempts"] == 2
    assert sorted(path.name for path in tmp_path.iterdir()) == ["resume-count.json"]


def test_the_cap_blocks_and_finishing_clears_the_block(tmp_path: Path) -> None:
    state = read_state(tmp_path, 0)
    assert state.blocked is True  # a zero cap is spent before the first resume

    for expected in range(1, CAP):
        state = record_attempt(tmp_path, CAP)
        assert state.blocked is False
    state = record_attempt(tmp_path, CAP)
    assert (state.attempts, state.blocked, state.state) == (CAP, True, "blocked")
    assert state.line == "resumes 4/4 - blocked"

    finished = mark_finished(tmp_path, CAP)
    assert (finished.attempts, finished.finished, finished.blocked) == (CAP, True, False)
    assert finished.line == "resumes 4/4 - finished"
    assert read_state(tmp_path, CAP).blocked is False


def test_finishing_keeps_the_attempts_for_the_record(tmp_path: Path) -> None:
    record_attempt(tmp_path, CAP)
    mark_finished(tmp_path, CAP)
    payload = json.loads((tmp_path / "resume-count.json").read_text(encoding="utf-8"))
    assert payload["attempts"] == 1
    assert payload["finished"] is True


def test_load_states_scans_only_teams_with_a_count_file(tmp_path: Path) -> None:
    (tmp_path / "Team 1_a").mkdir()
    record_attempt(tmp_path / "Team 1_a", CAP)
    (tmp_path / "Team 2_b").mkdir()  # a team without a count file is not blocked
    (tmp_path / "not-a-team.txt").write_text("x", encoding="utf-8")

    states = load_resume_states(tmp_path, CAP)
    assert list(states) == ["Team 1_a"]
    assert states["Team 1_a"] == ResumeState(1, CAP, False)


def test_missing_work_root_has_no_states(tmp_path: Path) -> None:
    assert load_resume_states(tmp_path / "missing", CAP) == {}


def test_a_finished_team_starts_a_new_episode_at_one(tmp_path: Path) -> None:
    for _ in range(CAP):
        record_attempt(tmp_path, CAP)
    mark_finished(tmp_path, CAP)
    state = record_attempt(tmp_path, CAP)
    assert (state.attempts, state.finished, state.blocked) == (1, False, False)

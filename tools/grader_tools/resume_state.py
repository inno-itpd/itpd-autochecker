"""Track the resume attempts spent on one team.

A grader that stops mid-batch is resumed with ``send_message`` at most
``max_agent_resumes`` times.  The count lives in
``work/<team_dir>/resume-count.json`` so the budget survives an orchestrator
restart, and ``scripts/record_resume.py`` is the only writer.  A team whose
budget is spent and whose report was never marked finished is blocked: the
extractor leaves it out of ``dev.md`` and the release CSV instead of shipping
the placeholder report it left behind.
"""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

FILENAME = "resume-count.json"


@dataclass(frozen=True)
class ResumeState:
    """How many resumes a team spent and whether it finished anyway."""

    attempts: int
    max_resumes: int
    finished: bool

    @property
    def blocked(self) -> bool:
        return not self.finished and self.attempts >= self.max_resumes

    @property
    def state(self) -> str:
        if self.finished:
            return "finished"
        return "blocked" if self.blocked else "resumable"

    @property
    def line(self) -> str:
        return f"resumes {self.attempts}/{self.max_resumes} - {self.state}"


def _decode(payload: object) -> tuple[int, bool]:
    if not isinstance(payload, dict):
        return 0, False
    attempts = payload.get("attempts")
    if isinstance(attempts, bool) or not isinstance(attempts, int) or attempts < 0:
        attempts = 0
    return attempts, payload.get("finished") is True


def read_state(work_dir: Path, max_resumes: int) -> ResumeState:
    """Read the team's count, treating a missing or broken file as zero."""
    try:
        payload = json.loads((Path(work_dir) / FILENAME).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ResumeState(0, max_resumes, False)
    attempts, finished = _decode(payload)
    return ResumeState(attempts, max_resumes, finished)


def _write(work_dir: Path, attempts: int, finished: bool) -> None:
    directory = Path(work_dir)
    directory.mkdir(parents=True, exist_ok=True)
    payload = {
        "attempts": attempts,
        "finished": finished,
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    handle, temporary = tempfile.mkstemp(dir=directory, prefix=".resume-count.", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            json.dump(payload, stream)
            stream.write("\n")
        os.replace(temporary, directory / FILENAME)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def record_attempt(work_dir: Path, max_resumes: int) -> ResumeState:
    """Count one more resume for the team.

    A finished team that fails again starts a new episode at one, so a later
    regrade does not inherit the previous episode's spent budget.
    """
    previous = read_state(work_dir, max_resumes)
    attempts = 1 if previous.finished else previous.attempts + 1
    _write(work_dir, attempts, False)
    return ResumeState(attempts, max_resumes, False)


def mark_finished(work_dir: Path, max_resumes: int) -> ResumeState:
    """Clear the block after a resume produced a final report."""
    previous = read_state(work_dir, max_resumes)
    _write(work_dir, previous.attempts, True)
    return ResumeState(previous.attempts, max_resumes, True)


def load_resume_states(work_root: Path, max_resumes: int) -> dict[str, ResumeState]:
    """Return the state of every team with a count file under `work_root`."""
    root = Path(work_root)
    if not root.is_dir():
        return {}
    states: dict[str, ResumeState] = {}
    for team_dir in sorted(root.iterdir()):
        if team_dir.is_dir() and (team_dir / FILENAME).exists():
            states[team_dir.name] = read_state(team_dir, max_resumes)
    return states

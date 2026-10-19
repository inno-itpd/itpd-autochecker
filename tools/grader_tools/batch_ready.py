"""Confirm that every team in an assignment has one finished report writer.

Extraction trusts ``itpd-assignments-feedback/<assignment>/feedback/<team_dir>/agent-feedback.md``,
so a batch must stop before extraction while a report is still being written.
Three signals decide that from what is on disk and from what the harness reports:

- a non-empty ``work/<team_dir>/`` with no report means a writer started and
  stopped before it wrote one;
- ``work/<team_dir>/payload.json`` with an mtime newer than the report's means
  the report was not rendered after the last payload update, so the report is
  half-rendered: the signature of an interrupted render or of a second writer
  that overwrote the payload after the first one rendered; equal mtimes are
  fine, because a render writes the report after it writes the payload;
- a team listed as active still has a grader registered or running.

This module cannot call ``list_agents``, so the harness registry arrives on
``scripts/check_batch_ready.py --active <team_dir>`` and is passed to
:func:`check_batch_ready` as ``active``.

``scripts/check_batch_ready.py`` prints one line per team, showing both mtimes
for an OK team and the refusal reason otherwise, then a final ready or
not-ready line; the exit code is 0 when ready, 1 when any team is refused, and
2 when the check cannot run.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT

FEEDBACK_FILENAME = "agent-feedback.md"
PAYLOAD_FILENAME = "payload.json"

ACTIVE_REASON = "grader still registered or running"


class BatchReadyError(RuntimeError):
    """The assignment is unknown or its feedback directory cannot be read."""


@dataclass(frozen=True)
class TeamStatus:
    """One team's report and payload mtimes, or the reason it is refused."""

    team: str
    report_mtime_ns: int | None
    payload_mtime_ns: int | None
    reason: str | None

    @property
    def ok(self) -> bool:
        return self.reason is None

    @property
    def line(self) -> str:
        if self.reason is not None:
            return f"{self.team}: refused - {self.reason}"
        return (
            f"{self.team}: ok - report {_mtime_text(self.report_mtime_ns)}, "
            f"payload {_mtime_text(self.payload_mtime_ns)}"
        )


@dataclass(frozen=True)
class BatchReadyResult:
    assignment: str
    teams: tuple[TeamStatus, ...]
    summary_lines: tuple[str, ...]

    @property
    def has_refusals(self) -> bool:
        return any(not status.ok for status in self.teams)

    @property
    def refused(self) -> tuple[TeamStatus, ...]:
        return tuple(status for status in self.teams if not status.ok)


def format_mtime(ns: int) -> str:
    """Render one ``st_mtime_ns`` as local ISO 8601 with its UTC offset."""
    return datetime.fromtimestamp(ns / 1_000_000_000, tz=timezone.utc).astimezone().isoformat(
        timespec="seconds"
    )


def _mtime_text(ns: int | None) -> str:
    return "missing" if ns is None else format_mtime(ns)


def normalize_team_dir(value: str) -> str:
    """Reduce an ``--active`` value to a team directory name.

    The option accepts a bare team directory as ``list_agents`` reports it, and
    also tolerates a path or a trailing separator so an operator can paste a
    work directory path without retyping the name.
    """
    text = value.strip()
    if not text:
        return ""
    return PurePosixPath(text.replace("\\", "/")).name


def _entries(directory: Path) -> tuple[Path, ...]:
    if not directory.is_dir():
        return ()
    try:
        return tuple(sorted(directory.iterdir(), key=lambda entry: entry.name))
    except OSError as exc:
        raise BatchReadyError(f"cannot list {directory}: {exc}") from exc


def _file_mtime_ns(path: Path) -> int | None:
    try:
        if not path.is_file():
            return None
        return path.stat().st_mtime_ns
    except OSError as exc:
        raise BatchReadyError(f"cannot stat {path}: {exc}") from exc


def _work_dir_has_a_writer(work_dir: Path) -> bool:
    """A non-empty work directory means a writer already touched it.

    An empty directory with no report and no payload is a leftover from a run
    that never started any tooling, so it is not part of the batch.
    """
    return bool(_entries(work_dir))


def _team_names(feedback_dir: Path, work_root: Path) -> set[str]:
    teams = {
        entry.name
        for entry in _entries(feedback_dir)
        if entry.is_dir() and (entry / FEEDBACK_FILENAME).is_file()
    }
    for entry in _entries(work_root):
        if entry.is_dir() and _work_dir_has_a_writer(entry):
            teams.add(entry.name)
    return teams


def _refusal_reason(
    report_mtime_ns: int | None,
    payload_mtime_ns: int | None,
    active: set[str],
    team: str,
) -> str | None:
    if team in active:
        return ACTIVE_REASON
    if report_mtime_ns is None:
        return (
            f"work directory exists but {FEEDBACK_FILENAME} is missing "
            "(a writer started and never wrote a report)"
        )
    if payload_mtime_ns is not None and payload_mtime_ns > report_mtime_ns:
        return (
            f"{PAYLOAD_FILENAME} is newer than the report; the report was not rendered after the "
            "last payload update (an interrupted or duplicate writer)"
        )
    return None


def check_batch_ready(
    assignment: str,
    root: Path = Path("."),
    *,
    active: Iterable[str] = (),
) -> BatchReadyResult:
    """Check one assignment's batch and shape the one-line-per-team report."""
    if assignment not in ASSIGNMENT_CONFIG:
        raise BatchReadyError(
            f"unknown assignment: {assignment}; known: {', '.join(sorted(ASSIGNMENT_CONFIG))}"
        )
    assignment_root = root / FEEDBACK_ROOT / assignment
    feedback_dir = assignment_root / "feedback"
    work_root = assignment_root / "work"
    if not feedback_dir.is_dir():
        raise BatchReadyError(f"missing feedback directory: {feedback_dir}")
    active_teams = {team for team in map(normalize_team_dir, active) if team}
    teams = sorted(_team_names(feedback_dir, work_root) | active_teams)
    statuses = []
    for team in teams:
        work_dir = work_root / team
        report_mtime_ns = _file_mtime_ns(feedback_dir / team / FEEDBACK_FILENAME)
        payload_mtime_ns = _file_mtime_ns(work_dir / PAYLOAD_FILENAME)
        reason = _refusal_reason(report_mtime_ns, payload_mtime_ns, active_teams, team)
        statuses.append(TeamStatus(team, report_mtime_ns, payload_mtime_ns, reason))
    refused = sum(1 for status in statuses if not status.ok)
    lines = [status.line for status in statuses]
    if refused:
        lines.append(f"result: not ready - {refused} of {len(statuses)} team(s) refused")
    else:
        lines.append(f"result: ready - {len(statuses)} team(s) checked, no refusals")
    return BatchReadyResult(assignment, tuple(statuses), tuple(lines))

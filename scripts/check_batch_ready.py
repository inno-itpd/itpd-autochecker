#!/usr/bin/env python3
"""Refuse extraction while a team still has a running grader or a half-rendered report.

The gate lists every team in ``itpd-assignments-feedback/<assignment>/`` from
its feedback report and its ``work/<team_dir>/``, prints one line per team, and
refuses the batch when:

- ``list_agents`` still reports a grader for the team; pass each one on
  ``--active <team_dir>``, because this script cannot call ``list_agents``
  itself and the harness registry has to come from the orchestrator;
- a non-empty work directory has no ``agent-feedback.md``, so a writer started
  and never wrote a report;
- ``work/<team_dir>/payload.json`` is newer than the report, because the report
  was not rendered after the last payload update; that mtime ordering is the
  signature of an interrupted render or of a second writer for the same team,
  and equal mtimes are fine.

The exit code is 0 when the batch is ready, 1 when any team is refused, and 2
when the check cannot run, for example for an unknown assignment or a missing
feedback directory.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.batch_ready import BatchReadyError, check_batch_ready


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Check that every team in an assignment has one finished report writer before "
            "extraction. Refuses a team the harness still reports as active, a work directory "
            "with no report, and a report older than its payload. Exit code 0 ready, 1 not "
            "ready, 2 usage error."
        )
    )
    parser.add_argument("assignment", metavar="A<N>", help="Assignment directory, for example A3")
    parser.add_argument(
        "--active",
        metavar="TEAM_DIR",
        action="append",
        default=[],
        help=(
            "Team directory that list_agents still reports as running or registered; repeat "
            "the option for each one"
        ),
    )
    return parser


def run(
    argv: Sequence[str],
    *,
    root: Path = ROOT,
    out: Callable[[str], None] = print,
) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = check_batch_ready(args.assignment, root, active=args.active)
    except BatchReadyError as exc:
        out(f"ERROR: {exc}")
        return 2
    for line in result.summary_lines:
        out(line)
    return 1 if result.has_refusals else 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

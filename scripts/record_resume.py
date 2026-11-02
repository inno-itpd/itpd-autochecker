#!/usr/bin/env python3
"""Count a team's resume attempts against the budget in grading.json.

Run this before every ``send_message`` resume of a grader session so the count
survives an orchestrator restart and the extractor can recognize a blocked
team.  ``--show`` prints the state without writing, and ``--done`` clears the
block once a resume produced the final report.

The exit code is 0 while the team is resumable or finished and 1 when the
budget is spent, which is the point to stop resuming and report the team as
blocked; 2 means the invocation or the assignment is invalid.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG, FEEDBACK_ROOT
from tools.grader_tools.grading_config import load_grading_config
from tools.grader_tools.resume_state import ResumeState, mark_finished, read_state, record_attempt

BLOCKED_HINT = "stop resuming and report the team as blocked"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Record one resume attempt for a team, show its budget, or mark it "
            "finished. Run this before every send_message resume."
        )
    )
    parser.add_argument("assignment", help="Assignment directory, for example A3")
    parser.add_argument("team_dir", help="Exact submission directory name, including spaces and parentheses")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--show", action="store_true", help="Print the state without recording an attempt")
    action.add_argument("--done", action="store_true", help="Mark the team finished and clear the block")
    parser.add_argument("--work-root", help=f"Override the work root (default: {FEEDBACK_ROOT}/<assignment>/work)")
    return parser


def work_root_for(assignment: str, override: str | None) -> Path:
    if override:
        return Path(override)
    return Path(FEEDBACK_ROOT) / assignment / "work"


def run(
    argv: Sequence[str],
    *,
    out: Callable[[str], None] = print,
    err: Callable[[str], None] = lambda line: print(line, file=sys.stderr),
) -> int:
    args = build_parser().parse_args(argv)
    if args.assignment not in ASSIGNMENT_CONFIG:
        err(f"Error: unknown assignment {args.assignment}")
        return 2

    work_dir = work_root_for(args.assignment, args.work_root) / args.team_dir
    max_resumes = load_grading_config().max_agent_resumes
    if args.done:
        state: ResumeState = mark_finished(work_dir, max_resumes)
    elif args.show:
        state = read_state(work_dir, max_resumes)
    else:
        state = record_attempt(work_dir, max_resumes)

    out(f"{args.team_dir}: {state.line}")
    if state.blocked:
        out(f"{args.team_dir}: {BLOCKED_HINT}")
        return 1
    return 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

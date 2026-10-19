#!/usr/bin/env python3
"""Scan a fetched snapshot or one feedback report for private-only material.

Findings are grouped by rule and printed as a path plus a kind; matched values
never reach stdout.  With ``--feedback --no-snapshot`` the report is scanned
with tokens derived from the submission PDF, so a cleaned ``work/<team_dir>/``
does not block the gate.  The exit code is 0 when the scan is clean, 1 when it
has findings, and 2 when the scan could not run.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.privacy_scan import PrivacyScanError, scan_privacy


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Scan the fetched snapshot for emails, phone numbers, env and key files, "
            "recording links outside meeting artifacts, and PDF member name tokens. "
            "With --feedback, scan that report file with the same rules instead."
        )
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    parser.add_argument(
        "--feedback",
        metavar="PATH",
        help="Scan this finished report file instead of the fetched snapshot",
    )
    parser.add_argument(
        "--no-snapshot",
        action="store_true",
        help=(
            "With --feedback, derive the privacy tokens from the submission PDF instead of "
            "work/<team_dir>/pdf-info.json, so a cleaned work directory does not block the scan"
        ),
    )
    return parser


def run(argv: Sequence[str], *, root: Path = ROOT, out: Callable[[str], None] = print) -> int:
    args = build_parser().parse_args(argv)
    if args.no_snapshot and not args.feedback:
        out(
            "ERROR: --no-snapshot requires --feedback <path>; the report scan needs the submission PDF "
            "for its privacy tokens"
        )
        return 2
    try:
        result = scan_privacy(
            args.assignment,
            args.team_dir,
            root,
            feedback_path=Path(args.feedback) if args.feedback else None,
            no_snapshot=args.no_snapshot,
        )
    except PrivacyScanError as exc:
        out(f"ERROR: {exc}")
        return 2
    for line in result.summary_lines:
        out(line)
    return 1 if result.has_findings else 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

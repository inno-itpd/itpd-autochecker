#!/usr/bin/env python3
"""Dump the live GitHub evidence for one submission into its work directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.live_evidence import LiveEvidenceError, collect_github_evidence


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Collect labels, issues, pull requests, runs, and commits for one team into "
            "itpd-assignments-feedback/<assignment>/work/<team_dir>/ and print a compact summary."
        )
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    parser.add_argument(
        "--issues",
        type=int,
        nargs="+",
        default=[],
        metavar="N",
        help="Issue numbers to drill into: comments, timeline, and edit history",
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        default=[],
        metavar="PATH",
        help="Repository paths, from the repository root, to fetch commit histories for",
    )
    args = parser.parse_args()

    try:
        result = collect_github_evidence(
            args.assignment,
            args.team_dir,
            root=ROOT,
            issues=args.issues,
            paths=args.paths,
        )
    except LiveEvidenceError as exc:
        raise SystemExit(f"ERROR: {exc}") from exc
    print("\n".join(result.summary_lines))


if __name__ == "__main__":
    main()

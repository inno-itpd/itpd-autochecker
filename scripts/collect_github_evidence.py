#!/usr/bin/env python3
"""Dump the live GitHub evidence for one submission into its work directory."""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.live_evidence import LiveEvidenceError, LiveEvidenceResult, collect_github_evidence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Collect labels, issues, pull requests, runs, and commits for one team into "
            "itpd-assignments-feedback/<assignment>/work/<team_dir>/ and print a compact summary. "
            "A submission with no resolvable snapshot is a judged outcome: the script prints "
            "'result: skipped (no snapshot)' and exits 0."
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
    return parser


def run(
    argv: Sequence[str],
    *,
    root: Path = ROOT,
    out: Callable[[str], None] = print,
    collect: Callable[..., LiveEvidenceResult] = collect_github_evidence,
) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = collect(
            args.assignment,
            args.team_dir,
            root=root,
            issues=args.issues,
            paths=args.paths,
        )
    except LiveEvidenceError as exc:
        out(f"ERROR: {exc}")
        return 2
    for line in result.summary_lines:
        out(line)
    return 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

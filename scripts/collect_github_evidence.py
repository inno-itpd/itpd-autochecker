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
from tools.grader_tools.evidence_sqlite import (
    EvidenceDatabaseError,
    write_evidence_database,
)
from tools.grader_tools.live_evidence import (
    LiveEvidenceError,
    LiveEvidenceResult,
    collect_github_evidence,
    regenerate_evidence_summary,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Collect labels, issues, pull requests, runs, commits, milestones, releases, and tags for "
            "one team into itpd-assignments-feedback/<assignment>/work/<team_dir>/, write a bounded "
            "summary.md digest and an evidence.sqlite projection, and print a compact summary. A "
            "submission with no resolvable snapshot is a judged outcome: the script prints 'result: "
            "skipped (no snapshot)' and exits 0. With --issue-fields it instead writes issue-fields.json, "
            "one row per issue with its type, milestone, assignees, and field values, from one paginated "
            "REST list call; that mode is not combined with --summary, --issues, or --paths. With "
            "--summary it rebuilds and prints the digest and evidence.sqlite from the saved dumps and "
            "never calls gh."
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
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--issue-fields",
        action="store_true",
        help=(
            "Write issue-fields.json: one row per issue with its type, milestone, assignees, and field "
            "values from one paginated REST list call, skipping pull requests; does not rewrite the "
            "other dumps, then rebuild evidence.sqlite from the saved dumps"
        ),
    )
    mode.add_argument(
        "--summary",
        action="store_true",
        help=(
            "Rebuild summary.md and evidence.sqlite from the dumps already in the team work directory "
            "and print the digest; never calls gh"
        ),
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
    if args.summary:
        try:
            summary_path, digest = regenerate_evidence_summary(args.assignment, args.team_dir, root=root)
            database = write_evidence_database(summary_path.parent)
        except (LiveEvidenceError, EvidenceDatabaseError) as exc:
            out(f"ERROR: {exc}")
            return 2
        for line in digest.splitlines():
            out(line)
        out(database.summary_line(root))
        return 0
    if args.issue_fields and (args.issues or args.paths):
        out("ERROR: --issue-fields cannot be combined with --issues or --paths")
        return 2
    try:
        result = collect(
            args.assignment,
            args.team_dir,
            root=root,
            issues=args.issues,
            paths=args.paths,
            issue_fields=args.issue_fields,
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

#!/usr/bin/env python3
"""Check relative links and heading anchors in a fetched snapshot's Markdown.

Findings are grouped as broken relative links, missing anchors, and pre-cut
research anchors, and each line names the file, the line, and the target.  The
exit code is 0 when the check is clean, 1 when it has findings, and 2 when it
cannot run.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.snapshot_links import SnapshotLinksError, check_snapshot_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Walk the Markdown in a fetched snapshot and check every relative link, "
            "every heading anchor, and every pre-cut #(alt|gap|vp)-NN- anchor. "
            "With --issue-bodies, check the anchors in a dumped issues.json too."
        )
    )
    parser.add_argument(
        "snapshot_dir",
        help="Fetched snapshot directory, for example itpd-assignments-feedback/A2/work/<team_dir>/snapshot",
    )
    parser.add_argument(
        "--issue-bodies",
        metavar="PATH",
        help="Dumped issues.json whose bodies' anchors are checked against the snapshot headings",
    )
    return parser


def run(argv: Sequence[str], *, out: Callable[[str], None] = print) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = check_snapshot_links(
            Path(args.snapshot_dir),
            issue_bodies_path=Path(args.issue_bodies) if args.issue_bodies else None,
        )
    except SnapshotLinksError as exc:
        out(f"ERROR: {exc}")
        return 2
    for line in result.summary_lines:
        out(line)
    return 1 if result.has_findings else 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

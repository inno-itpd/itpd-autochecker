#!/usr/bin/env python3
"""Write a bounded inventory digest of a fetched snapshot into a team work directory.

The digest lists the snapshot's root files, the ``QR-nn``, ``FR-nnn``, and
``ADR-nnn`` counts, the ``docs/`` and ``reports/`` trees, the workflow names, and
the site-config candidates, so a grader reads one short file instead of walking
the tree.  It prints counts and the path only.  The exit code is 0 when the
digest was written and 2 when it could not be, for example when the snapshot has
not been fetched yet.
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
from tools.grader_tools.snapshot_inventory import SnapshotInventoryError, write_inventory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Write work/<team_dir>/inventory.md from the snapshot fetched there: "
            "the root files, the QR/FR/ADR counts, the docs/ and reports/ trees, "
            "the workflow names, and the site-config candidates."
        )
    )
    parser.add_argument("assignment", help="Assignment directory, for example A4")
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    parser.add_argument(
        "--snapshot",
        metavar="DIR",
        help="Snapshot directory to read, defaulting to work/<team_dir>/snapshot",
    )
    parser.add_argument(
        "--output",
        metavar="PATH",
        help="File to write, defaulting to work/<team_dir>/inventory.md",
    )
    return parser


def run(argv: Sequence[str], *, out: Callable[[str], None] = print) -> int:
    args = build_parser().parse_args(argv)
    if args.assignment not in ASSIGNMENT_CONFIG:
        out(f"ERROR: unknown assignment {args.assignment!r}; known: {', '.join(sorted(ASSIGNMENT_CONFIG))}")
        return 2
    try:
        inventory = write_inventory(
            ROOT,
            args.assignment,
            args.team_dir,
            snapshot_dir=Path(args.snapshot) if args.snapshot else None,
            output_path=Path(args.output) if args.output else None,
        )
    except SnapshotInventoryError as exc:
        out(f"ERROR: {exc}")
        return 2
    out(f"{args.assignment} / {args.team_dir}")
    for line in inventory.summary_lines:
        out(f"  {line}")
    return 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Fetch the snapshot at a submission PDF's permalink SHA and record the PDF metadata."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.submission_pdf import (
    SnapshotFetchError,
    SubmissionPdfError,
    fetch_team_snapshot,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract the PDF permalink metadata and fetch the GitHub snapshot into work/<team_dir>/."
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    args = parser.parse_args()

    try:
        result = fetch_team_snapshot(args.assignment, args.team_dir, root=ROOT)
    except (SubmissionPdfError, SnapshotFetchError) as exc:
        raise SystemExit(f"ERROR: {exc}") from exc
    print("\n".join(result.summary_lines))


if __name__ == "__main__":
    main()

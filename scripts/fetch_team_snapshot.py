#!/usr/bin/env python3
"""Fetch the snapshot at a submission PDF's permalink SHA and record the PDF metadata.

A PDF that carries only a bare 40-character SHA and no repository URL is
resolved with `gh search commits`; pass `--repo org/repo` to pair that SHA with
a repository by hand instead, for example when the search is ambiguous.

When the permalink points at a different week than the assignment expects, the
fetcher prints a `warn:` line, writes the same warning to the team's
`summary.md`, skips the commit check and the snapshot fetch, and exits 1.
Pass `--permalink <url>` with the right full GitHub permalink to continue.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.submission_pdf import (
    REPO_FULL_PATTERN,
    SnapshotFetchError,
    SubmissionPdfError,
    fetch_team_snapshot,
)


def _repo_argument(value: str) -> str:
    if not REPO_FULL_PATTERN.fullmatch(value):
        raise argparse.ArgumentTypeError(f"expected org/repo, got {value!r}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract the PDF permalink metadata and fetch the GitHub snapshot into work/<team_dir>/snapshot/."
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    parser.add_argument(
        "--repo",
        type=_repo_argument,
        metavar="ORG/REPO",
        help=(
            "Pair the PDF's bare SHA with this repository when the PDF names none, recorded as "
            "permalink_source=operator. Ignored, with a note, when the PDF names its own repository "
            "or --permalink supplies one."
        ),
    )
    parser.add_argument(
        "--permalink",
        metavar="URL",
        help=(
            "Replace the PDF permalink with a full GitHub blob URL "
            "(https://github.com/<org>/<repo>/blob/<40-character-sha>/reports/week-NN/README.md), "
            "recorded as permalink_source=operator. Use it to supply the right week after a "
            "week mismatch; a malformed URL or SHA is an error."
        ),
    )
    return parser


def run(argv: list[str], *, root: Path = ROOT) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = fetch_team_snapshot(
            args.assignment,
            args.team_dir,
            root=root,
            repo=args.repo,
            permalink=args.permalink,
        )
    except (SubmissionPdfError, SnapshotFetchError) as exc:
        print(f"ERROR: {exc}")
        return 2
    print("\n".join(result.summary_lines))
    return 1 if result.week_mismatch else 0


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

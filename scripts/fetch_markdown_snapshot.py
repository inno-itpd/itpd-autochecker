#!/usr/bin/env python3
"""Fetch the snapshot at a Markdown submission wrapper's permalink SHA.

A team occasionally submits the Moodle wrapper as Markdown instead of a PDF.
This helper reads the same facts from that file, writes the canonical
``pdf-info.json`` in the team's work directory, and fetches the snapshot, so the
evidence collector and the privacy scan run unchanged.

Pass ``--permalink`` when the Markdown names the wrong week, and ``--repo`` when
it carries only a bare SHA and no repository URL.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.markdown_submission import fetch_markdown_submission
from tools.grader_tools.submission_pdf import (
    REPO_FULL_PATTERN,
    SnapshotFetchError,
    SubmissionPdfError,
)


def _repo_argument(value: str) -> str:
    if not REPO_FULL_PATTERN.fullmatch(value):
        raise argparse.ArgumentTypeError(f"expected org/repo, got {value!r}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Read a Markdown submission wrapper, write work/<team_dir>/pdf-info.json, "
            "and fetch the GitHub snapshot into work/<team_dir>/snapshot/."
        )
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("team_dir", help="Submission directory name under submissions/")
    parser.add_argument(
        "--repo",
        type=_repo_argument,
        metavar="ORG/REPO",
        help=(
            "Pair the Markdown's bare SHA with this repository when it names none, "
            "recorded as permalink_source=operator."
        ),
    )
    parser.add_argument(
        "--permalink",
        metavar="URL",
        help=(
            "Replace the Markdown permalink with a full GitHub blob URL "
            "(https://github.com/<org>/<repo>/blob/<40-character-sha>/reports/week-NN/README.md), "
            "recorded as permalink_source=operator. Use it to supply the right week after a "
            "week mismatch; a malformed URL or SHA is an error."
        ),
    )
    return parser


def run(argv: list[str], *, root: Path = ROOT) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = fetch_markdown_submission(
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

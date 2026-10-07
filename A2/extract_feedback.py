#!/usr/bin/env python3
"""Extract Assignment 2 feedback reports into dev.md and the release CSV."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.extract_reports import build_parser, run_extraction


ASSIGNMENT = "A2"


def main() -> None:
    args = build_parser(ASSIGNMENT).parse_args()
    raise SystemExit(run_extraction(ASSIGNMENT, Path(args.input), Path(args.dev_output), Path(args.release_output)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check gh authentication, pdftotext, and markdownlint-cli2 before a grader batch.

Each required tool is reported with an ok or FAIL line, and gh additionally
reports whether it is authenticated.  The exit code is 0 when every check
passes and 1 when any check fails.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.preflight import PreflightResult, run_preflight


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Report whether gh is authenticated and whether pdftotext and "
            "markdownlint-cli2 are on PATH. Run this before a grader batch; "
            "the exit code is non-zero when a check fails."
        )
    )
    return parser


def run(
    argv: Sequence[str],
    *,
    out: Callable[[str], None] = print,
    check: Callable[[], PreflightResult] = run_preflight,
) -> int:
    build_parser().parse_args(argv)
    result = check()
    for line in result.summary_lines:
        out(line)
    return 0 if result.ok else 1


def main() -> None:
    raise SystemExit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()

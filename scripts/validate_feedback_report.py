#!/usr/bin/env python3
"""Validate one feedback.md report against the shared report contract."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.validate import validate_feedback_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate one feedback.md report.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to feedback.md")
    args = parser.parse_args()

    feedback_path = Path(args.feedback_path)
    errors = validate_feedback_file(args.assignment, feedback_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"OK: {feedback_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run the report contract validator and markdownlint-cli2 on one agent-feedback.md."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.grader_tools.assignment_config import ASSIGNMENT_CONFIG
from tools.grader_tools.validate import validate_feedback_file

LINTER = "markdownlint-cli2"


def lint_errors(feedback_path: Path) -> list[str]:
    linter = shutil.which(LINTER)
    if linter is None:
        return [f"{LINTER} not found on PATH; run this check inside the project dev shell (`nix develop`, or `direnv allow` once), which provides it"]
    result = subprocess.run([linter, str(feedback_path)], cwd=ROOT)
    if result.returncode != 0:
        return [f"{LINTER} found problems in {feedback_path} (exit code {result.returncode})"]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate one agent-feedback.md report and lint it with markdownlint-cli2.")
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to agent-feedback.md")
    args = parser.parse_args()

    feedback_path = Path(args.feedback_path).resolve()
    if not feedback_path.is_file():
        print(f"ERROR: {feedback_path} does not exist")
        raise SystemExit(1)

    failures = [f"report validation: {error}" for error in validate_feedback_file(args.assignment, feedback_path)]
    failures.extend(f"markdownlint: {error}" for error in lint_errors(feedback_path))
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print(f"OK: {feedback_path} passes report validation and {LINTER}")


if __name__ == "__main__":
    main()

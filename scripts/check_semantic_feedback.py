#!/usr/bin/env python3
"""Validate one agent-semantic-feedback.md and lint it with markdownlint-cli2."""

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
from tools.grader_tools.semantic_feedback import default_report_path, validate_semantic_feedback

LINTER = "markdownlint-cli2"


def lint_errors(feedback_path: Path) -> list[str]:
    linter = shutil.which(LINTER)
    if linter is None:
        return [
            f"{LINTER} not found on PATH; run this check inside the dev shell "
            "(`nix develop`, or `direnv allow` once), which provides it"
        ]
    result = subprocess.run([linter, str(feedback_path)], cwd=ROOT)
    if result.returncode != 0:
        return [f"{LINTER} found problems in {feedback_path} (exit code {result.returncode})"]
    return []


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate one agent-semantic-feedback.md against docs/semantic-feedback-format.md and lint it."
    )
    parser.add_argument("assignment", choices=sorted(ASSIGNMENT_CONFIG))
    parser.add_argument("feedback_path", help="Path to agent-semantic-feedback.md")
    parser.add_argument(
        "--report",
        help="Path to the structural agent-feedback.md; defaults to the sibling file",
    )
    parser.add_argument(
        "--no-report-check",
        action="store_true",
        help="Skip the team, repository, and snapshot comparison with agent-feedback.md",
    )
    args = parser.parse_args()

    feedback_path = Path(args.feedback_path).resolve()
    if not feedback_path.is_file():
        print(f"ERROR: {feedback_path} does not exist")
        raise SystemExit(1)

    report_text: str | None = None
    if not args.no_report_check:
        report_path = Path(args.report).resolve() if args.report else default_report_path(feedback_path)
        if not report_path.is_file():
            print(f"ERROR: {report_path} does not exist; pass --no-report-check to validate the file alone")
            raise SystemExit(1)
        report_text = report_path.read_text(encoding="utf-8")

    failures = [
        f"semantic feedback validation: {error}"
        for error in validate_semantic_feedback(
            feedback_path.read_text(encoding="utf-8"),
            args.assignment,
            report_text=report_text,
        )
    ]
    failures.extend(f"markdownlint: {error}" for error in lint_errors(feedback_path))
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        raise SystemExit(1)
    print(f"OK: {feedback_path} passes semantic feedback validation and {LINTER}")


if __name__ == "__main__":
    main()

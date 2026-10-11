from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

from tests.conftest import ROOT
from tests.report_builder import build_report


def run_check(tmp_path: Path, feedback: Path, linter_exit: int | None) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    if linter_exit is None:
        empty_bin = tmp_path / "empty-bin"
        empty_bin.mkdir(exist_ok=True)
        env["PATH"] = str(empty_bin)
    else:
        bin_dir = tmp_path / "bin"
        bin_dir.mkdir(exist_ok=True)
        linter = bin_dir / "markdownlint-cli2"
        linter.write_text(f"#!{sys.executable}\nimport sys\nsys.exit({linter_exit})\n", encoding="utf-8")
        linter.chmod(0o755)
        env["PATH"] = f"{bin_dir}{os.pathsep}{env.get('PATH', '')}"
    return subprocess.run(
        [sys.executable, "scripts/check_feedback_report.py", "A1", str(feedback)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


def test_check_passes_valid_report(tmp_path: Path) -> None:
    feedback = tmp_path / "feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    result = run_check(tmp_path, feedback, linter_exit=0)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "passes report validation and markdownlint-cli2" in result.stdout


def test_check_fails_invalid_report_and_still_lints(tmp_path: Path) -> None:
    feedback = tmp_path / "feedback.md"
    feedback.write_text(build_report("A1").replace("## Summary", "## Wrong", 1), encoding="utf-8")
    result = run_check(tmp_path, feedback, linter_exit=0)
    assert result.returncode != 0
    assert result.stdout.startswith("ERROR: report validation:")


def test_check_fails_on_lint_findings(tmp_path: Path) -> None:
    feedback = tmp_path / "feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    result = run_check(tmp_path, feedback, linter_exit=1)
    assert result.returncode != 0
    assert "ERROR: markdownlint: markdownlint-cli2 found problems" in result.stdout


def test_check_reports_missing_linter_without_traceback(tmp_path: Path) -> None:
    feedback = tmp_path / "feedback.md"
    feedback.write_text(build_report("A1"), encoding="utf-8")
    result = run_check(tmp_path, feedback, linter_exit=None)
    assert result.returncode != 0
    assert "ERROR: markdownlint: markdownlint-cli2 not found on PATH" in result.stdout
    assert "Traceback" not in result.stdout + result.stderr


def test_check_reports_missing_report_without_traceback(tmp_path: Path) -> None:
    result = run_check(tmp_path, tmp_path / "missing.md", linter_exit=0)
    assert result.returncode != 0
    assert "does not exist" in result.stdout
    assert "Traceback" not in result.stdout + result.stderr

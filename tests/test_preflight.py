from __future__ import annotations

import subprocess
from types import SimpleNamespace

import pytest

from scripts.preflight import run
from tools.grader_tools.preflight import (
    PreflightCheck,
    PreflightResult,
    check_gh_auth,
    check_tool,
    run_preflight,
)

ALL_TOOLS = {"gh", "pdftotext", "markdownlint-cli2"}


def which_from(present: set[str]):
    def which(name: str) -> str | None:
        return f"/nix/store/bin/{name}" if name in present else None

    return which


def runner_returning(returncode: int, calls: list[list[str]] | None = None):
    def runner(argv, **kwargs):
        if calls is not None:
            calls.append(argv)
        return SimpleNamespace(returncode=returncode)

    return runner


def test_run_preflight_shapes_three_checks_when_ready() -> None:
    result = run_preflight(which_from(ALL_TOOLS), runner_returning(0))
    assert result.ok is True
    assert [check.name for check in result.checks] == ["gh auth", "pdftotext", "markdownlint-cli2"]
    assert result.failures == ()
    assert result.summary_lines[0] == "gh auth: ok - authenticated"
    assert result.summary_lines[1] == "pdftotext: ok - /nix/store/bin/pdftotext"
    assert result.summary_lines[-1] == "result: ready - all 3 checks passed"


def test_missing_tool_reports_failure_and_a_path_hint() -> None:
    result = run_preflight(which_from({"gh", "pdftotext"}), runner_returning(0))
    assert result.ok is False
    assert [check.name for check in result.failures] == ["markdownlint-cli2"]
    assert "PATH" in result.failures[0].detail
    assert result.summary_lines[-1] == "result: not ready - 1 of 3 check(s) failed"


def test_missing_gh_is_reported_without_calling_the_runner() -> None:
    calls: list[list[str]] = []
    result = run_preflight(which_from({"pdftotext", "markdownlint-cli2"}), runner_returning(0, calls))
    assert calls == []
    assert result.failures[0].name == "gh auth"
    assert "gh not found" in result.failures[0].detail


def test_unauthenticated_gh_fails_only_the_gh_check() -> None:
    result = run_preflight(which_from(ALL_TOOLS), runner_returning(1))
    assert result.ok is False
    assert result.checks[0].ok is False
    assert "gh auth login" in result.checks[0].detail
    assert result.checks[1].ok is True
    assert result.checks[2].ok is True


def test_gh_auth_timeout_and_oserror_are_reported() -> None:
    def timeout_runner(argv, **kwargs):
        raise subprocess.TimeoutExpired(argv, timeout=1)

    timed_out = check_gh_auth(which_from(ALL_TOOLS), timeout_runner)
    assert timed_out.ok is False
    assert "timed out" in timed_out.detail

    def broken_runner(argv, **kwargs):
        raise OSError("permission denied")

    broken = check_gh_auth(which_from(ALL_TOOLS), broken_runner)
    assert broken.ok is False
    assert "permission denied" in broken.detail


def test_check_tool_reports_the_resolved_path() -> None:
    found = check_tool("pdftotext", which_from({"pdftotext"}))
    assert (found.ok, found.detail) == (True, "/nix/store/bin/pdftotext")
    missing = check_tool("pdftotext", which_from(set()))
    assert missing.ok is False


def test_run_prints_result_and_returns_exit_code() -> None:
    ready = PreflightResult(
        (PreflightCheck("gh auth", True, "authenticated"),),
        ("gh auth: ok - authenticated", "result: ready - all 1 checks passed"),
    )
    lines: list[str] = []
    assert run([], out=lines.append, check=lambda: ready) == 0
    assert lines == list(ready.summary_lines)

    blocked = PreflightResult(
        (PreflightCheck("gh auth", False, "not authenticated; run: gh auth login"),),
        ("gh auth: FAIL - not authenticated; run: gh auth login", "result: not ready - 1 of 1 check(s) failed"),
    )
    lines = []
    assert run([], out=lines.append, check=lambda: blocked) == 1
    assert lines == list(blocked.summary_lines)


def test_run_rejects_unknown_arguments() -> None:
    with pytest.raises(SystemExit):
        run(["--bogus"], check=lambda: None)

"""Check the tools a grader batch needs before it starts.

The required environment is ``gh`` with a live login, ``pdftotext`` for the
Moodle PDF, and ``markdownlint-cli2`` for the report lint.  ``shutil.which``
locates each binary, and ``gh auth status`` decides whether GitHub access is
ready.  Both are injectable so the result shaping can be tested without a real
environment or network access.

``scripts/preflight.py`` prints one line per check; the exit code is 0 when
every check passes and 1 when any check fails.
"""

from __future__ import annotations

import shutil
import subprocess
from collections.abc import Callable
from dataclasses import dataclass

GH = "gh"
PDFTOTEXT = "pdftotext"
MARKDOWNLINT = "markdownlint-cli2"
GH_AUTH_TIMEOUT_SECONDS = 15

Which = Callable[[str], str | None]
Runner = Callable[..., object]


@dataclass(frozen=True)
class PreflightCheck:
    name: str
    ok: bool
    detail: str

    @property
    def line(self) -> str:
        status = "ok" if self.ok else "FAIL"
        return f"{self.name}: {status} - {self.detail}"


@dataclass(frozen=True)
class PreflightResult:
    checks: tuple[PreflightCheck, ...]
    summary_lines: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return all(check.ok for check in self.checks)

    @property
    def failures(self) -> tuple[PreflightCheck, ...]:
        return tuple(check for check in self.checks if not check.ok)


def check_tool(name: str, which: Which = shutil.which) -> PreflightCheck:
    located = which(name)
    if located is None:
        return PreflightCheck(name, False, "not found on PATH; run: nix develop")
    return PreflightCheck(name, True, located)


def check_gh_auth(which: Which = shutil.which, runner: Runner = subprocess.run) -> PreflightCheck:
    located = which(GH)
    if located is None:
        return PreflightCheck("gh auth", False, "gh not found on PATH; run: nix develop")
    try:
        completed = runner(
            [GH, "auth", "status"],
            capture_output=True,
            text=True,
            timeout=GH_AUTH_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return PreflightCheck("gh auth", False, "gh auth status timed out")
    except OSError as exc:
        return PreflightCheck("gh auth", False, f"could not run gh auth status: {exc}")
    if getattr(completed, "returncode", None) == 0:
        return PreflightCheck("gh auth", True, "authenticated")
    return PreflightCheck("gh auth", False, "not authenticated; run: gh auth login")


def run_preflight(which: Which = shutil.which, runner: Runner = subprocess.run) -> PreflightResult:
    checks = (
        check_gh_auth(which, runner),
        check_tool(PDFTOTEXT, which),
        check_tool(MARKDOWNLINT, which),
    )
    lines = [check.line for check in checks]
    failures = sum(1 for check in checks if not check.ok)
    if failures:
        lines.append(f"result: not ready - {failures} of {len(checks)} check(s) failed")
    else:
        lines.append(f"result: ready - all {len(checks)} checks passed")
    return PreflightResult(checks, tuple(lines))

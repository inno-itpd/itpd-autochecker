from __future__ import annotations

import re
import shutil
import subprocess
import textwrap
from pathlib import Path

import pytest

from tests.conftest import ROOT

GRADER_PROMPT = ROOT / "agents" / "grader.md"
WRAPPERS = (
    ROOT / ".opencode" / "agents" / "grader.md",
    ROOT / ".claude" / "agents" / "grader.md",
)
TEAM_DIR = "Team 5 - TmpTeam_12345_assignsubmission_file (1)"
ASSIGNMENT_DIR = "A3"
TEAM_WORK = f"/repo/itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
ASSIGNMENT_PROMPTS = tuple(
    ROOT / assignment / "grading_prompt.md" for assignment in ("A1", "A2", "A3")
)
POLICY = ROOT / "docs" / "grader-policy.md"
TEAM_DIR_PLACEHOLDER = "<team_dir>"
SCRIPT_COMMAND = re.compile(r"(?:^|[\s`])(?:uv run python\s+)?scripts/[\w.]+\.py\b")
INLINE_CODE = re.compile(r"`([^`\n]+)`")

FENCED_COMMAND = re.compile(
    r"^[ \t]*```(?:console|bash)[ \t]*\n(?P<body>.*?)^[ \t]*```[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


def _command_lines(text: str) -> list[tuple[int, str]]:
    """Return (line number, command line) for every console/bash fenced block."""
    lines: list[tuple[int, str]] = []
    for block in FENCED_COMMAND.finditer(text):
        body = textwrap.dedent(block.group("body"))
        first_line = text.count("\n", 0, block.start("body")) + 1
        for offset, line in enumerate(body.splitlines()):
            lines.append((first_line + offset, line))
    return lines


def _expand(
    command: str,
    *,
    team_dir: str = TEAM_DIR,
    team_work: str = TEAM_WORK,
) -> str:
    return (
        command.replace("{ASSIGNMENT_DIR}", ASSIGNMENT_DIR)
        .replace("{TEAM_WORK}", team_work)
        .replace("{TEAM_DIR}", team_dir)
    )


def _has_unquoted(command: str, needle: str) -> bool:
    """Return True when needle appears outside single or double quotes."""
    quote: str | None = None
    escaped = False
    index = 0
    while index < len(command):
        char = command[index]
        if escaped:
            escaped = False
            index += 1
            continue
        if char == "\\" and quote != "'":
            escaped = True
            index += 1
            continue
        if char in ("'", '"'):
            if quote is None:
                quote = char
            elif quote == char:
                quote = None
            index += 1
            continue
        if quote is None and command.startswith(needle, index):
            return True
        index += 1
    return False


def _team_path_violations(text: str) -> list[str]:
    violations: list[str] = []
    for line_number, line in _command_lines(text):
        if _has_unquoted(_expand(line), TEAM_DIR):
            violations.append(
                f"{GRADER_PROMPT.relative_to(ROOT)}:{line_number}: {line.strip()}"
            )
    return violations


def _placeholder_command_violations(path: Path) -> list[str]:
    """Return command lines and code spans that pass an unquoted ``<team_dir>``."""
    violations: list[str] = []
    text = path.read_text(encoding="utf-8")
    display = path.relative_to(ROOT) if ROOT in path.parents else path

    def check(line_number: int, command: str) -> None:
        if TEAM_DIR_PLACEHOLDER not in command or SCRIPT_COMMAND.search(command) is None:
            return
        if _has_unquoted(command, TEAM_DIR_PLACEHOLDER):
            violations.append(f"{display}:{line_number}: {command.strip()}")

    for line_number, line in _command_lines(text):
        check(line_number, line)
    for match in INLINE_CODE.finditer(text):
        line_number = text.count("\n", 0, match.start()) + 1
        check(line_number, match.group(1))
    return violations


def test_command_parser_reads_console_and_bash_blocks() -> None:
    text = "```console\necho one\n```\n\n```bash\necho two\n```\n"
    assert [line.strip() for _, line in _command_lines(text)] == ["echo one", "echo two"]


def test_grader_prompt_states_the_no_cd_and_quoting_rule() -> None:
    normalized = " ".join(GRADER_PROMPT.read_text(encoding="utf-8").split())
    assert (
        "A grader never changes directory and runs every command from the repository root"
        in normalized
    )
    assert "quotes every path that contains a team directory name" in normalized


def test_review_prompts_supply_the_exact_team_name_and_absolute_work_path() -> None:
    normalized = " ".join(GRADER_PROMPT.read_text(encoding="utf-8").split())
    assert "`{TEAM_WORK}` is the absolute path of the team work directory" in normalized
    assert "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}" in normalized
    assert "The fetcher takes the exact submission directory name" in normalized

    for wrapper in WRAPPERS:
        wrapper_text = " ".join(wrapper.read_text(encoding="utf-8").split())
        assert "{TEAM_WORK}" in wrapper_text
        assert "absolute" in wrapper_text
        assert "Never change directory" in wrapper_text

    agents = " ".join((ROOT / "AGENTS.md").read_text(encoding="utf-8").split())
    assert "{TEAM_WORK}" in agents


def test_grader_prompt_quotes_every_path_with_the_team_directory() -> None:
    text = GRADER_PROMPT.read_text(encoding="utf-8")
    assert _team_path_violations(text) == []


def test_quoting_check_fails_on_an_intentionally_unquoted_example() -> None:
    text = GRADER_PROMPT.read_text(encoding="utf-8")
    quoted = (
        'uv run python scripts/fetch_team_snapshot.py {ASSIGNMENT_DIR} "{TEAM_DIR}"'
    )
    assert quoted in text
    broken = text.replace(
        quoted,
        "uv run python scripts/fetch_team_snapshot.py {ASSIGNMENT_DIR} {TEAM_DIR}",
        1,
    )
    assert broken != text
    violations = _team_path_violations(broken)
    assert any("fetch_team_snapshot.py" in violation for violation in violations)


def test_quoting_check_fails_on_an_unquoted_absolute_work_path() -> None:
    block = "```console\nhead -n 40 {TEAM_WORK}/milestones.json\n```\n"
    violations = _team_path_violations(block)
    assert len(violations) == 1
    assert "head -n 40" in violations[0]


def test_assignment_prompts_quote_team_dir_in_helper_commands() -> None:
    violations = [
        violation
        for path in (*ASSIGNMENT_PROMPTS, POLICY)
        for violation in _placeholder_command_violations(path)
    ]
    assert violations == []


def test_placeholder_check_fails_on_an_unquoted_prompt_command(tmp_path: Path) -> None:
    prompt = tmp_path / "grading_prompt.md"
    prompt.write_text(
        "```console\n"
        "uv run python scripts/scan_privacy.py A3 <team_dir>\n"
        'uv run python scripts/scan_privacy.py A3 "<team_dir>"\n'
        "```\n",
        encoding="utf-8",
    )
    violations = _placeholder_command_violations(prompt)
    assert len(violations) == 1
    assert "<team_dir>" in violations[0]
    assert 'A3 "<team_dir>"' not in violations[0]


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required")
def test_documented_commands_accept_a_team_directory_with_spaces_and_parentheses(
    tmp_path: Path,
) -> None:
    work = (
        tmp_path
        / "itpd-assignments-feedback"
        / ASSIGNMENT_DIR
        / "work"
        / TEAM_DIR
    )
    work.mkdir(parents=True)
    (work / "milestones.json").write_text("[]\n", encoding="utf-8")
    (work / "issues.json").write_text("[]\n", encoding="utf-8")
    (work / "payload.json").write_text("{}\n", encoding="utf-8")

    text = GRADER_PROMPT.read_text(encoding="utf-8")
    commands: list[str] = []
    for _, line in _command_lines(text):
        expanded = _expand(line, team_work=str(work))
        if TEAM_DIR in expanded:
            commands.append(expanded)
    assert commands

    script = "\n".join(commands)
    parsed = subprocess.run(
        ["bash", "-n"], input=script, text=True, capture_output=True, check=False
    )
    assert parsed.returncode == 0, parsed.stderr

    filesystem_commands = [
        command
        for command in commands
        if command.strip().startswith(("rm -rf ", "mkdir -p "))
    ]
    assert filesystem_commands
    filesystem_result = subprocess.run(
        ["bash", "-euo", "pipefail", "-c", "\n".join(filesystem_commands)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert filesystem_result.returncode == 0, filesystem_result.stderr
    assert work.is_dir()
    assert (work / "snapshot").is_dir()

    (work / "milestones.json").write_text("[]\n", encoding="utf-8")
    reader_commands = [
        command for command in commands if command.strip().startswith("head -n 40 ")
    ]
    assert reader_commands
    reader_result = subprocess.run(
        ["bash", "-euo", "pipefail", "-c", "\n".join(reader_commands)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert reader_result.returncode == 0, reader_result.stderr
    assert "[]" in reader_result.stdout

from __future__ import annotations

import re
import shutil
import sqlite3
import subprocess
import textwrap
from pathlib import Path

import pytest

from tests.conftest import ROOT

COMPLIANCE_PROMPT = ROOT / "agents" / "compliance-agent.md"
SEMANTIC_PROMPT = ROOT / "agents" / "semantic-agent.md"
COMPLIANCE_WRAPPERS = (
    ROOT / ".opencode" / "agents" / "compliance-agent.md",
    ROOT / ".claude" / "agents" / "compliance-agent.md",
)
SEMANTIC_WRAPPERS = (
    ROOT / ".opencode" / "agents" / "semantic-agent.md",
    ROOT / ".claude" / "agents" / "semantic-agent.md",
)
TEAM_DIR = "Team 5 - TmpTeam_12345_assignsubmission_file (1)"
ASSIGNMENT_DIR = "A3"
TEAM_WORK = f"/repo/itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
ASSIGNMENT_PROMPTS = tuple(
    ROOT / assignment / "grading_prompt.md" for assignment in ("A1", "A2", "A3", "A4", "A5", "A6")
)
POLICY = ROOT / "docs" / "grading-policy.md"
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


def _team_path_violations(text: str, source: Path = COMPLIANCE_PROMPT) -> list[str]:
    violations: list[str] = []
    for line_number, line in _command_lines(text):
        if _has_unquoted(_expand(line), TEAM_DIR):
            violations.append(
                f"{source.relative_to(ROOT)}:{line_number}: {line.strip()}"
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


def test_compliance_prompt_states_the_no_cd_and_quoting_rule() -> None:
    normalized = " ".join(COMPLIANCE_PROMPT.read_text(encoding="utf-8").split())
    assert "A compliance agent never changes directory and runs every command from the repository root" in normalized
    assert "quotes every path that contains a team directory name" in normalized


def test_semantic_prompt_states_the_no_cd_and_quoting_rule() -> None:
    normalized = " ".join(SEMANTIC_PROMPT.read_text(encoding="utf-8").split())
    assert "A semantic agent never changes directory and runs every command from the repository root" in normalized
    assert "quotes every path that contains a team directory name" in normalized


def test_review_prompts_supply_the_exact_team_name_and_absolute_work_path() -> None:
    compliance = " ".join(COMPLIANCE_PROMPT.read_text(encoding="utf-8").split())
    assert "`{TEAM_WORK}` is the absolute path of the team work directory" in compliance
    assert "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}" in compliance
    assert "The fetcher takes the exact submission directory name" in compliance

    semantic = " ".join(SEMANTIC_PROMPT.read_text(encoding="utf-8").split())
    assert "`{TEAM_WORK}` is the absolute path" in semantic
    assert "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}" in semantic

    for wrapper in (*COMPLIANCE_WRAPPERS, *SEMANTIC_WRAPPERS):
        wrapper_text = " ".join(wrapper.read_text(encoding="utf-8").split())
        assert "{TEAM_WORK}" in wrapper_text
        assert "absolute" in wrapper_text
        assert "Never change directory" in wrapper_text

    agents = " ".join((ROOT / "AGENTS.md").read_text(encoding="utf-8").split())
    assert "{TEAM_WORK}" in agents


def test_agent_prompts_quote_every_path_with_the_team_directory() -> None:
    for prompt in (COMPLIANCE_PROMPT, SEMANTIC_PROMPT):
        text = prompt.read_text(encoding="utf-8")
        assert _team_path_violations(text, prompt) == []


def test_quoting_check_fails_on_an_intentionally_unquoted_example() -> None:
    text = COMPLIANCE_PROMPT.read_text(encoding="utf-8")
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

    text = COMPLIANCE_PROMPT.read_text(encoding="utf-8")
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


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required")
def test_semantic_prompt_commands_accept_a_team_directory_with_spaces_and_parentheses(
    tmp_path: Path,
) -> None:
    work = tmp_path / "itpd-assignments-feedback" / ASSIGNMENT_DIR / "work" / TEAM_DIR
    feedback = tmp_path / "itpd-assignments-feedback" / ASSIGNMENT_DIR / "feedback" / TEAM_DIR
    work.mkdir(parents=True)
    feedback.mkdir(parents=True)
    (work / "issues.json").write_text("[]\n", encoding="utf-8")
    (work / "summary.md").write_text("# Summary\n", encoding="utf-8")
    (work / "inventory.md").write_text("# Inventory\n", encoding="utf-8")
    (work / "semantic-claims.json").write_text("{}\n", encoding="utf-8")
    (work / "pdf-info.json").write_text("{}\n", encoding="utf-8")
    (feedback / "agent-compliance-feedback.md").write_text("# Assignment 3 Feedback Report\n", encoding="utf-8")
    (feedback / "agent-semantic-feedback.md").write_text(
        "# Assignment 3 Semantic Feedback\n", encoding="utf-8"
    )
    with sqlite3.connect(work / "evidence.sqlite") as connection:
        connection.execute("CREATE TABLE issues (number INTEGER, state TEXT, title TEXT)")

    text = SEMANTIC_PROMPT.read_text(encoding="utf-8")
    commands: list[str] = []
    for _, line in _command_lines(text):
        expanded = _expand(line, team_work=str(work))
        if TEAM_DIR in expanded:
            commands.append(expanded)
    assert commands

    parsed = subprocess.run(
        ["bash", "-n"], input="\n".join(commands), text=True, capture_output=True, check=False
    )
    assert parsed.returncode == 0, parsed.stderr

    readers = [
        command
        for command in commands
        if command.strip().startswith(("sha256sum ", "jq ", "uv run python -m sqlite3 "))
    ]
    assert readers

    for command in readers:
        working_dir = tmp_path if command.strip().startswith("sha256sum ") else ROOT
        result = subprocess.run(
            ["bash", "-euo", "pipefail", "-c", command],
            cwd=working_dir,
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, (command, result.stderr)


def _normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def test_prompt_names_the_four_modes_and_a_selection_table() -> None:
    text = COMPLIANCE_PROMPT.read_text(encoding="utf-8")
    assert "| Request | Mode |" in text
    for mode in ("`full review`", "`full regrade`", "`partial regrade`", "`segment inspect`"):
        assert mode in text


def test_full_regrade_keeps_the_work_directory_and_audits_every_segment() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "Never empty or delete the work directory" in text
    assert "A full regrade is a first-class mode" in text
    assert "State the saved claim" in text
    assert "Never change a status on prose alone" in text
    assert "write the payload first and render the report last" in text
    assert "regrade-changes.md" in text


def test_full_review_step_one_delete_does_not_apply_to_a_regrade() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "In `full review` mode only, empty the team work directory" in text
    assert "In `full regrade` and `partial regrade` mode, skip this step" in text


def test_prompt_reads_the_segment_count_from_assignment_config() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "len(ASSIGNMENT_CONFIG[ASSIGNMENT_DIR][\"segment_defs\"])" in text
    assert "13 for A3" not in text


def test_prompt_documents_the_regrade_diff_and_corrections() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "changes: S<n> <old> -> <new> (<reason>)" in text
    assert "corrections: <saved claim> -> <what the evidence shows>" in text
    assert "no status changes" in text


def test_prompt_names_the_one_writer_rule_and_the_active_gate() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "One writer per team" in text
    assert 'check_batch_ready.py {ASSIGNMENT_DIR} --active "<team_dir>"' in text


def test_prompt_documents_the_cutoff_view_and_the_collector_flag() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "issue_state_at_cutoff" in text
    assert "issue_events" in text
    assert "--timelines" in text
    assert "has_timeline" in text


def test_semantic_prompt_names_the_three_modes() -> None:
    text = SEMANTIC_PROMPT.read_text(encoding="utf-8")
    assert "| Request | Mode |" in text
    for mode in ("`semantic review`", "`semantic regrade`", "`semantic inspect`"):
        assert mode in text


def test_semantic_prompt_requires_a_claim_ledger_and_verification() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "semantic-claims.json" in text
    assert "`supported`" in text
    assert "`contradicted`" in text
    assert "`unverifiable`" in text
    assert "The compliance report is a map, not evidence" in text
    assert "evidence.sqlite" in text
    assert "At most three live `gh` calls" in text


def test_semantic_prompt_never_edits_the_report_and_escalates_conflicts() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "It never edits the compliance report" in text
    assert "record it in `conflicts` and keep the report untouched" in text
    assert "sha256sum" in text


def test_semantic_prompt_keeps_the_file_report_only_and_context_bounded() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "at most about twenty artifact files or sections" in text
    assert "never re-read them" in text
    assert "reuse a locator" in text


def test_semantic_prompt_refuses_an_existing_companion_and_names_the_mode() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "companion exists; use semantic regrade" in text
    assert "do not keep or overwrite it here" in text


def test_semantic_prompt_requires_the_complete_handoff() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "`{TEAM_WORK}/summary.md` and `{TEAM_WORK}/inventory.md` exist" in text
    assert "`{TEAM_WORK}/evidence.sqlite` exists" in text
    assert "If any of these is missing or mismatched" in text
    assert "no snapshot to verify against" in text


def test_semantic_prompt_uses_the_optional_ledger_check() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "--ledger" in text
    assert "semantic-claims.json" in text


def test_semantic_prompt_omits_only_unverified_dimensions() -> None:
    text = _normalized(SEMANTIC_PROMPT)
    assert "Omit a dimension only when all of its segments are `unverified`" in text
    assert "If fewer than three dimensions remain" in text


def test_semantic_wrappers_do_not_grant_edit() -> None:
    claude = (ROOT / ".claude" / "agents" / "semantic-agent.md").read_text(encoding="utf-8")
    claude_frontmatter = claude.split("---", 2)[1]
    assert "tools:" in claude_frontmatter
    assert "Write" in claude_frontmatter
    assert "Edit" not in claude_frontmatter

    opencode = (ROOT / ".opencode" / "agents" / "semantic-agent.md").read_text(encoding="utf-8")
    opencode_frontmatter = opencode.split("---", 2)[1]
    assert "permission:" in opencode_frontmatter
    assert "edit: deny" in opencode_frontmatter

    for wrapper in SEMANTIC_WRAPPERS:
        text = wrapper.read_text(encoding="utf-8")
        assert "agents/semantic-agent.md" in text


def test_compliance_prompt_hands_semantic_feedback_to_the_semantic_agent() -> None:
    text = _normalized(COMPLIANCE_PROMPT)
    assert "Do not write `agent-semantic-feedback.md` from this prompt" in text
    assert "agents/semantic-agent.md" in text
    assert "the semantic agent owns it" in text

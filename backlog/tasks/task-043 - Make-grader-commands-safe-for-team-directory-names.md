---
id: TASK-043
title: Make grader commands safe for team directory names
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 15:46'
labels: []
dependencies: []
ordinal: 43000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F6 from plan-1.md. Team directories contain spaces and parentheses. In the A3 batch one grader produced `syntax error near unexpected token '('` from an unquoted `cd`, and two graders got `No such file or directory` (exit 127) after changing away from the repository root. The second failure is structural now that `uv run python` is the only invocation: uv discovers `uv.toml` only inside the checkout, so leaving it fails on the read-only `~/.cache/uv` rather than merely losing a relative path.

Decision: never `cd`; run every command from the repository root and quote every path that contains a team name.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 `agents/grader.md` states that a grader never changes directory, runs every command from the repository root, and quotes every path that contains a team directory name or `{TEAM_DIR}`.
- [x] #2 The review prompt supplies `TEAM_DIR` and `TEAM_WORK` as absolute paths, so a grader does not assemble them with `cd`.
- [x] #3 Every command example that interpolates `{TEAM_DIR}` quotes the path.
- [x] #4 A test scans the command examples in `agents/grader.md` and fails when a path containing `{TEAM_DIR}` is unquoted.
- [x] #5 A dry run against a directory name containing spaces and `(` completes without a shell error.
- [x] #6 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Design: agents/grader.md now states the rule up front (a grader never changes directory, runs every command from the repository root, and quotes every path containing a team directory name or {TEAM_DIR}), defines {TEAM_WORK} as the absolute path of itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}, and uses it for every work-directory command and prose path. {TEAM_DIR} deliberately stays the exact submission directory name, not an absolute path: fetch_team_snapshot.py, collect_github_evidence.py, and scan_privacy.py join it under submissions/ and work/ themselves, and an absolute value would make pathlib discard those prefixes. AC #2 wording reconciled accordingly: the operator supplies the exact name and the absolute work path, so no command needs cd; this is documented in both wrappers and AGENTS.md. All fenced command examples quoting {TEAM_DIR} were fixed (fetch, collect, scan_privacy, pdftotext, privacy feedback scan), and work paths now use quoted {TEAM_WORK}. Added tests/test_grader_prompt_commands.py: it parses console/bash fences, expands {ASSIGNMENT_DIR}, {TEAM_DIR}, and {TEAM_WORK}, and flags paths whose team-name occurrence is outside quotes; the real document has zero violations, and mutation tests fail on an intentionally unquoted fetch command and an unquoted {TEAM_WORK}. The dry-run test creates a real temp work directory named Team 5 - TmpTeam_12345_assignsubmission_file (1), expands every documented team command, passes the whole script to bash -n, then executes the documented rm/mkdir/head commands successfully. Validation: uv run pytest -q -> 286 passed (7 new tests); markdownlint-cli2 on agents/grader.md, .opencode/agents/grader.md, .claude/agents/grader.md, and AGENTS.md -> 0 issues. Repo-wide markdownlint-cli2 still exits 1 with 31 pre-existing errors in ten itpd-assignments-feedback/A1|A2/feedback/*/denis-feedback.md files plus untracked TODO.md; left untouched.
<!-- SECTION:NOTES:END -->

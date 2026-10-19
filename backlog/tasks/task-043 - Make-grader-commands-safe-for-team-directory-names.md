---
id: TASK-043
title: Make grader commands safe for team directory names
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
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
- [ ] #1 `agents/grader.md` states that a grader never changes directory, runs every command from the repository root, and quotes every path that contains a team directory name or `{TEAM_DIR}`.
- [ ] #2 The review prompt supplies `TEAM_DIR` and `TEAM_WORK` as absolute paths, so a grader does not assemble them with `cd`.
- [ ] #3 Every command example that interpolates `{TEAM_DIR}` quotes the path.
- [ ] #4 A test scans the command examples in `agents/grader.md` and fails when a path containing `{TEAM_DIR}` is unquoted.
- [ ] #5 A dry run against a directory name containing spaces and `(` completes without a shell error.
- [ ] #6 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

---
id: TASK-042
title: Resume failed grader sessions without duplicate writers
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
labels: []
dependencies: []
ordinal: 42000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F5 from plan-1.md. Four of seven A3 graders died within seconds with `403 "Access denied by security policy."` (`code: AUTH`) after running 5 to 10 minutes. The harness auto-resumed them, and because fresh retries had already started for two teams, Teams 1 and 4 briefly had two graders writing the same report and payload; the duplicates were interrupted. Every retry at four-way concurrency succeeded.

Decision: `team_batch_size` stays as it is. Do not lower it to 4. Prefer `send_message` to the existing session, which may wake it and continue from the saved report and payload, instead of starting the team again in a new subagent; check `list_agents` first and never run two writers for one team.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 AGENTS.md records the 403 signature and `code: AUTH` in the observed failure modes, and notes that retries succeeded, without changing `grading.json` or the documented batch size.
- [ ] #2 The orchestration guidance says to check `list_agents`, then resume a failed team by `send_message` to its existing resumable session, and to launch a replacement only when that session cannot be resumed and no writer for the team is active.
- [ ] #3 A pre-extraction gate confirms exactly one writer per team from the report and payload mtimes, and refuses extraction while a grader is still registered or running for that team; the workflow documents the gate.
- [ ] #4 Verification: a seven-team batch at the current batch size produces seven valid reports with no duplicate writers and no truncated reports.
- [ ] #5 `markdownlint-cli2` passes.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

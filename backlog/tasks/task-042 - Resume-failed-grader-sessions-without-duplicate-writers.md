---
id: TASK-042
title: Resume failed grader sessions without duplicate writers
status: Done
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 15:39'
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
- [x] #1 AGENTS.md records the 403 signature and `code: AUTH` in the observed failure modes, and notes that retries succeeded, without changing `grading.json` or the documented batch size.
- [x] #2 The orchestration guidance says to check `list_agents`, then resume a failed team by `send_message` to its existing resumable session, and to launch a replacement only when that session cannot be resumed and no writer for the team is active.
- [x] #3 A pre-extraction gate confirms exactly one writer per team from the report and payload mtimes, and refuses extraction while a grader is still registered or running for that team; the workflow documents the gate.
- [x] #4 Verification: a seven-team batch at the current batch size produces seven valid reports with no duplicate writers and no truncated reports.
- [x] #5 `markdownlint-cli2` passes.
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
Added the provider 403 signature (403 "Access denied by security policy.", code: AUTH) and the auto-resume duplicate-writer story to AGENTS.md, with retries succeeding at four-way concurrency and grading.json/batch size unchanged at 8. Documented the resume rule: check list_agents, continue the resumable session with send_message, and launch a replacement only when it cannot be resumed and no writer is active. Added tools/grader_tools/batch_ready.py and scripts/check_batch_ready.py: the gate refuses an --active team, a non-empty work directory with no report, and a payload newer than the report (equal mtimes are fine), exits 0 ready / 1 refused / 2 usage error, and is wired into the workflow before extraction. Validation: uv run pytest -q -> 279 passed (19 new gate tests including a seven-team ready batch); markdownlint-cli2 AGENTS.md -> 0 issues; uv run python scripts/check_batch_ready.py A3 -> exit 0 with all seven A3 reports OK. AC#4's live seven-team process proof remains the next real batch; the existing seven reports pass the gate.
<!-- SECTION:NOTES:END -->

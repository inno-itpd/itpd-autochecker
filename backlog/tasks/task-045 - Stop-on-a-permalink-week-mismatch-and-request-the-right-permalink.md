---
id: TASK-045
title: Stop on a permalink week mismatch and request the right permalink
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
labels: []
dependencies: []
ordinal: 45000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F8 from plan-1.md. Team 5's PDF permalinks `reports/week-02/README.md` at `ec5016f`, while the assignment expects `reports/week-03/README.md`. `scripts/fetch_team_snapshot.py` records `permalink_path` faithfully, but neither the script nor `summary.md` warns that the week is wrong; the operator had to notice and supply the right permalink by hand because the submission report provided a wrong one.

Decision: derive and record the permalink week, warn on a mismatch, and stop to request the correct permalink instead of silently grading a wrong-week target. The mismatch remains a submission shortfall in S12, and once the right permalink is supplied the snapshot still governs every file check.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 `scripts/fetch_team_snapshot.py` derives `permalink_week` from the permalink path and writes it, together with the assignment's expected week, to `pdf-info.json`.
- [ ] #2 A mismatch prints a `warn:` line, repeats it in `summary.md`, exits non-zero instead of fetching or grading a wrong-week target, and prints the rerun command that requests the correct permalink.
- [ ] #3 A `--permalink <url>` override replaces the PDF permalink, records `permalink_source=operator`, and lets the run continue; the override is documented in `agents/grader.md` and `AGENTS.md`.
- [ ] #4 `agents/grader.md` step 8 states that a wrong-week PDF permalink is a submission shortfall in S12, that the snapshot still governs every file check, and that the grader requests the right permalink when the fetcher stops.
- [ ] #5 Tests: a fixture PDF with a week-02 permalink produces the warning and the stop and records `permalink_week`; a correct-week PDF proceeds; the operator override proceeds.
- [ ] #6 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

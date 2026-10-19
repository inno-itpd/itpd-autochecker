---
id: TASK-047
title: Re-verify the committed A3 regrade output after the fixes
status: To Do
assignee: []
created_date: '2026-10-19 14:58'
updated_date: '2026-10-19 15:00'
labels: []
dependencies:
  - TASK-039
  - TASK-040
  - TASK-041
  - TASK-042
  - TASK-043
  - TASK-044
  - TASK-045
  - TASK-046
ordinal: 47000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sequencing step 4 from plan-1.md, adjusted to the state on disk. The regrade output is already committed: `itpd-assignments-feedback` is at `ff7faad` (`fix(a3): update feedback`) with seven regenerated reports, `A3/dev.md`, and `A3/feedback_release.csv`, and this repository bumped the pointer in `6775432` (`chore(feedback): update`). That commit landed before the fixes, contrary to the "fix the prompt and scripts before committing the regrade output" decision, so this task re-verifies the committed reports against the fixed rubric and tooling and commits any correction. Team 5's S12 `Evidence gaps: yes` still needs instructor review before the output is treated as final.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The instructor has reviewed Team 5's S12 and decided whether it keeps `Evidence gaps: yes`; the report content changes only for that decision.
- [ ] #2 TASK-039 through TASK-046 are done, so the rubric, tooling, and guidance used for the next batch are fixed and committed before this verification.
- [ ] #3 All seven reports are re-checked against the fixed rubric and tooling, including the S2 hard deadlines, per-issue S6 fields, privacy findings, and permalink week; any status change is recorded in the submodule and the pointer is bumped here.
- [ ] #4 `A3/dev.md` and `A3/feedback_release.csv` are re-extracted with no warnings, and every report passes `scripts/check_feedback_report.py` and `scripts/scan_privacy.py --feedback`; if nothing changes, the notes record that `ff7faad` stands.
- [ ] #5 No unrelated submodule or working-tree changes are included.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

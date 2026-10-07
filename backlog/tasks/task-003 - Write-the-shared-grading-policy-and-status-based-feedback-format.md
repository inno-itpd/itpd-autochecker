---
id: TASK-003
title: Write the shared grading policy and status-based feedback format
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Port docs/ from swp-autochecker, replacing numeric scores with segment statuses (met/partial/missing/unverified) and adding ITPD rules: PDF+ZIP snapshot, gh api evidence, privacy, Since markers, deviations.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 docs/grading-feedback-format.md defines the status-based report contract
- [x] #2 docs/grader-policy.md covers snapshot, live GitHub evidence, privacy, deviations, regrades
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Statuses met/partial/missing/unverified replace SWP scores; no grade is proposed, the instructor decides. Admin-only branch-protection 403/404 is explicitly not an evidence gap (A1 rubric review flagged that it would push every team into manual review).
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

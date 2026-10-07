---
id: TASK-009
title: Add the itpd-assignments-feedback submodule
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 21:10'
labels: []
dependencies: []
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Initialise inno-itpd/itpd-assignments-feedback (gitignored submissions and work, feedback/markdown per assignment), push it, and add it as a submodule.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Feedback repo has an initial commit on GitHub
- [x] #2 itpd-autochecker has it as a submodule at itpd-assignments-feedback/
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Feedback repo pushed to inno-itpd/itpd-assignments-feedback and added as a submodule in ee0d053. Submission PDFs are committed there; work/ is gitignored because the grader fetches snapshots from GitHub.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

---
id: TASK-009
title: Add the itpd-assignments-feedback submodule
status: To Do
assignee: []
created_date: '2026-10-07 10:15'
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
- [ ] #1 Feedback repo has an initial commit on GitHub
- [ ] #2 itpd-autochecker has it as a submodule at itpd-assignments-feedback/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

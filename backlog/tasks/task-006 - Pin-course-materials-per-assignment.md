---
id: TASK-006
title: Pin course materials per assignment
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Add inno-itpd/itpd as A<N>/itpd submodules pinned to the reviewed commit.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A1/itpd is pinned to fe58ba70bbd90b92ffd6942d340f1e8b35b4bbb1 (A1 as published at the deadline)
- [x] #2 A2/itpd is pinned to a949e8d7ff7f677ed3b97fa1b9bd9291b4a05bc1
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Submodules dissociated from the local ../itpd reference clone (repacked, alternates removed) so they do not depend on a sibling checkout.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

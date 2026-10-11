---
id: TASK-022
title: 'Add small grader utilities: image info, preflight, and assignment windows'
status: To Do
assignee: []
created_date: '2026-10-11 14:24'
labels: []
dependencies: []
ordinal: 22000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Sessions probed for the markdownlint binary and parsed PNG headers in Python because identify was unavailable.
Add scripts/image_info.py <files...> reporting pixel dimensions, byte size, and transparency for PNG and JPEG without ImageMagick.
Add scripts/preflight.py checking gh auth status, pdftotext, and markdownlint-cli2 before a grader batch.
Extend tools/grader_tools/assignment_config.py with issue_cutoff and week_window_start per assignment so the A2 hard-deadline facts live in one place.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 image_info.py reports dimensions and size for PNG and JPEG files and flags transparent PNGs
- [ ] #2 preflight.py reports each required tool and exits non-zero when gh is not authenticated or a tool is missing
- [ ] #3 assignment_config.py carries issue_cutoff and week_window_start for A1 and A2
- [ ] #4 Tests cover image header parsing and preflight result shaping and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

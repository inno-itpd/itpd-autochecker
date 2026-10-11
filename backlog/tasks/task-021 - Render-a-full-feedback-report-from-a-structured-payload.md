---
id: TASK-021
title: Render a full feedback report from a structured payload
status: To Do
assignee: []
created_date: '2026-10-11 14:24'
labels: []
dependencies: []
ordinal: 21000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
In full review mode graders hand-write feedback.md and one session wrote its own renderer.
Add scripts/render_feedback_report.py with signature render_feedback_report.py <assignment> <payload.json> that renders a complete report from a structured payload: metadata, segment updates, unresolved gaps, summary, strengths, and main issues.
Reuse render_report and render_segment_block from tools/grader_tools/feedback_report.py, and document the payload shape in the script docstring and tests.
This complements scripts/patch_feedback_report.py which patches an existing report.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A payload renders a complete report that passes scripts/validate_feedback_report.py
- [ ] #2 Malformed payloads fail with a clear message and no partial report file
- [ ] #3 The payload shape is documented and covered by tests and uv run pytest passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

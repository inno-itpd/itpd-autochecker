---
id: TASK-033
title: Make the report write-early and crash-safe
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 11:54'
labels: []
dependencies: []
ordinal: 33000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A crash mid-review leaves no validated report. Team 4's half-written report failed validation, and Team 9 crashed while correcting its own report. The validated report must reach disk as soon as the statuses are decided, and a missing segment must render as an explicit placeholder rather than an invalid file.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 render_feedback_report.py accepts an incomplete segment_updates and renders each missing segment as unverified with Evidence gaps: yes and an explicit placeholder bullet, so the file validates
- [x] #2 Placeholders never render as met, and the rendered file passes validate_feedback_report.py
- [x] #3 validate_feedback_report.py quotes the computed status counts beside the declared ones when the overall assessment does not match
- [x] #4 agents/grader.md Output tells the grader to write the validated report as soon as the 13 statuses are decided, then run the gates
- [x] #5 Output describes building the payload per segment group and writing work/<team>/payload.json after each group
- [x] #6 Tests cover the partial render, the placeholder status, and the count-bearing error
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
Placeholder rendering lives in scripts/render_feedback_report.py: _parse_segment_updates returns the parsed blocks plus the omitted segment numbers, and _placeholder_segment builds an unverified block with Evidence gaps: yes, the fixed 'Not reviewed: ...' evidence bullet, and the fixed pending-review bullet; _parse_unresolved auto-supplies that bullet for omitted gap segments while still rejecting bullets for non-gap segments. A complete payload renders byte-identically. tools/grader_tools/validate.py parses the declared Met/Partial/Missing/Unverified lines and reports declared vs computed counts on mismatch, adding a formatting-only note when the counts agree. agents/grader.md Output and docs/grading-feedback-format.md document the write-early flow, the per-group payload.json, and the placeholder shape. Tests cover partial renders, placeholders never met, supplied gap bullets, the partial CLI render, and the count-bearing error. Validation: uv run pytest -q -> 210 passed; markdownlint-cli2 agents/grader.md docs/grading-feedback-format.md -> 0 issues; a manual empty segment_updates render produced 9/9 unverified and passed validation.
<!-- SECTION:NOTES:END -->

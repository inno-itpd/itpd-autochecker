---
id: TASK-021
title: Render a full feedback report from a structured payload
status: Done
assignee: []
created_date: '2026-10-11 14:24'
updated_date: '2026-10-11 16:33'
labels: []
dependencies: []
modified_files:
  - scripts/render_feedback_report.py
  - tests/test_render_feedback_report.py
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
- [x] #1 A payload renders a complete report that passes scripts/validate_feedback_report.py
- [x] #2 Malformed payloads fail with a clear message and no partial report file
- [x] #3 The payload shape is documented and covered by tests and uv run pytest passes
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-11: added scripts/render_feedback_report.py and tests/test_render_feedback_report.py.

Mechanics: render_feedback_report.py <assignment> <payload.json> reads one structured JSON object, renders the whole feedback.md with render_report and render_segment_block, and writes it to payload `output_path` (relative to the current working directory; parent directories are created). Payload keys: `output_path`, `team`, `repository`, `snapshot`, optional `snapshot_notes`, `summary` (3-5 bullets), `strengths` and `main_issues_to_fix` (at least one bullet each), `segment_updates` (the same per-segment shape as regrade_feedback_segments.py, with an optional matching `name`, and it must cover exactly the assignment's segments), and optional `unresolved_evidence_gaps` (one non-empty bullet list per gap segment, no other keys). Status, evidence, shortfall, and gap consistency is checked before rendering, then the rendered text is re-parsed and run through validate_report, so the script cannot write a report that scripts/validate_feedback_report.py would reject.

Decisions: metadata is derived from `team`, `repository`, and `snapshot` instead of free-form text, and the primary index link is built from the assignment config so it always matches the validator's canonical URL; when the repository or snapshot is missing the payload must carry `snapshot_notes` instead and the preamble renders `none` for the three metadata lines, matching the format's no-snapshot rule. Every check runs before the output file is opened, so malformed payloads leave no partial file and never overwrite an existing report. Unknown top-level and per-segment keys are rejected so typos like `sumary` or `verified_shortfall` fail loudly, and bullet lists must be single-line strings so the summary bullet count stays meaningful.

Validation: uv run pytest -> 157 passed, with 36 new tests covering exact equality with tests.report_builder, A2 coverage, the CLI write path plus scripts/validate_feedback_report.py exit 0, the no-snapshot notes path, an existing report preserved on failure, and rejection cases for JSON shape, metadata, segment updates, unresolved gaps, and multi-line bullets. A manual A1 run (partial S4, unverified S7) rendered a report that passed scripts/validate_feedback_report.py and scripts/check_feedback_report.py (markdownlint 0 errors). markdownlint-cli2 "**/*.md" reports only the pre-existing .claude/.opencode MD041 findings and the untracked TODO.md findings; no Markdown changed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

---
id: TASK-041
title: Cut privacy-scanner noise without suppressing name findings
status: Done
assignee: []
created_date: '2026-10-19 14:57'
updated_date: '2026-10-19 15:32'
labels: []
dependencies: []
ordinal: 41000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
F3 from plan-1.md. Two noise sources were reproduced in the A3 batch: the inline `data:font/woff2;base64,...` blob in Team 3's `docs/architecture/context.svg` is reported as a phone number, and name-token matching produced 114 hits for Team 1, 113 of them in `reports/week-0N/meeting-*` files, burying the one hit in `docs/project-plan.md` that mattered for S12. The scanner's exit codes and `--feedback` mode are correct.

Decision: real names anywhere in the repository are a shortfall, including public meeting artifacts. Reduce the noise by stripping base64 payloads and grouping hits per file, not by hiding meeting artifacts.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 `data:...;base64,` payloads are stripped before matching, so an inline SVG font cannot produce a phone or email finding.
- [x] #2 Findings are grouped per file with a count instead of one line per hit, and every member-name hit remains a finding, including hits in meeting artifacts; no switch suppresses them.
- [x] #3 Pytest fixtures cover an SVG with a base64 font (no phone finding), a meeting transcript with a member name (name finding), and a name outside meeting artifacts (name finding).
- [x] #4 Rescanning Team 3's snapshot drops the `context.svg` phone finding and keeps the transcript name hits; Team 1's output reports the meeting files as grouped counts.
- [x] #5 `uv run pytest` and `markdownlint-cli2` pass.
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
Stripped inline data:...;base64, payloads (including wrapped payloads) before matching, with newlines preserved so line numbers stay correct. Fixed the decimal-coordinate false positive by rejecting a digit-leading phone match right after a dot (lookbehind (?<![\w.])) while keeping real SVG text and 8 (999) / +7 999 formats. Grouped findings one per (rule, path) with count and matched lines; the summary now prints one line per file with a count plus per-rule hit/file totals, and every meeting-artifact name hit stays reported with no suppression switch. Updated the scanner docstrings, agents/grader.md step 12, A3 procedure step 14, AGENTS.md, and the tests (8 new tests covering base64, decimal coordinates, a real SVG phone, grouped counts, meeting transcript, and non-meeting names). Validation: uv run pytest -q -> 260 passed; markdownlint-cli2 on the three changed Markdown files -> 0 issues; live rescans: Team 3 drops the context.svg phone finding and keeps 6 grouped transcript hits, Team 1 reports 8 grouped files with 114 hits including docs/project-plan.md, and the feedback mode reports no findings. Deviation: repo-wide markdownlint-cli2 still reports the pre-existing A1/A2 denis-feedback.md issues and untracked TODO.md; left untouched.
<!-- SECTION:NOTES:END -->

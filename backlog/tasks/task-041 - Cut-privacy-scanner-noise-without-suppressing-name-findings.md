---
id: TASK-041
title: Cut privacy-scanner noise without suppressing name findings
status: To Do
assignee: []
created_date: '2026-10-19 14:57'
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
- [ ] #1 `data:...;base64,` payloads are stripped before matching, so an inline SVG font cannot produce a phone or email finding.
- [ ] #2 Findings are grouped per file with a count instead of one line per hit, and every member-name hit remains a finding, including hits in meeting artifacts; no switch suppresses them.
- [ ] #3 Pytest fixtures cover an SVG with a base64 font (no phone finding), a meeting transcript with a member name (name finding), and a name outside meeting artifacts (name finding).
- [ ] #4 Rescanning Team 3's snapshot drops the `context.svg` phone finding and keeps the transcript name hits; Team 1's output reports the meeting files as grouped counts.
- [ ] #5 `uv run pytest` and `markdownlint-cli2` pass.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

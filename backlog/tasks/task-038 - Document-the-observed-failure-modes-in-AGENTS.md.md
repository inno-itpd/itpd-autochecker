---
id: TASK-038
title: Document the observed failure modes in AGENTS.md
status: To Do
assignee: []
created_date: '2026-10-19 11:15'
labels: []
dependencies: []
ordinal: 38000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The A3 batch exposed failure modes the repo guide does not mention: context blowups from oversized dumps, bare-SHA PDFs, cleaned work directories, and the two independent uv failures.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The workflow documents the two legitimate interpreter invocations and the probe that picks one
- [ ] #2 A troubleshooting subsection covers the context blowup, the bare-SHA PDF, and the cleaned work directory
- [ ] #3 The guide says a grader must keep work/<team>/ until the batch is extracted, because the final scan_privacy.py run needs it
- [ ] #4 The two uv causes and their distinct remedies are stated separately, and the cache override is never presented as a complete fix
- [ ] #5 markdownlint passes on the changed Markdown
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

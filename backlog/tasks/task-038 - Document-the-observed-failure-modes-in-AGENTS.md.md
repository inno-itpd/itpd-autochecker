---
id: TASK-038
title: Document the observed failure modes in AGENTS.md
status: Done
assignee: []
created_date: '2026-10-19 11:15'
updated_date: '2026-10-19 12:27'
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
- [x] #1 The workflow documents the two legitimate interpreter invocations and the probe that picks one
- [x] #2 A troubleshooting subsection covers the context blowup, the bare-SHA PDF, and the cleaned work directory
- [x] #3 The guide says a grader must keep work/<team>/ until the batch is extracted, because the final scan_privacy.py run needs it
- [x] #4 The two uv causes and their distinct remedies are stated separately, and the cache override is never presented as a complete fix
- [x] #5 markdownlint passes on the changed Markdown
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
Decisions: (1) Documented both legitimate interpreter invocations in the Workflow with the one-line probe, kept the existing uv run python commands, and stated the substitution once (replace every uv run python command with .venv/bin/python when the probe prints it), so no command lines were rewritten and the helper/regrade commands stay consistent. (2) Added the retention rule under Workflow step 3: keep every work/<team_dir>/ until step 5 extracts the batch, because the final scan_privacy.py run reads pdf-info.json and the fetched snapshot. (3) Added '### Observed failure modes' under '## Troubleshooting' with three batch entries: context blowup (14 lost A3 runs; commits.json 1.35 MB, prs.json 284 KB; summary.md first, ~40-line projections, stop/narrow/continue, no re-reads), bare-SHA PDF (gh search commits <sha> --json repository resolves only an unambiguous repository; --repo org/repo operator override recorded as permalink_source=operator; collect_github_evidence.py prints result: skipped (no snapshot) and exits 0, a judged outcome, S12 shortfall stands), and cleaned work directory (default scan needs pdf-info.json plus the snapshot; fallback scan_privacy.py A<N> <team_dir> --feedback <report> --no-snapshot; --no-snapshot without --feedback is an error; keeping the work directory until extraction remains the primary rule). (4) Rewrote the two uv bullets as separate Cause 1 (read-only cache; run from the checkout for .local/uv-cache, --config-file, or UV_CACHE_DIR; --no-cache is not a substitute) and Cause 2 (broken Nix-Python sysconfig/platform data; use .venv/bin/python or repair the Python and _PYTHON_HOST_PLATFORM/_PYTHON_SYSCONFIGDATA_NAME), corrected the false 'uv run avoids it' claim, and added the explicit independence sentence: a cache override fixes only Cause 1 and is never a complete fix. Kept the uv.toml and direnv entries and did not touch the 'Adding a new assignment' smoke checks; added the new --repo/--no-snapshot flags to the helper-script reference. Validation: .venv/bin/python -m pytest -q -> 239 passed in 3.43s (exit 0); markdownlint-cli2 AGENTS.md -> 0 issues in 1 file (exit 0). Working-tree changes limited to AGENTS.md and this task file; no commit made, TODO.md and plan.md left untracked.

Final rerun after the last wording edit: .venv/bin/python -m pytest -q -> 239 passed in 3.00s (exit 0); markdownlint-cli2 AGENTS.md -> 0 issues in 1 file (exit 0).
<!-- SECTION:NOTES:END -->

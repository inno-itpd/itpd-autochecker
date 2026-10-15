---
id: TASK-026
title: 'Switch the commit-itpd skill to the Harness:/Model: metadata format'
status: Done
assignee: []
created_date: '2026-10-15 20:07'
updated_date: '2026-10-15 20:07'
labels: []
dependencies: []
ordinal: 26000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Update .agents/skills/commit-itpd/SKILL.md to the course commit skill's message format: replace the Co-Authored-By trailer with Harness: and Model: metadata lines, require Model: to hold the exact <provider>/<model> identifier quoted from the harness identity context, and forbid Co-authored-by trailers, while keeping this repository's path scopes and 2-4 bullet body. Update the AGENTS.md Git conventions bullet that still mandates the Co-Authored-By trailer.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The skill requires the Harness: and Model: metadata lines, with Model: as the exact <provider>/<model> identifier quoted from the harness identity context, and forbids Co-authored-by trailers.
- [x] #2 The skill keeps this repository's path scopes, 2-4 bullet body, staged-changes-only rule, and no literal backslash-n rule.
- [x] #3 AGENTS.md Git conventions state the Harness: and Model: lines instead of the Co-Authored-By trailer.
- [x] #4 markdownlint-cli2 (dev shell, 0.23.2) reports no issues on the changed Markdown.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Rewrote .agents/skills/commit-itpd/SKILL.md to the course skill's metadata format: the Co-Authored-By trailer became Harness: and Model: lines, Model: carries the exact <provider>/<model> quoted from the harness identity context, and Co-authored-by trailers are forbidden; the AGENTS.md Git conventions bullet was updated to match. Decisions: the scope list, 2-4 bullet body, and staged-changes-only rule stay this repository's; the course cross-check against scripts/opencode/current-model.sh has no counterpart here, so the fallback remains 'stop and ask the user'; the Model: example uses this repository's own session model, openrouter/deepseek/deepseek-v4.1-flash. Validation: markdownlint-cli2 0.23.2 from the dev shell reports 0 issues on both changed files (a global 0.21.0 binary shadows it outside the shell); uv run pytest is 180 passed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

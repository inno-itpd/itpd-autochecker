---
id: TASK-054
title: Rename the grader-era names around the two-agent split
status: Done
assignee: []
created_date: '2026-11-03 14:44'
updated_date: '2026-11-03 14:47'
labels: []
dependencies: []
ordinal: 54000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The 2026-11 split renamed the two prompts and wrappers, but the report file, the Python package, the policy doc, the format doc, the check scripts, the semantic companion's schema bullet, and the prose still use the retired single "grader" role or name the same file on three different axes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 agent-feedback.md is renamed to agent-compliance-feedback.md in all 45 submodule reports, the README, the dev.md tables, and the instructor notes
- [x] #2 tools/grader_tools no longer exists and every import and doc reference uses tools/autochecker
- [x] #3 docs/grader-policy.md and docs/grading-feedback-format.md are renamed to docs/grading-policy.md and docs/compliance-feedback-format.md with every link rewritten
- [x] #4 The semantic companion records `- Compliance report:` and semantic_feedback.py validates that bullet
- [x] #5 The check and validate compliance scripts are role-named, and no grader prose remains outside backlog history and grading-process words
- [x] #6 uv run pytest passes, markdownlint is clean on changed files, the five dev.md files regenerated with link-only diffs, and every feedback_release.csv is byte-identical
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Decisions: renamed the report contract to agent-compliance-feedback.md for all 45 reports so the compliance and semantic files share one naming axis; renamed tools/grader_tools to tools/autochecker (role-neutral and matching the project); renamed docs/grader-policy.md to docs/grading-policy.md and docs/grading-feedback-format.md to docs/compliance-feedback-format.md; renamed the check and validate scripts to check_compliance_feedback.py and validate_compliance_feedback.py; unified the semantic companion on the `- Compliance report:` bullet (constant renamed to COMPLIANCE_REPORT_PATTERN); replaced the retired "grader" prose with the role it now means, kept backlog history and the assignment-level grading_prompt.md/grading.json names. Added the missing `max_agent_resumes` scope sentence: the cap covers compliance resumes only.

Execution: submodule commit 11ceb2a (81 files: 45 renames plus the README, five dev.md, and the instructor notes) pushed to origin/main, then parent commit 2ecf086 (84 files) and bump 403aa50. Every dev.md diff is link-only; no feedback_release.csv changed.

Found in passing: A2's dev.md and feedback_release.csv were stale, last regenerated 2026-10-15 before Team 8's report existed. Regeneration would add Team 8, which is unrelated to the rename, so both were restored to HEAD; that catch-up is left for a deliberate export run.

Validation: uv run pytest 450 passed; markdownlint-cli2 on the 17 changed Markdown files 0 errors; scripts/check_compliance_feedback.py A5 Team 1 passes validation and lint; scripts/check_batch_ready.py A5 reports ready with 9 of 9 teams; a repo-wide search finds no grader-era path or prose outside backlog history.

Correction: after removing the untracked TODO.md and the task file from the first parent commit, the amended rename commit is 6102ed9 and the bump is 403aa50.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

---
id: TASK-052
title: Tighten the A5 rubric after the first grading pass
status: Done
assignee: []
created_date: '2026-11-01 16:04'
updated_date: '2026-11-01 16:04'
labels: []
dependencies: []
ordinal: 52000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The 2026-11-01 first A5 grading pass (nine reports, committed in the feedback submodule) exposed rubric wording that made graders diverge: S2 said "the two new stories" and duplicated S1's Sprint Backlog link, S8 judged the Week 6 due week that S9 owns, S10 and S11 contradicted the assignment's VM-unavailable fallback, and S13's milestone, CI-check, contribution-table, and privacy rules were narrower or wider than the weekly-report and visibility requirements. Apply precision-only fixes to A5/grading_prompt.md, keep every status rule and threshold, and do not re-grade in this session: the reports, dev.md, and feedback_release.csv stay as the first pass, and the affected segments are regraded in a later session.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A5/grading_prompt.md states each fix with one owning segment: S2's new-story split and the S1 Sprint Backlog boundary, S8's reappearance rule, S9's Week 6 class-week window, S10 and S11's VM-unavailable fallback, and S13's milestone, CI-check, contribution-table, and repository-wide privacy rules.
- [x] #2 No status threshold changes: the status guide, segment names, and evidence rules stay as they were.
- [x] #3 The saved A5 reports, dev.md, and feedback_release.csv are untouched; the next session re-grades only the affected segments.
- [x] #4 uv run pytest and markdownlint-cli2 on the changed file pass.
- [x] #5 The change is committed with this repository's Conventional Commit, Harness, and Model conventions.
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
# Result

Audited the nine saved A5 reports segment by segment (a compact digest of every `Why not met` bullet) and cross-checked each suspect criterion against the pinned materials: `assignments/assignment-5.md`, `weekly-report-requirements.md`, `customer-meetings-requirements.md`, `planning-requirements.md`, `sprint-ceremonies-requirements.md`, `quality-requirements-requirements.md`, `repository-requirements.md`, `visibility-requirements.md`, the deployment and validation guides, and the syllabus's Week 6 window.

## Fixes applied to A5/grading_prompt.md (precision only)

- S2: the "two new stories" split is now existential (at least one new story scheduled in `SPRINT-05`, at least one other left unscheduled and refined), so teams that add more than two are judged on what they actually have; the partial list names the new scheduled story in the role check, and the guardrail judges every new story rather than "the two".
- S2/S1 boundary: S2 no longer requires the plan's `**Sprint Backlog:**` link to reach the milestone; S1 owns that link, as S2's own guardrail already said.
- S8/S9 boundary: S8 judges that a not-carried-out action point reappears, not whether its new due week falls in Week 6; S9 owns the Week 6 window.
- S9 and the assignment parameters: the week is the Week 6 class week, 30 October to 5 November 2026, per the syllabus; 7 November is the Week 6 submission deadline, and a date from 6 November on is Week 7.
- S10 and S11: codify the assignment's VM-unavailable fallback. With the deviation declared, no deploy happens and the segment is met when the tag names the reviewed commit the checks ran on and no artifact claims a deploy or rework; the absent deployment stays S4's shortfall. The no-deploy guardrail now applies only when no fallback is declared.
- S13: name each plan milestone by its `**Due:**` in the range or say the plan carries none; accept "every check applies" when no check is non-applicable; use "where possible" for contribution links, matching the weekly-report rule; and make the privacy line a repository-wide claim that covers Week 1 to Week 4 files, with only Week 5 meeting artifacts left to S9.

## Deliberate non-changes

- No regrade in this session. The nine reports, `dev.md`, and `feedback_release.csv` are untouched and remain the first pass.
- No status threshold, segment name, or evidence rule changed; the status guide and the 14 segments are as they were.
- The shared guidance needed no edit: the VM fallback and privacy scope follow `docs/grader-policy.md`'s deviation and privacy rules, and the fixes belong to the A5 prompt.
- The pre-existing markdownlint errors in `TODO.md` and the A4 `danila-feedback.md` files are unrelated and were left alone.

## Expected effect on the next regrade

No status flip is expected from the wording alone. Team 2's S10 met now matches the written fallback rule; Team 3's S8 loses the duplicate Week 6 bullet but keeps its other shortfall; Team 6's and Team 9's S13 privacy scope is now explicit (both already partial); Team 4's contribution table and Team 1's "no in-range milestone" line are judged by the revised S13 wording.

## Validation

- `uv run pytest` - 393 passed.
- `markdownlint-cli2 "A5/grading_prompt.md"` - 0 errors.
- `git diff --check` - clean.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

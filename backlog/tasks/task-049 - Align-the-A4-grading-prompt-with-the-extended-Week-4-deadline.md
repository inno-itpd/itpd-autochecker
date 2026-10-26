---
id: TASK-049
title: Align the A4 grading prompt with the extended Week 4 deadline
status: Done
assignee: []
created_date: '2026-10-26 10:09'
updated_date: '2026-10-26 10:09'
labels: []
dependencies: []
ordinal: 49000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The A4 prompt, config, and tests assumed one Saturday 24 October cutoff. The instructor extended Week 4 to Sunday 25 October for every team except Team 2 - OK_10938_assignsubmission_file, which has Monday 26 October. The review also found content contradictions in S1, S2, S12, S14, S15, and the project views query.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 The prompt separates the original Saturday 24 October and effective Sunday 25 / Monday 26 deadlines, defines ISSUE_CUTOFF per team, and uses the team cutoff in every live-state segment.
- [x] #2 S1 accepts 2026-10-24, 2026-10-25, or 2026-10-26, never after the team cutoff, and requires the SPRINT-04 milestone to match **Due:**.
- [x] #3 S2 has no fixed estimate floor, requires every open non-Won't-Have product-backlog story to carry Story Points, and its partial and missing criteria are mutually exclusive.
- [x] #4 S12 and S14 treat a late tag and a lagging site as evidence caveats only; S15 removes the root README from met and accepts a link at another commit when the target exists.
- [x] #5 The views query selects fields, groupByFields, and sortByFields, and the docs name the route for a view's columns.
- [x] #6 The config and tests carry the per-team cutoff, the prompt carries both effective cutoffs, and a stale 2026-10-24T23:59:59 cutoff cannot survive.
- [x] #7 uv run pytest and markdownlint-cli2 pass on the changed Markdown.
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
Decisions: keep `A4/itpd` pinned at `35c9294`; record the extension in `A4/grading_prompt.md` Assignment parameters rather than the pinned syllabus, which still says Saturday 24 October; use Sunday 25 October 23:59 for the eight teams and Monday 26 October 23:59 for `Team 2 - OK_10938_assignsubmission_file`; accept 2026-10-24, 2026-10-25, or 2026-10-26 for `SPRINT-04` but require the GitHub milestone to match `**Due:**`; judge every open non-`Won't Have` product-backlog story in S2; keep a late tag and a lagging site as evidence caveats; record the root README as a note; accept a report link at another commit when the target exists; mark S1, S2, S8, S10-S16 `unverified` for Team 2 before its cutoff.

Validation: `uv run pytest -q` -> 327 passed; `markdownlint-cli2 A4/grading_prompt.md AGENTS.md` -> 0 issues; the `views` query validates against the `ProjectV2View` schema (`fields`, `groupByFields`, `sortByFields`); repo-wide `markdownlint-cli2 "**/*.md"` still flags pre-existing A3 feedback files and `TODO.md`, left untouched.
<!-- SECTION:NOTES:END -->

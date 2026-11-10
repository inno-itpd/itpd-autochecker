---
id: TASK-055
title: Add the semantic pass dimensions to A6
status: Done
assignee: []
created_date: '2026-11-10 06:10'
updated_date: '2026-11-10 06:10'
labels: []
dependencies: []
priority: medium
ordinal: 55000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Week 6 is the first assignment after A5 that carries a semantic companion pass: its compliance reports exist for all teams, but the semantic agent has no dimension definitions to read and `ASSIGNMENT_CONFIG["A6"]` has no `semantic_dimensions`, so `scripts/check_semantic_feedback.py A6` cannot validate a companion. The five A5 dimensions do not transfer: Week 6 grades analytics and observability rather than deployment and tests, so the prompt needs its own dimensions with their segment mapping, adequacy questions, probes, and verdict bands, and the config must carry the same names in the same order.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 A6/grading_prompt.md carries a `## Semantic feedback` section after the status guide: the companion-file handoff, the five dimensions in order with their segment mapping and question, per-dimension probes and verdict bands, and the guardrails.
- [x] #2 ASSIGNMENT_CONFIG["A6"]["semantic_dimensions"] carries the same five dimensions in the same order as the prompt's dimension headings.
- [x] #3 AGENTS.md, agents/README.md, and docs/semantic-feedback-format.md name A6 beside A5 where they state which assignments run a semantic pass, and the format doc records the A6 dimensions.
- [x] #4 A test fails when an assignment's prompt dimension headings and its configured semantic_dimensions disagree in name, order, or presence, for every assignment.
- [x] #5 uv run pytest and markdownlint-cli2 pass on the changed files, and the A5 semantic section is unchanged.
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
# Implementation plan: A6 semantic dimensions

## Status

Done in this session:

- `A6/grading_prompt.md` carries `## Semantic feedback` between the status guide (S18) and `## Assignment-specific procedure deltas`, 74 lines.
- `tools/autochecker/assignment_config.py` carries `A6["semantic_dimensions"]` in the prompt's order.
- `AGENTS.md`, `agents/README.md`, and `docs/semantic-feedback-format.md` name A6 and record its dimensions.
- `tests/test_assignment_prompts.py` pins the prompt dimension headings to the configured list for every assignment.

## Decisions locked

- Placement: inline in `A6/grading_prompt.md`, matching A5, rather than a separate file.
  The dimension-to-segment map then sits beside the segments it references, and the semantic agent's existing `rg`-to-heading read already bounds the read.
- Five dimensions, in A5's shape: `Measurement` (S3-S5), `Observability` (S6, S7, S10), `Plan` (S1, S2, S11, S16), `Customer loop` (S12-S14), `Publication` (S8, S9, S15, S17, S18).
  Every one of the 18 segments belongs to exactly one dimension.
- `Plan` absorbs S11 (threshold review) because the review steers the goal forecast; the three names shared with A5 keep A5's question, with `Plan` extended.
- The schema stays in `docs/semantic-feedback-format.md`; A6 defines dimensions and probes only, not a second contract.
- A5 is untouched, so the two prompts stay comparable.

## What not to do

- Do not split A5's section or A6's into separate files as part of this task; a split would be one mechanical refactor for both assignments.
- Do not add dimension names anywhere but the prompt and the config; the test keeps them in step.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
# Decisions

- The section lives inline in the prompt: the semantic agent already reads only `## Semantic feedback` by heading boundary, so a separate file saves one `rg` and adds a new path convention to four instruction files and the checker docs. Auditability came from the drift test instead.
- The dimension-to-segment map covers all 18 segments, as A5's covers all 14. S11 sits in `Plan` because it is the steering loop, not a second rubric.
- The model card wording follows A5's: verdict bands are `thin` and `not yet adequate`, `adequate` needs no band, and the guardrails keep the status-vocabulary ban and the conflict rule.

# Validation

- `uv run pytest` - 465 passed.
- `markdownlint-cli2` on the changed Markdown - 0 issues; the repo-wide run still reports the pre-existing `TODO.md` and A4/A5 `danila-feedback.md` findings, untouched here.
- Negative checks on the new test: a swapped dimension order, a missing dimension, and a prompt section with no configured dimensions each raise; the green run does not pass vacuously.
- `git diff --stat`: A6 prompt +74, config +7, test +16, three docs one line each.

# Follow-up

- The A6 batch now owes one semantic agent per team after each report is final; there is no A6 reference file yet, and `docs/semantic-feedback-format.md` already allows its example to be absent until the batch runs.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
## Summary

A6 now defines the same optional semantic companion pass as A5, with Week 6's own dimensions.

- `A6/grading_prompt.md` gained `## Semantic feedback`: the handoff paragraph, a five-row dimension table, one section per dimension (question, probes, `thin` and `not yet adequate` bands), and the guardrails.
- `ASSIGNMENT_CONFIG["A6"]["semantic_dimensions"]` lists `Measurement`, `Observability`, `Plan`, `Customer loop`, `Publication`, so `scripts/check_semantic_feedback.py A6` can validate a companion.
- The docs that described the semantic pass as A5-only now name both assignments, and the format doc records the A6 dimension list.
- A new parametrized test pins every assignment's prompt dimension headings to its configured list, so a rename cannot drift one side only.

## Tests

- `uv run pytest` - 465 passed.
- `markdownlint-cli2` on the changed Markdown - 0 issues.
- Negative checks confirm the drift test rejects a reordered, shortened, or absent dimension list.

## Risks and follow-ups

- The A6 batch must now run one semantic agent per team after its compliance report is final; no A6 companion example exists yet, which the format doc already anticipates.
- A5 is untouched, so the two sections stay directly comparable for a later refactor if the team ever decides to split them.
<!-- SECTION:FINAL_SUMMARY:END -->

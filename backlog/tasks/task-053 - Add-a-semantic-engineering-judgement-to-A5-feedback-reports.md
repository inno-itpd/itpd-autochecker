---
id: TASK-053
title: Add a companion semantic feedback file for A5
status: In Progress
assignee: []
created_date: '2026-11-03 08:45'
updated_date: '2026-11-03 08:55'
labels: []
dependencies: []
references:
  - docs/grading-feedback-format.md
  - A5/grading_prompt.md
  - agents/grader.md
  - TODO.md
  - backlog/tasks/task-050 - Improve-grader-instructions-after-the-A4-regrade.md
documentation:
  - A5/itpd/assignments/assignment-5.md
  - docs/grader-policy.md
  - docs/grading-feedback-format.md
priority: medium
ordinal: 53000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The A5 structural reports answer what is missing and what is met, but not whether an artifact does its job. Add a companion `agent-semantic-feedback.md` beside each `agent-feedback.md`: five A5 dimensions (Setup, Tests, Plan, Customer loop, Publication), a three-level verdict (`adequate`, `thin`, `not yet adequate`), one evidence-linked prose assessment per dimension, and a `## Where to start` list. It is written from the structural report's existing evidence, never collects new evidence, and never changes a status, gap, assessment, or grade. A trial file for Team 5 is written and passes the checker; the remaining eight teams are written in a later session. The format, the A5 dimension definitions, the grader instruction, and the checker are in place. The release export stays `## Summary`-only; the semantic file is report-only and sits beside the full report.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 docs/semantic-feedback-format.md defines the companion file, its path beside agent-feedback.md, the metadata, the five A5 dimensions, the verdict scale, the required blocks, the evidence-link rule, the forbidden vocabulary, and the non-scoring rule; a team without the file stays valid.
- [ ] #2 A5/grading_prompt.md defines the five A5 dimensions with their segment mapping, the adequacy question, the probes, the verdict signals, and the guardrails, including that a segment may be met while its dimension is thin.
- [ ] #3 agents/grader.md and AGENTS.md say when to write the file, that it uses only the structural report's evidence, that it never changes a status, and how a full regrade treats it.
- [ ] #4 scripts/check_semantic_feedback.py validates the schema against the format doc, compares the metadata with the sibling agent-feedback.md, checks the snapshot SHA in blob links, rejects the forbidden vocabulary, and runs markdownlint; tests cover a valid file and each rejection.
- [ ] #5 The Team 5 trial file exists, passes the checker, markdownlint, and the privacy scan, and is the reference example.
- [ ] #6 The remaining eight A5 teams each carry a semantic file written from their saved report and evidence in a later session.
- [ ] #7 The release export stays `## Summary`-only and the semantic file is documented as report-only; no extractor change is made.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
# Implementation plan: companion semantic feedback file

## Status

Done in this session:

- `docs/semantic-feedback-format.md` defines the companion file.
- `docs/grading-feedback-format.md` points at it and keeps it out of the report.
- `A5/grading_prompt.md` defines the five dimensions, the probes, the verdict signals, and the guardrails.
- `agents/grader.md` and `AGENTS.md` document when to write the file and the non-scoring rule.
- `tools/grader_tools/semantic_feedback.py`, `scripts/check_semantic_feedback.py`, and `tests/test_semantic_feedback.py` exist; the full suite passes.
- `itpd-assignments-feedback/A5/feedback/Team 5 - TmpTeam_10941_assignsubmission_file/agent-semantic-feedback.md` is the trial and the reference example.

Remaining:

- The other eight A5 teams. Write one file per team in a later session, from the saved report, with one writer per team.
- If a team's semantic file exposes a wrong status, schedule a regrade for that team; do not edit the status in the semantic pass.

## Decisions locked

- The semantic feedback is a separate file, not a report section: `itpd-assignments-feedback/<assignment>/feedback/<team_dir>/agent-semantic-feedback.md`.
  The structural report stays `agent-feedback.md` and keeps its canonical section list.
- Five dimensions, in order: `Setup`, `Tests`, `Plan`, `Customer loop`, `Publication`.
  Segment mapping: Setup S3-S4; Tests S5-S6; Plan S1-S2-S12; Customer loop S8-S9-S10; Publication S7-S11-S13-S14.
- Verdicts: `adequate`, `thin`, `not yet adequate`.
- The file is written from the structural report's evidence only: no new `gh` calls, no snapshot re-fetch, no new dump.
- It never changes a status, an `Evidence gaps` flag, `Manual review required`, the overall assessment, or the grade.
- The release export stays `## Summary`-only; the semantic file is report-only and is carried by the full report directory.
- No "mentor" wording; the mentor is the voice, not the label.
- A1-A4 are untouched; the schema is shared but the dimension list is per assignment.

## File schema

```markdown
# Assignment 5 Semantic Feedback

- Team: <n>
- Repository: `https://github.com/<org>/<repo>`
- Snapshot: `<40-character SHA>`
- Structural report: [`agent-feedback.md`](./agent-feedback.md)

## How to read this

<one short paragraph>

## Setup

**Verdict:** thin

**What works.** <one or two sentences>

**What breaks first.** <one or two sentences>

**What would make it adequate.** <one sentence>

**Evidence:**

- <a link and what it shows>

... Tests, Plan, Customer loop, Publication ...

## Where to start

- <2-3 imperative bullets>
```

The help block is `**What would make it stronger.**` when the verdict is `adequate`.
The full contract is in `docs/semantic-feedback-format.md`; the checker enforces it.

## Per-team pass for the remaining eight

1. Read the saved `agent-feedback.md`, `work/<team_dir>/payload.json`, and `work/<team_dir>/summary.md`.
2. Draft the five dimensions from the evidence already cited in the report.
   Use the Team 5 file as the reference for voice and depth: what works, what breaks first, what would change the verdict, and one evidence bullet per claim.
2a. Keep the verdict independent of the segment statuses: a `met` segment can be `thin`, and a `partial` segment does not make its whole dimension `not yet adequate`.
3. Write the file next to the report; do not touch `agent-feedback.md`.
4. Validate and privacy-scan:

   ```console
   uv run python scripts/check_semantic_feedback.py A5 "itpd-assignments-feedback/A5/feedback/<team_dir>/agent-semantic-feedback.md"
   uv run python scripts/scan_privacy.py A5 "<team_dir>" --feedback "itpd-assignments-feedback/A5/feedback/<team_dir>/agent-semantic-feedback.md"
   ```

5. Record the team and the two results.

## What not to do

- Do not re-audit segments or change statuses; a wrong status is a regrade, not a semantic-pass edit.
- Do not copy the `## Main issues to fix` list into `What breaks first`; say what the artifact can and cannot do yet.
- Do not compare teams, rank them, or use a grade.
- Do not use `met`, `partial`, `missing`, or `unverified` as prose.
- Do not write a dimension you cannot ground in the report's evidence.

## Verification

- `uv run pytest`
- `markdownlint-cli2 "**/*.md"`
- `scripts/check_semantic_feedback.py` on every A5 semantic file
- `scripts/scan_privacy.py ... --feedback` on every A5 semantic file
- One report without the companion still passes `check_feedback_report.py`
- `A5/extract_feedback.py` remains unchanged and still exports `## Summary` only
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
# Trial result (2026-11-03)

## What was built

- Companion-file format: `docs/semantic-feedback-format.md`.
- A5 dimension definitions: `## Semantic feedback` in `A5/grading_prompt.md`.
- Grader instruction: `## Semantic feedback` in `agents/grader.md`; `AGENTS.md` structure and helper list.
- Validator: `tools/grader_tools/semantic_feedback.py`, CLI `scripts/check_semantic_feedback.py`.
- Tests: `tests/test_semantic_feedback.py`, 15 cases.
- A5 dimensions in `ASSIGNMENT_CONFIG["A5"]["semantic_dimensions"]`.

## Trial file

`itpd-assignments-feedback/A5/feedback/Team 5 - TmpTeam_10941_assignsubmission_file/agent-semantic-feedback.md`, five dimensions:

- Setup: thin.
- Tests: thin.
- Plan: thin.
- Customer loop: thin.
- Publication: adequate.

The verdicts are independent of the report's 11 met / 3 partial: the report's statuses stay untouched.

## Validation

- `uv run pytest` - 434 passed.
- `markdownlint-cli2` on the touched Markdown - 0 errors.
- `scripts/check_semantic_feedback.py A5 <Team 5 file>` - OK.
- `scripts/scan_privacy.py A5 "Team 5 ..." --feedback <Team 5 file>` - no findings.

## Design corrections from the first proposal

- The semantic feedback is a companion file, not a `## Engineering judgement` report section; the report format stays unchanged.
- The checker compares the file's team, repository, and snapshot with the sibling `agent-feedback.md`, and the blob links with the snapshot SHA.
- The report-only export decision is recorded in the format doc; no extractor change.

## Remaining

- Eight A5 teams.
- One writer per team; do not touch `agent-feedback.md`.
- A wrong status found during the pass is a regrade for that team, not an edit in this pass.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

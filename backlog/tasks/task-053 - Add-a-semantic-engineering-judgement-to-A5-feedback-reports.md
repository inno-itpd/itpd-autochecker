---
id: TASK-053
title: Add a companion semantic feedback file for A5
status: Done
assignee: []
created_date: '2026-11-03 08:45'
updated_date: '2026-11-03 15:40'
labels: []
dependencies: []
references:
  - docs/grading-feedback-format.md
  - docs/semantic-feedback-format.md
  - A5/grading_prompt.md
  - agents/compliance-agent.md
  - agents/semantic-agent.md
  - agents/README.md
  - AGENTS.md
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
The A5 structural reports answer what is missing and what is met, but not whether an artifact does its job. Add a companion `agent-semantic-feedback.md` beside each `agent-feedback.md`: five A5 dimensions (Setup, Tests, Plan, Customer loop, Publication), a three-level verdict (`adequate`, `thin`, `not yet adequate`), one evidence-linked prose assessment per dimension, and a `## Where to start` list. A separate `agents/semantic-agent.md` writes it after the compliance report is final, verifies its own load-bearing claims against the snapshot at the saved SHA or the saved evidence, and never changes a status, gap, assessment, or grade. The compliance agent hands off a validated report and work directory and never writes the companion. A trial file for Team 5 is written and passes the checker; the remaining eight teams are written in a later session. The format, the A5 dimension definitions, both agent prompts, and the checker are in place. The release export stays `## Summary`-only; the semantic file is report-only and sits beside the full report.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 docs/semantic-feedback-format.md defines the companion file, its path beside agent-feedback.md, the metadata, the five A5 dimensions, the verdict scale, the required blocks, the evidence-link rule, the verification contract, the forbidden vocabulary, and the non-scoring rule; a team without the file stays valid.
- [x] #2 A5/grading_prompt.md defines the five A5 dimensions with their segment mapping, the adequacy question, the probes, the verdict signals, and the guardrails, including that a segment may be met while its dimension is thin and that the semantic agent verifies its own claims.
- [x] #3 agents/compliance-agent.md hands off the validated report and work directory; agents/semantic-agent.md and AGENTS.md say when to write the companion, that the report is a map rather than evidence, that the semantic agent verifies its load-bearing claims, that it never changes a status, and how a regrade treats it.
- [x] #4 scripts/check_semantic_feedback.py validates the schema against the format doc, compares the metadata with the sibling agent-feedback.md, checks the snapshot SHA in blob links, rejects the forbidden vocabulary, and runs markdownlint; tests cover a valid file and each rejection.
- [x] #5 The Team 5 trial file exists, passes the checker, markdownlint, and the privacy scan, and remains the voice and schema reference; it predates the claim ledger.
  The trial file is local until it is committed with the eight-team pass; the docs note that it may be absent on an earlier checkout.
- [x] #6 The remaining eight A5 teams each carry a semantic file written by the semantic agent from their saved report and verified evidence in a later session.
- [x] #7 The release export stays `## Summary`-only and the semantic file is documented as report-only; no extractor change is made.
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
# Implementation plan: companion semantic feedback file

## Status

Done in this session:

- `docs/semantic-feedback-format.md` defines the companion file.
- `docs/grading-feedback-format.md` points at it and keeps it out of the report.
- `A5/grading_prompt.md` defines the five dimensions, the probes, the verdict signals, and the guardrails.
- `agents/compliance-agent.md` (formerly `agents/grader.md`) and `AGENTS.md` document when to write the file and the non-scoring rule.
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

## Architecture update (2026-11-03)

The single grader prompt was split so compliance work and semantic judgement do not share one context window. This supersedes the earlier decision that the semantic file is written only from the report's evidence.

- `agents/compliance-agent.md` (renamed from `agents/grader.md`) owns the statuses, evidence, report, payload, summary, inventory, and SQLite handoff. It no longer writes `agent-semantic-feedback.md`; it leaves the work directory intact for the semantic agent.

- `agents/semantic-agent.md` owns the companion. It starts from the report as a map, verifies 2-4 load-bearing claims per dimension against the snapshot at the saved SHA or the saved evidence, records them in `work/<team_dir>/semantic-claims.json`, and writes only supported claims into the file. It never edits `agent-feedback.md` and never changes a status.

- `agents/README.md` documents the two roles, the handoff, the launch order, and the one-writer rule.

- Both harness wrappers are split: `.claude/agents/` and `.opencode/agents/` carry `compliance-agent.md` and `semantic-agent.md`.

- `docs/semantic-feedback-format.md`, `docs/grading-feedback-format.md`, and the A5 prompt's `## Semantic feedback` section now state the verification contract and the conflict-escalation rule.

- Phase 2 remains: a handoff generator, a claim-ledger validator, a semantic readiness gate, and per-role resume counters.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
# Trial result (2026-11-03)

## What was built

- Companion-file format: `docs/semantic-feedback-format.md`.
- A5 dimension definitions: `## Semantic feedback` in `A5/grading_prompt.md`.
- Grader instruction: `## Semantic feedback` in `agents/compliance-agent.md` (then `agents/grader.md`); `AGENTS.md` structure and helper list.
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

## Role split (2026-11-03)

Split the one-team review into `agents/compliance-agent.md` (renamed from `agents/grader.md`) and `agents/semantic-agent.md`, with wrappers and `agents/README.md`. The compliance prompt now ends at a validated report plus a handoff; the semantic prompt verifies its own claims, records them in `semantic-claims.json`, and escalates status conflicts instead of editing the report. The semantic contract in `docs/semantic-feedback-format.md`, `docs/grading-feedback-format.md`, and `A5/grading_prompt.md` was updated from 'use only the report's evidence' to 'the report is a map; verify the claims you rely on'.

Validation: `uv run pytest` 450 passed; `markdownlint-cli2` from the dev shell (0.21.0) reports 0 issues on the changed Markdown, including the wrappers; `scripts/check_semantic_feedback.py A5` still passes on the Team 5 reference file, `--ledger` passes with a matching report hash, and a stale hash exits 1. The claim-ledger validator, handoff generator, semantic readiness gate, and per-role resume counters are still Phase 2.

## Review fixes (2026-11-03)

- `semantic review` now refuses an existing companion; AGENTS launches `semantic review` only when the companion is absent and `semantic regrade` when it exists.
- `inventory.md` is a required compliance handoff; the semantic agent no longer writes it, so its write set is the companion plus `semantic-claims.json`.
- The verification contract is the A5 status-based omission rule, a 20-artifact read budget, an explicit stop on any missing or mismatched handoff item, and a no-snapshot stop.
- `scripts/check_semantic_feedback.py --ledger` compares `report_sha256` with the sibling report while the disposable ledger is present.
- The opencode semantic wrapper denies `edit`; tests cover the semantic prompt's commands and the wrapper tool policy.
- The trial file is deferred to the eight-team pass, so AC5 stays open and the docs say the example may be absent until then.

## Nine-team semantic pass (2026-11-03)

All nine A5 teams now carry `agent-semantic-feedback.md`. Teams 1, 2, 3, 4, 6, 7, 8, 9 were written in `semantic review`; Team 5 was rerun in `semantic regrade` and now carries a 24-claim ledger. Verdict totals across 45 dimensions: adequate 4, thin 35, not yet adequate 6; conflicts 0.

Validation for every team: `scripts/check_semantic_feedback.py --ledger` exits 0, both `scripts/scan_privacy.py --feedback` scans report `no findings`, and all nine compliance-report sha256 values are unchanged from the pre-pass baseline. `scripts/check_batch_ready.py A5` reports `ready`, `markdownlint-cli2` on the A5 feedback tree reports 0 issues, and `uv run pytest` reports 450 passed.

The Team 5 regrade corrected the trial file's claim that the generation path had no automated check: `backend/tests/conftest.py` sets `LLM_PROVIDER=fake` and `test_flow.py` exercises `/generate` and `/regenerate`. The Tests section now rests on `QR-02 QRT-01`'s pass criterion instead. Other Team 5 corrections: plan merge was 29 October, `## Deployment` names 248b766 only, and the unverifiable release-body/tag-ruleset claims were dropped.

One report-accuracy note, not a status conflict: Team 1's S7 evidence says `docs/features.md` carries twelve `##` capability entries; the snapshot has eleven. S7 remains `partial` on the other evidence, so no compliance regrade is scheduled.

AC5's 'predates the claim ledger' clause is superseded for Team 5: the regrade gave it a ledger, and it still passes the checker as the voice/schema reference. Team 8 needed an operator repair of two link typos (repository name `Team8TemporaryDebuggingGym` and one SHA character) before it validated; the ledger was unaffected.

The semantic files are report-only. `A5/extract_feedback.py` was not rerun because `dev.md` and `feedback_release.csv` already cover all nine teams and the semantic companion is not part of either export. Nothing is committed yet.
<!-- SECTION:NOTES:END -->

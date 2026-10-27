---
id: TASK-050
title: Improve grader instructions after the A4 regrade
status: Done
assignee: []
created_date: '2026-10-27 08:06'
updated_date: '2026-10-27 09:44'
labels: []
dependencies: []
ordinal: 50000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The 2026-10-26 A4 regrade exposed instruction gaps that cost a whole pass: no full-regrade mode (a full review starts by deleting the work directory), no audit of the saved report's claims, cutoff drift handled only by prose, S2 conflating project and issue fields, two conflicting Evidence-gaps rules, no schema home for advice, and missing validator invariants. Implement the agreed fixes in the shared guidance, the A4 rubric and the tooling, then migrate the five A4 reports. The Implementation Notes are the handoff: they record the failure evidence, the file-level plan, the cutoff-view contract, the suggested order and the verification.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 agents/grader.md documents a first-class `full regrade` mode that preserves `work/`, audits the saved report's claims, rebuilds `payload.json`, renders last, validates and returns a status diff, and the `full review` step-1 delete no longer applies to a regrade.
- [x] #2 docs/grading-feedback-format.md defines the optional `## Suggested next steps` between `## Main issues to fix` and `## Segment details` (0 or 1-3 one-sentence, artifact-linked bullets; no status effect; no "mentor" wording), and the validator, renderer, patch/regrade payload, inspector and parser accept it.
- [x] #3 docs/grader-policy.md states the status-changing evidence-gap rule and its precedence over assignment prompts; criterion-level uncertainty is an `**Evidence:**` caveat. Team 4's S2 gap clears and the report returns to `complete`.
- [x] #4 A4/grading_prompt.md adds the S1 velocity-history, S2 project-vs-issue-field (with the admin:org caveat), S8 cutoff labels, S9 code-style, S11 transcript and script timing, S12 tag timing and S15 latest-green-run checks, each with a "what does not count" example.
- [x] #5 evidence.sqlite imports collected timelines into `issue_events`, records the team cutoff, and exposes `issue_state_at_cutoff`; the collector can collect all timelines opt-in; missing timelines are marked, both documented and tested.
- [x] #6 The validator enforces body `blob/<sha>` links against the snapshot SHA (team repo) or `ASSIGNMENT_CONFIG[assignment]["course_commit"]` (`inno-itpd/itpd`) and the optional-section schema, while the existing gap/count/Summary invariants stay green; tests cover both.
- [x] #7 AGENTS.md documents the re-grading workflow, the new section and the cutoff view; grader segment counts come from assignment_config.py.
- [x] #8 The five A4 reports use `## Suggested next steps` (advice moved and unlabelled, at most three each), Team 4 has no S2 gap, all validate and pass privacy, check_batch_ready.py A4 is ready, and extraction regenerates dev.md and feedback_release.csv.
- [x] #9 Reports without the new section (A1-A3 and older fixtures) still validate; no forced backfill outside A4.
- [x] #10 uv run pytest and markdownlint-cli2 "**/*.md" pass.
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
# Implementation brief (handoff)

This task is the handoff. Work top to bottom; the sections below record the decisions, the failures that justify each rule, the file-level plan, the cutoff-view contract, and the verification.

## Decisions locked (2026-10-27)

- Scope: shared guidance plus the A4 rubric; A1-A3 rubrics stay untouched unless shared text changes.
- Advice section: a new optional top-level `## Suggested next steps` section between `## Main issues to fix` and `## Segment details`.
  The name is deliberately neutral: no "mentor" framing, no claim that a mentor wrote it, and no "mentor" wording in the reports or the docs.
  It holds 1-3 bullets, one sentence each, starts with a verb, cites the artifact it rests on, and never feeds a status.
- Export: unchanged. Only `## Summary` goes into `feedback_release.csv`; the new section is report-only and `extract_reports.py` ignores it.
- Evidence gaps: only a gap that could change the status sets `Evidence gaps: yes`.
  Criterion-level uncertainty that cannot change the status is an `**Evidence:**` caveat, never a gap and never `**Why not met (unverified):**`.
  This policy takes precedence where an assignment prompt says "an evidence gap for that criterion".
- Regrade: a first-class `full regrade` mode in `agents/grader.md`, not an operator-only delta.
- Tooling: validator invariants, an `issue_state_at_cutoff` SQLite view, collector support, and tests.

## Evidence from the A4 regrade (why each rule exists)

- S2, Team 4: the saved report kept `Evidence gaps: no` by reading `gh project field-list` as proof for the issue fields.
  The org `issueFields` route needs `admin:org` (404) and the issue sidebar is unreadable; project fields are a different family.
  The regrade added a gap; under the status-changing-gap decision it must instead be an `**Evidence:**` caveat, because the verified unset `Story Points`/`Priority` values already fix S2 at `partial`.
- S1: Team 1's saved shortfall claimed the Sprint Backlog linked SPRINT-03's milestone; the snapshot links `milestone/2`, SPRINT-04's milestone.
  Team 5's saved evidence called 21 "the stories the milestone held when planned", but all three stories were milestoned on the review day and the plan's fields were committed after the stories closed.
- S8: Team 3's `user-story`/`task` labels were removed at 21:16:32Z, after the 20:59:59Z cutoff; the current clean state is post-cutoff.
- S9: Team 4's `AGENTS.md` states the commit format and the branch naming but no code style, and `CONTRIBUTING.md` has none either; the saved pass treated the conventions as complete.
- S11: Team 6's transcript is one speaker turn per line, not one sentence per line (171 of 256 timestamped lines carry several sentences).
  Team 3's script's first commit is three days after the meeting it prepares.
- S15: Team 6's saved report cited a workflow run list instead of the green run URL; Team 4's and Team 5's saved runs were stale or misidentified.
- S12: Team 1's tag is 21:13:41Z, after the 20:59:59Z cutoff.
- Privacy: Team 1's report quoted a `week4-...` branch name that embedded a member-name token. The fix is to drop the branch name, not to add a note; the report scan is what catches it.

## Work plan

### 1. agents/grader.md

- Modes: `full review`, `full regrade`, `partial regrade`, `segment inspect`; add a short selection table (first review / whole re-audit / named segments / read-only).
- `full regrade` contract:
  - keep `work/` (never `rm -rf`); reuse `pdf-info.json`; re-fetch the snapshot at the same SHA;
  - refresh `summary.md`/`evidence.sqlite` from the saved dumps with `--summary`; collect a specific dump only when a claim needs it;
  - treat `agent-feedback.md` and `payload.json` as a draft;
  - audit every segment (below), rebuild the payload, write the payload first and render last so `check_batch_ready.py` sees report mtime >= payload;
  - validate and run both privacy scans (report and snapshot);
  - return the standard line plus a status diff and a corrections list.
- `full review` step 1: delete `work/` only for a first review or when the operator explicitly asks; a regrade must never use that step.
- Audit step, per segment: state the saved claim, the evidence checked, and keep/correct/withdraw; no status change on prose alone; every changed claim gets an `**Evidence:**` bullet.
- Cutoff procedure: add `## Judging at ISSUE_CUTOFF` (or reference the shared one and the SQL view) covering labels/type/fields (`issues/<n>.timeline.json`), milestones, plan/changelog (`paths/<path>.json` and PR merge times), and runs (`head_sha`).
- Counts: read the segment count from `assignment_config.py`, not "13 for A3".
- Return-value contract for a regrade: standard line + `changes: S<n> old -> new (reason)` or `no status changes`, plus `corrections: <claim> -> <evidence>`.

### 2. docs/grading-feedback-format.md

- Add the optional `## Suggested next steps`, after `## Main issues to fix` and before `## Segment details`.
- Rules: omit the section entirely when there is no grounded advice; otherwise 1-3 bullets, one sentence each, start with a verb, cite the artifact, never repeat a Main issues bullet, never state a status/grade/"unverified"; never a status input.
- No "mentor" wording; the section is the checker's suggestions.
- Update the required-section order and the "do not add extra top-level sections" wording.
- State the Summary-only export.
- Backward compatibility: a report without the section still validates.

### 3. docs/grader-policy.md

- Rewrite the Evidence-gaps rule around the status-changing test, with explicit precedence over assignment prompts, and show where a criterion-level caveat goes.
- Privacy: check branch/tag/URL names against the member tokens before quoting them; rewrite the reference if it embeds a name; re-run the report scan.
- Spell out the two scans: `scan_privacy.py ... --feedback` scans the report; the snapshot scan runs before extraction.
- Say the report must not use "mentor" wording.

### 4. A4/grading_prompt.md

- S1: planned velocity is the sum of the stories the milestone held at planning; read `milestoned`/`demilestoned` and the plan's `paths/` history; a prose or rounded figure is a shortfall; record post-planning edits as a caveat.
- S2: a project field-list result is never evidence for the issue fields; the org route needs `admin:org`; the sidebar is the fallback; if neither is readable, record an `**Evidence:**` caveat (not a gap) because the verified unset values fix the status; per-issue values prove the field name, data type and value only.
- S8: the six labels must be retired at the cutoff; read `labeled`/`unlabeled` events; a post-cutoff removal is a shortfall.
- S9: code style is a separate required convention; a commit or branch rule, or a placement rule, is not code style; read `AGENTS.md` and `CONTRIBUTING.md`.
- S11: the transcript's one-sentence-per-line form; the script's first commit against the meeting date; post-cutoff edits as drift.
- S12: the tag time against the cutoff.
- S15: the latest green run at the snapshot SHA, linked by run URL; a run list or a green run on another SHA is not the link; a Markdown wrapper is a submission-format shortfall.
- Add a "what does not count" counter-example beside each of these checks.

### 5. Tooling

- `tools/grader_tools/feedback_report.py`: headers/order/parse/render for the new section; a `next_steps` payload key; update `SECTION_ORDER` and the render signature.
- `scripts/render_feedback_report.py`, `scripts/patch_feedback_report.py` (`SECTION_BODY_KEYS`), `scripts/regrade_feedback_segments.py`, `scripts/inspect_feedback_segments.py`: carry `next_steps` through payloads, patches and predictions.
- `tools/grader_tools/validate.py`: new-section schema (0 or 1-3 bullets, no empty heading); body `blob/<sha>` check: for the team repo the SHA must equal `Snapshot reviewed`; for `inno-itpd/itpd` it must equal `ASSIGNMENT_CONFIG[assignment]["course_commit"]`; non-blob links are exempt. The existing gap/table/assessment/Summary/unresolved invariants stay green.
- `tools/grader_tools/extract_reports.py`: confirm the new section is ignored; add a test.
- `tools/grader_tools/evidence_sqlite.py` and `scripts/collect_github_evidence.py`: events table, cutoff row, cutoff view, and an opt-in all-timelines collection mode.

### 5a. Cutoff view contract

- `issue_events(issue_number INTEGER, event TEXT, label_name TEXT, milestone_title TEXT, created_at TEXT, actor_login TEXT)`: one row per event from `issues/<n>.timeline.json`.
- `cutoffs(team_dir TEXT, cutoff TEXT)`: one row from `issue_cutoff_for` (Team 2's later cutoff must work).
- `issue_state_at_cutoff` view: `labels_at_cutoff` (labeled minus unlabeled before the cutoff), `milestone_at_cutoff` (last milestoned/demilestoned), `state_at_cutoff` (closed/reopened), and a `has_timeline` marker for issues without one.
- Type and issue-field values have no timeline: the view cannot reconstruct them; document that the report reads the current value plus the timeline.
- Collector: opt-in `--timelines` (all issues, or a listed set) with its API cost documented; `--summary` rebuilds the events from the saved dumps without calling `gh`.
- Tests: label add/remove before and after the cutoff; milestone move; close/reopen; missing timeline.

### 6. AGENTS.md

- Add a "Re-grading a batch" workflow after "Reviewing teams": full regrade mode, preserved work dirs, gate, extraction, privacy, commit.
- Update the Exports note (Summary only; the new section is ignored).
- Document the new section, the cutoff view and the collector flag.
- Update the grader mode list and the script list.

### 6a. A4 reports backfill

- Move the advice bullets into the new section and strip the labels:
  - Team 1: "Mentor note (advice, not a rule violation): ...".
  - Team 3: two "Mentor note, advice and not a rule: ...".
  - Team 4: two "Advice, not a rule violation: consider ...".
  - Team 5: "**Next step (advice, not a shortfall):** ...".
  - Team 6: "Advice, not a shortfall: ...".
- Each moved bullet starts with a verb and keeps its citations; at most 3 per report.
- Team 4: S2 `Evidence gaps: no`; delete `**Why not met (unverified):**`; add the definitions caveat to `**Evidence:**`; set the `Manual review required` row to `no`; the unresolved section becomes `No manual review required. All evidence was accessible`; the overall status becomes `complete`.
- Re-render from payloads, validate, privacy-scan, run the gate, re-extract.

### 7. Verification

- `uv run pytest`
- `markdownlint-cli2 "**/*.md"`
- `check_feedback_report.py` on all five reports, plus one report without the section (backward compatibility) and one with it.
- `check_batch_ready.py A4` ready.
- `A4/extract_feedback.py` writes 5 rows.
- Report and snapshot privacy scans.
- Cutoff query: Team 3's `user-story` label is present at 2026-10-25T20:59:59Z and absent after 21:16:32Z.
- `render_feedback_report.py` with a payload carrying `next_steps`.

### 7a. Commit

- Commit the submodule first (reports + exports), then bump the outer pointer, via `commit-itpd`; include the Harness/Model lines.

## Touch points

- Files: `agents/grader.md`, `docs/grader-policy.md`, `docs/grading-feedback-format.md`, `A4/grading_prompt.md`, `AGENTS.md`, `tools/grader_tools/{feedback_report.py,validate.py,extract_reports.py,evidence_sqlite.py}`, `scripts/{render_feedback_report.py,patch_feedback_report.py,regrade_feedback_segments.py,inspect_feedback_segments.py,collect_github_evidence.py}`, `tests/{test_feedback_report.py,test_validate.py,test_render_feedback_report.py,test_segment_workflows.py,test_extract_reports.py,test_evidence_sqlite.py,test_project_queries.py,report_builder.py}`.
- `ASSIGNMENT_CONFIG[assignment]["course_commit"]` already exists (A1 `fe58ba7`, A2 `a949e8d`, A3 `23b22a6`, A4 `35c9294`); use it, do not add it.
- The validator already enforces the segment/table/gap/manual-review/assessment invariants, Summary 3-5 and the unresolved section; keep those green rather than re-adding them.

## Suggested order

1. Format + parser/validator/payload plumbing + tests (smallest complete unit).
2. `full regrade` mode in `agents/grader.md` and the `AGENTS.md` workflow.
3. Cutoff events/view + collector flag + tests.
4. A4 rubric updates.
5. Report migration + Team 4 gap + extraction.
6. Full checks, then commit.

## Risks / compatibility

- The new section is optional; A1-A3 reports and older batches remain valid.
- Changing `SECTION_ORDER` touches the parser, renderer, patcher, inspector and tests; update them together.
- The body-SHA check must allow the pinned course repo and live links, or it will flag valid citations.
- `check_batch_ready` requires report mtime >= payload: write payload first, render last.
- The cutoff view is only as complete as the collected timelines; mark missing timelines instead of guessing.
- Team 4's manual-review flip to `no` follows the gap decision; `dev.md` and the CSV must be regenerated.

## Open points

- All-timeline collection cost: keep it opt-in, document the request count.
- Revisit the S2 definitions caveat if a future token can read the organization `issueFields` list.

## Additional detail (captured after review)

- New section shape: exactly `## Suggested next steps`, a bullet list only, no nested bullets, no `None`, and no empty heading; place it after `## Main issues to fix` and before `## Segment details`; omit the section entirely when there is no grounded advice.
- Both `dev.md` and `feedback_release.csv` stay Summary-only, so the new section never reaches the export.
- Extra touch points: `tests/test_grader_prompt_commands.py` (commands added to `agents/grader.md`), `tests/test_assignment_prompts.py` (A4 prompt text), `tests/fixtures/` (timeline fixtures), and the `.opencode/agents/grader.md` and `.claude/agents/grader.md` wrappers (verify they still point at the canonical prompt).
- The `full regrade` mode must name the one-writer rule and the `check_batch_ready.py --active` gate, so a regrade batch never extracts while another writer is running.

## Implementation outcome (2026-10-27)

### Tooling and format

- `## Suggested next steps` is the only optional top-level section, between `## Main issues to fix` and `## Segment details`.
  The parser reads it as `next_steps_body` (`None` when absent), the renderer accepts a keyword-only `next_steps_body`, the validator enforces 1-3 single-level bullets, no empty heading, no `None`, and no third-party framing, and the render/patch payloads accept `next_steps` (0-3; an empty list removes the section).
  The regrade subset carries `sections.next_steps` through, and the inspector reports a predicted "next steps updated" change.
  The extractor never sees it, and a test pins that `dev.md` and `feedback_release.csv` stay Summary-only.
- The validator's body-citation rule checks full-SHA `blob/<sha>` links: the team repository must cite `Snapshot reviewed`, `inno-itpd/itpd` must cite the assignment's `course_commit`, branch refs such as `blob/main` are live links and exempt, other repositories are exempt, and `**Why not met (verified/unverified):**` bullets may cite an off-snapshot commit to prove an artifact was not submitted.
  That last exemption keeps the existing A2 Team 7 report valid without a backfill while the rule still guards positive evidence.
- The evidence-gap policy now states the status-changing test and its precedence over assignment prompts; criterion-level uncertainty goes into `**Evidence:**`, never a gap and never `**Why not met (unverified):**`.
- The privacy policy names the branch/tag/URL name check, the two scans, and the no-third-party-framing rule.

### Regrade mode and evidence database

- `agents/grader.md` has the four-mode selection table and a first-class `full regrade`: it keeps `work/`, re-fetches only `snapshot/` at the saved SHA, refreshes `summary.md`/`evidence.sqlite` with `--summary`, audits every segment, rebuilds the payload, renders last, validates, runs both privacy scans, names the one-writer rule and the operator's `--active` gate, and returns `changes:` and `corrections:` lines.
  The step-1 `rm -rf` is now explicitly full-review-only.
- `AGENTS.md` documents the re-grading workflow, the optional section, the cutoff view, and the split of segment counts from `assignment_config.py`.
- `evidence.sqlite` adds `issue_events`, `cutoffs`, the `issue_state_at_cutoff` view (`labels_at_cutoff`, `milestone_at_cutoff`, `state_at_cutoff`, `has_timeline`) and reads saved `issues/<n>.timeline.json` in every rebuild.
  The cutoff comes from `issue_cutoff_for`, so Team 2's Monday cutoff is read and tested.
  The collector's opt-in `--timelines` collects every issue or a listed set at one paginated request per issue; `--summary` rebuilds the events without calling `gh`.
  A missing timeline is marked with `has_timeline = 0`, never guessed.

### A4 rubric and report migration

- The A4 status guide adds the S1 planning-time milestone history and plan path history, the S2 project-field-versus-issue-field split with the `admin:org` caveat, the S8 cutoff label events, the S9 code-style convention, the S11 transcript line form and script timing, the S12 tag time, and the S15 snapshot-SHA green runs and Markdown wrapper.
  Each of the seven checks has a `**What does not count:**` counter-example.
- The five A4 reports were re-rendered from their payloads: the advice bullets moved to `## Suggested next steps` and lost their labels, each is verb-first and at most three.
  Teams 1, 4, 5, and 6 got the S2 definitions caveat and lost the S2 gap, because the verified unset values already fixed the status; Team 3 keeps its S2 gap because an unread option list could still change its `met`, and Team 6 keeps its S11 gap.
  Team 4 is now `Automatic review status: complete` with `Manual review required: no` and the no-review sentence.
  `dev.md` and `feedback_release.csv` were regenerated with 5 rows.

### Validation

- `uv run pytest` -> 378 passed.
- `scripts/validate_feedback_report.py` passes on all five A4 reports and on every A1-A3 report; a report without the optional section still validates.
- `scripts/check_feedback_report.py` passes on the five A4 reports, and `markdownlint-cli2` on every changed Markdown file reports 0 issues.
  The repo-wide `markdownlint-cli2 "**/*.md"` still reports the pre-existing findings in the A2/A3 instructor `denis-feedback.md`/`danila-feedback.md` files and the untracked `TODO.md`; this task leaves them untouched, as earlier tasks did.
- The report privacy scans on all five A4 reports report no findings; the snapshot scans report only the teams' own repository findings (graded material, not report leaks).
- `scripts/check_batch_ready.py A4` -> ready, 5 teams, no refusals.
- Cutoff query on Team 3's saved timelines: `issue_state_at_cutoff` keeps `user-story` on the issues at the cutoff, and `issue_events` shows the 21:16:35Z removal after it.
- `scripts/render_feedback_report.py` was exercised with the five payloads carrying `next_steps`, and a unit test renders and validates a payload with the key.
<!-- SECTION:NOTES:END -->

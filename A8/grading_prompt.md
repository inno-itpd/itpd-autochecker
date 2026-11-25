# Assignment 8 Grading Criteria

> **Draft scaffold — not yet a rubric.**
> The segment contract below is fixed, but the per-segment criteria are still to be written from `A8/itpd/assignments/assignment-8.md`.
> Do not run a compliance review against this file until the draft marker is removed.

This rubric is for the compliance agent that reviews ITPD Assignment 8 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/compliance-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grading-policy.md`.
This file states only what is specific to Assignment 8 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `753d81e9c8b7b78261674c8d4836ef4e4b01d583`.
If the checked-out submodule differs from that commit, read each file with `git -C A8/itpd show 753d81e9c8b7b78261674c8d4836ef4e4b01d583:<path>`.

- `A8/itpd/assignments/assignment-8.md` — the student-facing brief: Parts 1–13, What Good Looks Like, the repository report contents, the Moodle report contents, the submission procedure, and the checklist.
- `A8/itpd/requirements/` — the rules the week applies, including the Week 8 usability results and configuration-management rules.
- `A8/itpd/guides/configuration-management.md` — the method for the configuration plan and its goal-based evaluation.
- `A8/itpd/course/syllabus.md` — the Week 8 objectives and deliverables and the Saturday 21 November deadline.
- `A8/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the deadline policy.

Apply every rule marked `**Since: W1**` through `**Since: W8**`.

## Assignment parameters

- Report title: `# Assignment 8 Compliance Feedback`
- Week: `W8`
- Course materials: `A8/itpd` at `753d81e9c8b7b78261674c8d4836ef4e4b01d583`
- Primary index artifact: `reports/week-08/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-8.md`.
- Week window: from Friday 13 November 2026, 00:00 Innopolis time, `2026-11-13T00:00:00+03:00`.
  The syllabus gives the Week 8 class week as 13 to 19 November 2026; the submission is due on Saturday 21 November, and the window runs from that Friday to `ISSUE_CUTOFF`.
- Soft deadline: none; `course/rules.md` gives every group submission from Week 4 to Week 9 a single hard deadline, and `course/syllabus.md` and `assignments/assignment-8.md` state the same date.
- Hard deadline: Saturday 21 November 2026, 23:59, as the pinned `course/syllabus.md`, `course/rules.md`, and `assignments/assignment-8.md` state it.
- No per-team deadline override exists for Week 8: every team's deadline is Saturday 21 November 2026, 23:59.
- `ISSUE_CUTOFF`: `2026-11-21T23:59:59+03:00` for every team.
  Every later reference to `ISSUE_CUTOFF` means that cutoff, and `**Evidence:**` states the cutoff used.
- Hard deadline of the following week: Saturday 28 November 2026, 23:59, the deadline the Week 9 syllabus block gives and the due date `SPRINT-09`'s GitHub milestone carries.
- The time zone is not stated in the materials; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A8/submissions/<team_dir>/`; the Moodle export carries no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A8/work/<team_dir>/snapshot/`.

The segments, in order:

- S1: Sprint plan and milestones
- S2: Backlog refinement and task scheduling
- S3: UT-01 run and sanitized sessions
- S4: Results and conclusion
- S5: Instrumentation comparison
- S6: Findings
- S7: Triage and planned fixes
- S8: QR/QRT verdict and threshold
- S9: Configuration plan
- S10: Goal-based configuration evaluation
- S11: Glossary and risk register
- S12: Week 7 action points and open questions
- S13: Sprint Review
- S14: Review rework and testing-plan rows
- S15: REL-08 release
- S16: Sprint close and retrospective
- S17: Week report and submission
- S18: AI usage and Week 9 handoff

### Segment overview

Every checklist item and every coverage-table row, or named part of a row, of `assignment-8.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.
The mapping is written with the segment criteria in the next pass.

## Status guide

### S1 — Sprint plan and milestones

TODO: criteria pending.

### S2 — Backlog refinement and task scheduling

TODO: criteria pending.

### S3 — UT-01 run and sanitized sessions

TODO: criteria pending.

### S4 — Results and conclusion

TODO: criteria pending.

### S5 — Instrumentation comparison

TODO: criteria pending.

### S6 — Findings

TODO: criteria pending.

### S7 — Triage and planned fixes

TODO: criteria pending.

### S8 — QR/QRT verdict and threshold

TODO: criteria pending.

### S9 — Configuration plan

TODO: criteria pending.

### S10 — Goal-based configuration evaluation

TODO: criteria pending.

### S11 — Glossary and risk register

TODO: criteria pending.

### S12 — Week 7 action points and open questions

TODO: criteria pending.

### S13 — Sprint Review

TODO: criteria pending.

### S14 — Review rework and testing-plan rows

TODO: criteria pending.

### S15 — REL-08 release

TODO: criteria pending.

### S16 — Sprint close and retrospective

TODO: criteria pending.

### S17 — Week report and submission

TODO: criteria pending.

### S18 — AI usage and Week 9 handoff

TODO: criteria pending.

## Semantic feedback

`agent-semantic-feedback.md` is the optional companion file defined in `docs/semantic-feedback-format.md`.
The semantic agent writes it after the compliance report is final.
It never changes a status, an `Evidence gaps` flag, `Manual review required`, the overall assessment, or the grade; a segment may be `met` while its dimension is `thin`.

The five dimensions, in this order:

| Dimension | Segments | The question |
|-----------|----------|--------------|
| Results | S3, S4, S5, S8 | Do the sessions and the results support the conclusion the team draws, and is the verdict earned? |
| Configuration | S9, S10 | Is the configuration plan a real inventory, and does the evaluation judge the configuration by the goals it serves? |
| Plan | S1, S2, S11, S15, S16 | Is the run sprint a forecast the team could steer by, and does its release leave Week 9 a clean start? |
| Customer loop | S12, S13, S14 | Did the results review change the product or the plan, and did the change reach the artifacts? |
| Publication | S17, S18 | Can a reader who trusts the public record find the results, the configuration judgement, and the handoff? |

### Results

TODO: dimension guidance pending.

### Configuration

TODO: dimension guidance pending.

### Plan

TODO: dimension guidance pending.

### Customer loop

TODO: dimension guidance pending.

### Publication

TODO: dimension guidance pending.

### Guardrails

TODO: dimension guardrails pending.

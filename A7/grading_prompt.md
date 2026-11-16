# Assignment 7 Grading Criteria

This rubric is for the compliance agent that reviews ITPD Assignment 7 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/compliance-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grading-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 7 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `d7bcb1b24c142df8377da11ac5a1b4854e317fba`.
If the checked-out submodule differs from that commit, read each file with `git -C A7/itpd show d7bcb1b24c142df8377da11ac5a1b4854e317fba:<path>`.

- `A7/itpd/assignments/assignment-7.md` — the student-facing brief: Parts 1–14, What Good Looks Like, the repository report contents, the Moodle report contents, the submission procedure, and the checklist.
- `A7/itpd/requirements/usability-testing-requirements.md` — where the test lives, the test record and its index, the participant profile, the participants, the tasks, the protocol, the instruments, the instrumentation, the analysis, the consent, the private data repository, the public evidence, the results and findings, the triage, and the Week 8 execution.
- `A7/itpd/requirements/weekly-report-requirements.md` — the weekly public report and its Week 7 `## Usability test` section, the AI usage report, declaring deviations, and the Moodle PDF.
- `A7/itpd/requirements/quality-requirements-requirements.md` — the `QR-nn` file, the six-part scenario, the `## QRT-nn` section, the four test levels, the Week 7 usability requirement and its manual test, the index, and the matrix.
- `A7/itpd/requirements/planning-requirements.md` — `docs/project-plan.md` with `## Sprints`, `## Releases`, and `## Quality Requirement Testing Plan`; the `**Due:**`, `**Sprint Backlog:**`, `**Planned Velocity:**`, and `**Actual Velocity:**` fields; the `REL-nn` block with `**Released:**` and `**Checked QRs:**`.
- `A7/itpd/requirements/sprint-ceremonies-requirements.md` — sprint planning, product backlog refinement, estimation, the Sprint Review, and the retrospective with its four sections, row counts, and columns.
- `A7/itpd/requirements/customer-meetings-requirements.md` — the weekly meeting as the Sprint Review, the design review's showing rules, the permission questions, the script, the report's `## Previous action points` and `## Previous open questions`, and the transcript.
- `A7/itpd/requirements/analytics-requirements.md` — `docs/analytics.md`, the event table as the one registry, the `source` field and its `usability-test` value, and the Week 7 rule that the test adds the events its tasks need.
- `A7/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only, the private usability-data repository and recordings folder, screenshot sanitization, and telemetry and personal data.
- `A7/itpd/requirements/repository-requirements.md` — the link check and its exclusions, permalinks and snapshots, CI, the environments, and the private usability-data repository.
- `A7/itpd/requirements/risks-requirements.md` — `docs/risks.md`, the risk's fields, the ratings, and the contingency.
- `A7/itpd/requirements/glossary-requirements.md` — `docs/glossary.md` and the term's one-sentence definition.
- `A7/itpd/requirements/general-requirements.md` — artifact and measurement terms, the `reports/week-NN/` vs `docs/` split, the identifier rules including `UT-nn` and `P-nn`, and traceability into later weeks.
- `A7/itpd/requirements/task-issues-requirements.md` — the `Task` issue type, its `### Requirements` section, and the pull request that closes it.
- `A7/itpd/requirements/releases-requirements.md` — `CHANGELOG.md`, Semantic Versioning, tags and their protection, the release title, and the upgrade note that ends with the `Full changelog` line.
- `A7/itpd/requirements/agent-instructions-requirements.md` — the team's root `AGENTS.md`, read as an AI trace.
- `A7/itpd/requirements/issue-tracking-requirements.md` — scheduling as the sprint's GitHub milestone, the `Responsible` and `Accountable` fields, the `Priority` field, and the matching assignees.
- `A7/itpd/requirements/pull-requests-requirements.md` — every change through a pull request, review and approval, and closing a task issue.
- `A7/itpd/guides/usability-testing.md` — the method for the test record, the participants, the tasks, the instruments, the instrumentation, the consent, the private data repository, the sessions, the results, the triage, and the retention.
- `A7/itpd/guides/validating-with-the-customer.md` — the method for the meeting's target, questions, agenda, roles, and tracing what changed.
- `A7/itpd/guides/planning-and-tracking.md` — the method for the sprints, the release order, the release body, and the retrospective.
- `A7/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the deadline policy including the Week 7 Sunday.
- `A7/itpd/course/syllabus.md` — the Week 7 objectives and deliverables, the Sunday 15 November deadline, and the Week 8 deadline.
- `A7/itpd/AGENTS.md` — course terminology and the `docs/` destination map, which puts `docs/usability-tests/` in Week 7.

Apply every rule marked `**Since: W1**` through `**Since: W7**`.
No rule in the pinned materials carries a `**Since: W8**` marker that applies to Week 7, so nothing is excluded by a later marker; the Week 8 usability results and configuration management and the Week 9 pitch deck are not Assignment 7 deliverables, and their absence is never a shortfall.

## Assignment parameters

- Report title: `# Assignment 7 Compliance Feedback`
- Week: `W7`
- Course materials: `A7/itpd` at `d7bcb1b24c142df8377da11ac5a1b4854e317fba`
- Primary index artifact: `reports/week-07/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-7.md`.
- Week window: from Friday 6 November 2026, 00:00 Innopolis time, `2026-11-06T00:00:00+03:00`.
  The syllabus gives the Week 7 class week as 6 to 12 November 2026; the submission is due on the following Sunday, and the window runs from that Friday to `ISSUE_CUTOFF`.
- Soft deadline: none; `course/rules.md` gives every group submission from Week 4 to Week 9 a single hard deadline, and `course/syllabus.md` and `assignments/assignment-7.md` state the same date.
- Hard deadline: Sunday 15 November 2026, 23:59, as the pinned `course/syllabus.md`, `course/rules.md`, and `assignments/assignment-7.md` state it. Week 7 is the second exception to the Week 4 to Week 9 Saturday rule, after Week 6: the syllabus deadline is Sunday 15 November 2026.
- No per-team deadline override exists for Week 7: every team's deadline is Sunday 15 November 2026, 23:59.
- `ISSUE_CUTOFF`: `2026-11-15T23:59:59+03:00` for every team.
  Every later reference to `ISSUE_CUTOFF` means that cutoff, and `**Evidence:**` states the cutoff used.
- Hard deadline of the following week: Saturday 21 November 2026, 23:59, the deadline the Week 8 syllabus block gives and the due date `SPRINT-08`'s GitHub milestone carries.
  A Week 6 action point due in Week 7 carries a due date from 6 November through 15 November 2026, the Week 7 class week plus the submission deadline; a due date from 16 November on belongs to Week 8 and is outside the meeting's Week 7 window.
- The time zone is not stated in the materials; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A7/submissions/<team_dir>/`; the Moodle export carries no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A7/work/<team_dir>/snapshot/`.
- Live artifact families: the story and task issues with their types, field values, comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the link check, the Markdown check, `actionlint`, and the product code; the repository's tags and releases; the sprint GitHub milestones; the Sprint Review's Moodle recording link; and the private usability-data repository and the recordings folder, read only through the public record, the Moodle PDF, and the record's own claims because they need authentication.
- Story and task issues, their types, their field values, their milestones, and the labels are not in the snapshot, so they are read live and judged as of `ISSUE_CUTOFF`, per [procedure step 6](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by `ISSUE_CUTOFF` counts.
- Tags, releases, and milestones are read live and judged as of `ISSUE_CUTOFF` too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after `ISSUE_CUTOFF`, and say so in `**Evidence:**` when the timeline cannot settle it.
- The private usability-data repository, the recordings folder, and the design review's recording are private or Moodle-only.
  Judge them from the test record, the week report, and the Moodle PDF's links and access instructions; make the single access check of `docs/grading-policy.md#consumer-hosted-media` only when the agent has the access to reach them, and treat an unverifiable access claim as an evidence gap for that check, not as a shortfall.

The segments, in order:

- S1: Sprint plan and milestones
- S2: Backlog refinement and task scheduling
- S3: UT-01 test record and index
- S4: Surveys
- S5: Tasks and success criteria
- S6: Measures and instrumentation
- S7: Facilitation protocol, roles, and dry run
- S8: Consent and private data home
- S9: Interaction Capability requirement and manual test
- S10: Recruitment and session plan
- S11: Analysis plan and evidence map
- S12: Glossary and risk register
- S13: Week 6 action points and open questions
- S14: Customer validation of the test design
- S15: Design-review rework and testing-plan rows
- S16: REL-07 release
- S17: Sprint close and retrospective
- S18: Week report and submission
- S19: AI usage and honesty

### Segment overview

Every checklist item and every coverage-table row, or named part of a row, of `assignment-7.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Sprint plan and milestones | Part 1 items 1–3; the Sprint plan part of the coverage row Sprint plan; the plan's `### SPRINT-07` goal, `**Due:**`, `**Sprint Backlog:**`, and `**Planned Velocity:**`, and `### SPRINT-08`'s provisional goal, `**Due:**`, and backlog link; the checklist item "`SPRINT-07` planned with its goal, its `**Due:**` field, its `**Sprint Backlog:**` link, and its `**Planned Velocity:**`, and `SPRINT-08` given its provisional goal, its `**Due:**` of `2026-11-21`, and its backlog link" |
| S2: Backlog refinement and task scheduling | Part 1 items 4–7; the story and task-issue part of the coverage row Sprint plan; the checklist items "The design tasks scheduled in `SPRINT-07`, the instrumentation implementation in `SPRINT-07`, its verification in `SPRINT-07` or `SPRINT-08` before the first counted session and complete by the start of `SPRINT-09`, the sessions in the sprint of the last counted session, the results tasks in `SPRINT-08`, and each task issue carrying its `### Requirements`, its criteria, its `Responsible`, its `Accountable`, and its assignees" and the refined next two sprints' worth of the product backlog |
| S3: UT-01 test record and index | Part 2; the `UT-01` test record part of the coverage row `UT-01` test record; the checklist item "`docs/usability-tests/README.md` with the `UT-01` row, and `docs/usability-tests/ut-01/README.md` with its heading, its status, its design and run sprints, its `**Dropped:**` field when dropped, and its parts" |
| S4: Surveys | Part 3 item 1; the Surveys and post-test coverage row; the checklist item "`surveys.md` with the pre-test, the SEQ after each task, the full ten SUS items and the formula, and the open-ended post-test" |
| S5: Tasks and success criteria | Part 3 items 2–3; the tasks half of the Tasks and protocol coverage row; the checklist item "The main task and the two secondary tasks, the same for every participant, with their scenarios, start points, end states, success criteria, time limits, fixed order, and no UI labels or steps" |
| S6: Measures and instrumentation | Part 3 items 4–7; the measures part of the record and the Test instrumentation coverage row; the checklist items "The record's `## Instrumentation` section with what the test observes, the Week 6 events it reuses, the events or records it adds, how a session is linked to its records, the environment, the store, and what the instrumentation cannot cover" and "The instrumentation implemented and verified before the first counted session, with the implementation in `SPRINT-07` and the verification in `SPRINT-07` or `SPRINT-08`, complete by the start of `SPRINT-09`, and the verification recorded". The scheduling of those two tasks is S2's |
| S7: Facilitation protocol, roles, and dry run | Part 3 items 8–10; the protocol half of the Tasks and protocol coverage row; the checklist item "`sessions/README.md` with the facilitation script, the pre-test, the open-ended post-test, the no-help rule, the observation sheet, the roles by GitHub username, and the stop rule, and the dry run recorded as not counted" |
| S8: Consent and private data home | Part 4; the Consent template, Private usability-data repository, and Recordings folder coverage rows; the checklist items "`consent.md` as the public template, the private `<organization>/<repo>-usability-data` repository private and shared with the instructors, and the recordings folder created and shared" and "The public link to the private repository and its link-check exclusion, the retention and deletion rule, and the private links in the Moodle wrapper" |
| S9: Interaction Capability requirement and manual test | Part 5; the `QR-nn` and its test coverage row; the checklist items "The new `Interaction Capability` `QR-nn` with `High` business importance, the team's technical risk, one chosen sub-characteristic and its reason, a team-chosen measure from the recorded measures, read with a statistic the analysis plan reports, against a bar set before the sessions, and its scenario", "The `manual` `QRT-01` naming `UT-01` in `**Runs at:**`, with its `**Why Manual:**`, its procedure, its `**Pass when:**`, and its `Not verified` testing-plan row planned for `SPRINT-08`", and "The requirement's row in the quality requirements index (the matrix)" |
| S10: Recruitment and session plan | Part 6; the Recruitment target and session plan coverage row; the checklist items "A recruitment target of at least three representative participants, 18 or older, matching the profile, five as the design target, and the consent template ready to collect, covering the recording and the sanitized public results" and "The session plan in `## Schedule` with the team's dates or how it will arrange them, the results-due date, in person, on the university network, against staging, with the seed reset and the instrumentation verified before the first session" |
| S11: Analysis plan and evidence map | Part 7; the analysis, findings-template, and triage parts of the Week 8 handoff coverage row; the checklist item "The analysis plan written before the first session, with the minimum measures and any additional measure named before the first session, each task's outcome and the assistance, the instrumentation comparison and what it cannot cover, the `results.md` stub with its headings, the findings template, the triage plan, and the evidence map" |
| S12: Glossary and risk register | Part 8; the Glossary and Risk register coverage rows; the checklist item "The Week 7 usability terms in `docs/glossary.md` and the recruitment, consent, data-access, and schedule risks in `docs/risks.md`, each starting `**Status:** Open`" |
| S13: Week 6 action points and open questions | Part 9; the Week 6 action points and Week 6 open questions coverage rows; the checklist item "Each Week 6 action point's outcome in `## Previous action points`, and each Week 6 open question put to the customer or carried forward" |
| S14: Customer validation of the test design | Part 10; the Sprint Review, Meeting script, and Meeting transcript coverage rows; the checklist items "`reports/week-07/meeting-script.md` with the permission questions first, the design on staging, the Week 8 plan, and the read-back last" and "`reports/week-07/meeting-report.md`, with the design review's feedback, a `DEC-nnn` for any decision, and 2 or more action points due after Week 7, at least one in Week 8" |
| S15: Design-review rework and testing-plan rows | Part 11 items 1–4; the checklist item "The design review's decisions applied, including the `QR/QRT` when the review changes it, each `SPRINT-07` testing-plan row run or moved with a reason, and the testing plan updated" |
| S16: REL-07 release | Part 11 items 5–8; the `REL-07` coverage row; the checklist item "`REL-07` tagged on the release commit, its tag protected, with the changelog's released section, the upgrade note ending with the `Full changelog` line, the plan's `REL-07` block with `Released` and `Checked QRs` and the one sentence linking the testing plan, and the sprint milestone closed" |
| S17: Sprint close and retrospective | Part 12; the Sprint retrospective coverage row and the actual-velocity part of the Sprint plan row; the checklist item "`**Actual Velocity:**` set in `### SPRINT-07`, and `reports/week-07/sprint-retrospective.md` with its four sections, its carried actions, and any `Not done` action re-listed with `Carried: Yes`" |
| S18: Week report and submission | Assignment Report In The Repository items 1–6; Assignment Report On Moodle items 1–9; the Submission Procedure; the 21 coverage rows judged only as rows that exist and link; the checklist items "`reports/week-07/README.md` with the summary, the `## Usability test` section, the coverage rows, and the `## Privacy` line", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", "PDF ready with the permalink, the private repository and recordings folder links and access, the staging and production addresses, the staging analytics and observability credentials, and no participant identity", "The design review's recording and transcript in the PDF, or one line for each saying why", and "The Week 8 handoff ready". The underlying handoff artifacts are judged in S10, S11, and S16, and the report's handoff row is judged here |
| S19: AI usage and honesty | Part 13; the AI usage coverage row; the checklist item "`reports/week-07/ai-usage.md`, including whether an agent was given usability material, and if so, that it was the sanitized note" |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S18.
S14 owns the design review and the meeting artifacts; S15 owns the design-review rework and the testing-plan rows, so a decision the review records but the record does not apply is reported in S15 and its own record in S14 is judged there.
S16 owns the tag, its protection, the release body, the changelog, the plan's block, and the milestone close; S18 owns the report and the PDF.

## Status guide

Use the status vocabulary of `docs/compliance-feedback-format.md` and the evidence states of `docs/grading-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S16 when the tags and releases cannot be read at all, or S8 when the private repository cannot be reached and neither the record nor the PDF settles its state.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Sprint plan and milestones

**Check:**

- `docs/project-plan.md`'s `### SPRINT-07` and `### SPRINT-08` sections in the snapshot.
- `milestones.json` and the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` for `SPRINT-07` to `SPRINT-09`, their due dates, their states, and the issues in each.
- `issue-fields.json` for the `Story Points` of the stories scheduled in `SPRINT-07` and the stories the plan names.
- `reports/week-06/README.md` and the plan's `SPRINT-08` goal, for the provisional target the week inherits.

**met:**

- `### SPRINT-07` carries the sprint's real goal in one sentence, not the provisional goal the plan carried until now, and the goal is a result rather than a list of tasks.
- `### SPRINT-07` carries `**Due:** 2026-11-15`, `**Sprint Backlog:**` linked to its own GitHub milestone, and `**Planned Velocity:**` set at planning.
- `**Planned Velocity:**` is a whole number computed by hand from the `Story Points` of the stories scheduled in `SPRINT-07`'s milestone, and it equals their sum.
- A `SPRINT-07` that carries only tasks has a planned velocity of `0`, and its goal says what a task-only sprint is for.
- `### SPRINT-08` carries a provisional goal in one sentence, `**Due:** 2026-11-21`, and its backlog link, so the results sprint has its target already.
- The GitHub milestone `SPRINT-07` exists with the due date `2026-11-15` and carries the issues the sprint planned; `SPRINT-08`'s milestone exists with `2026-11-21`; `SPRINT-09`'s exists with `2026-11-28`.
- The plan's figures and the scheduled stories agree: no story counted in the planned velocity sits outside the sprint's milestone, and no story inside it is left out of the figure.

**What does not count:**

- `### SPRINT-07` still carrying its provisional goal, a goal that is a task list, or a goal that names the sprint's deliverables instead of a result.
- A missing `**Due:**`, a due date other than `2026-11-15`, or a `**Sprint Backlog:**` link to an issue list, the GitHub project, or a milestone that is not the sprint's.
- A planned velocity copied from another sprint, guessed, or differing from the scheduled stories' `Story Points`; a task-only sprint with a nonzero figure or with no figure.
- `**Planned Velocity:**` added after the sprint closed, or a figure that counts a story the sprint did not have at planning.
- A missing GitHub milestone, a due date that is not the syllabus deadline, or scheduled stories that are absent from the milestone.
- `SPRINT-08` with a missing goal, a missing `**Due:**`, or a missing backlog link when it already has issues.

**partial:**

- `### SPRINT-07` carries a goal and its `**Due:**` and at least one other `met` criterion fails.
- Typical shortfalls: a provisional goal left in place; a missing backlog link; a planned velocity that does not equal the scheduled stories; a task-only sprint with a figure; a wrong or missing milestone due date; `SPRINT-08` without its provisional goal.

**missing:**

- `### SPRINT-07` is absent, or it carries neither its goal nor its `**Due:**`, or `docs/project-plan.md` is absent at the snapshot.

**Guardrails:**

- The plan's Week 3 to Week 6 parts — its milestones, its older sprints, and `REL-04` to `REL-06` — are not re-graded; this segment judges `SPRINT-07` and `SPRINT-08` and the sprint milestones' due dates.
- Velocity is computed by hand from the `Story Points` values, because a single-select field holds one option and cannot be added up.
- The planned velocity is the stories selected at planning; when a story moves out during the sprint, the move is judged from the issues in S2 and the actual velocity in S17.
- The GitHub milestone's due date is the week's hard deadline; the milestone's close is S16's and the issues in it are S2's and S16's.
- `SPRINT-07` is a design sprint, so a task-only sprint with `0` is correct and is never a shortfall.
- A plan edited after `ISSUE_CUTOFF` is a caveat in `**Evidence:**` and never repairs the state at the cutoff.

### S2 — Backlog refinement and task scheduling

**Check:**

- `issue-fields.json`, `issues.json`, and the saved timelines for the open story and task issues, their types, their milestones, their `Priority`, `Responsible`, and `Accountable` values, their assignees, and their `Story Points` and `MoSCoW` values.
- `docs/project-plan.md`'s `### SPRINT-07` and `### SPRINT-08`, and the sprint milestones the issues sit in.
- `prs.json` for the Week 7 pull requests that closed the design task issues, and for the instrumentation implementation.

**met:**

- The next two sprints' worth of the product backlog, `SPRINT-08` and `SPRINT-09`, is refined: each item's scope is settled, its acceptance criteria are runnable, its `Story Points` is set, and it is at most `13SP`.
- Each refined item sits in no sprint's GitHub milestone, with no `Responsible` value, no `Accountable` value, and no assignee, so it is ready to schedule and not yet scheduled.
- Each design task of Part 1 is an issue scheduled in `SPRINT-07`'s milestone: the test record, the surveys, the tasks and protocol, the test's instrumentation, the consent and the private repository, the recordings folder, the `QR/QRT`, the recruitment, the dry run, and the analysis plan.
- The instrumentation implementation is its own scheduled issue in `SPRINT-07`, separate from the design of the instrumentation.
- The instrumentation's verification is scheduled in `SPRINT-07` or `SPRINT-08`, after the implementation, before the first counted session, and complete by the start of `SPRINT-09`.
- When every counted session runs before the design week's deadline, the sessions are scheduled in `SPRINT-07` and the verification is in `SPRINT-07`; otherwise the sessions are scheduled in `SPRINT-08`.
- The sanitized session notes, the results, the findings, and the triage are scheduled in `SPRINT-08`; `REL-08` and the `QR/QRT` verdict are planned into `SPRINT-08`.
- Every task issue carries its `### Requirements` section, at least one `AC-nn`, its `Priority`, its milestone, its `Responsible` and `Accountable` values, and the matching assignees.
- A task that is not product work says `None: repository upkeep` in its `### Requirements`, and a product task names an `FR-nnn` or `ADR-nnn`.

**What does not count:**

- A story that sits in `SPRINT-08` or `SPRINT-09`'s milestone, or that carries `Responsible`, `Accountable`, or assignees, and is called refined: scheduling is what leaves the product backlog.
- A story with no `Story Points`, with a `Story Points` above `13`, or with acceptance criteria that are not runnable.
- A design task absent from `SPRINT-07`'s milestone, or the instrumentation implementation folded into the design issue with no implementation task of its own.
- The verification scheduled in `SPRINT-08` while the first counted session runs in `SPRINT-07`, or scheduled after the first counted session, or planned for `SPRINT-09`.
- Sessions scheduled in `SPRINT-07` when the last counted session runs in `SPRINT-08`, or a session planned outside any sprint milestone.
- The results, the findings, the triage, `REL-08`, or the `QR/QRT` verdict scheduled in `SPRINT-07`.
- A task issue with no `### Requirements`, no acceptance criterion, no `Priority`, no milestone, no `Responsible` or `Accountable` value, or no assignee.
- A product task whose `### Requirements` says `None: repository upkeep`, or a non-product task that names a requirement it does not advance.

**partial:**

- The design tasks are scheduled and at least one other `met` criterion fails.
- Typical shortfalls: one refined item still carries a milestone or assignees; one design task is missing; the verification sits in the wrong sprint; the sessions or the results are scheduled in the wrong sprint; a task issue lacks a field or a criterion; a product task says `None: repository upkeep`.

**missing:**

- No design task is scheduled in `SPRINT-07`, or neither the product backlog nor the task schedule can be read at the cutoff.

**Guardrails:**

- The schedule is read at `ISSUE_CUTOFF`; a task rescheduled after the cutoff is a caveat and never repairs the state at the cutoff.
- The ten design artifacts need not be ten separate issues; a task may cover two artifacts the assignment names together, but each of the record, the surveys, the tasks and protocol, the instrumentation, the consent and private repository, the recordings folder, the `QR/QRT`, the recruitment, the dry run, and the analysis plan must be scheduled work.
- The verification is not a counted session, and a dry run is the verification only under [S6](#s6--measures-and-instrumentation)'s conditions; this segment judges where the verification is scheduled, not what it found.
- A story's `MoSCoW` is set when the story is written and its `Story Points` at refinement, per the Week 4 rules; a refined story that is ready carries both.
- The GitHub project's table view, the issue forms, and the label set are Week 2 to Week 4 mechanics and are not re-graded; this segment checks the scheduled task issues' shape where Assignment 7 requires it.
- A story larger than `13SP` is split before it is scheduled, so a `13SP` story is the largest scheduled story, and a larger one is a shortfall wherever it sits.

### S3 — UT-01 test record and index

**Check:**

- `docs/usability-tests/README.md` and `docs/usability-tests/ut-01/README.md` in the snapshot, read whole.
- `docs/usability-tests/ut-01/results.md`, `surveys.md`, `consent.md`, `sessions/`, and `images/` in the snapshot.
- The record's `QRT-nn` link against `docs/quality-requirements/`, and the record's claim that `QRT-01` names `UT-01`.

**met:**

- `docs/usability-tests/README.md` exists, carries the index table with the columns `UT`, `Goal`, `Status`, `Results`, and `Sprints`, in that order, and has one row for `UT-01`.
- The index row's `UT` cell links the record as `[UT-01](ut-01/README.md)`, its `Goal` cell copies the record's one-sentence goal, its `Status` cell is the record's `Planned`, its `Results` cell is `Pending`, and its `Sprints` cell links the design sprint and the run sprint.
- `docs/usability-tests/ut-01/README.md` is headed `# UT-01: <title>` and carries the fields in order: `**Status:** Planned`, `**Design sprint:**` linked to the plan's `SPRINT-07` section, and `**Run sprint:**` linked to the sprint of the last counted session.
- The run sprint is `SPRINT-08` in the default plan, `SPRINT-07` only when every counted session runs before the design week's deadline, and updated to `SPRINT-09` when the plan moves; when the sessions straddle two sprints, the record says which sessions run in which and the index lists both.
- The record states the goal in one sentence and two or three research questions as a numbered list, each answerable with the session's data.
- The record links the `QR-nn` the test serves, and the `QRT-nn` that names `UT-01` in `**Runs at:**` lives in that requirement's file.
- The record's sections appear in this order: `## Research questions`, `## The Requirement`, `## Participant Profile`, `## The Tasks`, `## Protocol`, `## Measures`, `## Instrumentation`, `## Analysis Plan`, `## Schedule`, `## Roles`, `## Environment`, `## Consent And Data`, `## Evidence Map`, and a link to `results.md`.
- `results.md` exists as the stub with the results table, the findings, the limitations, and the conclusion headings, and the record links it.
- `surveys.md`, `consent.md`, `sessions/`, and `images/` exist; `images/` carries a tracked `.gitkeep` so the empty directory is in the snapshot.

**What does not count:**

- A record marked `Completed` in the design week, or a record whose status is `Completed` with no results recorded.
- A heading that is not `# UT-01: <title>`, or a title carrying the team number instead of the test's title.
- An index without the five columns in order, without the `UT-01` row, or with a second list of the same tests.
- A `Results` cell that is not `Pending`, an index row whose status disagrees with the record, or a `Sprints` cell that does not link the sprint sections.
- A run sprint of `SPRINT-07` when the sessions run in `SPRINT-08`, or a missing run sprint.
- A goal that takes more than one sentence, one or four or more research questions, or a research question no session data can answer.
- A missing `QR-nn` link, or a link to a requirement whose test names a different test.
- A missing required section, a section out of order, or no link to `results.md`.
- No `results.md` stub, no `sessions/`, no `images/.gitkeep`, no `surveys.md`, or no `consent.md`.

**partial:**

- The record and the index exist with the heading and the fields, and at least one other `met` criterion fails.
- Typical shortfalls: an index column missing or out of order; `Results` not `Pending`; a section out of order; a missing stub; a run sprint that does not match the plan; one research question; no `QR-nn` link.

**missing:**

- `docs/usability-tests/ut-01/README.md` is absent, or `docs/usability-tests/README.md` is absent.

**Guardrails:**

- The record's prose, its title, and the content of each section are the team's; this segment judges the heading, the fields, the order of the named sections, and the index row.
- A section whose content another part writes — the tasks, the instruments, the instrumentation, the schedule, and the analysis plan — is judged for its content in S4 to S11; here it is judged for existing in its place, so an empty stub is not this segment's shortfall unless the assignment's other parts also left it empty.
- The index is the group's one table and is not a second record: the goal is copied, the design is not.
- A record whose sessions have already run still says `Planned` until the results are recorded, because the results are due with Submission 8.
- `**Dropped:**` is correct only on a dropped test, and it replaces the design and run sprints' claim; a dropped test is judged against the design it did write and is never a shortfall for having no sessions.
- A record written after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`; the state at the cutoff is what the snapshot shows.

### S4 — Surveys

**Check:**

- `docs/usability-tests/ut-01/surveys.md` in the snapshot, read whole.
- The record's `## Measures` section for which measures the instruments record, and the record's `## The Tasks` for which tasks the SEQ follows.
- The `SUS` and `SEQ` rules in `usability-testing-requirements.md`, and the record's `QRT-nn` for the measure it reads.

**met:**

- `surveys.md` exists and carries the pre-test, the SEQ after each task, the full ten SUS items, and the open-ended post-test.
- The pre-test asks for the participant's role and background, their familiarity with similar products, the device, and their expectations.
- The pre-test carries the 18-or-older declaration and asks for no name, email address, phone number, or free-text identification.
- The SEQ is the standard question `Overall, how difficult or easy was the task to complete?`, on the seven-point scale where 1 is very difficult and 7 is very easy, asked after each task.
- The SUS is the ten standard items, in their standard order and wording, with no item reworded, each answered from strongly disagree (1) to strongly agree (5).
- The SUS formula is stated as `SUS = 2.5 × (20 + sum(odd) - sum(even))`, computed from the responses as recorded, with the even items not reverse-coded before the formula.
- The open-ended post-test asks for the participant's overall impression, what the participant would change, and what the team did not ask.

**What does not count:**

- A SUS with fewer or more than ten items, a reworded item, a changed order, or a seven-point SUS scale.
- An instruction to reverse-code the even items before the formula, or a formula that differs from the standard one.
- A SEQ that is reworded, uses a five-point scale, or is asked only once after all tasks.
- A pre-test that asks for a name, an email address, a phone number, or free-text identification, or that omits the 18-or-older declaration.
- A post-test missing the overall impression, what the participant would change, or what the team did not ask.
- An ASQ, a product-specific survey, or extra questions that replace the standard items instead of following them.

**partial:**

- `surveys.md` carries the four instruments and at least one other `met` criterion fails.
- Typical shortfalls: one SUS item reworded or out of order; the SEQ scale or wording changed; the formula or the reverse-coding note wrong; the 18-or-older declaration missing; the post-test missing one of its three questions.

**missing:**

- `surveys.md` is absent, or it carries neither the SUS nor the SEQ.

**Guardrails:**

- The pre-test's wording and the open-ended post-test's wording are the team's; the criteria are the four areas, the 18-or-older declaration, and the three post-test prompts.
- The SEQ's question and the ten SUS items are fixed text: a survey that adapts them for the product is a shortfall, and extra questions after them are allowed.
- The ASQ is optional; its absence is never a shortfall.
- The SUS score is computed in the run week from the recorded responses; this week judges that the instrument and the formula are right, not that a score exists.
- The mean and median with the `n=<count>` caveat belong to the results report in Week 8; this week the instrument says how it is scored.
- The session template and the observation sheet are `sessions/README.md`, judged in S7; the surveys file holds the questions, not the session record.

### S5 — Tasks and success criteria

**Check:**

- The record's `## The Tasks` section in the snapshot.
- The record's `## Measures` and `## Instrumentation` for which task the measure and the instrumentation follow.
- The `QR-nn` and its `QRT-nn` for the main task the requirement reads.
- `sessions/README.md` for the fixed order and the wording the facilitator reads.

**met:**

- The test has one main usability test task and two secondary usability test tasks, and the main task runs first.
- The tasks are identical for every participant and run in a fixed order that the record states and `sessions/README.md` repeats.
- Each task is a scenario with a goal and a start point: what the participant wants to achieve, and where the session begins.
- Each task states an end state, a success criterion, a time limit, and a help rule that names what counts as help.
- The success criterion is one of `Unaided`, `Assisted`, or `Failed`, and it is written before the first counted session.
- No task's wording names a button, label, screen, step, or step count.
- The main task is the product's main flow, it is the subject of the `QR-nn` the test serves, and the test's instrumentation follows it.
- The two secondary tasks cover adjacent flows and keep their order fixed across participants.

**What does not count:**

- A task that names a button, a label, a screen, a step, or a step count, such as "click Book now" or "the third step".
- A task with no start point, no end state, no time limit, or no help rule.
- A success criterion outside `Unaided`, `Assisted`, and `Failed`, or a criterion added after the first counted session.
- One task, four tasks, or two tasks: the assignment's one main and two secondary are exact.
- A main task that is not the product's main flow, or a `QR-nn` whose test reads a different task.
- Tasks that differ between participants, or a secondary order that changes.

**partial:**

- The record carries the main task and two secondary tasks and at least one other `met` criterion fails.
- Typical shortfalls: a task names a screen or a step; a missing start point, end state, time limit, or help rule; a success criterion added after the first session; the main task is not the one the `QR` reads.

**missing:**

- The record has no `## The Tasks` section, or it carries no main task and no secondary task.

**guardrails:**

- The scenarios' prose, their names, and the way they describe the start and end states are the team's; the criteria are the count, the fixed order, the scenario shape, and the no-label rule.
- A scenario may name a product concept, such as the booking link, and may not name the interface control that reaches it; a start point that says which page or screen the session begins on is a UI label.
- The help rule names what the facilitator may say or do; a help rule that leaves the facilitator to decide what help is each session is not a rule.
- The time limit is the task's own, and the success criterion is written before the first counted session; the dry run may check the wording and the time limit without becoming evidence.
- The `QR-nn`'s measure and bar are S9's; this segment judges that the main task is the flow the requirement reads and that the instrumentation follows it, not which measure the requirement chooses.
- A task the Week 6 event table does not cover is a reason to instrument it, per S6, never a reason to drop the task.

### S6 — Measures and instrumentation

**Check:**

- The record's `## Measures` and `## Instrumentation` sections in the snapshot.
- `docs/analytics.md`'s `## The Events` table and its `source` rule, and the Week 7 rules for the test's events and the `participant_code` field.
- The snapshot's product code for the events the record names, and the Week 7 pull requests that added them.
- `sessions/README.md` and the record's `## Schedule` for the verification run and its date.
- `pdf-info.json` and `summary.md` for the cutoff and the snapshot time, when the verification's timing matters.

**met:**

- The record's `## Measures` section names the four recorded measures and the instrumentation: the task completion and assistance, the time on task, the SEQ after each task, the SUS and its score, and the test's instrumentation where it covers the task.
- The record's `## Instrumentation` section states what the test must observe to answer its research questions and to compare a session with the product's use, for each task and for the funnel the results compare.
- The instrumentation section names which Week 6 events it reuses, which events or records it adds and where each is emitted, the environment it runs in, the store the data goes to, and the method that tells one session's records from another's.
- The session link is one of the allowed methods — the session's time window, an opaque session token, the `P-nn` code, or another documented method — and a reader can reconstruct a session's events from the record without asking the team.
- The instrumentation section says which task or research question the instrumentation cannot cover, and the results are to repeat that limit rather than invent an event or a metric.
- The instrumentation collects no personal data; the identity mapping stays in the private repository, and the participant code is the documented exception to the opaque-identifier rule.
- The instrumentation runs on the staging deployment or a test-only path, never on production, and it writes no production data.
- Every test event that goes through the analytics pipeline carries `source=usability-test`, and every metric excludes both `usability-test` and `smoke` traffic.
- Every new event that goes through the analytics pipeline is a row in `docs/analytics.md#the-events` in the same pull request as the code that emits it, and a reused event's row lists `participant_code` (string, optional, staging test only) when the test uses the code.
- A test-only event that never goes through the analytics pipeline is documented in the record and is correctly absent from the event table.
- The instrumentation is implemented before the first counted session, with the implementation scheduled in `SPRINT-07`.
- The instrumentation is verified before the first counted session: a team-run or dry-run record reaches the store the record names, the participant link identifies that run, and the record says what was verified and when.
- The verification is scheduled before the first counted session, in `SPRINT-07` when the session runs there and otherwise in `SPRINT-08`, and it is complete by the start of `SPRINT-09`.
- The dry run is the verification only when it is that run, in the verification's sprint, after the implementation, and before the first counted session; otherwise a second run is recorded before the first counted session.

**What does not count:**

- An instrumentation section that lists tools or events without saying what the test must observe, or that omits the session link.
- The `P-nn` code, or any identifier, used as a session link without the record saying so and without the identity mapping staying private.
- An instrumentation path on the production deployment, a test event that writes production data, or a pipeline event without `source=usability-test`.
- A metric query that includes `usability-test` or `smoke` traffic, or a test event presented as a product metric.
- A new event that goes through the pipeline with no row in the event table, a reused event's row without `participant_code` when the code is used, or a test-only event wrongly listed in the table as pipeline traffic.
- No verification recorded, a verification after the first counted session, a verification in `SPRINT-09`, or a verification that names no store, no participant link, or no date.
- A dry run claimed as the verification when it ran before the implementation, in another sprint, or after the first counted session.
- An instrumentation section that claims to cover every task or question, with no limit recorded.

**partial:**

- The record carries the measures and the instrumentation section with the implementation, and at least one other `met` criterion fails.
- Typical shortfalls: no session-link method; the event table missing a new event; a missing `participant_code` on a reused row; the verification missing, undated, or after the first session; a metric that includes test traffic; the record not saying what the instrumentation cannot cover.

**missing:**

- The record has no `## Instrumentation` section, or the instrumentation is not implemented at the snapshot, with no implementation evidence.

**Guardrails:**

- The instrumentation is the team's design: reusing Week 6 events, adding events, and using a test-only path are all correct, and this segment judges the fit between the test's tasks and what the instrumentation observes.
- The Week 6 event table is the one registry, so an event the test sends through the pipeline must be a row there; a test-only path is documented in the record and is not a table row.
- The `source=usability-test` filter is Week 6's rule for every metric, and this segment judges the test's events against it; a metric that includes test traffic is reported once, in the segment that owns the claim, which is here for the instrumentation and S18 for the report's metric statement.
- The verification is the team's own run against staging, not a counted session; a teammate's dry run may be that run only under the conditions above.
- A verification after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff; a verification that cannot be read, with no record of it, is an evidence gap for that check only when a later record could still settle it.
- The instrumentation comparison and the test's filtered telemetry export belong to Week 8; this segment judges the design, the implementation, and the verification, not a result.

### S7 — Facilitation protocol, roles, and dry run

**Check:**

- The record's `## Protocol` and `## Roles` sections in the snapshot.
- `docs/usability-tests/ut-01/sessions/README.md` in the snapshot, read whole.
- The record's `## Schedule` and `## Instrumentation` for the dry run and its status.
- The Week 7 pull requests that added the protocol and the session template.

**met:**

- The record's `## Protocol` section states the session order: the welcome, the consent and recording check, the pre-test, the think-aloud instruction, the scenario reading, the observation, the SEQ after each task, the SUS and the open-ended post-test after all the tasks, and the debrief.
- The protocol states that every session is in person, on the university network, against the staging deployment, with the seed reset before the session, and that no real payment is made.
- The protocol states that the facilitator reads the scenario verbatim, answers only questions about the scenario and never about the interface, and does not solve the task for the participant.
- The protocol states that the observer records the help given, the time on task, the friction points, and the quotes.
- The protocol states that at least two team members run each session, and that the same facilitator runs all the counted sessions.
- The protocol states the stop rule: the facilitator stops the session when the participant asks, or when a critical or security-sensitive problem is observed, and the stop and its reason are recorded.
- The record's `## Roles` section names, by GitHub username, the facilitator who runs every counted session, the observer who records the help and the friction, and the member who keeps the recordings and the raw notes.
- `sessions/README.md` carries the session template, the facilitation script, the no-help rule, the observation sheet, the roles by GitHub username, and the stop rule.
- The dry run is recorded as a run with a teammate, it checks the wording, the time limit, and the instrumentation, and it is recorded as not evidence and not counted.
- The dry run is the verification only when it is that run, per S6; otherwise the record says a separate verification ran before the first counted session.

**What does not count:**

- A protocol missing the welcome, the consent and recording check, the pre-test, the think-aloud instruction, the scenario reading, the observation, the SEQ after each task, the SUS and post-test after all tasks, or the debrief.
- A session held against production, with no seed reset, or that takes a real payment.
- A facilitator who answers interface questions, solves the task, or helps without the observer recording it.
- One team member per session, or a different facilitator for a counted session.
- No stop rule, or a stop rule with no record of the stop and its reason.
- Roles given by real name, by team number, or by a name that is not a GitHub username.
- `sessions/README.md` missing the template, the script, the no-help rule, the observation sheet, the roles, or the stop rule.
- A dry run recorded as a counted session, a result, or evidence.
- A protocol that leaves the no-help rule to the facilitator's judgement each session.

**partial:**

- The protocol and the session template exist with the session order and the roles, and at least one other `met` criterion fails.
- Typical shortfalls: one protocol step missing; roles by real name; the same-facilitator rule missing; the stop rule missing; the dry run not recorded or counted as evidence; the observation sheet missing the help or the time on task.

**missing:**

- The record has no `## Protocol` section, or `sessions/README.md` is absent.

**Guardrails:**

- The protocol's prose and the observation sheet's shape are the team's; the criteria are the order of the steps, the in-person staging environment, the facilitator and observer rules, the two-member minimum, the same facilitator, the stop rule, and the dry run's status.
- The consent and recording check is the protocol's first gate; the consent template and the private data home are S8's, and the check that every counted session has its durable consent is judged there.
- A facilitator who helps by mistake does not invalidate the session; the help is recorded and the task's criterion becomes `Assisted`, per S5.
- The dry run is the instrumentation verification only when the first counted session runs in `SPRINT-07`; a dry run outside that condition is still useful and is still not evidence.
- A session run before the design week's deadline is allowed; it is judged by the protocol the record had when it ran, and the results remain Week 8's.
- A protocol written after the first counted session is a caveat in `**Evidence:**` when a later record could still show it; when the record plainly changed after the session, it is a shortfall.

### S8 — Consent and private data home

**Check:**

- `docs/usability-tests/ut-01/consent.md` in the snapshot, read whole.
- The record's `## Consent And Data` and `## Evidence Map` sections.
- `reports/week-07/README.md`'s `## Usability test` section and `## Privacy` line for the private links and the sanitization claim.
- The link check's configuration, `lychee.toml`, for the private repository's exclusion and its reason.
- `gh repo view <organization>/<repo>-usability-data --json isPrivate,visibility` when the agent has access, and the record's and the PDF's claims when it does not.
- `pdf-info.json` and the snapshot for the repository's organization and name.

**met:**

- `docs/usability-tests/ut-01/consent.md` is the public template, with the clauses left unfilled: the 18-or-older declaration, participation, the recording, the sanitized public results, an anonymized quote as optional and separate, the private usability-data repository, the recordings folder, the instructors' access, the tools used and the deletion of their copies, the right to withdraw, and the deletion after grading.
- The template carries an unfilled signature line, and it carries no real name, email address, or participant identity.
- The private `<organization>/<repo>-usability-data` repository exists, is private, and has the team and the instructors as readers.
- The private repository is the text home: the consent records, the identity mapping, the raw notes, the test's filtered telemetry export, the working analysis, and the recordings folder link and access.
- The recordings live in a team-owned cloud folder shared with the instructors, and the private repository records the folder's link and its access instructions.
- The product repository links the private repository from the test record, and the link check excludes it with its reason in `lychee.toml`.
- The record states the retention rule: the private repository, its history, and the recordings are deleted after the course is graded, and the sanitized public record stays.
- A session that has run has its durable consent recorded before it, and the consent covers the recording and the sanitized public results; a session without either is not counted.
- The product repository carries no raw participant data, no recording, no consent record, no identity mapping, and no private link other than the private repository link.

**What does not count:**

- A consent template missing the recording clause, the sanitized public results clause, the quote clause, the private repository and recordings folder clauses, the instructors' access, the tools' copies, the withdrawal, or the deletion after grading.
- A consent template filled with a real name, an email address, or a participant's signature.
- No private repository, a public private-data repository, or no instructors among its readers.
- A private repository that holds the recordings, or a recordings folder that is missing or is not shared with the instructors.
- The recordings folder's link committed to the product repository, or the private repository's raw data committed there.
- The private repository link with no link-check exclusion, an exclusion with no reason, or a report that does not justify the exclusion.
- No retention rule, or a retention rule that keeps the raw data after grading.
- A counted session without the recording and the sanitized-public-results consent.

**partial:**

- The consent template and the private home are declared, and at least one other `met` criterion fails.
- Typical shortfalls: one consent clause missing; the recordings folder link made public; the exclusion missing its reason; the retention rule missing; the access instructions missing from the private home.

**missing:**

- `consent.md` is absent, or no private usability-data repository is declared anywhere in the record, the report, or the PDF.

**Guardrails:**

- The private repository, its layout, the recordings folder's provider, and the access instructions are the team's; the criteria are privacy, the readers, the text-only split, the recordings' place, the public link and its exclusion, and the retention rule.
- The private repository's contents are not readable without access; judge them from the public record and the PDF, make the single access check when the agent has the access, and record an unverifiable access claim as an evidence gap for that check only.
- The durable consent records, the identity mapping, and the raw notes are private; the public template is the artifact this week requires, and a template with placeholders is correct.
- A session that has not run owes no consent record; a session that has run owes its durable consent in the private repository, and a public claim of a session with no recorded consent is an evidence gap when the private home cannot be reached.
- The link check's exclusion is required because the private repository needs authentication; a different link-check tool is acceptable when it records the same reason.
- An instructor who cannot access GitHub is met by the Moodle-only archive and a declared deviation, per S12's data-access fallback and S18's `## Deviations`.

### S9 — Interaction Capability requirement and manual test

**Check:**

- `docs/quality-requirements/qr/` for the new `QR-nn` file, read whole, and for the identifier it takes.
- `docs/quality-requirements/README.md` for the row and the sort.
- `docs/project-plan.md#quality-requirement-testing-plan` for the `QRT-01` row.
- The record's `## The Requirement` and `## Analysis Plan` for the measure the requirement reads.
- The Week 7 pull request that added the requirement and its test.

**met:**

- A new `QR-nn` file exists under `docs/quality-requirements/qr/`, with the next free identifier, headed `# QR-nn: <short outcome>`, and its first line is the outcome in one sentence.
- The requirement carries `**Status:** Active`, `**Characteristic:** Interaction Capability`, and one `**Sub-characteristic:**` chosen from `Learnability`, `Self-descriptiveness`, and `Operability`.
- The requirement carries `**Business importance:** High` and the team's `**Technical risk:**`.
- One sentence says why the chosen sub-characteristic is what the test measures, and why the chosen measure reads it.
- The `## Scenario` carries the six parts in order, and its `Source` is a representative participant completing the main usability test task, its `Environment` is the staging deployment on the university network with seeded data, its `Artifact` is the product capability the task exercises, its `Response` is the behaviour the chosen measure reads, and its `Response Measure` is a real, countable criterion.
- The measure is one of the four recorded measures — the main task's completion and assistance, the time on task, the main task's SEQ, or the SUS — and the criterion uses a statistic the analysis plan reports: the main-task completion or assistance count or proportion, the main-task median time, the main-task median SEQ, or the SUS mean or median.
- The bar is set before the first counted session, it is not a target the team coaches participants toward, and the measures the requirement does not read stay analysis results and are reported.
- The `## QRT-01` section sits after the scenario, is headed with the identifier alone, and opens with the test in one sentence.
- `QRT-01` carries `**Status:** Active`, `**Level:** manual`, `**Runs at:**` naming `UT-01` and its record, and `**Why Manual:**` saying why no command can judge the chosen measure and that the test reads no `SLI-nn`.
- The `QRT-01` does not carry a deviation: an `Interaction Capability` manual test whose `**Runs at:**` names a `UT-nn` is the expected manual test and needs none.
- The `### Procedure` runs the main usability test task with at least three participants per the record and reads `results.md`, and `**Pass when:**` restates the `Response Measure` and settles it.
- The testing-plan row is `Not verified`, `Checked: None`, `Planned for sprint:` linked to `SPRINT-08`, and `Evidence: None`.
- The requirement's row is in `docs/quality-requirements/README.md` with the columns `QR`, `Outcome`, `Business importance`, `Technical risk`, `Characteristic`, `Sub-characteristic`, and `Status`, sorted per the matrix rule, and the index links the testing plan once.

**What does not count:**

- A characteristic other than `Interaction Capability`, a sub-characteristic outside the three allowed ones, or `**Business importance:**` other than `High`.
- No `QRT-nn`, a `QRT-nn` at another level, or a manual test that carries a deviation.
- A `**Runs at:**` that does not name `UT-01`, or a `**Why Manual:**` that explains no command but not that no `SLI` is read.
- A `Response Measure` that uses a statistic the analysis plan does not report, a measure outside the four, or an adjective with no countable criterion.
- A bar added after the first counted session, or a requirement whose measure is not the one its sentence says it reads.
- A `QRT-01` procedure with fewer than three participants, or one that does not read `results.md`.
- A testing-plan row that is not `Not verified`, that carries a `Checked` sprint or evidence, or that is planned for `SPRINT-07` or `SPRINT-09`.
- A missing index row, an unsorted matrix, or a second link to the testing plan.
- A reused `QR-nn` or a new identifier that skips the next free number.

**partial:**

- The new requirement and its manual test exist with `Interaction Capability` and `High`, and at least one other `met` criterion fails.
- Typical shortfalls: one scenario part missing; the measure not one of the four; the statistic not in the analysis plan; no `**Why Manual:**` or no no-`SLI` statement; the testing-plan row planned for `SPRINT-07`; the matrix row missing.

**missing:**

- No new `QR-nn` file exists at the snapshot, or the requirement has no `QRT-nn`.

**Guardrails:**

- The sub-characteristic, the measure, and the bar are the team's choices among the allowed sets; the example median SEQ against a bar of at least five of seven is an example, not a rule.
- The measure is a recorded measure and the criterion a statistic, per `A7/itpd/requirements/general-requirements.md#measurement-terminology`; a requirement that names a metric, an `SLI`, or a product-analytics number instead has not chosen one of the four.
- The Week 4 and Week 5 requirements and tests are not re-graded on their own rules; this segment judges the new Week 7 requirement, its test, and its two rows.
- The requirement's bar changing at the design review is S15's; the verdict, `Passes` or `Fails`, is Week 8's, and the row stays `Not verified` this week even when sessions have already run.
- The one sentence linking the testing plan is required once on the index and once in the release block, per S16; a second link on the index is a shortfall only when it duplicates the same row.
- A defect in the requirement's file that the Week 4 rules own, such as a missing `**Changed:**` after an edit, is a caveat when it does not change the measure, and a shortfall when it does.

### S10 — Recruitment and session plan

**Check:**

- The record's `## Participant Profile`, `## Schedule`, and `## Environment` sections.
- The record's `## Roles` and `## Consent And Data` for the session arrangements.
- `reports/week-07/README.md`'s `## Usability test` section for the recruitment target and the no-result claim.
- `pdf-info.json` and the snapshot time for the window the sessions may run in.

**met:**

- The record's `## Participant Profile` carries observable criteria: the participant's role and the task the product's target user does, the participant's familiarity with similar products, the device the session runs on, and the participant's relation to the target user.
- The recruitment target is at least three representative participants, 18 or older, outside the team, and five is the design target.
- The record states how the team will find the participants, or the dates it has arranged, and it records the target beside the profile.
- A participant is not a teammate, the customer, the instructor, or the course staff; a classmate who is not on the team may be recruited when they match the profile.
- The participant codes are `P-01`, `P-02`, and so on, assigned in the order the sessions are arranged, with a replacement under the next free code and a withdrawn code retired.
- The record's `## Schedule` gives the dates the team has arranged, or how and when it will arrange them, in person, on the university network, and which session is planned for which sprint when they straddle `SPRINT-07` and `SPRINT-08`.
- The schedule states the results-due date and that the results are due with Submission 8.
- The record's `## Environment` names the staging deployment on the university network, the seed the session starts from, and that no real payment is made.
- The record states that the staging deployment and the instrumentation are checked for the sessions: the seed reset to synthetic data before each session, no real payment, the instrumentation verified before the first counted session, the participant link working, and every pipeline event tagged `source=usability-test`.

**What does not count:**

- A recruitment target below three, no five as the design target, or a target of participants who are teammates, the customer, the instructor, or the course staff.
- A profile with no observable criteria, or one that repeats the vision's `Stakeholders` table instead of saying who matches the test.
- A schedule with no dates and no plan for arranging them, or one that puts the sessions online, on production, or off the university network.
- No seed, no no-real-payment statement, no results-due date, or no statement of which session runs in which sprint.
- Participant codes reused, assigned out of order, or a participant identity recorded in the public record.
- No replacement plan, or a withdrawn code reused.
- A report that claims a result or reports a session outcome.

**partial:**

- The profile and the recruitment target exist with the session plan, and at least one other `met` criterion fails.
- Typical shortfalls: one profile criterion missing; the design target not stated; the codes' order or replacement rule missing; the schedule without the staging or seed statement; the report claiming a result.

**missing:**

- The record has no `## Participant Profile` section, or no recruitment target and no session plan.

**Guardrails:**

- The exact participants and the exact session dates are not due this week; the team sets the dates, and a session may run as soon as the design is written, including before the design week's deadline.
- The recruitment target of three is the minimum and five is the design target; a team that plans for three is correct, and a team that plans for five is doing the design target.
- The profile is the observable test for who matches; the vision's `Stakeholders` table is background and is not the profile.
- The participants' actual sessions, their notes, and their results are Week 8's; this segment judges the profile, the target, the codes, the plan, and the environment.
- The recruitment, consent, data-access, and schedule risks and their fallbacks are S12's; this segment judges the plan the record states.
- A session that has already run is judged by the profile it matches and the plan the record states, and its result is never a Week 7 claim.

### S11 — Analysis plan and evidence map

**Check:**

- The record's `## Analysis Plan` section and the record's `results.md` link.
- `docs/usability-tests/ut-01/results.md` for the stub and its headings.
- The record's `## Evidence Map` section.
- `reports/week-07/README.md`'s `## Usability test` section for the handoff's claims.
- The record's `## Measures` and the `QR-nn` for the measures the plan reports.

**met:**

- The record states that the analysis plan is written before the first session, and it covers the per-participant table with each task's outcome and the assistance.
- The plan covers the main task's aggregate completion rate: the count or proportion that reached the end state, and the count or proportion that did so unaided.
- The plan covers the main task's median time on task.
- The plan covers the median SEQ for each task: the main task and the two secondary tasks.
- The plan covers the SUS mean and median, with `n=<count>`.
- The plan covers the thematic analysis, the severity rating, the instrumentation comparison, and the limitations.
- An additional measure the team adds is named with its statistic and its scope before the first session, and no measure is added after the data.
- `results.md` exists as the stub with the results table, the findings, the limitations, and the conclusion headings, and it carries no finding.
- The findings template is `### Finding 1` with its `**Severity:**`, `**Tasks:**`, `**Evidence:**`, `**Recommendation:**`, and `**Task issue:**` fields.
- The triage plan states that every finding is triaged, that a significant finding becomes a task issue in `SPRINT-08` when one exists, and that a behaviour change or a defect links the story and the `AC-nn` it serves and names the `FR-nnn` or `ADR-nnn`.
- A task issue from a finding cites the finding by `docs/usability-tests/ut-01/results.md#finding-1` and the finding's `**Task issue:**` links the issue; a task that is not product work says `None: repository upkeep`.
- The evidence map names the public record, the private usability-data repository and the test's telemetry export, the cloud recordings folder, the Moodle wrapper, and the Week 8 report, with no item in two places and no raw participant data in the product repository.

**What does not count:**

- An analysis plan missing the per-participant table, the aggregate completion, the median time, the per-task SEQ, the SUS mean and median, the thematic analysis, the severity, the instrumentation comparison, or the limitations.
- The SUS reported without its mean, its median, or the `n=<count>` caveat.
- A measure added after the first session, or an added measure with no statistic or no scope.
- `results.md` carrying a finding, a result, or a verdict before the results are written.
- A findings template missing a field, or a triage plan that opens no task issue when a significant finding exists.
- A finding's task issue with no citation of the finding, or one whose `### Requirements` says `None: repository upkeep` for product work.
- An evidence map that puts the recordings or the raw notes in the product repository, or the same item in two places.
- An analysis plan written after the first counted session, when the first session's date precedes the plan's first commit.

**partial:**

- The analysis plan and the `results.md` stub exist with the minimum measures, and at least one other `met` criterion fails.
- Typical shortfalls: one minimum measure missing; the `n=<count>` caveat missing; the findings template incomplete; the triage plan missing; the evidence map leaving the private repository or the Moodle wrapper out.

**missing:**

- The record has no `## Analysis Plan` section, or `results.md` is absent.

**guardrails:**

- The plan's prose, its table columns beyond the required measures, and the triage's wording are the team's; the criteria are the minimum measures, the statistics, the `n` caveat, the findings template's fields, the triage plan, and the evidence map.
- The plan is the minimum every team reports and may add a measure the product needs, provided the plan names the measure, its statistic, and its scope before the first session.
- The plan reports the measures the `QR-nn` does not read as analysis results; the `QR-nn` reads one measure and S9 judges which.
- The results, the findings, the severity assigned to a finding, and the triage's execution are Week 8's; this week judges the plan and the templates that the run week will fill.
- The evidence map and the private home are S8's for the private repository's state; this segment judges the map's coverage and the no-raw-data claim.
- A results stub with empty sections is correct; a stub that carries a result or a finding is not.

### S12 — Glossary and risk register

**Check:**

- `docs/glossary.md` in the snapshot, for the Week 7 terms and their definitions.
- `docs/risks.md` in the snapshot, for the four Week 7 risks, their fields, and the summary table.
- The Week 7 pull requests that added the terms and the risks.

**met:**

- `docs/glossary.md` carries one `###` section for `usability test`, `participant`, `usability session`, `consent`, `recording`, `measure`, `metric`, `statistic`, `SUS`, and `SEQ`.
- Each term's definition is one sentence that says what the term means in this project, and `measure`, `metric`, and `statistic` are kept apart: a measure is what a session records, a statistic is the summary computed from it, and a metric is a product-analytics number.
- A term an artifact already defines carries its `**Defined by:**` line, and the term's anchor is the term alone.
- `docs/risks.md` carries the recruitment risk, the consent risk, the data-access risk, and the schedule risk, each a `## RISK-nn` section with its first line stating the cause, the event, and the impact.
- Each new risk carries `**Status:** Open`, `**Impact:**` and `**Likelihood:**` with their reasons on nested bullets, `**Trigger:**`, `**Window:**`, `**Mitigation:**`, and `**Contingency:**`.
- The recruitment risk's contingency is the recruitment fallback: recruit replacements, and when three participants still cannot be recruited, keep the `QR/QRT` row `Not verified` in `SPRINT-08` or move it to `SPRINT-09`, declare the shortfall, and claim no result.
- The consent risk's contingency is the withdrawal fallback: do not count the session, remove the raw text and the recording, retire the code, and recruit a replacement under the next code.
- The data-access risk's contingency is the access fallback: create the private repository and the recordings folder with the team and the instructors, and when an instructor cannot use GitHub, give the private text through a Moodle-only archive and declare the deviation.
- The schedule risk's contingency is the schedule fallback: move the `QR/QRT` row to `SPRINT-09` with a reason, declare it in the report, and claim no result.
- The register's summary table carries the four risks with the columns `ID`, `Status`, `Impact`, `Likelihood`, and `Risk`, the open risks first and sorted by impact then likelihood, and the settled ones after them in identifier order.

**What does not count:**

- A missing Week 7 term, or `measure`, `metric`, and `statistic` defined as one thing or swapped.
- A definition that is generic rather than the project's meaning, or a term section without its one-sentence definition.
- A missing recruitment, consent, data-access, or schedule risk.
- A risk without its first-line statement of cause, event, and impact, or missing `**Trigger:**`, `**Window:**`, `**Mitigation:**`, or `**Contingency:**`.
- A `**Status:**` other than `Open` on a new risk that has not settled, or an `Open` risk with no `**Outcome:**` after it settled.
- A contingency that is a restatement of the mitigation, a generic "we will handle it", or that omits the required fallback for its failure mode.
- A summary table that does not list the new risks, lists them unsorted, or disagrees with the sections' statuses.

**partial:**

- The terms and the four risks are present with most of their fields, and at least one other `met` criterion fails.
- Typical shortfalls: one term missing or one definition generic; one risk missing a field; a contingency that omits the Moodle archive or the `SPRINT-09` move; the summary table not updated.

**missing:**

- The glossary carries none of the Week 7 terms, or `docs/risks.md` carries none of the four risks.

**guardrails:**

- The glossary's earlier terms and the register's earlier risks are not re-graded; this segment judges the Week 7 additions and the summary table's state.
- The definitions' wording, the risks' ratings, and the mitigation are the team's; the criteria are the ten terms' presence and distinction, the four risks' fields, and the fallbacks' required content.
- A risk that has already materialized is settled with its `**Outcome:**`, and an open risk that a Week 8 result will settle stays `Open` this week.
- The register's summary table moves as risks settle and the sections do not; a table that disagrees with a section's status is a shortfall in S12, not in the risk's own row.
- The four fallbacks are the week's own: a team that writes a different, equivalent fallback is correct when it covers the same failure mode, and a fallback that leaves the `QR/QRT` row claiming a verdict is not.
- The risks' windows and triggers are read against the week; a window that already closed without its trigger is a caveat, not a shortfall.

### S13 — Week 6 action points and open questions

**Check:**

- `reports/week-06/meeting-report.md` in the snapshot, for its `## Action points` and `## Open questions`.
- `reports/week-07/meeting-report.md` in the snapshot, for `## Previous action points` and `## Previous open questions`.
- The artifacts the outcomes claim to have changed, in the snapshot.
- The Week 6 report's own content against the snapshot, to confirm it was not edited.

**met:**

- Every Week 6 action point due by Week 7, and every action carried from an earlier report, has its outcome in the Week 7 report's `## Previous action points` table.
- The table's `Action` cell cites the action point by `reports/week-06/meeting-report.md#action-points` with the action quoted, and its `Outcome` says whether it was carried out, what was found, and links each artifact the outcome changed and the task issue that carried it out, if any.
- The table's `Decision` cell links each `DEC-nnn` the outcome produced, or says `None` when the outcome needed no decision.
- Each outcome that changed an artifact is carried into that artifact, and an outcome recorded only in the table has not been carried out.
- Every Week 6 open question is answered in `## Previous open questions` with its `Answer` linking each artifact the answer changed and its `Decision` linking the `DEC-nnn` or saying `None`, or it is carried forward into the Week 7 report's `## Open questions`.
- The Week 6 report is not edited: its text at the snapshot is the text the Week 6 submission recorded.

**What does not count:**

- A Week 7 report without `## Previous action points` or `## Previous open questions` when the Week 6 report has an action point due by Week 7 or an open question.
- An action point's `Outcome` recorded in the table with no change to the artifact it names.
- An open question dropped with no answer and no carried-forward row.
- An action point whose `Outcome` says it was completed while the artifact shows otherwise.
- An edit to the Week 6 report, such as a rewritten outcome or a removed table.

**partial:**

- The previous sections exist with the outcomes, and at least one other `met` criterion fails.
- Typical shortfalls: an action point missing its citation or its artifact link; an open question carried forward without a row; a decision cell empty instead of `None`; one outcome not carried into its artifact.

**missing:**

- The Week 7 report has neither `## Previous action points` nor `## Previous open questions`, or no Week 6 report exists and no carried action or question replaced it.

**guardrails:**

- A Week 6 report with no action point due by Week 7 and no open question makes `None` in the matching `## Previous` section correct, and it is never a shortfall.
- An action point due in Week 8 is not due this week; it is judged from the Week 7 report's own new action points in S14, and a Week 6 action that reappears in the Week 7 report's `## Action points` with a later due week is correct.
- When the Week 6 report is absent from the snapshot, judge this week's work against what exists and report the absence once, here, rather than re-judging the Week 6 submission.
- The Week 6 report's prose and its earlier actions are Week 6's; this segment judges the outcomes and the questions' closure, and the Week 6 report itself is not re-graded.
- A carried action with an `Outcome` of `Not done` reappears with a new due week, and its absence from the Week 7 `## Action points` is a shortfall here unless the team or the customer dropped it, which the `Outcome` then says.
- An artifact change recorded after `ISSUE_CUTOFF` is a caveat and never repairs the outcome at the cutoff.

### S14 — Customer validation of the test design

**Check:**

- `reports/week-07/meeting-script.md`, `reports/week-07/meeting-report.md`, and `reports/week-07/meeting-transcript.md` in the snapshot.
- The Week 7 meeting's date against the Week 7 window, the cutoff, and the class week.
- The `DEC-nnn` entries in `docs/decisions.md` that the report cites, and the artifacts the decisions change.
- The script's and the report's first commits and pull requests, for whether the script came before the meeting.
- The meeting's recording and transcript claims against the Moodle PDF's items 7 and 8.

**met:**

- At least one customer meeting was held in the Week 7 window, on or after Friday 6 November 2026 and by `ISSUE_CUTOFF`, and the design review is that meeting, the sprint's Sprint Review.
- The script was written before the meeting and carries `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in order.
- `## Agenda` starts with the three permission questions, shows the deployed production instance and the `UT-01` record and the staging deployment, then the surveys, the tasks, the instrumentation and its verification, the consent and the private repository, the recordings folder, the session plan, the `QR/QRT`, and the Week 8 plan; it puts the open questions before the last part and ends with the read-back of the decisions and action points.
- The script's questions serve the target in `## Context`: the design's fit to the customer's questions, the participant profile, the recruitment target, the session plan, and what the results must show.
- The script shows at least one rewritten question in `## Key improvements`, with the before, the after, and the principle behind the rewrite.
- The report's `## Metadata` is a bulleted list with the date, the duration, the attendees by GitHub username with `Customer` for the customer, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- The report's `## Summary` has 3 to 5 bullets on what the meeting settled or changed, not on what was on the agenda.
- The report's `## Decisions` lists each decision with a `DEC-nnn` entry that the report cites, and each entry's decision agrees with the report's account.
- The report's `## Action points` has at least two rows with the columns `Action`, `Owner`, and `Due`, the owner is a GitHub username, each due date falls in a named week after Week 7, and at least one falls in Week 8.
- The report's `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`, and the report's `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`.
- The meeting agrees the Week 8 execution plan with the customer: how the team will arrange the sessions and the results date.
- A transcript exists when the meeting was recorded or held in writing, is written in English with one sentence per line and a timestamp and speaker label, carries the date and attendees above the first line, and is sanitized; when the customer refused publication, the transcript is not committed and the report says so.
- The report claims no usability result, and it is the team's own account rather than a generated or pasted transcript summary.

**What does not count:**

- No customer meeting in the Week 7 window, or a meeting after `ISSUE_CUTOFF`.
- A script written after the meeting, or a script with the agenda out of order, with no permission questions first, with no deployed instance or `UT-01` design shown, or with no read-back last.
- A script with no questions that could change the design, or with no rewritten question in `## Key improvements`.
- A report without its `## Metadata` items, with fewer than 3 or more than 5 summary bullets, with a decision that has no `DEC-nnn`, or with an action point due inside Week 7.
- An action point with no owner, no due week, or a due date with no week named.
- A missing `## Open questions` or `## Disagreements` section when the meeting had one.
- A transcript that restates raw notes, carries a real name, email address, phone number, address, or recording link, or is committed after the customer refused publication.
- A report that restates the transcript line by line, or that a tool generated and the team pasted in unchecked.
- A report that claims a result, a session outcome, or a verdict.

**partial:**

- The meeting report and the script exist with the review's content, and at least one other `met` criterion fails.
- Typical shortfalls: one agenda part out of order; a permission question unanswered in the metadata; fewer than two action points or none due in Week 8; the Week 8 plan not agreed; the transcript unsanitized or missing when the meeting was recorded; a report that claims a result.

**missing:**

- `reports/week-07/meeting-report.md` is absent, or no Week 7 customer meeting is recorded.

**guardrails:**

- The meeting is the Sprint Review, so a second review meeting is not required and the two are judged together; a team that held one design review has met the ceremony.
- A meeting held on 13, 14, or 15 November 2026 is in the Week 7 window and is a caveat in `**Evidence:**` rather than a shortfall, because the submission deadline, not the class week's end, closes the window; a meeting after `ISSUE_CUTOFF` is a shortfall.
- An asynchronous meeting held in writing is allowed, with the written exchange as its transcript and the substitution declared as a deviation; its `## Roles` and its timeboxes are not required.
- A customer who refused recording or publication makes the transcript's absence correct, and the report's `None` with the reason is complete.
- The recording is Moodle-only and the public report names it; the transcript is public only when the customer allowed publication.
- Story verdicts are judged only when the meeting showed stories; Week 7 is a design sprint, so showing no new story is correct and is not a shortfall.
- The decisions the review records are judged here for their agreement and citation; what the team did with them is S15's.
- The report's prose, its summary's wording, and the meeting's length are the team's; the criteria are the sections, the agenda's order, the action points' shape, the transcript's existence and hygiene, and the no-result claim.

### S15 — Design-review rework and testing-plan rows

**Check:**

- `reports/week-07/meeting-report.md`'s `## Decisions` and the `DEC-nnn` entries.
- The pull requests and commits merged after the meeting and by `ISSUE_CUTOFF`, from `prs.json` and `commits.json`.
- The record, `surveys.md`, `consent.md`, the task issues, `docs/project-plan.md#quality-requirement-testing-plan`, and the `QR-nn`/`QRT-01` files at the snapshot and in the Week 7 pull requests.
- `reports/week-07/README.md` for the declared moves and the `## Deviations` entry.

**met:**

- Each decision the design review recorded is applied by the cutoff to the artifact it changes: the record when the design changes, the surveys when the instruments change, the consent when a clause changes, a task issue when the work changes, the testing plan when a row changes, and the `QR-nn` and its `QRT-nn` when the sub-characteristic, the measure, or the bar changes.
- A same-week rework is merged into `main` as a pull request, not left as an action point for a later week.
- Each testing-plan row the team's own plan scheduled for `SPRINT-07` is run, or moved to `SPRINT-08` with a reason, and every move is declared in the Week 7 report.
- The testing plan records each row's result, its `Checked` sprint, and its evidence, and a `Passes` or `Fails` row links the proof its level requires.
- A row the team runs is run at its level, and its evidence is the run, the output, or the sanitized report its level requires.
- When the review changes the requirement's sub-characteristic, measure, or bar, the requirement, its test, and the testing plan still agree, and the bar was set before the first counted session.

**What does not count:**

- A decision recorded in the report but not applied to the artifact by the cutoff.
- A rework still listed as an action point due in a later week.
- A `SPRINT-07` testing-plan row silently dropped, or moved without its reason and its declaration.
- A testing-plan row whose `Status`, `Checked`, or `Evidence` was not updated after the row was run.
- A `Passes` or `Fails` row with no evidence, or evidence that does not match the test's level.
- A bar changed after the first counted session, or a requirement changed while its test and plan row still name the old measure.
- A `QR/QRT` verdict recorded in the testing plan this week, when the results are due with Submission 8.

**partial:**

- The review's decisions are applied and the testing plan is updated, and at least one other `met` criterion fails.
- Typical shortfalls: one decision not applied; one row moved without a declared reason; one row run without its `Checked` update; the bar or the measure changed with the test not updated.

**missing:**

- The design review recorded at least one decision and no artifact changed, or a `SPRINT-07` testing-plan row was due and neither ran nor moved.

**guardrails:**

- A sprint whose plan scheduled no row for `SPRINT-07` owes no run, and the usability requirement's row stays `Not verified` with `Planned for sprint: SPRINT-08` even when sessions have already run, per S9; the absence of a `Passes` or `Fails` row this week is never a shortfall.
- A review that asked for no change makes the absence of rework correct; the team records that in the report, and S14 judges the report's account.
- A docs-only rework may be one pull request for the record and one for the plan; the criterion is that the artifact the decision names changed by the cutoff.
- The release's sequence and its tag are S16's; this segment judges the artifacts the review changed, not the release order.
- A decision applied after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff.
- The design review's decisions are read for what they change; a decision that changes nothing is a decision the team records but no artifact owes, and it is not a shortfall here.

### S16 — REL-07 release

**Check:**

- `tags.json` and `releases.json`, and the raw `gh api "repos/$REPO/releases?per_page=100"` and `gh api "repos/$REPO/git/refs/tags/<tag>"` responses for the title, the body, and the commit.
- `CHANGELOG.md`'s `[Unreleased]` section and its dated released section.
- `docs/project-plan.md`'s `#### REL-07` block under `### SPRINT-07`.
- The `SPRINT-07` GitHub milestone's state and the issues rescheduled out of it.
- The testing plan's `Checked` cells, for the `**Checked QRs:**` list.
- `gh api "repos/$REPO/rulesets"` and each tag ruleset, for the tag's protection.
- `reports/week-07/README.md` for the release's record and its tag.
- The tag's push time and the merge times of the changelog, the plan's block, and the report.

**met:**

- The tag is named `v<major>.<minor>.<patch>`, it points at a commit on `main`, and that commit is the final production commit the week's record names.
- The release title is the tag, so the title and the tag match.
- The tag is protected against being moved or deleted, by a repository ruleset that covers tag pushes or an equivalent tag-protection rule.
- `CHANGELOG.md` follows Keep a Changelog: `[Unreleased]` was kept through the week, the released entries moved into a dated section such as `[0.7.0]` with `### Added` entries for the week's changes, that section links the release, and a new empty `[Unreleased]` follows.
- The release body is the upgrade note: it states whether the upgrade requires anything beyond deploying this version, or that it does not, and names the new environment variables and configuration when it does.
- When the release is docs-only, its body says there is no product change and no upgrade is required, and the tag is the team's next version.
- The body ends with the line `[Full changelog](<absolute url>)` linking the changelog's released section, and nothing comes after it; the body carries no address, credential, token, or other private-only value.
- `### SPRINT-07` carries a `#### REL-07` block with `**Released:**` and `**Checked QRs:**`.
- `**Checked QRs:**` lists every `QR-nn` with at least one test whose testing-plan row is `Checked` in `SPRINT-07`, one bullet each linked to its requirement file, or says `None` when none was checked, and after the list one sentence links the plan's `## Quality Requirement Testing Plan` once.
- `SPRINT-07`'s GitHub milestone is closed after each issue still open was moved into a later sprint's milestone.
- The tag was pushed on the release commit after the sprint's pull requests merged, and before the changelog's released section, the plan's `REL-07` block, and the report were merged.

**What does not count:**

- A tag on a commit that is not the final production commit, a tag on a branch name, or a tag on a commit that is not on `main`.
- A release title that is a nickname while the tag is the version, or a version without the `v` prefix.
- An unprotected tag, or one that a force push or a deletion could move.
- A body that lists the changelog's entries instead of the upgrade note, a body with no upgrade statement, or a body that ends with anything other than the `Full changelog` line.
- A relative changelog link, a body carrying a dashboard address, a credential, or the query endpoint.
- A changelog section that does not link the release, a missing `[Unreleased]`, or a released section with no dated heading.
- A `REL-07` block outside `### SPRINT-07`, or one missing its `**Released:**` or its `**Checked QRs:**`.
- A `**Checked QRs:**` list copied from `REL-06`, built from a requirement's status rather than its tests' `Checked` cells, or missing the one sentence that links the testing plan.
- `SPRINT-07`'s milestone left open, or closed with issues still in it.
- A tag pushed after the changelog's released section, the plan's block, or the report was merged.

**partial:**

- `REL-07` exists with a tag and a released changelog section, and at least one other `met` criterion fails.
- Typical shortfalls: a tag on a commit that is not the week's final production commit; an unprotected tag; a title that does not match the tag; a changelog section that does not link the release or a missing `[Unreleased]`; a body missing the upgrade statement or the `Full changelog` line; a private-only value in the body; a missing `**Released:**`; a `**Checked QRs:**` list that is wrong; a milestone left open; a tag pushed after the record was merged.

**missing:**

- No `REL-07` tag or release exists at the cutoff, or the plan has no `#### REL-07` block.

**guardrails:**

- The version number is the team's SemVer choice; the criteria are the tag's shape, its target, its protection, and the record's completeness.
- A docs-only release is correct this week because the usability results are Week 8's; the body's no-product-change statement replaces a product upgrade note.
- `**Checked QRs:**` is built from the testing plan's `Checked` cells and from nothing else: a requirement with a checked test belongs, whatever the row's `Status`, and a requirement with none does not.
- The tag's and the release's timing is read against `ISSUE_CUTOFF`; a tag placed after the cutoff is a caveat in `**Evidence:**` and never repairs the state at the cutoff, and a release page edited after the cutoff is drift.
- The changelog's `[Unreleased]` upkeep through the week is judged here as part of the released section, and the Week 5 and Week 6 released sections are not re-graded.
- The sprint milestone's close is judged from its state and the issues' milestones at the cutoff; an issue moved to `SPRINT-08` with its events is the expected record.
- The release body's exact shape is the team's, and the two required facts are the upgrade action (or that none is needed) and the `Full changelog` line; a body that states them in a different order is correct.
- `REL-06`'s tag, body, and changelog section were Week 6's and are not re-graded.

### S17 — Sprint close and retrospective

**Check:**

- `docs/project-plan.md`'s `### SPRINT-07` section and its `**Actual Velocity:**` field.
- The `User Story` issues closed as completed in `SPRINT-07`'s milestone at `ISSUE_CUTOFF`, and their `Story Points`.
- `reports/week-07/sprint-retrospective.md` in the snapshot.
- `reports/week-06/sprint-retrospective.md`'s `## Actions` rows with `Carried: Yes`.
- The pull requests in the Week 7 window that changed the plan and the retrospective.

**met:**

- `### SPRINT-07` carries `**Actual Velocity:**` as a whole number, and it equals the sum of the `Story Points` of the stories closed as completed in `SPRINT-07`'s milestone.
- One sentence after the figure says what moved out of the sprint and to which sprint.
- A sprint that carried only tasks has `0`, and the sentence says the sprint was a task sprint.
- `reports/week-07/sprint-retrospective.md` carries `## What Went Well`, `## What Did Not`, `## Actions`, and `## Carried Actions`.
- `## What Went Well` lists 3 or more items; `## What Did Not` lists 2 or 3 items with their root causes; `## Actions` lists 3 or 4 actions with their `Owner`, `Impact`, `Reason`, and `Carried` flag.
- `## Carried Actions` carries each `SPRINT-06` action marked `Carried: Yes`, cites `reports/week-06/sprint-retrospective.md#actions` with the action quoted, and gives each an `Outcome` of `Done`, `Not done`, or `Dropped`.
- Every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.

**What does not count:**

- An `**Actual Velocity:**` copied from `**Planned Velocity:**`, or a figure that does not match the completed stories' points.
- A velocity figure with no sentence on what moved out.
- A retrospective with the four headings but no root causes, or with fewer than the required rows.
- An action with no `Owner`, no `Impact`, no `Reason`, or no `Carried` flag.
- A carried action with no quoted action, no anchor citation, or no `Outcome`.
- A `Not done` action that is not re-listed in `## Actions`, or a `Done` action re-listed as if it were open.

**partial:**

- `**Actual Velocity:**` is set and the retrospective exists, and at least one other `met` criterion fails.
- Typical shortfalls: a velocity figure that does not equal the completed stories' points; a missing sentence on what moved out; a missing retrospective section or a row count short of the minimum; a `What Did Not` item with no root cause; an action without its `Owner`, `Impact`, or `Reason`; a carried action missing its citation, its quote, or its `Outcome`; a `Not done` action not re-listed.

**missing:**

- `**Actual Velocity:**` is absent from `### SPRINT-07`, or `reports/week-07/sprint-retrospective.md` is absent.

**guardrails:**

- Velocity is computed by hand from the stories' `Story Points`, because the single-select field cannot be added up; the segment checks the arithmetic against the completed stories at the cutoff.
- A story is completed when it is closed as completed in `SPRINT-07`'s milestone by `ISSUE_CUTOFF`; a story moved out before the close does not count, and the sentence on what moved out names it.
- A design sprint that carries only tasks has `0`, and that is correct; a task-only sprint with a figure, or with no sentence saying it was a task sprint, is a shortfall.
- The retrospective's prose, its exact action wording, and its root causes' depth are the team's; the criteria are the four sections, the row counts, the columns, and the carried actions' shape.
- The Week 6 retrospective's own shape is not re-graded; this segment judges the actions it marked `Carried: Yes` and what the Week 7 file does with them.
- `**Planned Velocity:**` belongs to S1 and the `REL-07` block to S16; a plan whose figures disagree is reported in the segment that owns the wrong field.
- A retrospective written after the cutoff is a caveat in `**Evidence:**`, not a shortfall, unless the file plainly copies the report's summary.

### S18 — Week report and submission

**Check:**

- `reports/week-07/README.md` in the snapshot, read whole, and every repository file it links.
- `reports/week-07/images/` when the report embeds an image, with `scripts/image_info.py` when a file's size or transparency matters.
- The Moodle PDF under `itpd-assignments-feedback/A7/submissions/<team_dir>/`, read once, for its items, its page count, and its addresses.
- `pdf-info.json` for the repository, the permalink, the SHA, the page count, the recording link, and the permalink-week check.
- `runs_main.json` and `runs_sha.json` for the latest link-check, Markdown-check, `actionlint`, and product-code runs on `main`, and the merged pull requests in the Week 7 window.
- `prs.json` for one merged pull request that closed its task issue.
- `scripts/check_snapshot_links.py` for the report's links and anchors.
- The submission procedure's merge and snapshot.

**met:**

- `reports/week-07/README.md` exists at the snapshot, is merged into `main`, and the snapshot is taken from that commit.
- The report identifies the week, the project, the team, and the covered scope.
- The report's summary says that the test is designed and the recruitment is planned, gives the recruitment target and the participant profile, the `QR/QRT`, the private repository, the recordings folder, the test's instrumentation and what was verified, the team's session plan, and the fact that no usability result is claimed.
- The summary says whether the design review's transcript was published, shared privately, or not made, and why.
- The summary says whether the focus metric has a value yet and what it would need, links `docs/analytics.md` and `docs/observability.md`, and copies no chart or row from either page.
- The summary points at `docs/project-plan.md#quality-requirement-testing-plan` for the rows that are not `Passes` and copies none of them.
- The summary says the team arranges the sessions and the results are due with Submission 8, and it carries the Week 8 handoff: the design, the recruitment target, the private repository and the recordings folder, the instrumentation and its verification, the `QR/QRT` row in `SPRINT-08`, and the `results.md` stub and the analysis and triage plan.
- The report carries the `## Usability test` section with the design summary, the recruitment target and the participant profile, the tasks, the surveys, the instrumentation and its verification, the consent and the private repository with the test's telemetry export, the link-check exclusion and its reason, the recordings folder, the session plan, the `QR/QRT`, and the Week 8 handoff.
- The report carries the coverage table with the 21 rows of `assignment-7.md`, in its order, and each artifact cell links its artifact: a repository file by its path from the repository root and the heading anchor when the row names a section, and anything else with descriptive link text.
- A coverage row whose artifact is not public, or whose absence the report explains, says so instead of linking it; when the customer refused publication of the transcript, the Meeting transcript row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table, and the report carries no separate usability results report or result claim.
- The report carries the repository evidence: one merged pull request that closed its task issue, and the latest green link-check, Markdown-check, `actionlint`, and product-code CI runs on `main`, each by its run URL, and each run's `conclusion` is `success`, its branch is `main`, and its `head_sha` is an ancestor of the snapshot.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- The report carries `## Deviations`, naming anything done differently, including a participant who could not be recruited or recorded, a private repository or recordings folder the instructors could not access, a `SPRINT-07` testing-plan row moved to `SPRINT-08` with its reason, an asynchronous meeting, and a staging deployment that was unavailable.
- The report carries a contribution table mapping each member's GitHub username to the work done, using links to their commits, pull requests, or reviews where possible, and the report does not assess an individual.
- The report carries `## Privacy`: one line that no private-only material was committed to the product repository, and no participant identity was committed to it.
- The Moodle PDF carries items 1–9: the project name and team number, the member table with GitHub username, real name, and university email, the permalink to `reports/week-07/README.md` at the full commit hash, the private usability-data repository URL and the access instructions and the recordings folder URL and the access instructions, the product's staging and production addresses on the university VM with the university-network note, the staging analytics dashboard and backend addresses and credentials and the staging observability dashboard, backend, and query addresses and credentials, the design review's recording link or the line saying why there is none, the transcript appendix when the customer refused publication, and the one-line privacy confirmation.
- The PDF's permalink points at `reports/week-07/README.md` at the same full 40-character SHA the snapshot uses; a bare SHA with no repository permalink does not satisfy it.
- The PDF is two pages or fewer, excluding a transcript appendix, and carries no participant identity and no deck.
- The report and every repository file it links are merged into `main` at the snapshot; nothing the assignment requires is left on an unmerged pull-request branch.
- The report's own text and the snapshot carry no real address, credential, token, real name, email address, or participant identity.

**What does not count:**

- A report that is not on `main`, or a permalink that names a branch, a tag, a short SHA, or a bare SHA with no URL.
- A report at the snapshot that differs from the merged `main` report the permalink names.
- A summary that copies a metric's value or a testing-plan row instead of linking it, or one that omits the designed test, the recruitment target, the no-result claim, or what the team left open for Week 8.
- A summary without the transcript's publication status, without the focus metric's state, or without the Week 8 handoff.
- A report without the `## Usability test` section, without `## Deviations`, or without the `## Privacy` line.
- A coverage table that omits a row, reorders the rows, or has a row whose link does not resolve; a row that neither links its artifact nor says why it is not public or absent.
- A report without a contribution table, or one that rates or explains a member's contribution.
- A workflow's run list page, a branch's run history, or a job URL as the run link: the report needs the individual green run's URL.
- A green run on a branch other than `main`, a pull-request run, or a run on a commit that is not an ancestor of the snapshot.
- A red, cancelled, or in-progress run cited as green; read `conclusion`, not the run's existence.
- A repository-evidence claim with no merged pull request or with no green `main` run.
- A Moodle PDF with a missing private-repository or recordings-folder link or access instruction, a missing staging or production address, a missing staging analytics or observability credential, a missing recording link or its reason, or no member table with university emails.
- A PDF longer than two pages, a deck included, or a participant identity in it.
- A private-only value committed in the repository, including a real address in the report's prose, a participant identity, or a screenshot that carries one.
- A submission that names the wrong week's report, or a permalink that points at `reports/week-06/README.md`.
- A Markdown wrapper instead of the PDF.

**partial:**

- `reports/week-07/README.md` and the Moodle PDF exist, and at least one other `met` criterion fails.
- Typical shortfalls: a report not merged or a permalink with a short or bare SHA; a missing week, project, team, or scope line; a summary without the design, the recruitment target, the no-result claim, the transcript's status, the focus metric's state, or the Week 8 handoff; a missing `## Usability test` section; a missing coverage row, a reordered row, or a non-resolving link; a missing contribution table or an individual assessment; missing repository evidence or a red `main` run; a missing or thin `## Deviations`; a missing privacy line; a PDF missing an item, over two pages, or carrying a deck; a private-only value in the repository; a wrong-week permalink.

**missing:**

- `reports/week-07/README.md` is absent at the snapshot, or the Moodle PDF is absent.

**guardrails:**

- The primary index is `reports/week-07/README.md`; a permalink to another week's report is the wrong-week shortfall, and the fetcher's `permalink_week_mismatch` records it.
- The report's prose, its section order beyond the required sections, and its length are the team's; the criteria are the required content, the links, and the evidence.
- The Moodle PDF's real names, emails, and addresses stay in the work directory and are never copied into feedback; a finding is reported by path and kind, such as "the PDF names the private repository but gives no access instructions".
- The design week's report claims no result; a session that has already run does not change that, and the report's summary of a session is a shortfall unless it is the session plan and not a result.
- A `Passes` claim in the report is not re-judged here; the testing plan's rows are S9 and S15's, and the report's pointer is judged for its existence and its no-copy rule.
- The snapshot's commit time against the deadline is a caveat in `**Evidence:**`, never a status change; a submission after the deadline is the instructor's late-penalty question, not this rubric's.
- A Markdown wrapper instead of a PDF is a shortfall here, and the fetcher's Markdown path records it.
- The coverage row that names why there is no transcript is correct when the customer refused publication; the PDF's appendix is the transcript itself, and the row points at the Moodle submission.
- A coverage row for an artifact the owning segment finds missing says so and is not a second shortfall here; the missing artifact is judged in its own segment.
- The contribution table is evidence of who did what, not a grading of a member; a table with links to merged work is correct even when one member has fewer rows.

### S19 — AI usage and honesty

**Check:**

- `reports/week-07/ai-usage.md` in the snapshot.
- The report's AI usage coverage row.
- The team's root `AGENTS.md`, for the AI trace it carries.
- The Week 7 commits and pull requests' trailers and messages, when a claim is checkable.
- The AI policy in `course/rules.md`.

**met:**

- `reports/week-07/ai-usage.md` exists and names each AI tool the team used, what it was used for, and what the team accepted, changed, or rejected from its output, with the reason for each rejection.
- When the team used no AI tools, the file says so in one line, and that line is complete.
- The file says whether an agent was given any usability material; if one was, the file confirms it was given the sanitized note rather than the raw recording or the private notes, and if none was, the file says so.
- The report's coverage table links the file, and the link resolves to the file the report names.
- The file's claims are consistent with the repository's AI trace: a tool it says it used appears in the team's `AGENTS.md` or its commits, and a tool it does not mention is not claimed elsewhere in the submission.
- The file carries no private-only material, no participant identity, no prompt that contains personal data, and no tool output copied wholesale.

**What does not count:**

- A file that names a tool with no use and no disposition.
- A generic "we used AI for coding and writing" with no accepted, changed, or rejected output.
- A rejection with no reason, or an accepted output that no artifact reflects.
- A file copied unchanged from an earlier week with no Week 7 content, including the agent-and-usability-material answer.
- An agent given the raw recording, the private notes, or a participant identity.
- A coverage row that links a file other than `reports/week-07/ai-usage.md`, or no row at all.
- A file that carries a participant identity, a real name, an address, a credential, or a prompt with personal data.

**partial:**

- `reports/week-07/ai-usage.md` exists with the tools and their uses, and at least one other `met` criterion fails.
- Typical shortfalls: one tool with no disposition; a rejection with no reason; the agent-and-usability-material answer missing; the coverage row missing or pointing at another file; an inconsistency with the AI trace.

**missing:**

- `reports/week-07/ai-usage.md` is absent.

**guardrails:**

- The file's language, its shape, and the number of tools are the team's; the criteria are the tools and their uses, the disposition of the output, the no-AI line when it applies, the usability-material answer, the coverage row, and the consistency with the repository's trace.
- The team is never required to have used an AI tool; a one-line no-tools answer is complete and is never a shortfall.
- The course's AI policy requires disclosure and the team's responsibility for what it submits; this segment judges the report, not the amount of AI use.
- The AI trace is the team's `AGENTS.md` and the commit and pull request trailers and messages; the team's `AGENTS.md` is not re-graded on its Week 4 requirements.
- The Week 6 AI usage file and its claims are Week 6's and are not re-graded; this segment judges the Week 7 file and the Week 7-specific question about usability material.
- Generated text submitted unchecked, or filler passed off as analysis, is a shortfall where a criterion names it, and it is never a reason to lower a status that the substance already meets.

## Semantic feedback

`agent-semantic-feedback.md` is the optional companion file defined in `docs/semantic-feedback-format.md`.
The semantic agent writes it after the compliance report is final, when the operator runs the semantic pass.
The compliance agent does not write the companion file.
The semantic agent starts from the report as a map, verifies each claim its verdict rests on against the snapshot at the saved SHA or the saved evidence, and never edits `agent-compliance-feedback.md`.
It never changes a status, an `Evidence gaps` flag, `Manual review required`, the overall assessment, or the grade; a segment may be `met` while its dimension is `thin`.

The five dimensions, in this order:

| Dimension | Segments | The question |
|-----------|----------|--------------|
| Design | S3, S5, S7, S10 | Could a stranger who was not in the room run this test and get sessions that compare? |
| Evidence | S4, S6, S8, S9, S11 | Could the team and its instructors answer what the sessions showed, compute the same statistics, and keep the raw data lawful and private? |
| Plan | S1, S2, S12, S16, S17 | Is the design sprint a forecast the team could steer by, and does its release leave Week 8 a clean start? |
| Customer loop | S13, S14, S15 | Did the design review change the test, and did the change reach the record, the plan, and the release? |
| Publication | S18, S19 | Can a reader who trusts the public record find the design, follow the evidence, and see what the team did without the raw data? |

### Design

Ask whether a stranger who was not in the room could run the test from the record and get sessions that compare with each other.
Read the index and the record's heading and fields, the goal and the research questions, the participant profile and the recruitment target, the one main and two secondary tasks with their start points and end states, the fixed order and the no-label wording, the protocol's session order, the facilitator and observer roles, the same-facilitator rule, the dry run, the session plan, and the environment's staging and seed statement.

`thin` when the record is complete but a session would depend on asking the team something: the profile is a copy of the vision's stakeholders, a task names a screen or a step, the order changes between participants, the raw schedule is a promise with no plan, or the dry run was never recorded.
`not yet adequate` when the record cannot be run without the team: the tasks are missing their success criteria, the facilitator's rule and the stop rule are absent, the roles are names rather than usernames, or the participant code scheme would not tell one session's data from another's.

### Evidence

Ask whether the team and the instructors could answer what the sessions showed, compute the same statistics, and keep the raw data lawful and private.
Read the surveys and the SUS formula, the measures the record names, the instrumentation section and its session link, the event table and the `source` rule, the verification run and its date, the consent template and the private repository's declaration, the retention rule, the `QR-nn` and its manual test, the analysis plan and its statistics, the findings template, the triage plan, and the evidence map.

`thin` when the instruments are the students' but the plan would not settle a result: the SUS formula is right and the plan reports no `n=<count>` caveat, the instrumentation covers the main task but not the questions, the verification is a teammate's run with no store named, the consent template is complete but the recordings folder is an address in the report, or the requirement reads a measure the analysis plan reports only as an aside.
`not yet adequate` when the evidence cannot be kept or trusted: the test would write to production, an event carries personal data, the consent omits the recording or the sanitized public results, the private home is the product repository, the requirement's bar is an adjective, or the analysis plan would let the team choose its statistics after the data.

### Plan

Ask whether the sprint was a forecast the team could steer by, and whether its release and handoff leave Week 8 a clean start.
Read the `SPRINT-07` goal and its planned velocity, the refined backlog, the design tasks' scheduling, the verification's sprint, the sessions' sprint, the `REL-08` and result tasks, the risk register and its fallbacks, the changelog and the `REL-07` block, the tag and its protection, the milestone close, the actual velocity, and the retrospective's carried actions.

`thin` when the plan is complete but the sprint would not steer: the goal is a list of the design artifacts, the planned velocity is a guess, the sessions sit in the sprint of the last session on paper only, the fallbacks restate the mitigation, or the retrospective records no cause.
`not yet adequate` when the plan and the record contradict each other: the sprint has no goal or no computed figure, `REL-07` tags a commit the record does not name, the milestone is closed with work still in it, or the actual velocity cannot be reconciled with the completed stories.

### Customer loop

Ask whether the design review changed the test, and whether the change reached the record, the plan, and the release.
Read the Week 6 action points and open questions with their outcomes, the script's first commit against the meeting date, the design shown on staging and the production instance shown with it, the permission answers, each decision's `DEC-nnn`, the action points' due weeks, the rework's pull requests, the artifacts they changed, and the testing-plan rows that ran or moved.

`thin` when the decisions are shared rather than specific, when no decision changes the record or the run plan, when the script was written after the meeting, when the rework is merged but the plan still lists it as an action point, or when a row moved with a reason that names no consequence.
`not yet adequate` when the meeting did not show the design or the deployed product, when the recorded decisions cannot be traced to any change, or when the release names a commit the rework never reached.

### Publication

Ask whether a reader who trusts the public record could find the design, follow the evidence, and see what the team did without the raw data.
Read the report's summary and `## Usability test` section, the 21 coverage rows, the private repository link and its exclusion, the recordings folder's naming, the test record and its links, the `QR/QRT` row, the `REL-07` record, the retrospective, `ai-usage.md` and its coverage row, the PDF's permalink and private-only items, and the contribution table.

`thin` when the record is complete but the reader still has to ask: the summary restates the record instead of linking it, a coverage row links an index page rather than the artifact, the private repository link is excluded with no reason, the report claims the test is ready while the record's verification is missing, or the AI usage file names a tool the repository never shows.
`not yet adequate` when the public record contradicts the repository or the PDF: the permalink names a different commit, the report the snapshot merges is not the one the PDF links, a private-only value or a participant identity is in the repository, the coverage table omits a deliverable, or the release and the report disagree about what is released.

### Guardrails

- Ground every claim in an artifact you verified at the saved SHA or a live URL; the compliance report is a map, not evidence.
- Verify the claims your judgement depends on, not every report claim, and do not re-audit the segments.
- Prefer `evidence.sqlite` and the saved dumps; issue, tag, and milestone facts are live, so at most three live `gh` lookups for this file, and record each one.
- Judge the private home and the recordings folder from the record, the report, and the PDF; they need authentication, so a failed single access check is not a semantic finding.
- Write `work/<team_dir>/semantic-claims.json` and mark each claim `supported`, `contradicted`, or `unverifiable`; only supported claims feed the semantic file.
- Do not copy an address, a credential, a participant identity, a recording link, a real name, or an email address from the PDF into the semantic file.
- Do not use status vocabulary (`met`, `partial`, `missing`, `unverified`), a grade, a score, a rank, or a cross-team comparison.
- Do not repeat the `## Main issues to fix` list; say what the artifact can and cannot do yet, and what breaks first.
- A `partial` or `missing` segment does not make its dimension `not yet adequate` by itself; judge the artifact, not the count.
- If a judgement contradicts a status, record the conflict in the ledger and return it; the status wins until the operator regrades the report.
  Never edit the report to fit the judgement, and never soften the judgement to fit the status.
- Omit a dimension only when all of its segments are `unverified`; keep at least three.
  If fewer than three dimensions remain, do not write the file.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A7/submissions/`.
   A directory that holds no PDF and no Markdown wrapper is a non-submission, not a rubric shortfall: do not launch a compliance agent for it, and report it to the operator.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-07/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A7 "<team_dir>"
   ```

   The fetcher writes `itpd-assignments-feedback/A7/work/<team_dir>/pdf-info.json` with the repository, the permalink, the SHA, the page count, the member tokens, the recording link, and the permalink-week check, and fetches the snapshot into `itpd-assignments-feedback/A7/work/<team_dir>/snapshot/`.
   It reads the PDF's links from its annotations as well as its text, so a permalink shown only as a hyperlink is still found; a bare 40-character SHA is resolved with `gh search commits` and adopted only when one repository matches.
   The primary index is `reports/week-07/README.md`; a permalink to another week's report records `permalink_week_mismatch`, and the fetcher prints a `warn:` line, repeats it in `work/<team_dir>/summary.md`, skips the commit check and the snapshot fetch, and exits 1 with a rerun command.
   Do not grade the wrong-week target; the wrong week is the S18 shortfall, and the operator supplies the right permalink with `uv run python scripts/fetch_team_snapshot.py A7 "<team_dir>" --permalink <url>`, recorded as `permalink_source=operator`, so the snapshot fetched from that permalink governs every file check.
   When the PDF carries no usable permalink, the fetcher stops and names the command; ask the operator for the permalink rather than guessing one, and do not invent a snapshot.
3. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S18 shortfall.
   Call the first value `SNAPSHOT_TIME`, and record the snapshot commit time against the deadline in `**Evidence:**`; it never changes a status.
4. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A7 "<team_dir>" --issue-fields [--issues <n> ...] [--paths <path> ...] [--timelines [<n> ...]]`, which reads `itpd-assignments-feedback/A7/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, `issue-fields.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   A bare `--timelines` collects every issue's timeline at one paginated request per issue; name the issues when only a few need it, and let `--issues` cover the rest.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB.
   `--summary` rebuilds the digest from the saved dumps without calling `gh`.
   The issue fields are their own mode, written by `--issue-fields`; it is not combined with `--summary`, `--issues`, or `--paths`.
   The raw fallback commands are:

   ```sh
   gh label list --repo "$REPO" --limit 200 --json name,description
   gh issue list --repo "$REPO" --state all --limit 1000 \
     --json number,title,labels,state,stateReason,createdAt,closedAt,body,url,author,type,closedByPullRequestsReferences
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,title,author,headRefName,baseRefName,state,createdAt,mergedAt,closedAt,body,closingIssuesReferences,reviews,files,url
   gh run list --repo "$REPO" --branch main --limit 100 \
     --json databaseId,workflowName,headSha,event,status,conclusion,createdAt,url
   gh api "repos/$REPO/actions/runs?head_sha=$SHA" \
     --jq '.workflow_runs[] | [.name, .event, .conclusion, .html_url] | @tsv'
   ```

   For each story and task issue a check needs, read its comments, its timeline of label, rename, milestone, and close events, and its body edit history:

   ```sh
   gh api "repos/$REPO/issues/<n>/comments" --paginate
   gh api "repos/$REPO/issues/<n>/timeline" --paginate
   gh api graphql -F owner='<org>' -F name='<repo>' -F n=<n> -f query='
     query($owner: String!, $name: String!, $n: Int!) {
       repository(owner: $owner, name: $name) {
         issue(number: $n) {
           milestone { title dueOn }
           assignees(first: 10) { nodes { login } }
           lastEditedAt
           userContentEdits(first: 100) { nodes { editedAt diff } }
         }
       }
     }'
   ```

   The REST `body` stays in `issues.json`, and the GraphQL fields add the milestone, the assignees, and the edit history beside it.
   For the history of a repository path and the pull request behind each commit:

   ```sh
   gh api "repos/$REPO/commits?sha=$SHA&path=<path>&per_page=100" \
     --jq '.[] | [.sha, .commit.committer.date, (.commit.message | split("\n")[0])] | @tsv'
   gh api "repos/$REPO/commits/<commit>/pulls" --jq '.[] | [.number, .title, .merged_at] | @tsv'
   gh pr diff <n> --repo "$REPO"
   ```

5. Judge every issue as of `ISSUE_CUTOFF`, `2026-11-15T23:59:59+03:00`, for every team:

   - Count only issues whose `createdAt` is at or before `ISSUE_CUTOFF`.
     An issue opened after `SNAPSHOT_TIME` but by `ISSUE_CUTOFF` counts like any other, and an issue opened after the cutoff is not judged.
   - Take an issue's labels at `ISSUE_CUTOFF` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `ISSUE_CUTOFF` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - Take its milestone from the `milestoned` and `demilestoned` events when the issue has them, and its current milestone otherwise, noting in `**Evidence:**` which was read.
   - The `issue_state_at_cutoff` view in `evidence.sqlite` answers the label set, milestone, and close or reopen state at the cutoff for every collected timeline in one query; `issue_events` answers when the question needs the events themselves or a time other than the cutoff, such as the planning time for S1.
   - A comment or edit made after `ISSUE_CUTOFF` is a caveat, never a shortfall.
   - Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`.
   - Set `Evidence gaps: yes` only when the state at `ISSUE_CUTOFF` cannot be read and the difference could change the status.
   - Pull requests, Actions runs, repository files, tags, releases, and milestones stay judged as of `ISSUE_CUTOFF`, and the snapshot stays the evidence for files.
6. Identify the Week 7 pull requests: every pull request created on or after Friday 6 November 2026, 00:00 Innopolis time, the start of Week 7 in `course/syllabus.md`, and by `ISSUE_CUTOFF`.
   A pull request merged at or before the team's Assignment 6 snapshot commit is part of the Week 6 submission, not a Week 7 pull request.
   Read that SHA from the saved A6 feedback report's `Primary index reviewed` link at `itpd-assignments-feedback/A6/feedback/<team_dir>/agent-compliance-feedback.md`, or from the A6 submission PDF.
   When neither is available, use the team's A6 cutoff as the boundary, `2026-11-08T23:59:59+03:00`, and say in `**Evidence:**` which boundary was used.
   The in-scope pull requests for the design review, the rework, the release, and the report's evidence run from the start of Week 7 to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.
7. Gather the pull-request facts below as evidence. These are Week 1 and Week 2 mechanics and are not re-graded in Assignment 7, except where a criterion names them: S2's task-issue shape, S15's rework, and S18's repository-evidence pull request. Record an anomaly in `**Evidence:**` only; never make it a shortfall in S18 or S2 unless a criterion names it.

   ```sh
   gh pr list --repo "$REPO" --state all --limit 500 \
     --json number,headRefName,author,state,mergedAt,closingIssuesReferences,reviews,milestone \
     --jq '.[] | {n: .number, branch: .headRefName, author: .author.login, state, merged: .mergedAt,
                  closes: [.closingIssuesReferences[].number],
                  approvers: [.reviews[] | select(.state == "APPROVED") | .author.login] | unique,
                  milestone: .milestone.title}'
   ```

   - `closes` has exactly one number, and that issue carries the `Task` issue type.
   - `branch` matches `^<that number>-[a-z0-9]+(-[a-z0-9]+)*$`.
   - A merged pull request has an approver other than its author, its task's body has every criterion ticked as `- [x] AC-nn:`, and the task's `stateReason` is `COMPLETED`.
   - A pull request closed without merging left its task `NOT_PLANNED` with a comment that gives the reason and links the pull request.
8. Read the new stories and the refined backlog from the issue dumps at `ISSUE_CUTOFF`:

   ```sh
   jq -r '.[] | [.number, (.type // "-"), (.milestone // "-"),
                   ((.field_values // []) | map(select(.name == "MoSCoW") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Story Points") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Responsible") | .value) | join(",")),
                   ((.field_values // []) | map(select(.name == "Accountable") | .value) | join(",")),
                   ((.assignees // []) | join(","))]
                  | @tsv' "{TEAM_WORK}/issue-fields.json" | head -n 60
   jq -r '.[] | select(.number == <n>) | .body' "{TEAM_WORK}/issues.json" | head -n 40
   ```

   - The first projection answers the type, the milestone, the four field values, and the assignees for the issues in the page it prints; narrow it with `select(...)` when the list is long.
   - The body projection answers the criteria and the `### Requirements`; read it for each design task and each refined story, and use `issues/<n>.edits.json` when the body changed at the cutoff.
   - The stories and tasks opened on or after `2026-11-06T00:00:00+03:00` are the week's; the open stories and tasks in no milestone are the product backlog, and the ones the team places in `SPRINT-08` and `SPRINT-09` are the ones refinement must have made ready.
   - Every `FR-nnn` and `ADR-nnn` a task's `### Requirements` names must resolve in the snapshot, and a task that serves none says `None: repository upkeep`.
9. Read the usability test's public record and its artifacts at the snapshot:

   ```sh
   find "{TEAM_WORK}/snapshot/docs/usability-tests" -maxdepth 3 -type f | sort
   uv run python scripts/check_snapshot_links.py "{TEAM_WORK}/snapshot" --issue-bodies "{TEAM_WORK}/issues.json"
   ```

   - The file list answers the index, the record, the surveys, the consent, the session template, the results stub, and the images; read the index and the record in full, and each other file as its segment needs it.
   - The link check answers the report's links and anchors and the record's internal anchors; a broken link is the shortfall of the segment that owns the file, and the report's own links are S18's.
   - Check the record's section order against S3, the task count and wording against S5, the protocol steps against S7, the instruments against S4, the measures and instrumentation against S6, the analysis plan and templates against S11, and the private-home claims against S8.
   - The private repository link is excluded from the link check; confirm the exclusion in `lychee.toml` and its reason, and do not fetch the private link.
10. Check the test's instrumentation against the analytics page and the code:

    ```sh
    rg -n "usability-test|participant_code|source" "{TEAM_WORK}/snapshot/docs/analytics.md" | head -n 40
    rg -n "\"source\"|'source'|participant_code" "{TEAM_WORK}/snapshot" -g '!**/node_modules/**' | head -n 40
    ```

    - The first projection answers the event table's `source` rule and the `participant_code` field; read the test's new events' rows in the table.
    - The second projection answers whether the events the record names exist in the code and carry the source; a record that names an event the snapshot does not emit is S6's shortfall.
    - The test's instrumentation must run on staging or a test-only path, never production; read the environment configuration and `docs/deployment.md` when the code does not settle it.
    - The verification run is the team's own staging run before the first counted session; a verification that no artifact records is S6's shortfall, and a verification the record dates after the first session is the same.
11. Check the usability quality requirement and the testing plan together:

    ```sh
    rg -n "^## QR-|^\*\*Characteristic:\*\*|^\*\*Sub-characteristic:\*\*|^\*\*Business importance:\*\*|^\*\*Technical risk:\*\*|^## QRT-|^\*\*Level:\*\*|^\*\*Status:\*\*|^\*\*Runs at:\*\*|^\*\*Why Manual:\*\*|^\*\*Pass when:\*\*|^### Procedure" "{TEAM_WORK}/snapshot/docs/quality-requirements" | head -n 80
    rg -n "^## Quality Requirement Testing Plan|^\| .*QRT-|^\| .*QR-" "{TEAM_WORK}/snapshot/docs/project-plan.md" | head -n 40
    ```

    - The first projection answers which requirement is the Week 7 one and its test's level, status, what runs it, and its pass criterion; read the new requirement's file in full.
    - The second projection answers the testing-plan row's columns and the row's `Planned for sprint`; read the table in full when the row's evidence or linkage matters.
    - The new requirement is the one with `Interaction Capability` and one of the three sub-characteristics; the `QRT-01` that names `UT-01` is its test, and the testing-plan row is built from that test and no other.
    - `**Checked QRs:**` in S16 is built from the `Checked` cells and from nothing else.
12. Check the release against the tag:
    - Read `releases.json` for the tag names and dates; read the release title and body from the rendered release page or the raw `gh api "repos/$REPO/releases?per_page=100"` response, because the collector's dump omits them; read `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-07` block, and `reports/week-07/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path.
    - Compare the merge time of those three pull requests with the tag; each must be later than, or at, the tag, and the changelog's dated section, the plan's block, and the report must be merged in that order. Use the tag's push time when it can be read; otherwise use the tag's commit date and say so in `**Evidence:**`.
    - Read `gh api "repos/$REPO/rulesets"` and each tag ruleset for the protection that covers tag pushes.
    - Build `**Checked QRs:**` from the testing plan's `Checked` cells: a requirement belongs when at least one of its tests has `SPRINT-07` there, whatever the row's `Status`.
13. Check the sprint close from the issue dumps and the plan:
    - From `issues.json`, take the stories closed as completed at `ISSUE_CUTOFF` in `SPRINT-07`'s milestone and their `Story Points` from `issue-fields.json`; add them by hand and compare the total with `**Actual Velocity:**`.
    - Read `reports/week-07/sprint-retrospective.md`'s four sections, their columns, and their row counts, and check each `## Carried Actions` row against `reports/week-06/sprint-retrospective.md`'s `Carried: Yes` actions.
    - Confirm every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.
14. Check the design review against the record and the plan:
    - Read `reports/week-07/meeting-script.md`, `meeting-report.md`, and `meeting-transcript.md` at the snapshot, and the `DEC-nnn` entries the report cites.
    - Compare the meeting date with the Week 7 window and the cutoff; a meeting on 13 to 15 November is a caveat, not a shortfall, and a meeting after the cutoff is a shortfall.
    - Find the script's first commit and the report's, and compare them with the meeting date; a script written after the meeting is S14's shortfall.
    - Read the report's action points' due weeks: at least two due after Week 7, at least one in Week 8; an action due inside Week 7 is a shortfall.
    - Read the Week 6 report's action points and open questions, and the Week 7 report's `## Previous action points` and `## Previous open questions`, for S13.
15. Check the private usability-data repository's declaration against the PDF:

    ```console
    gh repo view "<organization>/<repo>-usability-data" --json isPrivate,visibility 2>&1 | head -n 5
    ```

    - The call answers whether the repository exists and is private when the agent has access; when it fails, judge the declaration in the record, the report, and the PDF, and record the unverifiable access as an evidence gap for that check only.
    - The PDF's items 4, 5, 6, 7, and 8 carry the private repository and the recordings folder's links and access, the staging and production addresses, the staging telemetry credentials, the recording link, and the transcript; read them once here and in S18, and never copy a value into feedback.
16. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A7 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A7/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/usability-tests/ut-01/README.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    Its rules do not include participant identity or IPv4 addresses, so check the public usability files for a participant name or a raw note, and check the staging and production addresses separately against the PDF's entries; report a hit by path and kind.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in the submission and outside the meeting artifacts, `.env` files, and the addresses and credentials from the PDF searched over the snapshot.
    Report each finding by path and kind only, with the number of hits per file.
17. Grade each of the 19 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-07/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the private usability-data repository's link and access, the recordings folder's link and access, the staging and production addresses with the network note, the staging analytics and observability addresses and credentials, the design review's recording link, and a transcript the customer refused to publish.
- Never copy a real name, an email address, a dashboard or backend address, a credential, or a participant identity from the PDF into feedback; refer to people by GitHub username, to the customer as `Customer`, to a participant by `P-nn`, and to an address or credential by the placeholder or by the kind of finding.
- The participant codes are public; the participant identity, the consent records, the raw notes, and the identity mapping are private and are never copied from the private repository or the PDF.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 to Week 6 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the research content, the vision, the assumptions, the issue forms and fields, the project's table view, the risk register's older risks, the threshold of success, the plan's Week 3 to Week 6 parts, the Definition of Done, `CONTRIBUTING.md`, `docs/setup.md`, the documentation site, the functional requirements, the architecture document, the ADR records, the glossary's older terms, the team's `AGENTS.md`, `REL-04` to `REL-06`, and the Week 1 to Week 6 meeting artifacts, reports, and retrospectives.
- Week 1 to Week 6 artifacts are checked only where Assignment 7 requires it: the plan's `### SPRINT-07` and `### SPRINT-08` (S1), the stories, task issues, and backlog refinement (S2), the Week 6 events and `docs/analytics.md` (S6), the quality requirements index and matrix and the testing plan (S9 and S15), `docs/glossary.md`'s older terms and `docs/risks.md`'s older risks (S12), the Week 6 meeting report's action points and open questions (S13), the Week 6 retrospective's `Carried: Yes` actions (S17), `CHANGELOG.md`'s released section and `[Unreleased]` (S16), the link check and the Markdown check, `actionlint`, and the product-code CI green on `main` (S18), and the `SPRINT-07` milestone and the issues in it (S2, S16, and S17).
- When a Week 6 artifact Assignment 7 builds on is absent, such as a Week 6 meeting report with no action points, a Week 6 retrospective with no file, or a quality requirements directory with no active requirement, judge the Assignment 7 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 6 absence again.
- A Week 6 report with no action point due in Week 7 or no open question makes `None` in the matching `## Previous` section correct, and it is never a shortfall.
- The Week 6 deadline does not move Week 7: the A6 cutoff `2026-11-08T23:59:59+03:00` bounds the Week 6 submission only, and the Week 7 cutoff stays `2026-11-15T23:59:59+03:00` for every team.
- The Week 7 Sunday deadline is the submission's date, not the sprint's class-week end: `SPRINT-07`'s `**Due:**` and its GitHub milestone are `2026-11-15`, while the class week ends on 12 November.
- Week 7 claims no usability result: the sessions may have run, and their notes, results, findings, triage, and `QR/QRT` verdict are Week 8's, so their absence is never a shortfall and their presence is not a Week 7 result.
- Week 8's configuration management and usability results, Week 9's pitch deck, and the Week 10 presentation are not Assignment 7 deliverables, and their absence is never a shortfall.
- The usability test's participants are not the customer, the instructors, the course staff, or the team; the customer validates the design in the review and is never a participant.
- The private usability-data repository and the recordings folder are outside the product repository; their absence from it is correct, and the product repository links the private repository and names the recordings folder without linking it.
- A commit, comment, tag, deploy, or edit after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff; it is a shortfall only where a criterion names the cutoff, such as S16's tag date.
- The product code, its tests, the staging deployment, and the environments are Week 5 deliverables: their absence is never excused as "not this week's" where the test's instrumentation and environment need them.
- Week 7 has no pitch deck, no experiment, and no user-facing change: the design, the private home, the review, and `REL-07` are the week's work, and the absence of a deck or an experiment is never a shortfall.
- A design review the customer attended in writing instead of live is a declared deviation, and its written exchange is its transcript; it is never a shortfall by itself.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- A submission after the deadline is the instructor's late-penalty question, not this rubric's; read the snapshot's commit time against the deadline in `**Evidence:**` only.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, usability test, usability test task, usability test record, participant, participant profile, usability session, usability finding, consent, recording, `SUS`, `SEQ`, private usability-data repository, recordings folder, measure, metric, statistic, instrument, instrumentation, sprint, sprint planning, product backlog, product backlog refinement, sprint backlog, sprint review, sprint milestone, plan milestone, story points, velocity, retrospective, quality requirement, quality requirements index, quality requirement test, quality requirement testing plan, evidence, staging environment, production environment, university VM, university network, deployment runbook, glossary, risk register, functional requirement, architectural decision record, release, changelog, weekly report, weekly public report, private-only artifact, deviation, event, `SLI`, dashboard, and telemetry.

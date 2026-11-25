# Assignment 8 Grading Criteria

This rubric is for the compliance agent that reviews ITPD Assignment 8 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/compliance-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grading-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 8 and does not repeat those rules.

Week 8 is the run week, and the whole assignment runs around two streams.
The first stream is the `UT-01` usability test: the sessions have run or run this week, their sanitized notes and results are written, the findings are triaged, the verdict is recorded, and the fixes reach the product backlog.
The second stream is the configuration review: the team writes the maintained configuration plan and judges the configuration by the goals its artifacts serve.
The sprint still runs around both, so the plan, the Sprint Review, `REL-08`, the retrospective, and the Week 9 handoff are judged as the week's ordinary sprint work.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `753d81e9c8b7b78261674c8d4836ef4e4b01d583`.
If the checked-out submodule differs from that commit, read each file with `git -C A8/itpd show 753d81e9c8b7b78261674c8d4836ef4e4b01d583:<path>`.

- `A8/itpd/assignments/assignment-8.md` — the student-facing brief: Parts 1–13, What Good Looks Like, the repository report contents, the Moodle report contents, the submission procedure, and the checklist.
- `A8/itpd/requirements/usability-testing-requirements.md` — the test record, the participants, the tasks, the protocol, the instruments, the instrumentation, the analysis, the consent, the private data repository, the public evidence, the Week 8 results and findings, the triage, and the Week 8 execution.
- `A8/itpd/requirements/configuration-management-requirements.md` — the plan and the review: where both live, the five item groups, the `CFG-nn` fields, the connections, the goal-based evaluation, the recommendation, and the public review.
- `A8/itpd/requirements/weekly-report-requirements.md` — the run-week and review-week weekly public report, the AI usage report, declaring deviations, and the Moodle PDF.
- `A8/itpd/requirements/quality-requirements-requirements.md` — the `QR-nn` file, the `QRT-nn` test and its levels, the manual test whose `**Runs at:**` names a `UT-nn`, and the interaction-capability rule that makes it the expected manual test.
- `A8/itpd/requirements/planning-requirements.md` — `docs/project-plan.md` with `## Sprints` and `## Quality Requirement Testing Plan`; the `**Due:**`, `**Sprint Backlog:**`, `**Planned Velocity:**`, and `**Actual Velocity:**` fields; the `#### REL-08` block with `**Released:**` and `**Checked QRs:**`; and the threshold of success.
- `A8/itpd/requirements/sprint-ceremonies-requirements.md` — sprint planning, product backlog refinement, estimation, the Sprint Review, and the retrospective with its four sections, row counts, and columns.
- `A8/itpd/requirements/customer-meetings-requirements.md` — the weekly meeting as the Sprint Review, the run week's showing rules, the permission questions, the script, the report's `## Previous action points` and `## Previous open questions`, and the transcript.
- `A8/itpd/requirements/releases-requirements.md` — `CHANGELOG.md`, Semantic Versioning, tags and their protection, the release title, and the upgrade note that ends with the `Full changelog` line.
- `A8/itpd/requirements/repository-requirements.md` — the link check and its exclusions, the environments and the university VM, the configuration and sensitive information, the sensitive-data incident response, and the private usability-data repository.
- `A8/itpd/requirements/task-issues-requirements.md` — the `Task` issue type, its `### Requirements` section, its acceptance criteria, and the pull request that closes it.
- `A8/itpd/requirements/issue-tracking-requirements.md` — scheduling as the sprint's GitHub milestone, the `Responsible` and `Accountable` fields, the `Priority` field, and the matching assignees.
- `A8/itpd/requirements/risks-requirements.md` — `docs/risks.md`, a risk's fields, its ratings, and its response and contingency.
- `A8/itpd/requirements/glossary-requirements.md` — `docs/glossary.md`, the term's heading, and its one-sentence definition.
- `A8/itpd/requirements/general-requirements.md` — artifact and measurement terms, the `reports/week-NN/` versus `docs/` split, the identifier rules including `CFG-nn` and the finding citation, and traceability into Week 9.
- `A8/itpd/requirements/agent-instructions-requirements.md` — the team's root `AGENTS.md`, read as an AI trace, and the Week 8 rule that it links `docs/configuration-plan.md`.
- `A8/itpd/guides/configuration-management.md` — the method for the baseline, the inventory, the connections, the goals, the tradeoffs, and the sanitized publication.
- `A8/itpd/guides/usability-testing.md` — the method for the sessions, the results, and the triage.
- `A8/itpd/course/syllabus.md` — the Week 8 objectives and deliverables, the Saturday 21 November deadline, and the Week 9 deadline.
- `A8/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the deadline policy.

Apply every rule marked `**Since: W1**` through `**Since: W8**`.
No rule in the pinned materials carries a `**Since: W9**` marker, so nothing is excluded by a later marker; the Week 9 pitch deck, the final reflection, and the final repository state are not Assignment 8 deliverables, and their absence is never a shortfall except where the Week 9 handoff names them.

## Assignment parameters

- Report title: `# Assignment 8 Compliance Feedback`
- Week: `W8`
- Course materials: `A8/itpd` at `753d81e9c8b7b78261674c8d4836ef4e4b01d583`
- Primary index artifact: `reports/week-08/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-8.md`.
- Week window: from Friday 13 November 2026, 00:00 Innopolis time, `2026-11-13T00:00:00+03:00`.
  The syllabus gives the Week 8 class week as 13 to 19 November 2026; the submission is due on Saturday 21 November, and the window runs from that Friday to `ISSUE_CUTOFF`.
- Soft deadline: none; `course/rules.md` gives every group submission from Week 4 to Week 9 a single hard deadline, and `course/syllabus.md` and `assignments/assignment-8.md` state the same date.
- Hard deadline: Saturday 21 November 2026, 23:59, as the pinned `course/syllabus.md`, `course/rules.md`, and `assignments/assignment-8.md` state it.
  Week 8 is the ordinary Saturday deadline: the syllabus' two exceptions are Week 6 and Week 7, so no Sunday prose and no per-team override applies.
- No per-team deadline override exists for Week 8: every team's deadline is Saturday 21 November 2026, 23:59.
- `ISSUE_CUTOFF`: `2026-11-21T23:59:59+03:00` for every team.
  Every later reference to `ISSUE_CUTOFF` means that cutoff, and `**Evidence:**` states the cutoff used.
- Hard deadline of the following week: Saturday 28 November 2026, 23:59, the deadline the Week 9 syllabus block gives and the due date `SPRINT-09`'s GitHub milestone carries.
  An action point due in Week 9 carries a date from 20 November through 28 November 2026, the Week 9 class week plus the submission deadline.
- The time zone is not stated in the materials; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A8/submissions/<team_dir>/`; the Moodle export carries no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A8/work/<team_dir>/snapshot/`.
- Live artifact families: the story and task issues with their types, field values, comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the link check, the Markdown check, `actionlint`, and the product code; the repository's tags and releases; the sprint GitHub milestones; the Sprint Review's Moodle recording link; and the private usability-data repository and the recordings folder, read only through the public record, the Moodle PDF, and the record's own claims because they need authentication.
- Story and task issues, their types, their field values, their milestones, and the labels are not in the snapshot, so they are read live and judged as of `ISSUE_CUTOFF`, per [procedure step 5](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by `ISSUE_CUTOFF` counts.
- Tags, releases, and milestones are read live and judged as of `ISSUE_CUTOFF` too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after `ISSUE_CUTOFF`, and say so in `**Evidence:**` when the timeline cannot settle it.
- The private usability-data repository, the recordings folder, the test's filtered telemetry export, and the Sprint Review's recording are private or Moodle-only.
  Judge them from the test record, the results, the week report, and the Moodle PDF's links and access instructions; make the single access check of `docs/grading-policy.md#consumer-hosted-media` only when the agent has the access to reach them, and treat an unverifiable access claim as an evidence gap for that check, not as a shortfall.

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

| Segment | Covers |
|---------|--------|
| S1: Sprint plan and milestones | Part 1 items 2–3; the Sprint plan part of the coverage row Sprint plan; the plan's `### SPRINT-08` goal, `**Due:**`, `**Sprint Backlog:**`, and `**Planned Velocity:**`, and `### SPRINT-09`'s provisional goal, `**Due:**`, and backlog link; the checklist items "`SPRINT-08` planned with its goal, its `**Due:**` field, its `**Sprint Backlog:**` link, and its `**Planned Velocity:**`" and "`SPRINT-09` given its provisional goal and its `**Due:**` of `2026-11-28`" |
| S2: Backlog refinement and task scheduling | Part 1 items 1, 4, 5, and 6; the story and task-issue part of the coverage row Sprint plan; the checklist items "The results and configuration tasks scheduled in `SPRINT-08`", "The `UT-01` record's `**Run sprint:**` set, including which sessions ran in which sprint when they straddle", and "Each task issue carrying its `### Requirements`, its criteria, its `**Responsible:**`, its `**Accountable:**`, and its assignees"; the refined next two sprints' worth of the product backlog |
| S3: UT-01 run and sanitized sessions | Part 2; the Sanitized session notes coverage row; the checklist items "At least three counted sessions run, with five as the design target, at the dates the team scheduled", "Each session run in person on the university network against staging, with the seed reset before each, and the instrumentation verified before the first counted one", and the session-note and private-data part of "The raw text and the telemetry export in the private repository, the recordings in the cloud folder, and the sanitized `sessions/P-nn.md` notes written on the day with no identity" |
| S4: Results and conclusion | Part 3; the Usability results coverage row; the checklist items "`results.md` with the per-participant table, the aggregate completion, the medians, the SUS with `n=<count>`, every measure the plan named, the thematic analysis, the instrumentation comparison, the limitations, and the conclusion, or the qualitative record without aggregates" except its instrumentation comparison, "The conclusion answering each research question and naming the product response, with the changes the team commits to and declines", and "The `UT-01` record's `**Status:**` and the index updated" |
| S5: Instrumentation comparison | Part 3 item 3; the instrumentation-comparison part of the `results.md` checklist item in Part 3 |
| S6: Findings | Part 4 and Part 5 item 4's `**Task issue:**` field; the findings part of the coverage row Findings and their issues; the checklist item "One numbered section per finding (`### Finding 1`, `### Finding 2`, and so on), each with its severity, its task as `UT-01 Task 1` and participant codes, evidence, recommendation, and task issue, cited by its own anchor, and sanitized" |
| S7: Triage and planned fixes | Part 5; the task-issue part of the coverage row Findings and their issues; the checklist items "Every finding triaged, and a significant finding carried by a task issue scheduled in `SPRINT-08`" and "The fixes planned, with a landed one in `REL-08` and a later one moved to `SPRINT-09` with its reason declared" |
| S8: QR/QRT verdict and threshold | Part 6; the verdict part of the coverage row `QR-nn` and its test; the goal-settlement part of the coverage row Threshold review; the checklist items "The `QR/QRT` row recorded as `Passes` or `Fails` with `Checked: SPRINT-08` and the results as evidence, or `Not verified` or moved to `SPRINT-09` with a reason" and "The threshold's usability goal settled when the team has one" |
| S9: Configuration plan | Part 7; the plan part of the coverage row Configuration management; the checklist items "`docs/configuration-plan.md` with its `**Reviewed:**` date and its five groups", "At least 8 `Active` `CFG-nn` items with at least one in each group, each with its `**Status:**`, `**Type:**`, `**Purpose:**`, `**Owner:**`, `**Where:**`, `**Connections:**`, and `**What good looks like:**`", and "A dropped item in place, the plan in the team's `AGENTS.md`, and a missing configuration named in words" |
| S10: Goal-based configuration evaluation | Part 8; the evaluation part of the coverage row Configuration management; the checklist items "`reports/week-08/cm-evaluation.md` with its `**Baseline:**`, its `**Reviewed:**`, its `## Method`, one section per local goal with `**Today:**`, `**A more convenient way:**`, `**Why:**`, and `**Tradeoffs:**`, its `## What We Could Not Judge` note, and its `## The First Change` paragraph" and "The evaluation is goal-first and local, names the mechanism and the tradeoffs, and is public and sanitized" |
| S11: Glossary and risk register | Part 9; the Glossary and Risk register coverage rows; the checklist items "The configuration terms in `docs/glossary.md`" and "The four configuration risks in `docs/risks.md`, each starting `**Status:** Open`, with the fallback as its `**Contingency:**`" |
| S12: Week 7 action points and open questions | Part 10 items 1–2; the Week 7 action points and Week 7 open questions coverage rows; the checklist items "Each Week 7 action point's outcome in `## Previous action points`" and "Each Week 7 open question put to the customer or closed" |
| S13: Sprint Review | Part 10 items 3–6; the Sprint Review, Meeting script, and Meeting transcript coverage rows; the checklist items "`reports/week-08/meeting-script.md` with the permission questions first and the read-back last" and "`reports/week-08/meeting-report.md` with the Sprint Review's feedback, a `DEC-nnn` for any decision, two action points after Week 8 with at least one due in Week 9, and the transcript or its reason" |
| S14: Review rework and testing-plan rows | Part 11 items 1–3; the checklist items "The Sprint Review's decisions applied" and "Each `SPRINT-08` testing-plan row run or moved with a reason, and the testing plan updated" |
| S15: REL-08 release | Part 11 items 4–8; the `REL-08` coverage row; the checklist items "`REL-08` tagged on the release commit and its tag protected, with the changelog's released section, the upgrade note, and the plan's `REL-08` block with `Released` and `Checked QRs`" and "The `SPRINT-08` milestone closed, and the configuration plan's `**Reviewed:**` advanced if it was reviewed again" |
| S16: Sprint close and retrospective | Part 12; the Sprint retrospective coverage row and the actual-velocity part of the Sprint plan row; the checklist items "`**Actual Velocity:**` set in `### SPRINT-08`" and "`reports/week-08/sprint-retrospective.md` with its four sections, its carried actions, and any `Not done` action re-listed with `Carried: Yes`" |
| S17: Week report and submission | Assignment Report In The Repository items 1–9; Assignment Report On Moodle items 1–9; the Submission Procedure; the 18 coverage rows judged only as rows that exist and link; the checklist items "`reports/week-08/README.md` with the summary, the `## Usability test` and `## Configuration management` sections, the `## Week 9 handoff`, the coverage rows, and the `## Privacy` line", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready with the permalink, the private repository and recordings folder links and access, the staging and production addresses, the staging analytics and observability credentials, and no participant identity" |
| S18: AI usage and Week 9 handoff | Part 13; the AI usage coverage row; the checklist items "`reports/week-08/ai-usage.md`, including whether an agent was given the sanitized results and whether it was given the configuration plan" and "The Week 9 handoff written"; the handoff artifacts the report names |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S17.
S8 owns the testing plan's verdict and the threshold goal's fields; S17 owns the report's `## Threshold review` section and its row.
S9 owns the configuration plan and S10 the evaluation; S17 owns the report's `## Configuration management` section and the Configuration management row, and neither artifact gets a row of its own beyond that link.
S12 owns the Week 7 outcomes, and S13 owns the Week 8 review.
S15 owns the tag, its protection, the release body, the changelog, the plan's block, and the milestone close; S17 owns the report and the PDF.
S18 owns the handoff's artifact list, and S17 owns the report's `## Week 9 handoff` section; a Week 9 artifact that does not exist yet is never a shortfall.

## Status guide

Use the status vocabulary of `docs/compliance-feedback-format.md` and the evidence states of `docs/grading-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S15 when the tags and releases cannot be read at all, or S3 when the sessions cannot be reached and neither the record nor the report settles whether they ran.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Sprint plan and milestones

**Check:**

- `docs/project-plan.md`'s `### SPRINT-08` and `### SPRINT-09` sections in the snapshot.
- `milestones.json` and the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` for `SPRINT-08` and `SPRINT-09`, their due dates, their states, and the issues in each.
- `issue-fields.json` for the `Story Points` of the product stories scheduled in `SPRINT-08`.
- `reports/week-07/README.md` and the plan's provisional `SPRINT-08` goal, for the target the week inherits.

**met:**

- `### SPRINT-08` carries the sprint's real goal in one sentence, not the provisional goal the plan carried until now, and the goal is a result rather than a list of tasks.
- `### SPRINT-08` carries `**Due:** 2026-11-21`, `**Sprint Backlog:**` linked to its own GitHub milestone, and `**Planned Velocity:**` set at planning.
- `**Planned Velocity:**` is a whole number computed by hand from the `Story Points` of the product stories scheduled in `SPRINT-08`'s milestone, and it equals their sum.
- The results, the configuration, and the other task work carry no points and are not counted in the planned velocity.
- A `SPRINT-08` that carries only tasks has a planned velocity of `0`, and its goal says what a task-only sprint is for.
- `### SPRINT-09` carries a provisional goal in one sentence naming the final repository state, the 7-minute deck, the reflection, and whatever else the team plans, so the last sprint has its target already.
- `### SPRINT-09` carries `**Due:** 2026-11-28`, and its `**Sprint Backlog:**` link appears once the sprint has issues.
- The GitHub milestones `SPRINT-08` and `SPRINT-09` exist with the due dates `2026-11-21` and `2026-11-28`, and the team links `SPRINT-09`'s existing milestone rather than creating a new one.
- The plan's figure and the scheduled stories agree: no product story counted in the planned velocity sits outside `SPRINT-08`'s milestone, and no product story inside it is left out of the figure.

**What does not count:**

- `### SPRINT-08` still carrying its provisional goal, a goal that is a task list, or a goal that names the sprint's artifacts instead of a result.
- A missing `**Due:**`, a due date other than `2026-11-21`, or a `**Sprint Backlog:**` link to an issue list, the GitHub project, or a milestone that is not the sprint's.
- A planned velocity copied from `SPRINT-07`, guessed, or computed from the results, configuration, or other task work.
- `**Planned Velocity:**` added after the sprint closed, or a figure that counts a story the sprint did not have at planning.
- A missing GitHub milestone, a due date that is not the syllabus deadline, or a scheduled product story that is absent from the milestone.
- `SPRINT-09` with a missing provisional goal or a missing `**Due:**` when the plan already names the sprint's deliverables.
- A new `SPRINT-09` milestone created instead of the existing one linked.

**partial:**

- `### SPRINT-08` carries a goal and its `**Due:**` and at least one other `met` criterion fails.
- Typical shortfalls: a provisional goal left in place; a missing backlog link; a planned velocity that does not equal the scheduled product stories; a task-only sprint with a figure; a wrong or missing milestone due date; `SPRINT-09` without its provisional goal or its link.

**missing:**

- `### SPRINT-08` is absent, or it carries neither its goal nor its `**Due:**`, or `docs/project-plan.md` is absent at the snapshot.

**Guardrails:**

- The plan's Week 3 to Week 7 parts — its milestones, its older sprints, and `REL-03` to `REL-07` — are not re-graded; this segment judges `SPRINT-08` and `SPRINT-09` and the sprint milestones' due dates.
- Velocity is computed by hand from the `Story Points` values, because a single-select field holds one option and cannot be added up.
- The planned velocity is the product stories selected at planning; when a story moves out during the sprint, the move is judged from the issues in S2 and the actual velocity in S16.
- The GitHub milestone's due date is the week's hard deadline; the milestone's close is S15's, and the issues in it are S2's and S15's.
- `SPRINT-08` is the run week's sprint and may carry only tasks, so a planned velocity of `0` is correct and is never a shortfall.
- `SPRINT-09`'s `**Sprint Backlog:**` appears only once the sprint has issues; its absence while the milestone is empty is correct.
- A plan edited after `ISSUE_CUTOFF` is a caveat in `**Evidence:**` and never repairs the state at the cutoff.

### S2 — Backlog refinement and task scheduling

**Check:**

- `issue-fields.json`, `issues.json`, and the saved timelines for the open story and task issues, their types, their milestones, their `Priority`, `Responsible`, and `Accountable` values, their assignees, and their `Story Points` and `MoSCoW` values.
- `docs/project-plan.md`'s `### SPRINT-08` and `### SPRINT-09`, and the sprint milestones the issues sit in.
- `docs/usability-tests/README.md` and the `UT-01` record's `**Run sprint:**`.
- `prs.json` for the Week 8 pull requests that closed the results, configuration, and fix task issues.

**met:**

- The next two sprints' worth of the product backlog, `SPRINT-08` and `SPRINT-09`, is refined: each item's scope is settled, its acceptance criteria are runnable, its `Story Points` is set, and it is at most `13SP`.
- Each refined item that is not yet scheduled sits in no sprint's GitHub milestone, with no `Responsible` value, no `Accountable` value, and no assignee, so it is ready to schedule and not yet scheduled.
- The week's task work is scheduled in `SPRINT-08`'s milestone: the sanitized session notes, the results, the findings, the triage, the `QR/QRT` verdict, the configuration plan, the configuration evaluation, the glossary and risk updates, the Sprint Review, and `REL-08`.
- The product backlog leaves `SPRINT-09`'s items unscheduled while they are refined, and the plan's `### SPRINT-09` backlog link appears only once the sprint has issues.
- The `UT-01` record's `**Run sprint:**` is `SPRINT-08`, or `SPRINT-07` when every counted session ran before the Week 7 deadline of 15 November 23:59.
- When the sessions straddle the two sprints, the record writes both sprint sections and states which sessions ran in which, and the index lists both.
- The index's `Sprints` cell lists the same design and run sprints as the record, each linked to its plan section.
- Every task issue carries its `### Requirements` section, at least one `AC-nn`, its `Priority`, its milestone, its `Responsible` and `Accountable` values, and the matching assignees.
- A configuration task says `None: repository upkeep` in `### Requirements`.
- A usability fix that changes behaviour names the story and the `AC-nn` it serves and names the `FR-nnn` or `ADR-nnn`.

**What does not count:**

- A story that sits in `SPRINT-08` or `SPRINT-09`'s milestone, or that carries `Responsible`, `Accountable`, or assignees, and is called refined: scheduling is what leaves the product backlog.
- A story with no `Story Points`, with a `Story Points` above `13`, or with acceptance criteria that are not runnable.
- A results or configuration task absent from `SPRINT-08`'s milestone, or `REL-08` planned outside `SPRINT-08`.
- A run sprint of `SPRINT-07` when a counted session ran in `SPRINT-08`, or a missing run sprint.
- A record that does not say which sessions ran in which when they straddle, or an index whose `Sprints` cell disagrees with the record.
- A task issue with no `### Requirements`, no acceptance criterion, no `Priority`, no milestone, no `Responsible` or `Accountable` value, or no assignee.
- A configuration task that names a requirement it does not advance, or a product task whose `### Requirements` says `None: repository upkeep`.
- A usability fix that changes behaviour and names no story, no `AC-nn`, or no `FR-nnn`/`ADR-nnn`.

**partial:**

- The task work is scheduled and the record's run sprint is set, and at least one other `met` criterion fails.
- Typical shortfalls: one refined item still carries a milestone or assignees; one task absent from `SPRINT-08`; the run sprint wrong or the straddle unstated; a task issue lacking a field or a criterion; a configuration task naming a requirement.

**missing:**

- No results or configuration task is scheduled in `SPRINT-08`, or neither the product backlog nor the task schedule can be read at the cutoff.

**Guardrails:**

- The schedule is read at `ISSUE_CUTOFF`; a task rescheduled after the cutoff is a caveat and never repairs the state at the cutoff.
- The week's task work need not be ten separate issues; a task may cover two artifacts the assignment names together, but each of the sanitized notes, the results, the findings, the triage, the verdict, the configuration plan, the evaluation, the glossary and risks, the review, and `REL-08` must be scheduled work.
- The run sprint is the sprint of the last counted session; a session that ran in Week 7 is not rescheduled, and a shortfall that keeps the results `Planned` does not change the sprint the sessions ran in.
- A story's `MoSCoW` is set when the story is written and its `Story Points` at refinement, per the Week 4 rules; a refined story that is ready carries both.
- The GitHub project's table view, the issue forms, and the label set are Week 2 to Week 4 mechanics and are not re-graded; this segment checks the scheduled task issues' shape where Assignment 8 requires it.
- A story larger than `13SP` is split before it is scheduled, so a `13SP` story is the largest scheduled story, and a larger one is a shortfall wherever it sits.
- The tasks may already have been scheduled in the Week 7 window; this segment judges the schedule at the cutoff, not the week the issue was written.

### S3 — UT-01 run and sanitized sessions

**Check:**

- `docs/usability-tests/ut-01/README.md`, `docs/usability-tests/ut-01/sessions/README.md`, and each `docs/usability-tests/ut-01/sessions/P-nn.md` in the snapshot.
- `docs/usability-tests/ut-01/surveys.md` and `docs/usability-tests/ut-01/consent.md` for the measures a note records and the consent a session counts on.
- `pdf-info.json`, `summary.md`, and the snapshot time for the window the sessions may run in.
- The private usability-data repository and recordings folder claims in the record and the Moodle PDF, and `gh repo view <organization>/<repo>-usability-data --json isPrivate,visibility` when the agent has access.
- `reports/week-08/README.md`'s `## Deviations` for a session that did not count.

**met:**

- At least three counted sessions ran, and five is the design target.
- Each counted session matches the participant profile, the participant is 18 or older and is not a teammate, the customer, the instructor, or the course staff, the durable consent covers the recording and the sanitized public results, and the recording exists.
- Each session ran at the date the team scheduled, in person, on the university network, against the staging deployment, with the seed reset to synthetic data before it, and made no real payment.
- The instrumentation was verified before the first counted session, not during it, and the verification is recorded.
- The raw text and the test's telemetry export are in the private usability-data repository and the recordings are in the team's cloud folder, placed there on the day of the session.
- The private repository is private with the team and the instructors as readers; the recordings folder is shared with the instructors; neither the recordings nor the raw notes are in the product repository.
- Each counted session has a sanitized `sessions/P-nn.md` note, headed `# P-01`, written on the day, carrying the participant's relation to the target user, the familiarity, the device, the task outcomes, the assistance, the times, the SEQ, the SUS, and the themes.
- A quote appears only when the consent covers it, and it names no person and no organization.
- The public record carries no name, email address, phone number, postal address, free-text identification, or raw recording, and no private link other than the private repository link.
- The participant codes are `P-01`, `P-02`, and so on, assigned in the order the sessions were arranged, with a replacement under the next free code and a withdrawn code retired and never reused.
- The number of counted sessions and the reason a session did not count are recorded, so S4 can declare a shortfall when fewer than three counted.
- A session whose consent, recording, or participant is compromised is not counted, and its data is removed.

**What does not count:**

- Fewer than three counted sessions presented as a full run with no record of the shortfall.
- A session counted that is off the profile, is a teammate, the customer, the instructor, or the course staff, has no durable consent, or has no recording.
- A session run online, off the university network, against production, with no seed reset, or that took a real payment.
- A session whose seed was not reset, or one that reused the previous session's data.
- Instrumentation verified during or after the first counted session, or a verification no artifact records.
- Raw text, a recording, a consent record, an identity mapping, or a private link other than the private repository link in the product repository; the recordings folder linked from a public file.
- A session note with a name, an email address, a phone number, an address, a quoted identity, or a raw recording.
- A session note missing the relation, the familiarity, the device, the outcomes, the assistance, the times, the SEQ, the SUS, or the themes.
- A quote published without consent, or a note that is a raw transcript instead of a sanitized summary.
- Participant codes reused, assigned out of order, or a withdrawn code reused.
- A session counted whose data was later removed, or a session with no note.

**partial:**

- The sessions ran and the sanitized notes exist, and at least one other `met` criterion fails.
- Typical shortfalls: one session off the profile or without a recording; the private home declared but the notes not sanitized; a note missing the relation, the device, or the SEQ; the recordings folder linked publicly; two sessions with the same code; the verification recorded only for the second session.

**missing:**

- No `sessions/P-nn.md` note exists at the snapshot, or no counted session is recorded anywhere in the record, the results, or the report.

**Guardrails:**

- The sessions may have run in Week 7: a session on or before 15 November is correct when the design was written and the instrumentation verified before it, and the run sprint in S2 states which sessions ran where.
- A session run before the design was written or before the instrumentation was verified is not counted, and the record says why.
- The session notes' prose, their length, and the quote choice are the team's; the criteria are the count, the conditions, the private placement, and the sanitized fields.
- A teammate's dry run is not a counted session, and a pilot is never evidence.
- A session stopped before its data is complete does not count as completed; the stop and its reason are recorded in the note and the results.
- The private repository's contents are not readable without access; judge them from the record and the PDF, make the single access check when the agent has it, and record an unverifiable access claim as an evidence gap for that check only.
- An instructor who cannot access GitHub is met by the Moodle-only archive and a declared deviation, per S11's risk and S17's `## Deviations`.
- The three-session minimum and the qualitative fallback are S4's; this segment judges how many ran and under what conditions, not what the results concluded.
- A note written after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`; the state at the cutoff is what the snapshot shows.

### S4 — Results and conclusion

**Check:**

- `docs/usability-tests/ut-01/results.md` in the snapshot, read whole.
- The `UT-01` record's goal, research questions, `## Measures`, `## Analysis Plan`, and `## The Requirement`.
- `docs/usability-tests/README.md`'s `UT-01` row.
- `reports/week-08/README.md`'s summary and `## Usability test` section.
- `docs/usability-tests/ut-01/sessions/P-nn.md` for the per-participant values the table repeats.

**met:**

- `docs/usability-tests/ut-01/results.md` exists at the snapshot and is written in the run week.
- With at least three counted sessions, `results.md` carries the per-participant table with each task's outcome and the assistance.
- It carries `Task 1`'s aggregate completion rate: the count or proportion that reached the end state, and the count or proportion that did so unaided.
- It carries `Task 1`'s median time on task, and the median SEQ for each task: `Task 1`, `Task 2`, and `Task 3`.
- It carries the SUS mean and median with the `n=<count>` caveat, and the SUS is reported with its count wherever it appears.
- It carries every additional measure the analysis plan named, with the statistic and the scope the plan set before the first session, and no measure is added after the data.
- It carries a thematic analysis that groups the observations into a small set of themes, each with the sessions it came from, and reports no single participant's remark as a theme.
- It carries the limitations: the sample size, the participants' relation to the target user, the environment, and what the team could not measure.
- The conclusion answers each research question in the record, states the product response, and names the verdict the testing plan records by linking the plan's row.
- The conclusion names each change the team commits to, with the finding that carries it and its task issue, and each change it declines, with the reason and the triage or the `DEC-nnn` that records the decision; a null result says so and gives the reason.
- It links the sanitized session notes it summarizes and copies no raw data and no participant identity.
- When fewer than three counted sessions ran, the record stays `Planned`, `results.md` carries the per-participant table, the instrumentation comparison, the limitations, and the declared shortfall, with no aggregate statistic, and the report claims no result.
- The `UT-01` record's `**Status:**` is `Completed` when the counted sessions and the results are recorded, and `Planned` when the shortfall fallback applies.
- The index's `Results` cell links `results.md` when the results are written, and its `Status` cell agrees with the record.

**What does not count:**

- A missing per-participant table, aggregate completion, median time, a per-task median SEQ, or the SUS mean, median, and count.
- A SUS reported without its count, or a small sample presented as a claim about the population.
- An aggregate invented from missing data, or a participant added to the table without a session note.
- A measure the analysis plan did not name, or a statistic chosen after the data.
- A thematic analysis whose theme is one participant's remark, or one with no sessions named.
- Limitations that omit the sample size, the relation, the environment, or what could not be measured.
- A conclusion that answers some research questions, names no product response, or names a verdict the testing plan does not record.
- A conclusion that commits to a change with no finding or task issue, or declines one with no reason.
- Aggregates with fewer than three counted sessions, or a record marked `Completed` with no results.
- A `Results` cell still `Pending` after the results were written, or a `Status` cell that disagrees with the record.

**partial:**

- `results.md` and the conclusion exist with the results and the product response, and at least one other `met` criterion fails.
- Typical shortfalls: one minimum measure missing; the `n=<count>` caveat missing; a per-task SEQ omitted; the limitations thin; the conclusion not answering a research question; the record's status or the index row out of step; a declined change with no reason.

**missing:**

- `docs/usability-tests/ut-01/results.md` is absent at the snapshot, or it carries no result and no declared shortfall.

**Guardrails:**

- The results' prose, the table's extra columns, and the conclusion's shape are the team's; the criteria are the minimum measures, the statistics, the `n` caveat, the limitations, the answering of the questions, and the product response.
- The four measures and the minimum statistics are the analysis plan's; the `QR-nn` reads one measure, and S8 judges which and the verdict.
- The instrumentation comparison is S5's and the findings are S6's; the results link both without restating them, and a missing comparison is reported in S5.
- The three-session minimum is the run's requirement; when fewer ran, the qualitative record is correct, and the absence of aggregates is not a shortfall.
- The report's `## Usability test` section is S17's; this segment judges `results.md` and the record's own status and index row.
- The record's `**Status:**` and the index row must agree with each other; a disagreement is reported once, here, and not again in S3.
- A results file written after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`, and the state at the cutoff is what the snapshot shows.

### S5 — Instrumentation comparison

**Check:**

- `docs/usability-tests/ut-01/results.md`'s instrumentation comparison.
- The `UT-01` record's `## Instrumentation` section, for the task or question the design said it could not cover.
- `docs/analytics.md#the-events` and the `source` rule, for the test's pipeline events.
- The private usability-data repository's filtered telemetry export claim, and any saved export the agent can read.
- The session notes, for the observation that covered what the instrumentation could not.

**met:**

- `results.md` carries an instrumentation comparison written from the test's telemetry export, read with the participant link the record states.
- The comparison covers the events or records the test actually instrumented, with `source=usability-test` for the events that go through the analytics pipeline.
- It compares what the instrumentation recorded with what the session records show, for the funnel or tasks it covers.
- It says which task or research question the instrumentation could not cover, and how the observation covered it instead.
- It repeats the limit the record's `## Instrumentation` section states, and invents no event, metric, or observation the instrumentation does not produce.
- It presents no test event as a product metric: the comparison is read from the filtered data, and the product's metrics exclude `usability-test` traffic.
- The comparison names no address, credential, or participant identity, and copies no raw export.
- When the export cannot be read, the comparison draws only the conclusions the record and the session notes settle, and `**Evidence:**` says what could not be read.

**What does not count:**

- A comparison that lists events or tools instead of comparing them with the session records.
- A comparison that claims the instrumentation covered every task or question, with no limit recorded.
- A metrics claim that includes `usability-test` or `smoke` traffic, or a test event presented as a product metric.
- A comparison that reads an event the record does not name or the snapshot's code does not emit.
- A comparison that copies the record's instrumentation section instead of reporting what the export showed.
- A comparison that carries an address, a credential, a participant identity, or a raw export.
- A comparison that invents a metric the test did not instrument to cover a gap.

**partial:**

- `results.md` carries the comparison with what it covered and at least one other `met` criterion fails.
- Typical shortfalls: the limit missing; the export's source unstated; a test event presented as a metric; one task's coverage unstated; the observation's role in covering a gap unnamed.

**missing:**

- `results.md` carries no instrumentation comparison.

**Guardrails:**

- The test's instrumentation design, its event set, and its store are Week 7's; this segment judges the Week 8 comparison, not the design, and a design defect that the comparison reports is S3's or S5's only where this week's criteria name it.
- The comparison's shape and length are the team's; the criteria are the source, the coverage, the stated limit, and the no-product-metric rule.
- The export is private; judge it from the results' account and the record, make the single access check when the agent has it, and record an unverifiable export as an evidence gap for that check only.
- The instrumentation need not cover a secondary task; the comparison's value is saying so, and an uncovered `Task 2` or `Task 3` is not itself a shortfall.
- The report's instrumentation summary is S17's; this segment judges the results' comparison.
- A comparison written after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`.

### S6 — Findings

**Check:**

- `docs/usability-tests/ut-01/results.md`'s `### Finding n` sections.
- The task issues the findings name, at `ISSUE_CUTOFF`, for the anchor each cites.
- `docs/usability-tests/ut-01/sessions/P-nn.md` and the aggregate table for each finding's evidence.
- `docs/usability-tests/ut-01/results.md`'s headings and anchors, and `scripts/check_snapshot_links.py`.
- `reports/week-08/README.md`'s `## Usability test` and the findings' task issues.

**met:**

- `results.md` carries one section per finding, numbered `### Finding 1`, `### Finding 2`, and so on, in the order the results present them, with no zero padding and one stable anchor each.
- Each finding states what was observed and carries `**Severity:**` `Critical`, `Major`, or `Minor` with the reason for the rating.
- Each finding carries `**Tasks:**` the task as `UT-01 Task 1` together with the participant codes it came from, such as `UT-01 P-03` and `UT-01 P-05`.
- Each finding carries `**Evidence:**` linked to the session notes or the aggregate table.
- Each finding carries `**Recommendation:**` what the team would change and `**Task issue:**` a link to the issue that carries the work, or `None`.
- Each finding is cited by its own anchor, such as `docs/usability-tests/ut-01/results.md#finding-2`, and the number is stable once the report or an issue cites it.
- Each finding is sanitized: the participant codes are allowed, and a name, an address, or a quoted identity is not.
- A finding's evidence link resolves to the note or the table it names.
- A test that finds nothing significant records that, and no finding is invented to fill the section.

**What does not count:**

- A finding that is a paragraph without its severity, its tasks and codes, its evidence, its recommendation, or its task issue.
- A severity outside the three, or a rating with no reason.
- A task cited by its number alone, or a finding whose participant codes are missing.
- A participant named instead of coded, or a finding quoting an identity.
- A finding cited by a title, a number, or the test alone, or one renumbered after an issue cited it.
- A finding without its own anchor, or with an evidence link that does not resolve.
- A finding whose `**Task issue:**` link does not resolve, or a `None` that the triage does not explain.
- A finding that is a single participant's preference with no other evidence.

**partial:**

- `results.md` carries the findings with their sections and fields, and at least one other `met` criterion fails.
- Typical shortfalls: one field missing; a task cited by number alone; the anchor not stable; a `**Task issue:**` that does not resolve; one finding unsanitized; a finding with no evidence link.

**missing:**

- `results.md` carries no `### Finding` section at all, or its findings carry neither a severity nor a task and evidence.

**Guardrails:**

- The findings' prose, their count, and their order are the team's; the criteria are the one section per finding, the five fields, the anchor, and the sanitization.
- A severity is the team's judgement with its reason; a `Critical` finding is not required to exist, and a test that finds nothing is a result.
- The finding's task issue, its scheduling, and its `**Task issue:**` choice are S7's; this segment judges that the field exists and that a link resolves.
- The aggregate table and the session notes are S3 and S4's; this segment judges the finding's citation of them.
- A screenshot may be a finding's evidence only when it is sanitized and linked; a screenshot that carries an identity is a privacy shortfall here and in S17.
- Participant codes are public; an identity is not. Never copy a name, an address, or a quote from the PDF into feedback.
- A finding added after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`.

### S7 — Triage and planned fixes

**Check:**

- Each finding's `**Task issue:**` field in `docs/usability-tests/ut-01/results.md`.
- `issue-fields.json` and `issues.json` at `ISSUE_CUTOFF` for the task issues the findings name, their types, milestones, `### Requirements`, and closing pull requests.
- `prs.json` for the Week 8 pull requests that closed those issues and for the fix's pull request.
- `reports/week-08/README.md`'s summary and `## Usability test` for the triage record and the moves to `SPRINT-09`.
- `docs/project-plan.md#quality-requirement-testing-plan` and the `REL-08` changelog entry for the planned fixes.

**met:**

- Every finding is triaged: the team records its severity, whether it opens a task issue, and when the work is scheduled.
- When a significant finding exists, at least one task issue is opened from it and scheduled in `SPRINT-08`'s milestone; a finding is significant when its `**Severity:**` is `Critical` or `Major`.
- The task issue cites the finding by its path and anchor, such as `docs/usability-tests/ut-01/results.md#finding-1`, and the finding's `**Task issue:**` links the issue.
- The task issue names the story and the `AC-nn` it serves and names the `FR-nnn` or `ADR-nnn` in `### Requirements`; a defect never says `None`.
- A task that is not product work says `None: repository upkeep`.
- Each finding's `**Task issue:**` is the issue it became, or `None` with the triage saying why no issue was opened.
- The fixes are planned: a fix that lands is in `REL-08`'s changes, and a fix that does not land moves to `SPRINT-09` at the sprint close with its reason declared in the report.
- No fix is forced: when the test finds nothing significant, the triage says so and opens no issue, and a fix the team would not make is recorded as a decision.
- The triage is visible where a reader looks: the report's summary or `## Usability test`, or the results' conclusion, names each finding's disposition.

**What does not count:**

- A finding not triaged: no task issue, no `None` reason, and no scheduling anywhere.
- A `Critical` or `Major` finding with no task issue scheduled in `SPRINT-08` while the week plans a fix.
- A task issue whose `### Requirements` says `None` for a defect or a product change, or names an `FR-nnn`/`ADR-nnn` that does not resolve.
- A finding's `**Task issue:**` pointing at an issue that does not cite the finding, or an issue in no sprint's milestone.
- A fix said to land while `REL-08`'s changelog carries no such change.
- A fix moved to `SPRINT-09` with no reason, or a move the report does not declare.
- A forced task issue when the test found nothing significant.
- A triage that records a severity different from the finding's own.

**partial:**

- The findings are triaged with their issues and the fixes are planned, and at least one other `met` criterion fails.
- Typical shortfalls: one finding with no `None` reason; a significant finding's issue in the wrong sprint; a task issue without the finding citation; a defect saying `None`; a move to `SPRINT-09` without its declared reason.

**missing:**

- No finding is triaged anywhere in the results, the report, or an issue, or a significant finding exists and no task issue was opened.

**Guardrails:**

- The triage's wording, the number of issues, and which finding becomes work are the team's; the criteria are that every finding is considered, a significant one is carried by a scheduled issue, and the plan is recorded.
- The task-issue shape is Week 1 and Week 2 mechanics and is not re-graded except where this week names it: the finding citation, the story and `AC-nn`, the `FR-nnn`/`ADR-nnn`, the `None` rule, and the sprint.
- Whether the fix actually landed is S15's; this segment judges the plan and the triage record, and a disagreement between them is reported once, in S15.
- Scheduling is read at `ISSUE_CUTOFF`; a reschedule after the cutoff is a caveat and never repairs the state at the cutoff.
- A null result that opens no issue is correct and is never a shortfall; the required check is that the team said so.
- The triage record may live in the results' conclusion, the report's summary, or the issue itself; this segment accepts any of them when the finding links the issue and the issue cites the finding.
- A finding whose `**Task issue:**` is `None` is correct when no issue is opened, and the reason belongs in the triage, not in every finding.

### S8 — QR/QRT verdict and threshold

**Check:**

- `docs/project-plan.md#quality-requirement-testing-plan` for the `QR-nn` and `QRT-01` row.
- The `QR-nn` file under `docs/quality-requirements/qr/` and its `QRT-01` section.
- `docs/usability-tests/ut-01/results.md` for the measure the verdict reads.
- `docs/threshold-of-success.md` for the usability goal's status and outcome.
- `reports/week-08/README.md`'s `## Threshold review` for the report's account.

**met:**

- With at least three counted sessions, the `QR-nn` testing-plan row's `Status` is `Passes` or `Fails`.
- The row's `Checked` is `SPRINT-08` linked to its plan section, and its `Evidence` links `results.md`.
- The verdict is read against the `Response Measure` the team set before the first session, and it is the test's result at its last check rather than a status copied from the requirement.
- A `Fails` row is not dropped: the findings and the triage carry the fix, and the release claims no quality through it.
- The row's `QR` cell links the requirement file, and its `QRT` cell links the test's section.
- When fewer than three counted sessions ran, the row stays `Not verified` with its planned sprint, or moves to `SPRINT-09` with its reason, and the report declares the shortfall or the move.
- When the team has a threshold usability goal and the test ran, the goal's `**Status:**` is `Achieved` or `Missed` and its `**Outcome:**` cites `UT-01` and the results, with the evidence linked.
- A team without a usability goal is not penalised, and no goal is invented for it.
- The record's `**Status:**`, the index row, and the testing plan agree with one another.

**What does not count:**

- A row still `Not verified` after at least three counted sessions ran, or a `Passes`/`Fails` with `Checked` not `SPRINT-08`.
- A verdict with no evidence, evidence that is not the results, or a `Checked` sprint that is not linked.
- A `Fails` row dropped, or a release claiming quality through a failed requirement.
- A row whose `Status` is a claim about the requirement rather than the test's result.
- Fewer than three counted sessions with a `Passes` or `Fails` row.
- A usability goal left `Open` after the test ran and its measure settled.
- An `Achieved` or `Missed` with no `**Outcome:**`, or an `**Outcome:**` that does not cite `UT-01` and the results.
- A usability goal invented or forced on a team that has none.
- A record or index that still says `Planned` while the testing plan records a verdict.

**partial:**

- The testing plan carries a verdict with its check and evidence, and at least one other `met` criterion fails.
- Typical shortfalls: the `Checked` cell not linked; the evidence linking a different artifact; a goal's outcome missing its citation; a shortfall's move to `SPRINT-09` undeclared; the record or index out of step.

**missing:**

- The testing plan's `QR-nn` row is absent at the snapshot, or it is `Not verified` or unread while the sessions ran and no shortfall is declared.

**Guardrails:**

- The bar, the measure, and the sub-characteristic are Week 7's choices; this week records the verdict against them, and a bar that moved after the first counted session is a shortfall wherever it is recorded.
- The verdict belongs to the testing plan and its row, not to `results.md`; the results state what was found and link the row.
- The `**Checked QRs:**` list is S15's, built from the `Checked` cells; this segment judges the row itself.
- The threshold's failure and success statements and its earlier goals are not re-graded; this segment judges the usability goal's settlement.
- A team with no usability goal is correct, and the required check is the quality requirement and its test.
- The report's `## Threshold review` table is S17's; this segment judges the goal's field in `docs/threshold-of-success.md`, and a disagreement is reported once, there.
- A verdict or a goal settled after `ISSUE_CUTOFF` is a caveat in `**Evidence:**` and never repairs the state at the cutoff.
- A `Fails` verdict is a result, not a shortfall: the fix and the release are judged in S7 and S15.

### S9 — Configuration plan

**Check:**

- `docs/configuration-plan.md` in the snapshot, read whole.
- The team's root `AGENTS.md` for the plan link in its repository layout.
- The Week 8 pull requests that added or updated the plan, and any pull request that enacted a configuration change.
- `reports/week-08/README.md`'s `## Configuration management` for the item count the report claims.

**met:**

- `docs/configuration-plan.md` exists at the snapshot, and `**Reviewed:**` sits under its `#` heading with one date, the day the plan was last reviewed.
- The plan groups its items into the five groups, each item in exactly one: source control and release; checks; environments and secrets; dependencies and builds; agent context and artifacts.
- The plan carries at least 8 `Active` `CFG-nn` items, with at least one in each group.
- Each item is a `### CFG-nn` section under its group, headed with the identifier alone, its first line naming the item, and a two-digit repository-wide identifier.
- Each item carries, in this order as a bulleted list: `**Status:**` `Active` or `Dropped`, `**Type:**`, `**Purpose:**` saying what it is for and what breaks without it, `**Owner:**`, `**Where:**` as a file path or a settings page in words, `**Connections:**`, and `**What good looks like:**` stating the target and linking the course rule it must meet.
- Each item's `**Connections:**` is the single record of its edges, and each edge names the other end, its kind (`reads`, `enforces`, `produces`, `triggers`, or `cites`), and the concrete failure.
- An edge to an item outside the plan names the external item; an edge to an item in the plan links that item's `CFG-nn` section.
- A set of files is one item at its index or entry point, and its `**Where:**` names that path rather than listing every file.
- A dropped item stays where it is, in its group, with `**Status:**` `Dropped` and its `**Dropped:**` date and reason; it is neither counted nor judged, and its identifier is never reused.
- A configuration the team does not have is named in words in the evaluation, has no `CFG-nn`, and receives one only once it exists.
- The plan carries no secret value, no private deployment or dashboard address, and no credential; a private setting's `**Where:**` names the setting in words.
- A change that alters what the plan records is updated in the same pull request, and a settings change that leaves the plan accurate needs no update.
- The team's root `AGENTS.md` links `docs/configuration-plan.md` in its repository layout, by a path from the root.

**What does not count:**

- A plan without `**Reviewed:**`, with several dates, or with the date not under its `#` heading.
- Fewer than five groups, an item in two groups, or an item in no group.
- Fewer than 8 `Active` items, or a group with no `Active` item.
- An item with a missing field, a field out of order, a `**Status:**` other than `Active` or `Dropped`, or a `**Purpose:**` that does not say what breaks.
- An item whose `**What good looks like:**` states no target or links no course rule.
- A `**Connections:**` list of file names without kinds and failures, or an edge that names no other end.
- An item that is one file of a set instead of the set's index, or a `**Where:**` that names every file of a set.
- A dropped item deleted, moved to the end, renumbered, or counted as `Active`; a reused `CFG-nn`.
- A configuration the team does not have given a `CFG-nn` or described as existing.
- A plan carrying an address, a credential, or a secret; a `**Where:**` linking a private settings page.
- An `AGENTS.md` without the plan link, or a plan linked from a file other than the team's `AGENTS.md` layout section.

**partial:**

- The plan exists with the five groups and about the required items, and at least one other `met` criterion fails.
- Typical shortfalls: seven items or one group empty; one item missing a field or a connection's failure; a dropped item removed; a private setting linked; the `AGENTS.md` link missing; the review date missing.

**missing:**

- `docs/configuration-plan.md` is absent at the snapshot, or it carries no `CFG-nn` item.

**Guardrails:**

- The plan's prose, its types, its owners, and the wording of each purpose are the team's; the criteria are the groups, the count, the fields, the connections, the dropped form, and the sanitization.
- The five groups may be named in the course's words or an equivalent that covers the same area; what matters is that each item belongs to exactly one and the fifth covers the agent context.
- An item the team cannot open or read is still an item; a defect in the product's behaviour is not, and a security weakness in one is a risk or a task issue.
- The course materials are an upstream item: the team installs and judges them, does not edit them, and a proposed improvement is in the team's own repository.
- The plan is created this week, so every item is judged here; the earlier weeks' artifacts it names are not re-graded on their own rules.
- A plan edited after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`; the state at the cutoff is what the snapshot shows.
- A `**Reviewed:**` date that is older than the plan's last inventory change is a shortfall only when the change was not reviewed; a maintained plan that kept its date is correct.
- The plan's link check is S17's; a private setting named in words is correct and is not a missing link.

### S10 — Goal-based configuration evaluation

**Check:**

- `reports/week-08/cm-evaluation.md` in the snapshot, read whole.
- `docs/configuration-plan.md` for the `CFG-nn` items the goal sections link, and the plan's groups.
- The evaluation's `**Baseline:**` tag or commit in `tags.json` and `releases.json`, or in the snapshot's history.
- The Week 8 pull requests that added or updated the evaluation.
- `reports/week-08/README.md`'s `## Configuration management` for the report's account of the goals and the first change.

**met:**

- `reports/week-08/cm-evaluation.md` exists at the snapshot, headed `# CM Evaluation`.
- It carries `**Baseline:**`, `**Reviewed:**`, `## Method`, one `##` section per local goal, `## What We Could Not Judge`, and `## The First Change`, in that order.
- `**Baseline:**` names the tag or commit the review judged, and it is frozen, so a later week can tell what state the goal sections describe.
- `**Reviewed:**` gives the date of the review.
- `## Method` is one paragraph saying who judged, on what date, against which baseline, in what order, and what was out of scope, and it says the team wrote a local goal for each artifact family and grouped the artifacts by the goal they serve.
- Each goal is local: a purpose an artifact set serves, such as deciding what the product should be, specifying what it must do, verifying it, planning and tracking it, learning from its users, communicating it, or keeping the context trustworthy for a reader or an agent.
- The goal is chosen and explained in the team's own words, and it is not the project's goal.
- Each goal section carries, in this order as a bulleted list: `**Today:**` the artifacts that achieve it, each linked to its `CFG-nn` section or named in words when the plan does not carry it; `**A more convenient way:**` the proposed set and the concrete change, using `Keep`, `Merge`, `Replace`, `Cut`, or `Add`; `**Why:**` the goal is still achieved and the change removes a named mechanism, with the evidence from the team's own use; and `**Tradeoffs:**` what the change gives up and why the gain is worth the loss, or why the team would not make it.
- The mechanism named in `**Why:**` is concrete, such as duplication, a manual step, a readerless file, staleness, an unverifiable check, or a context cost.
- The evaluation judges whether the set of artifacts is the most convenient way to achieve the goal; it does not judge whether an item meets its `**What good looks like:**`.
- A change never removes an item the criteria require: a required item is fixed or simplified, and only configuration beyond the criteria is cut.
- `## What We Could Not Judge` names each item or artifact the team could not judge, with the reason and the risk it carries; when every item was judged, it says `None` and says so.
- `## The First Change` is one paragraph naming the one change the team would make first, what it keeps, what it removes, and its main tradeoff.
- The goal sections and the first change schedule no work: no task issue, sprint item, or implementation is required, and the evaluation gives no order beyond the first change.
- The evaluation carries no secret value, no private deployment or dashboard address, and no credential; a failing item's consequence is in words, without the step-by-step that would let a reader use it.
- The `**Today:**` and `**A more convenient way:**` cite a `**Connections:**` edge when an edge supports or blocks a change, and a proposal that removes an item names the edges it cuts.

**What does not count:**

- A missing section or field, a section out of order, or a field out of order.
- A baseline given as a branch name, a moving state, or a bare worktree; a missing reviewed date.
- A `## Method` that is several paragraphs, or one that omits who, when, the baseline, the order, or the scope.
- A goal that is the project's goal, a milestone, or a task list.
- A goal section missing a field; a `**Today:**` that links no `CFG-nn` and names nothing; a `**A more convenient way:**` that is a wish with no concrete change or no `Keep`/`Merge`/`Replace`/`Cut`/`Add`.
- A `**Why:**` with no named mechanism or no evidence from the team's own use; a `**Tradeoffs:**` with no loss or no reason the gain is worth it.
- A change that removes a required item, or one that loses the goal it claims to keep.
- An evaluation that grades items against their `**What good looks like:**` instead of judging the set by goal.
- A `## What We Could Not Judge` that omits an item the team plainly could not read, or an empty section instead of `None`.
- An evaluation that orders the changes, schedules work, or opens a task issue for the recommendation.
- An evaluation carrying a private value, an address, a credential, or a step-by-step that would let a reader use a weakness.

**partial:**

- The evaluation exists with its goal sections and first change, and at least one other `met` criterion fails.
- Typical shortfalls: the method missing a scope or a date; a goal section missing its tradeoff; the mechanism unnamed; the `What We Could Not Judge` note empty; the first change without its tradeoff; a goal that is the project's goal.

**missing:**

- `reports/week-08/cm-evaluation.md` is absent at the snapshot, or it carries no goal section and no first change.

**Guardrails:**

- The goals, their number, and the proposed changes are the team's; the criteria are the section order, the four fields, the local-goal test, the tradeoff, the limits, and the first change.
- No minimum number of goals applies; a team with three goals is correct when each is a real purpose, and a team with five is not better for the count.
- The recommendation is a judgement, not a plan: no implementation is required in the review week, and a change the team enacts is extra evidence.
- The `CFG-nn` items the sections name are S9's artifacts; this segment judges the judgement, not the plan's fields.
- The report's `## Configuration management` section is S17's; this segment judges the evaluation file.
- A baseline that is an earlier tag the team cut is correct even when the snapshot has later commits, and the plan's current state may differ from the baseline.
- An item the team could not judge belongs in the evaluation's note, not in the report's `## Deviations`; a reported deviation is judged in S17 for what it declares.
- An enactment after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff.

### S11 — Glossary and risk register

**Check:**

- `docs/glossary.md` in the snapshot, for the Week 8 terms and their definitions.
- `docs/risks.md` in the snapshot, for the four Week 8 risks, their fields, and the summary table.
- The Week 8 pull requests that added the terms and the risks.
- `reports/week-08/README.md` for the risk and glossary claims the report makes.

**met:**

- `docs/glossary.md` carries a `###` section for each of `configuration`, `configuration management`, `configuration review`, `configuration plan`, `configuration item`, `configuration evaluation`, `baseline`, `upkeep`, `reproducible build`, `dependency pinning`, `secret`, `context window`, and `agent instruction`, each under its domain heading.
- Each term's definition is one sentence that says what the term means in this project, not what it means in general.
- A term an artifact already defines carries its `**Defined by:**` line linking that artifact, and a term no artifact defines stands on its definition alone.
- Each term's heading is the term alone, so its anchor is the term and a link to it survives an edit to the definition.
- `docs/risks.md` carries the secret-leak risk, the stale-configuration risk, the unupdatable-dependency risk, and the environment-drift risk, each a `## RISK-nn` section with its first line stating the cause, the event, and the impact.
- Each new risk carries `**Status:** Open`, `**Impact:**` and `**Likelihood:**` with their rating word and the reason on a nested bullet, `**Trigger:**`, `**Window:**`, `**Mitigation:**`, and `**Contingency:**`.
- The secret-leak risk's contingency is the incident response: revoke or rotate the credential, tell the instructor, remove the material from the files and the history, and write the account privately.
- The stale-configuration risk's contingency is to update the plan in the pull request that records the change, and to treat a plan that describes an older repository as a defect.
- The unupdatable-dependency risk's contingency is to pin the working version, record why, and open the task that removes the need for it.
- The environment-drift risk's contingency is to deploy the commit staging passed, keep the runbook current, and redeploy rather than patch the VM by hand.
- The register's summary table lists the new risks with the columns `ID`, `Status`, `Impact`, `Likelihood`, and `Risk`, the open risks first and sorted by impact then likelihood, and the settled ones after them in identifier order.
- The summary table agrees with the sections' statuses and ratings.
- The new terms' anchors are unique and the glossary's earlier terms and the register's earlier risks are unchanged.

**What does not count:**

- A missing Week 8 term, or a term defined generically rather than as this project uses it.
- A definition of more than one sentence, or a term section with no definition.
- A missing `**Defined by:**` where an artifact defines the term.
- A missing secret-leak, stale-configuration, unupdatable-dependency, or environment-drift risk.
- A risk without its first-line cause, event, and impact, or missing `**Status:**`, `**Impact:**`, `**Likelihood:**`, `**Trigger:**`, `**Window:**`, `**Mitigation:**`, or `**Contingency:**`.
- A `**Status:**` other than `Open` on a new risk, or an `Open` risk with no `**Outcome:**` after it settled.
- A contingency that restates the mitigation, names no concrete fallback, or omits the required action for its failure mode.
- A summary table that omits a new risk, is unsorted, or disagrees with a section.
- A glossary entry, a risk, or the summary table carrying a private value, an address, or a credential.
- A risk whose mitigation or contingency is a decision the team has not made, or one with two possible fallbacks.

**partial:**

- The terms and the four risks are present with most of their fields, and at least one other `met` criterion fails.
- Typical shortfalls: one term missing or one definition generic; one risk missing a field; a contingency that omits the incident response or the redeploy; the summary table not updated.

**missing:**

- The glossary carries none of the Week 8 terms, or `docs/risks.md` carries none of the four risks.

**Guardrails:**

- The glossary's earlier terms and the register's earlier risks are not re-graded; this segment judges the Week 8 additions and the summary table's state.
- The definitions' wording, the ratings, the mitigation, and the windows are the team's; the criteria are the terms' presence and one-sentence definitions, the four risks' fields, and the fallbacks' required content.
- The 13 terms may appear in any order; the assignment's list is the set, not an order.
- Extra glossary terms and extra risks are allowed and are not judged here unless they break the file or contradict the additions.
- The fallbacks are the week's own: an equivalent fallback is correct when it covers the same failure mode and names the required action.
- A risk whose window has already closed without its trigger is a `Dropped` risk; a new risk is not re-numbered, and an identifier is never reused.
- The glossary and the register are maintained documentation; an edit after `ISSUE_CUTOFF` is a caveat in `**Evidence:**`, and the state at the cutoff is what the snapshot shows.
- The configuration plan's `AGENTS.md` link is S9's and the Week 9 handoff's AI trace is S18's; this segment judges the glossary and the register.

### S12 — Week 7 action points and open questions

**Check:**

- `reports/week-07/meeting-report.md` in the snapshot, for its `## Action points` and `## Open questions`.
- `reports/week-08/meeting-report.md` in the snapshot, for `## Previous action points` and `## Previous open questions`.
- The artifacts the outcomes claim to have changed, in the snapshot.
- The Week 7 report's own content against the snapshot, to confirm it was not edited.
- `docs/decisions.md` for the `DEC-nnn` entries the outcomes cite.

**met:**

- Every Week 7 action point due by Week 8, and every action carried from an earlier report, has its outcome in the Week 8 report's `## Previous action points` table.
- The table's `Action` cell cites the action point by `reports/week-07/meeting-report.md#action-points` with the action quoted.
- The table's `Outcome` says whether it was carried out, what was found, and links each artifact the outcome changed and the task issue that carried it out, if any.
- The table's `Decision` cell links each `DEC-nnn` the outcome produced, or says `None` when the outcome needed no decision.
- Each outcome that changed an artifact is carried into that artifact; an outcome recorded only in the table has not been carried out.
- Every Week 7 open question is answered in `## Previous open questions`, with its `Answer` linking each artifact the answer changed and its `Decision` linking the `DEC-nnn` or saying `None`.
- An open question that is not yet answered is carried forward into the Week 8 report's `## Open questions` rather than dropped.
- The Week 7 report is not edited: its text at the snapshot is the text the Week 7 submission recorded.
- A Week 7 report with no action point due by Week 8 and no open question makes `None` in the matching `## Previous` section correct.

**What does not count:**

- A Week 8 report without `## Previous action points` or `## Previous open questions` when the Week 7 report has an action point due by Week 8 or an open question.
- An action point's `Outcome` recorded in the table with no change to the artifact it names.
- An open question dropped with no answer and no carried-forward row.
- An action point whose `Outcome` says it was completed while the artifact shows otherwise.
- An edit to the Week 7 report, such as a rewritten outcome or a removed table.
- A decision cell empty instead of `None`.
- An action point due after Week 8 judged as if it were due this week.
- An outcome that links no artifact and no task issue when it changed one.

**partial:**

- The previous sections exist with the outcomes, and at least one other `met` criterion fails.
- Typical shortfalls: an action point missing its citation or its artifact link; an open question carried forward without a row; a decision cell empty instead of `None`; one outcome not carried into its artifact.

**missing:**

- The Week 8 report has neither `## Previous action points` nor `## Previous open questions`, or no Week 7 report exists and no carried action or question replaced it.

**Guardrails:**

- The Week 7 report's prose and its earlier actions are Week 7's; this segment judges the outcomes and the questions' closure, and the Week 7 report itself is not re-graded.
- A Week 7 report with no action point due in Week 8 and no open question makes `None` correct and is never a shortfall.
- When the Week 7 report is absent from the snapshot, judge this week's work against what exists and report the absence once, here, rather than re-judging the Week 7 submission.
- An action point due in Week 9 is not due this week; it is judged from the Week 8 report's own new action points in S13.
- A carried action with an `Outcome` of `Not done` reappears in the Week 8 report's `## Action points` with a new due week, unless the team or the customer dropped it, which `Outcome` then says.
- A Week 7 open question the customer answered outside a meeting still closes with its `Answer` and its `Decision`.
- The outcomes may have been carried out in the Week 7 window or during Week 8; the artifact's state at the snapshot is the evidence, and a change recorded after `ISSUE_CUTOFF` is a caveat.
- The report's new action points and open questions are S13's; this segment judges only the previous week's closure.

### S13 — Sprint Review

**Check:**

- `reports/week-08/meeting-script.md`, `reports/week-08/meeting-report.md`, and `reports/week-08/meeting-transcript.md` in the snapshot.
- The Week 8 meeting's date against the Week 8 window, the cutoff, and the class week.
- The `DEC-nnn` entries in `docs/decisions.md` that the report cites, and the artifacts the decisions change.
- The script's and the report's first commits and pull requests, for whether the script came before the meeting.
- The meeting's recording and transcript claims against the Moodle PDF's items 7 and 9.
- The results, the testing plan, and the findings the review showed, for the report's account of what was presented.

**met:**

- At least one customer meeting was held in the Week 8 window, on or after Friday 13 November 2026 and by `ISSUE_CUTOFF`, and the results review is that meeting, the sprint's Sprint Review.
- The script was written before the meeting and carries `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in order.
- `## Agenda` starts with the three permission questions and shows the deployed production instance with the analytics and observability dashboards, the sanitized results, the conclusion and its product response, the `QR/QRT` result, the findings and their task issues, the threshold outcome, and the next steps.
- The agenda puts the open questions before the last part and ends with the read-back of the decisions and action points.
- The script's questions serve the target in `## Context`: the results' conclusion, the product response, the findings' priority, and the next steps, and an answer could change what the team does next.
- The script shows at least one rewritten question in `## Key improvements`, with the before, the after, and the principle behind the rewrite.
- The report's `## Metadata` is a bulleted list with the date, the duration, the attendees by GitHub username with `Customer` for the customer, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- The report's `## Summary` has 3 to 5 bullets on what the meeting settled or changed, not on what was on the agenda.
- The report's `## Decisions` lists each decision with a `DEC-nnn` entry that the report cites, and each entry's decision agrees with the report's account.
- The report's `## Action points` has at least two rows with the columns `Action`, `Owner`, and `Due`, the owner is a GitHub username, each due date falls in a named week after Week 8, and at least one falls in Week 9.
- The report's `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`, and `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`.
- A transcript exists when the meeting was recorded or held in writing; it is in English with one sentence per line and a timestamp and speaker label, carries the date and the attendees above the first line, and is sanitized.
- When the customer refused publication, the transcript is not committed and the report says so; when the meeting was held in writing, the written exchange is the transcript.
- The report is the team's own account, and it claims no usability result or verdict that the results and the testing plan do not record.
- The report's `## Metadata` and `## Summary` say what the review showed, including the results, the verdict, the findings, and the next steps, and the configuration evaluation is not presented at the meeting.

**What does not count:**

- No customer meeting in the Week 8 window, or a meeting after `ISSUE_CUTOFF`.
- A script written after the meeting, an agenda out of order, no permission questions first, no deployed instance or dashboards shown, or no read-back last.
- A script with no questions that could change the next step, or with no rewritten question.
- A report without its `## Metadata` items, with fewer than 3 or more than 5 summary bullets, with a decision that has no `DEC-nnn`, or with an action point due inside Week 8.
- An action point with no owner, no due week, or a due date with no week named; fewer than two action points, or none due in Week 9.
- A missing `## Open questions` or `## Disagreements` section when the meeting had one.
- A transcript that restates raw notes, carries a real name, an email address, a phone number, an address, or a recording link, or is committed after the customer refused publication.
- A report that restates the transcript line by line, or that a tool generated and the team pasted in unchecked.
- A report that claims a usability result or verdict the results and the testing plan do not record.
- The configuration evaluation presented as the review's subject, or its absence reported as a shortfall.

**partial:**

- The meeting report and the script exist with the review's content, and at least one other `met` criterion fails.
- Typical shortfalls: one agenda part out of order; a permission question unanswered in the metadata; fewer than two action points or none due in Week 9; a summary bullet count outside 3 to 5; the transcript unsanitized or missing when the meeting was recorded; a report that claims a result.

**missing:**

- `reports/week-08/meeting-report.md` is absent, or no Week 8 customer meeting is recorded.

**Guardrails:**

- The meeting is the Sprint Review, so a second review meeting is not required; a team that held one results review has met the ceremony.
- A meeting held after the class week ends on 19 November but by `ISSUE_CUTOFF` is in the Week 8 window and is a caveat in `**Evidence:**` rather than a shortfall, because the submission deadline, not the class week's end, closes the window; a meeting after `ISSUE_CUTOFF` is a shortfall.
- A meeting before Friday 13 November is Week 7's review, not this week's, and does not satisfy the Week 8 ceremony.
- An asynchronous meeting held in writing is allowed, with the written exchange as its transcript and the substitution declared as a deviation; its `## Roles` and its timeboxes are not required.
- A customer who refused recording or publication makes the transcript's absence correct, and the report's `None` with the reason is complete.
- The recording is Moodle-only and the public report names it; the transcript is public only when the customer allowed publication.
- The week's results are the review's subject, and the configuration evaluation is not presented; showing no new story is correct and is not a shortfall.
- The decisions the review records are judged here for their agreement and citation; what the team did with them is S14's.
- The report's prose, its summary's wording, and the meeting's length are the team's; the criteria are the sections, the agenda's order, the action points' shape, the transcript's existence and hygiene, and the supported claims.
- A report written after `ISSUE_CUTOFF` is a caveat; the state at the cutoff is what the snapshot shows.

### S14 — Review rework and testing-plan rows

**Check:**

- `reports/week-08/meeting-report.md`'s `## Decisions` and the `DEC-nnn` entries.
- The pull requests and commits merged after the meeting and by `ISSUE_CUTOFF`, from `prs.json` and `commits.json`.
- The results, the findings, the task issues, `docs/project-plan.md#quality-requirement-testing-plan`, the configuration plan, and the evaluation at the snapshot and in the Week 8 pull requests.
- `reports/week-08/README.md` for the declared moves and its `## Deviations` entry.
- The `QR-nn` and `QRT-01` files for a changed sub-characteristic, measure, or bar.

**met:**

- Each decision the Sprint Review recorded is applied by the cutoff to the artifact it changes: the results when a finding or the conclusion changes, the findings when a severity or recommendation changes, a task issue when the work changes, the testing plan when a row changes, the configuration plan when an enacted change alters what it records, and the evaluation when its judgement changes.
- A same-week rework is merged into `main` as a pull request, not left as an action point for a later week.
- Each testing-plan row the team's own plan scheduled for `SPRINT-08` is run, or moved to `SPRINT-09` with a reason, and every move is declared in the Week 8 report.
- The testing plan records each row's result, its `Checked` sprint, and its evidence, and a `Passes` or `Fails` row links the proof its level requires.
- A row the team runs is run at its level, and its evidence is the run, the output, or the sanitized report its level requires.
- The `QR/QRT` verdict from Part 6 is in the plan, and the plan's rows and the results agree.
- When the review changes the requirement's sub-characteristic, the measure, or the bar, the requirement, its test, and the testing plan still agree.
- No bar moved after the first counted session.
- A configuration change the review enacts is recorded in the pull request that carries it, and the configuration plan is updated in that pull request when the change alters what it records.

**What does not count:**

- A decision recorded in the report but not applied to the artifact by the cutoff.
- A rework still listed as an action point due in a later week.
- A `SPRINT-08` testing-plan row silently dropped, or moved without its reason and its declaration.
- A testing-plan row whose `Status`, `Checked`, or `Evidence` was not updated after the row was run.
- A `Passes` or `Fails` row with no evidence, or evidence that does not match the test's level.
- A requirement changed while its test and its plan row still name the old measure, or a bar changed after the first counted session.
- A usability verdict claimed in the results instead of the plan.
- An enacted configuration change that the plan does not reflect, or a plan updated in a later pull request than the change.

**partial:**

- The review's decisions are applied and the testing plan is updated, and at least one other `met` criterion fails.
- Typical shortfalls: one decision not applied; one row moved without a declared reason; one row run without its `Checked` update; the bar or the measure changed with the test not updated; an enacted configuration change without its plan update.

**missing:**

- The Sprint Review recorded at least one decision and no artifact changed, or a `SPRINT-08` testing-plan row was due and neither ran nor moved.

**Guardrails:**

- A sprint whose own plan scheduled no row for `SPRINT-08` owes no run, and the rows the plan did schedule are the ones judged; the absence of a row this week is never a shortfall by itself.
- A review that asked for no change makes the absence of rework correct; the team records that in the report, and S13 judges the report's account.
- A docs-only rework may be one pull request for the results and one for the plan; the criterion is that the artifact the decision names changed by the cutoff.
- The release's sequence and its tag are S15's; this segment judges the artifacts the review changed, not the release order.
- A decision applied after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff.
- The configuration evaluation's first change is a recommendation and schedules no work; a review that enacts no configuration change is correct, and the absence of one is never a shortfall here.
- The bar's movement is a Week 7 action or a Week 8 decision; a bar moved after the first counted session is a shortfall wherever it is recorded, and the entry that moved it is judged in the artifact that owns it.
- The report's `## Deviations` entry is S17's for the report; this segment judges whether the move it declares is real.

### S15 — REL-08 release

**Check:**

- `tags.json` and `releases.json`, and the raw `gh api "repos/$REPO/releases?per_page=100"` and `gh api "repos/$REPO/git/refs/tags/<tag>"` responses for the title, the body, and the commit.
- `CHANGELOG.md`'s `[Unreleased]` section and its dated released section.
- `docs/project-plan.md`'s `#### REL-08` block under `### SPRINT-08`.
- The `SPRINT-08` GitHub milestone's state and the issues rescheduled out of it.
- The testing plan's `Checked` cells, for the `**Checked QRs:**` list.
- `gh api "repos/$REPO/rulesets"` and each tag ruleset, for the tag's protection.
- `reports/week-08/README.md` for the release's record, its fixes, and its tag.
- The tag's push time and the merge times of the changelog's released section, the plan's block, and the report.
- The configuration plan's `**Reviewed:**` and any enacted configuration change's pull request.

**met:**

- The tag is named `v<major>.<minor>.<patch>`, it points at a commit on `main`, and that commit is the final production commit the week's record names.
- The release title is the tag, so the title and the tag match.
- The tag is protected against being moved or deleted, by a repository ruleset that covers tag pushes or an equivalent tag-protection rule.
- `CHANGELOG.md` follows Keep a Changelog: `[Unreleased]` was kept through the week, the released entries moved into a dated section such as `[0.8.0]` with the week's changes, that section links the release, and a new empty `[Unreleased]` follows.
- The release body is the upgrade note: it states whether the upgrade requires anything beyond deploying this version, or that it does not, and names the new environment variables and configuration when it does.
- When the release is docs-only, its body says there is no product change and no upgrade is required, and the tag is the team's next version.
- The body ends with the line `[Full changelog](<absolute url>)` linking the changelog's released section, and nothing comes after it; the body carries no address, credential, token, or other private-only value.
- `### SPRINT-08` carries a `#### REL-08` block with `**Released:**` and `**Checked QRs:**`.
- `**Checked QRs:**` lists every `QR-nn` with at least one test whose testing-plan row is `Checked` in `SPRINT-08`, one bullet each linked to its requirement file, or says `None` when none was checked, and after the list one sentence links the plan's `## Quality Requirement Testing Plan` once.
- `REL-08` includes the fix the sprint lands: the changelog's released section carries the change, and the release's upgrade note covers any action it requires.
- `SPRINT-08`'s GitHub milestone is closed after each issue still open was moved into a later sprint's milestone.
- The tag was pushed on the release commit after the sprint's pull requests merged, and before the changelog's released section, the plan's `REL-08` block, and the report were merged.
- The configuration plan's `**Reviewed:**` advanced if the plan was reviewed again after the meeting, and an enacted configuration change is recorded in the pull request that carries it.

**What does not count:**

- A tag on a commit that is not the week's final production commit, a tag on a branch name, or a tag on a commit that is not on `main`.
- A release title that is a nickname while the tag is the version, or a version without the `v` prefix.
- An unprotected tag, or one that a force push or a deletion could move.
- A body that lists the changelog's entries instead of the upgrade note, a body with no upgrade statement, or a body that ends with anything other than the `Full changelog` line.
- A relative changelog link, a body carrying a dashboard address, a credential, or the query endpoint.
- A changelog section that does not link the release, a missing `[Unreleased]`, or a released section with no dated heading.
- A `REL-08` block outside `### SPRINT-08`, or one missing its `**Released:**` or its `**Checked QRs:**`.
- A `**Checked QRs:**` list copied from `REL-07`, built from a requirement's status rather than its tests' `Checked` cells, missing a checked requirement, or missing the one sentence that links the testing plan.
- A landed fix absent from the released section, or a fix the report says landed while the changelog does not carry it.
- `SPRINT-08`'s milestone left open, or closed with issues still in it.
- A tag pushed after the changelog's released section, the plan's block, or the report was merged.
- A configuration change enacted without the plan update and the pull request that carries it.

**partial:**

- `REL-08` exists with a tag and a released changelog section, and at least one other `met` criterion fails.
- Typical shortfalls: a tag on a commit that is not the week's final production commit; an unprotected tag; a title that does not match the tag; a changelog section that does not link the release or a missing `[Unreleased]`; a body missing the upgrade statement or the `Full changelog` line; a private-only value in the body; a missing `**Released:**`; a `**Checked QRs:**` list that is wrong; a milestone left open; a landed fix missing from the released section.

**missing:**

- No `REL-08` tag or release exists at the cutoff, or the plan has no `#### REL-08` block.

**Guardrails:**

- The version number is the team's SemVer choice; the criteria are the tag's shape, its target, its protection, and the record's completeness.
- A docs-only release is correct: the week may land no product change, and the body's no-product-change statement replaces the product upgrade note.
- `**Checked QRs:**` is built from the testing plan's `Checked` cells and from nothing else: a requirement with a checked test belongs, whatever the row's `Status`, and a requirement with none does not.
- The tag's and the release's timing is read against `ISSUE_CUTOFF`; a tag placed after the cutoff is a caveat in `**Evidence:**` and never repairs the state at the cutoff, and a release page edited after the cutoff is drift.
- The changelog's `[Unreleased]` upkeep through the week is judged here as part of the released section, and the Week 3 to Week 7 released sections are not re-graded.
- The sprint milestone's close is judged from its state and the issues' milestones at the cutoff; an issue moved to `SPRINT-09` with its events is the expected record.
- The release body's exact shape is the team's, and the two required facts are the upgrade action (or that none is needed) and the `Full changelog` line; a body that states them in a different order is correct.
- `REL-07`'s tag, body, and changelog section are Week 7's and are not re-graded.
- A release page that cannot be read is an evidence gap for that check only; the tag and the changelog are still judged.
- The report's claim about the fixes is S17's; this segment judges the release's record and the changelog.

### S16 — Sprint close and retrospective

**Check:**

- `docs/project-plan.md`'s `### SPRINT-08` section and its `**Actual Velocity:**` field.
- The `User Story` issues closed as completed in `SPRINT-08`'s milestone at `ISSUE_CUTOFF`, and their `Story Points`.
- `reports/week-08/sprint-retrospective.md` in the snapshot.
- `reports/week-07/sprint-retrospective.md`'s `## Actions` rows with `Carried: Yes`.
- The pull requests in the Week 8 window that changed the plan and the retrospective.

**met:**

- `### SPRINT-08` carries `**Actual Velocity:**` as a whole number, and it equals the sum of the `Story Points` of the stories closed as completed in `SPRINT-08`'s milestone.
- One sentence after the figure says what moved out of the sprint and to which sprint, or that nothing moved out.
- A sprint that carried only tasks has `0`, and the sentence says the sprint was a task sprint.
- `reports/week-08/sprint-retrospective.md` carries `## What Went Well`, `## What Did Not`, `## Actions`, and `## Carried Actions`.
- `## What Went Well` lists 3 or more items, each one sentence naming what happened.
- `## What Did Not` lists 2 or 3 items with their root causes.
- `## Actions` lists 3 or 4 actions with their `Owner`, `Impact`, `Reason`, and `Carried` flag; the `Owner` is a GitHub username, `Impact` is `High`, `Medium`, or `Low`, and `Carried` is `Yes` or `No`.
- `## Carried Actions` carries each `SPRINT-07` action marked `Carried: Yes`, cites `reports/week-07/sprint-retrospective.md#actions` with the action quoted, and gives each an `Outcome` of `Done`, `Not done`, or `Dropped`.
- Every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.
- An action `Done` or `Dropped` is not re-listed as if it were open.

**What does not count:**

- An `**Actual Velocity:**` copied from `**Planned Velocity:**`, or a figure that does not match the completed stories' points.
- A velocity figure with no sentence on what moved out.
- A retrospective with the four headings but no root causes, or with fewer than the required rows.
- An action with no `Owner`, no `Impact`, no `Reason`, or no `Carried` flag.
- A carried action with no quoted action, no anchor citation, or no `Outcome`.
- A `Not done` action that is not re-listed in `## Actions`, or a `Done` action re-listed as if it were open.
- A `Carried Actions` table with no previous retrospective note when the Week 7 file has actions marked `Carried: Yes`.
- An `Outcome` other than `Done`, `Not done`, or `Dropped`.

**partial:**

- `**Actual Velocity:**` is set and the retrospective exists, and at least one other `met` criterion fails.
- Typical shortfalls: a velocity figure that does not equal the completed stories' points; a missing sentence on what moved out; a missing retrospective section or a row count short of the minimum; a `What Did Not` item with no root cause; an action without its `Owner`, `Impact`, or `Reason`; a carried action missing its citation, its quote, or its `Outcome`; a `Not done` action not re-listed.

**missing:**

- `**Actual Velocity:**` is absent from `### SPRINT-08`, or `reports/week-08/sprint-retrospective.md` is absent.

**Guardrails:**

- Velocity is computed by hand from the stories' `Story Points`, because the single-select field cannot be added up; the segment checks the arithmetic against the completed stories at the cutoff.
- A story is completed when it is closed as completed in `SPRINT-08`'s milestone by `ISSUE_CUTOFF`; a story moved out before the close does not count, and the sentence on what moved out names it.
- A run sprint that carries only results and configuration tasks has `0`, and that is correct.
- The retrospective's prose, its exact action wording, and its root causes' depth are the team's; the criteria are the four sections, the row counts, the columns, and the carried actions' shape.
- The Week 7 retrospective's own shape is not re-graded; this segment judges the actions it marked `Carried: Yes` and what the Week 8 file does with them.
- `**Planned Velocity:**` belongs to S1 and the `REL-08` block to S15; a plan whose figures disagree is reported in the segment that owns the wrong field.
- A retrospective written after the cutoff is a caveat in `**Evidence:**`, not a shortfall, unless the file plainly copies the report's summary.

### S17 — Week report and submission

**Check:**

- `reports/week-08/README.md` in the snapshot, read whole, and every repository file it links.
- `reports/week-08/images/` when the report embeds an image, with `scripts/image_info.py` when a file's size or transparency matters.
- The Moodle PDF under `itpd-assignments-feedback/A8/submissions/<team_dir>/`, read once, for its items, its page count, and its addresses.
- `pdf-info.json` for the repository, the permalink, the SHA, the page count, the recording link, and the permalink-week check.
- `runs_main.json` and `runs_sha.json` for the latest link-check, Markdown-check, `actionlint`, and product-code runs on `main`, and the merged pull requests in the Week 8 window.
- `prs.json` for the merged pull requests the report cites, including one that closed its task issue.
- `scripts/check_snapshot_links.py` for the report's links and anchors.
- The submission procedure's merge and snapshot.
- `docs/threshold-of-success.md` for the goals the `## Threshold review` table names.

**met:**

- `reports/week-08/README.md` exists at the snapshot, is merged into `main`, and the snapshot is taken from that commit.
- The report identifies the week, the project, the team, and the covered scope.
- The summary gives the number of counted sessions, the aggregate completion and ease, the instrumentation comparison, the `QR/QRT` result, the conclusion and its product response, and the key findings and their triage.
- When fewer than three counted sessions ran, the summary gives the number of counted sessions and the declared shortfall instead of the aggregates.
- The summary says what the configuration review found: the `Active` configuration item count, the number of local goals, the first change and its tradeoff, and what the first change keeps.
- The summary links the results, the sanitized session notes, the `QR/QRT`, the task issues, the private repository, the configuration plan, the evaluation, `REL-08`, the retrospective, and the AI usage.
- The summary states the `n=<count>` caveat when there are aggregates, copies no raw participant data, and points at `docs/project-plan.md#quality-requirement-testing-plan` for the rows that are not `Passes`.
- The summary says whether the focus metric has a value yet and what it would need, links `docs/analytics.md` and `docs/observability.md`, and copies no chart or row from either page.
- The report carries a `## Usability test` section with the results summary, the conclusion, the sanitized session links, the SUS and SEQ summary, the instrumentation comparison, the findings, the triage, and the `QR/QRT` result.
- The report carries a `## Configuration management` section immediately after `## Usability test`, with the plan's link, the evaluation's link, the baseline the evaluation reviewed, the `Active` item count, the local goals, the first change and its tradeoff, and what is kept; it links both artifacts and restates neither.
- The report carries a `## Threshold review` section when a goal is still `Open` when the review starts, with one row per open goal in `TOS-nn` order, the columns `Goal`, `Current measure`, `New data can settle it`, and `Proposal`, one status sentence per row, and the reason the team proposed each measure or none.
- The report carries a `## Week 9 handoff` section naming the results, the configuration plan, the evaluation's goal sections and first change, the final repository state, the private repository and recordings folder, the `REL-08` tag, and the evidence the deck will cite.
- The report carries the coverage table with the 18 rows of `assignment-8.md`, in its order, and each artifact cell links its artifact: a repository file by its path from the repository root and the heading anchor when the row names a section, and anything else with descriptive link text.
- A coverage row whose artifact is not public, or whose absence the report explains, says so instead of linking it; when the customer refused publication, the Meeting transcript row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table, and the report carries no separate usability results report.
- The report carries `## Deviations`, naming anything done differently: a session that did not count, fewer than three counted sessions, a `SPRINT-08` testing-plan row moved to `SPRINT-09` with its reason, and a fix that could not land in `REL-08`.
- An item the evaluation could not judge is in its `## What We Could Not Judge` note, not in `## Deviations`; withholding a public-review detail is required by the public-review rule and is not a deviation.
- The report carries a contribution table mapping each member's GitHub username to the work done, using links to their commits, pull requests, or reviews where possible, and the report does not assess an individual.
- The report carries the repository evidence: the merged pull requests for the sessions, the results, the fix, and the configuration work, at least one of which closed its task issue, and the latest green link-check, Markdown-check, `actionlint`, and product-code CI runs on `main`, each by its run URL.
- Each cited run's `conclusion` is `success`, its branch is `main`, and its `head_sha` is an ancestor of the snapshot.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- The report carries `## Privacy`: one line that no private-only material was committed to the product repository, and no participant identity was committed to it.
- The report embeds at most two sanitized screenshots, each in the section that describes it, and one may come from the usability results and one from the configuration evaluation.
- The Moodle PDF carries items 1–9: the project name and the team number; the member table with GitHub username, real name, and university email; the permalink to `reports/week-08/README.md` at the full commit hash; the private usability-data repository URL and the access instructions and the recordings folder URL and the access instructions; the staging and production addresses on the university VM with the university-network note; the staging analytics dashboard and backend addresses and credentials and the staging observability dashboard, backend, and query addresses and credentials; the Sprint Review's recording link or the line saying why there is none; the one-line privacy confirmation; and the transcript appendix when the customer refused publication.
- The PDF's permalink points at `reports/week-08/README.md` at the same full 40-character SHA the snapshot uses; a bare SHA with no repository permalink does not satisfy it.
- The PDF is two pages or fewer, excluding a transcript appendix, and carries no participant identity and no deck.
- The PDF does not repeat the production analytics and observability dashboards, which the Week 6 wrapper carried.
- The report and every repository file it links are merged into `main` at the snapshot; nothing the assignment requires is left on an unmerged pull-request branch.
- The report's own text and the snapshot carry no real address, credential, token, real name, email address, or participant identity.

**What does not count:**

- A report that is not on `main`, or a permalink that names a branch, a tag, a short SHA, or a bare SHA with no URL.
- A report at the snapshot that differs from the merged `main` report the permalink names.
- A summary that copies a metric's value or a testing-plan row instead of linking it, or one that omits the session count, the aggregate or the declared shortfall, the configuration summary, the `n=<count>` caveat, or the configuration plan and evaluation links.
- A summary without the transcript's publication status, without the focus metric's state, or without the Week 9 handoff.
- A report without the `## Usability test` section, without `## Configuration management` immediately after it, without `## Week 9 handoff`, without `## Deviations`, or without the `## Privacy` line.
- A `## Configuration management` section that links an artifact other than the plan and the evaluation, or restates the evaluation's goal sections instead of linking them.
- A `## Threshold review` section missing when a goal is open, with no status sentence, with a settled goal in the table, or with no reason for the proposals.
- A coverage table that omits a row, reorders the rows, or has a row whose link does not resolve; a row that neither links its artifact nor says why it is not public or absent.
- A report without a contribution table, or one that rates or explains a member's contribution.
- A workflow's run list page, a branch's run history, or a job URL as the run link: the report needs the individual green run's URL.
- A green run on a branch other than `main`, a pull-request run, or a run on a commit that is not an ancestor of the snapshot.
- A red, cancelled, or in-progress run cited as green; read `conclusion`, not the run's existence.
- A repository-evidence claim with no merged pull request, with no green `main` run, or with no pull request that closed its task issue.
- A Moodle PDF with a missing item, a missing private-repository or recordings-folder link or access instruction, a missing staging or production address, a missing analytics or observability credential, a missing recording link or its reason, or no member table with university emails.
- A PDF longer than two pages, a deck included, a participant identity in it, or the production dashboards repeated from Week 6.
- A private-only value committed in the repository, including a real address in the report's prose, a participant identity, or a screenshot that carries one.
- A submission that names the wrong week's report, or a permalink that points at `reports/week-07/README.md`.
- More than two screenshots, an unsanitized screenshot, or a screenshot used as decoration rather than evidence.
- A Markdown wrapper instead of the PDF.

**partial:**

- `reports/week-08/README.md` and the Moodle PDF exist, and at least one other `met` criterion fails.
- Typical shortfalls: a report not merged or a permalink with a short or bare SHA; a summary without the session count, the configuration summary, the transcript's status, the focus metric's state, or the Week 9 handoff; a missing `## Usability test` or `## Configuration management` section; a missing coverage row, a reordered row, or a non-resolving link; a missing contribution table or an individual assessment; missing repository evidence or a red `main` run; a missing or thin `## Deviations`; a missing privacy line; a PDF missing an item, over two pages, or carrying a deck; a private-only value in the repository; a wrong-week permalink.

**missing:**

- `reports/week-08/README.md` is absent at the snapshot, or the Moodle PDF is absent.

**Guardrails:**

- The primary index is `reports/week-08/README.md`; a permalink to another week's report is the wrong-week shortfall, and the fetcher's `permalink_week_mismatch` records it.
- The report's prose, its section order beyond the required sections, and its length are the team's; the criteria are the required content, the links, and the evidence.
- The Moodle PDF's real names, emails, and addresses stay in the work directory and are never copied into feedback; a finding is reported by path and kind, such as "the PDF names the private repository but gives no access instructions".
- The run week's report gives the results and the configuration summary; the final reflection and the deck are Week 9's, so their absence is never a shortfall, and the handoff's naming of them is judged in S18.
- A `Passes` claim in the report is not re-judged here; the testing plan's rows are S8 and S14's, and the report's pointer is judged for its existence and its no-copy rule.
- The snapshot's commit time against the deadline is a caveat in `**Evidence:**`, never a status change; a submission after the deadline is the instructor's late-penalty question, not this rubric's.
- A Markdown wrapper instead of a PDF is a shortfall here, and the fetcher's Markdown path records it.
- The coverage row that names why there is no transcript is correct when the customer refused publication; the PDF's appendix is the transcript itself, and the row points at the Moodle submission.
- A coverage row for an artifact the owning segment finds missing says so and is not a second shortfall here; the missing artifact is judged in its own segment.
- The contribution table is evidence of who did what, not a grading of a member; a table with links to merged work is correct even when one member has fewer rows.

### S18 — AI usage and Week 9 handoff

**Check:**

- `reports/week-08/ai-usage.md` in the snapshot.
- The report's AI usage coverage row and its `## Week 9 handoff` section.
- The team's root `AGENTS.md`, for the AI trace it carries and its configuration-plan link.
- The Week 8 commits and pull requests' trailers and messages, when a claim is checkable.
- The AI policy in `course/rules.md`.
- The artifacts the handoff names: the results, the configuration plan, the evaluation, the release tag, the private repository and recordings folder, and the final repository state.

**met:**

- `reports/week-08/ai-usage.md` exists and names each AI tool the team used, what it was used for, and what the team accepted, changed, or rejected from its output, with the reason for each rejection.
- When the team used no AI tools, the file says so in one line, and that line is complete.
- The file says whether an agent was given any usability material; if one was, the file confirms it was given the sanitized note rather than the raw recording or the private notes, and if none was, the file says so.
- The file says whether an agent was given the configuration plan or the evaluation; if one was, it confirms it was given the public, sanitized state.
- The report's coverage table links the file, and the link resolves to the file the report names.
- The file's claims are consistent with the repository's AI trace: a tool it says it used appears in the team's `AGENTS.md` or its commits, and a tool it does not mention is not claimed elsewhere in the submission.
- The file carries no private-only material, no participant identity, no prompt that contains personal data, and no tool output copied wholesale.
- The Week 9 handoff's artifact list is complete: it names the results, the configuration plan, the evaluation's goal sections, its tradeoffs and first change, the final repository state, the private repository and recordings folder, the `REL-08` tag, and the evidence the deck will cite.
- The handoff's claims agree with the state the owning segments judge: a named artifact is present where it is public, and an absent one is reported in its own segment rather than presented as ready.
- The handoff names the private repository and the recordings folder as private-only, and does not link either from the public repository.
- The team's `AGENTS.md` links `docs/configuration-plan.md` in its layout section, and the AI trace the file claims is consistent with it.

**What does not count:**

- A file that names a tool with no use and no disposition.
- A generic "we used AI for coding and writing" with no accepted, changed, or rejected output.
- A rejection with no reason, or an accepted output that no artifact reflects.
- A file copied unchanged from an earlier week with no Week 8 content, including the agent-and-results and agent-and-configuration answers.
- An agent given the raw recording, the private notes, a participant identity, or a private address.
- A coverage row that links a file other than `reports/week-08/ai-usage.md`, or no row at all.
- A file that carries a participant identity, a real name, an address, a credential, or a prompt with personal data.
- A handoff that omits the results, the configuration plan, the evaluation's first change, the final repository state, the private access, the `REL-08` tag, or the deck evidence.
- A handoff that claims an artifact is ready while its owning segment finds it absent.
- A handoff that links a private item, a recording, or an address from the public repository.

**partial:**

- `reports/week-08/ai-usage.md` exists with the tools and their uses and the handoff is written, and at least one other `met` criterion fails.
- Typical shortfalls: one tool with no disposition; a rejection with no reason; the agent-and-results or agent-and-configuration answer missing; the coverage row missing or pointing at another file; an inconsistency with the AI trace; the handoff omitting the tag or the deck evidence.

**missing:**

- `reports/week-08/ai-usage.md` is absent.

**Guardrails:**

- The file's language, its shape, and the number of tools are the team's; the criteria are the tools and their uses, the disposition of the output, the no-AI line when it applies, the two agent answers, the coverage row, and the consistency with the repository's trace.
- The team is never required to have used an AI tool; a one-line no-tools answer is complete and is never a shortfall.
- The course's AI policy requires disclosure and the team's responsibility for what it submits; this segment judges the report, not the amount of AI use.
- The AI trace is the team's `AGENTS.md` and the commit and pull request trailers and messages; the team's `AGENTS.md` is not re-graded on its Week 4 requirements, and its configuration-plan link is S9's.
- The Week 7 AI usage file and its claims are Week 7's and are not re-graded; this segment judges the Week 8 file and the Week 8-specific questions about the results and the configuration material.
- Generated text submitted unchecked, or filler passed off as analysis, is a shortfall where a criterion names it, and it is never a reason to lower a status that the substance already meets.
- The configuration evaluation is about the configuration, not the AI usage; an agent that was given it is reported here, and the evaluation's own judgement is S10's.
- The Week 9 handoff is a report requirement and part of the week's submission; the deck, the reflection, and the final repository state are Week 9's deliverables, so their absence as artifacts is never a shortfall, and the handoff's naming of them is judged here.
- A handoff naming an artifact the owning segment finds absent is not a second shortfall here; the absence is reported in the segment that owns the artifact.

## Semantic feedback

`agent-semantic-feedback.md` is the optional companion file defined in `docs/semantic-feedback-format.md`.
The semantic agent writes it after the compliance report is final.
The compliance agent does not write the companion file.
The semantic agent starts from the report as a map, verifies each claim its verdict rests on against the snapshot at the saved SHA or the saved evidence, and never edits `agent-compliance-feedback.md`.
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

Ask whether the sessions and the results support the conclusion the team draws, and whether the verdict is earned.
Read the counted-session record and the sanitized notes, the results' per-participant table and aggregates with the `n=<count>` caveat, the thematic analysis and the limitations, the instrumentation comparison and the limit it states, the conclusion's product response and its task issues, and the testing plan's verdict against the bar set before the first session.

`thin` when the numbers are present and add up but the conclusion reaches past them: the aggregate is reported for a small sample with the caveat missing, the conclusion commits to a product change that no finding carries, the instrumentation comparison lists events without saying what it could not cover, or the verdict rests on a bar the team moved after the first session.
`not yet adequate` when the results cannot answer the questions at all: aggregates are computed from fewer than three counted sessions, the conclusion answers no research question or claims a verdict the plan does not record, the findings cite no evidence, or the verdict reads from a row whose evidence is another artifact.

### Configuration

Ask whether the configuration plan is a real inventory and whether the evaluation judges the configuration by the goals it serves.
Read the plan's five groups and its `Active` items with their fields and connections, the dropped item in place, the evaluation's baseline, method, local goals with their four fields, its `What We Could Not Judge` note, and its first change.

`thin` when the artifacts exist but the review is item-first: the goals are the project's goals or the plan's group names, a goal section's `Today` is a link list with no purpose, a tradeoff is `none` or `we accept it`, the note says `None` while a private setting was never read, the first change is the largest change rather than where the team would start, or the plan's connections list file names without what breaks.
`not yet adequate` when the plan is not an inventory or the evaluation is not a review: fewer than five groups or eight `Active` items, an item with no owner, purpose, or connections, a missing configuration described as an existing item, an evaluation that grades items against their `What good looks like` instead of judging the set by goal, or a plan or evaluation carrying a private value.

### Plan

Ask whether the run sprint was a forecast the team could steer by, and whether its release leaves Week 9 a clean start.
Read the `SPRINT-08` goal and its planned velocity, the refined backlog and the scheduling of the results and configuration work, the run sprint and the sessions' dates, the risk register and its fallbacks, the changelog and the `REL-08` block, the tag and its protection, the milestone close, the actual velocity, and the retrospective's carried actions.

`thin` when the plan is complete but the sprint would not steer: the goal is a list of the week's deliverables, the planned velocity counts task work, the results or configuration tasks sit outside `SPRINT-08`, a contingency restates its mitigation, the release carries no checked requirement while a row's `Checked` cell says it was, or the retrospective records no cause.
`not yet adequate` when the plan and the record contradict each other: the sprint has no goal or no computed velocity, `REL-08` tags a commit the record does not name, the milestone is closed with work still in it, or the actual velocity cannot be reconciled with the completed stories.

### Customer loop

Ask whether the results review changed the product or the plan, and whether the change reached the artifacts.
Read the Week 7 action points and open questions with their outcomes, the script's first commit against the meeting date, the deployed product and dashboards shown with the results, the permission answers, each decision's `DEC-nnn`, the action points' due weeks, the rework's pull requests, the artifacts they changed, and the testing-plan rows that ran or moved.

`thin` when the review happened but the loop is loose: the meeting repeated the results without asking what to do, a decision is shared rather than specific, no decision changes the results or the plan, the rework is merged but the report still lists it as an action point, a moved row's reason names no consequence, or the Week 7 action points close in the table only.
`not yet adequate` when the review did not show the results or the deployed product, when the recorded decisions cannot be traced to any change, or when `REL-08` names a commit the rework never reached.

### Publication

Ask whether a reader who trusts the public record could find the results, the configuration judgement, and the handoff.
Read the report's summary, its `## Usability test`, `## Configuration management`, `## Threshold review`, and `## Week 9 handoff` sections, the 18 coverage rows, the private repository link and its exclusion, the recordings folder's naming, the results and its session notes, the testing plan's verdict, the `REL-08` record, the retrospective, `ai-usage.md` and its coverage row, the PDF's permalink and private-only items, and the contribution table.

`thin` when the record is complete but the reader still has to ask: the summary restates the results instead of linking them, a coverage row links an index page rather than the artifact, the private repository link is excluded with no reason, the report claims a verdict while the testing plan says `Not verified`, the AI usage file names a tool the repository never shows, or the two-page PDF leaves out an item a reader needs.
`not yet adequate` when the public record contradicts the repository or the PDF: the permalink names a different commit, the report the snapshot merges is not the one the PDF links, a private-only value or a participant identity is in the repository, the coverage table omits a deliverable, or the release and the report disagree about what was released.

### Guardrails

- Ground every claim in an artifact you verified at the saved SHA or a live URL; the compliance report is a map, not evidence.
- Verify the claims your judgement depends on, not every report claim, and do not re-audit the segments.
- Prefer `evidence.sqlite` and the saved dumps; issue, tag, and milestone facts are live, so at most three live `gh` lookups for this file, and record each one.
- Judge the private home, the recordings folder, and the telemetry export from the record, the results, the report, and the PDF; they need authentication, so a failed single access check is not a semantic finding.
- Write `work/<team_dir>/semantic-claims.json` and mark each claim `supported`, `contradicted`, or `unverifiable`; only supported claims feed the semantic file.
- Do not copy an address, a credential, a participant identity, a recording link, a real name, or an email address from the PDF into the semantic file.
- Do not use status vocabulary (`met`, `partial`, `missing`, `unverified`), a grade, a score, a rank, or a cross-team comparison.
- Do not repeat the `## Main issues to fix` list; say what the artifact can and cannot do yet, and what breaks first.
- A `partial` or `missing` segment does not make its dimension `not yet adequate` by itself; judge the artifact, not the count.
- If a judgement contradicts a status, record the conflict in the ledger and return it; the status wins until the operator regrades the report.
  Never edit the report to fit the judgement, and never soften the judgement to fit the status.
- Omit a dimension only when all of its segments are `unverified`; keep at least three.
  If fewer than three dimensions remain, do not write the file.
- The configuration evaluation is a recommendation: judge whether it makes the configuration's cost visible, not whether the team implemented it.
- A declared shortfall in the usability results is a result, not a weakness of the evidence; judge whether the shortfall is declared and the conclusion stays honest.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A8/submissions/`.
   A directory that holds no PDF and no Markdown wrapper is a non-submission, not a rubric shortfall: `Team 5 - TmpTeam_10941_assignsubmission_file` and `Team 8 - Temporary name_10944_assignsubmission_file` hold no submission file, so do not launch a compliance agent for them, create no feedback directory, and report them to the operator.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-08/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A8 "<team_dir>"
   ```

   The fetcher writes `itpd-assignments-feedback/A8/work/<team_dir>/pdf-info.json` with the repository, the permalink, the SHA, the page count, the member tokens, the recording link, and the permalink-week check, and fetches the snapshot into `itpd-assignments-feedback/A8/work/<team_dir>/snapshot/`.
   It reads the PDF's links from its annotations as well as its text, so a permalink shown only as a hyperlink is still found; a bare 40-character SHA is resolved with `gh search commits` and adopted only when one repository matches.
   The primary index is `reports/week-08/README.md`; a permalink to another week's report records `permalink_week_mismatch`, and the fetcher prints a `warn:` line, repeats it in `work/<team_dir>/summary.md`, skips the commit check and the snapshot fetch, and exits 1 with a rerun command.
   Do not grade the wrong-week target; the wrong week is the S17 shortfall, and the operator supplies the right permalink with `uv run python scripts/fetch_team_snapshot.py A8 "<team_dir>" --permalink <url>`, recorded as `permalink_source=operator`, so the snapshot fetched from that permalink governs every file check.
   When the PDF carries no usable permalink, the fetcher stops and names the command; ask the operator for the permalink rather than guessing one, and do not invent a snapshot.
3. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S17 shortfall.
   Call the first value `SNAPSHOT_TIME`, and record the snapshot commit time against the deadline in `**Evidence:**`; it never changes a status.
4. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A8 "<team_dir>" --issue-fields [--issues <n> ...] [--paths <path> ...] [--timelines [<n> ...]]`, which reads `itpd-assignments-feedback/A8/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, `issue-fields.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   A bare `--timelines` collects every issue's timeline at one paginated request per issue; name the issues when only a few need it, and let `--issues` cover the rest.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB in an earlier batch.
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

5. Judge every issue as of `ISSUE_CUTOFF`, `2026-11-21T23:59:59+03:00`, for every team:

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
6. Identify the Week 8 pull requests: every pull request created on or after Friday 13 November 2026, 00:00 Innopolis time, the start of Week 8 in `course/syllabus.md`, and by `ISSUE_CUTOFF`.
   A pull request merged at or before the team's Assignment 7 snapshot commit is part of the Week 7 submission, not a Week 8 pull request.
   Read that SHA from the saved A7 feedback report's `Primary index reviewed` link at `itpd-assignments-feedback/A7/feedback/<team_dir>/agent-compliance-feedback.md`, or from the A7 submission PDF.
   When neither is available, use the team's A7 cutoff as the boundary, `2026-11-15T23:59:59+03:00`, and say in `**Evidence:**` which boundary was used.
   The in-scope pull requests for the sessions, the results, the configuration work, the review rework, the release, and the report's evidence run from the start of Week 8 to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.
7. Gather the pull-request facts below as evidence. These are Week 1 and Week 2 mechanics and are not re-graded in Assignment 8, except where a criterion names them: S2's task-issue shape, S14's rework, and S17's repository-evidence pull request. Record an anomaly in `**Evidence:**` only; never make it a shortfall unless a criterion names it.

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
8. Read the refined backlog and the scheduled tasks from the issue dumps at `ISSUE_CUTOFF`:

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
   - The body projection answers the criteria and the `### Requirements`; read it for each scheduled task and each refined story, and use `issues/<n>.edits.json` when the body changed at the cutoff.
   - The stories and tasks opened on or after `2026-11-13T00:00:00+03:00` are the week's; the open stories and tasks in no milestone are the product backlog, and the ones the team places in `SPRINT-08` and `SPRINT-09` are the ones refinement must have made ready.
   - Every `FR-nnn` and `ADR-nnn` a task's `### Requirements` names must resolve in the snapshot, and a task that serves none says `None: repository upkeep`.
9. Read the usability test's public record and its artifacts at the snapshot:

   ```sh
   find "{TEAM_WORK}/snapshot/docs/usability-tests" -maxdepth 3 -type f | sort
   uv run python scripts/check_snapshot_links.py "{TEAM_WORK}/snapshot" --issue-bodies "{TEAM_WORK}/issues.json"
   ```

   - The file list answers the index, the record, the surveys, the consent, the session template, the session notes, the results, and the images; read the index, the record, the results, and each session note, and each other file as its segment needs it.
   - The link check answers the results' links and anchors and the record's internal anchors; a broken link is the shortfall of the segment that owns the file, and the report's own links are S17's.
   - Check the record's `**Status:**`, `**Run sprint:**`, and the index row against S2 and S4, the counted sessions and their conditions against S3, the results' measures and conclusion against S4, the instrumentation comparison against S5, the findings against S6, the triage against S7, and the verdict and the threshold goal against S8.
   - The private repository link is excluded from the link check; confirm the exclusion in `lychee.toml` and its reason, and do not fetch the private link.
10. Check the sessions and the private home:
    - Compare the counted sessions' dates with the Week 8 window, the team's schedule, and `ISSUE_CUTOFF`; a session that ran in Week 7 is correct when the design and the verification preceded it, and a session after the cutoff is a caveat.
    - Judge the private usability-data repository and the recordings folder from the record, the results, the report, and the PDF; make the single access check of `docs/grading-policy.md#consumer-hosted-media` only when the agent has the access, and record an unverifiable claim as an evidence gap for that check only.
    - Read the sanitized notes and results for a name, an email address, a phone number, an address, or a quote without consent, and report a hit by path and kind.
11. Check the quality requirement and the testing plan together:

    ```sh
    rg -n "^## QR-|^\*\*Status:\*\*|^\*\*Runs at:\*\*|^\*\*Why Manual:\*\*|^\*\*Pass when:\*\*|^### Procedure" "{TEAM_WORK}/snapshot/docs/quality-requirements" | head -n 80
    rg -n "^## Quality Requirement Testing Plan|^\| .*QRT-|^\| .*QR-" "{TEAM_WORK}/snapshot/docs/project-plan.md" | head -n 40
    ```

    - The first projection answers which requirement the test serves, its test's level, status, what it runs at, and its pass criterion; read the requirement's file in full when the verdict depends on it.
    - The second projection answers the testing-plan row's columns, its `Status`, `Checked`, `Planned for sprint`, and `Evidence`; read the table in full when the row's evidence or linkage matters.
    - The new Week 7 requirement is the one with `Interaction Capability` and one of the three sub-characteristics; its `QRT-01` names `UT-01` in `**Runs at:**`, and the testing-plan row is built from that test and no other.
    - `**Checked QRs:**` in S15 is built from the `Checked` cells and from nothing else.
12. Check the configuration plan:

    ```sh
    rg -n "^## |^### CFG-|^\*\*Status:\*\*|^\*\*Type:\*\*|^\*\*Purpose:\*\*|^\*\*Owner:\*\*|^\*\*Where:\*\*|^\*\*Connections:\*\*|^\*\*What good looks like:\*\*|^  - " "{TEAM_WORK}/snapshot/docs/configuration-plan.md" | head -n 120
    rg -n "configuration-plan" "{TEAM_WORK}/snapshot/AGENTS.md"
    ```

    - The first projection answers the groups, the item count, and each item's fields; read the plan in full when an item's connections, purpose, or dropped form matters.
    - Check the `**Reviewed:**` date, the five groups, the 8 `Active` items with at least one per group, the `### CFG-nn` headings, the connection kinds and their failures, and the public-safe rule.
    - Check that the team's `AGENTS.md` links the plan in its layout section.
    - A configuration change the week enacted is read from its pull request and the plan's update in the same pull request.
13. Check the configuration evaluation:
    - Read `reports/week-08/cm-evaluation.md` in full; confirm the section order and the four fields per goal, the method's who, when, baseline, order, and scope, the `What We Could Not Judge` note, and the first change.
    - Confirm the `**Baseline:**` names a tag or commit that exists in `tags.json` or `releases.json`, or in the snapshot's history.
    - Check the evaluation's `CFG-nn` links resolve in the plan, and that a configuration the team does not have is named in words rather than linked.
    - Check the plan and the evaluation for a secret value, a private address, or a credential.
14. Check the release against the tag:
    - Read `releases.json` for the tag names and dates; read the release title and body from the rendered release page or the raw `gh api "repos/$REPO/releases?per_page=100"` response, because the collector's dump omits them; read `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-08` block, and `reports/week-08/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path.
    - Compare the merge time of those three pull requests with the tag; each must be later than, or at, the tag, and the changelog's dated section, the plan's block, and the report must be merged in that order. Use the tag's push time when it can be read; otherwise use the tag's commit date and say so in `**Evidence:**`.
    - Read `gh api "repos/$REPO/rulesets"` and each tag ruleset for the protection that covers tag pushes.
    - Build `**Checked QRs:**` from the testing plan's `Checked` cells: a requirement belongs when at least one of its tests has `SPRINT-08` there, whatever the row's `Status`.
    - Read `SPRINT-08`'s milestone state and the issues rescheduled out of it.
15. Check the sprint close from the issue dumps and the plan:
    - From `issues.json`, take the stories closed as completed at `ISSUE_CUTOFF` in `SPRINT-08`'s milestone and their `Story Points` from `issue-fields.json`; add them by hand and compare the total with `**Actual Velocity:**`.
    - Read `reports/week-08/sprint-retrospective.md`'s four sections, their columns, and their row counts, and check each `## Carried Actions` row against `reports/week-07/sprint-retrospective.md`'s `Carried: Yes` actions.
    - Confirm every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.
16. Check the Sprint Review against the record and the plan:
    - Read `reports/week-08/meeting-script.md`, `meeting-report.md`, and `meeting-transcript.md` at the snapshot, and the `DEC-nnn` entries the report cites.
    - Compare the meeting date with the Week 8 window and the cutoff; a meeting on 20 or 21 November is a caveat, not a shortfall, and a meeting after the cutoff is a shortfall.
    - Find the script's first commit and the report's, and compare them with the meeting date; a script written after the meeting is S13's shortfall.
    - Read the report's action points' due weeks: at least two due after Week 8, at least one in Week 9; an action due inside Week 8 is a shortfall.
    - Read the Week 7 report's action points and open questions and the Week 8 report's `## Previous action points` and `## Previous open questions` for S12.
    - Check the report's summary and `## Usability test` against the results and the testing plan: a claim the results do not support is S13's.
17. Check the private usability-data repository's declaration against the PDF:

    ```console
    gh repo view "<organization>/<repo>-usability-data" --json isPrivate,visibility 2>&1 | head -n 5
    ```

    - The call answers whether the repository exists and is private when the agent has access; when it fails, judge the declaration in the record, the results, the report, and the PDF, and record the unverifiable access as an evidence gap for that check only.
    - The PDF's items 4, 5, 6, 7, 8, and 9 carry the private repository and the recordings folder's links and access, the staging and production addresses, the staging telemetry credentials, the recording link, the privacy line, and the transcript; read them once here and in S17, and never copy a value into feedback.
18. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A8 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A8/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/usability-tests/ut-01/sessions/P-01.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    Its rules do not include participant identity or IPv4 addresses, so check the public usability files and the configuration plan and evaluation for a participant name, a raw note, a private address, or a credential; report a hit by path and kind.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in the submission and outside the meeting artifacts, `.env` files, and the addresses and credentials from the PDF searched over the snapshot.
    Report each finding by path and kind only, with the number of hits per file.
19. Grade each of the 18 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-08/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the private usability-data repository's link and access, the recordings folder's link and access, the staging and production addresses with the network note, the staging analytics and observability addresses and credentials, the Sprint Review's recording link, and a transcript the customer refused to publish.
- Never copy a real name, an email address, a dashboard or backend address, a credential, or a participant identity from the PDF into feedback; refer to people by GitHub username, to the customer as `Customer`, to a participant by `P-nn`, and to an address or credential by the placeholder or by the kind of finding.
- The participant codes are public; the participant identity, the consent records, the raw notes, the identity mapping, and the test's telemetry export are private and are never copied from the private repository or the PDF.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 to Week 7 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the research content, the vision, the assumptions, the issue forms and fields, the project's table view, the risk register's older risks, the threshold of success, the plan's Week 3 to Week 7 parts, the Definition of Done, `CONTRIBUTING.md`, `docs/setup.md`, the documentation site, the functional requirements, the architecture document, the ADR records, the glossary's older terms, the team's `AGENTS.md`'s Week 4 requirements, `REL-03` to `REL-07`, the usability test's design and instrumentation, and the Week 1 to Week 7 meeting artifacts, reports, and retrospectives.
- Week 1 to Week 7 artifacts are checked only where Assignment 8 requires it: the plan's `### SPRINT-08` and `### SPRINT-09` (S1), the stories, task issues, and backlog refinement (S2), the `UT-01` record, the sessions, the surveys, the consent, and the instrumentation (S2, S3, S5, and S8), the quality requirements index and testing plan (S8 and S14), `docs/glossary.md`'s older terms and `docs/risks.md`'s older risks (S11), the Week 7 meeting report's action points and open questions (S12), the Week 7 retrospective's `Carried: Yes` actions (S16), `CHANGELOG.md`'s released section and `[Unreleased]` (S15), the link check and the Markdown check, `actionlint`, and the product-code CI green on `main` (S17), and the `SPRINT-08` milestone and the issues in it (S2, S15, and S16).
- When a Week 7 artifact Assignment 8 builds on is absent, such as a Week 7 meeting report with no action points, a Week 7 retrospective with no file, or a `UT-01` record with no design, judge the Assignment 8 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 7 absence again.
- A Week 7 report with no action point due by Week 8 or no open question makes `None` in the matching `## Previous` section correct, and it is never a shortfall.
- The Week 7 deadline does not move Week 8: the A7 cutoff `2026-11-15T23:59:59+03:00` bounds the Week 7 submission only, and the Week 8 cutoff stays `2026-11-21T23:59:59+03:00` for every team.
- The Week 8 Saturday deadline is the submission's date, not the sprint's class-week end: `SPRINT-08`'s `**Due:**` and its GitHub milestone are `2026-11-21`, while the class week ends on 19 November.
- The sessions may have run in Week 7: a session that ran before the Week 8 window is correct when the design was written and the instrumentation verified before it, and its notes, results, findings, and verdict are written this week.
- Fewer than three counted sessions is a declared shortfall, not a missing submission: the record stays `Planned`, `results.md` carries the qualitative record without aggregates, the report declares the shortfall, and a `QR/QRT` row stays `Not verified` or moves to `SPRINT-09` with a reason.
- A declared shortfall is never presented as a result: a report that claims an aggregate the sessions cannot support is the shortfall, and a report that declares the shortfall and claims no result is correct.
- The configuration evaluation is the review's deliverable and its recommendation: no implementation, task issue, or scheduled work is required, and a change the team enacts is extra evidence rather than a requirement.
- A configuration the team does not have is named in words in the evaluation and carries no `CFG-nn`; a plan that invents the configuration is worse than a short one.
- The private usability-data repository and the recordings folder are outside the product repository; their absence from it is correct, and the product repository links the private repository and names the recordings folder without linking it.
- Week 8's pitch deck, final reflection, and final repository state are Week 9's deliverables, so their absence as artifacts is never a shortfall; the Week 9 handoff's naming of them is a submission requirement, and the handoff's artifacts are judged where they are public.
- A commit, comment, tag, deploy, or edit after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff; it is a shortfall only where a criterion names the cutoff, such as S15's tag date.
- The product code, its tests, the staging deployment, and the environments are Week 5 deliverables: their absence is never excused as "not this week's" where the sessions' staging environment or the telemetry the comparison reads needs them.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- A submission after the deadline is the instructor's late-penalty question, not this rubric's; read the snapshot's commit time against the deadline in `**Evidence:**` only.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, usability test, usability test task, usability test record, participant, participant profile, usability session, usability finding, consent, recording, `SUS`, `SEQ`, private usability-data repository, recordings folder, measure, metric, statistic, instrument, instrumentation, results, conclusions, triage, configuration, configuration management, configuration review, configuration plan, configuration item, configuration evaluation, baseline, upkeep, reproducible build, dependency pinning, secret, context window, agent instruction, `CFG-nn`, sprint, sprint planning, product backlog, product backlog refinement, sprint backlog, sprint review, sprint milestone, plan milestone, story points, velocity, retrospective, quality requirement, quality requirements index, quality requirement test, quality requirement testing plan, evidence, threshold of success, risk register, glossary, functional requirement, architectural decision record, release, changelog, weekly report, weekly public report, private-only artifact, deviation, action point, open question, decision, and telemetry.

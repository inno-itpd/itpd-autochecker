# Assignment 6 Grading Criteria

This rubric is for the compliance agent that reviews ITPD Assignment 6 team submissions.
ITPD assigns no points: each segment gets one status, `met`, `partial`, `missing`, or `unverified`, and an `Evidence gaps: yes|no` flag, per `docs/compliance-feedback-format.md`.
The instructor assigns the grade from the statuses and the evidence, so this rubric never proposes a grade, a score, or a late penalty.
The shared rules live in `docs/grading-policy.md`: evidence states, verified absence, blocked and conflicting artifacts, snapshot resolution, live GitHub evidence through `gh api`, the single access check for consumer-hosted media, privacy, undeclared deviations, and rule applicability by `Since:` marker.
This file states only what is specific to Assignment 6 and does not repeat those rules.

## Authoritative sources

All paths are in the course-materials submodule, pinned at itpd commit `312fb2f62fd3f8260efe47b8bec82bc8ba24248d`.
If the checked-out submodule differs from that commit, read each file with `git -C A6/itpd show 312fb2f62fd3f8260efe47b8bec82bc8ba24248d:<path>`.

- `A6/itpd/assignments/assignment-6.md` — the student-facing brief: Parts 1–16, What Good Looks Like, the repository report contents, the Moodle report contents, the submission procedure, and the checklist.
- `A6/itpd/requirements/general-requirements.md` — artifact terms, the `reports/week-NN/` vs `docs/` split, the identifier rules including the `SLI-nn` family, how an analytics metric is cited, and how a later week cites an earlier action point.
- `A6/itpd/requirements/planning-requirements.md` — `docs/project-plan.md` with `## Milestones`, `## Sprints`, `## Releases`, and `## Quality Requirement Testing Plan`; the `**Due:**`, `**Sprints:**`, `**Advances:**`, `**Planned Velocity:**`, and `**Actual Velocity:**` fields; the `REL-nn` block with `**Released:**` and `**Checked QRs:**`; and the threshold review of each open goal.
- `A6/itpd/requirements/sprint-ceremonies-requirements.md` — sprint planning, product backlog refinement, estimation, the Sprint Review, and the retrospective with its four sections, row counts, and columns.
- `A6/itpd/requirements/issue-tracking-requirements.md` — scheduling as the sprint's GitHub milestone, the `Responsible` and `Accountable` fields, the matching assignees, and the public GitHub project.
- `A6/itpd/requirements/user-stories-requirements.md` — the story issue's `User Story` type, its `MoSCoW` value, its `VP-nn` and `### Specified by` links, and its checkbox `AC-nn` criteria.
- `A6/itpd/requirements/task-issues-requirements.md` — the `Task` issue type, its `### Requirements`, and the pull request that closes it.
- `A6/itpd/requirements/quality-requirements-requirements.md` — the `QR-nn` file, the six-part scenario, the `## QRT-nn` section and its fields, the four levels and the environment each runs in, the Week 6 rules that make a runtime test name an `Active` `SLI-nn`, the index, and the matrix.
- `A6/itpd/requirements/functional-requirements-requirements.md` — the `FR-nnn` file that owns a capability's behavior, which a story's `### Specified by` and a feature entry link.
- `A6/itpd/requirements/architecture-requirements.md` — `docs/architecture/README.md`, the container view, the Week 6 rule that a self-hosted telemetry backend is an external system rather than a container, and the ADR index.
- `A6/itpd/requirements/adr-requirements.md` — the `ADR-nnn` record a story and a feature entry link, its `**Addresses:**` list, and its body sections.
- `A6/itpd/requirements/product-vision-requirements.md` — the vision's boundary and system context, which the Week 6 backends do not join.
- `A6/itpd/requirements/customer-meetings-requirements.md` — the weekly meeting as the Sprint Review, the Week 6 rule that it shows the four dashboards and the observability test's result, the script, the report's `## Previous action points` and `## Previous open questions`, and the transcript.
- `A6/itpd/requirements/decisions-requirements.md` — the `DEC-nnn` entry, its `**Source:**`, and what cites it.
- `A6/itpd/requirements/releases-requirements.md` — `CHANGELOG.md`, Semantic Versioning, tags and their protection, the release title, and the upgrade note that ends with the `Full changelog` line.
- `A6/itpd/requirements/weekly-report-requirements.md` — the weekly public report, its summary and `## Threshold review` section, the coverage table, the AI usage report, declaring deviations, and the Moodle PDF.
- `A6/itpd/requirements/visibility-requirements.md` — what is public, what is Moodle only including the four dashboards and the two backends, screenshot sanitization, and telemetry and personal data.
- `A6/itpd/requirements/glossary-requirements.md` — `docs/glossary.md` and the terms a feature entry links at first use.
- `A6/itpd/requirements/agent-instructions-requirements.md` — the team's root `AGENTS.md`, read as an AI trace.
- `A6/itpd/requirements/pull-requests-requirements.md` — every change through a pull request, one change per pull request, review and approval, and closing a task issue.
- `A6/itpd/requirements/repository-requirements.md` — the link check, the Markdown check, `actionlint`, the five product-code checks, the four environments, the two telemetry pipelines, and the manual deployment on the university VM.
- `A6/itpd/requirements/definition-of-done-requirements.md` — `docs/definition-of-done.md` and its `## Pull Request` list.
- `A6/itpd/requirements/minimum-usable-product-requirements.md` — the core task the deployed telemetry work exercises.
- `A6/itpd/requirements/features-requirements.md` — `docs/features.md`, its flat capability entries, the `**Stories:**`, `**Behavior:**`, and `**Decisions:**` links, and the Week 6 rule that an internal capability is a feature.
- `A6/itpd/requirements/analytics-requirements.md` — `docs/analytics.md`: the focus metric, the metric tree, the metric sections, the event table, the analytics pipeline and its environment scopes, the dashboards, and the collected data.
- `A6/itpd/requirements/observability-requirements.md` — `docs/observability.md`: the signals, the `SLI-nn` sections and their fields, the observability pipeline and its environment scopes, the dashboards, and the collected data.
- `A6/itpd/guides/analytics-and-observability.md` — the method for the metric tree, the events, the two telemetry pipelines, the four dashboards, the `SLI`s, and the threshold review.
- `A6/itpd/guides/quality-requirement-tests.md` — the method for turning a response measure into a test, choosing its level, reading an `SLI`, and recording its row.
- `A6/itpd/guides/deployment-and-environments.md` — the method for the environment map, the VM, the configuration, the staging and production deploys, the verification, and the rollback.
- `A6/itpd/guides/quality-and-architecture.md` — the method for the quality requirements, the container view, and the feature page.
- `A6/itpd/guides/planning-and-tracking.md` — the method for the milestones, the sprints, the release order, the release body, the retrospective, and the threshold review.
- `A6/itpd/guides/validating-with-the-customer.md` — the method for the meeting's target, questions, agenda, roles, and tracing what changed.
- `A6/itpd/course/rules.md` — the course contract, the AI policy, the submission channel, and the deadline policy including the Week 6 Sunday.
- `A6/itpd/course/syllabus.md` — the Week 6 objectives and deliverables, the Sunday 8 November deadline, and the Week 7 deadline.
- `A6/itpd/AGENTS.md` — course terminology and the `docs/` destination map, which puts `docs/analytics.md` and `docs/observability.md` in Week 6.

Apply every rule marked `**Since: W1**`, `**Since: W2**`, `**Since: W3**`, `**Since: W4**`, `**Since: W5**`, or `**Since: W6**`.
No rule in the pinned materials carries a `**Since: W7**` or later marker, so nothing is excluded by a later marker; the Week 7 usability testing, the Week 8 configuration management, and the Week 7 pitch deck are not Assignment 6 deliverables, and their absence is never a shortfall.

## Assignment parameters

- Report title: `# Assignment 6 Feedback Report`
- Week: `W6`
- Course materials: `A6/itpd` at `312fb2f62fd3f8260efe47b8bec82bc8ba24248d`
- Primary index artifact: `reports/week-06/README.md` at the snapshot, as named in Assignment Report In The Repository and in Moodle item 3 of `assignment-6.md`.
- Week window: from Friday 30 October 2026, 00:00 Innopolis time, `2026-10-30T00:00:00+03:00`.
  The syllabus gives the Week 6 class week as 30 October to 5 November 2026; the submission is due on the following Sunday, and the window runs from that Friday to `ISSUE_CUTOFF`.
- Soft deadline: none; `course/rules.md` gives every group submission from Week 4 to Week 9 a single hard deadline, and `course/syllabus.md` and `assignments/assignment-6.md` state the same date.
- Hard deadline: Sunday 8 November 2026, 23:59, as the pinned `course/syllabus.md`, `course/rules.md`, and `assignments/assignment-6.md` state it. Week 6 is the one exception to the Week 4 to Week 9 Saturday rule: the syllabus deadline is Sunday 8 November 2026.
- No per-team deadline override exists for Week 6: every team's deadline is Sunday 8 November 2026, 23:59.
- `ISSUE_CUTOFF`: `2026-11-08T23:59:59+03:00` for every team.
  Every later reference to `ISSUE_CUTOFF` means that cutoff, and `**Evidence:**` states the cutoff used.
- Hard deadline of the following week: Saturday 14 November 2026, 23:59, the deadline the Week 7 syllabus block gives and the due date `SPRINT-07`'s GitHub milestone carries.
  A Week 5 action point due in Week 6 carries a due date from 30 October through 8 November 2026, the Week 6 class week plus the submission deadline; a due date from 9 November on belongs to Week 7 and is outside the meeting's Week 6 window.
- The time zone is not stated in the materials; read every deadline as Innopolis time (UTC+3).
- Submission inputs: the Moodle PDF under `itpd-assignments-feedback/A6/submissions/<team_dir>/`; there is no ZIP, so the snapshot upload to Moodle is not judged.
  The snapshot is fetched from GitHub at the permalink SHA into `itpd-assignments-feedback/A6/work/<team_dir>/snapshot/`.
- Live artifact families: the story and task issues with their types, field values, comments, timelines, and edit history; repository labels; pull requests with their reviews, files, and closing references; Actions runs of the link check, the Markdown check, `actionlint`, and the product code; the repository's tags and releases; the sprint GitHub milestones; the organization's GitHub project; the four telemetry dashboards and the two backends, read only through the sanitized screenshots and the Moodle PDF because they sit on the university network; and the Moodle recording link.
- Story and task issues, their types, their field values, their milestones, and the labels are not in the snapshot, so they are read live and judged as of `ISSUE_CUTOFF`, per [procedure step 6](#assignment-specific-procedure-deltas).
  An issue opened after the snapshot commit but by `ISSUE_CUTOFF` counts.
- Tags, releases, milestones, and the GitHub project are read live and judged as of `ISSUE_CUTOFF` too.
  An issue-field value has no history in the API: read the current value and read the issue's timeline for what changed after `ISSUE_CUTOFF`, and say so in `**Evidence:**` when the timeline cannot settle it.
- The four dashboards and the two telemetry backends are on the university network.
  Judge them from the sanitized screenshots in `reports/week-06/images/`, the deployment runbook, the weekly report, and the Moodle PDF's addresses and credentials; make the single access check of `docs/grading-policy.md#consumer-hosted-media` only when the agent can reach the university network.

The segments, in order:

- S1: Sprint plan and milestones
- S2: New stories and backlog refinement
- S3: Analytics plan and metric tree
- S4: Events and instrumentation
- S5: Analytics backend and dashboards
- S6: Observability plan and SLIs
- S7: Observability backend and dashboards
- S8: ADRs and container view
- S9: Feature documentation
- S10: Observability requirement and test
- S11: Threshold review
- S12: Week 5 action points and open questions
- S13: Customer validation of the telemetry
- S14: Redeploy and retest after same-week rework
- S15: REL-06 release
- S16: Sprint close and retrospective
- S17: Week report and submission
- S18: AI usage and honesty

### Segment overview

Every checklist item and every coverage-table row, or named part of a row, of `assignment-6.md` maps to exactly one segment, and a shortfall is reported only in the segment that owns it.

| Segment | Covers |
|---------|--------|
| S1: Sprint plan and milestones | Part 1 items 1, 2, and 8; the goal, planned-velocity, and milestone part of the coverage row Sprint plan and new stories; the plan milestones due in `SPRINT-06` through `SPRINT-09`; the checklist item "`SPRINT-06` planned with its goal, its `**Due:**` field, its `**Sprint Backlog:**` link, and its `**Planned Velocity:**`" |
| S2: New stories and backlog refinement | Part 1 items 3–7; the story and task-issue part of the coverage row Sprint plan and new stories; the checklist items "One `US-nn` for the product analyst and one for the system operator, each with the end-user `VP-nn` it serves, its `### Specified by`, its `MoSCoW`, `Story Points`, `Responsible`, `Accountable`, and two assignees, both scheduled in `SPRINT-06`", "The next two sprints' worth of the product backlog refined, with the `Story Points` on each and no sprint milestone", and "The task issues for the two pipelines, the four dashboards, and the observability test, each with its `### Requirements`, scheduled in `SPRINT-06`" |
| S3: Analytics plan and metric tree | Part 2; the Analytics plan part of the coverage row Analytics plan; the checklist items "`docs/analytics.md` with the focus metric traced to its `VP-nn`, the seven criteria, one rejected vanity metric, the counter-metric at L1, the L1 and L2 inputs, and the tree" and "A `###` section for every node in the tree, each with its `**Definition:**`, `**Source:**`, and `**Query:**`, and one metric computed by its query named on the page". The plan's link from `docs/deployment.md` is judged here with the page; the report's coverage row is S17's |
| S4: Events and instrumentation | Part 3; the Events and instrumentation and the analytics functional-requirement part of the coverage row Functional requirements; the checklist items "The event table with its four columns, its naming convention, `source` on every event, no personal data, and the core task covered end to end", "The product instrumented, the staging test event tagged `source=smoke`, the staging dashboard's event list showing it, and the staging chart excluding it", and "The analytics functional requirement written with the next free `FR-nnn`, with its behavior, its criteria, and its index row". The dashboard itself is S5's |
| S5: Analytics backend and dashboards | Part 4; the Analytics dashboards part of the coverage row Analytics dashboards; the checklist items "The analytics backend on the university network, with a staging and a production environment scope, each with its own credential", and "A dashboard in each environment scope, with at least one chart for the focus metric or its L1 input, running the query recorded in the page". The pipeline's runbook section is shared with S7: S5 owns the analytics half, S7 the observability half |
| S6: Observability plan and SLIs | Part 5; the Observability plan and `SLI`s part of the coverage row Observability plan and `SLI`s; the checklist items "`docs/observability.md` with the signals and the `SLI-nn` sections, each with its definition, unit, window, source, query, and status", "The demonstrated `SLI` is `Active` and names the labels that identify the request, the route, and the failure", and "The observability functional requirement written with the next free `FR-nnn`, with its behavior, its criteria, and its index row" |
| S7: Observability backend and dashboards | Part 6; the Observability dashboards part of the coverage row Observability dashboards; the checklist item "OpenObserve on the university network with a staging and a production environment scope, each with a dashboard whose chart names its `SLI`". The shared `docs/deployment.md` telemetry section is split with S5 |
| S8: ADRs and container view | Part 7; the ADRs and container view coverage row; the checklist items "The analytics and observability ADRs, each addressing its `FR-nnn` or `QR-nn`, with its `**Containers:**` named, and both in the ADR index" and "The container view showing the two backends as external systems with the protocol on each arrow, the view's sentence and the legend's line that the team self-hosts them and does not build them, the container set and the context diagram unchanged, and no new view" |
| S9: Feature documentation | Part 8; the Feature documentation coverage row; the checklist items "`docs/features.md` with an entry for each internal capability, linking its story, its `FR-nnn`, and its `ADR-nnn`, and no dashboard address" and "The week's terms in `docs/glossary.md`, linked at first use in the two entries" |
| S10: Observability requirement and test | Part 9; the Observability requirement and Runtime test re-run coverage rows; the checklist items "The new `QR-nn` with its `Maintainability` / `Analysability` pair, `High` business importance, and its diagnosability scenario", "The new requirement's `QRT-01` at `deployed`, naming the staging deployment, `$OPENOBSERVE_URL`, and the demonstrated `SLI-nn` in `**Runs at:**`, with its procedure, its script, and its pass criterion", "The test run against staging, its row `Passes` with `Checked` in `SPRINT-06`, and its evidence linked", "Each `SPRINT-06` testing-plan row run or moved to `SPRINT-07` with a reason, the optional re-run recorded when it was run, and the moves declared in the report", and "The new requirement's row in the index and the matrix, and the index linking the testing plan once" |
| S11: Threshold review | Part 10; the Threshold review coverage row; the checklist item "Each goal that is `Open` when the review starts, as one row of the review table with its current measure and whether the new data can settle it, one status sentence per row after the table, each settled goal's `**Outcome:**` in `docs/threshold-of-success.md`, a goal due later left `Open`, and the `## Threshold review` in the report" |
| S12: Week 5 action points and open questions | Part 11; the Week 5 action points and Week 5 open questions coverage rows; the checklist item "Each Week 5 action point's outcome in `## Previous action points`, and each Week 5 open question answered or carried forward in `## Previous open questions`" |
| S13: Customer validation of the telemetry | Part 12; the Meeting script, Meeting transcript, and Customer validation coverage rows; the checklist items "`reports/week-06/meeting-script.md`", "`reports/week-06/meeting-report.md`, with the dashboards, the tests' results, the `SLI` each runtime test read, the threshold proposal, a `DEC-nnn` for any change, and 2 or more action points due in Week 7", and "`reports/week-06/meeting-transcript.md`, if the meeting was recorded or held in writing" |
| S14: Redeploy and retest after same-week rework | Part 13; the checklist item "Any same-week rework merged, redeployed to staging, retested, redeployed to production, and verified, or deferred to `SPRINT-07` with the reviewed commit released"; whether the released commit is the one the staging test ran and production served after the rework |
| S15: REL-06 release | Part 14; the `REL-06` coverage row; the checklist item "`REL-06` tagged on the final production commit, with the changelog's `[0.6.0]` section, the upgrade note ending with the `Full changelog` line, the plan's `REL-06` block, and the sprint milestone closed". The plan's testing-plan rows are S10's; the changelog's `[Unreleased]` upkeep through the week is judged here as part of the released section |
| S16: Sprint close and retrospective | Part 15; the Sprint retrospective coverage row and the actual-velocity part of the Sprint plan and new stories row; the checklist item "`**Actual Velocity:**` set in `### SPRINT-06`, and `reports/week-06/sprint-retrospective.md` with its four sections and its carried actions" |
| S17: Week report and submission | Assignment Report In The Repository items 1–6; Assignment Report On Moodle items 1–8; the Submission Procedure; the 20 coverage rows judged only as rows that exist and link; the checklist items "`reports/week-06/README.md` with the summary, the threshold review, the four screenshots, and the coverage rows", "Everything merged into `main`, with the permalink and the snapshot taken from that commit", and "PDF ready, the permalink opened in a browser at the full commit hash, the four dashboards' addresses and credentials in it, the two backends' addresses and all credentials in it, and the product's staging and production addresses in it"; plus the report's summary, contribution table, repository evidence, `## Deviations`, and privacy line. The underlying artifacts are judged in S1 to S16 and S18 |
| S18: AI usage and honesty | Part 16; the AI usage coverage row; the checklist item "`reports/week-06/ai-usage.md`"; the AI Usage Report rules for Week 6 text |

The coverage-table rows map to the segment that judges the artifact in the row.
Whether the table has each row, and whether each row links, is judged in S17.
S14 owns the deploy-and-retest sequence and the identity of the released commit; S15 owns the tag, its protection, the release body, the changelog, the plan's block, and the milestone close, so a tag placed on a commit the sequence does not produce is reported in S14 and its own record in S15 is judged there.

## Status guide

Use the status vocabulary of `docs/compliance-feedback-format.md` and the evidence states of `docs/grading-policy.md`.
A segment is `met` only when every `met` criterion below holds on verified evidence.
A segment is `partial` when its core artifact exists and at least one verified shortfall remains.
A segment is `missing` when the `missing` criterion below holds.
A segment is `unverified` when its core evidence could not be read, such as S15 when the tags and releases cannot be read at all, or S5 when neither the runbook, the screenshot, nor the Moodle PDF settles that a backend ran.
Recommended items and the What Good Looks Like points are quality notes for the instructor, and they never cause a shortfall unless they coincide with a Required rule.

### S1 — Sprint plan and milestones

**Check:**

- `docs/project-plan.md` in the snapshot, its `## Milestones` and `### SPRINT-06` sections, and the path history of the file for when each field was written.
- The repository's GitHub milestones: `milestones.json` for the titles and due dates, and the raw `gh api "repos/$REPO/milestones?state=all&per_page=100"` call at procedure step 12 for each milestone's state.
- The `User Story` issues in `SPRINT-06`'s milestone and their `Story Points`, from `issue-fields.json` or the REST `issue_field_values`.
- Each `User Story`'s `milestoned` and `demilestoned` events, from `issues/<n>.timeline.json` or the `issue_events` table filtered to the planning time, for the stories the milestone held when the sprint was planned.
- The pull requests in the Week 6 window that touch `docs/project-plan.md`, for when `**Planned Velocity:**` and the milestone fields were written.
- The plan milestone due in `SPRINT-06`, when the plan has one, and its description.

**met:**

- `### SPRINT-06` opens with the sprint's goal in one sentence, stated as a result rather than as a list of tasks, and it replaces the provisional goal the section carried before planning.
- Under the goal, `### SPRINT-06` carries `**Due:**`, `**Sprint Backlog:**`, and `**Planned Velocity:**`, in that order, as a bulleted list.
- `**Due:**` is `2026-11-08`, the Sunday the Week 6 submission is due.
- `**Sprint Backlog:**` links the `SPRINT-06` GitHub milestone, and the link resolves to the milestone whose title begins `SPRINT-06:`.
- `**Planned Velocity:**` is a whole number, and it equals the sum of the `Story Points` of the stories the milestone held when the sprint was planned, from its `milestoned` and `demilestoned` events where they exist and from its current stories otherwise; a story added mid-sprint does not change the planned figure.
- When a plan milestone is due in `SPRINT-06`, its description includes the telemetry increment the sprint delivers and states it as the increment rather than only as the team's task list.
  When no plan milestone is due in `SPRINT-06`, `### SPRINT-06`'s goal itself states the telemetry increment, and no new milestone is required.
- The GitHub milestones `SPRINT-06`, `SPRINT-07`, `SPRINT-08`, and `SPRINT-09` exist, each titled `SPRINT-nn: <focus>` with its own number, and due `2026-11-08`, `2026-11-14`, `2026-11-21`, and `2026-11-28`.
- `SPRINT-07`, `SPRINT-08`, and `SPRINT-09` are open at `ISSUE_CUTOFF`; `SPRINT-06`'s state belongs to S15.
- The plan copies no issue list into the file, and no `## Milestones` entry stands for a GitHub milestone.

**What does not count:**

- A prose sentence such as "we planned about 8 points", or a rounded total, as `**Planned Velocity:**`.
- The current story set when the milestone gained or lost a story after planning: the sum must use the stories the milestone held at planning, from `milestoned`/`demilestoned` events.
- A figure copied from `SPRINT-05` or from the week report instead of the sum of the planned stories' `Story Points`.
- A sprint milestone due `2026-11-07` or `2026-11-05`: the Saturday rule was replaced for Week 6 by the Sunday `2026-11-08`, and 5 November is the class week's last class day.
- A plan milestone due in `SPRINT-06` whose description lists tasks without naming the telemetry increment, such as "deploy OpenPanel, build four dashboards, and write the test".
- A new plan milestone invented only to satisfy the week: the assignment requires none, so its absence is never a shortfall.

**partial:**

- `docs/project-plan.md` has `### SPRINT-06` and a `## Milestones` section, and at least one other `met` criterion fails.
- Typical shortfalls: a provisional goal left in `SPRINT-06`; `**Planned Velocity:**` absent, not a whole number, or not the planning-time sum; a due date other than `2026-11-08`; a `**Sprint Backlog:**` link that does not resolve or points at another sprint's milestone; a plan milestone due in `SPRINT-06` whose description does not include the telemetry increment; a field missing or out of order; a missing or mistitled sprint milestone; a sprint milestone due on a date other than its deadline; a future sprint's milestone closed early.

**missing:**

- `docs/project-plan.md` is absent at the snapshot, or it has no `### SPRINT-06` section with a goal.

**Guardrails:**

- A sprint's due date is judged against `course/syllabus.md`: Week 6 is Sunday 8 November 2026 with no per-team override, and Week 7 is Saturday 14 November 2026.
- The `## Milestones` entries are **plan milestones**, which live only in the plan and carry no exit check of their own; the `SPRINT-nn` GitHub milestones are the **sprint milestones**, and the two are never the same artifact.
- The earlier plan milestones' own fields and runs were Week 3's and Week 4's and are not re-graded, and their due dates are not re-dated here; this segment judges `### SPRINT-06`'s plan fields, the description of a plan milestone due in `SPRINT-06` when the plan has one, and the four sprint milestones.
- `SPRINT-05`'s goal, fields, and sprint milestone were Week 5's and are not re-graded; a `SPRINT-05` milestone still open at the cutoff is Week 5's release question, not this segment's.
- `**Actual Velocity:**` belongs to S16, the `#### REL-06` block to S15, and the stories' `Story Points` and assignees to S2.
- A milestone section written after the sprint started is a caveat in `**Evidence:**`, never a shortfall, unless the goal or the increment was plainly written from what happened.
- Whether `**Planned Velocity:**` was set at planning is a caveat in `**Evidence:**`, read from the plan's path history against the sprint's first story close; it is a shortfall only when the history plainly shows the number was written after the sprint's stories had closed.
- When the milestone's timeline is unavailable and the current story set differs from the planning-time set, compare the number with the stories the report or the issues place at planning, and say in `**Evidence:**` which set was used.
- The focus phrase in a sprint milestone's title and the milestones' content are the team's choice and are not judged.

### S2 — New stories and backlog refinement

**Check:**

- `issues.json`, `issue-fields.json`, and each new story's body, comments, timeline, and edit history, at `ISSUE_CUTOFF`.
- The `User Story` type and the `MoSCoW` and `Story Points` values, from `issue-fields.json` or the REST `issue_field_values`.
- The `milestoned` and `demilestoned` events and the `Responsible`/`Accountable` field values of every story the segment judges.
- The assignees, from the issue's `assignees` or `issue-fields.json`.
- Every `FR-nnn`, `ADR-nnn`, and `VP-nn` a story links, for existence at the snapshot.
- The task issues opened this week, their `Task` type, their `### Requirements` sections, and their milestones.
- The `SPRINT-06` and `SPRINT-07` GitHub milestones and the open stories in no milestone.

**met:**

- At least two `US-nn` issues were opened on or after `2026-10-30T00:00:00+03:00` and by `ISSUE_CUTOFF`, and each carries the `User Story` issue type.
- One of the two is a product-analyst story and one is a system-operator story: their titles or bodies name the internal user and the capability, one about seeing how the product is used and one about diagnosing how it operates.
- Each carries one `MoSCoW` value, one of `Must Have`, `Should Have`, `Could Have`, or `Won't Have`.
- Each carries one `Story Points` value, and no story's scope is larger than the `13` points the scale tops out at.
- Each story's acceptance criteria are checklist items of the form `- [ ] AC-nn: <criterion>` or `- [x] AC-nn: <criterion>`, numbered from `AC-01` within the story.
- Each story carries `### Specified by`, and the section names one `FR-nnn` and one `ADR-nnn` that specify the story, each linked on `main`; the analyst's pair is the analytics capability's requirement and record, the operator's is the observability capability's, both use the next free identifier in each family, and the two pairs are distinct.
- Every `FR-nnn` and `ADR-nnn` a new story's `### Specified by` links exists at the snapshot, and the `FR-nnn` it names is the one S4 or S6 finds for the matching capability.
- Each story names a `VP-nn` the vision's goal traces to: the analyst's story names the end-user value proposition the analytics capability makes measurable, and the operator's story names the one the product's operation keeps deliverable.
  Each `VP-nn` exists in `docs/research/value-proposition.md`, no new value proposition is added, and the vision's `Supports:` list is unchanged.
- Both new stories sit in `SPRINT-06`'s GitHub milestone, each carries a `Responsible` value, an `Accountable` value naming a different member, and exactly the two assignees those values name.
- The task issues for the two telemetry pipelines, the four dashboards, and the observability test exist as `Task` issues opened by `ISSUE_CUTOFF`, each carries a `### Requirements` section, and each sits in `SPRINT-06`'s milestone.
- Every open `User Story` the team places in the next two sprints' worth of the product backlog carries a `Story Points` value, has runnable acceptance criteria, and sits in no milestone.
- The stories the team places in the next two sprints' worth are unscheduled: no milestone, no `Responsible`, no `Accountable`, and no assignees.
- No story larger than `13` points is scheduled in `SPRINT-06`.

**What does not count:**

- A story added by the issue form without its type or its `MoSCoW` value, because the form does not apply either: the type and the field are set on the issue after it is created.
- A label such as `user-story` or `moscow:must` as a substitute for the `User Story` type or the `MoSCoW` value.
- An estimate on a backlog story as the whole of refinement: a story whose criteria are not runnable is not ready to schedule.
- A `Story Points` value of `0`, `20`, or `14`: the field's options stop at `13`, so a larger story is split rather than estimated.
- The `Story Points` on a story counted from a project column or from a `gh project field-list` result: the per-issue field value is the evidence.
- One story that serves both internal users, cited as the two stories.
- A `### Specified by` that names two functional requirements or two records, or one that names a `US-nn`.
- The same `FR-nnn` or `ADR-nnn` pair reused for both stories.

**partial:**

- At least one new story with its `User Story` type and a `Story Points` value is readable, and at least one other `met` criterion fails.
- Typical shortfalls: fewer than two new stories or both for one internal user; a new story missing its type, its `MoSCoW` value, its `Story Points`, a criterion, a `VP-nn`, or a `### Specified by`; a `### Specified by` that does not resolve, names the wrong family, or reuses the other story's pair; a `VP-nn` that does not exist or that is newly added; a story scheduled in `SPRINT-06` without one of the two roles or with an assignee the roles do not name; one of the two stories left unscheduled; a missing task issue, a task issue without `### Requirements`, or a task issue outside `SPRINT-06`; a backlog story the team places in the next two sprints without an estimate or with a milestone; a story over `13` points scheduled.

**missing:**

- At `ISSUE_CUTOFF` no `US-nn` issue opened on or after `2026-10-30T00:00:00+03:00` exists, or the stories that exist carry neither a type nor a `Story Points` value and no issue field can be read.

**Guardrails:**

- Every new story is judged in the Week 4 shape, and the shape itself was Week 4's rule; a defect in an older story's criteria or `### Specified by` is not re-graded here.
  The older stories are judged only for their `Story Points` and their unscheduled state where they belong to the next two sprints' worth.
- "New" means opened on or after the Week 6 window start and by `ISSUE_CUTOFF`; a story opened after the snapshot but by the cutoff counts like any other, and one opened after the cutoff is not judged.
- Refinement's quantity is the team's judgement: judge the stories the team has placed in the next two sprints' worth of the product backlog, name them, and do not require an estimate on every open backlog story.
  The assignment's "next two sprints' worth" is the planning horizon, not a numeric floor.
- The internal user a story serves is read from its own text, not from its assignee or its labels; a story that names no user but whose capability is plainly the analytics or the observability one is judged on the capability and noted as a caveat.
- The `Responsible` and `Accountable` fields, the assignees, and the milestones are read live at `ISSUE_CUTOFF`; a field value changed after the cutoff is drift and never repairs the state at the cutoff.
- A `Won't Have` story is not estimated or scheduled, so its lack of `Story Points` is not a shortfall; it still carries no roles and no assignees while it is open and unscheduled.
- An already closed issue needs no values and no assignees, and its values stay on it after it closes.
- `SPRINT-06`'s `**Sprint Backlog:**` link and its planning-time contents are S1's; this segment judges the two stories that are scheduled and the items left unscheduled.
- Whether the issue forms and the issue fields exist at all was Week 2's and Week 3's rule; a team whose organization cannot create them declares a deviation, and that declaration is judged in S17.
- A task issue for a dashboard or a pipeline may carry its capability's `FR-nnn`; requiring a separate task for each chart is the team's split, and the four dashboard tasks may be named per environment.
- The two stories' `### Specified by` pairs are checked against the `FR-nnn` files S4 and S6 judge; when those files are absent, the link is the shortfall here and the absent file is reported once, in S4 or S6.

### S3 — Analytics plan and metric tree

**Check:**

- `docs/analytics.md` in the snapshot, read whole, with `rg` for its headings and field labels when it is long.
- `docs/research/value-proposition.md` for each `VP-nn` the page names.
- `docs/deployment.md` for its link to the page.
- The page's headings, the tree's links, and the metric sections' fields and queries.
- The page's path history and the pull requests that created it, for whether it was created this week.
- The `**Source:**` events each metric names against the event table S4 judges.
- `docs/glossary.md` for the week's metric terms.

**met:**

- `docs/analytics.md` exists as one page, was created in the Week 6 window, and `docs/deployment.md` links it.
- The page names one focus metric; the section's opening sentence states it, and its next sentence links the `VP-nn` the metric expresses, which exists in `docs/research/value-proposition.md`.
- The first sub-heading under `## The Value And The Metrics` is `### The Metric Tree`, and the tree is one nested list before `### Why This Focus Metric`.
- The tree carries the four labels in bold, one focus metric at the top, one counter-metric labelled `**L1 (counter-metric):**` and nested under the focus metric, one `**L1:**` input nested under the focus metric beside the counter-metric, and one or two `**L2:**` inputs under the L1 input.
- Each tree item's text is the metric's name as a link to that metric's `###` section, and the name matches the section's heading.
- One sentence above the list says the label is the metric's level, and the page says the counter-metric guards the focus metric rather than feeding it.
- Indentation carries the parent relation, and each metric has exactly one parent.
- `### Why This Focus Metric` follows the tree, states the seven North Star criteria as one bullet each with the focus metric's answer, carries one labelled rejected vanity metric with its reason, and states that the focus metric may have no value until real users produce traffic.
- Each node in the tree has exactly one `###` section under `## The Value And The Metrics`, in tree order, headed with the metric's name in sentence case; the only other `###` headings there are `### The Metric Tree` and `### Why This Focus Metric`.
- Each metric section carries `**Definition:**`, `**Source:**`, and `**Query:**`, in that order; the definition says what the metric counts and its unit, the source names and links the events that feed it, and the query states the window and the `source` filter it applies.
- Every event a section's `**Source:**` names has a row in the event table, and at least one metric's section says its value is computed by its query rather than by hand.
- No `MET-nn` family is invented, and a metric is cited by `docs/analytics.md#<metric-anchor>`.
- The week's metric terms are added to `docs/glossary.md`: `focus metric`, `input metric`, `counter-metric`, and `metric tree`.

**What does not count:**

- A focus metric stated as the value proposition itself, such as "the product is useful", rather than a measurable number.
- A tree written after the justification, or a justification that stands in for the tree.
- A counter-metric drawn as the focus metric's sibling, or an L2 input nested directly under the focus metric.
- A tree of bare metric names with no links, or a link that does not resolve to a `###` section.
- A tree with no level labels, or one whose labels do not match the tree's indentation.
- A metric section missing `**Definition:**`, `**Source:**`, or `**Query:**`, or a query that names no window or no `source` filter.
- A number presented as the focus metric's value when the only traffic is the team's own test traffic.
- A vanity metric given its own `###` section instead of the one labelled rejected line.
- A metric returned by a hand-kept table outside the pipeline.

**partial:**

- `docs/analytics.md` exists with a focus metric and a tree, and at least one other `met` criterion fails.
- Typical shortfalls: the page created before Week 6 or not linked from `docs/deployment.md`; a `VP-nn` that does not exist or is not linked; the tree after the justification or not under `### The Metric Tree`; a missing or extra level; a counter-metric not labelled or nested correctly; a tree link that does not resolve; a missing metric section or one out of tree order; a field missing, out of order, or not naming its events; a query with no window or filter; no metric computed by its query; a `MET-nn` invented; a vanity metric with its own section; a missing metric term.

**missing:**

- `docs/analytics.md` is absent at the snapshot, or it has no focus metric and no metric tree.

**Guardrails:**

- The analytics page is created this week and is not re-graded as a later week's maintained page; a later edit after `ISSUE_CUTOFF` is drift and never repairs the state at the cutoff, and the snapshot is the page's evidence.
- The focus metric's value is not required: the course has no end users beyond the customer and the team's test traffic, so a page that reports no value and says what it would need is correct, and a page that presents smoke or usability-test traffic as the metric's value is the shortfall.
- The seven criteria are the North Star Framework's: expresses value, represents the vision and strategy, is a leading indicator, is actionable, is understandable, is measurable, and is not a vanity metric. The bullet wording is the team's.
- The metric sections' anchors are citation forms, not identifier rules: a metric is not a `MET-nn`, and the absence of a `MET-nn` family is never a shortfall.
- The glossary's older terms were Week 4's; this segment judges the four metric terms the page adds, and S6 and S9 judge the observability and capability terms.
- The number of L2 inputs is one or two; the tree's exact shape above that is the team's choice.
- The page's link from the weekly report belongs to S17, and its links from the dashboards belong to S5.
- A metric that a chart shows but the page no longer defines is a shortfall in S5, not here, when the page's own sections are complete.

### S4 — Events and instrumentation

**Check:**

- `docs/analytics.md`'s `## The Events` section and its table in the snapshot.
- The product's code in the snapshot: search for each event name, for the instrumentation call, and for the `source` value it sends.
- `docs/functional-requirements/fr/` for the new analytics requirement and its index row in `docs/functional-requirements/README.md`.
- `.env.example` and the deployment runbook for the instrumentation's configuration.
- `reports/week-06/README.md` and its screenshots for the staging smoke event's evidence, when the report records it.
- The event names a metric's `**Source:**` names, from S3's page.

**met:**

- `## The Events` carries one table whose columns are `Event`, `Fires when`, `Fields`, and `Collected at`, in that order, and there is no section per event.
- One naming convention is stated above the table as `object_action` in snake case, and every row's event name follows it.
- The table is the one registry: an event is cited by its name plus `docs/analytics.md#the-events`, and every event a metric's `**Source:**` names has a row.
- Each `Fires when` states the user's or the system's action that produces the event in one sentence.
- Each `Fields` cell names each field's name, type, and whether it is required; an event carries no personal name, email address, phone number, postal address, free text, or payment card data; an opaque identifier is generated at random and cannot be reversed to a person.
- Every event carries a `source` field, and its values are the closed set `web`, `usability-test`, and `smoke`.
- `Collected at` names the product container that emits the event and the environment it emits from, such as `backend`, staging and production.
- The table covers the core task end to end, so a reader can see the steps from the product's start to its outcome.
- The product's code sends each event from the container and environment its `Collected at` names, and the `source` value it sends is the one the table records.
- A staging test event tagged `source=smoke` exists as evidence, and the staging dashboard's event list or raw-events panel shows it while the staging metric chart excludes it; the production scope carries no smoke event.
- The analytics functional requirement exists as a new `FR-nnn` written this week, a file under `docs/functional-requirements/fr/`; its behavior is that the product records an event for each step of the core task with the fields in `docs/analytics.md`, it carries its acceptance criteria, and its row in `docs/functional-requirements/README.md` is present.
- The metric sections whose events were renamed or added are updated in the same pull request as the change.

**What does not count:**

- A section per event, or a `Metrics fed` column that duplicates what a metric's `**Source:**` already owns.
- An event table whose `Fields` cell is a prose sentence with no field names, types, and required flags.
- A `source` field that is optional, absent from a row, or open-ended rather than one of the three values.
- Personal data or free text in any field, including a customer's name or email in a support field.
- An event table that stops before the core task's outcome, such as one that records the page view but not the completed action.
- A table that lists events the product does not send, or code that sends an event the table does not record.
- A smoke event sent to the production scope, or a test event that only the report claims and no dashboard shows.
- Auto-captured page views or clicks cited as the core task's events without the action's own event.
- A planning document that says the events exist without the instrumentation in the product's code.

**partial:**

- The event table and the instrumentation exist, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or reordered column; the naming convention absent or a row that breaks it; an event a metric names with no row; a field without its type or required flag; a personal field or free text; a missing or open `source`; a `Collected at` with no environment; the table not covering the core task end to end; an event sent from the wrong container or without its `source`; no smoke evidence in the staging event list; a smoke event in production; a missing analytics `FR-nnn`, a missing criteria list, or a missing index row.

**missing:**

- `docs/analytics.md` has no `## The Events` table, or the product's code sends no event of the table at all.

**Guardrails:**

- The event table's evidence is the page and the product's code together: a table alone is a plan, and code alone is unregistered telemetry.
- The core task is the one `docs/analytics.md` and the Week 5 feature documentation describe, and `minimum-usable-product-requirements.md` names; judge the task the product actually implements, not a generic shopping flow.
- The instrumentation's library, transport, and configuration are the team's choice; the criteria are the event, its fields, its `source`, and its emitting container and environment.
- The staging smoke event's dashboard evidence is shared with S5: S4 owns that the event exists and is tagged, S5 owns that the staging dashboard shows it and the chart excludes it.
- The analytics `FR-nnn` is one file with its behavior, criteria, and index row; whether the index lists every requirement once is S10's for the new quality requirements and Week 4's for the older requirements.
- The two new `FR-nnn` files are identified by behavior, not by ordinal: the assignment asks each for the next free identifier, so either one may carry the lower number.
- A `source` value of `usability-test` is not excluded from a metric unless the page says why, and its presence is not a shortfall.
- An event that carries an opaque identifier the team also stores in a user table is not personal data when the identifier is random and not derived from personal data; the test is reversibility, not linkage.
- The page's `## Collected Data` section is judged with the event rules here: what the page says the events collect, what it says is never collected, and how collection is disabled.
- A missing analytics `FR-nnn` is this segment's shortfall even when S6's observability `FR-nnn` exists.

### S5 — Analytics backend and dashboards

**Check:**

- `docs/analytics.md`'s `## The Pipeline`, `## The Dashboard`, and `## Collected Data` sections in the snapshot.
- `docs/deployment.md`'s telemetry-pipelines section, `.env.example`, and the configuration's shape.
- The two sanitized screenshots under `reports/week-06/images/` named for the analytics environments, with `scripts/image_info.py` when a file's size or transparency matters.
- `reports/week-06/README.md`'s links to the two screenshots and the metric each chart shows.
- The Moodle PDF's four dashboards' addresses and credentials and the two backends' addresses, read once, never copied.
- The pull requests and commits in the Week 6 window that record a deploy.
- The dashboards themselves only through the single access check of `docs/grading-policy.md#consumer-hosted-media`, when the agent can reach the university network.

**met:**

- The analytics backend is OpenPanel, or another self-hosted backend that `docs/analytics.md` documents, and it runs on the university VM or, when the VM could not host it, on a second machine on the university network that the report declares.
- One backend instance carries one environment scope per environment, `staging` and `production`; for OpenPanel each scope is a project, and a documented alternative uses its equivalent.
- Each scope has its own credential, such as an OpenPanel client ID, and each environment's build is configured with its own.
- The staging scope's dashboard and the production scope's dashboard both exist, and each carries at least one chart for a metric in the tree: the focus metric once it has a value, otherwise its L1 input metric.
- Each chart is named after its metric and runs the `**Query:**` recorded in that metric's section, with the staging chart excluding `source=smoke`.
- The staging dashboard's event list or raw-events panel shows the smoke event, so the exclusion is visible.
- The production dashboard carries the same required chart and query and received no test traffic.
- `docs/analytics.md` states the instrumentation, the retention that covers its longest metric window, and how collection is enabled and disabled, including the environment variable that turns it off.
- `docs/deployment.md` carries the analytics pipeline's steps and configuration, names the `staging` and `production` scopes and their credentials' shape, links `docs/analytics.md`, and repeats none of the plan's metric or event rules.
- `.env.example` carries the configuration's shape, and no real address, credential, token, or secret is tracked in the repository; the backend's and dashboards' addresses are private-only.
- Two sanitized screenshots, one per environment, sit under `reports/week-06/images/` and are linked from the weekly report with the metric each chart shows; neither screenshot shows an address, a credential, a real name, an email address, or personal data.

**What does not count:**

- One dashboard used for both environments, or one scope whose name appears in both.
- A dashboard with no chart for a tree metric, or a chart that does not run the query its metric records.
- A chart named after a dashboard rather than its metric.
- A staging chart that includes the smoke event, or a staging event list that does not show it.
- A smoke or test event in the production scope's data.
- A backend that is only claimed in the plan: the runbook, a screenshot, or a deploy record has to place it.
- An address, a credential, a client ID, or a token committed in `docs/deployment.md`, `.env.example`, a tracked dashboard definition, or a screenshot.
- A screenshot that shows the university VM's address, a dashboard URL with its query string, or a person's name or email.
- A `docs/deployment.md` that copies the analytics plan's metric or event rules instead of linking them.
- A VM unavailable this week with no recorded postponement and no `## Deviations` entry.

**partial:**

- `docs/analytics.md` and a deployment record place the backend, and at least one other `met` criterion fails.
- Typical shortfalls: one environment scope; a shared credential; a missing chart or a chart without its metric's query; the smoke event not excluded or not shown; test traffic in production; a missing retention, disable switch, or instrumentation statement; a telemetry section with no credentials' shape or no link to the plan; a tracked real address or secret; a missing or unsanitized screenshot; a screenshot not linked from the report; a declared VM fallback that the report does not declare.

**missing:**

- No evidence places an analytics backend: the plan names none, the runbook has no pipeline, and no screenshot or deploy record exists.

**Guardrails:**

- The four dashboards' addresses and credentials are Moodle-only, and the feedback never copies one; refer to a finding by path and kind, such as "a dashboard URL in `docs/deployment.md`".
- The dashboards sit on the university network, so the default evidence is the sanitized screenshots, the runbook, the report, and the Moodle PDF; the single access check is the only live look, and an unreachable view is an evidence gap for that check only.
- The backend's exact product, its version, its hosting details, and its chart's visual design are the team's choice; the criteria are the two scopes, the two dashboards, the chart's metric and query, and the smoke exclusion.
- A screenshot is the evidence that the pipeline stored and rendered the data; a chart described only in prose is not the same artifact.
- The analytics half of `docs/deployment.md`'s telemetry section is this segment's; the observability half is S7's, and a missing whole section is reported once in the segment whose half is absent first, with the other half named as a caveat.
- A VM that was unavailable is judged by its recorded postponement, its announced date, and its `## Deviations` entry, not by a deploy that could not happen; the analytics pipeline still has to run somewhere on the university network for the week to hold.
- Week 5's deployment of the product itself is not re-graded; this segment judges only the analytics backend and its dashboards.

### S6 — Observability plan and SLIs

**Check:**

- `docs/observability.md` in the snapshot, read whole, with `rg` for its `### SLI-nn` headings and field labels.
- `docs/deployment.md`'s link to the page and the runtime `QRT-nn`s' `**Runs at:**` citations, for the links the page owes.
- `docs/quality-requirements/` for each runtime requirement's `SLI-nn` citation.
- `docs/functional-requirements/fr/` and `docs/functional-requirements/README.md` for the new observability requirement.
- `docs/glossary.md` for the week's observability terms.
- The page's path history and the pull requests that created it, for whether it was created this week.

**met:**

- `docs/observability.md` exists as one page, was created in the Week 6 window, and `docs/deployment.md` links it.
- `## The Signals` names the three signal types, the metric, the log, and the trace, and states which of them the product emits.
- The product emits a metric for every `SLI`; the log and the trace are optional, except that a signal an `SLI`'s `**Source:**` names is emitted; an alert, when the team defines one, is recorded as a rule over a signal rather than as a signal of its own.
- `## The SLIs` groups the indicators: each is a `### SLI-nn` section headed with the bare identifier, with its name on the first line, and the family takes two digits and is repository-wide.
- Each `SLI` carries `**Status:**`, `**Definition:**`, `**Unit:**`, `**Window:**`, `**Source:**`, and `**Query:**`, in that order, with `**Status:**` one of `Active`, `Planned`, or `Dropped`, and a dropped `SLI` carries `**Dropped:**` with its date and reason.
- The team lists the `SLI`s its runtime quality requirements need, and at least one of them is `Active` and demonstrated.
- The demonstrated `SLI`'s `**Definition:**` names the labels that identify the request, the route, and the failure, and its per-request point is a structured log line carrying `request_id`, `route`, `outcome`, and `duration_ms`, not a metric label.
- The `**Query:**` is recorded in the backend's query language with the labels and the window it selects, and its window matches the `**Window:**` field.
- The page states the instrumentation: which container emits each signal, how it exports it, and the export interval that meets the `SLI`'s window.
- The page states the retention that covers its longest `SLI` window, how collection is enabled and disabled, and that the backend, its dashboards, and their credentials are reachable from the university network and are private-only.
- The observability functional requirement exists as a new `FR-nnn` written this week, a file under `docs/functional-requirements/fr/`; its behavior is that the product exposes the quality signal for each runtime requirement to the observability backend, including the per-request log line the diagnosability test reads, it carries its acceptance criteria, and its row in `docs/functional-requirements/README.md` is present.
- The week's glossary terms are added to `docs/glossary.md`: `signal`, `SLI`, `service level indicator`, `observability`, and `telemetry`.

**What does not count:**

- An `SLI` written as a quality requirement or a target; the target stays the requirement's `Response Measure`.
- An `SLO-nn` or a `MET-nn`.
- A per-request point recorded only as a metric label rather than as a structured log line.
- A definition without the labels that identify the request, the route, and the failure.
- A unit such as "number" with no scale, or a window that the source's export interval cannot meet.
- A query with no window, or one whose window contradicts the `**Window:**` field.
- A page that requires a log or a trace when no `SLI` names one.
- A runtime `QRT-nn` that names a `Planned` or `Dropped` `SLI`.
- A missing observability `FR-nnn` or a glossary that omits the week's terms.

**partial:**

- `docs/observability.md` exists with at least one `### SLI-nn` section, and at least one other `met` criterion fails.
- Typical shortfalls: the page created before Week 6 or not linked from `docs/deployment.md`; a missing signal type or no statement of what the product emits; an `SLI` field missing or out of order; a status other than the three values; a missing `**Dropped:**`; the demonstrated `SLI` not `Active` or without its request, route, and failure labels; a per-request point recorded as a metric label; a query or window mismatch; no instrumentation, retention, disable switch, or access statement; a missing observability `FR-nnn` or index row; a missing glossary term.

**missing:**

- `docs/observability.md` is absent at the snapshot, or it has no `### SLI-nn` section at all.

**Guardrails:**

- The `SLI` is the measured signal and the requirement's `Response Measure` is the target; a page that defines both or conflates them is the shortfall the rule names, and the target is judged in S10.
- The backend's query language is the team's; the criteria are that the query selects the labels and the window the `SLI` defines and that a chart can run it.
- The demonstrated `SLI` is the one the Week 6 observability requirement's test reads; when the page and the test disagree, the test's citation is S10's shortfall and the page's own definition is judged here.
- The analytics and observability functional requirements are identified by behavior, not by their numbers: the assignment asks each for the next free identifier, so a team that wrote the observability requirement first is not penalized.
- A log line's exact field names beyond the four the course requires are the team's choice; the four labels are the minimum the diagnosability test reads.
- The observability page is created this week and is not re-graded as a later week's maintained page; a later edit after `ISSUE_CUTOFF` is drift and never repairs the state at the cutoff.
- The glossary's older terms and anchors were Week 4's and are not re-graded; this segment judges the five observability terms the week adds.
- The page's link from the weekly report belongs to S17, and its links from the runtime tests are checked in S10.

### S7 — Observability backend and dashboards

**Check:**

- `docs/observability.md`'s `## The Pipeline`, `## The Dashboard`, and `## Collected Data` sections in the snapshot.
- `docs/deployment.md`'s telemetry-pipelines section for the observability half, `.env.example`, and the query endpoint's shape.
- The two sanitized screenshots under `reports/week-06/images/` named for the observability environments, with `scripts/image_info.py` when a file's size or transparency matters.
- `reports/week-06/README.md`'s links to the two screenshots and the `SLI` each chart shows.
- The Moodle PDF's four dashboards' addresses and credentials, the two backends' addresses, and the query's address and credential, read once, never copied.
- The pull requests and commits in the Week 6 window that record a deploy or a dashboard change.

**met:**

- The observability backend is OpenObserve, or another backend that `docs/observability.md` documents, and it runs on the university VM or, when the VM could not host it, on a second machine on the university network that the report declares.
- One backend instance carries one environment scope per environment, `staging` and `production`; for OpenObserve each scope is an organization, and a documented alternative uses its equivalent.
- Each scope has its own dashboard, and each environment's build is configured with its own scope.
- Each environment's dashboard carries at least one chart for an `Active` `SLI`, and the chart names the `SLI` and runs the `**Query:**` recorded in that `SLI`'s section.
- The staging scope carries the test traffic, and its dashboard shows a separate failure series with a numeric P95 for a failed request.
- The production dashboard carries the same chart and query and was not exercised with test traffic.
- `docs/observability.md` states the instrumentation's export interval, the retention that covers its longest `SLI` window, how collection is enabled and disabled, and that the backend and dashboards are reachable from the university network and are private-only.
- `docs/deployment.md` carries the observability pipeline's steps and configuration, including the log exporter's batch interval, the metric exporter's interval, and the query endpoint and its credential's shape; it links `docs/observability.md`, and it repeats none of the plan's `SLI` rules.
- `.env.example` carries the configuration's shape, and no real address, credential, token, or secret is tracked in the repository; the backend's, the dashboards', and the query's addresses are private-only.
- Two sanitized screenshots, one per scope, sit under `reports/week-06/images/` and are linked from the weekly report with the `SLI` each chart shows; neither screenshot shows an address, a credential, a real name, an email address, or personal data.

**What does not count:**

- One dashboard used for both environments, or one organization whose name appears in both.
- A dashboard with no chart for an `Active` `SLI`, or a chart that does not run the query its `SLI` records.
- A chart named after a dashboard or a generic latency panel rather than the `SLI` it shows.
- A staging chart with no failure series, or a P95 shown as a dash, a zero, or a "no data" label.
- Test traffic in the production scope's data.
- A backend that is only claimed in the plan: the runbook, a screenshot, or a deploy record has to place it.
- An address, a credential, a token, or a dashboard definition's private value committed in `docs/deployment.md`, `.env.example`, or a tracked file.
- A screenshot that shows the backend's address, a query URL with its credential, or a person's name or email.
- A `docs/deployment.md` that copies the observability plan's `SLI` rules instead of linking them.
- A VM unavailable this week with no recorded postponement and no `## Deviations` entry.

**partial:**

- `docs/observability.md` and a deployment record place the backend, and at least one other `met` criterion fails.
- Typical shortfalls: one environment scope; a dashboard missing in one scope; a chart without its `SLI` or its query; no failure series before the test; test traffic in production; a missing export interval, retention, disable switch, or access statement; a telemetry section without the query endpoint's shape or without its link to the plan; a tracked real address or secret; a missing or unsanitized screenshot; a screenshot not linked from the report; a declared VM fallback that the report does not declare.

**missing:**

- No evidence places an observability backend: the plan names none, the runbook has no pipeline, and no screenshot or deploy record exists.

**Guardrails:**

- The four dashboards' addresses and credentials and the two backends' addresses and all credentials are Moodle-only, and the feedback never copies one; refer to a finding by path and kind.
- The dashboards sit on the university network, so the default evidence is the sanitized screenshots, the runbook, the report, and the Moodle PDF; the single access check is the only live look, and an unreachable view is an evidence gap for that check only.
- The backend's exact product, its version, its hosting details, its chart type, and the query language are the team's choice; the criteria are the two scopes, the two dashboards, the chart's `SLI` and query, and the failure series.
- The observability half of `docs/deployment.md`'s telemetry section is this segment's; the analytics half is S5's, and a missing whole section is reported once in the segment whose half is absent first, with the other half named as a caveat.
- A VM that was unavailable is judged by its recorded postponement, its announced date, and its `## Deviations` entry, not by a deploy that could not happen; the observability pipeline still has to run somewhere on the university network for the week's demonstration to hold.
- The failed request's failure series is the staging evidence the test in S10 reads; when the chart is missing it here, the test's `Passes` row is S10's shortfall and the pipeline evidence is judged here.
- The assignment asks the team to check the failure series before writing the test; when the ordering cannot be read from the record, judge the series and record the ordering as a caveat, never a shortfall.
- Week 5's product deployment is not re-graded; this segment judges only the observability backend, the query endpoint, and the two dashboards.

### S8 — ADRs and container view

**Check:**

- The two new `ADR-nnn` files under `docs/architecture/adr/` in the snapshot, and `docs/architecture/adr/README.md`.
- `docs/architecture/README.md`'s `## Container View` section, its embedded diagram, its source, and its legend.
- `docs/product-vision.md`'s system context diagram and source, for whether it moved.
- The two functional requirements and the new quality requirement the records address, for existence.
- The container set before this week, from the Week 4 and Week 5 snapshots or the earlier reports, and the pull requests that changed the view.
- `scripts/check_snapshot_links.py` for the records' and the view's links.

**met:**

- The analytics `ADR-nnn` exists with the next free number, its `**Addresses:**` names the analytics `FR-nnn`, and its `**Containers:**` names the product containers that emit the events.
- The observability `ADR-nnn` exists with the next free number, its `**Addresses:**` names the new `QR-nn` and the observability `FR-nnn`, and its `**Containers:**` names the containers that emit the signals.
- Each record carries its fields in order, its four body sections, and at least one `FR-nnn` or `QR-nn` in `**Addresses:**`, and every identifier it names exists at the snapshot.
- The container view shows the analytics backend and the observability backend as external systems the product exchanges telemetry with, outside the product boundary, with the protocol on each arrow.
- One sentence under `## Container View` says the team self-hosts both backends and does not build them, and the legend says the same fact.
- The view's product container set is unchanged from the set the earlier weeks established: the two backends are external systems and no new product container is added for them.
- No new view is drawn, and the context diagram stays the product's business environment: neither backend joins it.
- Both records are listed once in the ADR index.

**What does not count:**

- A backend drawn as a container inside the product boundary.
- An arrow labelled only "telemetry" with no protocol, or an arrow with no direction.
- A record whose `**Addresses:**` names only another record, a story, or a container.
- A record with no `**Containers:**` field, or one that names the backends themselves as the emitting containers.
- The self-hosting fact stated only in the record or only in the report, rather than once under the view and once in the legend.
- A new context diagram or a new deployment view that puts the backends in the product's business environment.
- A container view rewritten to add a product container for an analytics or observability sidecar the team does not run.
- A record added to the ADR index twice or not at all.

**partial:**

- The two records exist and the view shows the backends, and at least one other `met` criterion fails.
- Typical shortfalls: a record addressing the wrong identifier or a missing `**Containers:**`; a record missing one of its four body sections; a backend inside the product boundary; a missing protocol or a missing self-hosting sentence or legend line; a new product container added; the context diagram changed; a new view drawn; a record missing from the index.

**missing:**

- No new `ADR-nnn` exists, or the container view does not show either telemetry backend.

**Guardrails:**

- The two records' design choices, their alternatives, and their body prose are the team's; the criteria are the fields, the `**Addresses:**` targets, the `**Containers:**`, and the view's shape.
- The container set is the set the product runs, not every system it talks to: the backends are external because the product works with collection off and does not depend on them to serve its core task.
- "Protocol on each arrow" means the technical exchange, such as OTLP/HTTP or HTTPS, not the direction of the data alone; the arrow's direction is judged with it.
- The view's source file and its embed are one artifact; a diagram changed without its source, or a source that no longer renders, is the shortfall.
- The context diagram was Week 2's and stays the product's business environment; a change to it made this week is this segment's shortfall, and a diagram that was already wrong is not re-graded.
- The Week 4 container view and the older records are not re-graded on their own requirements; this segment judges the two new records and the view's Week 6 change.
- The records' PRs and their review are Week 1 and Week 2 mechanics and are not re-graded, except that the two records and the view change must be merged into `main` by `ISSUE_CUTOFF`.

### S9 — Feature documentation

**Check:**

- `docs/features.md` in the snapshot, read whole.
- Each `US-nn`, `FR-nnn`, `ADR-nnn`, and glossary anchor the page links.
- The pull requests that added or changed each entry and each linked record, from `prs.json`'s `files`.
- `docs/glossary.md` for the five terms Part 8 adds.
- The glossary line in the page's intro.
- The four dashboards' addresses, for the no-address rule.

**met:**

- `docs/features.md` carries a `##` entry for the analytics capability and a `##` entry for the observability capability, in the same flat list as the earlier features.
- Each new entry opens with a user-language sentence that gives the capability to its user: the analytics entry to the product analyst and the observability entry to the system operator.
- Each new entry carries `**Stories:**`, `**Behavior:**`, and `**Decisions:**`, and each links the story, the `FR-nnn`, and the `ADR-nnn` that own its facts.
- Every link in the two entries resolves at the snapshot, and the story and record are the two new ones, not an older feature's.
- The entries link the capabilities, not the dashboards, and neither entry carries a dashboard address or a query.
- Each new entry links its glossary term at first use, the page's intro carries its one line linking `docs/glossary.md`, and the week's terms are added to the glossary: `event`, `instrumentation`, `analytics backend`, `observability backend`, and `dashboard`.
- The page is updated in the same pull request as each story, requirement, record, or term it links.

**What does not count:**

- An entry that lists the dashboards or the pipeline steps instead of a capability in the user's words.
- An entry whose links stop at a story, a requirement, or a record without all three.
- A link to a dashboard, a backend, or a screenshot as the feature.
- A glossary link on a later use but not the first, or a term defined only in the entry.
- An entry updated in a later pull request than the record it links.
- A dashboard address written into the entry or its link text.

**partial:**

- At least one of the two entries exists with its links, and at least one other `met` criterion fails.
- Typical shortfalls: one entry missing; an entry that names artifacts rather than the capability; a missing or non-resolving `**Stories:**`, `**Behavior:**`, or `**Decisions:**`; a dashboard address or a dashboard cited as the feature; a missing first-use glossary link or a missing week term; an entry updated after the record it links.

**missing:**

- `docs/features.md` has no entry for either internal capability.

**Guardrails:**

- The capability's name, its sentence, and its place in the page's order are the team's choice; the criteria are the capability, the three links, the no-address rule, and the glossary use.
- An internal user is a user: the analyst and the operator are the two the assignment names, and a feature entry that serves them is a user-facing capability.
- The dashboards are the evidence of the two capabilities and never the features themselves; a page that lists "OpenPanel", "OpenObserve", or "four dashboards" as its features is the shortfall.
- The older entries are Week 5's and are not re-graded; this segment judges the two new entries and their terms.
- The glossary's older terms, its anchors, and its definitions were Week 4's; this segment judges the first-use links and the five terms Part 8 adds.
- A link to a record on `main` is enough when the record is merged by the snapshot; a link to a branch or a pull request is not.
- When a story's or a record's own shape is short in S2 or S8, the missing link here is still this segment's shortfall only when the target does not exist; a target that exists but is weak is reported once, in the segment that owns its shape.

### S10 — Observability requirement and test

**Check:**

- The new `QR-nn` file under `docs/quality-requirements/qr/`, its scenario, its `Response Measure`, and its `## QRT-nn` section.
- The script or command the test names, in the snapshot.
- `docs/project-plan.md`'s `## Quality Requirement Testing Plan` rows and their `Checked` cells.
- `docs/quality-requirements/README.md` for the requirements index and the priority matrix, and its one link to the testing plan.
- `reports/week-06/README.md` and its screenshots for the test's evidence.
- The pull requests and commits in the Week 6 window that record the test's run.
- The `SLI-nn` the test names, for its `Active` status and its labels.

**met:**

- A new `QR-nn` uses the next free number, carries the `Maintainability` / `Analysability` pair, `**Business importance:** High`, and `**Technical risk:** Medium`.
- Its scenario's source is the system operator, its stimulus is a failed request in the core task, and its response measure states that within five seconds of the failed request's response a query of the staging organization returns one log point for it carrying its request identifier, route, and failure label, and that within one minute the `SLI`'s query returns the failure series with a P95 value.
- Its `QRT-01` sits after `## Scenario`, carries `**Status:** Active`, `**Level:** deployed`, and `**Runs at:**` naming the staging deployment, the `Active` `SLI-nn` it reads as a link, and `$OPENOBSERVE_URL` or a placeholder rather than a real address.
- The `### Procedure` runs the core task's traffic, fails one request, queries the staging organization for the log point, and reads the `SLI`'s five-minute P95; the one `**Pass when:**` criterion settles the response measure's threshold in that environment and window.
- The script or command the test names exists in the snapshot, for example `scripts/check-sli.ts`, generates the traffic, fails the request, reads the log point, and prints it with its `request_id`, route, and failure labels; it reads `$STAGING_URL` and `$OPENOBSERVE_URL` and takes the credential from the environment.
- The test was run against the staging deployment from a machine on the university network, and its testing-plan row is `Passes` with `Checked` in `SPRINT-06`.
- The row's evidence links the staging organization's log-query output for the failed request with its `request_id`, route, and failure labels, the `SLI`'s five-minute P95 query result, the dashboard screenshot, the staging environment, and the commit the test ran against.
- Each row the testing plan planned for `SPRINT-06` was run, or moved to `SPRINT-07` with its reason, and the report declares both.
- When a runtime `QRT-nn` from an earlier week was re-run, its `**Runs at:**` names the same `Active` `SLI`, its procedure reads that signal, and a failed re-run records `Fails` and does not remove this week's demonstration.
- The new requirement appears once in the quality requirements index and once in the priority matrix, and the index links the testing plan once.

**What does not count:**

- A `CI` or `scripted` test standing in for the `deployed` observability test.
- A `manual` test, because the assignment requires a command run against staging.
- A `QRT-nn` whose `**Runs at:**` omits the `SLI-nn`, or names a `Planned` or `Dropped` one.
- A pass criterion that drops the five-second or one-minute threshold, or one that settles a different value from the response measure.
- A procedure that reads the dashboard but never queries the staging organization for the log point.
- A test row whose evidence is the dashboard screenshot alone, with no log-query output and no commit.
- A `Passes` row checked in `SPRINT-05` or checked in `SPRINT-06` but marked `Not verified`.
- A row moved to `SPRINT-07` with no reason, or a moved row the report does not declare.
- A re-run that gives an older runtime test an `SLI` citation without reading it in the procedure.
- A requirement added to the matrix and not the index, or the index linking the testing plan twice.

**partial:**

- The new requirement and its `QRT-01` exist, and at least one other `met` criterion fails.
- Typical shortfalls: the wrong pair, importance, or risk; a scenario whose source or stimulus is wrong; a response measure missing one of its two thresholds; a test at the wrong level; a `**Runs at:**` with no `SLI` or with a real address; a procedure that misses the failed request or the staging query; a script that does not fail the request or does not print the log point; a `Passes` row without the log-query evidence or the commit; an unrun or unaccounted row; a re-run that does not read its signal; a missing index or matrix row, or a second testing-plan link.

**missing:**

- No new `QR-nn` exists with a `QRT-nn`, or the testing plan has no row for it.

**Guardrails:**

- The new requirement's identifier, its exact title, its scenario prose, and its procedure's commands are the team's; the criteria are the pair, the fields, the two thresholds, the `deployed` level, the `SLI` citation, and the recorded result.
- The requirement is about the product's diagnosability, not the dashboard's: a test that reads only the dashboard's rendered chart, or a requirement whose stimulus is the dashboard's configuration, is the shortfall the assignment names.
- The evidence of a `deployed` test is the command, the staging environment, the output, the measured value, and the commit; a screenshot alone is the visual evidence, not the whole result.
- The test's run time is read from the testing plan's `Checked` cell and the evidence, not from the test's own fields; a `Passes` row with no `Checked` sprint is the shortfall.
- A testing-plan row planned for `SPRINT-06` that could not run is moved to `SPRINT-07` with its reason and the report's declaration; a row left planned for `SPRINT-06` after the deadline is the shortfall, and a longer test the team runs on its own may stay `Not verified` with its `Planned for sprint`.
- The optional re-run is optional: its absence is never a shortfall, and its presence is judged only when the report says it ran.
- The index and the matrix were Week 4's and are not re-graded for their older rows; this segment judges the new requirement's rows and the one testing-plan link.
- A `QR-nn` whose `**Business importance:**` is `High` but whose test is `manual` is the shortfall the manual exception names, and the deviation belongs to S17's `## Deviations`.

### S11 — Threshold review

**Check:**

- `docs/threshold-of-success.md` in the snapshot: each `TOS-nn` section, its status, its `**Measure:**`, its `**Outcome:**`, and its `**Changed:**`.
- `reports/week-06/README.md`'s `## Threshold review` section.
- The metric sections in `docs/analytics.md` that a proposal links.
- `docs/decisions.md` for each `DEC-nnn` a change cites.
- `reports/week-06/meeting-report.md`'s `## Decisions` list.
- The pull requests in the Week 6 window that changed the threshold file.

**met:**

- The report carries `## Threshold review` with one table whose columns are `Goal`, `Current measure`, `New data can settle it`, and `Proposal`, in that order.
- The table has one row per `TOS-nn` that is `Open` when the review starts, in `TOS-nn` order, and a goal settled in an earlier week is not in it.
- Each `Goal` cell links the goal's section in `docs/threshold-of-success.md`.
- Each `Current measure` cell states the goal's current `**Measure:**` and the week it lands in.
- Each `New data can settle it` cell says `Yes` and names the analytics or observability data that settles it, or `No` and why the data cannot.
- Each `Proposal` cell states a proposed measure with its number, the week it lands in, and a link to the metric's `###` section in `docs/analytics.md`, or `—` when the team proposes none.
- Immediately after the table, one sentence per row in `TOS-nn` order states the goal's status after the review, `Open`, `Achieved`, or `Missed`, and links the goal to its section.
- A goal whose measure is already settled is set `Achieved` or `Missed` with its `**Outcome:**` in `docs/threshold-of-success.md`, and the report does not restate the outcome; a goal whose measure lands later stays `Open`.
- The section says why the team proposed each measure in the table, or why it proposed none.
- Any change the customer agrees is a `DEC-nnn`, cited under the goal's `**Changed:**`, and listed in the meeting report's `## Decisions`.
- No goal is required to change, and a review that records why nothing moves is complete.

**What does not count:**

- A table that copies each settled goal's `**Outcome:**` instead of linking the goal.
- A table that includes a goal settled in an earlier week.
- A `Proposal` with a number but no week, or with a week but no metric link.
- A measure changed in the threshold file with no customer `DEC-nnn` and no `**Changed:**`.
- A status sentence that gives the reason instead of the verdict, or one that restates the settled outcome.
- A review written only in the threshold file, with no `## Threshold review` in the report.
- A proposal the customer did not agree, recorded as if the bar moved.

**partial:**

- The report has a `## Threshold review` section and at least one row, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or reordered column; a missing open goal, a settled goal in the table, or a row out of `TOS-nn` order; a goal link that does not resolve; a current measure without its week; a `Yes` with no data or a `No` with no reason; a proposal without its week or metric link; a missing or misplaced status sentence; a settled goal whose `**Outcome:**` is missing or copied; a missing "why" paragraph; a change without its `DEC-nnn` or `**Changed:**`.

**missing:**

- The report has no `## Threshold review` section, or the table has no row for any open goal.

**Guardrails:**

- The review's evidence is the threshold file at the snapshot and the report's section; the table's data is judged against the goals' current measures, not against the Week 3 text.
- A goal's `**Outcome:**` is the threshold file's, and the report points at it; the report's sentence gives the verdict only, so the two artifacts do not carry two copies that drift.
- A proposal is a proposal: only the customer's `DEC-nnn` moves the measure, and a proposal with no decision is correct when the report says why.
- The `Proposal` cell's metric link points at `docs/analytics.md#<metric-anchor>`, not at the page's top or at a chart.
- The threshold file's older goals, their statements, and their Week 3 wording are not re-graded; this segment judges the review's rows and the changes it records.
- The customer's decision's own shape is S13's; this segment judges that the change cites a `DEC-nnn` and that the measure did not move without one.
- A goal whose measure lands after Week 6 stays `Open`; a team that marks it `Achieved` or `Missed` early is the shortfall the rule names.

### S12 — Week 5 action points and open questions

**Check:**

- `reports/week-05/meeting-report.md` at the Assignment 5 snapshot or, when it is not in the Week 6 snapshot, the A5 submission's report, for `## Action points` and `## Open questions`.
- `reports/week-06/meeting-report.md`'s `## Previous action points` and `## Previous open questions`.
- The artifacts and task issues an `Outcome` or `Answer` cell links, in the Week 6 snapshot.
- `docs/decisions.md`, for the entries a `Decision` cell links and their `**Source:**`.
- The Week 5 report's action points' due weeks and owners.

**met:**

- The Week 5 meeting report's `## Action points` and `## Open questions` can be read, or the Week 6 report says there were none.
- `## Previous action points` has the columns `Action`, `Outcome`, and `Decision`, with one row per Week 5 action point due in Week 6 or carried out early.
  Week 6 runs from Friday 30 October 2026 through the 8 November 2026 submission deadline, so a due date from 30 October to 8 November is a Week 6 due date.
- Every `Action` cell cites `reports/week-05/meeting-report.md#action-points` with the action quoted.
- Every `Outcome` says whether the action point was carried out and what was found, or why it was not, and links each artifact and task issue it changed.
- Every artifact an `Outcome` says changed holds that change, and the change is dated no later than `ISSUE_CUTOFF`.
- An action point not carried out reappears in the Week 6 `## Action points` with a new due week, unless its `Outcome` says the team or the customer dropped it.
  The due week's window is S13's, so a reappearance outside Week 7 is not a second shortfall here.
- Every `Decision` cell links the `DEC-nnn` the outcome produced, or says `None`, and every linked entry exists with a `**Source:**` that points at where the decision was made.
- `## Previous open questions` has the columns `Question`, `Answer`, and `Decision`, with one row per Week 5 open question not yet closed, and every Week 5 open question is either answered there or carried into the Week 6 `## Open questions`.
- Every `Question` cell cites `reports/week-05/meeting-report.md#open-questions` with the question quoted.
- Every `Answer` says what the work or the meeting found and links each artifact the answer changed.
- No Week 5 action point or open question is silently dropped: one that the team no longer intends to do is `Dropped` in its `Outcome` or carried forward, and one the meeting answered is answered with its `DEC-nnn`.
- The Week 5 meeting report is not edited; the Week 6 report is where the outcomes are recorded.

**What does not count:**

- An `Outcome` that says "done" with no artifact and no task issue linked, while the artifact it should have changed is unchanged.
- A citation by number alone, such as "action 2", without the report's path, the `#action-points` anchor, and the quoted action.
- A Week 5 open question that is neither answered in `## Previous open questions` nor carried into `## Open questions`.
- A `Decision` cell naming a `DEC-nnn` that does not exist, or one whose `**Source:**` points at another meeting.
- A Week 6 report that edits the Week 5 report to close its rows there.
- An action point whose due week is Week 7, cited as due this week.

**partial:**

- The Week 6 meeting report has both `## Previous` sections, and at least one other `met` criterion fails.
- Typical shortfalls: an action point due in Week 6 with no row; an outcome that exists only in the table, with the artifact unchanged; an action point not carried out that does not reappear; a Week 5 open question with no row and no carry-forward; a citation without the quoted action; an `Outcome` naming a task issue that does not exist; a `Decision` cell that links nothing and does not say `None`.

**missing:**

- The Week 5 meeting report is absent from the A5 snapshot and the A5 submission, or neither `## Previous action points` nor `## Previous open questions` is present when the Week 5 report has rows for it.

**Guardrails:**

- When the Week 5 report has no action point due in Week 6 or no open question, `None` in the matching section is correct.
- Do not re-grade the Week 5 report; judge only what Week 6 did with its rows.
- An outcome carried into an artifact is judged by whether the artifact changed, not by whether the change is large.
- An action point the customer dropped stays closed, and the customer's decision is cited.
- A Week 5 report edited in Week 6 is a quality note unless its content was rewritten; a formatting-only change is allowed.
- A Week 5 open question the work has not answered belongs in the Week 6 meeting's questions; when the report carries it forward without an answer and the script does not ask it, report it here as a shortfall.
- The Week 6 `## Action points` table's shape and due dates belong to S13; this segment judges the reappearance of an open action point, not the table.
- An action point due in Week 7 but carried out this week may close here, and the row is correct.

### S13 — Customer validation of the telemetry

**Check:**

- `reports/week-06/meeting-script.md`, `meeting-report.md`, and `meeting-transcript.md` when it exists, in the snapshot.
- The path history of the script, for whether it was committed before the meeting.
- Every `DEC-nnn` in `## Decisions`, in `docs/decisions.md`, and every story issue the meeting showed or changed, with its comments, timeline, and edit history.
- The analytics and observability pages and the four dashboards' screenshots, for what the meeting showed.
- The observability `QRT`'s result and each runtime `QRT`'s result, for what the review reported.
- The threshold review and each `DEC-nnn` it cites.
- The Week 6 meeting report's `## Decisions`, `## Previous action points`, and `## Previous open questions`.
- The Moodle PDF's recording link and transcript appendix, read once, never copied.
- `reports/week-06/images/` for the screenshots the report links.

**met:**

- The Week 6 meeting is the sprint's Sprint Review, and `reports/week-06/meeting-script.md` exists with exactly the sections `## Context`, `## Agenda`, `## Questions`, `## Roles`, and `## Key improvements`, in that order, with `## Roles` left out only for a meeting held in writing, and every empty section says `None`.
- `## Context` gives the problem-space sentence, what the team believes, and a one-sentence target that covers whether the telemetry answers the questions the customer recognises, whether the diagnosability requirement holds in staging, and what the threshold should measure next.
- `## Agenda` is a numbered list whose first part asks the three permission questions, whose last part reads back the decisions and action points, and whose parts each have a timebox that adds up to the planned length, or, for a meeting held in writing, the order of the exchange and what is sent with each part instead of timeboxes.
- The agenda shows the deployed product with the analytics staging and production dashboards, the observability staging and production dashboards, the observability `QRT`'s result, and each runtime `QRT`'s result at its level, ends with the threshold proposal, and asks for the customer's verdict on each story it shows.
- Every agenda part names what is shown, with a link or a statement that nothing is shown, and every question appears in exactly one part.
- `## Questions` is numbered, every question is tagged open or closed, and every question serves the target.
- `## Roles` names a moderator, a note taker, and an observer by GitHub username, and a written meeting omits the section.
- `## Key improvements` records at least one rewritten question with the before, the after, and the principle.
- The script was written before the meeting it prepares: its first commit is on or before the meeting date in `## Metadata`, and a same-day commit is accepted when the history shows it came before the meeting; its later commits are formatting-only changes.
- The report has exactly the sections `## Metadata`, `## Previous action points`, `## Previous open questions`, `## Summary`, `## Decisions`, `## Action points`, `## Open questions`, and `## Disagreements`, in that order, and every empty section says `None`.
- `## Metadata` is a bulleted list of `- **Label:** value` bullets giving the date, the duration, the attendees by GitHub username with the customer as `Customer`, what was presented, the answer to each of the three permission questions, the transcript link or `None` with the reason, and the script link.
- The report's `## Metadata` or `## Summary` says the meeting showed the deployed product with the four dashboards, the observability `QRT`'s result, and each runtime `QRT`'s result at its level, reached from the university network, and names what was shown.
  When the VM was unavailable, it says the team showed the local product and the deployment plan and declares the deviation.
- `## Summary` has 3 to 5 bullets on what the meeting settled or changed.
- `## Decisions` lists at least one `DEC-nnn` entry of the form `[DEC-nnn: <the entry's first line>](../../docs/decisions.md#dec-nnn)`, and every change the customer made has a `DEC-nnn` entry in `docs/decisions.md` naming what it changed, made by `Customer` or `Team, not contested`, with a `**Source:**` linking this report.
- The customer's decision on the threshold proposal is recorded as a `DEC-nnn`, and a proposal the customer rejected is recorded as no change.
- Every story the meeting showed has a verdict recorded as a decision naming its `US-nn`, and an accepted story has closed with a comment that cites its verdict's `DEC-nnn` and names the `AC-nn` it was accepted against.
- A rejected story's verdict names each `AC-nn` it failed, the story stays open, and its rework task names the story and the failed `AC-nn`.
- Every story issue the meeting showed, accepted, rejected, or changed has a comment dated on or after the meeting that names the verdict or the change, names each `AC-nn` affected, and links the `DEC-nnn` on `main`.
- `## Action points` has the columns `Action`, `Owner`, and `Due`, at least two rows, an owner given by GitHub username, and every due date inside Week 7, such as `End of Week 7` or a date from 9 November to 14 November 2026; a due date on or before the 8 November 2026 deadline is Week 6 and is not that window.
- `## Open questions` has the columns `Question`, `What it would change`, and `Follow-up`; `## Disagreements` has the columns `Your position`, `Customer's position`, and `What you changed`, and every row that changed nothing says why the team kept its position.
- The meeting was held in the Week 6 window, between Friday 30 October 2026 and `ISSUE_CUTOFF`, and a meeting held in writing says so and carries no `## Roles` section.
- Every meeting artifact names the customer `Customer` and identifies people only by GitHub username.
- When the meeting was recorded or held in writing, and publication was permitted, `reports/week-06/meeting-transcript.md` exists, opens with the date and the participants as `- **Label:** value` bullets above the first timestamped line, with a `#` title allowed above them, and then has one sentence per line in the form `[hh:mm:ss] <label>: <sentence>`, labels speakers by GitHub username and `Customer`, marks gaps with `[inaudible]` or `[redacted]`, and carries no personal data.
- When publication was refused, no transcript is committed, and the report's `## Metadata` says the transcript is Moodle-only; the PDF's appendix is S17's item.
- No meeting artifact carries a recording link or a recording timecode: the recording link and the timecodes are Moodle-only, per the visibility rule.

**What does not count:**

- An agenda that shows only the local product without the deployment, when the VM was available, and without a declared deviation.
- A review that shows the product but not the four dashboards, the observability `QRT`'s result, or a runtime `QRT`'s result.
- A dashboard shown only from a local or a development instance.
- A test's result reported as "the tests pass", with no level, no commit, and no measured value.
- A verdict recorded only in the report's table, with no `DEC-nnn` entry and no story comment.
- Shared decisions with no per-item verdict, or a single "the customer approved everything" sentence.
- A script with a missing or extra section, no permission part in the agenda, or no roles in a live meeting.
- A script written after the meeting, or a same-day commit the history cannot place before the meeting.
- A script or transcript rewritten after the meeting, or edited after `ISSUE_CUTOFF`, as the pre-meeting form.
- A `## Summary` that restates the transcript line by line.
- An action point due outside Week 7, or no owner on an action point.
- A transcript written one speaker turn per line when a turn carries several sentences: that is not the one sentence per line the rule requires.
- A transcript that says the customer refused publication but sits in the repository.
- A test result shown against production as a `deployed` test's run.
- A recording link or timecode inside a meeting artifact.
- A personal name, email, or real address in the meeting artifacts.

**partial:**

- `reports/week-06/meeting-report.md` exists with at least one dashboard or test shown, and at least one other `met` criterion fails.
- Typical shortfalls: a missing or extra section; no permission part in the agenda; the agenda showing neither the dashboards nor the tests' results; a dashboard or the observability `QRT`'s result missing; a runtime test's result missing or its `SLI` unnamed; a story shown with no `AC-nn` verdict; a verdict decision that does not name its `US-nn`; a change with no `DEC-nnn`; a missing `## Decisions`, `## Previous action points`, or `## Previous open questions`; a missing threshold proposal or no `DEC-nnn` decision on it; fewer than two action points due in Week 7 or an action point with no owner; a missing transcript where the meeting was recorded and publication was permitted; a published transcript without permission; a recording link or timecode in a meeting artifact; personal data in a meeting artifact; a report that restates the transcript line by line; the VM fallback claim without the deviation.

**missing:**

- There is no Week 6 meeting artifact: no script, report, or transcript.

**Guardrails:**

- The meeting is the Sprint Review, so a separate ceremony report is not required and the two are judged together.
- The dashboards are on the university network; the meeting's evidence is the report's links and the Moodle PDF's addresses, and the single access check is not repeated for each dashboard.
- The four screenshots the report links are the ones S5 and S7 judge for sanitization; this segment judges that the meeting showed them and that their links resolve.
- The transcript's language, its length, and its exact format are the team's; the criteria are its existence when recorded and publication was permitted, its appendix, and its privacy.
- The Week 6 report's coverage rows and its `## Threshold review` content are S17's and S11's; this segment judges the meeting's own artifacts and the decisions they record.
- A customer who refused recording makes the one-line reason correct, and the transcript's absence is never a shortfall then.
- A customer who refused publication of the transcript makes no repository transcript correct, and the report's `## Metadata` says it is Moodle-only; the PDF's appendix is S17's item.
- A meeting held on or after Friday 30 October 2026 and by `ISSUE_CUTOFF` was held in Week 6; a meeting on 6, 7, or 8 November is in the window and is a caveat in `**Evidence:**` rather than a shortfall.
- The two internal-user stories are shown only when the meeting presents them; when it does not, the story verdicts are not a shortfall, and the absence of the stories themselves is S2's.
- A story the customer accepted in a shared verdict is still judged by its own `AC-nn` comments, and a shared verdict is one decision.
- The meeting's decisions' `DEC-nnn` entries are judged here for their agreement and their citation, and S11 judges the threshold change they make.
- The PDF's own shape, page count, item list, recording link, and transcript appendix are S17's; this segment reads the report and the script, and reads the PDF only when the report's own statement about publication is unclear.

### S14 — Redeploy and retest after same-week rework

**Check:**

- The pull requests and commits merged after the Week 6 meeting and by `ISSUE_CUTOFF`, from `prs.json` and `commits.json`.
- `docs/deployment.md`, the report, and the testing plan for the deploy and the retest record.
- The observability `QRT`'s row and any re-run runtime `QRT`'s row, for the result and its commit.
- The release's tag target and the production deploy's commit, from S15's checks.
- The meeting report's verdicts, for what the review asked to change.

**met:**

- When the review asked for same-week rework, it was merged, deployed to staging, and the observability test and, when it was run, the optional runtime test were re-run at their levels against the new staging deployment.
- When they passed, the same final commit was deployed to production and the core task was verified again.
- When the rework could not finish before the deadline, it was deferred to `SPRINT-07` with its reason, and the reviewed and tested commit is the release commit.
- The commit the release names is the commit the staging test ran against and the commit production served after the rework.
- The report records the rework, the redeploy, the retest, and the verification, or the deferral and the reason, and the record names the commit or the release.
- No deploy claimed in the report runs a commit the staging test did not test.

**What does not count:**

- Rework merged to `main` but not deployed.
- A production deploy before the staging retest.
- A release cut on a commit that differs from the tested one, with no recorded reason.
- A retest that reuses the earlier run's result without running the command against the new staging deployment.
- A deferral with no reason, or a deferred rework released anyway.

**partial:**

- The rework and the deploy are recorded, and at least one other `met` criterion fails.
- Typical shortfalls: a merged rework that never reached staging or production; the retest missing for one of the two tests; production deployed before the retest; a release on a different commit than the tested one; a consulted record that does not name the commit; a deferral without its reason.

**missing:**

- The review asked for rework and the submission records neither its redeploy and retest nor its deferral, or the released commit and the tested commit plainly disagree with no record.

**Guardrails:**

- The sequence is judged only when the review asked for rework: a sprint with no rework releases the reviewed and tested commit, and the absence of a redeploy is then correct.
- The `deployed` evidence is the staging run's output and the production verification, per S10 and S5; this segment judges the sequence and the commit identity, not the tests' own shape.
- A production verification is the core task run on production from a machine on the university network, not a health endpoint alone.
- The rework's own code and its review are Week 1 and Week 2 mechanics and are not re-graded; this segment judges what was deployed and tested after it.
- When the release tag lands after `ISSUE_CUTOFF`, that timing is S15's caveat and this segment still judges the sequence the record shows.
- A rework deferred to `SPRINT-07` that was merged after the cutoff is drift; the reviewed commit is the release commit, and a tag on the later commit is S15's shortfall.

### S15 — REL-06 release

**Check:**

- `tags.json` and `releases.json`, and the raw `gh api "repos/$REPO/releases?per_page=100"` and `gh api "repos/$REPO/git/refs/tags/<tag>"` responses for the title, the body, and the commit.
- `CHANGELOG.md`'s `[Unreleased]` section and its dated released section.
- `docs/project-plan.md`'s `#### REL-06` block under `### SPRINT-06`.
- The `SPRINT-06` GitHub milestone's state and the issues rescheduled out of it.
- The testing plan's `Checked` cells, for the `**Checked QRs:**` list.
- `gh api "repos/$REPO/rulesets"` and each tag ruleset, for the tag's protection.
- `reports/week-06/README.md` for the release's record and its tag.

**met:**

- The tag is named `v<major>.<minor>.<patch>`, it points at a commit on `main`, and that commit is the final production commit the week's record names.
- The release title is the tag, so the title and the tag match.
- The tag is protected against being moved or deleted, by a repository ruleset that covers tag pushes or an equivalent tag-protection rule that blocks moving and deleting the tag.
- `CHANGELOG.md` follows Keep a Changelog: `[Unreleased]` was kept through the week, the released entries moved into a dated section such as `[0.6.0]` with `### Added` entries for the analytics and the observability, that section links the release, and a new empty `[Unreleased]` follows.
- The release body is the upgrade note: it states whether the upgrade requires anything beyond deploying this version, or that it does not, and names the new environment variables and configuration when it does.
- The body ends with the line `[Full changelog](<absolute url>)` linking the changelog's released section, and nothing comes after it; the body carries no address, credential, token, or other private-only value.
- `### SPRINT-06` carries a `#### REL-06` block with `**Released:**` and `**Checked QRs:**`.
- `**Checked QRs:**` lists every `QR-nn` with at least one test whose testing-plan row is `Checked` in `SPRINT-06`, and the new observability requirement is one of them.
- `SPRINT-06`'s GitHub milestone is closed after each issue still open was moved into a later sprint's milestone.

**What does not count:**

- A tag on a commit that is not the final production commit, or a tag on a branch name.
- A release title that is a nickname while the tag is the version, or a version without the `v` prefix.
- A body that lists the changelog's entries instead of the upgrade note.
- A body that ends with a changelog summary rather than the `Full changelog` line, or a relative changelog link.
- `**Checked QRs:**` copied from `REL-05`, or built from a requirement's status rather than its tests' `Checked` cells.
- A `REL-06` block outside `### SPRINT-06`, or one missing its `**Released:**` field.
- `SPRINT-06`'s milestone left open, or closed with issues still in it.
- An unprotected tag, or one that a force push or a deletion could move.
- A body carrying a dashboard address, a credential, or the query endpoint.

**partial:**

- `REL-06` exists with a tag and a released changelog section, and at least one other `met` criterion fails.
- Typical shortfalls: a tag on the wrong commit or not on `main`; an unprotected tag; a title that does not match the tag; a changelog section that does not link the release or a missing `[Unreleased]`; a body missing the upgrade statement, the configuration, or the `Full changelog` line; a private-only value in the body; a missing `**Released:**`; a `**Checked QRs:**` list that omits the new requirement or includes an unchecked one; a milestone left open.

**missing:**

- No `REL-06` tag or release exists at the cutoff, or the plan has no `#### REL-06` block.

**Guardrails:**

- The version number is the team's SemVer choice; the criteria are the tag's shape, its target, its protection, and the record's completeness.
- The release's `Checked QRs` is built from the testing plan's `Checked` cells and from nothing else: a requirement with a checked test belongs, whatever the row's `Status`, and a requirement with none does not.
- The tag's and the release's timing is read against `ISSUE_CUTOFF`; a tag placed after the cutoff is a caveat in `**Evidence:**` and never repairs the state at the cutoff, and a release page edited after the cutoff is drift.
- The changelog's `[Unreleased]` upkeep through the week is judged here as part of the released section, and the W5 released section is not re-graded.
- The sprint milestone's close is judged from its state and the issues' milestones at the cutoff; an issue moved to `SPRINT-07` with its events is the expected record.
- The release body's exact shape is the team's, and the two required facts are the upgrade action (or that none is needed) and the `Full changelog` line; a body that states them in a different order is correct.
- `REL-05`'s tag, body, and changelog section were Week 5's and are not re-graded.

### S16 — Sprint close and retrospective

**Check:**

- `docs/project-plan.md`'s `### SPRINT-06` section and its `**Actual Velocity:**` field.
- The `User Story` issues closed as completed in `SPRINT-06`'s milestone at `ISSUE_CUTOFF`, and their `Story Points`.
- `reports/week-06/sprint-retrospective.md` in the snapshot.
- `reports/week-05/sprint-retrospective.md`'s `## Actions` rows with `Carried: Yes`.
- The pull requests in the Week 6 window that changed the plan and the retrospective.

**met:**

- `### SPRINT-06` carries `**Actual Velocity:**` as a whole number, and it equals the sum of the `Story Points` of the stories closed as completed in `SPRINT-06`'s milestone.
- One sentence after the figure says what moved out of the sprint and to which sprint.
- `reports/week-06/sprint-retrospective.md` carries `## What Went Well`, `## What Did Not`, `## Actions`, and `## Carried Actions`.
- `## What Went Well` lists 3 or more items; `## What Did Not` lists 2 or 3 items with their root causes; `## Actions` lists 3 or 4 actions with their `Reason` and their `Carried` flag.
- `## Carried Actions` carries each `SPRINT-05` action marked `Carried: Yes`, cites `reports/week-05/sprint-retrospective.md#actions` with the action quoted, and gives each an `Outcome` of `Done`, `Not done`, or `Dropped`.
- Every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.

**What does not count:**

- An `**Actual Velocity:**` copied from `**Planned Velocity:**`, or a figure that does not match the completed stories' points.
- A velocity figure with no sentence on what moved out.
- A retrospective with the four headings but no root causes, or with fewer than the required rows.
- An action with no `Reason`, or a carried action with no quoted action, no anchor citation, or no `Outcome`.
- A `Not done` action that is not re-listed in `## Actions`.
- A `Carried Actions` section that lists the Week 5 actions without their outcomes.

**partial:**

- `**Actual Velocity:**` is set and the retrospective exists, and at least one other `met` criterion fails.
- Typical shortfalls: a velocity figure that does not equal the completed stories' points; a missing sentence on what moved out; a missing retrospective section or a row count short of the minimum; a `What Did Not` item with no root cause; an action without its `Reason` or `Carried`; a carried action missing its citation, its quote, or its `Outcome`; a `Not done` action not re-listed.

**missing:**

- `**Actual Velocity:**` is absent from `### SPRINT-06`, or `reports/week-06/sprint-retrospective.md` is absent.

**Guardrails:**

- Velocity is computed by hand from the stories' `Story Points`, because the single-select field cannot be added up; the segment checks the arithmetic against the completed stories at the cutoff.
- A story is completed when it is closed as completed in `SPRINT-06`'s milestone by `ISSUE_CUTOFF`; a story moved out before the close does not count, and the sentence on what moved out names it.
- The retrospective's prose, its exact action wording, and its root causes' depth are the team's; the criteria are the four sections, the row counts, and the carried actions' shape.
- The Week 5 retrospective's own shape is not re-graded; this segment judges the actions it marked `Carried: Yes` and what the Week 6 file does with them.
- `**Planned Velocity:**` belongs to S1 and the `REL-06` block to S15; a plan whose figures disagree is reported in the segment that owns the wrong field.
- A retrospective written after the cutoff is a caveat in `**Evidence:**`, not a shortfall, unless the file plainly copies the report's summary.

### S17 — Week report and submission

**Check:**

- `reports/week-06/README.md` in the snapshot, read whole, and every repository file it links.
- `reports/week-06/images/` for the four dashboard screenshots, with `scripts/image_info.py` when a file's size or transparency matters.
- The Moodle PDF under `itpd-assignments-feedback/A6/submissions/<team_dir>/`, read once, for its items, its page count, and its addresses.
- `pdf-info.json` for the repository, the permalink, the SHA, the page count, the recording link, and the permalink-week check.
- `runs_main.json` and `runs_sha.json` for the latest link-check, Markdown-check, `actionlint`, and product-code runs on `main`, and the merged pull requests in the Week 6 window.
- `prs.json` for one merged pull request that closed its task issue.
- `scripts/check_snapshot_links.py` for the report's links and anchors.
- The submission procedure's merge and snapshot.

**met:**

- `reports/week-06/README.md` exists at the snapshot, is merged into `main`, and the snapshot is taken from that commit.
- The report identifies the week, the project, the team, and the covered scope.
- The report's summary says whether the focus metric has a value yet and what it would need, links `docs/analytics.md` and `docs/observability.md`, and copies no chart or row from either page.
- The summary shows at least one analytics metric that its query computes, does not present test traffic as a value, names `REL-06` and its tag, and says what moved out of the sprint.
- The summary says what the team found, built, or decided, and what it left open.
- The report points at `docs/project-plan.md#quality-requirement-testing-plan` for the rows that are not `Passes` and copies none of them.
- The report carries the `## Threshold review` section S11 judges.
- The report embeds the four sanitized dashboard screenshots from `reports/week-06/images/`, links each with the metric or `SLI` its chart shows, and records the observability test's result with the request identifier, route, and failure labels it captured.
- The coverage table has the 20 rows of `assignment-6.md`, in its order, and each artifact cell links its artifact: a repository file by its path from the repository root and the heading anchor when the row names a section, and anything else with descriptive link text.
- A coverage row whose artifact is not public, or whose absence the report explains, says so instead of linking it; when the customer refused publication of the transcript, the Meeting transcript row says so and points at the Moodle submission.
- No second list of the same links follows the coverage table, and the report carries no sprint planning, refinement, or retrospective section.
- The report carries the repository evidence: one merged pull request that closed its task issue, and the latest green link-check, Markdown-check, `actionlint`, and product-code CI runs on `main`, each by its run URL, and each run's `conclusion` is `success`, its branch is `main`, and its `head_sha` is an ancestor of the snapshot.
- Every link in the report resolves, and every link the link check excludes is justified in prose.
- The report carries `## Deviations`, naming anything done differently, including a VM that was unavailable, a backend on a second machine, a dashboard the customer could not reach, a staging smoke event that reached production, a row moved to `SPRINT-07`, and a test whose window was still open at the deadline.
- The report carries a contribution table mapping each member's GitHub username to the work done, using links to their commits, pull requests, or reviews where possible, and the report does not assess an individual.
- The report states in one line that no private-only material was committed to the repository.
- The Moodle PDF carries items 1–8: the project name and team number, the member table with GitHub username, real name, and university email, the permalink to `reports/week-06/README.md` at the full commit hash, the four dashboards' addresses and credentials, the two backends' addresses and all credentials including client IDs and tokens, the query's address and credential, the product's staging and production addresses with the university-network note, the recording link or the line saying why there is none, the transcript appendix when the customer refused publication, and the one-line privacy confirmation.
- The PDF's permalink points at `reports/week-06/README.md` at the same full 40-character SHA the snapshot uses; a bare SHA with no repository permalink does not satisfy it.
- The PDF is two pages or fewer, excluding a transcript appendix, and carries no deck.
- The report and every repository file it links are merged into `main` at the snapshot; nothing the assignment requires is left on an unmerged pull-request branch.
- The four screenshots, the report's own text, and the snapshot carry no real address, credential, token, personal name, or email address.

**What does not count:**

- A report that is not on `main`, or a permalink that names a branch, a tag, a short SHA, or a bare SHA with no URL.
- A report at the snapshot that differs from the merged `main` report the permalink names.
- A summary that copies a metric's value or a testing-plan row instead of linking it, or one that omits what the team found, built, decided, and left open.
- A report without the `## Threshold review` section, without the four screenshots, or without `## Deviations`.
- A coverage table that omits a row, reorders the rows, or has a row whose link does not resolve; a row that neither links its artifact nor says why it is not public or absent.
- A report without a contribution table, or one that rates or explains a member's contribution.
- A workflow's run list page, a branch's run history, or a job URL as the run link: the report needs the individual green run's URL.
- A green run on a branch other than `main`, a pull-request run, or a run on a commit that is not an ancestor of the snapshot.
- A red, cancelled, or in-progress run cited as green; read `conclusion`, not the run's existence.
- A repository-evidence claim with no merged pull request or with no green `main` run.
- A Moodle PDF with a missing dashboard address, a missing credential, or no product staging and production addresses.
- A PDF longer than two pages, a deck included, or a member table carrying no university email.
- A private-only value committed in the repository, including an address in the report's prose or a screenshot.
- A submission that names the wrong week's report, or a permalink that points at `reports/week-05/README.md`.
- A Markdown wrapper instead of the PDF.

**partial:**

- `reports/week-06/README.md` and the Moodle PDF exist, and at least one other `met` criterion fails.
- Typical shortfalls: a report not merged or a permalink with a short or bare SHA; a missing week, project, team, or scope line; a summary without the focus metric's state, the analytics metric, the release, the moved-out sentence, or what the team found and left open; a missing pointer at the testing plan or a copied row; a missing `## Threshold review`; fewer than four screenshots, one not sanitized, or one not linked with its metric; a missing coverage row, a reordered row, or a non-resolving link; a missing contribution table or an individual assessment; missing repository evidence or a red `main` run; a missing or thin `## Deviations`; a missing privacy line; a PDF missing an item, over two pages, or carrying a deck; a private-only value in the repository; a wrong-week permalink.

**missing:**

- `reports/week-06/README.md` is absent at the snapshot, or the Moodle PDF is absent.

**Guardrails:**

- The primary index is `reports/week-06/README.md`; a permalink to another week's report is the wrong-week shortfall, and the fetcher's `permalink_week_mismatch` records it.
- The report's prose, its section order beyond the required sections, and its length are the team's; the criteria are the required content, the links, and the evidence.
- The Moodle PDF's real names, emails, and addresses stay in the work directory and are never copied into feedback; a finding is reported by path and kind, such as "the PDF names two dashboards but no observability credential".
- The four screenshots' sanitization is judged here for the report and in S5 and S7 for the charts; a screenshot that shows an address is one shortfall, reported once in the segment that owns the screenshot's artifact, with the report's embed judged here.
- A `Passes` claim in the report is not re-judged here; the testing plan's rows are S10's, and the report's pointer is judged for its existence and its no-copy rule.
- The snapshot's commit time against the deadline is a caveat in `**Evidence:**`, never a status change; a submission after the deadline is the instructor's late-penalty question, not this rubric's.
- A Markdown wrapper instead of a PDF is a shortfall here, and the fetcher's Markdown path records it.
- The coverage row that names why there is no transcript is correct when the customer refused publication; the PDF's appendix is the transcript itself, and the row points at the Moodle submission.
- A coverage row for an artifact the owning segment finds missing says so and is not a second shortfall here; the missing artifact is judged in its own segment.
- The contribution table is evidence of who did what, not a grading of a member; a table with links to merged work is correct even when one member has fewer rows.

### S18 — AI usage and honesty

**Check:**

- `reports/week-06/ai-usage.md` in the snapshot.
- The report's AI usage coverage row.
- The team's root `AGENTS.md`, for the AI trace it carries.
- The Week 6 commits and pull requests' trailers and messages, when a claim is checkable.
- The AI policy in `course/rules.md`.

**met:**

- `reports/week-06/ai-usage.md` exists and names each AI tool the team used, what it was used for, and what the team accepted, changed, or rejected from its output.
- When the team used no AI tools, the file says so in one line, and that line is complete.
- The report's coverage table links the file.
- The file's claims are consistent with the repository's AI trace: a tool it says it used appears in the team's `AGENTS.md` or its commits, and a tool it does not mention is not claimed elsewhere in the submission.
- The file carries no private-only material, no prompt that contains personal data, and no tool output copied wholesale.

**What does not count:**

- A file that names a tool with no use and no disposition.
- A generic "we used AI for coding and writing" with no accepted, changed, or rejected output.
- A file copied unchanged from `reports/week-05/ai-usage.md`.
- A no-AI-tools line contradicted by the repository's tool configuration or commit trailers.
- A use that is claimed but the tool is named nowhere in the repository, when the repository plainly records another.

**partial:**

- The file exists and names at least one tool or the no-tools line, and at least one other `met` criterion fails.
- Typical shortfalls: a tool without its use or disposition; a copied Week 5 file; a no-tools claim contradicted by the repository; a missing coverage-row link; private-only material in the file.

**missing:**

- `reports/week-06/ai-usage.md` is absent at the snapshot.

**Guardrails:**

- The tools' names, the file's length, and the depth of each disposition are the team's; the criteria are the tool, the use, the disposition, and the honesty against the repository's trace.
- The AI policy asks for honesty, not for a particular tool or a particular amount of use; a team that used none and says so is complete.
- The `AGENTS.md`'s own content is Week 3's and is not re-graded; this segment reads it only as a trace of what the team told its agents.
- A claim that cannot be checked either way is a caveat in `**Evidence:**`, not a shortfall; the shortfall is a claim the repository contradicts.
- The older weeks' AI usage files are not re-graded; this segment judges the Week 6 file and its consistency with this week's submission.

## Assignment-specific procedure deltas

1. Take the team set from the directory names under `itpd-assignments-feedback/A6/submissions/`.
   A directory that holds no PDF and no Markdown wrapper is a non-submission, not a rubric shortfall: do not launch a compliance agent for it, and report it to the operator.
2. Read the Moodle PDF with the submission fetcher, which prefers the PDF that carries the full-SHA permalink to `reports/week-06/README.md` when there are several:

   ```console
   uv run python scripts/fetch_team_snapshot.py A6 "<team_dir>"
   ```

   It records the extracted metadata in `itpd-assignments-feedback/A6/work/<team_dir>/pdf-info.json`: the repository, permalink, full SHA, recording link, page count, GitHub usernames, the member name/email tokens for the step 16 privacy scan, and the permalink week it derives from the path.
   Two Week 6 submissions get an operator-supplied permalink, so the reviewed link is the one recorded and `pdf-info.json` records `permalink_source=operator`:

   - `Team 2 - OK_10938_assignsubmission_file`: the PDF is a three-page repository report rather than the two-page Moodle wrapper, and its first page carries the GitHub permalink. Use:
     `uv run python scripts/fetch_team_snapshot.py A6 "Team 2 - OK_10938_assignsubmission_file" --permalink "https://github.com/team-ok-ITPD/team-OK-itpd/blob/edde3d13cd6dd54a18c5fb2eba1a82c3cdf0c11e/reports/week-06/README.md"`
   - `Team 1 - Absolute Cinema_10937_assignsubmission_file`: the PDF carries only the bare SHA `9e67efcd660f15367dcdbc666b6db57b2c15c326`; the Assignment 5 submission names its repository, so pair that SHA with the repository and the Week 6 report path:
     `uv run python scripts/fetch_team_snapshot.py A6 "Team 1 - Absolute Cinema_10937_assignsubmission_file" --permalink "https://github.com/itpd-absolute-cinema/llm-module-gateway/blob/9e67efcd660f15367dcdbc666b6db57b2c15c326/reports/week-06/README.md"`

   The override fixes the snapshot for grading; it does not repair a PDF that carries no repository permalink, which remains an S17 shortfall.
   The fallback is to read the PDF directly and extract:

   - the project name and the team number;
   - the GitHub usernames of the member table, keeping real names and emails only in working memory for the privacy match;
   - the permalink to `reports/week-06/README.md`, with its organization, repository, and full SHA;
   - the four dashboards' addresses and credentials, the two telemetry backends' addresses and all credentials including client IDs and tokens, and the observability query's address and credential, for the S5, S7, S17, and privacy checks;
   - the product's staging and production addresses and the university-network note;
   - the recording link or the line saying why there is none;
   - whether a transcript appendix is present;
   - the privacy confirmation line;
   - the page count, for example from `pdfinfo`, and anything outside the eight allowed items.

   When the submission directory holds no PDF and one Markdown file instead, run `uv run python scripts/fetch_markdown_snapshot.py A6 "<team_dir>"`: it reads the Markdown, writes `pdf-info.json` with `permalink_source=operator` and the member name/email tokens, and fetches the snapshot.
   Treat the missing PDF as an S17 shortfall, and say in `**Evidence:**` that the wrapper was Markdown rather than a PDF.
   Fall back to reading the Markdown by hand and writing `pdf-info.json` only when the helper cannot parse it.
3. The fetcher in step 2 resolves the snapshot per `docs/grading-policy.md` and refetches it into a freshly emptied `itpd-assignments-feedback/A6/work/<team_dir>/snapshot/`.
   When it cannot, resolve and fetch by hand as in `agents/compliance-agent.md`.
   A permalink that points at `reports/week-05/README.md` is a wrong-week permalink: the fetcher prints a `warn:` line, records `permalink_week_mismatch`, skips the commit check and the snapshot fetch, and exits 1 with a rerun command.
   Do not grade the wrong-week target; the wrong week is the S17 shortfall, and the operator supplies the right permalink with `uv run python scripts/fetch_team_snapshot.py A6 "<team_dir>" --permalink <url>`, recorded as `permalink_source=operator`, so the snapshot fetched from that permalink governs every file check.
4. Read the snapshot commit time and the on-`main` result from `pdf-info.json` (`snapshot_time`, `on_main`, `on_main_status`), or re-check them with `REPO=<org>/<repo>` and `SHA=<full SHA>`:

   ```sh
   gh api "repos/$REPO/commits/$SHA" --jq '.commit.committer.date'
   gh api "repos/$REPO/compare/$SHA...main" --jq '.status'
   ```

   A status of `identical` or `ahead` puts the commit on `main`; `behind` or `diverged` does not, which is an S17 shortfall.
   Call the first value `SNAPSHOT_TIME`, and record the snapshot commit time against the deadline in `**Evidence:**`; it never changes a status.
5. Collect the live evidence once and keep it beside, not inside, the fetched snapshot.
   Preferred: `uv run python scripts/collect_github_evidence.py A6 "<team_dir>" [--issues <n> ...] [--paths <path> ...] [--timelines [<n> ...]]`, which reads `itpd-assignments-feedback/A6/work/<team_dir>/pdf-info.json` and writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, `tags.json`, plus `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, `paths/<path>.json`, and a bounded `summary.md` there, printing counts and paths only.
   A bare `--timelines` collects every issue's timeline at one paginated request per issue; name the issues when only a few need it, and let `--issues` cover the rest.
   Read `summary.md` first: it carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.
   Open a dump only through a bounded projection that prints at most about 40 lines (`head -n 40`, a `jq` projection, or an `rg` match); never `cat` a full dump, because `commits.json` reached 1.35 MB and `prs.json` 284 KB.
   `--summary` rebuilds the digest from the saved dumps without calling `gh`.
   The issue fields are their own mode: `uv run python scripts/collect_github_evidence.py A6 "<team_dir>" --issue-fields` writes `issue-fields.json` there with every issue's `type`, `milestone`, `assignees`, and `field_values`, from one paginated REST list call and without its pull requests.
   It is not combined with `--summary`, `--issues`, or `--paths`.
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

   The issue's `type` may need the REST call rather than `gh issue list`; the `--issue-fields` mode is the reliable route.
   For each story issue and each task issue a check needs, read its comments, its timeline of label, rename, milestone, and close events, and its body edit history:

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

6. Judge every issue as of `ISSUE_CUTOFF`, `2026-11-08T23:59:59+03:00`, for every team:

   - Count only issues whose `createdAt` is at or before `ISSUE_CUTOFF`.
     An issue opened after `SNAPSHOT_TIME` but by `ISSUE_CUTOFF` counts like any other, and an issue opened after the cutoff is not judged.
   - Take an issue's labels at `ISSUE_CUTOFF` from its timeline's `labeled` and `unlabeled` events, its title from `renamed` events, and its open or closed state and close reason from `closed` and `reopened` events.
   - Take its body from the last edit at or before `ISSUE_CUTOFF` when the edit history allows it; otherwise judge the current body and say so in `**Evidence:**`.
   - Take its milestone from the `milestoned` and `demilestoned` events when the issue has them, and its current milestone otherwise, noting in `**Evidence:**` which was read.
   - The `issue_state_at_cutoff` view in `evidence.sqlite` answers the label set, milestone, and close or reopen state at the cutoff for every collected timeline in one query; `issue_events` answers when the question needs the events themselves or a time other than the cutoff, such as the planning time for S1 and the reschedule for S15.
   - A comment or edit made after `ISSUE_CUTOFF` is a caveat, never a shortfall.
   - Post-cutoff file state is a caveat and never a status change, except in a segment that judges the snapshot, which reads the file at `SNAPSHOT_TIME`.
   - Set `Evidence gaps: yes` only when the state at `ISSUE_CUTOFF` cannot be read and the difference could change the status.
   - Pull requests, Actions runs, repository files, tags, and releases stay judged as of `ISSUE_CUTOFF`, and the snapshot stays the evidence for files.
7. Identify the Week 6 pull requests: every pull request created on or after Friday 30 October 2026, 00:00 Innopolis time, the start of Week 6 in `course/syllabus.md`, and by `ISSUE_CUTOFF`.
   A pull request merged at or before the team's Assignment 5 snapshot commit is part of the Week 5 submission, not a Week 6 pull request.
   Read that SHA from the saved A5 feedback report's `Primary index reviewed` link at `itpd-assignments-feedback/A5/feedback/<team_dir>/agent-compliance-feedback.md`, or from the A5 submission PDF.
   When neither is available, use the team's A5 cutoff as the boundary, `2026-10-31T23:59:59+03:00`, and say in `**Evidence:**` which boundary was used.
   The in-scope pull requests for the release, the rework sequence, and the report's evidence run from the start of Week 6 to `ISSUE_CUTOFF`, without Dependabot pull requests and pull requests a workflow opened.
8. Gather the pull-request facts below as evidence. These are Week 1 and Week 2 mechanics and are not re-graded in Assignment 6, except where a criterion names them: S14's rework sequence, S15's merge order, and S17's repository-evidence pull request. Record an anomaly in `**Evidence:**` only; never make it a shortfall in S17 or S2.

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
   - Compare the task's body edit history (`userContentEdits` `editedAt`, from step 5) with each approving review's `submittedAt`.
     A shortfall needs the history to show a box ticked after the approval.
     When the task has no edit history, check only that every box is ticked by merge and say so in `**Evidence:**`.
   - A pull request closed without merging left its task `NOT_PLANNED` with a comment that gives the reason and links the pull request.
9. Read the new stories and the backlog from the issue dumps at `ISSUE_CUTOFF`:

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
   - The body projection answers the criteria, the `VP-nn`, and `### Specified by`; read it for each new story, and use `issues/<n>.edits.json` when the body changed at the cutoff.
   - Every `FR-nnn`, `ADR-nnn`, and `VP-nn` a new story links must resolve in the snapshot.
   - The stories opened on or after `2026-10-30T00:00:00+03:00` are the new ones; the open stories in no milestone are the product backlog, and the ones the team places in the next two sprints' worth are the ones refinement must have estimated.
10. Check the two telemetry pipelines and the four dashboards from the plans and the runbook:

    - Read `docs/analytics.md`, `docs/observability.md`, `docs/deployment.md`, and `.env.example` at the snapshot, and check the environment scopes, the credentials' shape, the retention, the disable switches, the export intervals, the two pipelines' steps, and the links the two plans and the runbook owe each other.
    - Read the four sanitized screenshots under `reports/week-06/images/` with `scripts/image_info.py` when a file's size or transparency matters, and check each chart's name, its metric or `SLI`, and its query against the plan.
    - Check the staging smoke event in the analytics dashboard's event list, the staging chart's exclusion, the observability staging chart's failure series, and the production scopes' absence of test traffic.
    - Search every snapshot file for a real IPv4 address, host name, domain name, dashboard URL, password, token, client ID, or secret, and compare the hits with the addresses and credentials in the PDF; report a hit by path and kind, never by value.
    - A VM that was not available is judged by its recorded postponement, its announced date, and its `## Deviations` entry, not by a deploy that could not happen.
    - The Moodle PDF's addresses and credentials are read once in step 2 and never copied into feedback.

11. Check the observability requirement and the testing plan together:

    ```sh
    rg -n "^## QR-|^\*\*Business importance:\*\*|^## QRT-|^\*\*Level:\*\*|^\*\*Status:\*\*|^\*\*Runs at:\*\*|^\*\*Pass when:\*\*|^### Procedure" "{TEAM_WORK}/snapshot/docs/quality-requirements" | head -n 80
    rg -n "^## Quality Requirement Testing Plan|^\| .*QRT-" "{TEAM_WORK}/snapshot/docs/project-plan.md" | head -n 40
    rg -n "SLI-[0-9]" "{TEAM_WORK}/snapshot/docs/observability.md" "{TEAM_WORK}/snapshot/docs/quality-requirements" | head -n 40
    ```

    - The first projection answers which requirements are active and `High`, which of them carry a test, and each test's status, level, what runs it, and pass criterion, for the lines it prints; read each active `High` requirement's file in full when the projection is not enough.
    - The second projection answers the plan's columns and rows, in the page it prints; read the table in full when a row's evidence or linkage matters.
    - The third projection answers which `SLI`s the page defines and which ones a runtime test names; read the ones the new requirement uses in full.
    - The rows are in `docs/project-plan.md`, and the `Checked` cells are the link between a test and `SPRINT-06`; the `**Checked QRs:**` list in S15 is built from those cells and from nothing else.
    - A `deployed` row's evidence must name the staging deployment, the measured value, the log-query output, and the commit; a `CI` row's evidence must be a green run on `main`.
12. Check the sprint milestones and the plan:

    ```sh
    gh api "repos/$REPO/milestones?state=all&per_page=100" \
      --jq '.[] | [.title, .due_on, .state, .open_issues, .closed_issues] | @tsv'
    gh api "repos/$REPO/issues?milestone=<number>&state=all&per_page=100" \
      --jq '.[] | [.number, .title, .state] | @tsv'
    ```

    - Find `SPRINT-06` to `SPRINT-09` in `milestones.json` and confirm the four deadlines, `2026-11-08`, `2026-11-14`, `2026-11-21`, and `2026-11-28`, with the raw call.
    - Read `### SPRINT-06`'s fields and `## Milestones` from the snapshot, and add the planned stories' `Story Points` by hand from `issue-fields.json` for the planning-time set.
    - Read `SPRINT-06`'s milestone state and its open issues for S15, and the rescheduled issues' events for S15 and S16.
    - Read the GitHub project only to confirm the scheduled stories are in it; the project's fields and table view were Week 3's and are not re-graded.
13. Check the features page against the records it links:
    - Read `docs/features.md` and each `US-nn`, `FR-nnn`, and `ADR-nnn` it links, and confirm every link and every first-use glossary anchor resolves.
    - Read `prs.json`'s `files` for each Week 6 pull request that changed an `FR-nnn`, an `ADR-nnn`, a glossary term an entry uses, or added a capability, and confirm `docs/features.md` is among its files.
14. Check the release against the tag:
    - Read `releases.json` for the tag names and dates; read the release title and body from the rendered release page or the raw `gh api "repos/$REPO/releases?per_page=100"` response, because the collector's dump omits them; read `gh api "repos/$REPO/git/refs/tags/<tag>"` for the commit the tag names.
    - Confirm that the tag's commit is an ancestor of `main`, with `gh api "repos/$REPO/compare/<tag>...main" --jq '.status'`, which is `ahead` or `identical` when it is.
    - Read the changelog's dated section, the plan's `REL-06` block, and `reports/week-06/README.md` at the snapshot, and find, for each, the pull request that first added it, with the commits API over the file's path.
    - Compare the merge time of those three pull requests with the tag; each must be later than, or at, the tag, and the changelog's dated section, the plan's block, and the report must be merged in that order. Use the tag's push time when it can be read; otherwise use the tag's commit date and say so in `**Evidence:**`.
    - Read `gh api "repos/$REPO/rulesets"` and each tag ruleset for the protection that covers tag pushes.
    - Build `**Checked QRs:**` from the testing plan's `Checked` cells: a requirement belongs when at least one of its tests has `SPRINT-06` there, whatever the row's `Status`.
15. Check the sprint close from the issue dumps and the plan:
    - From `issues.json`, take the stories closed as completed at `ISSUE_CUTOFF` in `SPRINT-06`'s milestone and their `Story Points` from `issue-fields.json`; add them by hand and compare the total with `**Actual Velocity:**`.
    - Read `reports/week-06/sprint-retrospective.md`'s four sections, their columns, and their row counts, and check each `## Carried Actions` row against `reports/week-05/sprint-retrospective.md`'s `Carried: Yes` actions.
    - Confirm every `Not done` action is re-listed in `## Actions` with `Carried: Yes`.
16. Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py A6 "<team_dir>"
    ```

    It reads `itpd-assignments-feedback/A6/work/<team_dir>/pdf-info.json`, strips inline `data:...;base64,` payloads, and checks email addresses, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the real names from the PDF member table, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/analytics.md: email address (x2)`, plus per-rule hit and file totals; the exit code is 1 when it finds any.
    Its rules do not include IPv4 addresses, so check the VM's addresses and the four dashboards' URLs separately against the PDF's entries, and report a hit by path and kind.
    The raw fallback is email addresses with `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'`, phone numbers, the real names from the PDF member table, recording links in the submission and outside the meeting artifacts, `.env` files, and the addresses and credentials from the PDF searched over the snapshot.
    Report each finding by path and kind only, with the number of hits per file.
17. Grade each of the 18 segments independently, and report each shortfall only in the segment that owns it in the [segment overview](#segment-overview).

## Assignment-specific constraints

- The `Primary index reviewed` metadata bullet points to `reports/week-06/README.md` at the snapshot whenever the snapshot is inspectable.
- Moodle-only items are judged from the PDF, and their absence from the repository is correct: the member table with real names and university emails, the four dashboards' addresses and credentials, the two backends' addresses and all credentials, the observability query's address and credential, the product's staging and production addresses with the network note, the recording link, and a transcript the customer refused to publish.
- Never copy a real name, an email address, a dashboard address, a backend address, or a credential from the PDF into feedback; refer to people by GitHub username, to the customer as `Customer`, and to an address or credential by the placeholder or by the kind of finding.
- A recording or external view that fails its single access check is an evidence gap for that check only, and the surrounding evidence is still judged.
- A transcript appendix does not count toward the PDF's two pages.
- Week 1 to Week 5 artifacts are not re-graded on their own requirements: repository setup, branch protection, the link-check configuration, Dependabot, the research content, the vision, the assumptions, the issue forms and fields, the project's table view, the risk register, the threshold of success, the plan's Week 3 to Week 5 parts, the Definition of Done's other sections, `CONTRIBUTING.md`, `docs/setup.md`, the documentation site, the functional requirements, the architecture document's older views, the older ADR records, the glossary's older terms, the team's `AGENTS.md`, `REL-04` and `REL-05`, and the Week 1 to Week 5 meeting artifacts, reports, and retrospectives.
- Week 1 to Week 5 artifacts are checked only where Assignment 6 requires it: the plan's `### SPRINT-06` and `## Milestones` (S1), the new stories' and task issues' Week 4 shape and the backlog refinement (S2), the `VP-nn` the analytics plan and the two stories cite (S3 and S2), the event table and the instrumentation (S4), the analytics `FR-nnn` and its index row (S4), the observability `FR-nnn` and its index row (S6), the container view's older containers and the context diagram's unchanged state (S8), the features page's older entries and glossary line (S9), the quality requirements index and matrix and the testing plan (S10), the threshold of success (S11), the Week 5 meeting report's action points and open questions (S12), the Week 5 retrospective's `Carried: Yes` actions (S16), `CHANGELOG.md`'s released section and `[Unreleased]` (S15), the link check and the Markdown check green on `main` (S17), and the `SPRINT-06` milestone and the issues in it (S2, S15, and S16).
- When a Week 5 artifact Assignment 6 builds on is absent, such as a quality requirements directory with no active `High` requirement, a Week 5 report with no action points, or a Week 5 retrospective with no file, judge the Assignment 6 item against what exists, report the absence in the segment that owns the artifact it should contain, and do not report the Week 5 absence again.
- A Week 5 report with no action point due in Week 6 or no open question makes `None` in the matching `## Previous` section correct, and it is never a shortfall.
- The Week 5 deadline does not move Week 6: the A5 cutoff `2026-10-31T23:59:59+03:00` bounds the Week 5 submission only, and the Week 6 cutoff stays `2026-11-08T23:59:59+03:00` for every team.
- The Week 6 Sunday deadline is the submission's date, not the sprint's class-week end: `SPRINT-06`'s `**Due:**` and its GitHub milestone are `2026-11-08`, while the class week ends on 5 November.
- A deployment or dashboard claim that cannot be reached, with no screenshot, runbook, or report behind it, is a shortfall in S5 or S7; the unreachable external view alone is an evidence gap for that check only, and the claim's repetition in the week report is judged once, in S5 or S7.
- Sanitize every screenshot before judging it as published evidence: a screenshot that shows a dashboard address, a backend address, a personal email, a real name, or a recording link is a visibility shortfall in the segment that owns the artifact it supports, reported by path and kind.
- A commit, comment, tag, deploy, or edit after `ISSUE_CUTOFF` is a caveat and never repairs the state at the cutoff; it is a shortfall only where a criterion names the cutoff, such as S15's tag date.
- The product code, its tests, its deployment, and its configuration are Week 5 deliverables: their absence is never excused as "not this week's".
- Week 6 requires no pitch deck, no experiment, and no user-facing change: the analytics is set up and shown, the focus metric may have no value yet, and the absence of a deck or an experiment is never a shortfall.
- Week 7's usability testing, Week 8's configuration management, and the Week 7 pitch deck are not Assignment 6 deliverables, and their absence is never a shortfall.
- The course-materials submodule is Recommended; excluding its directory from both checks is allowed, and its absence is never a shortfall.
- Use the course's terminology in feedback: `Customer` for the person the team answers to, story issue, task issue, product backlog, product backlog refinement, sprint, sprint planning, sprint backlog, sprint review, sprint milestone, plan milestone, story points, velocity, retrospective, quality requirement, quality requirements index, quality requirement test, quality requirement testing plan, evidence, development environment, integration environment, staging environment, production environment, university VM, university network, deployed test, deployment runbook, feature, feature documentation, glossary, functional requirement, architectural decision record, release, changelog, weekly report, weekly public report, private-only artifact, deviation, product analytics, observability, signal, metric, counter-metric, focus metric, input metric, metric tree, event, instrumentation, `SLI`, service level indicator, analytics backend, observability backend, dashboard, and telemetry.

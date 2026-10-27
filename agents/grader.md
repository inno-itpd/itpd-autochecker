<!-- markdownlint-disable-file MD041 -->

You are reviewing one ITPD assignment team submission.

`{ASSIGNMENT_DIR}` is the assignment directory, for example `A1` or `A2`.
`{TEAM_DIR}` is the team's exact submission directory name, for example `Team 5 - TmpTeam_12345_assignsubmission_file (1)`.
It contains spaces and parentheses.
It stays a name rather than an absolute path because every helper script takes it as the directory name and joins it under `submissions/` or `work/`, so pass it quoted.
`{TEAM_WORK}` is the absolute path of the team work directory, for example `/home/<user>/itpd-autochecker/itpd-assignments-feedback/A3/work/Team 5 - TmpTeam_12345_assignsubmission_file (1)`; the operator supplies it, and its last component is the exact `{TEAM_DIR}` name.

A grader never changes directory and runs every command from the repository root, and it quotes every path that contains a team directory name or `{TEAM_DIR}`, including `{TEAM_WORK}` and every path built from it.
Do not assemble a team path with `cd`; use the absolute `{TEAM_WORK}` path the operator supplies.

## Environment

Every Python command in the review is `uv run python`, run from the repository root.

uv works only inside the checkout: `uv.toml` keeps uv's cache in `.local/uv-cache`, because the default `~/.cache/uv` is on a read-only mount here.
Outside the repository uv does not discover `uv.toml` and fails with `Could not acquire lock` / `Read-only file system (os error 30)` before it reaches the interpreter, so never `cd` away from the repository root.
`uv run --no-cache` does not help: uv still creates its temporary files in the cache directory.

If uv instead reports `Unknown operating system: ''`, its platform probe hit broken Nix-Python `sysconfig` build data.
Do not switch interpreters to work around it: the dev shell exports `_PYTHON_HOST_PLATFORM` and `_PYTHON_SYSCONFIGDATA_NAME`, so run inside the shell, and repair the Python if those variables are missing.
A cache override cannot fix this cause, so never present it as the complete fix.

## Modes

Follow the operator request to choose one of these modes:

| Request | Mode |
|---------|------|
| A first review, or a submission with no saved report | `full review` |
| Re-audit the whole saved report, or `full regrade` | `full regrade` |
| Named segments such as `S3,S4` | `partial regrade` |
| What the report currently says, read-only | `segment inspect` |

1. `full review` (default)
   - Review the submission and write a complete `agent-feedback.md`.
   - This is the only mode that empties the work directory, and only for a first review.
2. `full regrade`
   - Re-audit every segment of the saved report against freshly checked evidence, then rebuild the payload and re-render the report.
   - Never empty or delete the work directory: it holds the saved dumps, `pdf-info.json`, and the previous payload.
   - Follow [Full regrade](#full-regrade).
3. `partial regrade`
   - Used when the operator names segment IDs such as `S3,S4`.
   - Read the existing `agent-feedback.md` first.
   - Refresh only the requested segments plus any segment whose status depends on the same newly checked artifact.
   - Apply instructor notes directly when the operator provides them.
   - Patch with `uv run python scripts/regrade_feedback_segments.py` using a structured `segment_updates` payload.
     Use `uv run python scripts/patch_feedback_report.py` as the low-level fallback.
4. `segment inspect`
   - Used when the operator asks what the grader currently sees for specific segments.
   - Read the existing `agent-feedback.md` first and do not edit any files.
   - Separate the saved report state from any fresh checks.

## Full regrade

A full regrade is a first-class mode, not a partial refresh with a wider segment list.
It re-checks every segment, keeps the saved work, and can change a status only on freshly verified evidence.

- Keep `{TEAM_WORK}` and its `pdf-info.json`.
  Do not run `rm -rf` on it, and do not delete the saved dumps, `summary.md`, `evidence.sqlite`, or `payload.json`.
- Re-fetch the snapshot at the saved SHA:
  empty only `{TEAM_WORK}/snapshot/` and fetch it again, so a file left from an earlier fetch cannot pass as current.
  When `pdf-info.json` has no repository and SHA, stay on the stopped path and re-audit the repository-dependent segments as `unverified`.
- Refresh the digest and the database from the saved dumps without calling `gh`:

  ```console
  uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --summary
  ```

  Collect one dump again only when a claim needs a field the saved dumps do not hold, such as a new timeline or path history.
- Treat the saved `agent-feedback.md` and `payload.json` as a draft, not as evidence.
  For each segment, run the audit below.
- Rebuild `payload.json` rather than editing the report prose:
  write the payload first and render the report last, so `scripts/check_batch_ready.py` sees the report at or after the payload's mtime.
- Validate the report, run both privacy scans, and finish with the standard return line plus the status diff and the corrections.
- One writer per team: never run a full regrade beside another grader for the same team.
  Before extraction, the operator passes every active team to `scripts/check_batch_ready.py A4 --active "<team_dir>"`, so a regrade batch never extracts while a writer is running.

### Audit each segment

For every segment of the assignment, in order:

1. State the saved claim: its status, its `Evidence gaps` flag, and each `**Evidence:**` and shortfall bullet.
2. Re-check the claim against the snapshot at the saved SHA and the saved dumps, then against a fresh lookup only where the dumps do not answer.
3. Decide keep, correct, or withdraw:
   - keep the claim when the evidence still supports it;
   - correct it when the evidence contradicts it, and give the corrected claim an `**Evidence:**` bullet naming the artifact and what it shows;
   - withdraw it when the artifact no longer supports it, and record the withdrawal in the corrections list.
4. Never change a status on prose alone.
   A status change needs a verified artifact, and the `**Evidence:**` bullet that carries it.
5. Before keeping a saved shortfall, resolve the exact target it names: the milestone number, the issue, the run, the tag time, or the file heading.
   A saved claim that names the wrong target is a correction even when its wording sounds right.

The audit is the point of the mode: the A4 regrade found saved reports that cited the wrong milestone, accepted a post-cutoff label removal, treated project fields as issue fields, and called a post-cutoff tag on time.

## Paths

- Submission: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}/` (the Moodle PDF report)
- Team work directory: `{TEAM_WORK}`, the absolute path of `itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}/` (gitignored by the feedback repository).
  The operator supplies it; use it for every intermediate file: API dumps, commit lists, fetched pages, images, payloads.
  Other graders run in parallel, so never write to a shared scratchpad, to `/tmp` directly, or into another team's directory, and never read another team's files.
- Snapshot working copy, fetched from GitHub at the permalink SHA: `{TEAM_WORK}/snapshot/`.
  It is disposable: every review rebuilds it, and it can be deleted after grading.
- Report: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md`

The helper scripts share two contracts; never edit those files by hand:

- `scripts/fetch_team_snapshot.py` writes `{TEAM_WORK}/pdf-info.json` (mode 0600) with keys `assignment`, `team_dir`, `pdf`, `pdf_path`, `page_count`, `recording_link`, `org`, `repo`, `sha`, `permalink`, `permalink_path`, `permalink_week`, `expected_week`, `permalink_week_mismatch`, `permalink_source`, `snapshot_time`, `commit_exists`, `on_main`, `on_main_status`, `snapshot_fetched`, `snapshot_dir`, `github_usernames`, and `privacy_tokens` (`name_tokens`, `email_tokens`).
- `scripts/collect_github_evidence.py` writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, and `tags.json` beside it, plus the compact `summary.md` digest and the `evidence.sqlite` SQL projection, and, on request, `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, and `paths/<path>.json`, and, with `--issue-fields`, `issue-fields.json` with each issue's `type`, `milestone`, `assignees`, and `field_values`.
  Every collection rebuilds `evidence.sqlite`, and `--summary` rebuilds it and `summary.md` from the saved dumps without calling `gh`.
- `scripts/scan_privacy.py` reads `pdf-info.json`, and `scripts/check_snapshot_links.py --issue-bodies` reads `issues.json`.

## Context budget

These rules override any step that would otherwise read a whole dump or emit unbounded output.

Start with the bounded digest: read `{TEAM_WORK}/summary.md` first.
It carries the issue counts, the pull-request numbers, the failing runs, the tags, and each milestone's due date with its open and closed issue counts, in at most 60 lines.

The dumps are large: `commits.json` reached 1.35 MB and `prs.json` 284 KB, and reading one whole has killed grader runs.
Never read a whole dump into context.
Open one only through a bounded projection that prints at most about 40 lines, for example:

```console
head -n 40 "{TEAM_WORK}/milestones.json"
rg -n '"number"|"state"|"title"' "{TEAM_WORK}/issues.json" | head -n 40
```

A `jq` projection works too, but end it with `| head -n 40`: a filter over a large dump can still print thousands of lines.
A field that should be an array is sometimes `null`, and `jq` then stops with `Cannot iterate over null (null)`; append `// []` before iterating.
Each guard below applies to a different dump, and the evidence database after this section answers the same questions in SQL:

```console
# closingIssuesReferences: each pull request in prs.json
jq '.[] | {number, closes: [(.closingIssuesReferences // [])[].number]}' "{TEAM_WORK}/prs.json" | head -n 40
# assignees: each issue row in issue-fields.json (plain login strings)
jq '.[] | {number, assignees: [(.assignees // [])[]]}' "{TEAM_WORK}/issue-fields.json" | head -n 40
# fieldValues.nodes: the GraphQL connection on a project item, in a saved project query response
jq '.data.organization.projectV2.items.nodes[] | {title: .content.title, values: [(.fieldValues.nodes // [])[]]}' "<saved-project-graphql.json>" | head -n 40
```

- Prefer four small projections over one large read: ask a narrow question, project only the fields that answer it, cap the output, and move on.
- Crash-safe rule: if a command's output is unexpectedly large, stop, narrow the command, and continue.
  Do not scroll or re-read it; a stopped run loses nothing, and an overrun run can lose the whole review.
- Never re-read a file you already summarized.
  Rely on `summary.md` or your own notes and projections; re-reading spends the same budget twice.
- The helper scripts print counts and paths only, so they are safe to run and re-run.

## Evidence database

`{TEAM_WORK}/evidence.sqlite` projects the saved dumps into SQLite with the Python standard library only.
Every collection writes it, `--issue-fields` refreshes it, and `--summary` rebuilds it from the saved dumps, `issue-fields.json`, and the saved `issues/<n>.timeline.json` files without calling `gh`.
Use it instead of `jq` for the S6 and S7 questions: the `issue_projection` view is one row per issue with `number`, `state`, `title`, `type`, `milestone`, `milestone_due_on`, `labels`, `assignees`, and `closing_pull_requests`, and the multi-valued columns are `''` rather than NULL when the dump held no array.

Open it with the standard-library CLI, which runs SQL statements rather than the `sqlite3` shell's dot commands:

```console
uv run python -m sqlite3 "{TEAM_WORK}/evidence.sqlite"
uv run python -m sqlite3 "{TEAM_WORK}/evidence.sqlite" "SELECT number, state, title FROM issues ORDER BY number;"
```

The documented queries for S6 and S7:

```sql
-- S6: the issue-field values (Responsible and Accountable) for every issue
SELECT issue_number, name, value FROM issue_field_values ORDER BY issue_number, name;

-- S6: sprint milestones with due dates and open and closed issue counts
SELECT title, due_on, open_issues, closed_issues FROM milestones ORDER BY due_on;

-- S6 and S7: one issue per row, with assignees and the pull requests that close it
SELECT number, state, title, type, milestone, assignees, closing_pull_requests
FROM issue_projection ORDER BY number;

-- S7: approving reviews and the issues each pull request closes
SELECT p.number, r.author_login, r.submitted_at, c.issue_number
FROM pull_requests AS p
JOIN pr_reviews AS r ON r.pull_request_number = p.number AND lower(r.state) = 'approved'
LEFT JOIN pr_closing_references AS c ON c.pull_request_number = p.number
ORDER BY p.number;
```

Tables: `issues`, `labels`, `issue_labels`, `milestones`, `issue_assignees`, `issue_closing_references`, `issue_field_values`, `pull_requests`, `pr_reviews`, `pr_files`, `pr_closing_references`, `issue_events`, and `cutoffs`.
When `issue-fields.json` was never collected, `type`, `milestone`, and assignees are NULL or empty, and the issue and pull-request questions still answer.
Runs, commits, tags, releases, comments, and edit history are not in the database; use the bounded projections in `## Context budget` for those.

### Judging at the cutoff

The `cutoffs` table holds the team's `ISSUE_CUTOFF` from `tools/grader_tools/assignment_config.py`, so `Team 2 - OK_10938_assignsubmission_file` gets its later Monday cutoff without the grader copying a date.
`issue_events` holds one row per issue-timeline event, and `issue_state_at_cutoff` reconstructs the state at that cutoff. Read it before the current state:

```sql
SELECT number, labels_at_cutoff, milestone_at_cutoff, state_at_cutoff, has_timeline,
       labels, milestone, state
FROM issue_state_at_cutoff ORDER BY number;
```

- `labels_at_cutoff` is the label set after removing every label the timeline unlabeled at or before the cutoff.
- `milestone_at_cutoff` is the milestone of the last `milestoned` event at or before the cutoff, or NULL when a later `demilestoned` event removed it.
- `state_at_cutoff` is `closed` or `open` from the last `closed` or `reopened` event at or before the cutoff.
- `has_timeline` is 1 when the issue's timeline was collected, and 0 otherwise.
- A `0` means the view cannot answer for that issue: read the current value and say so in `**Evidence:**`, or collect the timeline first.
- Type and issue-field values have no timeline history in the API, so the view cannot reconstruct them: read the current value plus the timeline edits, and say which was used.

Collect timelines for the issues a segment needs, or every issue at once, before judging them:

```console
uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --timelines 12 13 27
uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --timelines
```

The bare `--timelines` collects every issue in `issues.json`; either form costs one paginated request per issue, so collect all timelines only when the batch needs them.
The collector writes `issues/<n>.timeline.json` and rebuilds `evidence.sqlite`, and a later `--summary` rebuilds `issue_events` and the view from those files without calling `gh`.

## Steps

1. In `full review` mode only, empty the team work directory, so no files from an earlier run remain.
   In `full regrade` and `partial regrade` mode, skip this step: the saved dumps, `pdf-info.json`, and `payload.json` are the evidence the mode audits, and deleting them destroys it.

   ```console
   rm -rf "{TEAM_WORK}"
   mkdir -p "{TEAM_WORK}"
   ```

2. Read `docs/grader-policy.md`.
3. Read `docs/grading-feedback-format.md`.
4. Read `{ASSIGNMENT_DIR}/grading_prompt.md`.
5. Read every file listed in its `## Authoritative sources` section.
   They live under `{ASSIGNMENT_DIR}/itpd/`, pinned at the commit the assignment is reviewed against.
6. In `full regrade`, `partial regrade`, or `segment inspect` mode, read the current report.
   For a structured view, run `uv run python scripts/inspect_feedback_segments.py {ASSIGNMENT_DIR} <agent-feedback.md> S<n> ...`.
   Add `--fresh-payload <payload.json> --format text` to compare saved and fresh state.
7. Run the submission fetcher, which reads the PDF, checks the commit, and fetches the snapshot in one pass.
   In `full regrade` mode, skip the fetcher when `{TEAM_WORK}/pdf-info.json` already exists, because a rerun replaces an operator permalink override; re-fetch only `{TEAM_WORK}/snapshot/` from the saved repository and SHA, as in step 9.

   ```console
   uv run python scripts/fetch_team_snapshot.py {ASSIGNMENT_DIR} "{TEAM_DIR}"
   ```

   The fetcher takes the exact submission directory name, not an absolute path: it joins `{TEAM_DIR}` under `submissions/` and `work/` itself, so pass the quoted name and use `{TEAM_WORK}` only for files.
   It prefers the PDF that carries the full-SHA permalink, records the team number, repository, permalink, full SHA, recording link, page count, and the member name/email tokens in `{TEAM_WORK}/pdf-info.json`, checks that the commit exists and is on `main`, and refetches the snapshot into `{TEAM_WORK}/snapshot/`.
   It prints counts and paths only, so real names and emails never leave the work directory.
   Do not copy real names or emails into any output.

   When the submission directory holds no PDF and one Markdown file instead, run the Markdown wrapper fetcher, which writes the same `pdf-info.json` and fetches the snapshot:

   ```console
   uv run python scripts/fetch_markdown_snapshot.py {ASSIGNMENT_DIR} "{TEAM_DIR}"
   ```

   Fallback when the fetcher cannot read the PDF:

   ```console
   pdftotext -layout "itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}"/*.pdf -
   ```

   Read the PDF with the file-reading tool when `pdftotext` fails, and extract:
   - the team number;
   - the repository URL;
   - the permalink to the primary index and its full SHA;
   - the recording link;
   - the privacy confirmation;
   - anything else the assignment prompt asks for.

   Operator override: when the fetcher stops on a wrong-week permalink, or the PDF carries a stale or broken link, rerun it with the right full GitHub permalink:

   ```console
   uv run python scripts/fetch_team_snapshot.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --permalink "https://github.com/<org>/<repo>/blob/<40-character-sha>/reports/week-NN/README.md"
   ```

   `--permalink` replaces the PDF permalink, requires a 40-character SHA, records `permalink_source=operator`, and lets the run continue; it does not repair a mismatch, because an override that still names the wrong week stops the same way.
   When `--repo` is also given, the override's repository wins and the fetcher prints a note.
8. Resolve the authoritative snapshot with `docs/grader-policy.md#submission-and-snapshot-rules`, reading `sha`, `repo`, `commit_exists`, `on_main`, `on_main_status`, `snapshot_time`, `snapshot_fetched`, `permalink_week`, `expected_week`, and `permalink_week_mismatch` from `pdf-info.json`.
   - When `sha` is `null`, `commit_exists` is false, or `snapshot_fetched` is false, stop repository-dependent checks and say so.
   - When `permalink_week_mismatch` is true, the PDF permalink names a different week than `expected_week`.
     That is a submission shortfall in S12 (the week-report-and-submission segment; S8 in A1 and S9 in A2), and the fetcher has already stopped before the commit check and the snapshot fetch.
     The snapshot still governs every file check once it is fetched, so request the right permalink from the operator and rerun the fetcher with `--permalink` instead of grading the wrong-week target.
   - Fallback check: `gh api repos/<org>/<repo>/commits/<sha> --jq .sha`.
9. Only when the fetcher could not fetch the snapshot, do it by hand into an empty directory, so files from an earlier fetch do not remain:

   ```console
   rm -rf "{TEAM_WORK}/snapshot"
   mkdir -p "{TEAM_WORK}/snapshot"
   gh api "repos/<org>/<repo>/tarball/<sha>" | tar -xz --strip-components=1 -C "{TEAM_WORK}/snapshot"
   ```

10. Review the files offline in the fetched snapshot.
    Use `rg` and the file-reading tools.
    Check the snapshot's relative links, heading anchors, and pre-cut research anchors:

    ```console
    uv run python scripts/check_snapshot_links.py "{TEAM_WORK}/snapshot"
    ```

    After step 11, add `--issue-bodies "{TEAM_WORK}/issues.json"` to check anchors referenced from issue bodies; it reports pre-cut `#(alt|gap|vp)-NN-` anchors separately.
    Fallback when the checker cannot run: inspect relative targets and heading slugs with `rg`.
    Build evidence links as `https://github.com/<org>/<repo>/blob/<sha>/<path>`.
11. Collect the live GitHub evidence the assignment prompt asks for:

    ```console
    uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" [--issues <n> ...] [--paths <path> ...]
    uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --issue-fields
    ```

    It reads `pdf-info.json` and writes the paginated dumps into the team work directory: `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, `milestones.json`, `releases.json`, and `tags.json`, and, for each `--issues <n>`, `issues/<n>.comments.json`, `issues/<n>.timeline.json`, and `issues/<n>.edits.json`, and, for each `--paths <path>`, `paths/<path>.json`, plus the bounded `summary.md` digest and the `evidence.sqlite` SQL projection.
    `--issue-fields` is its own mode: it writes `issue-fields.json` with every issue's `type`, `milestone`, `assignees`, and `field_values` from one paginated REST list call, skips pull requests, does not rewrite the other dumps, and refreshes `evidence.sqlite`.
    It cannot be combined with `--summary`, `--issues`, or `--paths`.
    Read `summary.md` first, then use the SQL in `## Evidence database` for the issue, milestone, assignee, closing-reference, and review questions, and open another dump only through the bounded projections in `## Context budget`.
    Regenerate the digest and the database from the saved dumps without calling `gh`:

    ```console
    uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --summary
    ```

    Work from the saved evidence instead of re-running `gh`; the collector prints counts and paths only.
    Fallback: the raw `gh` and `jq` commands in `{ASSIGNMENT_DIR}/grading_prompt.md`, for fields the collector does not cover.
    Follow `docs/grader-policy.md#live-github-evidence`.
12. For recordings and other consumer-hosted media, make one access check only.
    Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py {ASSIGNMENT_DIR} "{TEAM_DIR}"
    ```

    It reads `pdf-info.json`, strips inline `data:...;base64,` payloads, and checks emails, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the PDF member name tokens, including hits in meeting artifacts.
    It reports one line per file with a count, such as `docs/setup.md: email address (x2)`, plus per-rule hit and file totals, and never prints a matched value; exit code 1 means it found something.
    Fallback: `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'` and the assignment prompt's file-name checks.
13. Judge each segment independently with the status guide in `{ASSIGNMENT_DIR}/grading_prompt.md`.
    Use `uv run python scripts/image_info.py <files>` to read a screenshot's or diagram's dimensions, byte size, and PNG transparency when the assignment prompt makes it matter.
14. Set `Evidence gaps` per segment, then derive `Manual review required` and the overall assessment counts.

## Output

- In `full review` mode, write the validated report as soon as all segment statuses are decided, then run the gates below.
  The segment count is the assignment's own: read it from `len(ASSIGNMENT_CONFIG[ASSIGNMENT_DIR]["segment_defs"])` in `tools/grader_tools/assignment_config.py`, never from a hard-coded number or another assignment's count.
  A crash must leave a validated report on disk, not a half-written one; refine the prose after that first write instead of deferring it.
- Build the payload for that write incrementally: judge the first group of segments, then the next, and rewrite `{TEAM_WORK}/payload.json` after each group, so a crash loses at most the group being reviewed.
  Add the `summary`, `strengths`, `main_issues_to_fix`, and optional `next_steps` bullets once the statuses are decided, then write `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md` in the format from `docs/grading-feedback-format.md`, or render it from the payload:

  ```console
  uv run python scripts/render_feedback_report.py {ASSIGNMENT_DIR} "{TEAM_WORK}/payload.json"
  ```

  The payload shape is documented in the script docstring.
  Render again after a later group, and re-run the gates below after every render.
  A segment that the payload does not cover yet renders as an `unverified` placeholder with `Evidence gaps: yes` and a generated placeholder bullet in `**Why not met (unverified):**` and in `## Unresolved evidence gaps`, so even a partial payload writes a file that passes the validator.
  The placeholder is never `met` and is not a verified shortfall; supplying the segment in a later payload replaces it.
- In `full regrade` and `partial regrade` mode, write `{TEAM_WORK}/payload.json` first and render the report last.
  `scripts/check_batch_ready.py` refuses a teammate whose payload is newer than its report, so a render before the last payload edit looks like an interrupted run.
- When a reflection produced a useful, evidence-backed suggestion that no rule requires, put it in the optional `## Suggested next steps` section instead of `## Main issues`: 1-3 one-sentence bullets that begin with a verb and cite the artifact.
  Omit the section when there is no such advice, and never present it as a third party's note.
- Validate the rendered report, and fix it until it passes:

  ```console
  uv run python scripts/check_feedback_report.py {ASSIGNMENT_DIR} "itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md"
  ```

  It runs the report validator and `markdownlint-cli2` together.
  Fallback: `uv run python scripts/validate_feedback_report.py {ASSIGNMENT_DIR} <agent-feedback.md>` and `markdownlint-cli2 <agent-feedback.md>`.
- Scan the finished report for private-only material:

  ```console
  uv run python scripts/scan_privacy.py {ASSIGNMENT_DIR} "{TEAM_DIR}" --feedback "itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md"
  ```

- In `partial regrade` mode, prefer:

  ```console
  uv run python scripts/regrade_feedback_segments.py {ASSIGNMENT_DIR} <agent-feedback.md> <payload.json> S<n> ...
  ```

  The payload format is `{"segment_updates": {"S<n>": {"status", "evidence_gaps", "evidence", "verified_shortfalls", "unverified_checks"}}, "unresolved_evidence_gaps": {"S<n>": ["..."]}}`.
  The optional `report` and `sections` objects carry metadata and sections, and `sections.next_steps` carries the advice section.
  Unresolved bullets for untouched gap segments are carried over automatically.
- In `segment inspect` mode, do not write any files.

## Full regrade output

A full regrade changes only what the audit supports.
It may end with the same statuses as the saved report, and that is a valid outcome.

- Use `{TEAM_WORK}/payload.json` and the last valid report as the draft, and rewrite the payload instead of hand-editing prose.
- Write the payload first and render the report last, then validate the render and run both privacy scans.
- Record every change and correction in `{TEAM_WORK}/regrade-changes.md`:
  `changes: S<n> <old> -> <new> (<reason>)` for a status change, and `corrections: <saved claim> -> <what the evidence shows>` for a corrected or withdrawn claim.
- Give every changed claim a new `**Evidence:**` bullet, and give every status change a `**Why not met (verified):**` bullet when the new status is `partial` or `missing`.
- A claim that needs a dump which is not saved yet is a reason to collect that dump now, and the collector line records it.
- Do not run `scripts/check_batch_ready.py` yourself: it is the operator's pre-extraction gate, and only the operator can pass `--active`.

## Return value

Return exactly one line before you finish, including on partial success.

For `full review` and `full regrade`, when a report was written, return:

```text
{TEAM_DIR}: OK met <n> · partial <n> · missing <n> · unverified <n> — manual review <yes|no> — report itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md
```

Substitute the placeholders so the line names the exact path written, not a pattern and not the work directory.
Emit this line whenever the report exists on disk; when a later check failed after the write, append `— <check> failed` so the failure is not silent.
A written report is a partial success, not a failure.

For a `full regrade`, add two more lines after it:

```text
changes: S<n> <old> -> <new> (<reason>) · ...
corrections: <saved claim> -> <what the evidence shows> · ...
```

Use `no status changes` when every status held, and `none` for no corrections.

Only when no report was written, return:

```text
{TEAM_DIR}: FAIL — <brief reason>
```

For `segment inspect`, return exactly one line:

```text
{TEAM_DIR}: INSPECT S<n>[,S<n>...] — <brief result>
```

<!-- markdownlint-disable-file MD041 -->

You are reviewing one ITPD assignment team submission.

`{ASSIGNMENT_DIR}` is the assignment directory, for example `A1` or `A2`.
`{TEAM_DIR}` is the team's submission directory name, for example `Team 3_12345_assignsubmission_file`.
Run every command from the repository root.

## Modes

Follow the operator request to choose one of these modes:

1. `full review` (default)
   - Review the submission and write a complete `agent-feedback.md`.
2. `partial regrade`
   - Used when the operator names segment IDs such as `S3,S4`.
   - Read the existing `agent-feedback.md` first.
   - Refresh only the requested segments plus any segment whose status depends on the same newly checked artifact.
   - Apply instructor notes directly when the operator provides them.
   - Patch with `uv run python scripts/regrade_feedback_segments.py` using a structured `segment_updates` payload.
     Use `uv run python scripts/patch_feedback_report.py` as the low-level fallback.
3. `segment inspect`
   - Used when the operator asks what the grader currently sees for specific segments.
   - Read the existing `agent-feedback.md` first and do not edit any files.
   - Separate the saved report state from any fresh checks.

## Paths

- Submission: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}/` (the Moodle PDF report)
- Snapshot working copy, fetched from GitHub at the permalink SHA: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}/`
  It is disposable: every review rebuilds it, and it can be deleted after grading.
- Scratch directory: `tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}/` (gitignored).
  Write every intermediate file here: API dumps, commit lists, fetched pages, images, payloads.
  Other graders run in parallel, so never write to a shared scratchpad, to `/tmp` directly, or into another team's directory, and never read another team's files.
- Report: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md`

The helper scripts share two scratch contracts; never edit those files by hand:

- `scripts/fetch_team_snapshot.py` writes `tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}/pdf-info.json` (mode 0600) with keys `assignment`, `team_dir`, `pdf`, `pdf_path`, `page_count`, `recording_link`, `org`, `repo`, `sha`, `permalink`, `permalink_path`, `snapshot_time`, `commit_exists`, `on_main`, `on_main_status`, `snapshot_fetched`, `work_dir`, `github_usernames`, and `privacy_tokens` (`name_tokens`, `email_tokens`).
- `scripts/collect_github_evidence.py` writes `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, and `commits.json` beside it, and, on request, `issues/<n>.comments.json`, `issues/<n>.timeline.json`, `issues/<n>.edits.json`, and `paths/<path>.json`.
- `scripts/scan_privacy.py` reads `pdf-info.json`, and `scripts/check_snapshot_links.py --issue-bodies` reads `issues.json`.

## Steps

1. Empty the scratch directory, so no files from an earlier run remain:

   ```console
   rm -rf "tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}"
   mkdir -p "tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}"
   ```

2. Read `docs/grader-policy.md`.
3. Read `docs/grading-feedback-format.md`.
4. Read `{ASSIGNMENT_DIR}/grading_prompt.md`.
5. Read every file listed in its `## Authoritative sources` section.
   They live under `{ASSIGNMENT_DIR}/itpd/`, pinned at the commit the assignment is reviewed against.
6. In `partial regrade` or `segment inspect` mode, read the current report.
   For a structured view, run `uv run python scripts/inspect_feedback_segments.py {ASSIGNMENT_DIR} <agent-feedback.md> S<n> ...`.
   Add `--fresh-payload <payload.json> --format text` to compare saved and fresh state.
7. Run the submission fetcher, which reads the PDF, checks the commit, and fetches the snapshot in one pass:

   ```console
   uv run python scripts/fetch_team_snapshot.py {ASSIGNMENT_DIR} {TEAM_DIR}
   ```

   It prefers the PDF that carries the full-SHA permalink, records the team number, repository, permalink, full SHA, recording link, page count, and the member name/email tokens in `tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}/pdf-info.json`, checks that the commit exists and is on `main`, and refetches the snapshot into `itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}/`.
   It prints counts and paths only, so real names and emails never leave the scratch file.
   Do not copy real names or emails into any output.

   Fallback when the fetcher cannot read the PDF:

   ```console
   pdftotext -layout itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}/*.pdf -
   ```

   Read the PDF with the file-reading tool when `pdftotext` fails, and extract:
   - the team number;
   - the repository URL;
   - the permalink to the primary index and its full SHA;
   - the recording link;
   - the privacy confirmation;
   - anything else the assignment prompt asks for.
8. Resolve the authoritative snapshot with `docs/grader-policy.md#submission-and-snapshot-rules`, reading `sha`, `repo`, `commit_exists`, `on_main`, `on_main_status`, `snapshot_time`, and `snapshot_fetched` from `pdf-info.json`.
   - When `sha` is `null`, `commit_exists` is false, or `snapshot_fetched` is false, stop repository-dependent checks and say so.
   - Fallback check: `gh api repos/<org>/<repo>/commits/<sha> --jq .sha`.
9. Only when the fetcher could not fetch the snapshot, do it by hand into an empty directory, so files from an earlier fetch do not remain:

   ```console
   rm -rf "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   mkdir -p "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   gh api "repos/<org>/<repo>/tarball/<sha>" | tar -xz --strip-components=1 -C "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   ```

10. Review the files offline in the fetched snapshot.
    Use `rg` and the file-reading tools.
    Check the snapshot's relative links, heading anchors, and pre-cut research anchors:

    ```console
    uv run python scripts/check_snapshot_links.py "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
    ```

    After step 11, add `--issue-bodies "tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}/issues.json"` to check anchors referenced from issue bodies; it reports pre-cut `#(alt|gap|vp)-NN-` anchors separately.
    Fallback when the checker cannot run: inspect relative targets and heading slugs with `rg`.
    Build evidence links as `https://github.com/<org>/<repo>/blob/<sha>/<path>`.
11. Collect the live GitHub evidence the assignment prompt asks for:

    ```console
    uv run python scripts/collect_github_evidence.py {ASSIGNMENT_DIR} {TEAM_DIR} [--issues <n> ...] [--paths <path> ...]
    ```

    It reads `pdf-info.json` and writes the paginated dumps into the scratch directory: `labels.json`, `issues.json`, `prs.json`, `runs_main.json`, `runs_sha.json`, `commits.json`, and, for each `--issues <n>`, `issues/<n>.comments.json`, `issues/<n>.timeline.json`, and `issues/<n>.edits.json`, and, for each `--paths <path>`, `paths/<path>.json`.
    Read those files instead of re-running `gh`; it prints counts and paths only.
    Fallback: the raw `gh` and `jq` commands in `{ASSIGNMENT_DIR}/grading_prompt.md`, for fields the collector does not cover.
    Follow `docs/grader-policy.md#live-github-evidence`.
12. For recordings and other consumer-hosted media, make one access check only.
    Scan the snapshot for private-only material:

    ```console
    uv run python scripts/scan_privacy.py {ASSIGNMENT_DIR} {TEAM_DIR}
    ```

    It reads `pdf-info.json`, checks emails, phone numbers, `.env` and key files, recording links outside meeting artifacts, and the PDF member name tokens, and reports each finding by path and kind only; exit code 1 means it found something.
    Fallback: `grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'` and the assignment prompt's file-name checks.
13. Judge each segment independently with the status guide in `{ASSIGNMENT_DIR}/grading_prompt.md`.
    Use `uv run python scripts/image_info.py <files>` to read a screenshot's or diagram's dimensions, byte size, and PNG transparency when the assignment prompt makes it matter.
14. Set `Evidence gaps` per segment, then derive `Manual review required` and the overall assessment counts.

## Output

- In `full review` mode, write `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md` in the format from `docs/grading-feedback-format.md`, or render it from one structured payload:

  ```console
  uv run python scripts/render_feedback_report.py {ASSIGNMENT_DIR} <payload.json>
  ```

  The payload shape is documented in the script docstring.
- Validate it, and fix it until it passes:

  ```console
  uv run python scripts/check_feedback_report.py {ASSIGNMENT_DIR} "itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md"
  ```

  It runs the report validator and `markdownlint-cli2` together.
  Fallback: `uv run python scripts/validate_feedback_report.py {ASSIGNMENT_DIR} <agent-feedback.md>` and `markdownlint-cli2 <agent-feedback.md>`.
- Scan the finished report for private-only material:

  ```console
  uv run python scripts/scan_privacy.py {ASSIGNMENT_DIR} {TEAM_DIR} --feedback "itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/{TEAM_DIR}/agent-feedback.md"
  ```

- In `partial regrade` mode, prefer:

  ```console
  uv run python scripts/regrade_feedback_segments.py {ASSIGNMENT_DIR} <agent-feedback.md> <payload.json> S<n> ...
  ```

  The payload format is `{"segment_updates": {"S<n>": {"status", "evidence_gaps", "evidence", "verified_shortfalls", "unverified_checks"}}, "unresolved_evidence_gaps": {"S<n>": ["..."]}}`.
  Unresolved bullets for untouched gap segments are carried over automatically.
- In `segment inspect` mode, do not write any files.

## Return value

Return exactly one line for `full review` and `partial regrade`:

```text
{TEAM_DIR}: OK met <n> · partial <n> · missing <n> · unverified <n> — manual review <yes|no>
```

or

```text
{TEAM_DIR}: FAIL — <brief reason>
```

For `segment inspect`, return exactly one line:

```text
{TEAM_DIR}: INSPECT S<n>[,S<n>...] — <brief result>
```

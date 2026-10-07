<!-- markdownlint-disable-file MD041 -->

You are reviewing one ITPD assignment team submission.

`{ASSIGNMENT_DIR}` is the assignment directory, for example `A1` or `A2`.
`{TEAM_DIR}` is the team's submission directory name, for example `Team 3_12345_assignsubmission_file`.
Run every command from the repository root.

## Modes

Follow the operator request to choose one of these modes:

1. `full review` (default)
   - Review the submission and write a complete `feedback.md`.
2. `partial regrade`
   - Used when the operator names segment IDs such as `S3,S4`.
   - Read the existing `feedback.md` first.
   - Refresh only the requested segments plus any segment whose status depends on the same newly checked artifact.
   - Apply instructor notes directly when the operator provides them.
   - Patch with `uv run python scripts/regrade_feedback_segments.py` using a structured `segment_updates` payload.
     Use `uv run python scripts/patch_feedback_report.py` as the low-level fallback.
3. `segment inspect`
   - Used when the operator asks what the grader currently sees for specific segments.
   - Read the existing `feedback.md` first and do not edit any files.
   - Separate the saved report state from any fresh checks.

## Paths

- Submission: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}/` (the Moodle PDF report)
- Snapshot working copy, fetched from GitHub at the permalink SHA: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}/`
  It is disposable: every review rebuilds it, and it can be deleted after grading.
- Scratch directory: `tmp/{ASSIGNMENT_DIR}/{TEAM_DIR}/` (gitignored).
  Write every intermediate file here: API dumps, commit lists, fetched pages, images, payloads.
  Other graders run in parallel, so never write to a shared scratchpad, to `/tmp` directly, or into another team's directory, and never read another team's files.
- Report: `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/markdown/{TEAM_DIR}/feedback.md`

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
   For a structured view, run `uv run python scripts/inspect_feedback_segments.py {ASSIGNMENT_DIR} <feedback.md> S<n> ...`.
   Add `--fresh-payload <payload.json> --format text` to compare saved and fresh state.
7. Read the PDF:

   ```console
   pdftotext -layout itpd-assignments-feedback/{ASSIGNMENT_DIR}/submissions/{TEAM_DIR}/*.pdf -
   ```

   If `pdftotext` fails, read the PDF with the file-reading tool.
   Extract:
   - the team number;
   - the repository URL;
   - the permalink to the primary index and its full SHA;
   - the recording link;
   - the privacy confirmation;
   - anything else the assignment prompt asks for.
   Do not copy real names or emails into any output.
8. Resolve the authoritative snapshot with `docs/grader-policy.md#submission-and-snapshot-rules`.
   - Confirm that the commit exists with `gh api repos/<org>/<repo>/commits/<sha> --jq .sha`.
   - If no full SHA can be found, or the commit does not exist, stop repository-dependent checks.
9. Fetch the snapshot at the permalink SHA into an empty directory, so no files from an earlier fetch remain:

   ```console
   rm -rf "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   mkdir -p "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   gh api "repos/<org>/<repo>/tarball/<sha>" | tar -xz --strip-components=1 -C "itpd-assignments-feedback/{ASSIGNMENT_DIR}/work/{TEAM_DIR}"
   ```

10. Review the files offline in the fetched snapshot.
    Use `rg` and the file-reading tools.
    Build evidence links as `https://github.com/<org>/<repo>/blob/<sha>/<path>`.
11. Collect the live GitHub evidence the assignment prompt asks for with `gh` (pull requests, reviews, issues, labels, Actions runs, branch protection).
    Follow `docs/grader-policy.md#live-github-evidence`.
12. For recordings and other consumer-hosted media, make one access check only.
13. Judge each segment independently with the status guide in `{ASSIGNMENT_DIR}/grading_prompt.md`.
14. Set `Evidence gaps` per segment, then derive `Manual review required` and the overall assessment counts.

## Output

- In `full review` mode, write `itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/markdown/{TEAM_DIR}/feedback.md` in the format from `docs/grading-feedback-format.md`.
- Validate it, and fix it until it passes:

  ```console
  uv run python scripts/validate_feedback_report.py {ASSIGNMENT_DIR} "itpd-assignments-feedback/{ASSIGNMENT_DIR}/feedback/markdown/{TEAM_DIR}/feedback.md"
  ```

- In `partial regrade` mode, prefer:

  ```console
  uv run python scripts/regrade_feedback_segments.py {ASSIGNMENT_DIR} <feedback.md> <payload.json> S<n> ...
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

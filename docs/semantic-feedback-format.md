# Semantic Feedback Format

This document defines the optional companion file that judges whether a team's artifacts do their job.
It is not a second status record and not a second rubric.

The compliance report stays `agent-compliance-feedback.md`, defined in `docs/compliance-feedback-format.md`.
It records what is met, what is partial, the evidence, and the shortfalls.
The semantic feedback answers a different question: would a reader who was not in the room be able to use this artifact, and what breaks first if the team leans on it next week.

The semantic feedback never changes a status, an `Evidence gaps` flag, `Manual review required`, the overall assessment, or the grade.

## File

`itpd-assignments-feedback/<assignment>/feedback/<team_dir>/agent-semantic-feedback.md`

The file sits beside the compliance report in the same team directory.
It is optional: a report without it stays valid.
It is written by the semantic agent, not the compliance agent, after the compliance report is validated.
The semantic agent starts from the report as a map, then verifies each claim its judgement depends on against the snapshot at the saved SHA or the saved live evidence.
The report is never evidence for this file.
It never collects a new evidence dump or re-fetches the snapshot.
The release export ignores it; only `## Summary` goes into `feedback_release.csv`, and the full report directory is the channel that carries this file.
A change to that export rule is a change to this document and to the extractor together.

## Voice

Write for the team, not about it.
Name the artifact and what it does, then say what breaks first and for whom.
Do not grade the team's taste: the standard is the assignment's own quality guidance, not the reviewer's preference.
No praise that is not tied to an artifact, and no criticism that is not tied to one.

## Structure

Every file has these parts, in this order:

1. `# Assignment <N> Semantic Feedback`
2. Four metadata bullets: `- Team:`, `- Repository:`, `- Snapshot:`, `- Compliance report:`
3. `## How to read this`
4. One `##` section per dimension, in the assignment's order
5. `## Where to start`

The A5 dimensions are `Setup`, `Tests`, `Plan`, `Customer loop`, and `Publication`, defined in `A5/grading_prompt.md`.
Other assignments define their own dimensions in their own prompt; the schema is shared, the dimension list is not.

### Metadata

```markdown
- Team: 5
- Repository: `https://github.com/<org>/<repo>`
- Snapshot: `<full 40-character lowercase commit SHA>`
- Compliance report: [`agent-compliance-feedback.md`](./agent-compliance-feedback.md)
```

The repository and snapshot must match the compliance report's metadata.
The compliance report link is relative, because the two files share a directory.

### How to read this

One short paragraph: what this file judges, that the compliance report holds the statuses and the evidence, and that nothing here changes them.
Do not repeat the counts or the shortfall list.
If a dimension is omitted, say why here.

### Dimension section

```markdown
## Setup

**Verdict:** thin

**What works.** One or two sentences on what the artifact already does for its reader.

**What breaks first.** One or two sentences on the load-bearing part that is missing or unproven, and who hits it.

**What would make it adequate.** One sentence on the smallest change that changes the verdict.

**Evidence:**

- A link to the artifact the claim rests on, with one sentence on what it shows.
```

The last block is `**What would make it stronger.**` when the verdict is `adequate`.

### Where to start

Two or three bullets, one sentence each, starting with a verb.
Each names the artifact it changes.
Do not repeat the compliance report's `## Main issues to fix` list; this is the one or two moves that change the judgement.

## Verdict scale

| Verdict | Meaning |
|---------|---------|
| `adequate` | The artifact does its job; the remaining weakness is local and already visible. |
| `thin` | It would function, but one load-bearing part is missing or unproven, and the next week's work will expose it. |
| `not yet adequate` | It exists but cannot do its job yet; the gap is structural, not cosmetic. |

A segment can be `met` and its dimension `thin`: compliance is not adequacy.
A `partial` or `missing` segment does not make its whole dimension `not yet adequate` by itself; judge the artifact, not the count.

## Rules

- Ground every claim in an artifact you verified at the saved SHA, a live URL, or the saved handoff evidence in `work/<team_dir>/`.
  The compliance report is a map, not evidence.
- Verify the claims your judgement depends on, not every claim in the report; do not re-audit the segments.
- Prefer `work/<team_dir>/evidence.sqlite` and the saved dumps.
  At most three live `gh` lookups for one file, and record each one.
- A claim whose only source is the report is unverifiable and cannot carry a verdict.
- Do not edit `agent-compliance-feedback.md`.
  A claim that contradicts a status is a conflict, not an edit; the status wins until the operator regrades the report.
- No status vocabulary: do not use `met`, `partial`, `missing`, or `unverified`.
- No grade, score, rank, or cross-team comparison.
- No `None`, no `TBD`, no placeholder bullet.
- No "mentor" wording: the reviewer's voice is in the prose, not in a label.
- One sentence per line and no hard wrapping.
- Every evidence bullet holds at least one link.
  A repository file link cites the reviewed snapshot, `https://github.com/<org>/<repo>/blob/<snapshot-sha>/<path>`, not `main`.
  A live link (a run, a release, an issue, a pull request) cites the exact URL.
- Omit a dimension only when all of its segments are unverified (a status in the report; the file must not use that word); keep at least three dimensions.
  If fewer than three dimensions remain, do not write the file.
- Stop when the file stops being grounded: a shorter, honest file beats a longer, speculative one.

## Verification

The semantic agent keeps `itpd-assignments-feedback/<assignment>/work/<team_dir>/semantic-claims.json` as its audit trail.
The ledger is disposable, like the rest of the work directory; it is not a committed artifact.
Each load-bearing claim records `id`, `dimension`, `statement`, `locator`, `link`, `check`, `result`, and a short `quote`.

`result` is one of:

- `supported`: the locator was opened and shows what the claim says.
- `contradicted`: the locator shows the opposite.
  The claim goes into `conflicts` with the segment and the report's status, and never into the semantic file.
- `unverifiable`: the claim could not be checked within the budget.
  It may be a caveat, never the basis of a verdict.

Only `supported` claims feed the prose and the `**Evidence:**` bullets.
The ledger also records `report_sha256`; while the ledger is still present, `scripts/check_semantic_feedback.py --ledger` compares it with the report and refuses a companion whose report changed after the pass.
The operator then reruns the semantic agent in `semantic regrade` mode.

## Validation

```console
uv run python scripts/check_semantic_feedback.py A5 "itpd-assignments-feedback/A5/feedback/<team_dir>/agent-semantic-feedback.md" --ledger "itpd-assignments-feedback/A5/work/<team_dir>/semantic-claims.json"
```

The checker enforces the metadata, the dimension order, the verdict and block schema, the evidence links, the snapshot SHA in blob links, and the forbidden vocabulary, and it runs `markdownlint-cli2`.
It does not judge the prose.
With `--ledger`, it compares the ledger's recorded report hash with the sibling report; without the flag, or after the work directory is cleaned, the ledger is only the semantic agent's audit trail.

## Example

The A5 Team 5 file, `itpd-assignments-feedback/A5/feedback/Team 5 - TmpTeam_10941_assignsubmission_file/agent-semantic-feedback.md`, is the reference example for voice and schema: five dimensions, four `thin` and one `adequate`.
It is committed with the eight-team semantic pass, so it may be absent on an earlier checkout; use the structure above in that case.
It predates the verification contract, so use it for depth and tone, not as a claim-ledger example.

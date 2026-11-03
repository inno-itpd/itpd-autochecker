# Agent roles

One team review is split into two agents so that compliance work and semantic judgement do not compete for the same context window.

```text
compliance-agent  ->  validated agent-feedback.md + work/<team_dir>/
        |
        v
semantic-agent    ->  agent-semantic-feedback.md + work/<team_dir>/semantic-claims.json
```

The operator launches them in that order.
There is no LLM orchestrator: the operator or a script starts each role, and the files on disk are the handoff.

## Roles

| Agent | Question | Writes | Must not |
| --- | --- | --- | --- |
| [`compliance-agent.md`](compliance-agent.md) | What is the status of each segment? | `agent-feedback.md`, `payload.json`, evidence, `summary.md`, `inventory.md` | Write semantic feedback or change the semantic file |
| [`semantic-agent.md`](semantic-agent.md) | Does the artifact do its job, and does the evidence support that claim? | `agent-semantic-feedback.md`, `semantic-claims.json` | Change a status, edit the report, or re-run the whole audit |

The two prompts share the same conventions: the operator supplies `{ASSIGNMENT_DIR}`, `{TEAM_DIR}`, and the absolute `{TEAM_WORK}`; commands run from the repository root; every path containing a team name is quoted.

## Handoff

The compliance agent leaves a complete work directory:

- `payload.json`: the structured statuses and evidence.
- `summary.md`: the compact GitHub digest.
- `inventory.md`: the snapshot file inventory.
- `evidence.sqlite`: the queryable GitHub evidence.
- `pdf-info.json`: repository, SHA, and PDF metadata.
- `snapshot/`: the repository at the recorded commit.

The semantic agent must not re-fetch the snapshot or collect new dumps. It reads the handoff, chooses a few artifacts, and verifies only the claims its verdicts depend on. It records each one in `semantic-claims.json`.

## Sequence

1. Run the compliance agent for each team. Its report must pass `scripts/check_feedback_report.py` and the privacy scan before semantic work starts.
2. Run the semantic agent for that team. It writes `agent-semantic-feedback.md` next to `agent-feedback.md` and validates it with `scripts/check_semantic_feedback.py`.
3. Run semantic passes only for assignments that define `semantic_dimensions`, currently A5.
   - `semantic review` creates the file.
   - `semantic regrade` re-verifies an existing file after a report or artifact change.
   - `semantic inspect` reports without writing.

A semantic review does not block the release export. `agent-feedback.md` is still the only report that feeds `dev.md` and `feedback_release.csv`.

## One writer per team

The report and the semantic file live in the same feedback directory.

- Do not start semantic work while a compliance writer is active for the team.
- Do not run two semantic agents on the same team.
- A changed report makes the saved semantic file stale: rerun the semantic agent after the report is final.
- If the semantic agent finds a contradiction with a status, it records a conflict and leaves the report alone; the operator schedules a regrade.

See [`AGENTS.md`](../AGENTS.md) for batch sizes, resume budgets, and the pre-extraction gate.

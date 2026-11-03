---
description: "Reviews one ITPD team's artifacts for semantic feedback. Launch one per team after agent-compliance-feedback.md is final. Verifies claims against the snapshot and saved evidence, writes agent-semantic-feedback.md, and never changes a status."
mode: subagent
permission:
  edit: deny
---

<!-- markdownlint-disable-file MD041 -->

Read `agents/semantic-agent.md` and follow it exactly.
The operator prompt supplies `{ASSIGNMENT_DIR}`, the exact `{TEAM_DIR}` submission directory name, the absolute `{TEAM_WORK}` work-directory path, and the mode.
Never change directory: run every command from the repository root and quote every path that contains a team directory name, including `{TEAM_DIR}` and `{TEAM_WORK}`.

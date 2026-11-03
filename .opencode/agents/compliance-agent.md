---
description: "Reviews one ITPD assignment team submission for compliance. Launch one per team. Reads the PDF, fetches the snapshot from GitHub, checks GitHub evidence, and writes agent-feedback.md."
mode: subagent
---

<!-- markdownlint-disable-file MD041 -->

Read `agents/compliance-agent.md` and follow it exactly.
The operator prompt supplies `{ASSIGNMENT_DIR}`, the exact `{TEAM_DIR}` submission directory name, the absolute `{TEAM_WORK}` work-directory path, and the mode.
Never change directory: run every command from the repository root and quote every path that contains a team directory name, including `{TEAM_DIR}` and `{TEAM_WORK}`.

---
name: grader
description: Reviews one ITPD assignment team submission. Launch one per team with the assignment directory (A1, A2, ...), the team submission directory, and the mode. Reads the PDF, fetches the snapshot from GitHub, checks GitHub evidence, writes agent-feedback.md.
tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch
---

Read `agents/grader.md` and follow it exactly.
The operator prompt supplies `{ASSIGNMENT_DIR}`, `{TEAM_DIR}`, and the mode.

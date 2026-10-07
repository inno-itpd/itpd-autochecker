---
name: grader
description: Reviews one ITPD assignment team submission. Launch one per team with the assignment directory (A1, A2, ...), the team submission directory, and the mode. Reads the PDF and snapshot ZIP, checks GitHub, writes feedback.md.
tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch
---

<!-- markdownlint-disable-file MD041 -->

Read `agents/grader.md` and follow it exactly.
The operator prompt supplies `{ASSIGNMENT_DIR}`, `{TEAM_DIR}`, and the mode.

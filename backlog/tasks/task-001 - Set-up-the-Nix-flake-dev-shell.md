---
id: TASK-001
title: Set up the Nix flake dev shell
status: In Progress
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 10:17'
labels: []
dependencies: []
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Provide a pinned dev shell mirroring itpd/flake.nix (flake-parts, same nixpkgs and backlog-md pins) with the grading toolchain.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 flake.nix provides python3.13, uv, gh, pdftotext, unzip, jq, ripgrep, markdownlint-cli2, lychee, backlog
- [x] #2 .envrc loads the flake and .env via direnv
- [ ] #3 nix develop starts and all tools report a version
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
flake.nix mirrors itpd pins; flake.lock copied from itpd. nix develop verification still pending.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 All acceptance criteria are satisfied
- [ ] #2 `uv run pytest` passes
- [ ] #3 `markdownlint-cli2` passes on the changed Markdown
- [ ] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

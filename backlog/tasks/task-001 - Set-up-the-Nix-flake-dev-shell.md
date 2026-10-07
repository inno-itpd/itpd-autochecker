---
id: TASK-001
title: Set up the Nix flake dev shell
status: Done
assignee: []
created_date: '2026-10-07 10:15'
updated_date: '2026-10-07 21:10'
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
- [x] #3 nix develop starts and all tools report a version
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
flake.nix mirrors itpd pins; flake.lock copied from itpd. nix develop verification still pending.

2026-10-08: nix develop -c starts; versions: Python 3.13.15, uv 0.12.17, gh 2.100.0, pdftotext 26.06.0, UnZip 6.00, jq 1.8.2, ripgrep 15.2.0, markdownlint-cli2 0.23.2, lychee 0.24.2, backlog 1.52.0. uv run pytest: 30 passed.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

---
id: TASK-024
title: Add the commit-itpd skill and the /commit command
status: Done
assignee: []
created_date: '2026-10-11 14:41'
updated_date: '2026-10-11 14:49'
labels: []
dependencies: []
ordinal: 24000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Port the commit-itpd skill from the course repository (A2/itpd/.agents/skills/commit-itpd/SKILL.md) to .agents/skills/commit-itpd/SKILL.md and add the opencode /commit command at .opencode/command/commit.md. Adapt the course rules to this repository: path scopes from AGENTS.md, the 2-4 bullet body, and the Co-Authored-By trailer; drop the course-only Harness:/Model: lines and the current-model helper. Update AGENTS.md and .gitignore.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 .agents/skills/commit-itpd/SKILL.md carries valid Agent Skills frontmatter and the repository rules: path scopes, 2-4 bullet body, Co-Authored-By trailer, staged-changes-only, and no literal backslash-n
- [x] #2 .opencode/command/commit.md loads the commit-itpd skill and treats $ARGUMENTS as optional guidance
- [x] #3 .gitignore tracks .opencode/command/, and AGENTS.md lists the skill and command in the repo map and the Git conventions section
- [x] #4 markdownlint-cli2 passes on the changed Markdown files
- [x] #5 The harness directories take their MD041 exemption from the .markdownlint-cli2.jsonc overrides block, not per-file disable comments
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Ported the course commit-itpd skill to .agents/skills/commit-itpd/SKILL.md and added the /commit command at .opencode/command/commit.md. Decisions: adapted to this repo, so the trailer is the required Co-Authored-By line rather than the course Harness:/Model: lines, the scope list follows the AGENTS.md repo map, and the scripts/opencode/current-model.sh helper was not ported because this repo does not ship it (the skill falls back to asking the user). The command, .opencode/agents/grader.md, and .claude/agents/grader.md no longer carry inline markdownlint-disable-file MD041 comments; .markdownlint-cli2.jsonc now disables MD041 through an overrides block filtered to .opencode/, .claude/, and .agents/, and ignores the vendored .opencode/node_modules/ tree. The overrides option needs markdownlint-cli2 0.23.0 or newer: the flake lock provides 0.23.2, while a global ~/.nix-profile 0.21.0 binary shadows it outside the dev shell, so the checks must run under nix develop or direnv. Validation with the pinned 0.23.2: a probe without a heading fails MD041 at the repo root but passes under .opencode/, all four harness files lint clean, uv run pytest is 57 passed, git check-ignore confirms .opencode/command/commit.md is tracked, and the full markdownlint-cli2 **/*.md run reports only the pre-existing untracked TODO.md issues. opencode loads project skills from .agents/skills on restart; Claude Code does not scan that path.
<!-- SECTION:NOTES:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 All acceptance criteria are satisfied
- [x] #2 `uv run pytest` passes
- [x] #3 `markdownlint-cli2` passes on the changed Markdown
- [x] #4 Implementation notes record the decisions made and the validation results
<!-- DOD:END -->

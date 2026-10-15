---
name: commit-itpd
description: Create a git commit with this repository's conventions: use when the user explicitly asks to commit changes.
---

# Commit

- Write Conventional Commits with a path scope, matching the Git conventions in `AGENTS.md`.
- Use a scope that names the area changed, following the repository map in `AGENTS.md`: `A<N>/prompt` for an assignment's rubric and segments, `agents` for the canonical prompts and their harness wrappers, `tools` for `tools/grader_tools/`, `scripts` for the CLI scripts, `docs` for the policy and feedback-format docs, `tests`, `backlog`, `feedback` for a feedback submodule bump, `deps`, and `nix`.
  Scopes name the area, not the directory, so they survive a file moving.
- Use this required format:

  ```text
  <type>(<scope>): <imperative summary>

  - <what changed and why>
  - <what changed and why>

  Harness: <active harness>
  Model: <current LLM model>
  ```

- The body is 2-4 short bullets, one change and its reason each.
  The `Harness:` and `Model:` metadata lines are required on commits an AI agent makes, per `AGENTS.md`.
- Fill in `Model:` with the exact `<provider>/<model>` identifier, such as `openrouter/deepseek/deepseek-v4.1-flash`; do not use a bare model name.
- Determine the value from your own harness identity context:
  under opencode your system prompt states "You are powered by the model named ... The exact model ID is `<provider>/<model>`"; quote that exact string.
- Never derive `Model:` from `opencode.json`, `opencode debug config`, or environment variables;
  the resolved config often has no `model` set because selection is per-session, and nothing environment-visible exposes the live choice.
- When the identity context is absent or you are uncertain, stop and ask the user for the model name instead of guessing.
- Commit only changes that are already staged.
  If no changes are staged, stop and ask the user to stage the intended files before continuing.
- **Never include literal `\n` character sequences anywhere in a commit message.** Use actual newline characters for every line break.
- Do not mention unrelated changes.
- Do not include `Co-authored-by` trailers.

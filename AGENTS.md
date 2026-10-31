# AI Automation — Contributor Guidelines

Codex is the main harness. Claude Code, Cursor, and Gemini CLI read the same `skills/`, `knowledge/`, and `agents/` through their adapters.

## Structure

See `docs/architecture.md`.

## Rules

- `.codex-plugin/plugin.json` is the only hand-edited manifest. Run `scripts/render-manifests.py` after changing it and commit the generated files.
- Skills are discovered only at `skills/<name>/SKILL.md`. Do not nest them.
- `description` says only WHEN to use a skill or agent, starting with "Use when …". Never summarize the workflow.
- A skill's own rules, templates, and examples live in `skills/<name>/references/`. Anything two or more skills share lives in `knowledge/`. Point to a file, never copy it.
- Request → skill routing lives only in `skills/using-ai-automation/SKILL.md`. Request → repository mapping lives only in `knowledge/routing.md`.
- Agents live only in `agents/<name>.md`. Do not copy them into `adapters/`.
- Skills name actions, not tools: "dispatch a subagent", "read a file".
- User-specific values (local paths) live in `~/.config/ai-automation/config.json`, never in this repository.

## Before a PR

1. `python3 scripts/validate.py`
2. Run a changed skill in at least one real Codex session and paste the transcript in the PR.
3. Fill in `.github/pull_request_template.md`.

## Release

See `docs/releasing.md`.

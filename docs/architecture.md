# Architecture

```
.codex-plugin/plugin.json   source manifest (hand-edited)
.agents/plugins/            Codex marketplace (generated)
.claude-plugin/             Claude Code manifest + marketplace (generated)
.cursor-plugin/             Cursor manifest (generated)
gemini-extension.json       Gemini CLI manifest (generated)
GEMINI.md                   Gemini context: bootstrap skill + Gemini adapter notes

skills/using-ai-automation/ bootstrap: setup check, where things live, request → skill routing
skills/<workflow>/          SKILL.md + references/ (RULE.md, TEMPLATE.md, examples.md), optional scripts/ assets/
knowledge/                  shared across skills; INDEX.md says what to read when
agents/<name>.md            subagent prompts, single source for every harness
adapters/<harness>/         what differs per harness: hooks.json, tool mapping, notes
hooks/                      session-start + run-hook.cmd, called by adapters/{claude,cursor}/hooks.json
config/                     schema and example of the per-user config
scripts/                    render-manifests.py, bump-version.sh, validate.py
```

## How each harness reaches the content

| | Bootstrap | Skills | Agents |
|---|---|---|---|
| Codex | skill description | `.codex-plugin` `skills` | skill reads `agents/<name>.md` and spawns a subagent |
| Claude Code | `hooks/session-start` | `skills/` | `agents/` native |
| Cursor | `hooks/session-start` | `.cursor-plugin` `skills` | skill reads `agents/<name>.md` |
| Gemini CLI | `GEMINI.md` @-include | via bootstrap | skill reads `agents/<name>.md` |

## What reads what

- `using-ai-automation` → `knowledge/INDEX.md`, `knowledge/routing.md`, `adapters/<harness>/README.md`
- a workflow skill → its own `references/`, then `knowledge/` files named in `INDEX.md`
- a workflow skill → `agents/<name>.md` when it dispatches a subagent

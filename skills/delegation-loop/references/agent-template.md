# Agent Template

Build an agent only when the gate says a step needs a fresh context. The agent is one prompt file; the job's knowledge still lives in a skill's `references/` or in `knowledge/`.

## The file

`agents/<name>.md`:

````markdown
---
name: <name>
description: Use when <the step in the calling skill that needs a fresh context>
model: inherit
---

You are <role in one line>.

## Input

You receive: <exactly what the calling skill passes: file paths, the item to process, the checks to run>.

## Read first

- `skills/<job>/references/<file>` <why>
- `knowledge/<file>` <why>

## Do

1. <step>
2. <step>

## Do not

- Change files outside <scope>.
- Pass anything you could not verify.

## Return

<The exact shape of the answer, in order. Example for a reviewer: one line per check, PASS or FAIL, evidence; then the list of checks that could not be run.>
````

## Wire it into the calling skill

Add a step to `skills/<job>/SKILL.md`:

```markdown
4. Dispatch a subagent with the body of `agents/<name>.md` as its prompt. Pass <inputs>. Use its return as <what>.
```

Codex and Gemini CLI do not load `agents/` natively: the skill reads the file and spawns a subagent with its body (see `adapters/codex/README.md`). Claude Code and Cursor load it natively. Never copy the agent into `adapters/`.

## Proof for an agent

The calling skill's `## Done when` covers the agent's output. Add one check that the return has the shape in `## Return`.

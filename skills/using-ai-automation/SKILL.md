---
name: using-ai-automation
description: Use when starting any conversation - establishes how to find and use ai-automation skills, knowledge, and agents before any response
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

## The Rule

Invoke a relevant ai-automation skill before any response or action, including clarifying questions.

## Setup Check

Read `~/.config/ai-automation/config.json`.
Missing or unreadable → follow `references/setup.md` before any other ai-automation skill.

## Where Things Live

Paths below are relative to the plugin root (two directories above this file).

| What | Where | How to use it |
|------|-------|---------------|
| Skills | `skills/<name>/SKILL.md` | Invoke by name |
| Shared knowledge | `knowledge/INDEX.md` | Read the index, then only the files it points to for this request |
| Request → repository | `knowledge/routing.md` | Read when a request names a repository or service |
| Agents | `agents/<name>.md` | Dispatch a subagent with the file body as its prompt |

## Routing

| Request | Skill |
|---------|-------|
| TODO: 팀원이 실제로 쓰는 요청 문구 | TODO: skill name |

## Platform Adaptation

- Codex: `adapters/codex/README.md`
- Gemini CLI: `adapters/gemini/README.md`

Claude Code and Cursor need no mapping and load `agents/` natively.
Codex and Gemini CLI have no session-start hook and do not load `agents/`: read the agent file and dispatch a subagent with its body.

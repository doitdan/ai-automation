---
name: delegation-loop
description: Use when a repeated job should be handed to AI as a new skill or agent, when an existing skill or agent produced a wrong result that must be fixed at its source, or when someone says "스킬 만들어줘", "에이전트 만들어줘", "이거 AI한테 맡기고 싶어", "자동화해줘", "위임 루프", "결과가 또 틀렸어", "매번 같은 걸 고쳐"
---

# Delegation Loop

## Overview

One job gets one playbook: a skill folder the AI reads and follows. A playbook has three layers.

| Layer | What it holds | Where it lives in this repo |
|-------|---------------|-----------------------------|
| Process | Purpose, triggers, inputs, ordered steps, decision rules, definition of done, edge cases | `skills/<job>/SKILL.md` |
| Toolbox | Templates, rule files, reference data, approved examples, scripts | `skills/<job>/references/`, `skills/<job>/scripts/` |
| Proof | 5–10 checks that can fail, each with outside evidence | `## Done when` in `SKILL.md` |

When the result is wrong, fix the playbook, never only the output in chat. The next run must not need the same correction.

Talk to your human partner in their language. Write the files in English, like the rest of this repo, except words people type to trigger the skill.

## Where to Start

| Situation | Start at |
|-----------|----------|
| A new job to hand over | Phase 0 |
| An existing skill or agent gave a wrong result | Phase 4. No gate, no interview |
| An existing skill should cover more | Phase 0, then interview only the topics the skill does not answer yet |
| An existing skill has fewer than five checks | Phase 3 |

## The Loop

Each phase ends with something your partner can see.

0. **Gate.** Read `references/gate.md`. Confirm the job qualifies, search for an existing skill, agent, or knowledge file that already covers it, and choose skill, agent, or knowledge file. Report the choice in two lines; the first interview question may follow in the same message.
1. **Interview.** Read `references/interview.md`. One question per message, at least eight, no file until your partner says they are done. Then write `SKILL.md` from `references/skill-template.md` (or the agent from `references/agent-template.md`), show the whole file, and ask what you got wrong and what they did not tell you.
2. **First run, then toolbox.** Run the job once on real past input. When your partner approves a result, follow `references/toolbox.md`: save what was approved, rerun from scratch, report which saved files were used and what was rebuilt.
3. **Proof.** Follow `references/proof.md`: write the checks into `## Done when`, run every check, fix, rerun, report one line per check with its evidence.
4. **Fix loop.** Every wrong result, now or months later, goes through `references/fix-loop.md`: diagnose the layer in two sentences, make the smallest durable fix, add a line to `notes.md`, rerun from scratch, show before and after.
5. **Ship.** New skill: add the routing row in `skills/using-ai-automation/SKILL.md`. Every change: a line in `CHANGELOG.md` and `python3 scripts/validate.py`. Run the changed skill once in a real Codex session (AGENTS.md "Before a PR"); outside Codex, say that transcript is still owed. Commit only when your partner asks.

`references/examples.md` walks one job through every phase.

## Hard Rules

- During the interview, one question per message, and one thing per question: no "and".
- No file before your partner says the interview is over.
- Extra work you think the job needs is listed as a proposal when you show the file. Build it only after a yes.
- Sending, publishing, paying, or deleting outside the repo is a `Person:` step unless `knowledge/rules/approval.md` says otherwise.
- Client names, recipients, account data, and real results never go into this repo. Examples use made-up names and numbers.
- Rules set outside the team (law, platform policy, a client contract) come from the primary source, cited with its date in the rule file.
- A fix lands in a playbook file and in `notes.md`. A fix only in chat is not a fix.
- "Looks good" is not evidence. Every check names its evidence or says why it could not be checked.
- More than two checks fail on the first pass → stop patching the output and name the process step that caused it.
- The same mistake twice → an explicit rule that blocks it, not a reminder.
- After any fix, rerun the whole job from scratch.
- Cannot write a file → never pretend you did. Print the full content, the exact path, and tell your partner to replace the old copy.

## Red Flags

| You catch yourself | Do this instead |
|--------------------|-----------------|
| Sending a numbered list of questions | Send the first question only |
| "I have enough to draft it" before your partner says done | Ask the next uncovered interview topic |
| Correcting the output and moving on | Diagnose the layer, edit the playbook, log it |
| Writing "clear", "professional", "accurate" as a check | Rewrite it as something a file, count, link, or test can fail |
| Creating `report-v2.md` next to `report.md` | Replace the file; one file per purpose |
| Building a separate agent for a job a skill can do | Write the skill; an agent only for the reasons in `references/gate.md` |
| Copying a shared rule into a skill | Move it to `knowledge/` and point to it |
| Reusing a rule from `references/examples.md` | Take rules only from your partner or the primary source |

## Source

Adapted from the AI delegation loop playbook (https://sdk-kim-builds.com/guides/ai-delegation-loop-playbook/) and mapped onto this repository's layout.

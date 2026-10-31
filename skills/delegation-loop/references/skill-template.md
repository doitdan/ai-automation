# Skill Template

Copy this into `skills/<job>/SKILL.md` and fill every slot from the interview. A slot you cannot fill is a question you have not asked yet.

````markdown
---
name: <job>
description: Use when <the situation in plain words>, or when someone says "<phrase 1>", "<phrase 2>", "<phrase 3>"
---

# <Job title>

<Purpose in one line: what this produces, for whom.>

## When to Use

- "<words your partner types to start it>"
- "<another real phrasing>"
- Not for: <the neighbouring job this must not be confused with>

## Inputs

| Input | Location | Format |
|-------|----------|--------|
| <input> | <shared location, or the role it plays when it differs per person> | <CSV, Notion page, ...> |

## Steps

1. <Plain-language step. Name the file it uses: "Fill `references/TEMPLATE.md`".>
2. <Next step in the order your partner really works.>
3. Person: <decision that stays with a person>.

## Decisions

- If <X>, then <Y>.
- If <X>, then <Y>.

## Done when

Run every check before showing anything. Report one line per check: pass or fail, and its evidence. Say which checks could not be run and why.

- [ ] <check that a file, count, link, test, or quote can fail>
- [ ] <5 to 10 checks in total; see delegation-loop proof.md>

## Edge Cases

- <past case that broke the flow> → <what to do>

## Files

See `references/INDEX.md`.
````

## Rules for filling it

- `description` says only when to use the skill. No workflow summary. It starts with "Use when" (`scripts/validate.py` checks this).
- Trigger phrases are what people really type, in their language. A vague trigger such as "help with content" never loads.
- A shared location (a team drive folder, a Notion database) is written as is. A location that differs per person, such as a local download folder, is never written into the skill: name the input by its role ("this week's export the user names") and ask for it at run time.
- Steps are numbered and plain. No jargon your partner did not use.
- Sending, publishing, paying, or deleting outside the repo is a `Person:` step unless `knowledge/rules/approval.md` says otherwise.
- Every step that uses a toolbox file names it.
- Every decision is "If X, then Y". "Use judgment" is not a decision.
- `## Done when` starts empty or with your partner's own checks; phase 3 fills it (`proof.md`).
- Also create `skills/<job>/notes.md` containing only the heading `# Notes`, and `skills/<job>/references/INDEX.md` from `toolbox.md`.

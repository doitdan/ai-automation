# Gate

Answer these before the interview. Report the result to your partner in two lines: what you will build and why. The first interview question may follow in the same message.

## 1. Does the job qualify?

All four must be yes.

| Test | Yes means |
|------|-----------|
| Repeats | It happens at least once a week, or on a fixed trigger that comes back |
| Bad output is visible | Your partner can tell a bad result at a glance |
| Explainable | A new hire could learn it in about 20 minutes |
| Real input exists | You can get at least one real past input, or your partner can produce one |

A test the request does not answer → ask it as one of the first interview questions and call the gate report provisional.

Any no → say which one and suggest the most repeated piece of the job instead. Start with the most repeated job, not the most complex one.

A checker job (find what is wrong in someone's output) fails "bad output is visible" by nature: a miss is invisible. It qualifies only if you can build a set of known-bad and known-clean inputs for its proof (`proof.md`).

A decision that cannot be written as a rule stays with a person. Record it in the steps as `Person: <decision>` and keep it out of the delegated scope.

## 2. Does it already exist?

Search before you build:

- `skills/*/SKILL.md` descriptions and step lists
- `agents/*.md` descriptions and bodies
- `knowledge/INDEX.md`

| Found | Do |
|-------|----|
| A skill that does this job | Run the fix loop on that skill instead of creating a new one |
| A skill that does part of it | Extend that skill, or split the shared part into `knowledge/` |
| A generic agent whose body is still a stub | Fill it only if the job is the generic role its description names; otherwise build a job-specific agent and leave the stub alone |
| An agent that already does this role | Point the calling skill at it and put the job's rules in the skill's `references/` |
| A file with a similar name that does something else | Choose a name that cannot be confused with it |
| Nothing | Continue |

## 3. Skill, agent, or knowledge file?

Default to a skill. One general AI with one playbook per job beats a chain of specialist agents.

| Build | When |
|-------|------|
| Skill `skills/<job>/` | A person starts the job and the AI follows steps. This is almost always the answer |
| Agent `agents/<name>.md` | A step must run in a fresh context: an independent reviewer who did not write the output, the same work fanned out over many items in parallel, or a long search whose raw material would flood the main conversation |
| Knowledge file `knowledge/...` | It is a rule, list, or template that two or more skills need, not a procedure |

An agent never stands alone. A skill step dispatches it, so building an agent also means editing the calling skill's step (see `agent-template.md`). When the work it checks is produced outside this repo, build a thin calling skill whose trigger is the request to check ("이 글 검사해줘") and whose step dispatches the agent. When a skill in this repo produces that work, add the dispatch step to that skill instead.

Your partner asked for an "agent" and you build a skill plus an agent → say so in the gate report in one line: the skill is what they call, the agent is the fresh-context checker it runs.

## 4. Name

- Lowercase letters, digits, hyphens. The folder name and the `name:` field match.
- Name the job, not the tool: `weekly-client-update`, not `gmail-helper`.
- One job per folder. Two jobs that share steps get two folders and a shared `knowledge/` file.

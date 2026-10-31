# Interview

The interview pulls out the judgment your partner uses without noticing. Do not write the steps yourself; the detail that makes the playbook work is usually the one nobody wrote down.

## How to ask

- One question per message, and one thing per question. "뭐라고 입력하세요? 얼마나 자주 하세요?" is two questions. Wait for the answer before the next one.
- At least eight questions. Keep going until your partner says they are done.
- A topic the request already answered counts as covered. Spend that question on a deeper follow-up, never on repeating it.
- Do not write any file during the interview.
- Ask for real material early: a past output they were happy with, the input it came from, a bad version.
- Follow up on vague answers with "what exactly do you look at?" or "what would make you redo it?"
- Keep a private checklist of the eight topics below. Before you stop, every topic has an answer.

## The eight topics

| # | Topic | What you need to come away with | Example question |
|---|-------|--------------------------------|------------------|
| 1 | Trigger and frequency | The exact words they would type to start it, and how often | 이 일을 AI에게 시킬 때 실제로 뭐라고 입력하실 것 같으세요? (next message: 얼마나 자주 하세요?) |
| 2 | Inputs and locations | Every input with its exact location and format | 이 일에 쓰는 자료는 각각 어디에 있고 어떤 형식인가요? |
| 3 | Steps in real order | The order they actually work in, not the official SOP | 지난번에 이 일을 했을 때 맨 처음 뭘 열어 보셨어요? 그다음은요? |
| 4 | Decisions and rules | Every fork written as "if X, then Y" | 여기서 판단이 갈리는 순간이 있나요? 어떤 기준으로 정하세요? |
| 5 | Done check | What they check before calling it finished | 끝났다고 보기 전에 마지막으로 뭘 확인하세요? |
| 6 | Past exceptions | Cases that broke the usual flow and what they did | 평소 순서대로 안 됐던 적이 있나요? 그때 어떻게 하셨어요? |
| 7 | Tone and quality bar | Concrete markers of acceptable quality, ideally an approved example | 잘 됐다고 생각하는 결과물 하나를 보여 주실 수 있나요? |
| 8 | What bad looks like | The mistakes they would catch at a glance | 받자마자 다시 하라고 할 결과물은 어떤 모습이에요? |

Ask about the person boundary as part of topic 4: which decisions must stay with a person. Those become `Person:` lines in the steps.

When a rule is set outside the team (law, platform policy, a client contract), ask where your partner checks it. Read the primary source yourself and cite it with its date in the rule file. The source wins over habit; when they differ, tell your partner which line conflicts.

For a checker job, topic 7's approved example is a past output with the problems your partner found in it, and topic 8 is a problem they once missed.

## When your partner says they are done

1. Check the eight topics. A missing topic → ask it now, still one at a time.
2. Run the gate's third question again with what you learned: skill, agent, or knowledge file.
3. Write the file from `skill-template.md` or `agent-template.md`.
4. Show the whole file, not a summary.
5. In the same message, list any extra work you think the job needs as proposals, and ask these two numbered questions. This is the one message with two questions:
   1. 제가 잘못 쓴 부분은 어디인가요?
   2. 말씀 안 하신 것 중에 빠진 게 있나요?
6. Apply the answers, then move to the first run.

## If you cannot write files

Print the full file in the chat, give the exact path (`skills/<job>/SKILL.md`), and tell your partner to delete any older uploaded copy before adding the new one. Two copies bring retired instructions back.

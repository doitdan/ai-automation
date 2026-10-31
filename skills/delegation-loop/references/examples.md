# Worked Example: weekly client update

One job through every phase. Every name, number, and rule here is made up to show the shape. Never copy a rule from this file into a real skill; rules come only from your partner or a primary source.

## Phase 0 — Gate

Partner: "매주 월요일마다 고객사별 주간 광고 성과 메일 써. 이거 AI한테 맡기고 싶어."

- Repeats weekly, a wrong number is visible at a glance, explainable in 20 minutes → qualifies.
- No skill, agent, or knowledge file covers it.
- Skill, because a person starts it and the AI follows steps. Name: `weekly-client-update`.

Report: "주간 고객 메일은 위임 조건(매주 반복, 틀리면 바로 보임, 20분 안에 설명 가능)을 모두 충족합니다. 기존 스킬이 없어서 `weekly-client-update` 스킬로 새로 만들겠습니다."

## Phase 1 — Interview (one question per message)

1. 이 일을 AI에게 시킬 때 실제로 뭐라고 입력하실 것 같으세요?
2. 숫자는 어디서 가져오세요? 파일 형식은요?
3. 지난주에 이 메일 쓸 때 맨 처음 뭘 여셨어요?
4. 그다음엔 뭘 하셨어요? (repeated until the order is complete)
5. 메일 첫 문장은 어떻게 정하세요?
6. 보내기 전에 마지막으로 뭘 확인하세요?
7. 평소처럼 안 됐던 주가 있었나요?
8. 고객이 좋게 답장한 메일 하나 보여 주실 수 있나요?
9. 받자마자 다시 쓰라고 할 메일은 어떤 모습이에요?

The detail no SOP had came from question 5: open with the metric that moved most since last week. It became a decision rule.

Partner: "이 정도면 됐어." → write `SKILL.md`, show it whole, ask what is wrong and what is missing.

## Phase 2 — First run, toolbox

The first approved email produces three saved files and an example:

```
skills/weekly-client-update/
  SKILL.md
  notes.md
  references/
    INDEX.md
    client-update-template.md
    RULE.md
    examples/2026-09-08-approved.md
  scripts/
    numbers-pull.py
    test_numbers_pull.py
```

Second run report: "Used `numbers-pull.py`, `client-update-template.md`. Rebuilt from nothing: the week-over-week table → save next: `wow-table.py`."

## Phase 3 — Proof

```markdown
## Done when

- [ ] Every number appears in `numbers-pull.py` output for this week
- [ ] The first sentence names the metric with the largest week-over-week change
- [ ] Body is 200 words or fewer
- [ ] Client name matches the team's client sheet exactly
- [ ] Every promise in last week's sent email is mentioned
- [ ] No adjective from the banned list in `references/RULE.md`
```

## Phase 4 — Fix loop (week 4)

Partner: "CTR 3.2%라고 써 있는데 파일에 그런 숫자가 없어. 지난주에도 그랬어."

Diagnosis to partner: "숫자를 어디서만 가져오라는 규칙이 없어 프로세스가 실패했고, 그 숫자를 잡을 검사가 없어 증명도 실패했습니다. 같은 실수가 두 번이라 권고가 아니라 실패하는 검사로 막겠습니다."

Fix:

- Process: step 3 now says "Use only numbers in `numbers-pull.py` output. A metric that is not there is left out and named at hand-over."
- Proof: `scripts/check-numbers.py` added, and the first `## Done when` line now says to run it.
- `notes.md`: `- 2026-09-29 | process, proof | CTR 3.2% not in the export, second time | numbers only from numbers-pull.py; check-numbers.py added to Done when`
- Rerun with the same week's export: before shows `3.2%`, after leaves CTR out and the proof report shows `PASS numbers traced: check-numbers.py printed ok`.

## Phase 5 — Ship

- Routing row: `| "주간 광고 성과 메일", "월요일 고객사 리포트" | weekly-client-update |`
- `CHANGELOG.md` line, `python3 scripts/validate.py` → `ok`, one real Codex session transcript for the PR.

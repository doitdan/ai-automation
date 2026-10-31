---
name: using-ai-automation
description: 모든 대화를 시작할 때, 어떤 답이나 확인 질문보다 먼저 쓴다
---

<SUBAGENT-STOP>
특정 작업을 맡아 실행 중인 서브에이전트라면 이 스킬을 무시한다.
</SUBAGENT-STOP>

## 규칙

관련된 ai-automation 스킬이 있으면 어떤 답이나 행동보다 먼저 그 스킬을 실행한다.
확인 질문을 하기 전에도 마찬가지다.

## 설정 확인

`~/.config/ai-automation/config.json`을 읽는다.
파일이 없거나 읽을 수 없으면 다른 ai-automation 스킬보다 먼저 `references/setup.md`를 따른다.

## 어디에 무엇이 있나

아래 경로는 플러그인 루트(이 파일에서 두 단계 위) 기준이다.

| 무엇 | 위치 | 쓰는 법 |
|------|------|---------|
| 스킬 | `skills/<name>/SKILL.md` | 이름으로 실행한다 |
| 공유 지식 | `knowledge/INDEX.md` | 색인을 읽고, 이번 요청에 필요한 파일만 읽는다 |
| 요청 → 저장소 | `knowledge/routing.md` | 요청이 저장소나 서비스를 가리킬 때 읽는다 |
| 에이전트 | `agents/<name>.md` | 파일 본문을 프롬프트로 서브에이전트를 띄운다 |

## 요청 → 스킬

| 요청 | 스킬 |
|------|------|
| TODO: 팀원이 실제로 치는 요청 문구 | TODO: 스킬 이름 |
| "스킬 만들어줘", "에이전트 만들어줘", "이거 AI한테 맡기고 싶어", "자동화해줘", "위임 루프", "결과가 또 틀렸어", "매번 같은 걸 고쳐" | delegation-loop |

## 하네스별 차이

- Codex: `adapters/codex/README.md`
- Gemini CLI: `adapters/gemini/README.md`

Claude Code와 Cursor는 따로 맞출 것이 없고 `agents/`를 직접 읽는다.
Codex와 Gemini CLI는 세션 시작 훅이 없고 `agents/`를 읽지 않는다.
에이전트가 필요하면 `agents/<name>.md`를 읽고 그 본문으로 서브에이전트를 띄운다.

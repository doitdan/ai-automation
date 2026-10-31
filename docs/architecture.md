# 구조

```
.codex-plugin/plugin.json   원본 매니페스트 (직접 고침)
.agents/plugins/            Codex 마켓플레이스 (생성)
.claude-plugin/             Claude Code 매니페스트·마켓플레이스 (생성)
.cursor-plugin/             Cursor 매니페스트 (생성)
gemini-extension.json       Gemini CLI 매니페스트 (생성)
GEMINI.md                   Gemini 컨텍스트: 진입 스킬 + Gemini 어댑터

skills/using-ai-automation/ 진입 스킬: 설정 확인, 위치 안내, 요청 → 스킬
skills/<workflow>/          SKILL.md + references/(RULE.md, TEMPLATE.md, examples.md), 필요하면 scripts/ assets/
knowledge/                  여러 스킬이 함께 쓰는 지식. INDEX.md가 언제 무엇을 읽을지 정한다
agents/<name>.md            서브에이전트 프롬프트. 모든 하네스가 이 한 곳을 쓴다
adapters/<harness>/         하네스마다 다른 것: hooks.json, 도구 대응표, 메모
hooks/                      session-start, run-hook.cmd. adapters/{claude,cursor}/hooks.json이 부른다
config/                     사용자 설정 형식과 예시
scripts/                    render-manifests.py, bump-version.sh, validate.py
```

## 하네스가 내용에 닿는 길

| | 진입 스킬 | 스킬 | 에이전트 |
|---|---|---|---|
| Codex | description | `.codex-plugin`의 `skills` | 스킬이 `agents/<name>.md`를 읽어 서브에이전트를 띄운다 |
| Claude Code | `hooks/session-start` | `skills/` | `agents/`를 직접 읽는다 |
| Cursor | `hooks/session-start` | `.cursor-plugin`의 `skills` | 스킬이 `agents/<name>.md`를 읽는다 |
| Gemini CLI | `GEMINI.md`의 @ | 진입 스킬을 거쳐서 | 스킬이 `agents/<name>.md`를 읽는다 |

## 무엇이 무엇을 읽나

- `using-ai-automation` → `knowledge/INDEX.md`, `knowledge/routing.md`, `adapters/<harness>/README.md`
- 업무 스킬 → 자기 `references/`, 그다음 `INDEX.md`가 가리키는 `knowledge/` 파일
- 업무 스킬 → 서브에이전트가 필요하면 `agents/<name>.md`

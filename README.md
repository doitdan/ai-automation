# AI Automation

TODO: 플러그인 소개

Codex를 기준으로 Claude Code, Cursor, Gemini CLI에서 같은 스킬·지식·에이전트를 쓴다.

## 설치

Codex

```bash
codex plugin marketplace add https://github.com/doitdan/ai-automation.git
codex plugin add ai-automation@ai-automation
```

Claude Code

```
/plugin install ai-automation --marketplace doitdan/ai-automation
```

Gemini CLI

```bash
gemini extensions install https://github.com/doitdan/ai-automation
```

자세한 내용은 [docs/installation.md](docs/installation.md).

## 사용 예시

TODO

## 구성

- `skills/` 업무 절차
- `knowledge/` 여러 스킬이 함께 쓰는 지식
- `agents/` 서브에이전트 프롬프트

구조와 참조 관계는 [docs/architecture.md](docs/architecture.md), 기여 규칙은 [AGENTS.md](AGENTS.md).

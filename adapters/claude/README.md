# Claude Code

- 매니페스트: `.claude-plugin/plugin.json` (생성 파일)
- 마켓플레이스: `.claude-plugin/marketplace.json` (생성 파일)
- 훅: `adapters/claude/hooks.json`. 매니페스트의 `hooks` 필드로 연결한다.
- 세션 시작: `hooks/session-start`가 `skills/using-ai-automation/SKILL.md`를 넣는다.
- 에이전트: `agents/*.md`를 플러그인 에이전트로 직접 읽는다.

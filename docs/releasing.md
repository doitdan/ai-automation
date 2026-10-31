# 릴리스

언제 어느 자리를 올리는지는 `AGENTS.md`의 "버전 규칙"을 따른다.

1. `scripts/bump-version.sh <version>`을 돌린다. `.codex-plugin/plugin.json`의 버전을 바꾸고 나머지 매니페스트를 다시 만든다.
2. `CHANGELOG.md`에 `## <version> — <날짜>` 제목과 바뀐 것을 적는다.
3. `python3 scripts/validate.py`를 돌린다.
4. 커밋하고 푸시한다.
5. `git tag v<version>` 후 `git push origin v<version>`으로 태그를 푸시한다.
6. 사용자는 아래 명령으로 업데이트한다.
   - Codex: `codex plugin marketplace upgrade`
   - Claude Code: `/plugin marketplace update ai-automation` 후 `/plugin update ai-automation@ai-automation`
   - Gemini CLI: `gemini extensions update ai-automation`

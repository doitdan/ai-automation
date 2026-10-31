# 릴리스

1. `scripts/bump-version.sh <version>`을 돌린다. `.codex-plugin/plugin.json`의 버전을 바꾸고 나머지 매니페스트를 다시 만든다.
2. `CHANGELOG.md`에 항목을 추가한다.
3. `python3 scripts/validate.py`를 돌린다.
4. 커밋하고 `v<version>` 태그를 붙여 푸시한다.
5. 사용자는 `codex plugin marketplace upgrade`, `/plugin marketplace update ai-automation`, `gemini extensions update ai-automation`으로 업데이트한다.

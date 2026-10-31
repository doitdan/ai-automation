# Releasing

1. `scripts/bump-version.sh <version>` — updates `.codex-plugin/plugin.json` and regenerates every other manifest
2. Add an entry to `CHANGELOG.md`
3. `python3 scripts/validate.py`
4. Commit, tag `v<version>`, push
5. Users update: `codex plugin marketplace upgrade`, `/plugin marketplace update ai-automation`, `gemini extensions update ai-automation`

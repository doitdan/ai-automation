# Claude Code

- Manifest: `.claude-plugin/plugin.json` (generated)
- Marketplace: `.claude-plugin/marketplace.json` (generated)
- Hooks: `adapters/claude/hooks.json`, wired through the manifest `hooks` field
- Session start: `hooks/session-start` injects `skills/using-ai-automation/SKILL.md`
- Agents: `agents/*.md` load natively as plugin agents

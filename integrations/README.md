# Integrations

This folder contains provider/client-specific wiring.

- `assistant/settings.json`: original hook/permission config example for assistant clients.

For any other client (Codex CLI, OpenClaw, Cursor, local agents):
1. Keep `.studio/agents`, `.studio/skills`, `.studio/rules`, `.studio/hooks` as source of truth.
2. Register slash/prompt commands by mapping command name → `.studio/skills/<name>/SKILL.md`.
3. Reuse shell hooks in `.studio/hooks` where your client supports pre/post tool hooks.

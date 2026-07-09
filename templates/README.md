# templates

Templates consumed by the generators (`src/aiagentready/generators/`) to produce the
per-repo deliverable PR:

- `CLAUDE.md` skeleton (architecture overview, module map, conventions, test/lint commands, landmines)
- Agent settings / noise exclusions (`.claude/settings.json`)
- MCP configs (`.mcp/codebase-memory.json`, `.mcp/git-intelligence.json`)
- Freshness-hook CI workflows (GitHub Actions, GitLab CI)

**Status: placeholder.** Filled in during **Phase 2** (automate layers 1–3); CI templates
land in **Phase 4**.

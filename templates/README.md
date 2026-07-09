# templates

Templates consumed by the generators (`src/aiagentready/generators/`) to produce the
per-repo deliverable PR:

- `CLAUDE.md` skeleton (architecture overview, module map, conventions, test/lint commands, landmines)
- Agent settings / noise exclusions (`.claude/settings.json`)
- MCP configs (`.mcp/codebase-memory.json`, `.mcp/git-intelligence.json`)
- Freshness-hook CI workflows (GitHub Actions, GitLab CI)

**Status: partially filled.** `validation/` (the 10-question check: question types, rubric,
result format, edx-platform example) landed with the `validation-rubric` change. Generator
templates arrive in **Phase 2**; CI templates land in **Phase 4**.

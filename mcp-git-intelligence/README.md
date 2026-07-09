# mcp-git-intelligence

MCP server over mined git history, answering questions agents can't get from code alone:

- `why_exists` — why does this code exist?
- `change_history` — what changed here, when, and by whom?
- `change_coupling` — what files change together?
- `blast_radius` — what broke here before?

**Status: placeholder.** Built in **Phase 3** of the roadmap (see root README), gated on a
linkage-coverage spike: if commit–PR–issue linkage on the target repo is too sparse (<~60%
usable), this ships in degraded mode (coupling + blame aggregation only, no rationale).

This directory will become its own Python package with a separate `pyproject.toml`.

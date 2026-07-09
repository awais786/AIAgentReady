# Phase 0 Bootstrap — Repository Scaffold

## Why

AIAgentReady (design doc v4.1) has an agreed roadmap and a tracked phase ticket (ARBISOFTOPEN-438), but the GitHub repo (https://github.com/awais786/AIAgentReady) is still empty and the local directory has nothing committed. Every later phase — the manual edx-platform pilot, the analyzer/generators, the git-intelligence MCP server — needs a canonical repository structure, Python packaging, and a first push to build on.

## What Changes

- Create the canonical repository layout per design doc §7 and the agreed plan:
  - `src/aiagentready/` — single Python package with `analyzer/`, `generators/`, `grounding/`, `validation/` subpackages (stubs only in Phase 0)
  - `mcp-git-intelligence/` — separate package placeholder for the Layer-4 MCP server (Phase 3)
  - `templates/` — CLAUDE.md / CI / MCP-config templates consumed by generators
  - `pilots/edx-platform/` — home for Phase 1 manual pilot artifacts
  - `docs/adr/` — architecture decision records, seeded with ADR-0001 (language/stack choice)
- Add Python packaging and dev tooling: `pyproject.toml` (package metadata, pytest, ruff), a smoke test proving the package imports, `.gitignore`, `README.md`, `LICENSE`.
- Make the initial commit on `main` and push to the empty GitHub remote.

## Capabilities

### New Capabilities
- `repo-structure`: the canonical directory layout and placeholder packages that all later phases build into
- `python-packaging`: installable `aiagentready` package with working test and lint tooling

### Modified Capabilities

None — this is the first change; no existing specs.

## Impact

- Everything is additive; no existing code is touched (repo is empty).
- Establishes Python as the implementation stack (recorded as ADR-0001).
- First push makes the repo public-facing; the design doc itself stays out of the commit until the naming conflict (aiagentready.dev) is resolved.

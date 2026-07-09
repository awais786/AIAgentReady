# AIAgentReady

**AI-Aware Repo Onboarding Kit** — point it at a legacy repository and it emits a single
reviewable pull request containing everything an AI coding agent needs to work in that repo
effectively: configuration, indexes, generated documentation, git intelligence, and a
freshness hook.

> **Status: Phase 0 — bootstrap.** Repository scaffold only; no functional code yet.

## The five layers

| # | Layer | What it is | Build / adopt / generate |
|---|-------|------------|--------------------------|
| 1 | Agent configuration | `CLAUDE.md` / `AGENTS.md` at root; noise exclusions in agent settings | Generate |
| 2 | Structural index | codebase-memory MCP installed, indexed, config committed | Adopt |
| 3 | Documentation layer | Module map, entry-point flow guides, conventions inferred from actual code | Generate (grounded, human-reviewed) |
| 4 | Git intelligence | MCP server: *why does this exist, what changed together, what broke here before* | Build |
| 5 | Freshness hook | CI step: re-index on merge; flag drift between `CLAUDE.md` and reality | Build |

## Repository layout

```
src/aiagentready/       # the kit: analyzer, generators, grounding, validation
mcp-git-intelligence/   # layer-4 MCP server (separate package, Phase 3)
templates/              # CLAUDE.md / MCP-config / CI templates (Phase 2+)
pilots/edx-platform/    # Phase 1 manual pilot artifacts
docs/adr/               # architecture decision records
openspec/               # spec-driven change workflow (OpenSpec)
```

## Roadmap

| Phase | Deliverable | Duration |
|-------|-------------|----------|
| 0 | Repository bootstrap (this scaffold) | — |
| 1 | Manual pilot: edx-platform onboarded by hand, all five layers | 1–2 wks |
| 2 | Automate layers 1–3: analyzer + generators, grounded-generation guardrails | 3–4 wks |
| 3 | Git-intelligence MCP server | 3–4 wks |
| 4 | Freshness hook + packaging; kit runs end-to-end on a fresh repo | 2 wks |
| 5 | Second repo (different language/framework) to expose overfitting | 1 wk |

## Development

Requires Python ≥3.11.

```bash
pip install -e . --group dev
pytest
ruff check .
```

## Contributing

This repo is spec-first: every feature starts as an OpenSpec change, reviewed by a teammate
**before** implementation. See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow.

## License

[Apache-2.0](LICENSE)

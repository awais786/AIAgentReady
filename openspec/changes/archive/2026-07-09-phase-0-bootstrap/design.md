# Phase 0 Bootstrap — Design

## Context

The repo is empty: local dir is git-initialized on `main` with `origin` → https://github.com/awais786/AIAgentReady, nothing committed. Design doc v4.1 fixes the product shape (five layers, single-PR deliverable) and the roadmap; the agreed repo plan is a single Python package plus a separate MCP-server package. Phase 0 turns that plan into a committed, pushed skeleton that ARBISOFTOPEN-438 can be closed against.

## Goals / Non-Goals

**Goals:**
- A pushed `main` with the canonical layout every later phase builds into.
- `pip install -e .` works; `pytest` and `ruff check` pass on a fresh clone.
- The stack decision (Python) is recorded where it can be argued with (ADR-0001).

**Non-Goals:**
- No analyzer/generator/grounding/validation logic — subpackages are import-able stubs only.
- No `mcp-git-intelligence` implementation (Phase 3); placeholder README only, not a Python package yet.
- No CI workflow for this repo itself (added when there is code worth gating; Phase 4 covers the *kit's* CI templates, a separate thing).
- The design doc `.docx`/`.txt` files stay untracked until the naming conflict is resolved.

## Decisions

1. **Python ≥3.11, single package under `src/` layout** — `src/aiagentready/` avoids accidental imports from the repo root and matches modern packaging guidance. Alternative (flat layout) rejected: bites later when templates/pilots dirs sit next to the package.
2. **`pyproject.toml` with hatchling backend, no requirements.txt** — one file for metadata, deps, ruff and pytest config. Alternatives (setuptools + setup.cfg, poetry) rejected as either legacy or heavier than needed.
3. **`mcp-git-intelligence/` as a sibling directory, not a workspace member yet** — it will have its own `pyproject.toml` in Phase 3; premature packaging now would just be churn. 
4. **ADR-0001 records the Python choice** — the one open decision from planning gets written down as accepted, with the rationale (LLM/MCP ecosystem, edx-platform pilot is Python, team familiarity).
5. **Dev tooling: pytest + ruff only** — no mypy/pre-commit in Phase 0; add when there is real code. Smoke test = `import aiagentready` and its four subpackages, asserting `__version__`.

## Risks / Trade-offs

- [Public repo goes live with placeholder content] → README states the project status and links the roadmap phases; no design-doc content is pushed.
- [Layout may not survive contact with Phase 2 automation] → everything is stubs; renames are cheap before any real code lands. ADRs give a place to record such changes.
- [Name conflict (aiagentready.dev) unresolved] → package name only lives in `pyproject.toml`/directory name; a rename before public launch is a mechanical change, noted in ADR-0001.

## Migration Plan

Single additive commit on `main`, pushed to the empty remote. Rollback = force-push removal or repo reset; nothing depends on it yet.

## Open Questions

- None blocking. Product/package rename is deferred to pre-launch (tracked in proposal Impact and ADR-0001).

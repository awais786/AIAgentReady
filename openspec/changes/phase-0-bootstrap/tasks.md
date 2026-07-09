# Phase 0 Bootstrap — Tasks

## 1. Package skeleton

- [x] 1.1 Create `src/aiagentready/__init__.py` with `__version__ = "0.0.1"` and empty `__init__.py` in `analyzer/`, `generators/`, `grounding/`, `validation/` subpackages
- [x] 1.2 Create `pyproject.toml` — hatchling backend, src layout, Python ≥3.11, `[dependency-groups] dev = pytest + ruff`, ruff and pytest config sections
- [x] 1.3 Create `tests/test_smoke.py` — imports `aiagentready` and all four subpackages, asserts `__version__ == "0.0.1"`

## 2. Repo directories and docs

- [x] 2.1 Create `mcp-git-intelligence/README.md`, `templates/README.md`, `pilots/edx-platform/README.md` — each states purpose and the roadmap phase that fills it (Phase 3, Phase 2, Phase 1 respectively)
- [x] 2.2 Create `docs/adr/0001-python-stack.md` — Status: Accepted; rationale (MCP/LLM ecosystem, edx-platform pilot is Python, team familiarity); note deferred package rename (aiagentready.dev conflict)
- [x] 2.3 Create root `README.md` — one-sentence product description, project status (Phase 0), five-layer overview, roadmap table
- [x] 2.4 Create `LICENSE` (Apache-2.0) and `.gitignore` (Python defaults + `AIAgentReady-Design-Doc.*`)

## 3. Verify

- [x] 3.1 Fresh virtualenv: `pip install -e ".[dev]"` (or dev group) succeeds; `python -c "import aiagentready"` prints version
- [x] 3.2 `pytest` passes; `ruff check .` exits clean

## 4. Commit and push

- [ ] 4.1 Stage scaffold (confirm design-doc files NOT staged), commit on `main` with message referencing ARBISOFTOPEN-438
- [ ] 4.2 Push to `origin main`; verify GitHub repo shows the scaffold
- [ ] 4.3 Update ARBISOFTOPEN-438 in Plane: link the commit, mark verification criteria met

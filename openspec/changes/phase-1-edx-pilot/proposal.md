# Phase 1 — Manual Pilot: edx-platform Onboarded by Hand

## Why

Before automating anything, the kit must be executed by hand once, end to end, on a real legacy repo (design doc §5). The pilot produces the three things Phase 2 cannot start without: a reference example of ideal output, the real spec for what automation must produce, and the effort baseline that prices client engagements. edx-platform is the target (ARBISOFTOPEN-439); layers 1–2 exist partially from prior work and are completed first.

## What Changes

- Hand-craft all five layers for edx-platform, producing the full PR-shape deliverable file set (design doc §3) under `pilots/edx-platform/`:
  - Layer 1: `CLAUDE.md` + noise exclusions (`.claude/settings.json`)
  - Layer 2: structural index config (`.mcp/codebase-memory.json`), index built locally
  - Layer 3: `docs/ai/modules.md`, 5–10 flow walkthroughs (`docs/ai/flows/*.md`), `docs/ai/conventions.md` — every claim citing a real file/symbol
  - Layer 4: git-intelligence *notes* (manual mining: why-exists/coupling examples) — the MCP server itself is Phase 3
  - Layer 5: freshness-hook CI job draft (`.github/workflows/ai-aware.yml`)
- Keep a timing log: minutes spent and analysis required per artifact — this is the automation spec and pricing baseline.
- Run the before/after 10-question validation check and score it. **Depends on ARBISOFTOPEN-444** (question template + rubric); if 444 isn't done when we reach validation, its template work happens first as its own change.
- Write a pilot report summarizing findings, timings, and what automation must reproduce.

## Capabilities

### New Capabilities

Both capabilities are **generic** — they define what any manual pilot run must produce for any target repo (`pilots/<target-repo>/`). This change executes their first instance, edx-platform; the Phase 5 second repo and future client engagements reuse the same requirements unchanged.

- `pilot-deliverables`: the complete five-layer, PR-shape artifact set a pilot produces for its target repo
- `pilot-measurements`: the timing log, before/after validation results, and pilot report that automation specs and engagement pricing consume

### Modified Capabilities

None — `repo-structure`, `python-packaging`, and `contribution-workflow` are untouched.

## Impact

- All new files under `pilots/edx-platform/`; no kit code is written (that's Phase 2).
- Requires a local edx-platform checkout and codebase-memory-mcp installed; index data itself is NOT committed (design doc §3), only configs and reviewed docs.
- Human review is non-removable (design doc §4): generated/drafted docs are reviewed by the engineer who knows edx-platform before being called done.
- Output artifacts become Phase 2's acceptance fixtures — changing their shape later invalidates Phase 2 tests, so shape is decided here.

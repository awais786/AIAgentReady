# Phase 1 — Manual Pilot: Tasks

## 1. Setup and baseline

- [ ] 1.1 Clone edx-platform locally; record repo size, language mix, and checkout SHA in `pilots/edx-platform/pilot/timing-log.md` (start the log now)
- [ ] 1.2 Install codebase-memory-mcp against the checkout; build the structural index; log time + any failures
- [ ] 1.3 Run the "before" 10-question check (template from ARBISOFTOPEN-444 — if not ready, do that change first) with an agent that has no pilot artifacts; save answers to `pilots/edx-platform/pilot/validation.md`

## 2. Layer 1 — Agent configuration

- [ ] 2.1 Complete `pilots/edx-platform/CLAUDE.md` from prior partial work: architecture overview, module map, conventions, test/lint commands, known landmines
- [ ] 2.2 Write `.claude/settings.json` noise exclusions (migrations, .po, vendored, generated); verify each excluded path exists in edx-platform

## 3. Layer 2 — Structural index config

- [ ] 3.1 Write `.mcp/codebase-memory.json` so a fresh developer's agent gets graph queries; document the one-command setup in the timing log

## 4. Layer 3 — Generated documentation

- [ ] 4.1 Write `docs/ai/modules.md` — one section per top-level module: purpose, key classes, entry points, owning tests
- [ ] 4.2 Write 5–10 flow walkthroughs in `docs/ai/flows/` (start: enrollment, grading, authentication), each tracing the actual call path from the index
- [ ] 4.3 Write `docs/ai/conventions.md` from patterns as they are in the code (serializers, service layer, test layout)
- [ ] 4.4 Ground-check: sample citations across all Layer-3 docs; fix or remove any claim that doesn't resolve to a real file/symbol

## 5. Layer 4 — Git-intelligence notes

- [ ] 5.1 Pick ~5 modules; manually mine history for why-exists / change-coupling / blast-radius answers with commit/PR/issue citations; write up as notes
- [ ] 5.2 Record observed commit–PR–issue linkage quality as an early signal for the Phase 3 spike (note in pilot report)
- [ ] 5.3 Add `.mcp/git-intelligence.json` stub noting the Phase 3 server it will configure

## 6. Layer 5 — Freshness hook

- [ ] 6.1 Draft `.github/workflows/ai-aware.yml`: re-index on merge, regenerate module map on file moves, open issue on CLAUDE.md drift

## 7. Review, validate, report

- [ ] 7.1 Human review of the full artifact set by the teammate who knows edx-platform; corrections + landmines added by hand; reviewer named in report
- [ ] 7.2 Run the "after" 10-question check; human-score both runs; complete `pilot/validation.md`
- [ ] 7.3 Write `pilot/report.md`: total + per-layer effort, findings, tooling failures, before/after result, explicit Phase-2-must-produce list
- [ ] 7.4 PR per CONTRIBUTING.md, merge, update ARBISOFTOPEN-439, archive this change

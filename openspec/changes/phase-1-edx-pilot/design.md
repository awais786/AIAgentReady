# Phase 1 — Manual Pilot: Design

## Context

This change produces artifacts, not code: a by-hand execution of the kit on edx-platform. The quality bar is "what we'd deliver to a paying client"; the process bar is "measured well enough to spec the automation." Layers 1–2 partially exist from prior work on edx-platform and are completed, not restarted.

## Goals / Non-Goals

**Goals:**
- Complete PR-shape file set (design doc §3) in `pilots/edx-platform/`, human-reviewed.
- Timing + analysis log accurate enough to (a) spec Phase 2 generators and (b) price engagements.
- Scored before/after 10-question table.

**Non-Goals:**
- No automation code — resist the urge to script anything beyond throwaway helpers; scripted steps get timed as manual-equivalent or noted.
- No git-intelligence MCP server (Phase 3) — Layer 4 here is manually mined *notes* proving what the server should answer.
- No PR against the real edx-platform repo — the deliverable lands in `pilots/edx-platform/` as a reference, not upstream.

## Decisions

0. **Specs are generic; this change is their first instance** — the `pilot-deliverables` and `pilot-measurements` capabilities are written repo-agnostically (`pilots/<target-repo>/`), so Phase 5's second repo and future engagements run against the same spec. Everything edx-specific (flow choices, module choices, prior partial work) lives in this change's tasks, not the specs. Rationale: capabilities outlive changes; an edx-shaped spec would need rewriting in Phase 5.
1. **`pilots/edx-platform/` mirrors the target-repo layout** — files sit at the paths they'd occupy in edx-platform (`CLAUDE.md`, `.claude/settings.json`, `.mcp/*.json`, `docs/ai/*`, `.github/workflows/ai-aware.yml`), plus a `pilot/` subdirectory for meta-artifacts (timing log, validation table, report). Rationale: the file set doubles as the Phase 2 acceptance fixture — the closer to real, the better the fixture. Alternative (freeform notes directory) rejected: wouldn't validate the §3 deliverable shape.
2. **Timing log is per-artifact, structured** (`pilot/timing-log.md`: artifact, minutes, analysis performed, inputs needed, could-automate notes) — captured *as work happens*, not reconstructed at the end.
3. **Flow selection: 5–10 flows chosen from design doc examples** (enrollment, grading, authentication) plus whatever the index reveals as highest-traffic; each walkthrough traces the actual call path from the structural index.
4. **Layer 4 as notes, not server** — pick ~5 modules/files, manually mine git history for why-exists/coupling/blast-radius answers with PR/issue citations. This doubles as an early linkage-quality signal for the Phase 3 spike.
5. **Validation depends on ARBISOFTOPEN-444** — the 10-question template/rubric is a separate parallelizable change; this change *consumes* it. Sequencing guard: run the "before" check early (against the un-onboarded repo) so onboarding work doesn't contaminate it.
6. **Review per CONTRIBUTING.md** — proposal+specs reviewed by a teammate before pilot work starts; the pilot artifacts themselves are reviewed by whoever knows edx-platform best.

## Risks / Trade-offs

- [Timing data polluted by learning-curve effects (first-ever run)] → log "first-time overhead" separately from repeatable effort in the could-automate notes.
- [edx-platform is huge; flow walkthroughs could balloon] → cap at 10 flows, timebox per design doc estimate (1–2 weeks total).
- [Layer-2 tooling (codebase-memory-mcp) may fight a repo this size] → note failures in the log; they are findings, not blockers — degraded output is itself pilot data.
- [Before/after check biased if the same person onboards and answers] → answerer for the 10 questions is the agent (per design doc §6), scored by a human who didn't write the docs where team size allows.

## Migration Plan

Additive files only. Merge via PR per CONTRIBUTING.md; archive the change after merge.

## Open Questions

- Which teammate owns the pilot review (should be whoever knows edx-platform best) — assign in Plane before starting.

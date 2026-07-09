# Team Workflow — Design

## Context

3-person team, spec-driven workflow already used for `phase-0-bootstrap`. Enforcement today = zero. GitHub branch protection can't be set from repo files, so enforcement is layered: written rule → PR template prompt → CI gate → (manual) branch protection.

## Goals / Non-Goals

**Goals:**
- The workflow rule is discoverable in the repo and enforced by CI, not by memory.
- CI fails on broken tests, lint violations, or malformed OpenSpec artifacts.

**Non-Goals:**
- No CODEOWNERS / formal capability sign-off — overkill at 3 people.
- No CLI entry point (still Phase 2).
- No enforcement bots (e.g. PR-body linting) — the human reviewer checks the spec link.

## Decisions

1. **Single CI workflow, one job** — `pytest` + `ruff check` + `openspec validate --all --no-interactive` in one job on ubuntu-latest, Python 3.12. Matrix builds and job splitting are noise at this repo size. OpenSpec runs via `npx --yes @fission-ai/openspec@1` (pinned major; no global install to maintain).
2. **PR template asks for the spec-change link with a trivial-fix escape hatch** — typo/docs-only fixes shouldn't require a spec change; the reviewer judges whether the exemption is abused. Alternative (hard-require via bot) rejected: friction > value at this size.
3. **CONTRIBUTING.md is the single source of the rule** — README links to it; the PR template references it. One place to update.
4. **Review = 1 approving teammate on the spec artifacts before implementation starts** — recorded in CONTRIBUTING.md; mechanically backed by branch protection (manual GitHub setting, documented in CONTRIBUTING.md).

## Risks / Trade-offs

- [CI can't verify "spec was reviewed before coding started"] → branch protection + PR template make it socially auditable; accepted.
- [`openspec validate --all` may fail on future schema changes after CLI upgrades] → version pinned to major 1 in CI.
- [pip `--group` needs pip ≥25.1] → CI upgrades pip before install (same fix used locally).

## Migration Plan

Additive files; CI turns on automatically on push. Repo owner enables branch protection once. Rollback = delete the workflow file.

## Open Questions

None.

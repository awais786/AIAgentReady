# Team Workflow — Spec-First Rule, Enforced in the Repo

## Why

The team is growing to 3 contributors. The spec-first loop (propose → review → implement → archive) currently exists only as convention in one person's head; nothing in the repo states it or enforces it. Without written rules and CI gates, the review-before-coding contract will erode as soon as two people work in parallel.

## What Changes

- Add `CONTRIBUTING.md` stating the mandatory workflow: every feature starts as an OpenSpec change; a second teammate reviews proposal + specs before implementation; archive on merge.
- Add a pull-request template requiring a link to the approved OpenSpec change (or an explicit exemption for trivial fixes).
- Add CI (GitHub Actions) that runs on every PR and push to `main`: `pytest`, `ruff check`, and `openspec validate --all` — closing the CI item deferred from `phase-0-bootstrap` (ARBISOFTOPEN-438).
- Document the branch-protection setting (require 1 approving review) that must be enabled in GitHub settings — not enforceable from inside the repo.

## Capabilities

### New Capabilities
- `contribution-workflow`: the written, tooling-enforced rules a change must pass to reach `main`

### Modified Capabilities

None — `repo-structure` and `python-packaging` requirements are unchanged; CI consumes their existing verification commands.

## Impact

- New files only: `CONTRIBUTING.md`, `.github/pull_request_template.md`, `.github/workflows/ci.yml`; README gains a Contributing pointer.
- CI supersedes the "no repo CI in Phase 0" non-goal in `phase-0-bootstrap/design.md` — the calculus changed with 3 contributors.
- Requires a one-time manual step by the repo owner: enable branch protection on `main`.

# Team Workflow — Tasks

## 1. Documentation

- [x] 1.1 Create `CONTRIBUTING.md` — spec-first workflow steps, 1-reviewer rule on proposal+specs before coding, archive-on-merge, trivial-fix exemption, branch-protection instructions
- [x] 1.2 Add Contributing section/link to root `README.md`

## 2. Enforcement tooling

- [x] 2.1 Create `.github/pull_request_template.md` — OpenSpec change link field + trivial-fix exemption checkbox
- [x] 2.2 Create `.github/workflows/ci.yml` — on PR + push to main: Python 3.12, upgrade pip, `pip install -e . --group dev`, `pytest`, `ruff check .`, `npx --yes @fission-ai/openspec@1 validate --all --no-interactive`

## 3. Verify

- [x] 3.1 Run the three CI commands locally (pytest, ruff, openspec validate --all) — all pass
- [x] 3.2 `openspec validate team-workflow` passes

## 4. Ship

- [x] 4.1 Commit on `main` referencing ARBISOFTOPEN-438 (closes deferred CI scope), push, confirm Actions run is green
- [ ] 4.2 Repo owner enables branch protection on `main` (require 1 approving review) — manual GitHub step

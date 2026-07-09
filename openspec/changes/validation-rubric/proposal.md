# Validation Rubric — 10-Question Template + Scoring

## Why

The kit is never delivered with zero measurement (design doc §6): every engagement includes a before/after table from a ten-question check. That template and rubric don't exist yet, and Phase 1's first tasks need them — the "before" run must happen prior to any onboarding artifacts being produced (ARBISOFTOPEN-444, extracted from ARBISOFTOPEN-439 so it can be built in parallel).

## What Changes

- Create `templates/validation/` containing:
  - `questions.md` — ten fixed question *types* about a codebase ("where is X implemented", "how does flow Y work", "why does module Z exist"), with guidance for instantiating them per target repo
  - `rubric.md` — human-reviewer scoring scale per question and what counts as correct / partial / wrong
  - `before-after-table.md` — the result-table format that drops into engagement reports
- Instantiate the template once against edx-platform (ten concrete questions) as its first use and a worked example, stored with the template as `example-edx-platform.md`.

## Capabilities

### New Capabilities
- `validation-rubric`: the repo-agnostic 10-question check — question types, instantiation guidance, scoring rubric, and result format — consumed by every pilot and engagement (already referenced by the `pilot-measurements` capability)

### Modified Capabilities

None — `pilot-measurements` already references this capability by name; its requirements don't change.

## Impact

- New files under `templates/validation/` only; no code.
- Unblocks `phase-1-edx-pilot` task 1.3 (the "before" run on edx-platform).
- Reused by Phase 4's engagement report template and Phase 5's second-repo run.

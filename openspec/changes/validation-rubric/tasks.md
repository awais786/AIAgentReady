# Validation Rubric — Tasks

## 1. Templates

- [x] 1.1 Write `templates/validation/questions.md` — ten question types (≈4 location / 3 behavior / 3 rationale) with per-type instantiation guidance (draw from real tasks/issues) and the exact agent prompt to use for runs
- [x] 1.2 Write `templates/validation/rubric.md` — 0/1/2 scale with per-level definitions and the one-line-justification rule
- [x] 1.3 Write `templates/validation/before-after-table.md` — result table format + run-log fields (agent, model, date)

## 2. Worked example

- [x] 2.1 Instantiate for edx-platform: `templates/validation/example-edx-platform.md` with ten concrete questions, each traceable to a real edx-platform task, flow, or module

## 3. Verify and ship

- [ ] 3.1 Dry-run: a teammate (not the author) scores a sample answer with the rubric and confirms the guidance is unambiguous; adjust wording if not
- [ ] 3.2 `openspec validate validation-rubric` passes; PR per CONTRIBUTING.md; update ARBISOFTOPEN-444; archive on merge

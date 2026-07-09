# 10-Question Validation Check — Result Format

Copy this file into the pilot/engagement workspace (e.g.
`pilots/<target-repo>/pilot/validation.md`), fill it in, and include the table directly in
the engagement report. Full answer transcripts are kept alongside but the table must
communicate the delta on its own.

## Run log

| Run | Date | Agent / model | Repo state (SHA) | Onboarding artifacts present? |
|-----|------|---------------|------------------|-------------------------------|
| Before | | | | none (must predate Layer-1 work) |
| After | | | | full kit output |

Prompt: per `templates/validation/questions.md`, byte-identical across runs.
Scorer(s): `<name>` — justifications per `templates/validation/rubric.md`.

## Results

| # | Type | Question | Before — answer summary | Score | After — answer summary | Score |
|---|------|----------|------------------------|:-----:|------------------------|:-----:|
| 1 | location | | | | | |
| 2 | location | | | | | |
| 3 | location | | | | | |
| 4 | location | | | | | |
| 5 | behavior | | | | | |
| 6 | behavior | | | | | |
| 7 | behavior | | | | | |
| 8 | rationale | | | | | |
| 9 | rationale | | | | | |
| 10 | rationale | | | | | |

## Totals

| | Before | After | Delta |
|---|:---:|:---:|:---:|
| Total (max 20) | | | |
| Location (max 8) | | | |
| Behavior (max 6) | | | |
| Rationale (max 6) | | | |
| Honest-misses | | | |
| Fabrications | | | |

## Reading the result

- **Total delta** is the headline number for the engagement report.
- **Per-category deltas** attribute the gain: location/behavior gains usually come from
  Layers 1–3; rationale gains from Layer 4.
- **Fabrications after onboarding** are a red flag regardless of total: investigate the
  artifact that misled the agent before delivering.

## Score justifications

One line per cell, per the rubric:

```
Q1 before: ...
Q1 after: ...
...
```

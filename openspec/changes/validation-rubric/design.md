# Validation Rubric — Design

## Context

Design doc §6 fixes the shape: ten fixed questions, same agent before and after onboarding, human-scored, ~1 day per repo. This change turns that paragraph into concrete, reusable templates. It is deliberately small — a good starter change for a teammate learning the workflow.

## Goals / Non-Goals

**Goals:**
- A repo-agnostic template any teammate can instantiate for a new target repo in under an hour.
- Scoring consistent enough that two reviewers would land within one point of each other per question.

**Non-Goals:**
- No automation/harness — running the check stays manual (design doc scoped the benchmark harness out).
- No statistical rigor claims — this is the minimum evidence standard, not the v2/v3 benchmark.

## Decisions

1. **Question *types*, not fixed questions** — the ten entries are parameterized types spanning the three design-doc categories (location: "where is X implemented", behavior: "how does flow Y work", rationale: "why does module Z exist"), instantiated per repo. Rationale: fixed questions can't transfer across repos; types + instantiation guidance can. Distribution decided in the template (roughly 4 location / 3 behavior / 3 rationale — rationale questions are what Layer 4 exists for).
2. **3-point scale per question (0 wrong / 1 partial / 2 correct)** with per-level definitions in the rubric. Alternative (binary) rejected: partial answers are the common case on legacy repos and a binary scale hides the delta the kit produces.
3. **Worked example ships with the template** — the edx-platform instantiation lives in `templates/validation/example-edx-platform.md`, doing double duty as documentation and as the actual question set Phase 1 will use.
4. **Answering agent gets the same prompt before and after** — the template records the exact prompt wording so before/after runs differ only in the repo's onboarding state.

## Risks / Trade-offs

- [Questions instantiated by whoever onboards the repo may be soft-balls] → instantiation guidance requires questions be drawn from real tasks/issues, and the reviewer of the pilot change reviews the question set too.
- [One human scorer = subjectivity] → rubric per-level definitions + scores recorded with a one-line justification each.

## Migration Plan

Additive files under `templates/validation/`. No rollback concerns.

## Open Questions

None.

# 10-Question Validation Check — Scoring Rubric

Each answer is scored by a human reviewer on a 0/1/2 scale. Every recorded score MUST
carry a one-line justification. Where team size allows, the scorer should not be the
person who produced the onboarding artifacts.

## The scale

| Score | Level | Definition |
|-------|-------|------------|
| **2** | Correct | Factually right AND concretely grounded: names the actual files/classes/functions (or commits/PRs for rationale questions). A contributor could act on it directly without re-verification. |
| **1** | Partial | Right general area or mechanism but missing the concrete grounding — e.g. correct module but wrong/absent file, correct flow shape but a wrong step, correct rationale without support. A contributor would still need to search. |
| **0** | Wrong | Factually incorrect, fabricated paths/symbols, an honest "cannot find" — or an answer so vague it gives a contributor nothing actionable. |

## Scoring rules

- **Fabrication caps at 0** even if parts are right: an answer citing files or symbols that
  don't exist scores 0 — confident misinformation is worse for an agent workflow than no
  answer (design doc §4).
- **"I could not find this" scores 0** but note it as `honest-miss` in the justification;
  the before-run typically contains several of these and the distinction matters when
  reading the delta.
- **Score the answer, not the effort**: a short correct answer outranks a long partial one.
- **Rationale questions (Q8–Q10)**: a 2 requires the answer to be supported (commit, PR,
  issue, doc, or code comment); an unsupported-but-plausible story is at most 1.
- **Resolve doubt downward**: if torn between two scores, give the lower and say why in
  the justification.

## Justification format

One line per score, stating what earned or lost points:

```
Q5 after: 2 — traced enrollment from views.py:enroll() through CourseEnrollment.enroll,
matches code.
Q8 before: 0 (honest-miss) — agent said it could not determine why the module exists.
```

## Consistency check

The rubric intends two independent reviewers to land within one point of each other on any
answer. On a team's first use (and periodically after), have a second reviewer blind-score
2–3 answers; if any score differs by 2 points, tighten the question's expected answer notes
before finalizing results.

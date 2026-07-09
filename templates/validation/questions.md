# 10-Question Validation Check — Question Types

The kit's minimum evidence standard (design doc §6). Instantiate these ten question types
for a target repo, run the same agent **before** onboarding (no kit artifacts present) and
**after**, score with [rubric.md](rubric.md), record results in
[before-after-table.md](before-after-table.md).

## Instantiation guidance

- Every question MUST be drawn from the target repo's **real tasks, flows, or modules** —
  things a new contributor genuinely needs to know. Source them from recent issues, PRs,
  onboarding pain points, or support questions; never invent hypotheticals.
- Fill each `<placeholder>` with a concrete name from the repo. Keep the question wording
  otherwise unchanged.
- The question set is fixed **before** the "before" run and never edited afterwards.
- A worked instantiation lives in [example-edx-platform.md](example-edx-platform.md).

## The ten question types

### Location — where is it? (Q1–Q4)

1. **Where is `<feature X>` implemented?** — expected answer names the primary module/files
   and the key class or function.
2. **Where would a change to `<behavior Y>` need to be made?** — expected answer names the
   file(s) a correct patch would touch.
3. **Which tests cover `<component Z>`, and how do I run just those?** — expected answer
   names the test files/suites and the command.
4. **Where is `<configuration/setting W>` defined and where is it consumed?** — expected
   answer traces definition to point(s) of use.

### Behavior — how does it work? (Q5–Q7)

5. **How does `<runtime flow Y>` work end to end?** — expected answer traces the actual
   call path (entry point → key steps → outcome).
6. **What happens when `<event/input E>` occurs?** — expected answer describes the
   handling path including error/edge branches.
7. **How do `<component A>` and `<component B>` interact?** — expected answer names the
   interface/contract between them (API, signal, queue, table).

### Rationale — why is it this way? (Q8–Q10)

8. **Why does `<module Z>` exist?** — expected answer gives the purpose and the problem it
   was introduced to solve.
9. **Why is `<surprising pattern P>` done this way?** — expected answer gives the
   historical or technical constraint (the "landmine" class of knowledge).
10. **What is risky to change in `<area Q>`, and why?** — expected answer names known
    coupling or past breakage.

## Agent prompt (use verbatim for both runs)

The before and after runs MUST use this prompt byte-identically; only the repo's onboarding
state may differ between runs. Record agent, model, and date per run in the results table.

```
You are working in the repository at the current directory. Answer the following question
about this codebase as concretely as you can: name specific files, classes, functions, or
commits. If you cannot find the answer, say so explicitly rather than guessing.

Question: <question text>
```

Ask the ten questions in separate, fresh sessions (no shared conversation state), in the
same order in both runs.

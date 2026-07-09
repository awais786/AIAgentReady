# Contributing

This repo uses a **spec-first workflow** ([OpenSpec](https://github.com/Fission-AI/OpenSpec)).
The rule, in one line: **nobody starts coding a feature whose proposal hasn't been read and
approved by a second teammate.**

## The workflow

1. **Propose.** Start every non-trivial change as an OpenSpec change:
   `/opsx:propose` (in Claude Code) or `openspec new change <kebab-name>`, then fill in
   `proposal.md`, `specs/`, and `tasks.md` under `openspec/changes/<name>/`.
   Add `design.md` only when there is a real decision to argue (new dependency,
   architecture, cross-cutting concern).
2. **Review — before any implementation.** Open a PR containing only the change directory.
   One teammate reads `proposal.md` and the scenario lists and approves. Behavioral
   disagreements happen here, where a change costs a sentence instead of a refactor.
3. **Implement.** Work through `tasks.md` (`/opsx:apply`), ticking checkboxes as tasks
   complete — honestly, never in advance. The scenarios in the specs are the acceptance
   criteria; implementation review checks code against them.
4. **Verify.** `pytest`, `ruff check .`, and `openspec validate --all` must pass locally
   (CI runs the same three).
5. **Archive on merge.** When the implementation merges, run `/opsx:archive` (or
   `openspec archive <name>`) so the delta specs fold into `openspec/specs/` — the living
   description of what the system does. Archiving is part of "done".

## Trivial-fix exemption

Typo fixes, comment/docs-only edits, and pure formatting need no OpenSpec change — tick the
exemption box in the PR template instead. The reviewer judges whether the exemption fits;
anything that changes behavior does not qualify.

## Pull requests

- Every PR links its approved OpenSpec change (or claims the trivial-fix exemption).
- CI must be green: tests, lint, and OpenSpec validation.
- One approving review required to merge.

## Branch protection (repo owner, one-time setup)

GitHub → Settings → Branches → Add branch ruleset for `main`:

- Require a pull request before merging, with **1 approving review**
- Require status checks to pass: **ci**

Without this, everything above is convention only.

## Development setup

Requires Python ≥3.11 and pip ≥25.1 (`pip install --upgrade pip`).

```bash
pip install -e . --group dev
pytest
ruff check .
```

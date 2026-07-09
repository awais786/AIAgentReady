# contribution-workflow

## ADDED Requirements

### Requirement: Workflow rule is documented in the repo
The repository SHALL contain a `CONTRIBUTING.md` that states the mandatory spec-first workflow: every non-trivial change starts as an OpenSpec change; one teammate MUST approve the proposal and specs before implementation begins; the change MUST be archived when the implementation merges. It SHALL also document the required branch-protection setting.

#### Scenario: New contributor finds the rule
- **WHEN** a contributor opens the repository README or `CONTRIBUTING.md`
- **THEN** they find the spec-first workflow steps, the review requirement, and the archive-on-merge rule without asking a teammate

### Requirement: Pull requests declare their spec change
The repository SHALL provide a pull-request template that requires either a link to the approved OpenSpec change or an explicit trivial-fix exemption.

#### Scenario: Feature PR opened
- **WHEN** a contributor opens a PR on GitHub
- **THEN** the PR body is pre-filled with a section asking for the OpenSpec change link and an exemption checkbox for trivial fixes

### Requirement: CI gates every pull request and push to main
The repository SHALL run a CI workflow on every pull request and push to `main` that fails if `pytest` fails, `ruff check .` reports violations, or `openspec validate --all` reports invalid changes or specs.

#### Scenario: Broken test blocks merge
- **WHEN** a PR contains a failing test, a lint violation, or a malformed OpenSpec artifact
- **THEN** the CI workflow fails and the PR cannot be merged cleanly

#### Scenario: Healthy PR passes
- **WHEN** a PR passes tests, lint, and OpenSpec validation
- **THEN** the CI workflow succeeds with all three checks executed

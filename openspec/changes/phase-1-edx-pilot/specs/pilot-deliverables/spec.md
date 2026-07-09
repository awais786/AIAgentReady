# pilot-deliverables

Generic requirements for any manual pilot run of the kit. A pilot targets one repository
("the target repo"); its artifacts land in `pilots/<target-repo>/`. The first instance is
edx-platform (this change); later instances (e.g. the Phase 5 second repo) reuse these
requirements unchanged.

## ADDED Requirements

### Requirement: Complete PR-shape file set
A pilot SHALL produce the full deliverable file set of design doc §3 under `pilots/<target-repo>/`, at the paths the files would occupy in the target repo: `CLAUDE.md`, agent settings with noise exclusions, structural-index MCP config, git-intelligence MCP config (stub until the Phase 3 server exists), `docs/ai/modules.md`, at least five flow walkthroughs in `docs/ai/flows/`, `docs/ai/conventions.md`, and a freshness-hook CI workflow.

#### Scenario: Deliverable set is complete
- **WHEN** a pilot is declared done
- **THEN** every file above exists under `pilots/<target-repo>/` and none is an empty placeholder

### Requirement: Layer 1 covers the agent-configuration contract
The pilot `CLAUDE.md` SHALL cover architecture overview, module map, key conventions, how to run tests and lint, and known landmines — all specific to the target repo; the agent settings SHALL exclude the target repo's noise directories (e.g. migrations, translation files, vendored and generated code) from agent context.

#### Scenario: CLAUDE.md sections present
- **WHEN** a reviewer reads the pilot `CLAUDE.md`
- **THEN** all five content areas are present and specific to the target repo (no template boilerplate left)

#### Scenario: Noise exclusions active
- **WHEN** a reviewer inspects the agent settings
- **THEN** every excluded path exists in the target repo and matches its actual noise directories

### Requirement: Generated docs are grounded
Every claim in the pilot's `docs/ai/` documentation SHALL cite a file path or symbol that exists in the target repo checkout; flow walkthroughs SHALL trace actual call paths from the structural index.

#### Scenario: Spot-check citations
- **WHEN** a reviewer samples ten citations across the generated docs
- **THEN** all ten resolve to real files or symbols in the target repo

### Requirement: Git-intelligence notes with citations
A pilot SHALL include Layer-4 notes answering why-exists, change-coupling, and blast-radius questions for at least five modules of the target repo, each answer citing real commits, PRs, or issues.

#### Scenario: Rationale is traceable
- **WHEN** a reviewer follows any citation in the git-intelligence notes
- **THEN** it resolves to a real commit/PR/issue supporting the stated rationale

### Requirement: Human review before done
Every pilot artifact SHALL be reviewed by an engineer familiar with the target repo, with corrections and tribal knowledge (landmines) added by hand, before the pilot is declared complete.

#### Scenario: Review recorded
- **WHEN** the pilot PR is merged
- **THEN** the PR shows an approving review and the pilot report names who reviewed the artifact set

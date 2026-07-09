# repo-structure Specification

## Purpose
TBD - created by archiving change phase-0-bootstrap. Update Purpose after archive.
## Requirements
### Requirement: Canonical directory layout
The repository SHALL contain the canonical Phase 0 layout: `src/aiagentready/` with subpackages `analyzer/`, `generators/`, `grounding/`, `validation/`; `mcp-git-intelligence/`; `templates/`; `pilots/edx-platform/`; and `docs/adr/`.

#### Scenario: Fresh clone has all top-level directories
- **WHEN** the repository is cloned from GitHub
- **THEN** `src/aiagentready/`, `mcp-git-intelligence/`, `templates/`, `pilots/edx-platform/`, and `docs/adr/` all exist and are non-empty (each contains at least a README or `__init__.py`)

#### Scenario: Placeholder directories explain their purpose
- **WHEN** a contributor opens `mcp-git-intelligence/`, `templates/`, or `pilots/edx-platform/`
- **THEN** each contains a README stating what will live there and which roadmap phase fills it in

### Requirement: Stack decision recorded as ADR
The repository SHALL contain `docs/adr/0001-python-stack.md`, an accepted ADR recording the choice of Python as the implementation language, its rationale, and the deferred package-rename note.

#### Scenario: ADR-0001 present and accepted
- **WHEN** a contributor reads `docs/adr/0001-python-stack.md`
- **THEN** it has Status: Accepted, states why Python was chosen, and notes the pending product-name decision

### Requirement: Repository pushed to GitHub
The scaffold SHALL be committed on `main` and pushed to `origin` (https://github.com/awais786/AIAgentReady), and the commit SHALL NOT include the design-doc files (`AIAgentReady-Design-Doc.docx`, `AIAgentReady-Design-Doc.txt`).

#### Scenario: Remote main matches local scaffold
- **WHEN** the initial commit is pushed
- **THEN** `git log origin/main` shows the scaffold commit and the GitHub repo is no longer empty

#### Scenario: Design doc excluded
- **WHEN** the initial commit is inspected
- **THEN** no `AIAgentReady-Design-Doc.*` file is tracked, and `.gitignore` prevents accidental staging


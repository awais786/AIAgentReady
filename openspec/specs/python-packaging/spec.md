# python-packaging Specification

## Purpose
TBD - created by archiving change phase-0-bootstrap. Update Purpose after archive.
## Requirements
### Requirement: Installable package
The `aiagentready` package SHALL be installable with `pip install -e .` from the repo root, using a `pyproject.toml` (src layout, Python ≥3.11) as the single source of packaging metadata.

#### Scenario: Editable install succeeds
- **WHEN** `pip install -e .` is run in a fresh virtualenv at the repo root
- **THEN** the install succeeds and `python -c "import aiagentready; print(aiagentready.__version__)"` prints the version

#### Scenario: Subpackages importable
- **WHEN** the package is installed
- **THEN** `aiagentready.analyzer`, `aiagentready.generators`, `aiagentready.grounding`, and `aiagentready.validation` all import without error

### Requirement: Test tooling works from a fresh clone
The repository SHALL include pytest configuration and at least one smoke test, such that `pytest` passes on a fresh clone after an editable install.

#### Scenario: Smoke test passes
- **WHEN** `pytest` is run at the repo root
- **THEN** the smoke test verifying the package and all four subpackages import (and `__version__` is set) passes with zero failures

### Requirement: Lint tooling works from a fresh clone
The repository SHALL include ruff configuration in `pyproject.toml`, such that `ruff check .` passes on a fresh clone.

#### Scenario: Lint passes clean
- **WHEN** `ruff check .` is run at the repo root
- **THEN** it exits 0 with no violations


# validation-rubric

The repo-agnostic 10-question validation check (design doc §6): the kit's minimum evidence
standard, consumed by every pilot run (`pilot-measurements`) and engagement report.

## ADDED Requirements

### Requirement: Ten parameterized question types
`templates/validation/questions.md` SHALL define exactly ten question types covering the three design-doc categories — location ("where is X implemented"), behavior ("how does flow Y work"), and rationale ("why does module Z exist") — each with instantiation guidance requiring questions be drawn from the target repo's real tasks or issues.

#### Scenario: Template is instantiable
- **WHEN** a teammate instantiates the template for a new target repo
- **THEN** they can produce ten concrete questions without inventing new structure, and every question traces to a real task, flow, or module of that repo

#### Scenario: Categories covered
- **WHEN** the ten questions are instantiated per the template's distribution
- **THEN** all three categories (location, behavior, rationale) are represented

### Requirement: Scoring rubric
`templates/validation/rubric.md` SHALL define a 0/1/2 scale (wrong / partial / correct) with per-level definitions, and SHALL require a one-line justification per recorded score.

#### Scenario: Two reviewers converge
- **WHEN** two reviewers independently score the same answer set using the rubric
- **THEN** per-question scores differ by at most one point

### Requirement: Before/after result format
`templates/validation/before-after-table.md` SHALL define the result table — per question: question text, before answer summary, before score, after answer summary, after score — plus totals, suitable for direct inclusion in an engagement report.

#### Scenario: Report-ready output
- **WHEN** a completed check is transcribed into the table
- **THEN** the table alone communicates the before/after delta without reading the full answer transcripts

### Requirement: Identical prompting before and after
The template SHALL record the exact agent prompt used for the check, and both runs of a before/after pair SHALL use it unchanged — the only difference between runs being the presence of onboarding artifacts in the repo.

#### Scenario: Prompt parity
- **WHEN** the before and after runs are executed
- **THEN** their prompts are byte-identical per the template, and the run log records agent, model, and date for each

### Requirement: Worked example
`templates/validation/example-edx-platform.md` SHALL contain a full instantiation for edx-platform — ten concrete questions ready for the Phase 1 pilot to execute.

#### Scenario: Example doubles as pilot input
- **WHEN** the Phase 1 pilot reaches its "before" check
- **THEN** the edx-platform question set already exists and passes the instantiation guidance (each question traceable to a real edx-platform task, flow, or module)

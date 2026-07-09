# pilot-measurements

Generic measurement requirements for any manual pilot run. Together with the deliverables,
these make every pilot produce comparable evidence: effort baseline, validation delta, and
an automation spec. Applies to the first instance (edx-platform) and all later runs.

## ADDED Requirements

### Requirement: Per-artifact timing log
A pilot SHALL maintain `pilots/<target-repo>/pilot/timing-log.md` recording, for every deliverable artifact: time spent, analysis performed, inputs required, and notes on what automation would need to reproduce it — captured while the work happens, with first-time learning overhead flagged separately from repeatable effort.

#### Scenario: Log covers all artifacts
- **WHEN** a pilot is declared done
- **THEN** every file in the deliverable set has a timing-log entry with all four fields filled

### Requirement: Before/after validation check
A pilot SHALL run the 10-question check (template and rubric from the validation-rubric capability, ARBISOFTOPEN-444): the same agent answers the ten questions against the target repo before onboarding and after, scored by a human reviewer, with the "before" run executed prior to any onboarding artifacts being available to the agent.

#### Scenario: Scored table exists
- **WHEN** a pilot is declared done
- **THEN** `pilots/<target-repo>/pilot/validation.md` contains the ten questions, both answer sets, and per-question scores from the rubric

#### Scenario: Before-run is uncontaminated
- **WHEN** the "before" answers are produced
- **THEN** the agent had no access to any pilot-produced artifact (verified by the run being dated/logged before Layer-1 work began)

### Requirement: Pilot report
A pilot SHALL produce `pilots/<target-repo>/pilot/report.md` summarizing total and per-layer effort, findings, tooling failures or degraded output encountered, the before/after result, and an explicit list of what automation must produce per layer — usable as an automation acceptance reference and an engagement pricing baseline.

#### Scenario: Report answers the three pilot questions
- **WHEN** a teammate reads the report without having done the pilot
- **THEN** they can state the ideal output shape, what automation must produce per layer, and the effort baseline per layer

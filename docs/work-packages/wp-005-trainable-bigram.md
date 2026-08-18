# WP-005: Trainable bigram model

## Identifier

WP-005

## Title

Trainable bigram model

## Status

Proposed

## Purpose

Introduce the first trainable neural model and compare it with counts.

## Learning outcomes

Explain and implement trainable bigram model in an evidence-backed way.

## Background concepts

Probability, tensor shapes, optimization, software packaging, and component-specific architecture concepts.

## Relevant mathematics

Use the equations and tensor-shape conventions from `docs/architecture/mathematical-foundations.md` and link any new math to tests or experiments.

## Scope

Implement and document trainable bigram model with tests, experiments, and guide updates appropriate to the work package stage.

## Explicit exclusions

Do not skip tests, evidence capture, or documentation updates. Do not widen scope into unrelated infrastructure.

## Dependencies

WP-004

## Related ADRs

ADR-0003, ADR-0009, ADR-0010

## Design impact

Extends the `tiny_llm` package while preserving explicit architectural boundaries and CPU-first headless operation.

## Expected files

Relevant updates under `src/`, `tests/`, `configs/`, `docs/`, and `reports/`.

## Implementation steps

1. Refine assumptions and constraints.
2. Implement the smallest correct version.
3. Add tests and numerical checks.
4. Run a bounded smoke experiment or operational check.
5. Update guides and evidence artifacts.

## Tests

- Unit tests for the component or workflow.
- Numerical tests where applicable.
- Integration coverage for end-to-end behavior.

## Experiments

- Short smoke run or deterministic example showing the behavior is observable.

## Acceptance criteria

- Code works for the scoped behavior.
- Tests pass.
- Evidence artifacts are recorded.
- Documentation reflects observed behavior and limitations.

## Required evidence

- Exact commands used.
- Updated documentation.
- Relevant tests.
- Configuration or checkpoint evidence where applicable.
- Honest limitations and follow-up notes.

## Process-documentation updates

- Update roadmap or status tables if the work package state changes.
- Update changelog for material additions.
- Update reports and experiment artifacts as needed.

## User-guide updates

Document any new user-facing commands, workflows, or caveats.

## Operations-guide updates

Document any new runtime requirements, monitoring steps, or recovery procedures.

## Developer-guide updates

Document any new architectural boundaries, test commands, or extension points.

## Risks

- Educational clarity may be lost if implementation becomes too abstract.
- Legacy hardware constraints may force design adjustments.
- Missing evidence could lead to overstated confidence.

## Recovery or rollback approach

Revert the affected component, keep the last known-good checkpoint or config, and document the failure mode before retrying.

## Reflection questions

- What concept does this work package teach?
- What evidence demonstrates correctness or current limitations?
- What assumptions remain unverified after completion?

## Definition of done

The work package is done only when implementation, tests, documentation, and evidence are all updated consistently.

## Completion record

Pending.

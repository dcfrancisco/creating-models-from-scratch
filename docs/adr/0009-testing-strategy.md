# ADR-0009: Testing and Numerical Correctness Strategy

## Status

Accepted

## Date

2026-08-18

## Context

Educational trust requires layered tests instead of relying on visual inspection or anecdotal runs.

## Decision drivers

- Preserve educational clarity.
- Support headless CPU-first operation.
- Maintain reproducibility and inspectability.
- Avoid unverified assumptions on legacy hardware.

## Considered options

- Ad-hoc manual checks
- Unit/numerical/integration layers
- Only end-to-end tests

## Decision

Adopt layered unit, numerical, and integration tests with deterministic fixtures and tolerant floating-point comparisons.

## Consequences

- Documentation, tests, and implementation must align with this decision.
- Future work packages should revisit this decision only when the stated evidence changes.

## Risks

- The chosen path may slow progress compared with using more abstraction.
- Some follow-on work depends on runtime evidence that may contradict current expectations.

## Validation evidence

- Project charter and roadmap align with the decision.
- Engineering baseline code and configuration structure implement the decision where currently possible.
- Additional runtime evidence will be gathered in the linked work packages when required.

## Revisit conditions

- New hardware evidence invalidates a compatibility assumption.
- A later work package exposes a material limitation or contradiction.
- A replacement design provides better educational clarity without hiding core mechanisms.

## Related work packages

- WP-001 through WP-014

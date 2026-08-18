# ADR-0008: Configuration and Reproducibility Strategy

## Status

Accepted

## Date

2026-08-18

## Context

Model and training parameters should live outside source code where practical and be captured in artifacts.

## Decision drivers

- Preserve educational clarity.
- Support headless CPU-first operation.
- Maintain reproducibility and inspectability.
- Avoid unverified assumptions on legacy hardware.

## Considered options

- Hard-coded parameters
- TOML configs
- Interactive notebook state

## Decision

Use TOML configuration files validated before execution and persisted into checkpoints and experiment records.

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

- WP-001, WP-008, WP-010

# ADR-0010: Experiment Evidence and Checkpoint Format

## Status

Accepted

## Date

2026-08-18

## Context

Runs need machine-readable and human-readable evidence plus compatibility-checked checkpoints.

## Decision drivers

- Preserve educational clarity.
- Support headless CPU-first operation.
- Maintain reproducibility and inspectability.
- Avoid unverified assumptions on legacy hardware.

## Considered options

- Loose text notes
- Structured JSON + markdown + self-describing checkpoints
- Opaque binary only

## Decision

Store structured experiment records and checkpoint metadata containing config, identity, versions, metrics, and timestamps.

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

- WP-011, WP-012

# ADR-0003: Numerical Backend and PyTorch Compatibility Strategy

## Status

Proposed

## Date

2026-08-18

## Context

PyTorch compatibility is uncertain on the target legacy CPU, so the numerical backend decision requires runtime evidence.

## Decision drivers

- Preserve educational clarity.
- Support headless CPU-first operation.
- Maintain reproducibility and inspectability.
- Avoid unverified assumptions on legacy hardware.

## Considered options

- Require PyTorch
- NumPy first, PyTorch optional
- Custom C backend immediately

## Decision

Adopt NumPy as the required baseline and treat PyTorch as optional pending hardware qualification evidence.

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

- WP-000, WP-001, WP-010

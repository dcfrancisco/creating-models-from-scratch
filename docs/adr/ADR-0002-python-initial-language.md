# ADR-0002: Python as the Initial Implementation Language
- Status: Accepted
- Date: 2026-08-18

## Context
Need portable, inspectable implementation for CPU-first headless host.

## Decision drivers
Ecosystem maturity, readability, low friction for learners.

## Considered options
Python, C++, Rust.

## Decision
Use Python for baseline implementation.

## Consequences
Faster iteration; lower raw performance than compiled implementations.

## Risks
Potential runtime overhead on legacy CPU.

## Validation evidence
Python CLI baseline committed.

## Revisit conditions
If performance constraints block educational milestones.

## Related work packages
WP-000, WP-001

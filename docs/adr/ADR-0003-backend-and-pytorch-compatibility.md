# ADR-0003: Numerical Backend and PyTorch Compatibility Strategy
- Status: Proposed
- Date: 2026-08-18

## Context
Target CPU may not support modern prebuilt PyTorch wheels.

## Decision drivers
Compatibility, educational progression, reproducibility.

## Considered options
1. PyTorch required immediately
2. NumPy-first with optional PyTorch

## Decision
Adopt NumPy-first baseline; enable PyTorch only after qualification.

## Consequences
Can proceed on legacy CPUs without blocking.

## Risks
Split backend complexity over time.

## Validation evidence
Requires WP-000 hardware qualification on target machine.

## Revisit conditions
After PyTorch compatibility evidence is collected.

## Related work packages
WP-000, WP-005+

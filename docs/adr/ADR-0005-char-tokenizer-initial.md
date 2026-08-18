# ADR-0005: Character-Level Tokenization for the Initial Milestone
- Status: Accepted
- Date: 2026-08-18

## Context
Initial implementation should minimize complexity.

## Decision
Start with character-level tokenizer.

## Consequences
Simple and inspectable, but less efficient than subword tokenization.

## Validation evidence
Planned WP-003 with deterministic round-trip tests.

## Related work packages
WP-003, WP-014

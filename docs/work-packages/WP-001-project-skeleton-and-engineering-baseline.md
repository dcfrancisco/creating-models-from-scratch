# WP-001: Project Skeleton and Engineering Baseline

- Status: In Progress
- Purpose: Establish package, CLI, tests, and developer baseline.
- Scope: package skeleton, `doctor` command, tests, docs, repository hygiene.
- Explicit exclusions: tokenizer/model training logic.
- Dependencies: WP-000 (partial), ADR-0001, ADR-0002.
- Related ADRs: ADR-0001, ADR-0002, ADR-0007, ADR-0009, ADR-0011.

## Acceptance criteria
- Headless CLI command works
- Unit tests run for current baseline
- Core docs and governance skeleton exist

## Required evidence
- `python -m tiny_llm doctor`
- `pytest tests/unit`

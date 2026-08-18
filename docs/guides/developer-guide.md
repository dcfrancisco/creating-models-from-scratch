# Developer Guide

## Repository structure
- `src/tiny_llm/`: implementation
- `tests/unit`, `tests/integration`, `tests/numerical`, `tests/fixtures`
- `configs/smoke`, `configs/experiments`
- `docs/` architecture, governance, ADRs, work packages, reports

## Local setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Dependency policy
See `docs/governance/dependency-policy.md`.

## Architectural boundaries
No pretrained weights; no imported Transformer blocks; explicit component implementation.

## Coding conventions
- Type hints required
- Small focused modules
- Explicit shape notation in docs/comments

## Tensor-shape conventions
`B` batch, `T` sequence length, `C` embedding, `H` heads, `V` vocabulary, `L` blocks.

## Configuration system
Pending WP-001/WP-008 implementation under `configs/`.

## Test commands
```bash
pytest tests/unit
```

## Lint and type-check commands
```bash
ruff check src tests
mypy src
```

## Adding a model component
1. Create source module
2. Add unit + numerical tests
3. Update architecture docs
4. Record in relevant work package

## Adding an experiment
Follow evidence model and update `docs/reports/experiment-report.md`.

## Adding a configuration
Add file under `configs/smoke` or `configs/experiments` and document expected runtime cost.

## Adding an ADR
Copy `docs/adr/adr-template.md` and update `docs/adr/README.md` index.

## Adding a work package
Copy `docs/work-packages/work-package-template.md` and update index.

## Updating documentation
Documentation must reflect current implementation status and evidence.

## Evidence expectations
No correctness claim without tests/measurements/recorded commands.

## Definition of done
Code + tests + docs + evidence complete for the work package.

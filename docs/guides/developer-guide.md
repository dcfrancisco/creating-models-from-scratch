# Developer Guide

## Repository structure

- `src/tiny_llm/`: implementation modules
- `tests/`: unit, numerical, and integration tests
- `configs/`: smoke and experiment TOML files
- `docs/`: architecture, ADRs, work packages, guides, governance, and reports
- `scripts/`: operational helper scripts
- `data/`: local dataset placement guidance
- `artifacts/`: generated outputs that normally stay out of Git

## Local setup

```bash
python3 -m pip install -e ".[dev]"
python3 -m tiny_llm doctor
```

## Dependency policy

Runtime dependencies are intentionally minimal. NumPy is required. PyTorch is optional and must not be assumed present. See `docs/governance/dependency-policy.md`.

## Architectural boundaries

- `config.py`: configuration schema and validation
- `data.py`: text loading, checksums, splitting, and batching
- `tokenizer.py`: character tokenization only
- `model.py`: baseline modeling logic and future Transformer placeholders
- `train.py`: training orchestration
- `evaluate.py`: evaluation metrics and checkpoint-based evaluation
- `generate.py`: sampling and text generation
- `checkpoint.py`: serialization and metadata checks
- `doctor.py`: environment verification
- `experiment.py`: experiment evidence capture
- `cli.py`: user-facing headless interface

## Coding conventions

- Use clear type hints.
- Add a module docstring to every Python file.
- Add a docstring to every function.
- Prefer small explicit functions over hidden abstractions.
- Use `logging` in library code.
- Keep torch imports optional and local when possible.

## Tensor-shape conventions

Use `B` for batch size, `T` for sequence length, `C` for embedding dimension, `V` for vocabulary size, `H` for head count, and `L` for layer count.

## Configuration system

Configuration lives in TOML files under `configs/` and is loaded through `tiny_llm.config.load_config`. Always validate before starting expensive work.

## Test commands

```bash
python3 -m pytest tests/ -v
```

## Lint and type-check commands

```bash
python3 -m ruff check src tests
python3 -m mypy src
```

## Adding a model component

1. Record any material design change in an ADR if needed.
2. Implement the smallest correct version.
3. Add or update tests.
4. Update architecture and guide documentation.
5. Record evidence from a bounded run or numerical example.

## Adding an experiment

1. Create or choose a config under `configs/experiments/`.
2. Capture dataset checksum, config, backend, seed, and hardware notes.
3. Save checkpoint and sample outputs.
4. Write a machine-readable and human-readable record.

## Adding a configuration

- Keep names descriptive.
- Explain intended use in comments or nearby docs.
- Prefer smoke configs for routine development.

## Adding an ADR

Follow the format in `docs/adr/README.md` and keep numbering sequential.

## Adding a work package

Start from `docs/work-packages/template.md`, fill all fields, and keep the status honest.

## Updating documentation

Whenever behavior, commands, risks, or evidence changes, update the relevant guide, ADR, work package, and report stub.

## Evidence expectations

A change is not complete when code compiles alone. It also needs tests, docs, and observable evidence.

## Definition of done

A change is done when implementation, validation, documentation, and operational guidance are all synchronized.

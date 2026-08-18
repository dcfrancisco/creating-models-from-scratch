# Contributing

Thanks for contributing to `tiny_llm`.

## Development setup

```bash
python3 -m pip install -e ".[dev]"
python3 -m tiny_llm doctor
python3 -m pytest tests/ -v
python3 -m ruff check src tests
python3 -m mypy src
```

## Contribution expectations

- Keep changes small, explicit, and inspectable.
- Update documentation when behavior or decisions change.
- Preserve the learning-first architecture and dependency policy.
- Prefer tests and numerical checks before broad claims of correctness.

## Adding an ADR

1. Copy the structure documented in `docs/adr/README.md`.
2. Use the next sequential ADR number.
3. Record context, alternatives, decision, consequences, risks, evidence, and revisit conditions.
4. Link affected work packages.

## Adding a work package

1. Start from `docs/work-packages/template.md`.
2. Fill every required field.
3. Keep status honest: `Proposed`, `Ready`, `In Progress`, `Blocked`, `In Review`, or `Complete`.
4. Include tests, experiments, evidence, and guide updates in the definition of done.

## Evidence requirements

Important claims should be backed by one or more of:

- passing tests
- numerical checks
- exact commands used
- configuration files
- dataset checksums
- checkpoint metadata
- experiment records
- generated samples
- documented limitations

## Coding notes

- Every Python module needs a module docstring.
- Every function needs a docstring and type hints.
- Library code should use `logging`; user-facing CLI commands may print.
- Keep the package importable without PyTorch installed.

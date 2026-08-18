# Contributing

## Principles

- Evidence precedes assertion
- Make small, cohesive changes
- Keep docs synchronized with implementation
- Do not claim tests passed unless executed

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Commands

```bash
pytest tests/unit
python -m tiny_llm doctor
```

## Process requirements

- For architecture changes: add/update ADR
- For milestone work: add/update work package
- For experiments: record evidence under `docs/reports/`

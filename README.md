# creating-models-from-scratch

Learning-first project to build a tiny decoder-only language model from first principles.

## Current milestone

This repository now contains:

- A project charter and architecture/design documentation
- ADR and work-package systems
- Initial roadmap (WP-000 to WP-014)
- A minimal headless CLI baseline
- A first environment qualification command (`python -m tiny_llm doctor`)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m tiny_llm doctor
pytest tests/unit
```

## Intent

This project is educational. It does **not** use pretrained weights or imported Transformer model implementations.

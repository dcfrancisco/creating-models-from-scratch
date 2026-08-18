# User Guide

## Understand what the project does
This project teaches how to build a tiny decoder-only language model from scratch, step by step, with evidence.

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Verify the environment
```bash
python -m tiny_llm doctor
```

## Obtain or prepare the dataset
Pending WP-002. See `docs/governance/dataset-card.md`.

## Inspect the dataset
Pending WP-002 command: `python -m tiny_llm data inspect --config <path>`.

## Train the smallest model
Pending WP-004/WP-005.

## Train the tiny Transformer
Pending WP-010.

## Monitor a run
Current baseline:
```bash
top
free -h
df -h
```

## Stop a run safely
Pending WP-011.

## Resume from a checkpoint
Pending WP-011.

## Evaluate a model
Pending WP-012 command: `python -m tiny_llm evaluate --checkpoint <path>`.

## Generate text
Pending WP-012/WP-010 command: `python -m tiny_llm generate --checkpoint <path> --prompt "..."`.

## Read experiment output
Pending WP-012 evidence files under `artifacts/runs/` + `docs/reports/`.

## Interpret loss and perplexity
Pending WP-012 with caveats on tiny-data evaluations.

## Locate logs and checkpoints
Runtime outputs are expected under `artifacts/`.

## Remove old local artifacts safely
Delete run/checkpoint directories under `artifacts/` after confirming they are not needed.

## Understand current limitations
See `docs/governance/limitations.md` and `docs/governance/responsible-use.md`.

# User Guide

This project is meant to be used from a terminal or SSH session.

## What the project does

`tiny_llm` helps you inspect a text dataset, build a character tokenizer, train small baseline models, evaluate checkpoints, and generate text while keeping the process explicit and inspectable.

## Install

```bash
python3 -m pip install -e ".[dev]"
```

## Verify the environment

```bash
python3 -m tiny_llm doctor
```

## Obtain or prepare the dataset

For smoke testing, the repository includes `tests/fixtures/tiny_corpus.txt`. For larger work, place a clearly licensed text file under `data/` and point a config file to it.

## Inspect the dataset

```bash
python3 -m tiny_llm data inspect --config configs/smoke/bigram.toml
```

## Train the smallest model

```bash
python3 -m tiny_llm train --config configs/smoke/bigram.toml
```

## Train the tiny Transformer

The Transformer configuration is scaffolded, but the full Transformer implementation is still planned work. Use the smoke bigram path for the currently working baseline.

## Monitor a run

Training output is emitted through terminal-friendly logging. Redirect output safely if needed:

```bash
python3 -m tiny_llm train --config configs/smoke/bigram.toml | tee run.log
```

## Stop a run safely

Use `Ctrl+C` or terminate the process cleanly. Do not delete a checkpoint directory while a save is in progress.

## Resume from a checkpoint

Resume support is part of planned checkpoint lifecycle work. Current checkpoints are self-describing and can be inspected, evaluated, and used for generation.

## Evaluate a model

```bash
python3 -m tiny_llm evaluate --checkpoint artifacts/smoke/bigram/checkpoint-step-000010
```

## Generate text

```bash
python3 -m tiny_llm generate --checkpoint artifacts/smoke/bigram/checkpoint-step-000010 --prompt "Alice" --temperature 0.8 --top-k 5 --length 80
```

## Read experiment output

Experiment records are stored under `artifacts/experiments/` when experiment helpers are used.

## Interpret loss and perplexity

- lower loss is better than higher loss on the same dataset split
- perplexity is `exp(loss)`
- neither metric alone proves useful language understanding

## Locate logs and checkpoints

Check the configured `output_dir`, usually under `artifacts/`.

## Remove old local artifacts safely

Delete only generated files under `artifacts/`, `logs/`, or other ignored local directories after confirming you no longer need the evidence.

## Understand current limitations

See `docs/governance/limitations.md` and `docs/governance/responsible-use.md`.

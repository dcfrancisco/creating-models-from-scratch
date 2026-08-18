# creating-models-from-scratch

`tiny_llm` is a learning-first project for building a tiny decoder-only language model from scratch. The goal is not to ship a production LLM; the goal is to understand the full lifecycle: dataset inspection, tokenization, batching, baseline modeling, training, checkpointing, evaluation, generation, and evidence-backed experimentation.

## What this project is

This repository teaches how a decoder-only language model is constructed from first principles. It starts with the smallest useful components, validates them with tests and documentation, and incrementally grows toward a tiny Transformer.

## Target hardware

The primary target environment is a headless Linux machine similar to:

- AMD Phenom II X6
- 16 GB RAM
- CPU-first execution
- No GUI required
- No AVX assumed
- SSH and terminal driven workflow

The project is designed to remain usable on legacy CPUs. NumPy is the default required backend. PyTorch is optional and treated as a compatibility-gated backend rather than a mandatory assumption.

## What “from scratch” means here

From scratch means:

- no pretrained weights
- no imported Transformer architecture
- no trainer framework that hides the learning mechanics
- no external inference API
- no copying a complete tutorial without reconstruction and explanation

Allowed foundations include the Python standard library, NumPy, and optionally PyTorch tensors/autograd after compatibility is verified.

## Status

**Status: early development.**

This repository currently contains the project skeleton, engineering baseline, character tokenizer, data utilities, count-based bigram baseline, CLI, and supporting documentation. The tiny Transformer remains planned work.

## Quick start

### 1. Install the package

```bash
python3 -m pip install -e ".[dev]"
```

### 2. Verify the environment

```bash
python3 -m tiny_llm doctor
```

### 3. Inspect the tiny fixture dataset

```bash
python3 -m tiny_llm data inspect --config configs/smoke/bigram.toml
```

### 4. Build the character tokenizer

```bash
python3 -m tiny_llm tokenizer build --config configs/smoke/bigram.toml
```

### 5. Run the smoke baseline

```bash
python3 -m tiny_llm train --config configs/smoke/bigram.toml
```

### 6. Inspect a checkpoint

```bash
python3 -m tiny_llm checkpoint inspect --checkpoint artifacts/smoke/bigram/checkpoint-step-000010
```

### 7. Evaluate or generate from a checkpoint

```bash
python3 -m tiny_llm evaluate --checkpoint artifacts/smoke/bigram/checkpoint-step-000010
python3 -m tiny_llm generate --checkpoint artifacts/smoke/bigram/checkpoint-step-000010 --prompt "Alice" --temperature 0.8 --top-k 5 --length 80
```

## Project structure

```text
configs/     runnable smoke and experiment configurations
src/         tiny_llm package
scripts/     operational helper scripts
tests/       unit, numerical, and integration tests
docs/        architecture, ADRs, guides, governance, and reports
data/        dataset guidance and local data placement
artifacts/   generated outputs kept outside Git history by default
```

## Documentation map

Start with:

- [`docs/project-charter.md`](docs/project-charter.md)
- [`docs/roadmap.md`](docs/roadmap.md)
- [`docs/architecture/README.md`](docs/architecture/README.md)
- [`docs/guides/user-guide.md`](docs/guides/user-guide.md)
- [`docs/guides/operations-guide.md`](docs/guides/operations-guide.md)
- [`docs/guides/developer-guide.md`](docs/guides/developer-guide.md)

## Current emphasis

The current milestone focuses on the learning and engineering baseline:

- repository and documentation skeleton
- hardware qualification procedure
- headless CLI
- reproducible configuration loading
- character tokenizer
- tiny committed fixture data
- count-based bigram baseline
- checkpoint, evaluation, and generation workflow

For the planned execution order, see [`docs/roadmap.md`](docs/roadmap.md) and the work packages under [`docs/work-packages/`](docs/work-packages/).

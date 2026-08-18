# Project Charter

## Purpose

Build a small decoder-only language model from first principles in a way that teaches how modern autoregressive language models are assembled, trained, evaluated, and operated.

## Learning goals

- Understand the data → tokenizer → model → loss → optimizer → checkpoint → generation lifecycle.
- Explain each architectural component in plain language and mathematical language.
- Validate correctness through tests, numerical checks, reproducible configurations, and experiment evidence.
- Learn the operational constraints of CPU-first, headless model development on legacy hardware.

## Intended audience

- The repository owner, an experienced software engineer learning LLM internals.
- Contributors who want an explicit, inspectable educational codebase rather than a framework-heavy implementation.
- Readers who prefer command-line workflows and documentation-backed learning.

## Scope

This project covers environment qualification, dataset inspection and provenance tracking, character-level tokenization, count-based and trainable bigram baselines, tiny decoder-only Transformer components, checkpointing, evaluation, text generation, experiment evidence, and supporting guides.

## Non-goals

The first milestone does **not** aim to compete with commercial LLMs, train billions of parameters, deploy production inference services, implement distributed training, support multimodal input, build RAG systems or agents, perform alignment training or RLHF, or provide a GUI.

## Meaning of “from scratch”

From scratch means no pretrained weights, no imported Transformer block, no external inference API, and no hidden trainer framework. Foundational numerical libraries are allowed, but the concepts being learned must be implemented explicitly in repository code.

## Target hardware

Primary target:

- AMD Phenom II X6-class CPU
- 16 GB RAM
- headless Linux
- SSH access only
- CPU-first execution
- no AVX assumption

## Engineering principles

- Evidence precedes assertion.
- Prefer explicit code over clever abstractions.
- Keep the repository fully usable from a terminal.
- Separate model, data, training, evaluation, checkpoint, and CLI concerns.
- Minimize dependencies and document why each exists.
- Keep smoke workflows fast enough for routine development.

## Evidence requirements

Important claims should be backed by tests, numerical checks, configuration capture, dataset checksums, checkpoint metadata, experiment records, exact commands, and documented limitations.

## Initial success criteria

- Repository contains the full documentation and project structure.
- `python -m tiny_llm doctor` runs on a headless machine.
- Character tokenization works end-to-end.
- Dataset inspection, baseline training, checkpoint saving, evaluation, and generation all function in smoke form.
- Tests pass for the engineering baseline.

## Constraints

- Python >= 3.9
- headless operation only
- CPU-first execution
- optional PyTorch, never assumed
- no unsafe system changes required
- no long training run started automatically

## Risks

- PyTorch may be incompatible with the legacy CPU.
- Small datasets can encourage memorization and misleadingly good samples.
- Educational clarity can degrade if abstractions grow too quickly.
- Performance constraints may limit model size and iteration speed.

## Long-term direction

Progress from baseline data and tokenization work to trainable bigram models, then to a tiny Transformer, then to controlled evaluation and optimization. Optional future work includes subword tokenization and running larger experiments on alternative hardware without changing the conceptual architecture.

## Definition of project completion

The first milestone is complete when the repository can reproducibly inspect a legal dataset, build a tokenizer, train and evaluate a tiny model, save and restore checkpoints, generate text, and explain each step with honest evidence and documentation.

# Project Charter

## Purpose
Build a tiny decoder-only language model from first principles for learning.

## Learning goals
- Understand each core LM component by implementing it progressively.
- Validate each stage using tests and experiment evidence.

## Intended audience
Hands-on learners using CPU-first, headless Linux workflows.

## Scope
Progressive vertical slices from dataset + tokenizer through tiny Transformer.

## Non-goals (initial milestone)
- Competing with production/commercial LLMs
- Billion-parameter training
- Production serving, RAG, agents, RLHF, multimodal, GUI

## Meaning of “from scratch”
No pretrained weights or imported Transformer model blocks.

## Target hardware
Primary target: AMD Phenom II X6, 16 GB RAM, headless Linux, CPU-first.

## Engineering principles
- Evidence precedes assertion
- Small cohesive changes
- Reproducibility and explicit configuration
- Educational clarity over abstraction

## Evidence requirements
Claims require tests, numerical checks, measured outputs, and recorded commands.

## Initial success criteria
- Working project skeleton and headless CLI
- Hardware qualification process and report format
- ADR and work-package governance in place

## Constraints
- Legacy CPU compatibility
- Limited compute and storage
- No GUI assumptions

## Risks
- PyTorch wheel incompatibility on legacy CPU
- Slow training and tight memory budgets

## Long-term direction
From count-based baseline to tiny decoder-only Transformer with experiments.

## Definition of completion
Documented, tested, reproducible end-to-end tiny model workflow with evidence.

# Evidence Model

This project follows the rule: **evidence precedes assertion**.

## Evidence by component

### Dataset pipeline

Evidence includes checksum calculation, size reporting, sample output, empty-input handling, and reproducible split behavior.

### Tokenizer

Evidence includes deterministic vocabulary construction, encode/decode round trips, save/load fidelity, and unknown-character behavior.

### Batch creation

Evidence includes tensor shapes, index bounds, reproducibility under fixed seeds, and correct target shifting.

### Bigram baseline

Evidence includes probability normalization, finite loss, deterministic greedy generation, and integration from text → tokens → model → samples.

### Transformer components

Evidence will include tensor-shape tests, masking tests, numerical toy examples, and gradient-flow checks where autograd is available.

### Checkpointing

Evidence includes metadata presence, model-array serialization, compatibility checks, and restore-to-evaluate or restore-to-generate tests.

### Evaluation

Evidence includes loss computation, perplexity derivation, and clear explanation of what the metrics do and do not mean.

### CLI

Evidence includes successful command execution on a headless shell, helpful error messages, and documented copyable commands.

## Evidence record types

- unit tests
- numerical tests
- integration tests
- configuration files
- checkpoint metadata
- experiment JSON
- experiment markdown summary
- exact commands in reports or guides

## Evidence quality bar

A component is not complete just because code exists. It should also be testable, documented, and backed by observable output.

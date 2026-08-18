# Component Model

## Data pipeline

Loads text, validates that it is non-empty, computes checksums, splits train/validation text, and creates context-window batches.

## Tokenizer

Builds a stable character vocabulary, maps text to token IDs, decodes IDs back to text, and persists vocabulary metadata.

## Model

### Embedding
Maps token IDs to dense vectors of shape `(B, T, C)` in later work packages.

### PositionalEncoding
Injects order information so the model can distinguish sequences with the same tokens in different positions.

### CausalSelfAttention
Computes attention weights while forbidding attention to future positions.

### MultiHeadAttention
Runs several attention heads in parallel and combines their outputs.

### FeedForward
Applies a position-wise nonlinear transformation.

### TransformerBlock
Composes attention, feed-forward, normalization, and residual paths.

### DecoderLM
Produces logits over the next token for each position.

## Trainer

Owns the training loop, loss reporting, validation cadence, checkpoint saves, and experiment bookkeeping.

## Evaluator

Loads checkpoints, recomputes loss on validation data, and derives metrics such as perplexity.

## Generator

Encodes a prompt, samples from model outputs, and decodes generated token IDs to text.

## CheckpointManager

Writes and reads model state, configuration, identity metadata, and metrics in a compatibility-checked format.

## CLI

Provides the headless user interface for doctor, data inspection, tokenizer building, training, evaluation, generation, and checkpoint inspection.

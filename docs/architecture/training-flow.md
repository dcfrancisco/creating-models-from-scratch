# Training Flow

This document uses the notation:

- `B`: batch size
- `T`: sequence length or context length
- `C`: embedding dimension
- `V`: vocabulary size
- `L`: number of Transformer layers

## Baseline flow

For the count-based bigram baseline, the smallest useful input is a sequence of token IDs:

- token sequence: shape `(N,)`
- current token: scalar integer
- next-token distribution: shape `(V,)`

## Transformer-oriented flow

Later work packages will use the following training path:

1. **Batch creation**
   - input IDs `x`: shape `(B, T)`
   - target IDs `y`: shape `(B, T)`
2. **Embedding lookup**
   - token embeddings: shape `(B, T, C)`
3. **Positional representation**
   - positional tensor: shape `(1, T, C)` or `(T, C)`
   - combined hidden state: shape `(B, T, C)`
4. **Transformer stack**
   - each of `L` blocks preserves shape `(B, T, C)`
5. **Output projection**
   - logits: shape `(B, T, V)`
6. **Loss**
   - flatten logits to `(B*T, V)`
   - flatten targets to `(B*T,)`
   - cross-entropy returns a scalar loss
7. **Optimization**
   - backpropagate gradients
   - update parameters
8. **Evaluation interval**
   - run the same forward path on held-out batches without parameter updates
9. **Checkpoint interval**
   - persist parameters, configuration, identity, and metrics

## Educational emphasis

Every stage should be explainable at both the tensor-shape level and the probabilistic level: the model predicts the next token distribution conditioned on the prefix seen so far.

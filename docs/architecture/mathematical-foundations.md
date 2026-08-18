# Mathematical Foundations

This project develops the language model progressively. Each equation below includes symbol definitions, expected tensor shapes, a small example, and an implementation anchor.

## 1. Next-token probability distribution

We model the probability of the next token `x_{t+1}` given a prefix `x_{1:t}` as `P(x_{t+1} | x_{1:t})`.

- symbols: `x_t` is the token at position `t`; `V` is vocabulary size.
- shapes: baseline next-token distribution has shape `(V,)`.
- example: after `'A'`, the model may assign `P('l'|'A') = 0.30`.
- implementation: `src/tiny_llm/model.py::BigramLM.forward`.
- test/evidence: `tests/unit/test_model.py`.

## 2. Negative log likelihood

For an observed next token `y`, the loss contribution is `-log P(y | x)`.

- shapes: selected probability is scalar; loss contribution is scalar.
- example: if `P(y|x)=0.25`, loss is about `1.386`.
- implementation: `src/tiny_llm/model.py::BigramLM.loss`.

## 3. Cross-entropy loss

For vocabulary classification, `L = -Σ y_i log p_i`. With a one-hot target, this is the negative log probability of the correct token.

- shapes: prediction `(V,)`, one-hot target `(V,)`, scalar loss.
- example: target class `1` and `p=[0.1, 0.8, 0.1]` gives `-log(0.8)`.
- evidence: `tests/numerical/test_numerical.py::test_cross_entropy`.

## 4. Embedding lookup

Later work packages will map token IDs through an embedding matrix `E` with shape `(V, C)`, producing `(B, T, C)` output.

- symbols: `C` is embedding dimension.
- example: token ID `2` retrieves row `E[2]`.
- implementation anchor: planned in `WP-006` and `WP-010`.

## 5. Positional information

Token identity alone does not encode order, so later work will use `H0 = E[x] + P`.

- shapes: token embeddings `(B, T, C)`, positional representation `(1, T, C)`, combined `(B, T, C)`.
- example: the same character at positions `0` and `5` gains different positional information.

## 6. Linear projections

Attention begins with `Q = XW_Q`, `K = XW_K`, `V = XW_V`.

- symbols: `X` hidden state, `d_h` head dimension.
- shapes: `X` `(B, T, C)`, each projection `(B, T, d_h)`.
- example: if `C=8` and `H=2`, one head can use `d_h=4`.

## 7. Attention scores

Unnormalized scores are `S = QK^T`.

- shapes: `Q` `(B, T, d_h)`, `K^T` `(B, d_h, T)`, scores `(B, T, T)`.
- example: position `3` produces one score for each earlier position.

## 8. Scaling

Scaled dot-product attention uses `S / sqrt(d_h)` to control score magnitude.

- reason: without scaling, softmax can become too sharp in larger dimensions.

## 9. Causal masking

Future positions are hidden by forcing masked scores to `-∞` when `j > i`.

- shapes: mask `(T, T)` or broadcastable to `(B, T, T)`.
- evidence anchor: planned masking tests in `WP-007`.

## 10. Softmax

Attention probabilities are `A = softmax(S_masked)`.

- shapes: attention weights `(B, T, T)`.
- property: each row sums to `1`.
- evidence: `tests/numerical/test_numerical.py::test_probability_normalization`.

## 11. Weighted value aggregation

Attention output is `O = AV`.

- shapes: `A` `(B, T, T)`, `V` `(B, T, d_h)`, output `(B, T, d_h)`.
- example: each position receives a weighted mixture of earlier values.

## 12. Multiple heads

Multi-head attention concatenates head outputs and applies an output projection: `Concat(O1...OH)W_O`.

- shapes: per-head `(B, T, d_h)`, concatenated `(B, T, C)`, projected `(B, T, C)`.

## 13. Feed-forward network

A position-wise FFN applies `W2 σ(W1x + b1) + b2`.

- shapes: input `(B, T, C)`, hidden width often `(B, T, 4C)`, output `(B, T, C)`.

## 14. Activation function

ReLU or GELU introduces nonlinearity. Early educational implementations may start simple.

## 15. Residual connections

Residual updates use `X' = X + SubLayer(X)`.

- shapes: both tensors must match, typically `(B, T, C)`.

## 16. Layer normalization

Layer norm uses `γ * (x-μ)/sqrt(σ²+ε) + β` across the channel dimension.

- shapes: input and output both `(B, T, C)`.

## 17. Gradient descent and autograd

Parameter updates follow `θ ← θ - η ∇θ L`.

- symbols: `η` learning rate, `θ` parameters.
- note: if PyTorch is used later, autograd computes gradients but the architecture remains repository code.

## 18. Temperature, greedy decoding, multinomial, and top-k

Sampling rescales logits or log-probabilities by temperature `τ`, uses `argmax` for greedy decoding, categorical draws for multinomial sampling, and optionally keeps only the highest-probability `k` tokens before renormalizing.

- implementation: `src/tiny_llm/generate.py::sample_next`.
- evidence: `tests/numerical/test_numerical.py::test_sample_next`.

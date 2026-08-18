# Mathematical Foundations

Notation: `B` batch, `T` sequence length, `C` embedding size, `H` heads, `d_h=C/H`, `V` vocabulary, `L` blocks.

Each equation will be tied to implementation and tests as work packages land.

## Probability over next token
`p(x_t | x_{<t}) = softmax(z_t)` where `z_t in R^V`.

## Negative log-likelihood / cross-entropy
`L = -log p(y_t | x_{<t})` and sequence loss is mean over predicted positions.

## Embedding lookup
`E[token_id] -> R^C`, producing `[B,T,C]`.

## Positional information
Add position embedding `P[pos]` (or another positional map) to token embeddings.

## Linear projections
`Q = XW_Q`, `K = XW_K`, `V = XW_V`.

## Attention scores
`S = QK^T` with shape `[B,H,T,T]`.

## Scaling
`S_scaled = S / sqrt(d_h)`.

## Causal masking
`S_masked = S_scaled + M`, where `M_{i,j}=-inf` for `j>i`.

## Softmax
`A = softmax(S_masked, dim=-1)`; each row sums to ~1.

## Weighted value aggregation
`O = AV`.

## Multi-head combination
Concatenate head outputs then output projection.

## Feed-forward network
`FFN(x) = W2 * act(W1x + b1) + b2`.

## Residual and normalization
`x <- x + sublayer(x)` and layer normalization around sublayers.

## Optimization
Gradient descent uses automatic differentiation to update parameters.

## Parameter updates
`theta <- theta - lr * grad(theta)` (optimizer-specific variant in practice).

## Sampling controls
- Temperature: `softmax(logits / temp)`
- Greedy: `argmax`
- Multinomial: categorical draw
- Top-k: truncate to top-k logits before sampling

## Links to implementation and tests
- Current implementation: environment qualification CLI (`src/tiny_llm/doctor.py`)
- Planned mapping: WP-004 through WP-010
- Planned numerical tests: `tests/numerical/`

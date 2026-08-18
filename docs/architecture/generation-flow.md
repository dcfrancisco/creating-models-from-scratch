# Generation Flow

Generation is autoregressive: the model repeatedly predicts one next-token distribution conditioned on the current prompt or already generated prefix.

## Steps

1. **Prompt encoding**
   - input text becomes token IDs, usually shape `(T,)` for the baseline or `(1, T)` in batched form.
2. **Model forward**
   - the model produces logits or log-probabilities over `V` next-token candidates.
3. **Sampling**
   - optionally scale by temperature.
   - optionally restrict to top-`k` tokens.
   - choose the next token greedily or by multinomial sampling.
4. **Append token**
   - add the chosen token ID to the running sequence.
5. **Decode**
   - map token IDs back to text.

## Baseline shape intuition

For the current bigram baseline, only the most recent token is required:

- current token ID: scalar
- returned log-probabilities: `(V,)`
- sampled next token ID: scalar

## Future Transformer shape intuition

A decoder-only Transformer can accept `(1, T)` input IDs, produce logits `(1, T, V)`, and sample from the final time step `logits[:, -1, :]` of shape `(1, V)`.

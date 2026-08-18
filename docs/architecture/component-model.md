# Component Model

- Dataset loader and splitter
- Character tokenizer (`str <-> ids`)
- Batch generator (`[B,T] -> x,y`)
- Model components (embeddings, position, attention, FFN, norm, residual)
- Trainer and evaluator
- Checkpoint manager
- Generator (greedy/sampling)

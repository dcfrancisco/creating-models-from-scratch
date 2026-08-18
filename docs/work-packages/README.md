# Work Packages

Work packages define bounded units of learning, implementation, testing, and evidence collection.

| ID | Title | Status | Description |
| --- | --- | --- | --- |
| WP-000 | Hardware qualification | Ready | Establish the exact capabilities and limits of the target CPU-first environment. |
| WP-001 | Project skeleton and engineering baseline | Ready | Create the package layout, CLI, tests, configuration system, and reproducible developer baseline. |
| WP-002 | Dataset acquisition and inspection | Proposed | Select a legal small corpus, record provenance, and inspect its properties. |
| WP-003 | Character tokenizer | Proposed | Build a deterministic character-level tokenizer with persistence and tests. |
| WP-004 | Count-based baseline | Proposed | Implement the smallest next-token baseline to establish the full path to generation. |
| WP-005 | Trainable bigram model | Proposed | Introduce the first trainable neural model and compare it with counts. |
| WP-006 | Embeddings and position | Proposed | Add token embeddings and positional information. |
| WP-007 | Single-head causal self-attention | Proposed | Implement explicit causal attention with shape and masking evidence. |
| WP-008 | Multi-head attention | Proposed | Expand attention into multiple heads and combine them. |
| WP-009 | FFN, normalization, and residual | Proposed | Complete the Transformer block internals. |
| WP-010 | Decoder-only Transformer | Proposed | Assemble and smoke-train the tiny decoder-only model. |
| WP-011 | Checkpoint and recovery lifecycle | Proposed | Make checkpoint save/resume compatibility explicit and testable. |
| WP-012 | Evaluation and comparative experiments | Proposed | Compare baseline, bigram, and Transformer behavior with evidence. |
| WP-013 | Profiling and CPU optimization | Proposed | Measure performance and optimize carefully for constrained CPUs. |
| WP-014 | Optional subword tokenization | Proposed | Explore subword tokenization only after the character baseline is understood. |

# Roadmap

The roadmap is organized as evidence-backed work packages. All work packages are currently in the planning state for the broader project, with WP-000 and WP-001 immediately executable.

| ID | Title | Status | Description | Dependencies |
| --- | --- | --- | --- | --- |
| WP-000 | Repository and hardware qualification | Proposed | Qualify CPU-first headless environment and decide initial backend. | None |
| WP-001 | Project skeleton and engineering baseline | Proposed | Create package, CLI, tests, configs, and reproducible developer workflow. | WP-000 |
| WP-002 | Dataset acquisition and inspection | Proposed | Establish legal dataset workflow, checksum tracking, and inspection utilities. | WP-001 |
| WP-003 | Character-level tokenizer | Proposed | Build deterministic character vocabulary, encode/decode, and tokenizer persistence. | WP-002 |
| WP-004 | Count-based baseline | Proposed | Implement the smallest next-token model and end-to-end baseline generation. | WP-002, WP-003 |
| WP-005 | Trainable bigram model | Proposed | Introduce the first trainable neural language model and compare against counts. | WP-004 |
| WP-006 | Embeddings and position | Proposed | Add token embeddings and positional representation. | WP-005 |
| WP-007 | Single-head causal self-attention | Proposed | Implement explicit causal attention with tests and numerical checks. | WP-006 |
| WP-008 | Multi-head attention | Proposed | Expand single-head attention into multi-head attention. | WP-007 |
| WP-009 | FFN, normalization, residual | Proposed | Implement the remaining Transformer block components. | WP-008 |
| WP-010 | Decoder-only Transformer | Proposed | Assemble the complete tiny decoder-only model. | WP-009 |
| WP-011 | Checkpoint and recovery | Proposed | Add resume-compatible checkpoint lifecycle and recovery validation. | WP-010 |
| WP-012 | Evaluation experiments | Proposed | Compare baseline, bigram, and Transformer runs with reproducible evidence. | WP-011 |
| WP-013 | Profiling and optimization | Proposed | Measure CPU performance and optimize without sacrificing clarity. | WP-012 |
| WP-014 | Optional subword tokenization | Proposed | Explore subword tokenization after the character baseline is understood. | WP-012 |

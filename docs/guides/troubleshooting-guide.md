# Troubleshooting Guide

## NaN loss

- verify probability normalization
- inspect for empty datasets or malformed token IDs
- reduce temperature during generation if outputs are unstable
- confirm no divide-by-zero path exists in custom math

## Out of memory

- reduce batch size
- reduce context length
- use the NumPy baseline first
- close unrelated processes on the target machine

## Checkpoint mismatch

- inspect `metadata.json`
- confirm dataset checksum and vocabulary identity
- ensure the checkpoint matches the expected model type and config

## Slow training

- use smoke configs first
- reduce model size
- reduce checkpoint frequency
- verify thread count and BLAS behavior
- run hardware qualification before blaming the model code

## Dependency issues

- rerun `python3 -m tiny_llm doctor`
- confirm NumPy imports cleanly
- treat PyTorch as optional and compatibility-gated
- reinstall dev dependencies if test tools are missing

# Reproducibility Guide

## Environment setup
Use a virtual environment and record Python/platform versions with `python -m tiny_llm doctor`.

## Dependency locking
Pin versions for published experiments (strategy finalization pending WP-008).

## Dataset checksums
Record dataset hashes in dataset/evidence reports.

## Random seeds
Set and record seeds in configs and experiment records.

## Backend differences
Document NumPy vs PyTorch backend used for each run.

## Floating-point limitations
Do not claim bit-for-bit equivalence across platforms.

## Exact training commands
Record exact command line and config path in each experiment record.

## Configuration capture
Store full resolved config alongside run artifacts.

## Artifact naming
Use run IDs and timestamps (pending implementation).

## Checkpoint identity
Include schema version, model config, optimizer state, seed, and dataset/vocab identities.

## Git state
Record commit hash and dirty-tree status.

## Hardware recording
Record CPU, RAM, swap, storage summaries.

## Expected nondeterminism
Thread scheduling, BLAS behavior, and floating-point ordering can vary.

## Reproducing published results
Replay the same config, seed, dataset checksum, software versions, and backend.

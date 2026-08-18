# Reproducibility Guide

## Environment setup

Use a documented Python version and install the package in editable mode.

## Dependency locking

The project currently uses a minimal dependency set. Record exact installed versions in experiment records and checkpoint metadata.

## Dataset checksums

Always compute and record the SHA-256 checksum of the dataset file used for a run.

## Random seeds

Capture the configured random seed. For deterministic smoke behavior, set the same seed before sampling or batch creation.

## Backend differences

NumPy and PyTorch may differ in numerical behavior, performance, or availability. Do not assume identical results across backends.

## Floating-point limitations

Bit-for-bit reproducibility is not promised across machines or dependency versions. Use tolerant numerical comparisons where appropriate.

## Exact training commands

Record the exact shell command used to start the run.

## Configuration capture

Persist the full config into checkpoints and experiment records.

## Artifact naming

Prefer stable, descriptive paths under `artifacts/` that include the run identity or training step.

## Checkpoint identity

A checkpoint should include schema version, config, dataset checksum, vocabulary identity, metrics, timestamp, and software versions.

## Git state

Record the commit hash and whether the working tree was dirty.

## Hardware recording

Record CPU, RAM, OS, and backend notes, especially for legacy hardware.

## Expected nondeterminism

Small floating-point differences, backend implementation differences, and sampling randomness can all affect results.

## Reproducing published results

To reproduce a published result, use the original config, dataset, checksum, seed, command, and backend, then compare logs, metrics, checkpoints, and generated samples.

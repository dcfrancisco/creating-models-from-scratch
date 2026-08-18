# Experiment Guide

## Goal

Experiments should produce evidence, not just output text.

## Running an experiment

1. Choose a config file.
2. Verify the environment with `python3 -m tiny_llm doctor`.
3. Record the dataset checksum.
4. Run training with exact command capture.
5. Save checkpoints and generated samples.
6. Write machine-readable and human-readable evidence.

## Minimum evidence fields

- experiment identifier
- timestamp
- purpose
- hypothesis
- git commit or note if unavailable
- dirty working tree status
- configuration snapshot
- dataset identity and checksum
- vocabulary identity
- random seed
- backend
- dependency versions
- hardware summary
- parameter count
- start and end time
- training duration
- metrics
- checkpoint path
- generated samples
- errors or warnings
- interpretation
- limitations
- next action

## Evidence file format

- JSON for machine-readable metadata
- Markdown for human-readable narrative

## Practical advice

- Use smoke configs before larger runs.
- Never invent missing values; write `Pending measurement` instead.
- If a run fails, record the failure and suspected cause.

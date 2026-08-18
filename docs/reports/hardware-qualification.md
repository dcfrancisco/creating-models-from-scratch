# Hardware Qualification Report

**Status:** Placeholder. This report must be completed by running `scripts/qualify_hardware.sh` on the actual target machine.

## Purpose

Capture exact hardware and runtime evidence before making backend assumptions.

## Required commands

```bash
bash scripts/qualify_hardware.sh
```

## Required observations

- operating system and kernel
- CPU model and flags
- available RAM and swap
- storage availability
- Python version
- NumPy smoke test
- matrix multiplication timing
- PyTorch import/tensor/autograd result if available
- backend recommendation
- constraints discovered

## Current note

This repository includes the script and report template, but the canonical qualification result should come from the target headless machine rather than from a generic CI runner.

# Operations Guide

## Headless installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Environment activation
`source .venv/bin/activate`

## Dependency verification
```bash
python -m tiny_llm doctor
```

## CPU compatibility verification
Run `doctor` and record results in `docs/reports/hardware-qualification.md`.

## Directory and storage planning
Use `data/` for datasets and `artifacts/` for generated outputs. Keep large files out of Git.

## Dataset preparation
Pending WP-002.

## Starting training
Pending WP-005/WP-010 commands.

## Running training after SSH disconnection
Use `tmux`, `screen`, or `nohup` (no root required).

## Process monitoring
`ps`, `top`, `htop` (if installed).

## CPU monitoring
`top`, `mpstat` (if available).

## Memory and swap monitoring
`free -h`, `vmstat 1`.

## Disk monitoring
`df -h`, `du -sh artifacts/*`.

## Log inspection
`tail -f artifacts/logs/<run>.log` (pending log format implementation).

## Checkpoint rotation
Pending WP-011 policy.

## Safe interruption
Use SIGINT and wait for graceful checkpoint (pending implementation details).

## Resume procedure
Pending WP-011.

## Backup and restore
Copy `artifacts/checkpoints/` + config + vocab metadata (pending format finalization).

## Reproducing an experiment
Follow `docs/guides/reproducibility-guide.md`.

## Handling OOM failures
Reduce batch size/context length/model width in config (pending config implementation).

## Handling NaN/inf loss
Pending WP-012 troubleshooting checks.

## Handling corrupted checkpoints
Pending WP-011 compatibility and checksum checks.

## Handling incompatible dependencies
Default to NumPy-first backend and record evidence.

## Diagnosing slow training
Reduce model size, thread count, and checkpoint frequency; profile in WP-013.

## Upgrade procedure
Pin and review dependency updates; rerun `doctor` and unit tests.

## Recovery procedure
Restore from last valid checkpoint and rerun validation.

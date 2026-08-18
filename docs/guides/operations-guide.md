# Operations Guide

## Headless installation

```bash
python3 -m pip install -e ".[dev]"
```

## Environment activation

If using a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e ".[dev]"
```

## Dependency verification

```bash
python3 -m tiny_llm doctor
```

## CPU compatibility verification

Run the hardware qualification script:

```bash
bash scripts/qualify_hardware.sh
```

## Directory and storage planning

- keep datasets under `data/`
- keep generated outputs under `artifacts/`
- monitor free space before long runs

## Dataset preparation

Place a plain text corpus at a configured path and record provenance in the dataset card.

## Starting training

```bash
python3 -m tiny_llm train --config configs/smoke/bigram.toml
```

## Running after SSH disconnection

Use tools such as `tmux`, `screen`, or `nohup` when you need persistence:

```bash
tmux new -s tiny-llm
python3 -m tiny_llm train --config configs/smoke/bigram.toml
```

## Safe monitoring

- `ps -f -u "$USER"`
- `top` or `htop` if available
- `free -h`
- `df -h .`
- `tail -f run.log`

## CPU, memory, swap, and disk monitoring

Monitor CPU and memory pressure during training, especially on legacy hardware. Check swap before assuming a run is safe.

## Checkpoint rotation

Keep only checkpoints that still support a useful comparison or recovery point. Avoid filling the disk with redundant smoke outputs.

## Safe interruption

Stop training cleanly and do not interrupt a checkpoint write if avoidable.

## Resume procedure

Resume support will expand in WP-011. Current checkpoint inspection and evaluation already validate metadata presence.

## Backup and restore

Archive the full checkpoint directory, not just `model.npz`, because `metadata.json` is required for compatibility checks.

## Reproducing an experiment

Reuse the original config, dataset checksum, backend choice, seed, and command line. Record the git state and hardware summary.

## Failure handling

- OOM: reduce batch size or context length.
- NaN/Inf loss: inspect inputs, probabilities, and sampling temperature.
- Corrupted checkpoint: restore from backup or rerun the bounded experiment.
- Incompatible dependencies: prefer the NumPy baseline and document the failure.
- Slow training: use smoke configs first, reduce size, and capture timing evidence before changing architecture.

## Upgrade procedure

Update dependencies deliberately, rerun `doctor`, rerun tests, and record any behavior change.

## Recovery procedure

Return to the last known-good config, rerun the smoke test, and use the reports plus test results to localize the regression.

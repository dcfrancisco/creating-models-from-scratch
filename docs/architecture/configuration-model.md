# Configuration Model

Configuration is stored in TOML files and loaded into dataclasses.

## Top-level object

`Config` contains four sections:

- `data: DataConfig`
- `model: ModelConfig`
- `training: TrainingConfig`
- `generation: GenerationConfig`

## DataConfig

- `dataset_path: str` — input corpus path.
- `tokenizer_type: str` — currently `character`.

## ModelConfig

- `context_length: int`
- `embedding_dim: int`
- `num_heads: int`
- `num_layers: int`
- `dropout: float`

## TrainingConfig

- `random_seed: int`
- `batch_size: int`
- `learning_rate: float`
- `training_steps: int`
- `eval_interval: int`
- `eval_batches: int`
- `checkpoint_interval: int`
- `output_dir: str`
- `numerical_backend: str` (`numpy` or `torch`)
- `num_threads: int`

## GenerationConfig

- `temperature: float`
- `top_k: int`
- `generation_length: int`

## Validation rules

Validation fails early when string paths or identifiers are empty, dimensions or counts are non-positive, dropout is outside `[0, 1)`, backend is not `numpy` or `torch`, `top_k < 0`, or generation temperature is non-positive.

## Operational notes

- Configuration defaults allow minimal smoke execution.
- Files under `configs/smoke/` are intended for quick validation.
- Files under `configs/experiments/` are intended for slower, explicit learning runs.
- The configuration object is saved into checkpoint metadata so a run can be reproduced or rejected as incompatible.

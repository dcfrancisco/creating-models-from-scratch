"""Configuration dataclasses and TOML loading for tiny_llm."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping, TypeVar

try:
    import tomllib
except ImportError:  # pragma: no cover - exercised only on Python < 3.11
    import tomli as tomllib  # type: ignore[no-redef]


@dataclass
class DataConfig:
    """Configuration for dataset loading and tokenization selection."""

    dataset_path: str = "data/corpus.txt"
    tokenizer_type: str = "character"


@dataclass
class ModelConfig:
    """Configuration for model architecture dimensions."""

    context_length: int = 64
    embedding_dim: int = 64
    num_heads: int = 2
    num_layers: int = 2
    dropout: float = 0.0


@dataclass
class TrainingConfig:
    """Configuration for training, evaluation cadence, and output paths."""

    random_seed: int = 42
    batch_size: int = 32
    learning_rate: float = 1e-3
    training_steps: int = 1000
    eval_interval: int = 100
    eval_batches: int = 10
    checkpoint_interval: int = 500
    output_dir: str = "artifacts/runs"
    numerical_backend: str = "numpy"
    num_threads: int = 1


@dataclass
class GenerationConfig:
    """Configuration for text generation and sampling."""

    temperature: float = 1.0
    top_k: int = 0
    generation_length: int = 200


@dataclass
class Config:
    """Top-level configuration container."""

    data: DataConfig = field(default_factory=DataConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)


T = TypeVar("T")


def _update_dataclass(instance: T, values: Mapping[str, Any]) -> T:
    """Update a dataclass instance from a TOML mapping.

    Args:
        instance: Dataclass instance to mutate.
        values: Parsed TOML key/value mapping for the relevant section.

    Returns:
        The updated instance.
    """
    for key, value in values.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    return instance


def config_to_dict(config: Config) -> Dict[str, Any]:
    """Convert a configuration dataclass tree into a serializable dictionary."""
    return asdict(config)


def config_from_dict(data: Mapping[str, Any]) -> Config:
    """Build a Config object from nested dictionaries.

    Args:
        data: Mapping containing optional `data`, `model`, `training`, and
            `generation` sections.

    Returns:
        Populated `Config` object.
    """
    config = Config()
    _update_dataclass(config.data, data.get("data", {}))
    _update_dataclass(config.model, data.get("model", {}))
    _update_dataclass(config.training, data.get("training", {}))
    _update_dataclass(config.generation, data.get("generation", {}))
    return config


def load_config(path: str) -> Config:
    """Load and validate a TOML configuration file.

    Args:
        path: Filesystem path to a TOML file.

    Returns:
        A validated `Config` object.
    """
    config_path = Path(path)
    with config_path.open("rb") as handle:
        parsed = tomllib.load(handle)
    config = config_from_dict(parsed)
    validate_config(config)
    return config


def validate_config(config: Config) -> None:
    """Validate configuration values and raise `ValueError` on invalid input.

    Args:
        config: Parsed configuration object.

    Raises:
        ValueError: If any field value is invalid.
    """
    if not config.data.dataset_path:
        raise ValueError("data.dataset_path must not be empty")
    if config.data.tokenizer_type != "character":
        raise ValueError("data.tokenizer_type must be 'character' in the current milestone")
    if config.model.context_length <= 0:
        raise ValueError("model.context_length must be > 0")
    if config.model.embedding_dim <= 0:
        raise ValueError("model.embedding_dim must be > 0")
    if config.model.num_heads <= 0:
        raise ValueError("model.num_heads must be > 0")
    if config.model.num_layers <= 0:
        raise ValueError("model.num_layers must be > 0")
    if not 0.0 <= config.model.dropout < 1.0:
        raise ValueError("model.dropout must be in [0, 1)")
    if config.training.batch_size <= 0:
        raise ValueError("training.batch_size must be > 0")
    if config.training.learning_rate <= 0:
        raise ValueError("training.learning_rate must be > 0")
    if config.training.training_steps <= 0:
        raise ValueError("training.training_steps must be > 0")
    if config.training.eval_interval <= 0:
        raise ValueError("training.eval_interval must be > 0")
    if config.training.eval_batches <= 0:
        raise ValueError("training.eval_batches must be > 0")
    if config.training.checkpoint_interval <= 0:
        raise ValueError("training.checkpoint_interval must be > 0")
    if not config.training.output_dir:
        raise ValueError("training.output_dir must not be empty")
    if config.training.numerical_backend not in {"numpy", "torch"}:
        raise ValueError("training.numerical_backend must be 'numpy' or 'torch'")
    if config.training.num_threads <= 0:
        raise ValueError("training.num_threads must be > 0")
    if config.generation.temperature <= 0:
        raise ValueError("generation.temperature must be > 0")
    if config.generation.top_k < 0:
        raise ValueError("generation.top_k must be >= 0")
    if config.generation.generation_length < 0:
        raise ValueError("generation.generation_length must be >= 0")

"""Tests for configuration loading and validation."""

from __future__ import annotations

from pathlib import Path

import pytest

from tiny_llm.config import Config, load_config, validate_config


def test_load_default_config(tmp_path: Path) -> None:
    """Loading an empty TOML file should yield default configuration values."""
    config_path = tmp_path / "config.toml"
    config_path.write_text("", encoding="utf-8")
    config = load_config(str(config_path))
    assert config.data.dataset_path == "data/corpus.txt"
    assert config.model.context_length == 64
    assert config.training.numerical_backend == "numpy"


def test_validate_config_valid() -> None:
    """A default configuration should validate successfully."""
    config = Config()
    validate_config(config)


def test_validate_config_invalid_context_length() -> None:
    """A non-positive context length should raise `ValueError`."""
    config = Config()
    config.model.context_length = 0
    with pytest.raises(ValueError):
        validate_config(config)

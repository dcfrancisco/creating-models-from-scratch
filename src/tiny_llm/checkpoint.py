"""Checkpoint save, load, and inspection helpers."""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any, Dict

import numpy as np

from tiny_llm import __version__
from tiny_llm.config import Config, config_to_dict
from tiny_llm.data import compute_checksum
from tiny_llm.utils import ensure_dir, get_timestamp

LOGGER = logging.getLogger(__name__)


def save_checkpoint(model: Any, config: Config, step: int, metrics: Dict[str, Any], path: str) -> str:
    """Save model arrays and self-describing metadata to a checkpoint directory.

    Args:
        model: Model object exposing `transition_counts` and optional `vocab`.
        config: Configuration snapshot.
        step: Training step recorded in metadata.
        metrics: Metrics dictionary to persist.
        path: Checkpoint directory path.

    Returns:
        The checkpoint directory path.
    """
    checkpoint_dir = Path(path)
    ensure_dir(str(checkpoint_dir))
    vocab = list(getattr(model, "vocab", []) or [])
    vocab_identity = (
        hashlib.sha256(json.dumps(vocab, ensure_ascii=False).encode("utf-8")).hexdigest()
        if vocab
        else "unknown"
    )
    metadata = {
        "version": __version__,
        "schema_version": 1,
        "model_type": type(model).__name__,
        "step": step,
        "config": config_to_dict(config),
        "metrics": metrics,
        "timestamp": get_timestamp(),
        "vocab": vocab,
        "vocab_identity": vocab_identity,
        "dataset_checksum": compute_checksum(config.data.dataset_path),
        "software_versions": {
            "numpy": np.__version__,
        },
    }
    (checkpoint_dir / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    np.savez(checkpoint_dir / "model.npz", transition_counts=model.transition_counts)
    LOGGER.info("Saved checkpoint to %s", checkpoint_dir)
    return str(checkpoint_dir)


def load_checkpoint(path: str) -> Dict[str, Any]:
    """Load and minimally validate checkpoint contents.

    Args:
        path: Checkpoint directory path.

    Returns:
        Dictionary with `metadata` and `arrays` keys.
    """
    checkpoint_dir = Path(path)
    metadata_path = checkpoint_dir / "metadata.json"
    arrays_path = checkpoint_dir / "model.npz"
    if not metadata_path.exists() or not arrays_path.exists():
        raise FileNotFoundError("checkpoint must contain metadata.json and model.npz")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    required_keys = {"version", "schema_version", "model_type", "step", "config", "metrics"}
    missing = required_keys.difference(metadata)
    if missing:
        raise ValueError(f"checkpoint metadata missing keys: {sorted(missing)}")
    arrays = np.load(arrays_path, allow_pickle=False)
    return {"metadata": metadata, "arrays": arrays}


def inspect_checkpoint(path: str) -> Dict[str, Any]:
    """Load and return a summarized checkpoint description.

    Args:
        path: Checkpoint directory path.

    Returns:
        Summary dictionary for user-facing display.
    """
    loaded = load_checkpoint(path)
    metadata = loaded["metadata"]
    arrays = loaded["arrays"]
    summary = {
        "path": path,
        "model_type": metadata["model_type"],
        "step": metadata["step"],
        "timestamp": metadata.get("timestamp"),
        "metrics": metadata.get("metrics", {}),
        "array_keys": list(arrays.keys()),
    }
    LOGGER.info("Checkpoint inspection: %s", summary)
    return summary

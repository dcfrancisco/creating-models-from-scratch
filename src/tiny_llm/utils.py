"""Utility helpers for reproducibility, directories, and parameter counting."""

from __future__ import annotations

import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


def set_seed(seed: int) -> None:
    """Set random seeds for Python, NumPy, and torch when available.

    Args:
        seed: Integer random seed used for reproducible smoke experiments.
    """
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:
        pass


def get_timestamp() -> str:
    """Return an ISO 8601 UTC timestamp string."""
    return datetime.now(timezone.utc).isoformat()


def ensure_dir(path: str) -> None:
    """Create a directory path if it does not already exist.

    Args:
        path: Directory path to create.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def count_parameters(model: Any) -> int:
    """Count parameter-like values for NumPy or torch-based models.

    Args:
        model: Model object exposing torch parameters, NumPy arrays, or a
            `transition_counts` matrix.

    Returns:
        Total number of scalar parameter values.
    """
    if hasattr(model, "parameters"):
        try:
            return int(sum(int(parameter.numel()) for parameter in model.parameters()))
        except TypeError:
            pass
    if hasattr(model, "transition_counts"):
        transition_counts = getattr(model, "transition_counts")
        if transition_counts is not None:
            return int(transition_counts.size)
    if isinstance(model, np.ndarray):
        return int(model.size)
    if isinstance(model, (list, tuple)):
        total = 0
        for item in model:
            if isinstance(item, np.ndarray):
                total += int(item.size)
        return total
    return 0

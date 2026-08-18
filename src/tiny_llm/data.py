"""Dataset loading, validation, checksum, splitting, and batching utilities."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path
from typing import Dict, Optional, Sequence, Tuple

import numpy as np

from tiny_llm.config import Config

LOGGER = logging.getLogger(__name__)


def load_text(path: str) -> str:
    """Load a UTF-8 text file and ensure it is non-empty.

    Args:
        path: Text file path.

    Returns:
        File contents as a string.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If the file is empty after reading.
    """
    text = Path(path).read_text(encoding="utf-8")
    if text == "":
        raise ValueError(f"dataset is empty: {path}")
    return text


def compute_checksum(path: str) -> str:
    """Compute the SHA-256 checksum of a file.

    Args:
        path: File path.

    Returns:
        Hex-encoded SHA-256 checksum string.
    """
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def train_val_split(text: str, val_fraction: float = 0.1, seed: int = 42) -> Tuple[str, str]:
    """Split text into train and validation partitions.

    The current baseline uses a deterministic tail split. The `seed` argument is
    retained for API stability and future strategies.

    Args:
        text: Input corpus text.
        val_fraction: Fraction of characters assigned to validation.
        seed: Reserved for future split strategies.

    Returns:
        Tuple of `(train_text, val_text)`.
    """
    del seed
    if not 0.0 < val_fraction < 1.0:
        raise ValueError("val_fraction must be between 0 and 1")
    split_index = max(1, int(len(text) * (1.0 - val_fraction)))
    split_index = min(split_index, len(text) - 1)
    return text[:split_index], text[split_index:]


class CharacterDataset:
    """Create fixed-length next-token training windows from token IDs.

    Args:
        token_ids: Encoded token ID sequence of shape `(N,)`.
        context_length: Number of input tokens per example `T`.
    """

    def __init__(self, token_ids: Sequence[int], context_length: int) -> None:
        self.token_ids = np.asarray(token_ids, dtype=np.int64)
        self.context_length = int(context_length)
        if self.context_length <= 0:
            raise ValueError("context_length must be > 0")
        if self.token_ids.size <= self.context_length:
            raise ValueError("token_ids must be longer than context_length")

    def __len__(self) -> int:
        """Return the number of valid context windows."""
        return int(self.token_ids.size - self.context_length)

    def sample_batch(
        self,
        batch_size: int,
        rng: Optional[np.random.Generator] = None,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Sample a batch of input and target windows.

        Args:
            batch_size: Number of windows `B` to sample.
            rng: Optional NumPy generator for deterministic sampling.

        Returns:
            Tuple `(input_ids, target_ids)` with shapes `(B, T)` and `(B, T)`.
        """
        if batch_size <= 0:
            raise ValueError("batch_size must be > 0")
        max_start = len(self)
        if rng is None:
            starts = np.random.randint(0, max_start, size=batch_size)
        else:
            starts = rng.integers(0, max_start, size=batch_size)
        inputs = np.stack([self.token_ids[start : start + self.context_length] for start in starts])
        targets = np.stack(
            [self.token_ids[start + 1 : start + self.context_length + 1] for start in starts]
        )
        return inputs, targets


def inspect_dataset(config: Config) -> Dict[str, object]:
    """Inspect a dataset configured for the project.

    Args:
        config: Loaded project configuration.

    Returns:
        Dictionary containing dataset metadata for display or logging.
    """
    text = load_text(config.data.dataset_path)
    stats: Dict[str, object] = {
        "path": config.data.dataset_path,
        "length": len(text),
        "unique_chars": len(set(text)),
        "checksum": compute_checksum(config.data.dataset_path),
        "sample": text[:200],
    }
    LOGGER.info("Dataset inspection: %s", stats)
    return stats

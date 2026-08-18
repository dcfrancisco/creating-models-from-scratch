"""Evaluation helpers for checkpointed baseline models."""

from __future__ import annotations

import logging
import math
from typing import Any, Dict, List

from tiny_llm.checkpoint import load_checkpoint
from tiny_llm.config import config_from_dict
from tiny_llm.data import load_text, train_val_split
from tiny_llm.model import BigramLM
from tiny_llm.tokenizer import CharacterTokenizer

LOGGER = logging.getLogger(__name__)


def compute_loss(model: Any, token_ids: List[int]) -> float:
    """Compute scalar loss for a token sequence using a compatible model.

    Args:
        model: Model exposing a `loss` method.
        token_ids: Encoded token IDs.

    Returns:
        Scalar average loss.
    """
    return float(model.loss(token_ids))


def compute_perplexity(loss: float) -> float:
    """Convert average negative log likelihood to perplexity."""
    return float(math.exp(loss))


def run_evaluation(checkpoint_path: str) -> Dict[str, float]:
    """Load a checkpoint and evaluate it on the validation split.

    Args:
        checkpoint_path: Checkpoint directory path.

    Returns:
        Dictionary containing validation loss and perplexity.
    """
    loaded = load_checkpoint(checkpoint_path)
    metadata = loaded["metadata"]
    arrays = loaded["arrays"]
    config = config_from_dict(metadata["config"])
    text = load_text(config.data.dataset_path)
    _, val_text = train_val_split(text, seed=config.training.random_seed)
    tokenizer = CharacterTokenizer(list(metadata.get("vocab", [])))
    model = BigramLM(tokenizer.vocab_size())
    model.transition_counts = arrays["transition_counts"]
    val_ids = tokenizer.encode(val_text)
    loss = compute_loss(model, val_ids)
    perplexity = compute_perplexity(loss)
    result = {"loss": loss, "perplexity": perplexity}
    LOGGER.info("Evaluation result: %s", result)
    return result

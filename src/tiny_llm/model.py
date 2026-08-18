"""Baseline language-model implementations for tiny_llm."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

import numpy as np


class BigramLM:
    """A count-based bigram language model using Laplace-smoothed counts.

    The model predicts the next token from the current token only.

    Args:
        vocab_size: Vocabulary size `V`.
    """

    def __init__(self, vocab_size: int) -> None:
        self.vocab_size = int(vocab_size)
        self.transition_counts = np.ones((self.vocab_size, self.vocab_size), dtype=np.float64)
        self.vocab: Optional[List[str]] = None

    def fit(self, token_ids: List[int]) -> None:
        """Accumulate transition counts from a token sequence.

        Args:
            token_ids: Token sequence of length `N`.
        """
        if len(token_ids) < 2:
            raise ValueError("token_ids must contain at least two tokens")
        self.transition_counts = np.ones((self.vocab_size, self.vocab_size), dtype=np.float64)
        for current_token, next_token in zip(token_ids[:-1], token_ids[1:]):
            self.transition_counts[current_token, next_token] += 1.0

    def forward(self, token_id: int) -> np.ndarray:
        """Return log-probabilities for the next token.

        Args:
            token_id: Current token ID.

        Returns:
            Log-probability vector of shape `(V,)`.
        """
        counts = self.transition_counts[token_id]
        probabilities = counts / counts.sum()
        return np.log(probabilities)

    def loss(self, token_ids: List[int]) -> float:
        """Compute average negative log likelihood over a token sequence.

        Args:
            token_ids: Token sequence of length `N`.

        Returns:
            Scalar average loss.
        """
        if len(token_ids) < 2:
            return 0.0
        losses = []
        for current_token, next_token in zip(token_ids[:-1], token_ids[1:]):
            logprobs = self.forward(current_token)
            losses.append(-float(logprobs[next_token]))
        return float(np.mean(losses))


@dataclass
class TinyTransformer:
    """Placeholder for the tiny decoder-only Transformer planned in WP-010.

    This class documents the intended future implementation point. The current
    engineering baseline focuses on the data pipeline, tokenizer, bigram
    baseline, checkpointing, and CLI.
    """

    note: str = "Transformer implementation planned for WP-010."

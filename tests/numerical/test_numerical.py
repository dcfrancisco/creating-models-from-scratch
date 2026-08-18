"""Numerical tests for probability and sampling helpers."""

from __future__ import annotations

import numpy as np

from tiny_llm.generate import sample_next


def test_probability_normalization() -> None:
    """Softmax probabilities should sum to one."""
    logits = np.array([1.0, 2.0, 3.0])
    shifted = logits - logits.max()
    probabilities = np.exp(shifted) / np.exp(shifted).sum()
    assert np.isclose(probabilities.sum(), 1.0)


def test_cross_entropy() -> None:
    """Manual cross-entropy should match the expected negative log probability."""
    probabilities = np.array([0.1, 0.8, 0.1])
    target_index = 1
    loss = -np.log(probabilities[target_index])
    assert np.isclose(loss, 0.2231435513142097)


def test_sample_next() -> None:
    """Sampled token index should always be in range."""
    logprobs = np.log(np.array([0.2, 0.3, 0.5]))
    token = sample_next(logprobs, temperature=1.0, top_k=0)
    assert token in {0, 1, 2}

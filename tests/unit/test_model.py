"""Tests for the count-based bigram model."""

from __future__ import annotations

import numpy as np

from tiny_llm.model import BigramLM
from tiny_llm.tokenizer import CharacterTokenizer


def test_bigram_fit() -> None:
    """Fitting should create a square transition matrix of shape `(V, V)`."""
    tokenizer = CharacterTokenizer.from_text("hello world")
    token_ids = tokenizer.encode("hello world")
    model = BigramLM(tokenizer.vocab_size())
    model.fit(token_ids)
    assert model.transition_counts.shape == (tokenizer.vocab_size(), tokenizer.vocab_size())


def test_bigram_loss() -> None:
    """Loss should be finite and positive after fitting."""
    tokenizer = CharacterTokenizer.from_text("banana bandana")
    token_ids = tokenizer.encode("banana bandana")
    model = BigramLM(tokenizer.vocab_size())
    model.fit(token_ids)
    loss = model.loss(token_ids)
    assert np.isfinite(loss)
    assert loss > 0.0


def test_bigram_forward_sums_to_one() -> None:
    """Exponentiated forward log-probabilities should sum to one."""
    tokenizer = CharacterTokenizer.from_text("abcd")
    token_ids = tokenizer.encode("abcd")
    model = BigramLM(tokenizer.vocab_size())
    model.fit(token_ids)
    probabilities = np.exp(model.forward(token_ids[0]))
    assert np.isclose(probabilities.sum(), 1.0)

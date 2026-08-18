"""Sampling and text generation utilities for tiny_llm baseline models."""

from __future__ import annotations

import logging
from typing import Any

import numpy as np

from tiny_llm.checkpoint import load_checkpoint
from tiny_llm.model import BigramLM
from tiny_llm.tokenizer import CharacterTokenizer

LOGGER = logging.getLogger(__name__)


def sample_next(logprobs: np.ndarray, temperature: float, top_k: int) -> int:
    """Sample the next token index from log-probabilities.

    Args:
        logprobs: Log-probability vector of shape `(V,)`.
        temperature: Positive sampling temperature.
        top_k: If positive, sample only from the top-k tokens.

    Returns:
        Sampled token index.
    """
    if temperature <= 0.0:
        return int(np.argmax(logprobs))
    scaled = logprobs / temperature
    if top_k > 0 and top_k < scaled.size:
        top_indices = np.argpartition(scaled, -top_k)[-top_k:]
        masked = np.full_like(scaled, -np.inf)
        masked[top_indices] = scaled[top_indices]
        scaled = masked
    shifted = scaled - np.max(scaled)
    probabilities = np.exp(shifted)
    probabilities = probabilities / probabilities.sum()
    return int(np.random.choice(len(probabilities), p=probabilities))


def generate_text(
    model: Any,
    tokenizer: CharacterTokenizer,
    prompt: str,
    length: int,
    temperature: float,
    top_k: int,
) -> str:
    """Generate text autoregressively from a prompt.

    Args:
        model: Model exposing `forward(token_id) -> (V,)` log-probabilities.
        tokenizer: Character tokenizer.
        prompt: Initial text prompt.
        length: Number of new tokens to generate.
        temperature: Sampling temperature.
        top_k: Optional top-k restriction.

    Returns:
        Prompt plus generated continuation.
    """
    generated_ids = tokenizer.encode(prompt)
    if not generated_ids:
        generated_ids = [tokenizer.unk_id]
    for _ in range(length):
        logprobs = model.forward(generated_ids[-1])
        next_token = sample_next(logprobs, temperature=temperature, top_k=top_k)
        generated_ids.append(next_token)
    return tokenizer.decode(generated_ids)


def run_generation(
    checkpoint_path: str,
    prompt: str,
    temperature: float,
    top_k: int,
    length: int,
) -> str:
    """Generate text from a checkpointed baseline model.

    Args:
        checkpoint_path: Checkpoint directory path.
        prompt: Prompt text.
        temperature: Sampling temperature.
        top_k: Optional top-k restriction.
        length: Number of new tokens to generate.

    Returns:
        Generated text string.
    """
    loaded = load_checkpoint(checkpoint_path)
    metadata = loaded["metadata"]
    arrays = loaded["arrays"]
    tokenizer = CharacterTokenizer(list(metadata.get("vocab", [])))
    model = BigramLM(tokenizer.vocab_size())
    model.transition_counts = arrays["transition_counts"]
    text = generate_text(model, tokenizer, prompt, length, temperature, top_k)
    LOGGER.info("Generated text: %s", text)
    return text

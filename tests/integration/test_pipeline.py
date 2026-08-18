"""Integration tests for the baseline dataset-tokenizer-model pipeline."""

from __future__ import annotations

from pathlib import Path

from tiny_llm.data import CharacterDataset, load_text
from tiny_llm.generate import generate_text
from tiny_llm.model import BigramLM
from tiny_llm.tokenizer import CharacterTokenizer
from tiny_llm.utils import set_seed

FIXTURE = Path("tests/fixtures/tiny_corpus.txt")


def test_tokenizer_to_batch() -> None:
    """Fixture text should tokenize and produce `(B, T)` batch tensors."""
    text = load_text(str(FIXTURE))
    tokenizer = CharacterTokenizer.from_text(text)
    token_ids = tokenizer.encode(text)
    dataset = CharacterDataset(token_ids, context_length=8)
    inputs, targets = dataset.sample_batch(batch_size=4)
    assert inputs.shape == (4, 8)
    assert targets.shape == (4, 8)


def test_bigram_train_and_generate() -> None:
    """The full baseline pipeline should train and generate deterministically with a fixed seed."""
    text = load_text(str(FIXTURE))
    tokenizer = CharacterTokenizer.from_text(text)
    token_ids = tokenizer.encode(text)
    model = BigramLM(tokenizer.vocab_size())
    model.fit(token_ids)
    set_seed(123)
    output_a = generate_text(model, tokenizer, prompt="Alice", length=20, temperature=1.0, top_k=2)
    set_seed(123)
    output_b = generate_text(model, tokenizer, prompt="Alice", length=20, temperature=1.0, top_k=2)
    assert output_a == output_b
    assert output_a.startswith("Alice")

"""Tests for dataset loading and splitting."""

from __future__ import annotations

from pathlib import Path

from tiny_llm.data import load_text, train_val_split

FIXTURE = Path("tests/fixtures/tiny_corpus.txt")


def test_load_text() -> None:
    """Fixture text should load successfully."""
    text = load_text(str(FIXTURE))
    assert "Alice" in text


def test_train_val_split() -> None:
    """Split lengths should approximately match the requested fraction."""
    text = load_text(str(FIXTURE))
    train_text, val_text = train_val_split(text, val_fraction=0.2)
    assert len(train_text) + len(val_text) == len(text)
    assert abs(len(val_text) - int(len(text) * 0.2)) <= 1


def test_split_reproducible() -> None:
    """The same seed should return the same split for the current strategy."""
    text = load_text(str(FIXTURE))
    assert train_val_split(text, seed=42) == train_val_split(text, seed=42)

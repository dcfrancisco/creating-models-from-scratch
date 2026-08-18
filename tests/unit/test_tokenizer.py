"""Tests for the character tokenizer."""

from __future__ import annotations

from pathlib import Path

from tiny_llm.tokenizer import CharacterTokenizer, UNK_TOKEN


def test_from_text() -> None:
    """Tokenizer vocabulary should include unique characters and `<UNK>`."""
    tokenizer = CharacterTokenizer.from_text("aba")
    assert tokenizer.vocab[0] == UNK_TOKEN
    assert set(tokenizer.vocab[1:]) == {"a", "b"}


def test_encode_decode_roundtrip() -> None:
    """Known text should round-trip through encode/decode."""
    tokenizer = CharacterTokenizer.from_text("hello world")
    text = "hello"
    assert tokenizer.decode(tokenizer.encode(text)) == text


def test_vocab_size() -> None:
    """Vocabulary size should reflect the unique characters plus `<UNK>`."""
    tokenizer = CharacterTokenizer.from_text("abca")
    assert tokenizer.vocab_size() == 4


def test_save_load(tmp_path: Path) -> None:
    """Saving and loading should preserve tokenizer behavior."""
    tokenizer = CharacterTokenizer.from_text("abc")
    path = tmp_path / "tokenizer.json"
    tokenizer.save(str(path))
    loaded = CharacterTokenizer.load(str(path))
    assert loaded.vocab == tokenizer.vocab
    assert loaded.encode("cab") == tokenizer.encode("cab")


def test_unknown_char_policy() -> None:
    """Unknown characters should map to the `<UNK>` token without crashing."""
    tokenizer = CharacterTokenizer.from_text("abc")
    encoded = tokenizer.encode("az")
    assert encoded[1] == tokenizer.unk_id

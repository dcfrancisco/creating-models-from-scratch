"""Character-level tokenizer implementation and persistence helpers."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Dict, List

from tiny_llm.config import Config
from tiny_llm.data import load_text
from tiny_llm.utils import ensure_dir

LOGGER = logging.getLogger(__name__)
UNK_TOKEN = "<UNK>"


class CharacterTokenizer:
    """A deterministic character-level tokenizer.

    Args:
        vocab: Ordered list of tokens. The `<UNK>` token is added automatically
            if it is missing.
    """

    def __init__(self, vocab: List[str]) -> None:
        normalized_vocab = list(vocab)
        if UNK_TOKEN not in normalized_vocab:
            normalized_vocab = [UNK_TOKEN] + normalized_vocab
        self.vocab = normalized_vocab
        self.token_to_id: Dict[str, int] = {token: index for index, token in enumerate(self.vocab)}
        self.id_to_token: Dict[int, str] = {index: token for index, token in enumerate(self.vocab)}
        self.unk_id = self.token_to_id[UNK_TOKEN]

    @classmethod
    def from_text(cls, text: str) -> "CharacterTokenizer":
        """Build a tokenizer from all unique characters found in text.

        Args:
            text: Source text used to construct the vocabulary.

        Returns:
            Tokenizer with lexicographically sorted character vocabulary.
        """
        vocab = sorted(set(text))
        return cls(vocab)

    def encode(self, text: str) -> List[int]:
        """Encode text into token IDs.

        Unknown characters map to the `<UNK>` token ID.
        """
        return [self.token_to_id.get(character, self.unk_id) for character in text]

    def decode(self, ids: List[int]) -> str:
        """Decode token IDs back into text.

        Args:
            ids: Token IDs.

        Returns:
            Decoded string. Unknown IDs are rendered as `<UNK>`.
        """
        return "".join(self.id_to_token.get(index, UNK_TOKEN) for index in ids)

    def vocab_size(self) -> int:
        """Return the vocabulary size `V`."""
        return len(self.vocab)

    def save(self, path: str) -> None:
        """Save tokenizer vocabulary as JSON.

        Args:
            path: Output JSON path.
        """
        destination = Path(path)
        ensure_dir(str(destination.parent))
        payload = {"version": "0.1.0", "vocab": self.vocab}
        destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str) -> "CharacterTokenizer":
        """Load a tokenizer from JSON.

        Args:
            path: JSON file path.

        Returns:
            Loaded tokenizer.
        """
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls(list(payload["vocab"]))


def build_vocab(config: Config) -> str:
    """Build and save a character tokenizer for the configured dataset.

    Args:
        config: Loaded project configuration.

    Returns:
        Filesystem path to the saved tokenizer JSON.
    """
    text = load_text(config.data.dataset_path)
    tokenizer = CharacterTokenizer.from_text(text)
    output_path = Path(config.training.output_dir) / "tokenizer.json"
    tokenizer.save(str(output_path))
    LOGGER.info("Saved tokenizer with vocab size %s to %s", tokenizer.vocab_size(), output_path)
    return str(output_path)

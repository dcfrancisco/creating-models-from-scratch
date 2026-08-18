"""Training orchestration for the tiny_llm baseline models."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict

from tiny_llm.checkpoint import save_checkpoint
from tiny_llm.config import Config
from tiny_llm.data import load_text, train_val_split
from tiny_llm.evaluate import compute_perplexity
from tiny_llm.model import BigramLM
from tiny_llm.tokenizer import CharacterTokenizer
from tiny_llm.utils import ensure_dir, set_seed

LOGGER = logging.getLogger(__name__)


class BigramTrainer:
    """Trainer for the count-based bigram baseline.

    Args:
        config: Loaded project configuration.
    """

    def __init__(self, config: Config) -> None:
        self.config = config

    def train(self, text: str, tokenizer: CharacterTokenizer) -> BigramLM:
        """Fit the bigram model on training text and log simple metrics.

        Args:
            text: Full corpus text.
            tokenizer: Tokenizer used to encode the corpus.

        Returns:
            Fitted `BigramLM` instance.
        """
        set_seed(self.config.training.random_seed)
        train_text, val_text = train_val_split(text, seed=self.config.training.random_seed)
        train_ids = tokenizer.encode(train_text)
        val_ids = tokenizer.encode(val_text)
        model = BigramLM(tokenizer.vocab_size())
        model.vocab = tokenizer.vocab
        model.fit(train_ids)
        train_loss = model.loss(train_ids)
        val_loss = model.loss(val_ids)
        LOGGER.info(
            "bigram baseline train_loss=%.6f val_loss=%.6f perplexity=%.6f",
            train_loss,
            val_loss,
            compute_perplexity(val_loss),
        )
        return model


def run_training(config: Config) -> str:
    """Run the bounded baseline training workflow and save a checkpoint.

    Args:
        config: Loaded project configuration.

    Returns:
        Path to the saved checkpoint directory.
    """
    if config.training.numerical_backend == "torch":
        LOGGER.warning(
            "Torch backend is configured but not yet implemented; using the NumPy bigram baseline."
        )
    ensure_dir(config.training.output_dir)
    text = load_text(config.data.dataset_path)
    tokenizer = CharacterTokenizer.from_text(text)
    tokenizer_path = Path(config.training.output_dir) / "tokenizer.json"
    tokenizer.save(str(tokenizer_path))
    trainer = BigramTrainer(config)
    model = trainer.train(text, tokenizer)
    token_ids = tokenizer.encode(text)
    metrics: Dict[str, float] = {
        "train_loss": model.loss(token_ids),
        "vocab_size": float(tokenizer.vocab_size()),
    }
    checkpoint_path = Path(config.training.output_dir) / f"checkpoint-step-{config.training.training_steps:06d}"
    return save_checkpoint(model, config, config.training.training_steps, metrics, str(checkpoint_path))

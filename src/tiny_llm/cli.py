"""Argparse-based command-line interface for tiny_llm."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from typing import List, Optional

from tiny_llm.checkpoint import inspect_checkpoint
from tiny_llm.config import load_config
from tiny_llm.data import inspect_dataset
from tiny_llm.doctor import run_doctor
from tiny_llm.evaluate import run_evaluation
from tiny_llm.generate import run_generation
from tiny_llm.tokenizer import build_vocab
from tiny_llm.train import run_training

LOGGER = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI parser and subcommands."""
    parser = argparse.ArgumentParser(prog="tiny_llm", description="Learning-first tiny language model CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor", help="Inspect Python, CPU, memory, disk, NumPy, and optional torch availability.")

    data_parser = subparsers.add_parser("data", help="Dataset-related commands.")
    data_subparsers = data_parser.add_subparsers(dest="data_command", required=True)
    data_inspect = data_subparsers.add_parser("inspect", help="Inspect dataset statistics from a config file.")
    data_inspect.add_argument("--config", required=True, help="Path to a TOML config file.")

    tokenizer_parser = subparsers.add_parser("tokenizer", help="Tokenizer-related commands.")
    tokenizer_subparsers = tokenizer_parser.add_subparsers(dest="tokenizer_command", required=True)
    tokenizer_build = tokenizer_subparsers.add_parser("build", help="Build and save the configured tokenizer.")
    tokenizer_build.add_argument("--config", required=True, help="Path to a TOML config file.")

    train_parser = subparsers.add_parser("train", help="Run the bounded baseline training workflow.")
    train_parser.add_argument("--config", required=True, help="Path to a TOML config file.")

    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate a checkpoint on the validation split.")
    evaluate_parser.add_argument("--checkpoint", required=True, help="Checkpoint directory path.")

    generate_parser = subparsers.add_parser("generate", help="Generate text from a checkpoint.")
    generate_parser.add_argument("--checkpoint", required=True, help="Checkpoint directory path.")
    generate_parser.add_argument("--prompt", required=True, help="Prompt text used to start generation.")
    generate_parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature; 0 uses greedy decoding.")
    generate_parser.add_argument("--top-k", type=int, default=0, help="Optional top-k restriction; 0 disables it.")
    generate_parser.add_argument("--length", type=int, default=200, help="Number of new tokens to generate.")

    checkpoint_parser = subparsers.add_parser("checkpoint", help="Checkpoint-related commands.")
    checkpoint_subparsers = checkpoint_parser.add_subparsers(dest="checkpoint_command", required=True)
    checkpoint_inspect = checkpoint_subparsers.add_parser("inspect", help="Inspect checkpoint metadata.")
    checkpoint_inspect.add_argument("--checkpoint", required=True, help="Checkpoint directory path.")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    """Parse CLI arguments and dispatch commands.

    Args:
        argv: Optional argument vector for tests.

    Returns:
        Exit status code.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "doctor":
            print(run_doctor())
            return 0
        if args.command == "data" and args.data_command == "inspect":
            config = load_config(args.config)
            print(json.dumps(inspect_dataset(config), indent=2))
            return 0
        if args.command == "tokenizer" and args.tokenizer_command == "build":
            config = load_config(args.config)
            print(build_vocab(config))
            return 0
        if args.command == "train":
            config = load_config(args.config)
            print(run_training(config))
            return 0
        if args.command == "evaluate":
            print(json.dumps(run_evaluation(args.checkpoint), indent=2))
            return 0
        if args.command == "generate":
            print(
                run_generation(
                    args.checkpoint,
                    prompt=args.prompt,
                    temperature=args.temperature,
                    top_k=args.top_k,
                    length=args.length,
                )
            )
            return 0
        if args.command == "checkpoint" and args.checkpoint_command == "inspect":
            print(json.dumps(inspect_checkpoint(args.checkpoint), indent=2))
            return 0
        print("not yet implemented")
        return 1
    except NotImplementedError as error:
        print(f"not yet implemented: {error}", file=sys.stderr)
        return 1
    except Exception as error:
        LOGGER.error("Command failed: %s", error)
        return 1

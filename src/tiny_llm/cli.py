"""Headless command-line interface for tiny_llm."""

from __future__ import annotations

import argparse

from tiny_llm.doctor import run_doctor_command


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tiny_llm")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("doctor", help="Inspect host and dependency compatibility")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "doctor":
        return run_doctor_command()

    parser.print_help()
    return 0

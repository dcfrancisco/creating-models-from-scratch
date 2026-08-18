"""Experiment metadata capture for reproducible evidence records."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List

import numpy as np

from tiny_llm.config import Config, config_to_dict
from tiny_llm.data import compute_checksum
from tiny_llm.utils import ensure_dir, get_timestamp


@dataclass
class ExperimentRecord:
    """Machine-readable metadata for a training or evaluation experiment."""

    experiment_id: str
    timestamp: str
    purpose: str
    hypothesis: str
    git_commit: str
    dirty_working_tree: bool
    configuration: Dict[str, Any]
    dataset_identity: str
    dataset_checksum: str
    vocabulary_identity: str
    random_seed: int
    backend: str
    dependency_versions: Dict[str, str]
    hardware_summary: Dict[str, str]
    parameter_count: int
    start_time: str
    end_time: str = ""
    training_duration_seconds: float = 0.0
    metrics: Dict[str, Any] = field(default_factory=dict)
    checkpoint_path: str = ""
    generated_samples: List[str] = field(default_factory=list)
    errors_or_warnings: List[str] = field(default_factory=list)
    interpretation: str = "Pending interpretation"
    limitations: str = "Pending limitations"
    next_action: str = "Pending next action"


def _git_commit() -> str:
    """Return the current git commit hash or `unknown`."""
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "unknown"


def _git_dirty() -> bool:
    """Return whether the git working tree is dirty."""
    try:
        output = subprocess.check_output(["git", "status", "--porcelain"], text=True, stderr=subprocess.DEVNULL)
        return bool(output.strip())
    except Exception:
        return False


def start_experiment(config: Config) -> ExperimentRecord:
    """Create an experiment record before running a bounded experiment.

    Args:
        config: Loaded configuration for the run.

    Returns:
        Partially populated experiment record.
    """
    timestamp = get_timestamp()
    experiment_id = timestamp.replace(":", "-")
    return ExperimentRecord(
        experiment_id=experiment_id,
        timestamp=timestamp,
        purpose="Baseline experiment",
        hypothesis="A small reproducible baseline can be trained and evaluated end-to-end.",
        git_commit=_git_commit(),
        dirty_working_tree=_git_dirty(),
        configuration=config_to_dict(config),
        dataset_identity=Path(config.data.dataset_path).name,
        dataset_checksum=compute_checksum(config.data.dataset_path),
        vocabulary_identity="pending",
        random_seed=config.training.random_seed,
        backend=config.training.numerical_backend,
        dependency_versions={"numpy": np.__version__},
        hardware_summary={"platform": "see doctor output"},
        parameter_count=0,
        start_time=timestamp,
    )


def finish_experiment(record: ExperimentRecord, metrics: Dict[str, Any], samples: List[str]) -> str:
    """Finalize and persist an experiment record.

    Args:
        record: Experiment metadata record.
        metrics: Final metrics.
        samples: Generated text samples.

    Returns:
        Path to the experiment directory.
    """
    record.end_time = get_timestamp()
    record.metrics = metrics
    record.generated_samples = samples
    experiment_dir = Path("artifacts") / "experiments" / record.experiment_id
    ensure_dir(str(experiment_dir))
    (experiment_dir / "record.json").write_text(json.dumps(asdict(record), indent=2), encoding="utf-8")
    markdown_lines = [
        f"# Experiment {record.experiment_id}",
        "",
        f"- timestamp: {record.timestamp}",
        f"- purpose: {record.purpose}",
        f"- hypothesis: {record.hypothesis}",
        f"- git commit: {record.git_commit}",
        f"- backend: {record.backend}",
        f"- dataset checksum: {record.dataset_checksum}",
        f"- metrics: {record.metrics}",
        "",
        "## Samples",
        "",
    ]
    markdown_lines.extend(f"- {sample}" for sample in samples)
    (experiment_dir / "report.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")
    return str(experiment_dir)

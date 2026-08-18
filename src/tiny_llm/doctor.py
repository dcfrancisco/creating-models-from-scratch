"""Environment qualification helpers for CPU-first headless execution."""

from __future__ import annotations

import json
import platform
import shutil
import sys
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class DoctorReport:
    python_version: str
    implementation: str
    platform: str
    machine: str
    processor: str
    has_numpy: bool
    numpy_version: str | None
    has_torch: bool
    torch_version: str | None
    has_torch_autograd: bool
    has_gcc: bool


def collect_doctor_report() -> DoctorReport:
    """Collect host information for baseline qualification."""
    python_version = platform.python_version()
    implementation = platform.python_implementation()
    has_numpy = False
    numpy_version: str | None = None
    has_torch = False
    torch_version: str | None = None
    has_torch_autograd = False

    try:
        import numpy

        has_numpy = True
        numpy_version = numpy.__version__
    except ImportError:
        has_numpy = False

    try:
        import torch

        has_torch = True
        torch_version = torch.__version__
        x = torch.tensor([1.0], requires_grad=True)
        y = x * 2
        y.backward()
        has_torch_autograd = x.grad is not None
    except (ImportError, OSError, RuntimeError, ValueError):
        has_torch = False

    return DoctorReport(
        python_version=python_version,
        implementation=implementation,
        platform=platform.platform(),
        machine=platform.machine(),
        processor=platform.processor(),
        has_numpy=has_numpy,
        numpy_version=numpy_version,
        has_torch=has_torch,
        torch_version=torch_version,
        has_torch_autograd=has_torch_autograd,
        has_gcc=shutil.which("gcc") is not None,
    )


def format_doctor_report_json(report: DoctorReport) -> str:
    """Return a machine-readable JSON report."""
    return json.dumps(asdict(report), indent=2, sort_keys=True)


def run_doctor_command() -> int:
    """Run doctor command and print report."""
    report = collect_doctor_report()
    print(format_doctor_report_json(report))

    if not report.has_numpy:
        print("ERROR: NumPy is required for initial milestone.", file=sys.stderr)
        return 2
    return 0

"""Environment qualification helpers for headless CPU-first execution."""

from __future__ import annotations

import platform
import shutil
import sys
from pathlib import Path
from typing import Dict, Optional

import numpy as np


def _read_first_cpu_model() -> str:
    """Read the first CPU model name from `/proc/cpuinfo` when available."""
    cpuinfo_path = Path("/proc/cpuinfo")
    if not cpuinfo_path.exists():
        return platform.processor() or "unknown"
    for line in cpuinfo_path.read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("model name"):
            return line.split(":", 1)[1].strip()
    return platform.processor() or "unknown"


def _read_meminfo_total() -> Optional[str]:
    """Return the `MemTotal` line from `/proc/meminfo` when available."""
    meminfo_path = Path("/proc/meminfo")
    if not meminfo_path.exists():
        return None
    for line in meminfo_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("MemTotal:"):
            return line.split(":", 1)[1].strip()
    return None


def run_doctor() -> str:
    """Collect a headless environment report and return it as formatted text.

    Returns:
        Multi-line string with Python, CPU, memory, disk, NumPy, and optional
        torch compatibility information.
    """
    report: Dict[str, object] = {}
    report["python_version"] = sys.version.replace("\n", " ")
    report["platform"] = platform.platform()
    report["machine"] = platform.machine()
    report["cpu"] = _read_first_cpu_model()
    report["ram"] = _read_meminfo_total() or "unavailable"

    matrix_a = np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float64)
    matrix_b = np.array([[5.0, 6.0], [7.0, 8.0]], dtype=np.float64)
    matrix_c = matrix_a @ matrix_b
    report["numpy_version"] = np.__version__
    report["numpy_smoke"] = matrix_c.tolist()

    torch_status = "not available"
    try:
        import torch

        tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
        result = (tensor @ tensor).sum()
        result.backward()
        torch_status = f"available ({torch.__version__})"
        report["torch_autograd"] = "ok"
    except ImportError:
        report["torch_autograd"] = "not available"
    except Exception as error:  # pragma: no cover - depends on local torch install
        torch_status = f"imported with runtime issue: {error}"
        report["torch_autograd"] = f"error: {error}"
    report["torch"] = torch_status

    disk_usage = shutil.disk_usage(Path.cwd())
    report["disk_total_gb"] = round(disk_usage.total / (1024 ** 3), 2)
    report["disk_free_gb"] = round(disk_usage.free / (1024 ** 3), 2)

    recommendation = "numpy-first"
    if torch_status.startswith("available"):
        recommendation = "numpy-first with optional torch follow-up"
    report["recommendation"] = recommendation

    lines = [
        "tiny_llm doctor report",
        f"Python: {report['python_version']}",
        f"Platform: {report['platform']}",
        f"Machine: {report['machine']}",
        f"CPU: {report['cpu']}",
        f"RAM: {report['ram']}",
        f"NumPy: {report['numpy_version']} smoke={report['numpy_smoke']}",
        f"Torch: {report['torch']} autograd={report['torch_autograd']}",
        f"Disk: total={report['disk_total_gb']}GB free={report['disk_free_gb']}GB",
        f"Recommendation: {report['recommendation']}",
    ]
    return "\n".join(lines)

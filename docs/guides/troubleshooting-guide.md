# Troubleshooting Guide

## Common early issues
- `doctor` reports missing NumPy: install runtime dependencies.
- PyTorch import failure on legacy CPU: keep NumPy-first path and log evidence in WP-000.
- Slow execution: use smoke configs and smaller inputs.

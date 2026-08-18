# Hardware Qualification Report (Initial)

## Scope note
This first report records sandbox evidence only. Final qualification must be rerun on the target AMD Phenom II X6 host.

## Exact commands used
```bash
uname -a
python --version
python3 --version
python -m tiny_llm doctor
```

## Observed results (sandbox)
- OS/kernel: Linux 6.17.0-1022-azure x86_64
- Python: 3.12.3
- Doctor summary:
  - NumPy: available
  - PyTorch: unavailable in sandbox runtime
  - GCC: available

## Compatibility conclusions
- Baseline Python + NumPy path is viable.
- PyTorch availability is not guaranteed and remains optional pending host-specific checks.

## Constraints discovered
- No direct evidence yet for target CPU flags (AVX/SSE) on final host.
- No direct evidence yet for target host RAM/swap/storage limits.

## Recommended initial configuration
- NumPy-first path for early work packages.
- Keep PyTorch optional until target-host import/autograd checks pass.

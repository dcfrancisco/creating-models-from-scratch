# Dependency Policy

Dependencies are intentionally minimal and must remain justified.

| Dependency | Purpose | Why stdlib alone is insufficient | Compatibility notes | License | Required/Optional |
| --- | --- | --- | --- | --- | --- |
| numpy | Numerical arrays, matrix math, probability operations | Efficient dense numerical computation is central to the project | Expected to work on CPU-first Linux; verify exact environment with `doctor` | BSD-3-Clause | Required |
| torch | Optional tensor/autograd backend for later neural work | Autograd and richer tensor APIs can accelerate learning about optimization | Must be treated as compatibility-gated on legacy non-AVX CPUs | BSD-style | Optional |
| pytest | Test runner | Stdlib `unittest` is possible, but pytest improves concise evidence-backed tests | Dev-only; no runtime impact | MIT | Optional (dev) |
| ruff | Linting and import organization | Stdlib has no equivalent integrated fast linter | Dev-only | MIT | Optional (dev) |
| mypy | Static type checking | Stdlib has no equivalent static type checker | Dev-only | MIT | Optional (dev) |

## Policy rules

- Do not add a dependency solely to avoid writing a small educational component.
- Keep runtime and development dependencies separate.
- Document replacement or fallback strategies when a dependency is optional.
- Revisit dependency choices through ADRs when they materially affect architecture or portability.

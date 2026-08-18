# WP-000: Repository and Hardware Qualification

- Status: In Progress
- Purpose: Qualify target host and choose compatible numerical backend.
- Scope: OS/CPU/RAM/storage/Python/NumPy/PyTorch compatibility checks.
- Explicit exclusions: model training implementation.
- Dependencies: ADR-0003, ADR-0007.
- Related ADRs: ADR-0003, ADR-0007, ADR-0008.

## Acceptance criteria
- Commands and observed results recorded
- Compatibility conclusion documented
- Recommended backend documented

## Required evidence
- CPU/memory/storage snapshots
- Python and NumPy smoke checks
- PyTorch import + autograd if available
- Matrix multiplication benchmark

## Implementation steps
1. Run qualification commands on target server.
2. Record outputs in `docs/reports/hardware-qualification.md`.
3. Decide backend and update ADR-0003 status.

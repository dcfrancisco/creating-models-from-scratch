# Reflection Questions

## WP-000: Hardware qualification

- What constraints did the target machine reveal?
- What evidence supports the backend decision?
- What operational risks remain after qualification?

## WP-001: Project skeleton and engineering baseline

- Why does the CLI matter for a headless learning project?
- What evidence shows the baseline is operationally usable?
- Which parts are designed versus fully verified?

## WP-002: Dataset acquisition and inspection

- Why must licensing and provenance be explicit?
- What dataset issues could break later work?
- How would you explain the split strategy?

## WP-003: Character tokenizer

- What does a character-level tokenizer simplify?
- What does it sacrifice compared with subword tokenization?
- How do you prove encode/decode correctness?

## WP-004 through WP-014

For each later work package, ask:

- What concept does this work package teach?
- What evidence would convince you the implementation is correct?
- What failure modes are most likely at this stage?
- How would you explain the tensor shapes or data flow to another engineer?

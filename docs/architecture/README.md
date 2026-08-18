# Architecture Documents

This directory explains the conceptual and operational architecture of `tiny_llm`.

## Contents

- [`system-overview.md`](system-overview.md): end-to-end lifecycle from dataset to generated text.
- [`component-model.md`](component-model.md): responsibilities and boundaries of major components.
- [`training-flow.md`](training-flow.md): training loop walkthrough with tensor-shape notation.
- [`generation-flow.md`](generation-flow.md): prompt-to-sample generation path.
- [`mathematical-foundations.md`](mathematical-foundations.md): progressive equations and worked examples.
- [`configuration-model.md`](configuration-model.md): TOML configuration schema and validation rules.
- [`evidence-model.md`](evidence-model.md): what evidence is required to support claims.
- `diagrams/`: optional supporting diagrams kept separately from the main documents.

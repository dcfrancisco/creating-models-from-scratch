# Configuration Model

Configuration values stay outside source where practical.

Core fields (planned): dataset path, seed, batch size, context length, embedding size,
head count, layer count, learning rate, steps, eval/checkpoint intervals, output dirs,
sampling settings, backend, threads.

Validation strategy: fail early on missing/incompatible values.

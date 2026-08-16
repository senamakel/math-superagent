# Lean bench — `deepseek/deepseek-v4-pro`

Provider: `deepseek`.

Each task is one call, with `src/prompts/lean_prover.md` as the system prompt, and the reply's Lean checked by the kernel through `scripts/lean-check`. A `statement` task ends in `sorry` by construction and is scored on compiling; a `proof` task is scored on the verdict.

**0 of 9 passed.**

| Task | Kind | Outcome | Result |
| --- | --- | --- | --- |
| `p1-proof-order-two` | proof | provider-error | fail |
| `p2-proof-sum-cubes` | proof | provider-error | fail |
| `p3-proof-cited` | proof | provider-error | fail |

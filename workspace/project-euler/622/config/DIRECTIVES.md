# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Stop building the library. METHOD.md is the binding constraint and nothing has been formalised yet: delegate to lean_prover now and get code/lean/Lib/ started. Statement first — the shuffle definition and the order-of-2 reduction as Lean theorems ending in sorry, checked with lean_check so a verdict is filed. A run that ends with an answer and no passing verdict has failed this task.

Stopped library-building: dropped the "expand the research/source library" task and recorded the reason (directive: METHOD.md is the binding constraint, nothing is formalised, an answer without a passing verdict is a failure). Replaced it with a top-of-list task delegating statement-first Lean work — the out-shuffle definition and the s(n) = ord_{n−1}(2) reduction as theorems ending in `sorry`, checked with `lean_check` — and opened `research/threads/lean-formalisation.md` to carry that direction, plus a one-paragraph CONTEXT.md update so every role sees formalisation is now the immediate step.

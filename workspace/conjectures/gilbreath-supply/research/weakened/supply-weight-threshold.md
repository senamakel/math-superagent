# SUPPLY — weight-threshold ladder (superseded)

This file was a duplicate ladder for the third-pass head question. It has been
**merged into** `research/weakened/supply-threshold-limit.md`, which holds the
canonical decomposition (difficulties: `sampling-bound`,
`limit-indeterminacy`, `boundary-spike`, `genericity-transfer`,
`primes-transfer`).

The two additions this file contributed were folded into the canonical ladder:

- `R-threshold-high-sample` — raise the sample count at n=64,128 from 300 to
  ≥1000 per weight before the frac column can support a plateau claim (GOAL.md's
  explicit demand), and decide whether the two consecutive 0.125 readings
  reproduce.
- `R-threshold-n512`'s sample count was raised from 300 to 1000 per weight to
  match.

No ladder block is present here, so the ledger derives nothing from this file.
Do not re-create a second ladder for this goal; work on
`research/weakened/supply-threshold-limit.md`.

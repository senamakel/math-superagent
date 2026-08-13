# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it. It carries what an agent would otherwise
rebuild from disk, from the note store, or from a session it was not present
for. Not a file catalogue (`research/INDEX.md` is) and not a narration of what
agents did.

Token budget 10,000; file is re-sent on nearly every model call, so length is a
bill the whole run pays many times over. Link the file that holds detail
compressed away.

## Established

- **The three witnesses, computed and checked** (exact integer arithmetic, `code/out/witnesses.json`):
  `2^0 = 1 = 1_3`, `2^2 = 4 = 11_3`, `2^8 = 256 = 100111_3`. These are the
  falsification oracle: **every claimed obstruction must be run against them**.
  A lemma that forbids digit-free `2^n` for all `n` above some point, but also
  forbids `n = 8`, is false — record it as refuted, not weakened. A lemma not
  run against the witnesses is `asserted`, never `checked`.
- **Verification bound reproduced, computed and checked**: exhaustive `n=0..2000`
  by exact big-int base-3 expansion finds **no digit-`2`-free value of `2^n`
  besides `0, 2, 8`** (`witnesses.json`). This is the bound the run has actually
  reproduced; anything computed past it is new.
- **Structure, sourced** (standard, stated in `problem.md`): the multiplicative
  order of `2` mod `3^k` is `2·3^(k-1)` for `k ≥ 1`. Hence `2^n mod 3^k` depends
  only on `n mod 2·3^(k-1)`, and the digit-avoidance sieve on residue classes is
  `A_k = { n mod 2·3^(k-1) : low k ternary digits of 2^n mod 3^k lie in {0,1} }`.
  `|S_k| = 2^k` out of `3^k`; `A_{k+1}` refines `A_k`.
- **Sieve count, computed and checked for k ≤ 26** (`code/out/sieve_Ak.captured.txt`,
  `code/out/sieve_cannot_close.md`): `|A_k| = 2^(k-1)` exactly at every k tested.
  Computed by lifting rather than re-scanning — each surviving class mod
  `2·3^(k-2)` lifts to three candidates mod `2·3^(k-1)`, and exactly two survive.
  The witnesses `n = 0, 2, 8` remain in `A_k` at every level. **k=26 used 333s and
  2.1 GiB; further k by materialising A_k as a set will OOM-kill the container.
  Directive: no more sieving past k=26.**
- **Negative result (checked for k ≤ 22, not yet proved unconditionally)**: because
  `|A_k| = 2^(k-1)` grows without bound, the modular sieve never empties. No
  obstruction modulo any power of 3 can prove the conjecture at any finite 3-adic
  precision. The density `|A_k|/(2·3^(k-1)) = (1/2)(2/3)^(k-1) → 0` while the
  count doubles — the naive-count obstruction in `problem.md` is realized.
- **Lifting proof sketch (conjectured, not checked)**: LTE should give
  `2^{2·3^(k-2)} ≡ 1 + c·3^(k-1) (mod 3^k)` with `3 ∤ c`. Then the three
  lifts shift the top ternary digit by `{0, c, 2c} mod 3`, exactly one of
  which is 2, so exactly two survive. Proving this would make `|A_k| = 2^(k-1)`
  a theorem. The constant `c` and the congruence need verification before
  recording as proved. See `research/threads/lifting-proof.md`.

## Ruled out

- **Pure modular sieve** (`|A_k|` alone): `|A_k| = 2^(k-1)` grows without bound
  for `k ≤ 22`, so the sieve never empties. No obstruction modulo any power of 3
  can prove the conjecture at any finite 3-adic precision. Proven for `k ≤ 22`
  by exact computation; the 2-to-1 lifting still needs an unconditional proof
  (`research/threads/lifting-proof.md`). This is a negative result about the
  method, not about the conjecture: the conjecture may still be true, but the
  kill comes from structure the sieve cannot see.

Two arguments are already known to be true-and-irrelevant heuristics, never proofs (`problem.md`,
`GOAL.md`):
- **Density argument**: "density of integers whose ternary expansion avoids `2`
  tends to 0" is true but says nothing about the thin sequence `2^n`.
- **i.i.d.-digits heuristic**: gives `(2/3)^k`, explains why the conjecture is
  believed, proves nothing (no mechanism exhibited).
Neither is to be recorded as a proof.

## Numbers

- Witnesses verified: `1_3`, `11_3`, `100111_3` for `n = 0, 2, 8`.
- Exhaustive digit-free search, `n = 0..2000`: none besides `0, 2, 8`.
- `|A_k|` sieve counts for `k = 1..22`: `1, 2, 4, 8, ..., 2^(k-1)` exactly — size doubles at every level. Captured at `code/out/sieve_Ak.captured.txt` and `code/out/sieve_cannot_close.md`.
- Density `|A_k| / (2·3^(k-1)) = (1/2)(2/3)^(k-1) → 0` while count grows without bound.

## Recalled

No durable Cognee memory on this problem yet (recall_memory/relate_memory and
search_claims both empty). Nothing to import; hypotheses of any future recalled
claim must be checked against this problem before relying on it.

## Contradictions

- The **naive count obstruction** (`problem.md`, `GOAL.md`): `|A_k| ≈ 2·3^(k-1)·(2/3)^k ≈ 2^k/3` — the naive estimate **grows**, does not tend to 0. So `|S_k|/3^k → 0` (good) yet the indexed count needed is not monotone-down from this estimate. Any approach must say how it beats this estimate or why it is wrong. State it in `research/ROOT.md` before proposing an approach.

## Gaps

- **Narkiewicz (1980) primary source** — the claim (bound `N(x) ≤ 1.62·x^(log_3 2)`) is already extracted as `EP-406` from the Erdős problems catalogue (`research/summaries/erdos-problems-b33.md`), and Lagarias (LAG-2) independently gives the same exponent `α_0 = log_3 2`. The primary Narkiewicz paper itself is not yet in the library; downloading it is a verification step, not a gap in the statement. Thread: `research/threads/narkiewicz-bound.md`.
- **Proof of 2-to-1 lifting** — the LTE argument sketched in `code/out/sieve_cannot_close.md` and in `research/threads/lifting-proof.md`. Needs: computing `c = (2^{2·3^(k-2)} - 1)/3^(k-1) mod 3` and verifying `c ≠ 0 mod 3`. A proof turns `|A_k| = 2^(k-1)` from a fact about `k ≤ 22` into a theorem.
- **What the sieve cannot see** — once the lifting proof is done, the central question shifts from "does `|A_k| → 0`?" (answered: no, it grows) to "what non-modular structure kills the remaining classes?" Lagarias (LAG-4) states that the real truncated method and the 3-adic method each control opposite ends of the digits, and combining them is open. Dmitrov-Howe and Saye have further partial results.

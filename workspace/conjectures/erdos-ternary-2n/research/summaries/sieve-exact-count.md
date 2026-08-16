# The counting obstruction: |A_k| = 2^(k-1)

Prior-run result, recorded in CONTEXT.md as recalled, not this-run-verified. It is
the starting obstruction of the whole run (`problem.md`), so it earns a claim block.

## Statement

Let `A_k = { r mod 2·3^(k-1) : the low k ternary digits of 2^r mod 3^k avoid the digit 2 }`.
Claim: `|A_k| = 2^(k-1)` for all k ≥ 1.

## Why it is true (the bijection, from Lagarias'/Saye's order facts)

2 is a primitive root mod `3^k` (`ord_{3^k}(2) = 2·3^(k-1) = φ(3^k)`), so the map
`Φ_k : r ↦ 2^r mod 3^k` is a bijection from `r mod 2·3^(k-1)` onto the units
`(Z/3^k Z)^×`. A unit whose digit pattern avoids 2 must have low digit 1 (units are
odd mod 3, i.e. ≡ ±1; a 0 low digit would be divisible by 3) and the other k−1
digits in {0,1}: exactly `2^(k-1)` patterns. So `|A_k| = 2^(k-1)`.

## Consequence

`|A_k|` grows like `2^k`, never decays; the modular sieve can NEVER close by
counting at any finite 3-adic precision. Each of the `2^(k-1)` survivor classes
lifts to exactly 2 of 3 children at the next k. This is the obstruction every
approach must beat, and re-sieving to larger k after establishing it is not
progress.

**Status:** recalled from prior session (verified there to k=26 by direct sieve to
k=12, lift-count to k=11, order/LTE/witnesses to k=40), and reproduced here only
by the hand-check k=1 (`A_1 = {0}`, |A_1| = 1 = 2^0 ✓). Per GOAL.md this workspace
was cleared and restarted, so this must be re-verified by a fresh program before
being built on — cheap and one-time.

```claim
id: SIEVE-EXACT-COUNT
statement: |A_k| = 2^(k-1) for all k >= 1, where
  A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }.
  The modular sieve can therefore never close by counting at any finite 3-adic
  precision; a proof must show finitely many paths survive, not that the count
  decays.
hypotheses: ord_{3^k}(2) = 2·3^(k-1) for k >= 1 (2 a primitive root mod 3^k).
holds-here: yes.
status: asserted (recalled from prior session; only k=1 hand-checked in THIS
  workspace. Re-prove with a fresh sieve program before building on it.)
bearing: the counting obstruction this run must beat. Reframes the goal: orbit of
  1 under ×2 in Z_3^× (closure = all Z_3^×) meets the digit-{0,1} Cantor set S in
  exactly {1,4,256}. Proving |A_k|=2^(k-1) here is the cheap one-time re-check.
anchor: research/summaries/sieve-exact-count.md
follows-from: SAYE-ORDER-AND-LIFT
```

```claim
id: naive-heuristic-growth
statement: The naive heuristic estimate |A_k| ≈ 2·3^(k-1)·(2/3)^k GROWS like
  2^k/3 rather than tending to zero — it predicts A_k grows, in line with the
  exact |A_k| = 2^(k-1). It is a heuristic, never a proof.
hypotheses: none — a probabilistic estimate, recorded to be distinguished from
  proof.
holds-here: yes (it is the good heuristic), but as evidence-less heuristic under
  GOAL.md's rule it proves nothing.
status: conjectured (heuristic)
bearing: explains why the conjecture is believed and matches the exact count, but
  does not rule out counterexamples. Never to be recorded as a proof.
```

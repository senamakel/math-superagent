# The local step law of the leading {0,2} block — PROVED (general class)

**Status: proved (elementary), for ANY absolute-difference array — no parity,
no primes.** This is the strongest general-class theorem the run has, and it
makes the consumption/regeneration accounting exact. It upgrades the earlier
depth-1000 *observation* (`regeneration-lemma-edge-2-intruder-4-established`)
to a theorem.

## Setup and notation

Let `A_{k+1}(j) = |A_k(j) − A_k(j+1)|` on nonnegative integers, and let
`b_k` be the length of the maximal leading `{0,2}` block of `A_k`
(positions `1..b_k` in `{0,2}`, `b_k` maximal). Suppose an intruder
`y_k = A_k(b_k + 1)` exists (finite row; the block does not reach the row end)
and `b_k ≥ 1`. Write `x_k = A_k(b_k) ∈ {0,2}` for the edge (last block value).

## Theorem

```
b_{k+1} ≥ b_k   ⟺   (x_k, y_k) = (2,4),
b_{k+1} = b_k − 1   otherwise      (so b_{k+1} ≥ b_k − 1 always).
```

## Proof

Positions `1..b_k − 1` of row `k+1` are `|{0,2} − {0,2}| ⊆ {0,2}` — the only
arithmetic used is the closure of `{0,2}` under absolute differencing. Position
`b_k` of row `k+1` is `|x_k − y_k|`. Hence

```
b_{k+1} ≥ b_k  ⟺  |x_k − y_k| ∈ {0,2}.
```

With `x_k ∈ {0,2}` and `y_k ∉ {0,2}` (maximality): `x_k = 0` gives
`|0 − y_k| = y_k ∉ {0,2}`; `x_k = 2` gives `|2 − y_k| ∈ {0,2} ⟺ y_k ∈ {0,2,4}`,
and maximality excludes `y_k ∈ {0,2}`, so `y_k = 4`. That proves the iff; and
since nothing can make `b_{k+1} < b_k − 1` (the closure argument runs to
position `b_k − 1` regardless of the intruder), the complementary case is
exactly `b_{k+1} = b_k − 1`. ∎

## Corollaries (also exact)

1. **Drain law (erosion).** On an erosion step `b_{k+1} = b_k − 1`, the new
   intruder is `y_{k+1} = A_{k+1}(b_{k+1}+1) = A_{k+1}(b_k) = |x_k − y_k| =
   y_k − 2·[x_k = 2]`. The intruder never rises during erosion; at `y ≥ 4`
   it stays `≥ 4`, dropping by 2 exactly when the edge is 2.
2. **Intruder-4 absorbing.** At `y_k = 4`, an erosion step with `x_k = 0`
   keeps `y_{k+1} = 4`; a row with `y = 4` either stays in the 4-run (edge 0)
   or regenerates (edge 2). Hence every maximal run of intruder-4 rows ends in
   a regeneration (until finite-width exhaustion).
3. **Recharge identity.** For every `k`, with events = rows `i < k` at
   `(x_i, y_i) = (2,4)` and `j_i = b_{i+1} − b_i ≥ 0` at events:
   ```
   b_k = b_1 + Σ_{events i<k} (j_i + 1) − (k − 1).
   ```
   So for a parity-shape array (rows `≥ 1` even after position 0, e.g. the
   primes with `b_1 = 2`), **Gilbreath's conjecture is equivalent to**
   ```
   Σ_{events i<k} (j_i + 1) ≥ k − b_1   for all k.
   ```
   The whole open content of the conjecture is the rate at which the boundary
   pair `(2,4)` recurs — the recharge sum must never fall `k − b_1` behind.

## Sharpness

`(1,2,4)` → next row `(1,2, …)`: regenerates (`b` stays ≥ 1, here grows).
`(1,0,4)` → next row `(1,4, …)`: `b → 0` in one step.
`(1,2,6)` → next row `(1,4, …)`: `b → 0` in one step.
So the exclusion of `y ∉ {0,2,4}` is sharp: `y = 6` fails exactly as the
conjecture's failure mode requires (second entry 4, next row leading 3).

## Verification (independent routes, all exact integer)

- **Route 1 — numpy, sieve 2e7 (1,270,607 primes), depth 1000** (`step_law_theorem.py`,
  capture `code/out/step_law_captured.txt`): oracle k=1..40 block lengths
  match `witnesses.json`; step-law failures over 999 transitions = 0; drain
  law on erosion steps with intruder 101/101; recharge identity failures
  over k=2..1000 = 0; 60 (2,4)-events; total recharge 1,270,603 vs
  consumption 998, surplus ≈ 1273×.
- **Route 2 — pure Python, sieve 2e6 (148,933 primes), depth 300**
  (`step_law_independent.py`, capture `code/out/step_law_independent.captured.txt`):
  step-law failures 0, drain failures 0, recharge failures 0 over k=2..300,
  42 events, no b=1→b=0 transition. Includes the sharpness triples above.
- **Route 3 — general-class brute force (no primes, no parity)**
  (`step_law_theorem.py` §2): 400 random nonnegative arrays (200 even-shape
  `[1]+evens`, 200 fully arbitrary), depth 40 each: 3,521 eligible rows
  (`b ≥ 1`, intruder exists), 610 (2,4)-events, **zero step-law failures**.
  This is the theorem's hypotheses exactly — arbitrary absolute-difference
  arrays — and it holds.

## What is proved vs what is not

- **Proved:** the step law, drain law, intruder-4 absorption, and recharge
  identity as theorems of the absolute-difference operator on any array —
  this is the consumption side made exact, and the reduction of the
  conjecture to a recharge-rate statement.
- **Not proved:** that events keep arriving — that `Σ (j_i + 1)` never falls
  `k − b_1` behind. The primes enter only through the event density; nothing
  here shows the arrival rate is sufficient. That remains the whole open
  content (`research/threads/regeneration.md`).

## Fenced claim

```claim
id: step-law-theorem-proved
statement: For ANY absolute-difference array A_{k+1}(j) = |A_k(j) − A_k(j+1)| on nonnegative integers, with b_k the maximal leading {0,2} block length (positions 1..b_k), edge x_k = A_k(b_k), intruder y_k = A_k(b_k+1) (exists), b_k ≥ 1: b_{k+1} ≥ b_k ⟺ (x_k,y_k) = (2,4); otherwise b_{k+1} = b_k − 1. Corollaries: drain law y_{k+1} = y_k − 2·[x_k=2] on erosion; intruder-4 is absorbing under erosion (every maximal 4-run ends in regeneration); recharge identity b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1) — so for parity-shape arrays (primes, b_1=2) Gilbreath's conjecture is exactly Σ_{events i<k}(j_i+1) ≥ k − 2 for all k: the entire open content is the (2,4)-event arrival rate.
hypotheses: nonnegative integer entries; b_k ≥ 1; finite row with an intruder (b_k + 1 < row width). Sharp at the boundary: (1,0,4) and (1,2,6) die in one step, (1,2,4) regenerates.
holds-here: yes — verified on the real prime rows to depth 1000 (zero failures, 60 events, recharge surplus) and on 400 random non-negative arrays (3,521 eligible rows, 610 events, zero failures); the theorem needs no parity or prime hypothesis.
status: proved (elementary, 6-line argument: {0,2}-closure + |x−y| ∈ {0,2} analysis); independent exact verification on two prime sieves plus general-class brute force.
bearing: the consumption side is now an exact theorem; the step law, the recharge identity and the equivalent form of the conjecture (recharge sum ≥ k − 2) are proved; only the regeneration rate is open. Primes enter only through event density.
anchor: code/regeneration/step_law_theorem.py; code/regeneration/step_law_independent.py; code/out/step_law_captured.txt; code/out/step_law_independent.captured.txt
```

## Files

- `code/regeneration/step_law_theorem.py` — proof docstring + Route 1 & 3 checks.
- `code/regeneration/step_law_independent.py` — Route 2 independent check.
- `code/out/step_law_captured.txt`, `code/out/step_law_independent.captured.txt` — captures.
- `code/out/step_law_and_recharge_verified.md` — the earlier operator re-derivation
  (same content, `checked` status); this note supersedes it with the proof.
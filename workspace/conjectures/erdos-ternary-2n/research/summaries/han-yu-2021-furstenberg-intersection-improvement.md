# Han Yu, "Discrepancies of irrational rotations, binary expansions of powers of 3 and an improvement on Furstenberg's slicing problem"

Source: arXiv:1811.11073 (2018), published as Trans. AMS (2021), DOI 10.1090/tran/8410.
Full text: `research/sources/han-yu-2021-furstenberg-intersection-improvement.full.md`.

## What it establishes

**Number-theoretic theorem (Section 6).** For almost all integers `k ∈ ℕ`, the positions of digit-`1` in the
binary expansion of `3^k` contain 3-term arithmetic progressions. Method: discrepancy estimates for
irrational rotations (`{kα}`, `α = log 2/log 3`).

**Furstenberg slicing improvement (Theorems 1.5, 1.6, Corollary 1.7).** Let `A2, A3 ⊂ [0,1]` be closed,
`×2`- and `×3`-invariant respectively, with `dim_H A2 + dim_H A3 < 1`. Then the intersection
`A2 ∩ (uA3 + v)` is *sparse* and has **box dimension zero**, uniformly in real parameters `u, v` with
`u, u^{-1}` bounded away from 0. This is a sharp quantitative version of the Furstenberg intersection
problem (dimension of intersections of ×p- and ×q-invariant sets, p,q multiplicatively independent).

## Why it does NOT apply to this run's problem — the key boundary check

The Erdős problem, read 3-adically, is: does the orbit closure of `{2^n}` under `×2` meet the digit-`{0,1}`
Cantor set `S ⊂ Z_3` in more than the three known points? Two candidate translations to the torus fail:

- **The candidate sets have dimension sum > 1, violating the hypothesis.** `S` is a digit-restricted set of
  Hausdorff dimension `log 2/log 3 ≈ 0.6309`. The orbit closure of `2^n` is all of `Z_3^×` (dimension 1).
  So `dim(S) + dim(orbit closure) ≈ 0.6309 + 1 = 1.63 > 1`. Han Yu's theorems require the sum `< 1`.
- **The orbit closure is not ×3-invariant in the relevant sense.** `2^n` under `×2` fills `Z_3^×`; the
  transversality theorems need *two different* invariant sets (one ×2-invariant, one ×3-invariant), which
  is not the structure here (S is closed but its `×3`-invariance is trivial/absent; the orbit closure is the
  whole of `Z_3^×`).

So the Hen Yu/Furstenberg slicing machine **is silent exactly in the regime this problem occupies**: the
regime where the orbit closure has full dimension and the "bad" set has positive dimension, so the sum
exceeds 1. This confirms the `problem.md`/ROOT.md point that dimension/measure statements about `S` do not
reach which integers lie in it — and here the transversality theorems do not even *apply* because the
dimension sum is too large. The middle-digit gap (neither low-digits sieve nor high-digits size) is where
every one of these tools is silent.

## Status

Sourced; full text held. The negative boundary check (hypothesis `dim sum < 1` fails here) is the durable
finding — it rules out the entire Furstenberg-slicing line as a direct instrument for this problem, which
is worth recording so nobody re-derives it.

```claim
id: HAN-YU-2021-SLICING-DIM-SUM-LT-1
statement: The Furstenberg slicing theorems (Theorems 1.5/1.6, Cor 1.7) give box-dimension-zero, sparse intersections A2 ∩ (uA3+v) for closed ×2-invariant A2 and ×3-invariant A3 with dim_H A2 + dim_H A3 < 1.
hypotheses: A2 ×2-invariant, A3 ×3-invariant closed in [0,1], dim_H A2 + dim_H A3 < 1, u,u^{-1} bounded away from 0.
holds-here: no
status: asserted
bearing: the dimension-sum hypothesis FAILS for this problem (dim S ≈ 0.6309, orbit closure of 2^n under ×2 = all Z_3^× has dim 1, sum ≈ 1.63 > 1), so the whole Furstenberg-slicing/transversality machine is silent in exactly the regime this problem occupies. Rules out this line as a direct instrument.
anchor: research/summaries/han-yu-2021-furstenberg-intersection-improvement.md
```

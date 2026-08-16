# Pattern-finder deliverable: exact description of `{ M_d △ M_{d'} }`

Claim id: `pf-s2multiset`
Status: **verified numerically to n = 256; conjecture (not proved).**

## Statement

For `n ≥ 4`, let `{ M_d △ M_{d'} }` be the multiset of pairwise symmetric
differences of the fold down-sets `M_d = { n-1-d+o : o ⊆ d }` as `d, d'`
range over `[2, n-1]`. This is the index multiset of `S(n,h)²`, the sum of
Walsh characters that GOAL priority 4 asks to describe.

**The multiset is exactly:**
1. the **empty set**, with multiplicity `n − 2` (realized precisely by the
   `d = d'` pairs);
2. **every nonempty set with multiplicity exactly 2.**

## Equivalent reformulations (all verified to n = 256)

- The map on **unordered** pairs `{d,d'} ↦ M_d △ M_{d'}`, `d ≠ d'`, is
  **injective**.
- Number of distinct sets `= 1 + C(n-2, 2)` — the central polygonal /
  Lazy-Caterer number, **OEIS A152947** (`a(n) = 1+(n-2)(n-1)/2`), also part
  of A000124.
- Cardinality check: `(n−2)` [empty] + `2·C(n-2,2)` [nonempty, each ×2]
  = `(n−2) + (n-2)(n-3) = (n-2)²` ✓, consistent with the known total of
  `(n-2)²` ordered pairs.

## What establishes it

- `code/out/verify_multiple2.py`: n = 4..60, all pass.
- `code/out/verify_multiple2_big.py`: n = 64, 80, 96, 128, 160, 192, 256, all
  pass — empty multiplicity `n-2`, all nonempty multiplicities exactly 2,
  distinct count matching `1+C(n-2,2)`, total `(n-2)²`.
- `analyze_sequence` on the distinct-count sequence confirmed non-polynomial;
  `find_linear_recurrence` found `a(n) = 3a(n-1) − 3a(n-2) + a(n-3)`
  (reproduces the C(n,2) generating structure), consistent with the closed
  form.

## Sizes

All occurring sizes are **even** (predicted by the closed form
`2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`, each term a power of 2, and two
even popcount-powers canceling). Observed size distributions (distinct sets),
e.g. n=24: `{0:1, 2:20, 4:67, 6:28, 8:71, 10:6, 12:18, 14:6, 16:15}`.

## Bearing on COLLAPSE

This is the counting half of the crux: the index multiset of `S²` is
**not** dominated by a bounded number of candidate sets — it has quadratically
many *distinct* sets (so the Walsh-character expansion of `S²` spans many
distinct characters), yet the *multiplicities* are extremely rigid (2, except
the diagonal's `n−2`). Whether those quadratically-many distinct characters all
lie in the span of short-range (pair) correlations is the question GOAL
priority 2/3 poses; the pair-injectivity says the multiset itself carries no
redundancy to hide behind, so any collapse must come from algebraic relations
among the characters, not from multiplicity collapse.

## Falsifier

The first `n ≥ 4` such that either (a) some nonempty `M_d △ M_{d'}` has
multiplicity ≠ 2, or (b) the number of distinct sets ≠ `1 + C(n-2,2)`, or
(c) the empty set does not have multiplicity `n−2`. **None found up to n=256.**

## Caveat

This is a verified-numerical regularity, not a proof. The claim that survives
deserves a derivation (the down-set/translate structure of `M_d△M_{d'}` is
almost certainly the route); recorded here as conjectured so nobody re-runs the
census.

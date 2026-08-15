# Refuter report — R-weighted-excess-potential refuted

## Statement attacked
`R-weighted-excess-potential` (excess-energy-ladder, research/BACKWARD.md):
there exists a summable weight sequence `(w_i)_{i≥1}` with `w_1 > 0`,
`w_i ≥ 0`, and defect `d_i = max(0, A_k(i) − 2)`, such that the weighted
potential `P_k = Σ_i w_i·d_i` is non-increasing under the row operator for
EVERY nonneg-integer absolute-difference array: `P_{k+1} ≤ P_k`.

## Why this one
This is the excess-energy ladder's attempt at a universal monotone invariant
— a summable weighted potential. It is a "there exists weights" claim, and
"exists" universal claims are exactly the ones a single counterexample kills.
The run's settled `R-excess-max-nonincrease` uses a non-summable quantity
(max); the ladder hoped a summable weighted average would work. The
leftward-drift asymmetry of the operator is the natural place to break it.

## Answer: refuted (by hand, exact arithmetic)
Counterexample family (exists for every column length L):
```
A_L  = (1, 0, 0, ..., 0, Z)     Z >= 4 in last column L
A'   = (1, 0, 0, ..., 0, Z)     same shape, Z now in column L-1
```
(Start with the last column 0: |0−0|=0 everywhere; the front |1−0|=1; the
only Z contributes |0−Z| = Z.) Only the column holding Z has defect Z−2 > 0;
all 0-columns have defect 0. So:
```
P(parent) = w_L·(Z−2)
P(child)  = w_{L−1}·(Z−2)
```
Monotonicity `P_child ≤ P_parent` forces `w_{L−1}·(Z−2) ≤ w_L·(Z−2)`, i.e.
`w_{L−1} ≤ w_L`, for every L. Hence `w_1 ≤ w_2 ≤ ...`, and with `w_1 > 0`
every `w_i ≥ w_1 > 0`, so `Σ w_i` diverges: **the weights are not summable.**
No such summable weighted potential exists.

## Four-answer status
`find_counterexample` returned **undecided** on the `$int` arithmetic
encoding — this environment's model finder cannot interpret arithmetic
(documented in the run's own `cb_dying_pair_statement.md`, it returns
`undecided` on every refutable encoding here). The result rests on exact hand
arithmetic, fully written out above: `A' = (1,0,...,0,Z)` for
`A = (1,0,...,0,Z)`, `d(Z) = Z−2 > 0`, and the `P` comparison reduces to
`w_{L−1} ≤ w_L` for all L. `code/refute/check_weighted_potential.py` encodes
the identity; `find_counterexample` on `code/refute/weighted_potential.p`
came back `undecided`.

## What it means
The leftward drift of the operator forces any monotone weighted defect
potential to have non-decreasing weights — which a summable sequence cannot
have. So a *summable* weighted potential is out as the universal invariant.
What survives: non-summable monotone quantities (already owned as
`R-excess-max-nonincrease`), or a weighted potential over a **finite frontier
window** (weights only on columns near the block boundary, not the whole
tail). The excess-energy ladder should redirect to the finite-window form and
needs a recharge term at (2,4)-events.

## Not touched
The core conjecture, the step law, the recharge identity, Lemma 5.4, and every
settled restricted class (consecutive-odds, corner, {0,2}-block, lipschitz)
are untouched. This closes only the *summable* weighted-potential search.

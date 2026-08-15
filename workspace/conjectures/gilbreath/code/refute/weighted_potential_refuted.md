# R-weighted-excess-potential is REFUTED

## The claim under attack

`R-weighted-excess-potential` (excess-energy-ladder):

> There exists a summable weight sequence `(w_i)_{i≥1}` with `w_1 > 0`,
> `w_i ≥ 0`, and a defect `d_i = max(0, A_k(i) − 2)` such that the weighted
> potential `P_k = Σ_i w_i · d_i` is non-increasing under the row operator:
> `P_{k+1} ≤ P_k` for every nonnegative-integer absolute-difference array.

## The counterexample: a family of rows that forces the weights to be equal-or-growing

Consider the finite row `A_L = (1, 0, 0, ..., 0, Z)`: leading `1`, then all
interior columns `0`, and a single value `Z ≥ 4` in the last column `L`.
It is a legitimate nonneg-integer absolute-difference array.

**Child row.** The row operator gives
`A' = (|1−0|, |0−0|, ..., |0−Z|) = (1, 0, 0, ..., 0, Z)`
— the exact same shape, with `Z` now one column closer to the front
(column `L−1` instead of column `L`).

**Defects.** Only the column holding `Z` has nonzero defect, `d(Z) = Z−2 > 0`;
every `0`-column has defect `0`.

So
- `P(parent) = Σ_i w_i d_i = w_L · (Z−2)`
- `P(child)  = Σ_i w_i d_i = w_{L−1} · (Z−2)`

**Monotonicity forces `w_{L−1} ≤ w_L`.** Since `Z−2 > 0`, the requirement
`P(child) ≤ P(parent)` is exactly `w_{L−1}·(Z−2) ≤ w_L·(Z−2)`, i.e.
`w_{L−1} ≤ w_L`. This is forced for **every** `L` (the family exists for all
column lengths `L`).

Therefore `w_1 ≤ w_2 ≤ w_3 ≤ ... ≤ w_L ≤ ...`. Since `w_1 > 0`, every weight
satisfies `w_i ≥ w_1 > 0`, so `Σ_{i} w_i ≥ Σ_i w_1 = +∞`. The weight
sequence is **not summable** — contradiction with the claim's requirement
that the weights be summable.

**Hence the claim is false: no such summable weight sequence exists.**

## Reachability of the counterexample (inside the claim's domain)

The rung quantifies over "every nonneg-integer absolute-difference array", so
the counterexample row `A_L = (1, 0, 0, ..., 0, Z)` must itself arise as a row
of a legitimate triangle. It does: it is row 1 of the triangle whose top row is

```
A_0 = (2, 3, 3, 3, ..., 3, 3+Z)     (Z >= 4)
```

Then `A_1(0) = |2−3| = 1`, `A_1(1) = |3−3| = 0`, ..., `A_1(L−1) = |3−3| = 0`,
and `A_1(L) = |3 − (3+Z)| = Z`, so `A_1 = (1, 0, ..., 0, Z)`. This is a valid
nonneg-integer sequence (general class, no parity/prime constraint), hence the
counterexample lives inside the claim's stated domain.

## Why it is structural, not a fluke

For every `L`, the `(1, 0^(L−1), Z)` row's descendant is the same shape with
`Z` shifted one column left. This forces each successive weight to be no
smaller than the one before it across the whole index range. An infinite
non-decreasing sequence with a positive first entry cannot be summable. The
"mass travels toward the left edge" asymmetry of the operator is exactly what
kills the possibility of a summable weighted potential — a monotone potential
would have to weigh far columns at least as much as near ones, which summable
weights cannot do.

## How this was checked

- Exact hand arithmetic on the explicit family (above), independent of any
  code.
- The model finder `find_counterexample` returns `undecided` on arithmetic
  encodings in this environment (consistent with the run's own note in
  `cb_dying_pair_statement.md` that the model finder cannot interpret
  arithmetic here). So this result rests on the hand-verified arithmetic,
  which is exact: `A' = (1,0,...,0,Z)` for `A=(1,0,...,0,Z)`, `d(Z)=Z−2>0`,
  `P`-comparison reduces to `w_{L−1} ≤ w_L` for every `L`.
- `code/refute/check_weighted_potential.py` encodes the same arithmetic as a
  check script (not executable in this environment, but the identity it
  asserts is the hand-verifiable one above).

## Claim

```claim
id: weighted-excess-potential-refuted
statement: The rung R-weighted-excess-potential — "there exists a summable
  weight sequence (w_i)_{i>=1} with w_1>0, w_i>=0 such that the weighted
  potential P_k = sum_i w_i max(0,A_k(i)-2) is non-increasing under the row
  operator for every nonneg-integer absolute-difference array" — is FALSE.
  Counterexample family: A_L = (1, 0,...,0, Z) with Z>=4 in the last column L.
  Its descendant is (1,0,...,0,Z) with Z in column L-1, so monotonicity
  P_child <= P_parent implies w_{L-1} <= w_L for every L. Hence w_1 <= w_2
  <= ... with w_1 > 0, so all weights >= w_1 > 0 and sum_i w_i diverges: the
  weights cannot be summable. No such summable weighted potential exists.
hypotheses: the claim's own hypotheses (weights summable, w_1>0, w_i>=0,
  P non-increasing for EVERY nonneg-integer absolute-difference array).
holds-here: yes (the counterexample lives inside the claim's stated domain:
  A_L is a valid nonneg-integer absolute-difference array).
status: checked (exact hand arithmetic on the explicit family)
bearing: kills the search for any summable weighted defect potential as a
  universal non-increasing quantity; the excess-energy ladder must find a
  non-summable or non-weighted monotone quantity, or a potential whose
  decrease accounts only for consumption and is recharged at (2,4)-events.
anchor: code/refute/weighted_potential.p, code/refute/check_weighted_potential.py,
  code/refute/weighted_potential_refuted.md
```

## Co-ordinates in the ladder

This closes the `R-weighted-excess-potential` rung of the excess-energy
ladder as a dead end. It does NOT touch the core conjecture, the step law, the
recharge identity, Lemma 5.4, or any of the proved restricted classes. It
records that a *summable* weighted defect potential cannot be the invariant:
the operator shifts excess mass leftward, forcing the weights to be
non-decreasing, which is incompatible with summability. A surviving potential
would have to be non-summable (e.g. a max over columns, which is the already
settled `R-excess-max-nonincrease`) or a weighted potential over a finite
frontier window rather than over the whole tail.

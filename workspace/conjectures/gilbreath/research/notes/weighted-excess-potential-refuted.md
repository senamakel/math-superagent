# R-weighted-excess-potential — REFUTED universally by a one-line counterexample

## The rung (research/WEAKENED.md, excess-energy-ladder)

> There exists a summable weight sequence (w_i)_{i≥1} with w_1 > 0, w_i ≥ 0,
> and a defect d_i = max(0, A_k(i) − 2) such that the weighted potential
> P_k = Σ_i w_i · d_i is non-increasing under the row operator:
> P_{k+1} ≤ P_k for every nonnegative-integer absolute-difference array.

The difficulty the weights were meant to fix: `R-excess-total-nonincrease`
(weights ≡ 1) already fails because a spike deep in a row (e.g. 12) halves to a
6 that still exceeds the 2-defect floor while an entry moves left. The weights
were the advertised correction (mass far from the left edge must count less).
This refutation shows no weights can fix it.

## The counterexample

Parent row `A = (1, 4, 12, 0)` — leading 1, interior (4, 12, 0), all valid
(odd leading, even interior).

Row-operator image: `A' = (|1−4|, |4−12|, |12−0|) = (3, 8, 12)`.

Defects (interior columns):
- parent `d = (max(0,4−2), max(0,12−2), max(0,0−2)) = (2, 10, 0)`
- child  `d' = (max(0,8−2), max(0,12−2)) = (6, 10)`

## Why it refutes the universal claim

```
P(A') − P(A) = (6−2)w_1 + (10−10)w_2 − (0)w_3  =  4 w_1  >  0
```

- Column 1: child defect 6 > parent defect 2, strict at the exact column where
  the claim forces `w_1 > 0`.
- Column 2: 10 = 10, neutral.
- Column 3 (the dropped column, absorbed into A'(2)=12's column-2 defect): parent
  defect 0, so it cannot offset anything with its nonnegative weight.

So `P(A') > P(A)` for **every** admissible weight sequence (any w_1 > 0,
arbitrary nonnegative w_2, w_3, ...). The monotonicity claim fails universally,
no matter which weights are chosen.

## Mechanism / structure

This is the same failure shape as the run-count lemma and the raw total-excess
(`runcount-lemma-refuted`, `R-excess-total-nonincrease`): a two-element
interior pair `(4,12)` with large defect difference produces a child whose
first *position* carries a large merged defect. The defect moves *left and
grows* — `4 → 8` (defect 2 → 6) is a strict increase at position 1 — so any
left-biased weighting (w_1 > 0, which the claim mandates) makes the potential
increase. Only the *maximum* excess is monotone (`R-excess-max-nonincrease`,
Ducci max non-increase), and maximum is not a linear weighted sum.

The correct survival machinery is therefore **not** a linear weighted potential
over defects; it is the factored-max / rigidity template (Chamberland Ducci,
`ducci-max-factoring-potential-template`), exactly as `runcount-lemma-refuted`
already concluded. This closes the excess-energy ladder's weighted rung.

## Falsification anchor

`code/refute/weighted_excess_potential_refute.p` encodes the same pair with
the conjecture "P is non-increasing on (A,A')" (i.e. 4·w_1 ≤ 0 given w_1 > 0).
`find_counterexample` returned `undecided` — but that engine is **known
non-functional in this environment** (it returns `undecided` even on a
deliberately-false 2-element universal, and the prior run's
`cb-dying-pair_statement.md` already records "the model finder is unavailable
for refutation in this environment"). The refutation above is a two-line exact
arithmetic check, independent of any solver, and needs no execution engine.

## Claim

```claim
id: weighted-excess-potential-refuted
statement: R-weighted-excess-potential is FALSE: there is NO weight sequence
  (w_i>=0, w_1>0) making P_k = sum_i w_i max(0,A_k(i)-2) non-increasing for
  every absolute-difference array. Counterexample A=(1,4,12,0), A'=(3,8,12):
  parent defects (2,10,0), child defects (6,10), and P(A')-P(A)=4 w_1 > 0 for
  all w_1>0, since the strict increase is at column 1 (mandated w_1>0) and the
  dropped column 3 has defect 0.
hypotheses: the rung's own definition (defect d_i=max(0,A(i)-2), leading
  entry 1, even interiors, finite-support arrays, weight-1 column = left edge).
holds-here: yes
status: checked (one-line exact arithmetic; model finder unavailable here but
  the algebra is operator-truth, not a model search)
bearing: closes the excess-energy-ladder's weighted rung universally; the
  defect potential is not fixable by weights because the dropped column's
  weight cannot offset a strict left-position increase, and the left column
  weight is exactly what the claim forces positive. Confirms the
  ducci-max-factoring / rigidity template is the only surviving potential
  shape (consistent with runcount-lemma-refuted).
anchor: code/refute/weighted_excess_potential_refute.p,
  research/notes/weighted-excess-potential-refuted.md
```

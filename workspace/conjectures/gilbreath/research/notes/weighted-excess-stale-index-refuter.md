# R-weighted-excess-potential — already refuted; index is stale (refuter)

## Result

The weakened rung `R-weighted-excess-potential` (excess-energy-ladder) is
**FALSE**, and this was already banked on the claims ledger as
`weighted-excess-potential-refuted` (note `research/notes/weighted-excess-potential-refuted.md`).
However the rung file `research/weakened/excess-energy-ladder.md` STILL marks it
`stance: open` with the merge text "This is the rung to attack next." The
current task brief hands me exactly that as a live target. **This is a stale
index: a forward attempt on this rung would be wasted.**

## A smaller independent counterexample (this run)

`weighted-excess-potential-refuted` uses `A = (1,4,12,0)`. The following is
cheaper and independent:

```text
A      = (1, 4, 0)          d = max(0, A-2) = (0, 2, 0)   ->  P = 2·w2
child  = (|1-4|, |4-0|) = (3, 4)
                                    d' = (1, 2)           ->  P' = w1 + 2·w2
monotonicity P' <= P  ==>  w1 + 2·w2 <= 2·w2  ==>  w1 <= 0.
```

The rung mandates `w_1 > 0`. So **no** admissible weight sequence makes `P`
non-increasing on this single pair — the existential is false, universally.
The defect moves to the left edge and *grows* there (position 1 defect 0 -> 1),
which is exactly the one column whose weight the claim is forced to keep
positive. Mechanism is the same as `runcount-lemma-refuted` /
`R-excess-total-nonincrease` (Chamberland borderline spike-merge): the
operator sharpens rather than smooths, so no linear weighted defect potential
survives. Only the **max** excess is monotone
(`R-excess-max-nonincrease`), and max-monotonicity is far too weak to force
`A_k(1) ∈ {0,2}`.

## Recommend the index be corrected

Mark `R-weighted-excess-potential` in `WEAKENED.md` as `refuted` (killed by)
before any school spends a forward attempt re-deriving it. The refutation is
two lines of exact arithmetic and does not need a solver.

## Confirmation of a neighbouring open rung (by hand, not a proof)

I also hand-checked `R-intruder-4-always` (gap-lipschitz-ladder /
intruder-magnitude-ladder): the claim that all-intruder-equals-4 forces the
block never to die. Death forces the reachable checkpoint `A_k = (1, 0, 4, …)`
(because at b=1 the dying value is |v−4| with v∈{0,2}: only v=0 gives 4).
Backward, `(1,0,4,..)` needs parents `(1,a,b,c,..)` with |a−b|=0, |b−c|=4,
a∈{0,2}: the a=2 branch forces a 6 (intruder 6, violating the hypothesis),
the a=0 branch extends the zero block one position backward per row,
eventually forcing A_1(1)=0 against g_1=2. So this rung survives the obvious
attack — it looks TRUE, and I found no counterexample. It should not be the
refuter's next target.

## Falsification-anchor files

- `code/refute/weighted_excess_simple.py` — arithmetic check of the pair.
- `code/refute/weighted_excess_simple.p` — TPTP encoding of the same pair.
- `code/refute/weighted_excess_lp.py` — LP-feasibility formulation (would
  certify infeasibility over a window when an LP solver is available).

`find_counterexample` returned `undecided` on the TPTP pair; the existing
record (`weighted-excess-potential-refuted`) already notes the model finder is
non-functional in this environment (it returns `undecided` even on a
deliberately-false 2-element universal). The refutation is operator-truth by
exact arithmetic, independent of any solver.

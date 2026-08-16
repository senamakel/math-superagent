# Hit-set / positional-supply functional — priced out (closed by directive 43)

```approach
idea: >
  The n=8 witness separates h=e_6 from h'=e_5 (equal C_1, S²=0 vs 4) by WHICH
  depths reach each position: e_{n-2} is read exactly at odd d, e_{n-3} at a
  different hit set. Generalising: for each position j define the hit set
  H_j = {d ∈ [2,n-1] : j ∈ M_d}, and consider functionals of the multiset
  {H_j : h_j = 1}. The natural positional-supply functional asks whether the
  prime switch bits concentrate on HIGH-hit positions (large |H_j|), so an
  arithmetic input of the form "the switch bits land on high-hit positions
  often enough" would force wt(Φ_n h) ≥ c·n.
mechanism: >
  A 1 at position j is read by |H_j| = #{d ∈ [2,n-1] : (n-1-j) ⊆ d} depths
  (claim read-cone-closed-form-exact), so the positional resource is the
  distribution of |H_j| over the positions with h_j = 1. Linear supply forced
  by positional concentration needs the high-hit positions to carry the switch
  bits, and the high-hit positions to have positive density.
status: refuted
killed-by: >
  Operator directive 43 computed the hit-set profile directly and it fails
  priority 2's pricing test. Table (operator-computed, not yet independently
  re-derived by the run):

      n     max|H_j|   median|H_j|   frac(|H_j| >= 0.4n)
      16      14           4            0.312
      32      30           8            0.188
      64      62           8            0.109
     128     126          16            0.062
     256     254          16            0.035

  Two consequences. (1) It confirms the mechanism exactly: |H_{n-2}| equals the
  number of odd d in [2,n-1] (7, 15, 31, 63, 127), so the e_{n-2} result and
  its odd-d explanation are independently correct. (2) The finding: the
  fraction of positions with a LARGE hit set falls like 1/n (0.312, 0.188,
  0.109, 0.062, 0.035, roughly halving per doubling) while the median stays
  tiny (4, 8, 8, 16, 16). Only a vanishing fraction of positions carry linear
  positional supply, so "switch bits land on high-hit positions often enough"
  demands that h concentrate on a set of density -> 0 — a STRONGER demand than
  positive switch density, not weaker. The route fails priority 2's pricing
  test.
precedent: >
  In-workspace: read-cone-closed-form-exact (|H_j| = #{d : (n-1-j) ⊆ d}),
  enminus2-linear-supply-switch-density-not-necessary (the e_{n-2} witness),
  fixed-single-1-fold-weight-bounded-by-j (a fixed single 1 gives nu2 = O(1)).
falsifies: >
  A hit-set functional whose value is NOT controlled by the positional scarcity
  above would reopen the route — but none exists, and any future candidate must
  be priced against the table above before it can be claimed weaker than switch
  density.
```

## The honest caveat (directive 43)

`nu2` is an XOR over `M_d`, not a sum of `|H_j|`, so this prices the
**positional resource** only; it does not refute every functional built from
hit sets. A functional whose value is not controlled by the positional scarcity
above is still open — but it must be priced against this table.

Witness: the table is the operator's own direct computation (directive 43),
recorded here as the directive states it. It is **not** a run-established claim
until tool_builder independently re-derives it; treat the numbers as
operator-asserted, not as this run's measurement.

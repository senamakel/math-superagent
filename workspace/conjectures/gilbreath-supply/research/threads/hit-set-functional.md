# The hit-set functional — generalising the n=8 separating quantity

Directive 41 (priority 1, the head): the n=8 witness separates `h = e_6` from
`h' = e_5` — both single-1 strings with identical pair correlations `C_1`, yet
`S² = 0` vs `4`. The separation comes from *which depths reach each position*:
`e_{n-2}` is read exactly when `d-1 ⊆ d`, i.e. exactly at odd `d`, giving
`nu2 ~ n/2`; `e_{n-3}` has a different hit set entirely. So the separating
quantity is the arithmetic of the read-cone/hit-set of a position under the
submask relation, not any correlation of `h`. That is a functional, and it is
the priority-1 object this pass exists to build.

**CLOSED by directive 43.** The operator computed the hit-set profile directly
and priced the positional resource out: the fraction of positions with a large
hit set falls like `1/n` (0.312, 0.188, 0.109, 0.062, 0.035) while the median
stays tiny (4, 8, 8, 16, 16). An input phrased as "the prime switch bits land
on high-hit positions often enough" demands concentration on a set of density
→ 0 — a stronger demand than positive switch density, not weaker. The push
(directives 41/42) is withdrawn. Recorded as closed candidate
`hit-set-positional-supply` with the table as its witness, and the caveat that
this prices the positional resource, not every hit-set functional.

```thread
id: hit-set-functional
question: What is the precise functional of the fold that separates the n=8
  witness (h=e_6 vs h'=e_5, equal pair correlations, S²=0 vs 4), and how does
  it generalise from single-1 strings to general h? Concretely the per-position
  read-cone profile: a 1 at position j is read by exactly
  |C_j(n)| = #{d∈[2,n-1] : (n-1-j) ⊆ d} depths, weight 2^{-popcount(n-1-j)}
  per 1. Is this functional constant on C_1 (pair-correlation) fibres but not
  on the whole cube, at what lowest correlation order K does it become
  determined, and what arithmetic input on the prime string does it demand
  (priced against pointwise mod-4 switch density)?
status: dead
rests-on: read-cone-closed-form-exact,
  enminus2-linear-supply-switch-density-not-necessary,
  fixed-single-1-fold-weight-bounded-by-j
blocked-by:
killed-by: directive 43 — the operator computed the hit-set profile directly and
  priced the positional resource out: frac(|H_j| >= 0.4n) falls like 1/n
  (0.312, 0.188, 0.109, 0.062, 0.035) while median|H_j| stays tiny (4, 8, 8,
  16, 16), so "switch bits on high-hit positions" is a stronger demand than
  positive switch density. See closed candidate hit-set-positional-supply.
next: none — closed. The positional resource fails priority 2's pricing test
  (directive 43). A hit-set functional not controlled by that scarcity is still
  open but unbuilt; it must be priced against the table before being claimed
  weaker than switch density. No candidate survives pricing: the pass's
  conclusion is NO (research/CONCLUSION-PASS2.md).
```

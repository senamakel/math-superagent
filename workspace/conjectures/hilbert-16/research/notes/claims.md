### `approach-certified-lower-bound-target-escalated`

```claim
id: approach-certified-lower-bound-target-escalated
status: formalised
formalisation: code/lean/approach_certified_lower_bound_target_escalated-e7ec278b.lean
```
Lean formalises the logical shape of the cited Torregrosa claim: there exist two real-parameter families of planar fields, each having a parameter value with twelve distinct radii satisfying the file's explicit small-amplitude predicate. The theorem is conditional on the explicitly cited `Cited.torregrosa_two_families` axiom; the kernel-checked implication has no `sorry`.

Hypothesis mapping: `CubicFamily` carries the one-parameter family; `UnfoldsTwelve` carries existence of one parameter, twelve indexed radii, positivity and subunit smallness, and pairwise distinctness. The informal source's cubic-polynomial, equilibrium, degenerate-Hopf, and exact-computation hypotheses are not represented by Mathlib objects here; this is therefore a deliberately weaker formal statement of the literature claim, not a formalisation of the full dynamical assertion.
```
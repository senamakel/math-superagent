# Claim: exact logical exhibit shape

```claim
id: toeplitz-square-peg-G-curve-outside-published-classes-formal
statement: For a finite exact curve `γ₀`, if predicates `C`, `locallyMonotone`, `matschkeClass`, and `twoLipschitzGraphs` satisfy `C γ₀`, `¬ locallyMonotone γ₀`, `¬ matschkeClass γ₀`, `¬ twoLipschitzGraphs γ₀`, and `IsNondegenerateSquare γ₀`, then there exists a curve with all five properties.
status: formalised
formalisation: code/lean/toeplitz_square_peg_G_curve_outside_published_classes-a7681979.lean
```

The binders correspond as follows: `C` is the named class; `locallyMonotone`,
`matschkeClass`, and `twoLipschitzGraphs` are the three exclusion predicates;
`γ₀` is the exhibited Jordan curve; `hC`, `hnotLocal`, `hnotMatschke`,
and `hnotLipschitz` carry the three exclusions and class membership; `hsquare`
carries exact nondegenerate-square verification. The theorem is formally
verified, but conditional on these hypotheses. The source text does not define
these classes (nor Jordan curves as maps `S¹ → ℝ²`) sufficiently to prove that
such a `γ₀` exists. Therefore this is not evidence that the requested concrete
outside-class curve has been exhibited; it precisely records the missing
specification and proves only the existential packaging.

`lean_check` verdict: compiled, verified; no sorry warnings. Axioms:
`propext`, `Classical.choice`, `Quot.sound`.
```
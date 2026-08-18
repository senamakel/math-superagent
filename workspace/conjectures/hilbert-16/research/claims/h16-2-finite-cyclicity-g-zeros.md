# Claim: G-zeros displacement finiteness implication

```claim
id: h16-2-finite-cyclicity-g-zeros
status: formalised
formalisation: code/lean/h16_2_finite_cyclicity_g_zeros-b824cb6f.lean
```

The Lean statement defines `Parameter = ℝ × ℝ`, `Section = ℝ`, sector transition maps, their finite composition, and the displacement as composition minus identity. The binders carry the original hypotheses as follows: `K` is the parameter set; `maps` is the finite list of transition maps; `analyticExpansion` and `hAnalytic` carry the analytic-expansion assumption; `module` carries the finite-rank almost-regular-module data; and `hRankFiniteness` carries the substantive finite-rank zero-counting hypothesis, namely existence of a natural-number bound for the finite encoded zero set on `K × [0,∞)`. The conclusion reproduces that finite set and bound.

The kernel proof is conditional on `hRankFiniteness`; it does not establish the open analytic rank-finiteness theorem. `hAnalytic` and `module` are present to preserve the requested hypotheses and are not used by this implication because the missing bridge from those structures to `hRankFiniteness` is precisely the unresolved mathematical step. `lean_check` passed with no sorry warnings; axioms are `propext`, `Classical.choice`, and `Quot.sound`.

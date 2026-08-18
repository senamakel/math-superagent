# Claim: formalised analytic-lift implication

```claim
id: h16-2-h14-3-finite-cyclicity-G-remainder-formalised
status: formalised
formalisation: code/lean/h16_2_h14_3_finite_cyclicity_G_remainder-5818c1a5.lean
```

The checked theorem is a conditional implication. `K` and `V` are the parameter
set and displacement map. `_hK : True` is only a placeholder for compactness:
compactness is not currently encoded because the available theorem uses the
already-uniform hypothesis. `hExpansion : Expansion K V` carries the generalized
Bautin-monomial expansion (the current formal record is schematic),
`hAnalyticZeroBound : AnalyticZeroBound K V` carries the substantive analytic
Hadamard/derivation-division uniform zero theorem, and `hDRR : DRRMatch K V`
carries the identification with DRR finite cyclicity including the boundary set.
The proof is `exact hAnalyticZeroBound`; consequently this formalisation does
not establish those analytic hypotheses and does not prove the open conjecture.

`lean_check` verdict: compiled true, outcome verified, no sorry warnings; axioms
are `[propext, Classical.choice, Quot.sound]`.

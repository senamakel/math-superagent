# Claim: formalised ECT-specialisation theorem (G-specialise-uniform-bound)

```claim
id: slow-divergence-ect-partial-specialisation-formalised
status: formalised
formalisation: code/lean/Lib/SlowDivergenceECTPartial.lean
```

The `sorry` in `SlowDivergenceECTPartial.full_graphic_zero_bound` is closed.
The theorem now states: given a compact parameter set `K`, a displacement
`δ : K → Section → ℝ`, propositional placeholders `endpoint_maps` and
`analytic_uniform_remainder` (the conditional content, to be supplied by the
endpoint-maps and analytic-remainder work), and an `ECTReduction K δ`
carrying (i) a finite-dimensional basis, (ii) the representation
`δ p x = ∑ i, coefficient p i * basis i p x`, (iii) nontriviality, and
(iv) the ECT property — every nontrivial linear combination of the basis has
a finite zero set with `ncard ≤ dimension - 1` — then

```
∃ N : ℕ, ∀ p ∈ K, ({x : Section | δ p x = 0}).Finite ∧
  Set.ncard {x : Section | δ p x = 0} ≤ N
```

holds with the uniform `N = reduction.dimension - 1`.

Proof: for each `p ∈ K`, rewrite the zero set through
`reduction.representation p hp x`, then apply
`reduction.ect_property p hp (reduction.coefficient p)
(reduction.nonzero p hp)`. Uniformity in `p` is exactly the ECT property being
quantified over `p ∈ K` in the reduction's `ect_property` field — this is the
step the naive "pointwise finiteness ⇒ uniform bound" would fake, and here the
uniform bound comes from the ECT structure of the basis family, not from
compactness.

`lean_check` verdict: compiled true, outcome verified, no sorries; axioms are
exactly `[propext, Classical.choice, Quot.sound]` (the kernel's three) —
`hK`, `hendpoint`, `hanalytic` are unused by this specialisation step and
remain as binders carrying the conditional content.

Evidence class: proved (the specialisation step is kernel-checked); the
`endpoint_maps` and `analytic_uniform_remainder` hypotheses remain open —
this is the conditional theorem of the `h16-2-i6b-four-dulac-finite-cyclicity`
skeleton's `G-specialise-uniform-bound`, and the gap that remains is the
analytic content itself (G-endpoint-germs, G-reduce-finite-rank,
G-ect-certificates), not this logical projection.

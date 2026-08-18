```claim
id: h16-2-finite-cyclicity-G-uniform
statement: Given a compact parameter set K and a family Z of zero sets, if the finite-dimensional/algebraic expansion principle supplies a common natural-number bound N with each Z(p) finite and ncard(Z(p)) ≤ N for p ∈ K, then the same N is a uniform cyclicity bound over K.
evidence: proved
status: formalised
formalisation: code/lean/h16_2_finite_cyclicity_G_uniform-62fab7f2.lean
falsifier: A model of the explicit UniformZeroBound hypothesis in which no common N exists.
```

Scope warning: this formalisation proves the logical uniformity extraction from the explicit hypothesis `finiteDimensionalExpansion : UniformZeroBound K Z`. It does not prove the analytic/algebraic expansion theorem itself, nor does it derive uniformity from pointwise finiteness. The binders carry the source hypotheses as follows: `K : Set ℝ` is the compact parameter box; `Z : ℝ → Set ℝ` is the zero-set family; `finiteDimensionalExpansion` carries compactness and the common bound supplied by the expansion module. The theorem's proof is projection of the existential component, so compactness is retained in the hypothesis but not needed by this final logical projection.
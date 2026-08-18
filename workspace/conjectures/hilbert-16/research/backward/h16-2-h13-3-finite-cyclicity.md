# Backward skeleton — finite cyclicity of the full `H^3_13` graphic

This skeleton isolates the missing H^3_13 row in the quadratic DRR program. Roussarie–Rousseau 2015 proves finite cyclicity only for its boundary limit-periodic set (Theorem 3.6); the full graphic still requires the intermediate and lower blown-up limit-periodic sets. The source says these should use arguments analogous to the complete I^1_14 proof, with one-dimensional displacement maps and generalized derivation–division.

```skeleton
goal: cycl(Λ = H^3_13) < ∞ inside the family of quadratic polynomial vector fields; equivalently, every limit-periodic set arising from the family blow-up of the H^3_13 graphic has a uniform finite cyclicity bound.
implies: The boundary limit-periodic set is discharged by RR 2015 Thm 3.6 (drr-rr-boundary-only-for-3-graphics). For every remaining intermediate/lower blown-up set, H13-blowup-strata-reduction classifies the finitely many strata and reduces each to a one-dimensional displacement V on a transversal (or on leaves rρ=ν). H13-generalized-displacement-expansion puts each V in the Bautin/generalized-monomial form of RR Thm 5.8 uniformly over a compact box, covering resonant σ0∈Q/N strata by compensator terms. H13-derivation-division-uniform-zero-bound applies the generalized derivation–division theorem uniformly, giving ≤ l−1 zeros per non-identical map. Finitely many strata ⇒ max of the bounds plus the boundary bound is a uniform cycl(Λ) bound; the DRR equivalence (h16-drr-121-graphics) makes it one conjunction member of H(2)<∞.
killed-by: (1) A stratum classification that misses a limit-periodic set of H^3_13 — the blow-up list for H^3_13 must be complete, not inherited from I^1_14. (2) An expansion that never uses the analytic/quasianalytic Dulac structure or uniform remainder — topology/formal jets alone bound a smooth falsity (Dulac's error shape). (3) A zero bound obtained per-stratum with no uniformity argument over the compact parameter box — pointwise finiteness does not imply a uniform bound.
rests-on: h16-drr-121-graphics, drr-rr-boundary-only-for-3-graphics, drr-rr-closes-i14; source: research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md (Thm 1.1, 3.6, 2.2, 2.3, 5.8, eq 3.27-3.32)
status: live
```

```gap
id: H13-boundary-cyclicity
lemma: The boundary limit-periodic set of the quadratic graphic H^3_13 has finite cyclicity.
status: discharged
discharged-by: drr-rr-boundary-only-for-3-graphics
next: discharged; RR 2015 Theorem 3.6 is the cited source. Its proof gives an explicit displacement form with at most two isolated zeros via Theorem 5.8.
```

```gap
id: H13-blowup-strata-reduction
lemma: For every parameter stratum in the family blow-up of H^3_13 other than the boundary stratum, the corresponding limit-periodic set is one of finitely many explicitly classified intermediate or lower sets, and its periodic orbits are exactly the isolated zeros of a one-dimensional displacement map V on a fixed transversal (equivalently, on each invariant leaf rρ=ν). The sections, regular transitions, saddle/Dulac transitions, and the parameter strata must be specified uniformly over a compact neighborhood of the graphic.
status: open
next: Read RR 2015 Table 2 and Sections 2.4–2.5 against the H^3_13 family (3.27); encode the finite list of H^3_13 blown-up strata and their section/leaf maps as a Lean structure, then use SymPy over Q to verify for each listed stratum that the composed return correspondence has one scalar displacement coordinate. Capture the list and exact maps in code/out/h13_blowup_strata.captured.txt.
```

```gap
id: H13-generalized-displacement-expansion
lemma: On each non-boundary H^3_13 stratum from H13-blowup-strata-reduction, the scalar displacement V admits, uniformly in the compact parameter neighborhood, a finite Bautin expansion V=Σ_{i=1}^l A_i(λ) M_i(ξ)(1+g_i(ξ,λ)), where A_i are coefficients in the relevant center ideal, M_i are generalized monomials in the transversal variable (including power and compensator factors), g_i are uniformly controlled C^k-functions on monomials with g_i=o(1), and all resonant parameter strata are represented by the corresponding logarithmic/compensator terms. The leading coefficients generate enough of the center ideal to prevent an identically uncontrolled displacement.
status: open
next: For each scalar map in the classified list, symbolically compose the RR Theorem 2.2 first-type Dulac formula, the regular transition, and the saddle power map; normalize the result into the generalized-monomial form of RR Theorem 5.8, treating σ₀∈Q and σ₀∈N separately. Check the center-ideal coefficient generators by exact polynomial ideal membership over Q, and capture formulas and remainder orders in code/out/h13_displacement_expansion.captured.txt.
```

```gap
id: H13-derivation-division-uniform-zero-bound
lemma: If a H^3_13 displacement has the expansion in H13-generalized-displacement-expansion, then the generalized derivation–division theorem applies uniformly on a sufficiently small compact parameter box: each non-identically-zero V has at most l−1 isolated zeros counted with multiplicity on every invariant leaf, with a bound independent of the parameter; identically-zero cases are excluded by the center-ideal/nonzero clause or are reduced to the first nonvanishing coefficient. The same finite bound holds on every non-boundary stratum.
status: open
next: Formalize the exact H^3_13 instance of RR Theorem 5.8 in Lean with explicit hypotheses for nonresonance, compact parameter box, generalized monomials, and uniform o(1) remainder; discharge the finite algebraic side conditions with `norm_num`, polynomial ideal membership, and Sturm/resultant checks. Separately test the resonant σ₀∈N formulas symbolically and verify that the bound is unchanged after compensator division. The theorem-prover target is a conditional Lean theorem whose only non-kernel assumptions are the cited RR derivation–division theorem and the expansion lemma.
```

The smooth test is located at `H13-generalized-displacement-expansion`: the uniform analytic/quasianalytic Dulac structure and controlled remainder are essential; topology or a formal asymptotic jet alone would not determine the displacement. Uniformity is supplied by the compact parameter box plus the finite generalized-monomial/derivation–division theorem, not by pointwise finiteness alone. The lower-bound test is harmless for this per-graphic finiteness statement, while the slow–fast test requires the resonant and center-ideal strata to be treated rather than silently omitted.

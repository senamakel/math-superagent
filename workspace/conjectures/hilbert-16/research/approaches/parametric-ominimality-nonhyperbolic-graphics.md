# Parametric o-minimality for the open non-hyperbolic graphics

```approach
idea: Replace the graphic-by-graphic normal-form resolution of the DRR program with a
     model-theoretic uniformity statement: prove that the FULL PARAMETRIC return map of a
     quadratic field near the open non-hyperbolic graphics (I⁶b¹, H¹₃³, DI₂b, H³₁₄) is
     definable in a fixed o-minimal (or tame quasianalytic) structure, and let the uniform
     finiteness principle deliver the uniform bound without resolving vertices. This extends
     Kaiser–Rolin–Speissegger (Crelle 636 (2009) 1–45), who made transition maps at isolated
     NON-RESONANT HYPERBOLIC singularities definable in the o-minimal, polynomially bounded
     expansion ℝ_Q, from the hyperbolic case to the semi-hyperbolic / nilpotent / degenerate
     vertices where the return germ is a transseries with iterated logs and exponentials.

mechanism: Roussarie's finite-cyclicity conjecture follows from o-minimality of the language of
     parametric transition maps via the uniform-finiteness principle (Speissegger arXiv:1804.03585,
     held). The proved case (K–R–S) covers exactly the non-resonant hyperbolic part; the open
     graphics are precisely where vertices are non-hyperbolic. The change of representation: the
     uniformity a graphic-by-graphic normal form extracts from finitely many vertex resolutions
     (G-resolve → G-transition → G-zeros) is, in the model-theoretic frame, a single definability
     theorem for the parametric map in a structure of "tamed" transseries — whence the uniform
     bound falls out of the uniform-finiteness principle with no case split over the 121 graphics.
     The definability object is genuinely different from the short-Dulac/fewnomial line (refuted):
     that one failed because the germ is a transseries, not a short function; here the transseries
     IS the object of study, and the analytic input (Test 1) is the quasianalytic/algebraic
     structure in which the map is definable. Concrete named machinery: parametric generalized
     power series / the quasianalytic Ilyashenko algebras of Kaiser–Rolin–Speissegger, and the
     tame-geometry extension to resonant and nilpotent transition maps (per the transseries
     normal-form literature the run already holds: Mardesić–Resman, Peran, Yeung natural-levels).

status: proposed

first-step: Choose ONE open graphic, say DI₂b (degenerate, through a multiplicity-3 nilpotent
     point, where RR 2015 close only the boundary limit periodic set), and attempt to write its
     parametric transition map as a definable function in a Kaiser–Rolin–Speissegger-type
     expansion extended by one tamed transseries monomial family — i.e. reduce "finite cyclicity
     of DI₂b" to "the return map is definable in an o-minimal structure extending ℝ_Q". First
     executed check: re-derive the known finite-cyclicity of a hyperbolic graphic (the K–R–S
     territory, e.g. I¹₂¹ from Rousseau–Shan–Zhu) by this definability route, so the method is
     validated on ground it already covers before it is trusted on DI₂b. State the definability
     claim as a Cited axiom in Lean (it is a literature-level result, not this run's to prove)
     and record what Mathlib lacks for "o-minimal structure / definable function".
```

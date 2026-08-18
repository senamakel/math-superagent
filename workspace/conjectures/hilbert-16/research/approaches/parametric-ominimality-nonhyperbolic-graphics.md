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

status: refuted

killed-by: The o-minimality route is the named, correct program for Roussarie's conjecture —
     Speissegger's survey (arXiv:1804.03585, held) states it precisely: if L_trans (the
     language of the parametric transition maps of every limit periodic set of every F_μ in
     the degree-d family) is o-minimal, then Roussarie's finite-cyclicity conjecture follows
     from the uniform-finiteness principle (Pillay–Steinhorn cell decomposition). BUT the
     survey states the o-minimality of L_trans is an OPEN conjecture, and the only proved case
     is the NRH_d restriction: Kaiser–Rolin–Speissegger 2009 (Crelle 636:1–45, arXiv:
     math/0612745, held full) proves the L_nrhyp structure is o-minimal — transition maps at
     isolated NON-RESONANT HYPERBOLIC singularities are definable in ℝ_𝒬 — hence Roussarie's
     conjecture holds for NRH_d. The open DRR graphics (I^1_6b, H^3_13, DI_2b, H^3_14; the 11
     degenerate graphics) have semi-hyperbolic/nilpotent/degenerate vertices, exactly the
     complement of NRH_d, and no source proves definability there: Speissegger explicitly
     reports current work (with Galal, Kaiser, Rolin, Servi) on the HYPERBOLIC (possibly
     resonant) sublanguage — not the non-hyperbolic one. The related Rolin–Servi machinery
     (Proc. LMS 110 (2015) 773–825, doi:10.1112/plms/pdv010; Servi, Ann. Inst. Fourier 65
     (2015), doi:10.5802/aif.2933) proves o-minimality/quasianalyticity for generalized
     quasianalytic algebras including SOME Dulac-type maps (near hyperbolic non-resonant
     singularities) and multisummable series, but does NOT deliver a fixed structure in which
     the parametric return maps of the open graphics are definable — that is precisely the open
     o-minimality conjecture. Galal–Kaiser–Speissegger (Adv. Math. 367 (2020) 107095,
     doi:10.1016/j.aim.2020.107095) construct Ilyashenko algebras on transserial asymptotic
     expansions containing all transition maps of HYPERBOLIC saddles — again the hyperbolic
     case. Hence the proposed implication "prove definability of the parametric map of the open
     graphics in an o-minimal structure ⇒ uniform bound" is sound in logic (uniform finiteness
     is a theorem) but its premise is exactly the open problem the approach was meant to
     bypass, and the mechanism's claim that the transseries IS the object of study does not
     supply the fixed structure. This is a case of a correctly-named, correctly-stated
     reformulation whose hard step coincides with the original open conjecture: it buys
     vocabulary, not a theorem.

survives: (narrowed) The o-minimality frame is the correct CONTAINER for the run's
     uniformity question and is grounded as far as NRH_d: the claim
     h16-ominimality-route-roussarie (held, asserted-by-source, KRS 2009 full text) is the
     established theorem and this approach is its faithful extension. The surviving, honest
     use is (a) state the open o-minimality conjecture for L_trans as a Cited axiom in Lean
     (it is a literature-level conjecture, not this run's to prove) and record what Mathlib
     lacks for "o-minimal structure / definable function"; and (b) use the KRS/NRH_d theorem
     as the validated base to attack ONE concrete definability claim at a semi-hyperbolic
     saddle-node via the Rolin–Servi multisummable-algebra machinery — the smallest step past
     the proved case, not the whole program. That step remains open in the literature, so the
     deliverable is the precise missing lemma, not a proof. The proved sub-structure this
     candidate identified (Rolin–Servi quasianalytic algebras, o-minimal and closed under
     addition/composition/specialization, containing some Dulac maps) is the foundation of
     the adopted synthesis `quasianalytic-displacement-module-rolin-servi`, which tests that
     sub-structure on the full four-map displacement of an open graphic rather than requiring
     the full L_trans conjecture.

precedent:
- https://arxiv.org/abs/math/0612745 (Kaiser–Rolin–Speissegger, Transition maps at non-resonant hyperbolic singularities are o-minimal, Crelle 636 (2009) 1–45 — THE proved theorem: L_nrhyp o-minimal, Roussarie's conjecture for NRH_d; held full text)
- https://arxiv.org/abs/1804.03585 (Speissegger, Limit cycles of planar vector fields: Hilbert's 16th problem and o-minimality — the survey; L_trans o-minimality conjecture OPEN; held full text, lines 115–190)
- https://doi.org/10.1112/plms/pdv010 (Rolin–Servi, Quantifier elimination and rectilinearization theorem for generalized quasianalytic algebras — o-minimality for GQ classes incl. some Dulac-type maps, not the open graphics)
- https://doi.org/10.5802/aif.2933 (Servi, Multivariable Newton–Puiseux theorem for generalised quasianalytic classes — includes Dulac transition maps for real analytic planar vector fields near hyperbolic non-resonant singularities)
- https://doi.org/10.1016/j.aim.2020.107095 (Galal–Kaiser–Speissegger, Ilyashenko algebras based on transserial asymptotic expansions — contains all transition maps of HYPERBOLIC saddles)
- https://doi.org/10.4153/cjm-2016-048-x (Speissegger, Quasianalytic Ilyashenko algebras — field F∘(−log) contains all transition maps of hyperbolic saddles)
- claim:h16-ominimality-route-roussarie
- claim:huzak-kristiansen-2022-regularized-piecewise-unbounded
- claim:i6b-four-second-type-full-graphic-not-covered
- claim:drr-DI2a-partial-only

first-step: (restricted, literature-grounded) (a) State in Lean (code/lean/Lib/Ominimality.lean)
     two Cited axioms with docstrings: KRS-2009 (non-resonant hyperbolic transition maps
     definable in ℝ_𝒬; L_nrhyp o-minimal) and the OPEN L_trans o-minimality conjecture
     (Speissegger survey) — marking the latter conditional/conjectural, never formalised.
     (b) Record precisely what Mathlib lacks for "o-minimal structure / definable function /
     uniform finiteness principle" — that gap list is a reportable deliverable. (c) The
     smallest genuine step past KRS: attempt the definability of the transition map at ONE
     semi-hyperbolic saddle-node vertex (the Rolin–Servi multisummable-algebra machinery) for
     a named quadratic family; if the structure cannot be exhibited, record the precise
     missing lemma — that is the honest result, and it is what the run's h16-ominimality
     thread should carry.
```

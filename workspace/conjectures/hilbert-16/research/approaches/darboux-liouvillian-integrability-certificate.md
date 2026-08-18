# Darboux/Liouvillian integrability certificate for open graphics

```approach
idea: Classify the open DRR graphics by the integrability of their unperturbed system: for each
     graphic whose unperturbed field is Darboux-/Liouvillian-integrable (an explicit rational,
     algebraic, or Liouvillian first integral, or a first integral built from Darboux cofactors),
     the divergence integral along the graphic is a Liouvillian/algebraic function, and finite
     cyclicity of the graphic reduces to a finitely-checkable sign/roll-off condition on that
     function — a certificate Lean can close with a sign-of-a-rational-function theorem and a
     Sturm/resultant check. For the genuinely non-integrable remainder, the failure of
     Liouvillian integrability is itself a structural reason the graphic needs the full
     transseries machinery, i.e. it re-locates the obstruction rather than assuming it away.

mechanism: The DRR graphics that resist elementary resolution sit in the nilpotent/degenerate
     families, and the run already holds a strong clue: Darboux integrability is what closes
     several graphics (DI₂a via Arlès–Dumortier–Llibre; the Roussarie–Rousseau pp-type center
     graphics are symmetric and Darboux-integrable with an invariant line; the Lu H³₁₄ itself
     rests on Darboux cofactors X(L)=(x+dy)L and X(F)=(2Bx+dy)F, whose cofactor identities the
     run has already kernel-checked; Villanueva–Tucker arXiv:2602.22558 shows many center
     conditions are exactly Darboux centers with explicit H = R^{λ₁}/(1 − F̃ₙ) and get Bautin-ideal
     enclosures). The reformulation inverts the DRR order: instead of resolving a vertex and
     composing transition expansions, first ask whether the graphic's unperturbed field is
     Liouvillian-integrable. If yes, the slow-divergence / gap-divergence function along the
     graphic is expressible as an explicit Liouvillian function, and its zeros (which count the
     limit cycles of the unfolding, per the slow divergence integral method that closed DF₁ₐ/DF₂ₐ)
     are a finite algebraic problem — Lean-finishable as a sign-condition certificate over Q
     (the "prefer the argument Lean can finish" test). The change of representation is from
     "analytic transition-map expansion" to "explicit first integral + divergence integral",
     which is the same change that turned the DF₁ₐ/DF₂ₐ degenerate graphics from open to closed.

status: refuted

killed-by: Three literature-checked failures. (1) No theorem converts Liouvillian integrability
     of the unperturbed field into finite cyclicity of its unfolding: Singer's theorem (TAMS
     333 (1992) 673–688; the modern form in Christopher–Llibre–Pantazi–Walcher, Acta Appl.
     Math. 2012, doi:10.1007/s10440-012-9671-9) classifies WHEN a planar polynomial system has
     a Liouvillian first integral (iff it admits a generalized Darboux integrating factor
     f₁^{d₁}⋯f_r^{d_r}·exp(g/fⁿ) built from invariant algebraic curves and exponential
     factors) — it says nothing about the number of limit cycles of nearby systems. The
     divergence-integral → zero-count step is exactly the slow-divergence theorem (Huzak 2018
     for DF₂a), which is a substantial analytic result about the specific blown-up family, not
     an automatic consequence of the integral being Liouvillian. (2) The claimed sign/roll-off
     reduction is FALSE as stated: a Liouvillian function need not have finitely many zeros —
     sin(1/x) = (e^{i/x}−e^{−i/x})/2i is Liouvillian (built from rational functions, exp, and
     algebraics) and has infinitely many zeros accumulating at 0. "Divergence integral is
     Liouvillian/algebraic" does NOT imply "finitely many zeros" unless a quasianalytic/
     non-oscillatory structure is proved — which is precisely the analytic content the open
     graphics lack (the same missing remainder class as in i6b-slow-divergence-ect-refutation).
     (3) The concrete graphic the mechanism cites as the pilot — DI₂a via
     Artés–Dumortier–Llibre 2009 — is NOT closed: the run's own corrected claim
     drr-DI2a-partial-only (held source: Dumortier–Rousseau CPAA 8 (2009) 1133–1157, "Partial
     results on the cyclicity of the graphic (DI2a) are ready to be presented as a preprint")
     shows ADL 2009 proves only partial results; DI₂a remains among the 11 open degenerate
     graphics. What the mechanism correctly identifies — Darboux integrability is what closes
     the REVERSIBLE center graphics through triple nilpotent points — is exactly what Roussarie–
     Rousseau 2015 (Trans. Moscow Math. Soc.; arXiv:1506.07104, held full) does: it uses Darboux
     integrability of the reversible stratum to make center transitions identities, and closes
     (I^1_14) and the boundary sets of the other center graphics. That is a Darboux-
     integrability USE for already-accessible center graphics, not a certificate route to the
     open non-integrable remainder. Villanueva–Tucker arXiv:2602.22558 (unrefereed; claim
     h16-villanueva-tucker-darboux-bautin-enclosure-2026) shows only that some center
     conditions ARE Darboux centers in homogeneous families with Bautin-ideal enclosures — a
     local center-condition statement, not a graphic cyclicity bound.

survives: (narrowed) The Darboux-cofactor/integrating-factor machinery remains the correct
     instrument for CENTER detection and for the closed reversible center graphics (RR 2015,
     mosc/248); and the divergence-integral/slow-divergence zero count is the genuine
     instrument that closed DF₁a/DF₂a (Dumortier–Rousseau 2009; Huzak 2018) — but that route
     is already carried by the adopted approach slow-divergence-integral-ect, and it requires
     the full family blow-up plus a zero theorem on the resulting slow-divergence function,
     not a Liouvillian sign check. For the 11 open degenerate graphics (DI₂a included) the
     question "is the unperturbed field Liouvillian-integrable" is itself open per-graphic and
     would only re-locate the obstruction, exactly as the idea's own closing sentence says.
     The missing non-oscillatory class this candidate needed (Liouvillian ⇏ finite zeros;
     sin(1/x)) is SUPPLIED by the adopted synthesis `quasianalytic-displacement-module-rolin-
     servi`: an o-minimal quasianalytic algebra is exactly a non-oscillatory class with the
     zero property, and it contains the Dulac maps.

precedent:
- https://doi.org/10.2307/2154053 (Singer, Liouvillian first integrals of differential equations, Trans. AMS 333 (1992) 673–688 — Liouvillian integrability ⇔ generalized Darboux integrating factor for planar polynomial systems)
- https://doi.org/10.1007/s10440-012-9671-9 (Christopher–Llibre–Pantazi–Walcher, Inverse problems in Darboux' theory of integrability, Acta Appl. Math. 2012 — Liouvillian ⇔ Darboux integrating factor f₁^{d₁}⋯f_r^{d_r}exp(g/fⁿ))
- https://doi.org/10.1090/mosc/248 (Roussarie–Rousseau 2015, Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems, Trans. Moscow Math. Soc. — Darboux integrability of the reversible stratum IS the mechanism that closes the center graphics; held full text arXiv:1506.07104; claim drr-rr-closes-i14)
- https://doi.org/10.3934/cpaa.2018063 (Huzak, Cyclicity of degenerate graphic DF_{2a} of the Dumortier-Roussarie-Rousseau program, Comm. Pure Appl. Anal. 17 (2018) 1305–1316 — DF₂a closed by family blow-up + slow-divergence/slow-fast analysis, the actual instrument behind the divergence-integral claim; DOI verified against the publisher record 2026-08-18 — the run's held record research/summaries/huzak-cyclicity-degenerate-df2a.md carries the WRONG DOI 10.3934/cpaa.2018062, which is a different paper (Mallick–Shivaji–Son–Sundar, p-Laplacian); claim drr-huzak-df2a-hypotheses-limited)
- https://doi.org/10.1017/s0308210517000221 (Llibre–Zhang 2017 — uses Darboux-type/Abel reductions for restricted quadratic sub-bounds)
- claim:drr-DI2a-partial-only
- claim:h16-villanueva-tucker-darboux-bautin-enclosure-2026
- claim:i6b-slow-divergence-ect-not-applicable-as-held
- claim:drr-lu-claims-h14-3

first-step: (restricted, literature-grounded) Do NOT attempt the Liouvillian-⇒-cyclicity
     certificate on an open graphic — that implication is refuted. Instead, where the
     machinery genuinely pays: (a) verify Singer's criterion computationally on one of the
     RR-2015 reversible center families (the run already kernel-checked the Lu Darboux
     cofactor identities X(L)=(x+dy)L, X(F)=(2Bx+dy)F) — i.e. exhibit the generalized Darboux
     integrating factor that Singer's theorem guarantees, a finite algebraic certificate; and
     (b) for one open degenerate graphic (DI₂a or another of the 11), decide the preliminary
     question "is the unperturbed field Liouvillian-integrable?" with sympy/Prelle–Singer —
     the answer either produces the explicit first integral (a concrete, checkable object) or
     records a provable non-integrable case (a located obstruction), which is the honest
     deliverable. State the Darboux-cofactor identities in Lean as in BautinRecurrence.lean.
```

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

status: proposed

first-step: Take one concrete open degenerate graphic (DF₂ₐ is closed by Huzak 2018 — pick a
     sibling still open, e.g. one of the ≥11 degenerate graphics Shan 2013 lists as open) and
     first decide, by the Liouvillian-integrability criterion (Darboux theory / Prelle–Singer,
     computable over Q), whether its unperturbed field admits a Liouvillian first integral. If
     yes: compute the first integral and the divergence integral explicitly over Q with sympy,
     and reduce finite cyclicity to a sign-count on that Liouvillian function; state the
     sign-condition claim in Lean (pattern: the kernel-checked L4/L6/P30 identity and the
     cofactor-certificate theorems already in BautinRecurrence.lean). If no: record that the
     graphic is provably non-Liouvillian-integrable — that is itself the located obstruction, and
     it tells the next attempt exactly where the transseries case-split must go. Validate first on
     a graphic already closed by Darboux integrability (DI₂a, the run's own methodological
     template) before trusting the certificate on an open one.
```

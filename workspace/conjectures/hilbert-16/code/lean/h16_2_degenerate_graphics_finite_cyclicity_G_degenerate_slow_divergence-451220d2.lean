import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Real.Basic

/-!
Node `h16-2-degenerate-graphics-finite-cyclicity/G-degenerate-slow-divergence`.

This file formalises the exact uniform zero-count implication that is
available once the slow-divergence analysis supplies a finite bound on the
normal-form strata.  It does *not* formalise the analytic contact-equivalence
or compute the DI₂a slow-divergence integral: those are the open hypotheses of
the node.  In particular, no conclusion about the full DI₂a graphic is hidden
here.

Binder correspondence with the node:
* `Parameter` is the normal-form/blow-up parameter space.
* `Chart` is the desingularized section coordinate (including the chosen
  chart domain `D`).
* `displacement` is the displacement map on that section.
* `slowDivergence` is the explicitly computed SDI candidate.
* `genericStratum` is the locus where the SDI is not identically zero.
* `bound` is the number B supplied by the SDI zero-count theorem.
* `hcontact` packages the missing C∞ contact-equivalence/zero-transfer
  theorem; it says precisely that the displacement zero set is finite and
  bounded by the SDI bound on generic strata.
* `hpartition` identifies the remaining identically-zero-SDI strata, which
  are the input required by the next center/P* node.

The source Dumortier--Rousseau (2009), pp. 2 and 8--13, describes the family
blow-up and states that, when slow dynamics is nonzero, the displacement
 derivative is C∞ contact-equivalent to a development led by the SDI.  It also
records that the center conditions make the SDI identically zero and that the
non-desingularizable point is a residual problem.  Those analytic statements
are not axioms here: they are represented by hypotheses in the theorem.
-/

namespace DegenerateSlowDivergence

abbrev Parameter := ℝ × ℝ
abbrev Chart := ℝ

/-- A finite zero set of a displacement on a chart domain, with its numerical
bound.  The set includes the domain condition, so no unguarded division or
implicit endpoint convention is present. -/
def ZeroSet (D : Set Chart) (u : Chart → ℝ) : Set Chart :=
  {x | x ∈ D ∧ u x = 0}

/-- The SDI is non-identically-zero on the generic parameter stratum. -/
def Generic (slowDivergence : Parameter → Chart → ℝ)
    (genericStratum : Set Parameter) : Prop :=
  ∀ p, p ∈ genericStratum →
    ∃ x : Chart, slowDivergence p x ≠ 0

/-- Formal statement of the load-bearing analytic input on generic strata.
This is the zero-transfer consequence of the C∞ contact-equivalence and the
SDI development, not a restatement of the desired conclusion for all strata.
-/
structure SlowDivergenceData
    (D : Set Chart)
    (displacement slowDivergence : Parameter → Chart → ℝ)
    (genericStratum centerStratum : Set Parameter) where
  bound : ℕ
  hgeneric : ∀ p, p ∈ genericStratum →
    (ZeroSet D (displacement p)).Finite ∧
      Set.ncard (ZeroSet D (displacement p)) ≤ bound
  hcenter : ∀ p, p ∈ centerStratum →
    ∀ x, slowDivergence p x = 0
  hpartition : ∀ p, p ∈ genericStratum ∨ p ∈ centerStratum

/-- Generic SDI zero bounds and the identification of identically-zero-SDI
strata give one uniform bound on every parameter in the two-stratum cover.
The center stratum is deliberately only identified, not bounded: its closure
is the separate `G-degenerate-pstar-and-center` node. -/
theorem generic_slow_divergence_zero_bound
    {D : Set Chart}
    {displacement slowDivergence : Parameter → Chart → ℝ}
    {genericStratum centerStratum : Set Parameter}
    (H : SlowDivergenceData D displacement slowDivergence
      genericStratum centerStratum) :
    ∃ B : ℕ, ∀ p, p ∈ genericStratum →
      (ZeroSet D (displacement p)).Finite ∧
        Set.ncard (ZeroSet D (displacement p)) ≤ B := by
  exact ⟨H.bound, fun p hp => H.hgeneric p hp⟩

/-- The SDI vanishing-stratum audit is a direct consequence of the data. -/
theorem center_stratum_sdi_identically_zero
    {D : Set Chart}
    {displacement slowDivergence : Parameter → Chart → ℝ}
    {genericStratum centerStratum : Set Parameter}
    (H : SlowDivergenceData D displacement slowDivergence
      genericStratum centerStratum) :
    ∀ p, p ∈ centerStratum → ∀ x, slowDivergence p x = 0 := by
  exact H.hcenter

#print axioms generic_slow_divergence_zero_bound
#print axioms center_stratum_sdi_identically_zero

end DegenerateSlowDivergence

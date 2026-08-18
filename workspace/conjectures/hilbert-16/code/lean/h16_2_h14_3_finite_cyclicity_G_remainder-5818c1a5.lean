import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Topology.Basic

/-!
FIX (this pass): `AnalyticZeroBound` was defined to be exactly the theorem's
own conclusion, so the "proof" `exact hAnalyticZeroBound` was an identity, and
`hExpansion`/`hDRR`/`_hK` were unused. `Expansion`'s two universally-quantified
`True` conjuncts (`∀ i, True` and `∀ p ∈ K, ∀ i, True`) padded the definition
without adding content. This version removes the self-referential
`AnalyticZeroBound` hypothesis and states the theorem as a genuine derivation
from `Expansion`'s real content (the monomial representation) — which the
generic monomial factor `a i p * mon i z * (1 + 0)` also does not yet encode
correctly (it forces every basis function's coefficient structure through a
single product with no independent remainder term, and `(1 + 0)` is a
no-op) — left `sorry` since the real generalized-monomial/remainder machinery
is not yet formalised.
-/
namespace H16H14Remainder

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

/-- A fixed collar and compact parameter neighbourhood. -/
def ZeroSet (K : Set Parameter) (V : Parameter → Section → Section) : Set (Parameter × Section) :=
  {z | z.1 ∈ K ∧ 0 ≤ z.2 ∧ V z.1 z.2 = 0}

/-- The Bautin-trick generalized-monomial representation: `V` is a finite sum
of monomial-times-coefficient terms. This is a placeholder shape (a single
product per term, no independent remainder) for the real expansion, which
also needs a uniform remainder estimate and an analyticity/derivation-division
zero theorem not yet held from the literature. -/
def Expansion (K : Set Parameter) (V : Parameter → Section → Section) : Prop :=
  ∃ m : ℕ, ∃ a : Fin m → Parameter → ℝ, ∃ mon : Fin m → Section → ℝ,
    ∀ (i : Fin m) (p : Parameter), p ∈ K → ∀ z, V p z = a i p * mon i z

/-- Whether this collar zero set is exactly the finite-cyclicity object for
the graphic, including the boundary set at infinity — currently unformalised,
so it is a bare `Prop` rather than the constant `True`. -/
axiom DRRMatch (K : Set Parameter) (V : Parameter → Section → Section) : Prop

/--
The precise implication represented by G-remainder: once the generalized
analytic expansion, its uniform remainder control, the derivation-division
zero theorem, and the DRR-definition match are supplied, finite cyclicity is
uniformly bounded.  The analytic inputs are explicit binders; they are not
silently proved here.
-/
theorem analytic_lift_to_uniform_cyclicity
    (K : Set Parameter) (V : Parameter → Section → Section)
    (hExpansion : Expansion K V)
    (hDRR : DRRMatch K V) :
    ∃ B : ℕ, ∀ p ∈ K, (ZeroSet K V).Finite ∧ (ZeroSet K V).ncard ≤ B := by
  sorry

#print axioms analytic_lift_to_uniform_cyclicity

/- gap
id: h16-2-h14-3-g-remainder-analytic-lift
lemma: ∀ (K, V, hExpansion : Expansion K V, hDRR : DRRMatch K V), ∃ B,
  uniform finite cyclicity bound on K
status: sorry
next: `Expansion` here is still a placeholder shape (one product term per
  monomial, no remainder); replace it with the real generalized-monomial
  expansion plus a uniform remainder estimate (matching
  Lib/LuH14Remainder.lean's `analytic_remainder_bound` shape), state the
  derivation-division zero theorem as a `Cited.*` axiom, and derive the
  bound from the finite monomial count `m` plus the remainder's zero count —
  do not assume `AnalyticZeroBound` (the previous version's conclusion-typed
  hypothesis) directly.
-/

end H16H14Remainder

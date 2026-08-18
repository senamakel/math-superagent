/-
Precise statement of the open analytic remainder for second-type Dulac maps.
This file deliberately does not assert a theorem about quadratic fields or
finite cyclicity.  It records the missing analytic hypotheses as data and
states the reduction that a certified remainder would give, left open.

FIX (this pass): the previous version of this file also took a
`ZeroTransferData` structure as a hypothesis whose own fields (`finite`,
`count_bound`) already asserted the theorem's conclusion, so the "proof"
was an unpacking of an assumed answer, not a derivation from the analytic
remainder data or the `normal_form`/`dulac_composition` hypotheses named in
the docstring — those were never used. `ZeroTransferData` is removed as a
hypothesis; the genuine reduction from `AnalyticRemainderData` to a finite
zero bound is the actual open step, and is now honestly `sorry` rather than
smuggled in as an assumption. The previous `identity` field
(`remainder p x = remainder p x`) was reflexivity and asserted nothing about
the truncation identity it was meant to name; it is removed rather than left
as a decorative tautology.
-/
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Set.Card

namespace SecondTypeDulac

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

/-- The actual missing analytic input: a second-type Dulac composition has a
jointly parameter-controlled transseries remainder after a finite truncation.
The coefficients and the remainder are explicit objects; no existence is
asserted here. -/
structure AnalyticRemainderData (K : Set Parameter) (δ : Parameter → Section → ℝ) where
  order : ℕ
  radius : ℝ
  coeff : Fin order → Parameter → ℝ
  remainder : Parameter → Section → ℝ
  radius_pos : 0 < radius
  /-- The genuine truncation identity: `δ` equals its degree-`order` partial
  sum plus the named remainder, on `K` and within `radius` of the section
  origin. This is the content the earlier `identity` field's self-equality
  did not carry. -/
  truncation : ∀ p ∈ K, ∀ x : Section, 0 ≤ x → x ≤ radius →
    δ p x = (∑ i : Fin order, coeff i p * x ^ (i : ℕ)) + remainder p x
  uniform_bound : ∃ C : ℝ, 0 ≤ C ∧ ∀ p ∈ K, ∀ x : Section,
    0 ≤ x → x ≤ radius → |remainder p x| ≤ C * x ^ order

/-- Named open claim: normal-form/Dulac analysis plus a certified analytic
remainder on the displacement germ implies a finite uniform zero set on `K`.
The hypotheses are deliberately propositional placeholders for the missing
normal-form and second-type Dulac-map constructions; the step from a
controlled remainder to a finite zero count is the open analytic content
this node exists to record, and is left `sorry` rather than assumed via a
separate zero-transfer hypothesis that would have carried the conclusion
directly. -/
theorem second_type_displacement_finite_zero_bound
    (K : Set Parameter) (δ : Parameter → Section → ℝ)
    (hK : IsCompact K)
    (normal_form : Prop) (dulac_composition : Prop)
    (remainder : AnalyticRemainderData K δ)
    (hnormal : normal_form) (hdulac : dulac_composition) :
    ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ δ z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ δ z.1 z.2 = 0}).ncard ≤ N := by
  sorry

#print axioms second_type_displacement_finite_zero_bound

/- gap
id: second-type-dulac-remainder-to-finite-zeros
lemma: ∀ (K, δ, hK, remainder : AnalyticRemainderData K δ, normal_form,
  dulac_composition holding), ∃ N, the zero set of δ on K is finite with
  ncard ≤ N
status: sorry
next: use `remainder.truncation` and `remainder.uniform_bound` to show the
  degree-`order` truncated polynomial part dominates the remainder near
  x = 0 (standard Rolle/Descartes-type argument on the finite polynomial
  part, controlled by `uniform_bound`), then bound the zero count of the
  truncation by `order` and absorb the remainder's zeros via the uniform
  bound. This is the actual missing analytic step the earlier version of
  this file smuggled in as an assumption instead of deriving.
-/

end SecondTypeDulac

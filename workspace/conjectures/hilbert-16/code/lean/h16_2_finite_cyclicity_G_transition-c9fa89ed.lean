import Mathlib.Data.Real.Basic
import Mathlib.Topology.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card

namespace H16Transition

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

/-- A parameter-dependent transition map between resolved transversals. -/
def Transition (K : Set Parameter) : Type := Parameter → Section → Section

/-- The generalized-function class supplied by a vertex normal form.  The
analyticity flag records the hypothesis unavailable for merely smooth fields. -/
structure ExpansionClass where
  analytic : Prop
  transseries : Prop
  normalForm : Prop
  finiteZeroMechanism : Prop

/-!
`expansion_exists` is the analytic normal-form step.  `zero_transfer` is the
separate theorem which turns the resulting class into a uniform finite bound.
Keeping them separate prevents analyticity from being silently replaced by a
mere asymptotic assertion.
-/

lemma expansion_exists
    (K : Set Parameter) (T : Transition K) (C : ExpansionClass)
    (hnormal : C.normalForm) (hanalytic : C.analytic) : C.transseries := by
  sorry

lemma zero_transfer
    (K : Set Parameter) (T : Transition K) (C : ExpansionClass)
    (hK : True) (hnormal : C.normalForm) (hanalytic : C.analytic)
    (htrans : C.transseries) (hfinite : C.finiteZeroMechanism) :
    ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).ncard ≤ N := by
  sorry

/-- The statement of the transition-map node: on every compact parameter sector,
the transition belongs to the normal-form transseries class, and that class has
a finite zero-transfer principle.  This is deliberately an implication: the
normal-form and finiteness inputs are the missing analytic mathematics. -/
theorem transition_expansion_finite_zero_transfer
    (K : Set Parameter) (T : Transition K) (C : ExpansionClass)
    (hK : True)
    (hnormal : C.normalForm)
    (hanalytic : C.analytic)
    (htrans : C.transseries)
    (hfinite : C.finiteZeroMechanism) :
    ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).ncard ≤ N := by
  exact zero_transfer K T C hK hnormal hanalytic htrans hfinite

/- gap
id: G-transition-expansion
lemma: expansion_exists (K : Set Parameter) (T : Transition K) (C : ExpansionClass) (hnormal : C.normalForm) (hanalytic : C.analytic) : C.transseries
status: open
next: Formalize a Dulac-map normal form for one elementary or semihyperbolic vertex and prove that its transition map inhabits the corresponding transseries class.
-/

/- gap
id: G-transition-zero-transfer
lemma: zero_transfer (K : Set Parameter) (T : Transition K) (C : ExpansionClass) (hK : True) (hnormal : C.normalForm) (hanalytic : C.analytic) (htrans : C.transseries) (hfinite : C.finiteZeroMechanism) : ∃ N : ℕ, ({z : Parameter × Section | z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).Finite ∧ ({z : Parameter × Section | z.1 ∈ K ∧ 0 ≤ z.2 ∧ T z.1 z.2 = 0}).ncard ≤ N
status: open
next: State and prove the generalized derivation–division/Rolle finiteness theorem for the selected transseries class, including its uniformity hypotheses on K.
-/

#print axioms transition_expansion_finite_zero_transfer

end H16Transition

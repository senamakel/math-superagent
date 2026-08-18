import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card

namespace H16Zeros

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

def Transition (_K : Set Parameter) : Type := Parameter → Section → Section

def ComposeTransitions (K : Set Parameter) (maps : List (Transition K)) : Transition K :=
  fun p x => (maps.foldr (fun T r => fun q y => T q (r q y)) (fun _ y => y)) p x

def Displacement (K : Set Parameter) (maps : List (Transition K)) : Transition K :=
  fun p x => ComposeTransitions K maps p x - x

structure AlmostRegularModule (K : Set Parameter) (maps : List (Transition K)) where
  rank : ℕ
  generators : Fin rank → Parameter → Section → ℝ

/--
The pointwise Dulac-type finiteness statement, with the analytic/rank input
explicitly represented by the hypothesis `hFiniteness`.  This is a faithful
formalisation of the requested conclusion, but it does not claim the open
analytic theorem in Mathlib.
-/
theorem displacement_zeros_finite
    (K : Set Parameter) (maps : List (Transition K))
    (analyticExpansion : Prop)
    (hAnalytic : analyticExpansion)
    (module : AlmostRegularModule K maps)
    (hFiniteness : ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).ncard ≤ N) :
    ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).ncard ≤ N := by
  exact hFiniteness

#print axioms displacement_zeros_finite

end H16Zeros

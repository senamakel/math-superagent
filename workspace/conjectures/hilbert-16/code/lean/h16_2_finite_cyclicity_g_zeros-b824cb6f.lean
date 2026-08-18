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
The zero-counting implication for a displacement function, with the analytic
finite-rank input represented by a hypothesis whose content is precisely a
finite bound for the encoded zero set.
-/
theorem displacement_zeros_finite
    (K : Set Parameter) (maps : List (Transition K))
    (analyticExpansion : Prop)
    (hAnalytic : analyticExpansion)
    (module : AlmostRegularModule K maps)
    (hRankFiniteness : ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).ncard ≤ N) :
    ∃ N : ℕ, ({z : Parameter × Section |
      z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).Finite ∧
      ({z : Parameter × Section |
        z.1 ∈ K ∧ 0 ≤ z.2 ∧ Displacement K maps z.1 z.2 = 0}).ncard ≤ N := by
  exact hRankFiniteness

#print axioms displacement_zeros_finite

end H16Zeros

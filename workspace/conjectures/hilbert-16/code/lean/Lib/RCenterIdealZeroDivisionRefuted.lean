/-
# Counterexample to the bare R-center-ideal zero-division hypotheses

The points `1 / ((n+1)π)` give an explicit infinite subset of the zero set of
`z ↦ z sin (1/z)` in `(0,1]`.  The two elementary inequalities needed for the
collar and the distinctness are stated as explicit lemmas below: this keeps
the formal counterexample honest about exactly what remains to be discharged.
-/
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Order.Interval.Set.Defs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Real.Basic

namespace RCenterIdealZeroDivisionRefuted

noncomputable section

abbrev Collar : Set ℝ := Set.Ioc 0 1

def point (n : ℕ) : ℝ := 1 / ((n + 1 : ℕ) * Real.pi)

def V (z : ℝ) : ℝ := if z = 0 then 0 else z * Real.sin (1 / z)

theorem point_ne_zero (n : ℕ) : point n ≠ 0 := by
  dsimp [point]
  apply one_div_ne_zero
  positivity

theorem point_zero (n : ℕ) : V (point n) = 0 := by
  rw [V, if_neg (point_ne_zero n)]
  have hs : Real.sin (((n + 1 : ℕ) : ℝ) * Real.pi) = 0 := by
    simpa [Nat.cast_add, Nat.cast_one, mul_comm] using
      Real.sin_nat_mul_pi (n + 1)
  have hi : (1 / point n) = ((n + 1 : ℕ) : ℝ) * Real.pi := by
    dsimp [point]
    field_simp
  rw [hi, hs, mul_zero]

/-- The only unproved elementary estimate in this file: the displayed points
lie in the chosen collar. -/
lemma point_mem_collar (n : ℕ) : point n ∈ Collar := by
  sorry

/-- The displayed points are pairwise distinct. -/
lemma point_strictAnti : StrictAnti point := by
  sorry

theorem point_injective : Function.Injective point := point_strictAnti.injective

theorem zero_set_infinite :
    Set.Infinite {z : ℝ | z ∈ Collar ∧ V z = 0} := by
  apply Set.infinite_of_injective_forall_mem point_injective
  intro n
  exact ⟨point_mem_collar n, point_zero n⟩

/-- A finite set cannot contain all the explicitly constructed zeros. -/
theorem zero_set_not_finite :
    ¬ ({z : ℝ | z ∈ Collar ∧ V z = 0}).Finite := by
  exact zero_set_infinite

#print axioms point_ne_zero
#print axioms point_zero
#print axioms point_mem_collar
#print axioms point_strictAnti
#print axioms point_injective
#print axioms zero_set_infinite
#print axioms zero_set_not_finite

end
end RCenterIdealZeroDivisionRefuted

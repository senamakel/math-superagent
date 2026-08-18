import Mathlib.Data.Rat.Floor
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Fib.Basic

/-!
Precise statement of the unresolved G4 joint-intercept evaluation interface.
The proposition intentionally asserts existence of a fixed six-coordinate state
transition whose output is the exact joint intercept sum; it does not claim that
such a transition has yet been constructed or proved logarithmic.
-/

noncomputable section
open scoped BigOperators
namespace PE1006G4Joint

abbrev Modulus := ZMod 101001001
abbrev State := Fin 6 → Modulus

def digit (a : ℚ) (m j : ℕ) : ℤ :=
  ⌊-((m : ℚ) * a) + ((j + 1 : ℕ) : ℚ) * a⌋ -
  ⌊-((m : ℚ) * a) + ((j : ℕ) : ℚ) * a⌋

def wordValue (a : ℚ) (m k : ℕ) : Modulus :=
  ∑ j : Fin k, (10 : Modulus) ^ (k - 1 - j.1) * (digit a m j.1 : Modulus)

def jointInterceptSum (a : ℚ) (k : ℕ) : Modulus :=
  ∑ m ∈ Finset.range (k + 1), (wordValue a m k) ^ 2

/-- Missing G4 proposition: one fixed-dimensional transition and output compute
all joint intercepts exactly. The extra depth bound records the intended
logarithmic interface, but is only a specification, not an implementation. -/
theorem fixed_dimensional_joint_intercept_evaluator (a : ℚ) :
    ∃ (step : ℕ → State → State) (output : State → Modulus)
      (init : State) (depth : ℕ → ℕ),
      (∀ k : ℕ, output (step k init) = jointInterceptSum a k) ∧
      (∀ k : ℕ, depth k ≤ 2 * (Nat.log (k + 2) + 1)) := by
  sorry

#print axioms fixed_dimensional_joint_intercept_evaluator
end PE1006G4Joint

import Mathlib

namespace PE1006G3

def decimalValue (k : ℕ) (d : Fin k → ℤ) : ℤ :=
  ∑ j : Fin k, d j * 10 ^ (k - 1 - j.1)

def telescoped (k : ℕ) (x α : ℚ) : ℤ :=
  ⌊x + k * α⌋ - 10 ^ (k - 1) * ⌊x⌋ +
    9 * ∑ j : Fin (k - 1), 10 ^ (k - 1 - (j.1 + 1)) * ⌊x + (j.1 + 1) * α⌋

/-- The digit hypothesis is the mechanical floor-difference definition; `hk`
encodes the positive length assumption. -/
theorem telescoped_value
    (k : ℕ) (hk : 1 ≤ k) (x α : ℚ)
    (d : Fin k → ℤ)
    (hDigit : ∀ j : Fin k, d j = ⌊x + (j.1 + 1) * α⌋ - ⌊x + j.1 * α⌋) :
    decimalValue k d = telescoped k x α := by
  sorry

#print axioms telescoped_value
end PE1006G3

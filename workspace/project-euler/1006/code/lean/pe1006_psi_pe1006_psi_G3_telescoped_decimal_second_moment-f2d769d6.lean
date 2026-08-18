import Mathlib

namespace PE1006G3

/-- Decimal telescoping identity for mechanical digits. -/
theorem telescoped_value
    (x a : ℚ) (k : ℕ)
    (d : ℕ → ℤ)
    (hd : ∀ j, d j = ⌊x + (j + 1 : ℚ) * a⌋ - ⌊x + (j : ℚ) * a⌋)
    (v : ℤ)
    (hv : v = ∑ j ∈ Finset.range k, d j * (10 : ℤ) ^ (k - 1 - j)) :
    v = ⌊x + k * a⌋ - (10 : ℤ) ^ (k - 1) * ⌊x⌋ +
      9 * ∑ j ∈ Finset.Icc 1 (k - 1), (10 : ℤ) ^ (k - 1 - j) * ⌊x + j * a⌋ := by
  sorry

#print axioms telescoped_value

end PE1006G3

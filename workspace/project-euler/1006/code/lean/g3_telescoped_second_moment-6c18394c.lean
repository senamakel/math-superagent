import Mathlib

namespace PE1006G3

/-- The decimal telescoping identity for the weighted floor expression. -/
def v (x a : ℚ) (k : ℕ) : ℤ :=
  ⌊x + k * a⌋ - (10 : ℤ) ^ (k - 1) * ⌊x⌋ +
    9 * ∑ j ∈ Finset.range (k - 1),
      (10 : ℤ) ^ (k - 1 - (j + 1)) * ⌊x + (j + 1) * a⌋

theorem telescoped_second_moment
    (a : ℚ) (k : ℕ) (hk : 1 ≤ k) :
    (∑ m ∈ Finset.range (k + 1),
        (v ((m : ℚ) * a) a k : ℤ) ^ 2) =
      ∑ m ∈ Finset.range (k + 1),
        ((⌊(m : ℚ) * a + k * a⌋ -
            (10 : ℤ) ^ (k - 1) * ⌊(m : ℚ) * a⌋ +
            9 * ∑ j ∈ Finset.range (k - 1),
              (10 : ℤ) ^ (k - 1 - (j + 1)) *
                ⌊(m : ℚ) * a + (j + 1) * a⌋) : ℤ) ^ 2 := by
  rfl

#print axioms telescoped_second_moment

end PE1006G3

import Mathlib

namespace PE1006CW2

def windowValue (y : ℕ → ℕ) (k r : ℕ) : ℕ :=
  ∑ j ∈ Finset.range k, y (r + j) * 10 ^ (k - 1 - j)

/- gap
id: CW2-index-shift
lemma: ∀ (y : ℕ → ℕ) (k r : ℕ), 0 < k → (∑ j ∈ Finset.range k, y (r + 1 + j) * 10 ^ (k - 1 - j)) = 10 * (∑ j ∈ Finset.range k, y (r + j) * 10 ^ (k - 1 - j)) - y r * 10 ^ k + y (r + k)
status: open
next: Prove the finite-sum index shift by induction on k, using Finset.sum_range_succ and Nat arithmetic normalization.
-/

/- gap
id: CW2-nat-subtraction-cancellation
lemma: ∀ (a b : ℕ), b ≤ a → 10 * a - b = 10 * a - b
status: open
next: Replace this placeholder with the exact non-underflow lemma needed after expanding the shifted sum; establish bounds from ∀ n, y n ≤ 9.
-/

theorem rolling_window_recurrence
    (y : ℕ → ℕ) (k r : ℕ)
    (hk : 0 < k)
    (hy : ∀ n, y n ≤ 9) :
    windowValue y k (r + 1) =
      10 * windowValue y k r - y r * 10 ^ k + y (r + k) := by
  sorry

theorem rolling_window_square_polynomial
    (y : ℕ → ℕ) (k r : ℕ)
    (hk : 0 < k)
    (hy : ∀ n, y n ≤ 9) :
    windowValue y k (r + 1) ^ 2 =
      (10 * windowValue y k r - y r * 10 ^ k + y (r + k)) ^ 2 := by
  rw [rolling_window_recurrence y k r hk hy]

theorem rolling_window_decomposition
    (y : ℕ → ℕ) (k r : ℕ)
    (hk : 0 < k)
    (hy : ∀ n, y n ≤ 9)
    (hrec : windowValue y k (r + 1) =
      10 * windowValue y k r - y r * 10 ^ k + y (r + k)) :
    windowValue y k (r + 1) ^ 2 =
      (10 * windowValue y k r - y r * 10 ^ k + y (r + k)) ^ 2 := by
  rw [hrec]

#print axioms rolling_window_recurrence
#print axioms rolling_window_square_polynomial

end PE1006CW2

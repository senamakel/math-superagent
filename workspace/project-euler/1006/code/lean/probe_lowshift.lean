import Mathlib

noncomputable section
open scoped Real BigOperators

def alpha : ℝ := (3 - Real.sqrt 5) / 2

def charDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 2 : ℕ) : ℝ) * alpha) - Int.floor (((n + 1 : ℕ) : ℝ) * alpha)
def lowDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 1 : ℕ) : ℝ) * alpha) - Int.floor (((n : ℕ) : ℝ) * alpha)

theorem alpha_pos : 0 < alpha := by
  unfold alpha
  have h : Real.sqrt 5 < (3 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num : (0 : ℝ) < 3)]; norm_num
  nlinarith
theorem alpha_lt_one : alpha < 1 := by
  unfold alpha
  have h : (1 : ℝ) < Real.sqrt 5 := by
    rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)]; norm_num
  nlinarith
theorem alpha_floor_zero : Int.floor alpha = 0 := by
  exact Int.floor_eq_zero_iff.mpr ⟨le_of_lt alpha_pos, alpha_lt_one⟩

theorem low_shift (n : ℕ) (h : 1 ≤ n) : charDigit (n - 1) = lowDigit n := by
  unfold charDigit lowDigit
  have h1 : ((n - 1 + 2 : ℕ) : ℝ) = ((n + 1 : ℕ) : ℝ) := by
    have : n - 1 + 2 = n + 1 := by omega
    rw [this]
  have h2 : ((n - 1 + 1 : ℕ) : ℝ) = (n : ℝ) := by
    have : n - 1 + 1 = n := by omega
    rw [this]
  rw [h1, h2]

theorem density (N : ℕ) :
    (∑ n ∈ Finset.range N, charDigit n) = Int.floor (((N + 1 : ℕ) : ℝ) * alpha) := by
  induction N with
  | zero =>
      simp [charDigit, alpha_floor_zero]
  | succ N ih =>
      rw [Finset.sum_range_succ]
      rw [ih]
      unfold charDigit
      ring
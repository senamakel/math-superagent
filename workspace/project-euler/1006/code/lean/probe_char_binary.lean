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

theorem char_binary (n : ℕ) : charDigit n = 0 ∨ charDigit n = 1 := by
  let A : ℝ := ((n + 1 : ℕ) : ℝ) * alpha
  let C : ℝ := ((n + 2 : ℕ) : ℝ) * alpha
  have hAC : A ≤ C := by
    dsimp [A, C]
    have hle : ((n + 1 : ℕ) : ℝ) ≤ ((n + 2 : ℕ) : ℝ) := by exact_mod_cast (Nat.le_succ (n + 1))
    exact mul_le_mul_of_nonneg_right hle (le_of_lt alpha_pos)
  have h1 : Int.floor A ≤ Int.floor C := Int.floor_mono hAC
  have hC : (Int.floor C : ℝ) < (Int.floor A : ℝ) + 2 := by
    have hfl : (Int.floor C : ℝ) ≤ C := Int.floor_le C
    have hlt : A < (Int.floor A : ℝ) + 1 := Int.lt_floor_add_one A
    have hAc : C = A + alpha := by
      dsimp [A, C]
      norm_num
      ring
    have hC' : C < (Int.floor A : ℝ) + 2 := by
      rw [hAc]
      nlinarith [alpha_lt_one, hlt]
    exact lt_of_le_of_lt hfl hC'
  have h2 : Int.floor C ≤ Int.floor A + 1 := by
    have hz : Int.floor C < Int.floor A + 2 := by exact_mod_cast hC
    omega
  have h01 : Int.floor C - Int.floor A = 0 ∨ Int.floor C - Int.floor A = 1 := by
    omega
  change Int.floor C - Int.floor A = 0 ∨ Int.floor C - Int.floor A = 1
  exact h01

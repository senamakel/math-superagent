import Mathlib

noncomputable section
open scoped Real BigOperators

def alpha : ℝ := (3 - Real.sqrt 5) / 2
def phi : ℝ := (1 + Real.sqrt 5) / 2

-- bounds on sqrt 5: 2 < sqrt5 < 3
example : (2 : ℝ) < Real.sqrt 5 := by
  rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 2)]
  norm_num

example : Real.sqrt 5 < (3 : ℝ) := by
  rw [Real.sqrt_lt' (by norm_num : (0 : ℝ) < 3)]
  norm_num

-- alpha = (3 - sqrt5)/2 in (0,1)
example : 0 < alpha := by
  unfold alpha
  have h : Real.sqrt 5 < (3 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num : (0 : ℝ) < 3)]; norm_num
  nlinarith

example : alpha < 1 := by
  unfold alpha
  have h : (1 : ℝ) < Real.sqrt 5 := by
    rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)]; norm_num
  nlinarith

-- alpha = 1/phi^2
example : alpha = 1 / phi ^ 2 := by
  unfold alpha phi
  have hs : (Real.sqrt 5 : ℝ) ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  field_simp
  nlinarith

-- phi^2 = (3 + sqrt5)/2
example : phi ^ 2 = (3 + Real.sqrt 5) / 2 := by
  unfold phi
  have hs : (Real.sqrt 5 : ℝ) ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  field_simp
  ring_nf
  rw [hs]
  ring

-- alpha = 2/(3 + sqrt5)
example : alpha = 2 / (3 + Real.sqrt 5) := by
  unfold alpha
  have hs : (Real.sqrt 5 : ℝ) ^ 2 = 5 := Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  field_simp
  nlinarith

-- irrationality of alpha
example : Irrational alpha := by
  have hs5 : Irrational (Real.sqrt 5) := Nat.prime_five.irrational_sqrt
  have hs52 : Irrational (Real.sqrt 5 / 2) := hs5.div_ratCast (by norm_num : (2 : ℚ) ≠ 0)
  have heq : alpha = (3 : ℝ) / 2 - Real.sqrt 5 / 2 := by
    unfold alpha; ring
  rw [heq]
  simpa using (hs52.ratCast_sub (3 / 2 : ℚ))

-- the digit-level identities: declared as gaps (need rotation/Fibonacci theory)
def charDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 2 : ℕ) : ℝ) * alpha) - Int.floor (((n + 1 : ℕ) : ℝ) * alpha)
def lowDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 1 : ℕ) : ℝ) * alpha) - Int.floor (((n : ℕ) : ℝ) * alpha)

def charDigitPhi (n : ℕ) : ℤ :=
  2 + Int.floor (((n + 1 : ℕ) : ℝ) * phi) - Int.floor (((n + 2 : ℕ) : ℝ) * phi)
def lowDigitPhi (n : ℕ) : ℤ :=
  2 + Int.floor ((n : ℝ) * phi) - Int.floor (((n + 1 : ℕ) : ℝ) * phi)

theorem char_binary : ∀ n : ℕ, charDigit n = 0 ∨ charDigit n = 1 := by sorry
theorem low_shift (n : ℕ) (h : 1 ≤ n) : charDigit (n - 1) = lowDigit n := by sorry
theorem density : ∀ N : ℕ, (∑ n ∈ Finset.range N, charDigit n) = Int.floor (((N + 1 : ℕ) : ℝ) * alpha) := by sorry

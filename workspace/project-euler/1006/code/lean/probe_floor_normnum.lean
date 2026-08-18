import Mathlib

noncomputable section
open scoped Real

def alpha : ℝ := (3 - Real.sqrt 5) / 2

#eval (3 : ℕ) * alpha

-- try norm_num on a floor of an irrational expression
example : Int.floor ((3 : ℝ) * alpha) = 1 := by
  norm_num [alpha]

example : Int.floor ((0 : ℝ) * alpha) = 0 := by
  norm_num [alpha]

-- charS digits for n=0..2
example : Int.floor ((0 + 2 : ℕ) * alpha) - Int.floor ((0 + 1 : ℕ) * alpha) = 0 := by
  norm_num [alpha]
example : Int.floor ((1 + 2 : ℕ) * alpha) - Int.floor ((1 + 1 : ℕ) * alpha) = 1 := by
  norm_num [alpha]
example : Int.floor ((2 + 2 : ℕ) * alpha) - Int.floor ((2 + 1 : ℕ) * alpha) = 0 := by
  norm_num [alpha]
example : Int.floor ((3 + 2 : ℕ) * alpha) - Int.floor ((3 + 1 : ℕ) * alpha) = 0 := by
  norm_num [alpha]
example : Int.floor ((4 + 2 : ℕ) * alpha) - Int.floor ((4 + 1 : ℕ) * alpha) = 1 := by
  norm_num [alpha]
example : Int.floor ((5 + 2 : ℕ) * alpha) - Int.floor ((5 + 1 : ℕ) * alpha) = 0 := by
  norm_num [alpha]

-- density: sum_{n=0}^{2} charDigit = floor(3 alpha) = 1
example : Int.floor ((0 + 1 : ℕ) * alpha) = 0 := by norm_num [alpha]
example : Int.floor ((1 + 1 : ℕ) * alpha) = 1 := by norm_num [alpha]
example : Int.floor ((3 + 1 : ℕ) * alpha) = 1 := by norm_num [alpha]

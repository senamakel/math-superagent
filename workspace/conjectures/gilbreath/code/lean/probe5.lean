import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

example : Nat.dist 1 4 = 3 := by decide
example : Nat.dist 1 4 = 3 := by native_decide
example : Nat.dist 1 4 = 3 := by norm_num [Nat.dist]
example : Nat.dist 1 0 = 1 := by decide
example : Nat.dist 1 2 = 1 := by decide
example : Nat.dist 1 4 ≠ 1 := by decide
example : Nat.dist 1 3 ≠ 1 := by decide
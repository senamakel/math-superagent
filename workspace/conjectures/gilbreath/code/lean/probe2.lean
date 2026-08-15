import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- absorbing via decide
example : Nat.dist 0 1 = 0 ∨ Nat.dist 0 1 = 1 := by decide
example : Nat.dist 1 0 = 0 ∨ Nat.dist 1 0 = 1 := by decide
example : Nat.dist 0 0 = 0 ∨ Nat.dist 0 0 = 1 := by decide
example : Nat.dist 1 1 = 0 ∨ Nat.dist 1 1 = 1 := by decide

-- sub_one_lt
lemma sub_one_lt {a b : Nat} (h : b + 1 < a) : b < a - 1 := by omega
lemma sub_one_lt2 {a b : Nat} (ha : 0 < a) (h : b < a - 1) : b + 1 < a := by omega

-- (w-1) - c = w - (1+c) agrees
example (w c : Nat) (h : 2 ≤ w) : (w - 1) - c = w - (1 + c) := by omega

-- dist w 1 <= 1 when w <= 1
example (w : Nat) (h : w ≤ 1) : Nat.dist w 1 ≤ 1 := by
  have h01 : w = 0 ∨ w = 1 := by omega
  rcases h01 with rfl | rfl <;> decide

-- sub_le
example (a b c : Nat) (h : a ≤ b) : a - c ≤ b := by omega

-- run_high e=1 arithmetic target
example (w rest : Nat) (h : countOnes rest + 2 < w) : countOnes rest + 1 < w - 1 := by
  exact sub_one_lt (by omega : (countOnes rest + 1) + 1 < w)

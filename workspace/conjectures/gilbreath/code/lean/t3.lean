import Mathlib.Tactic
#check Even
#check Odd
#check Nat.even_or_odd
#check Nat.Even
#check Nat.dist
#check Nat.dist_eq_abs
#check abs
#check | (4:Nat) - 1 |
#check Nat.dist_comm
example : Nat.dist 1 4 = 3 := by norm_num
example : Odd 3 := by norm_num
example : Even 4 := by norm_num
example : Odd 1 := by norm_num
example : Even 0 := by norm_num
#check Nat.odd_iff
#check Nat.even_iff
#check Nat.not_even_iff_odd
#check Odd.add_odd
#check Even.add_even
#check Odd.add_even

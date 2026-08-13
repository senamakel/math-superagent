import Mathlib.Data.Nat.Dist
import Mathlib.Tactic
#check Nat.dist
#check Nat.dist_comm
#check Nat.dist_eq_sub_of_le
#check Nat.dist_eq_sub_of_ge
#check Nat.dist_add_dist
#check Nat.dist_sub_dist_le
#check Nat.dist_eq
#check Nat.dist_self
#check Nat.dist_eq_zero
example : Nat.dist 4 0 = 4 := by norm_num
example : Nat.dist 1 4 = 3 := by norm_num
example : Nat.dist 0 2 = 2 := by norm_num
example : Nat.dist 2 0 = 2 := by norm_num
#check Nat.even_sub
#check Nat.odd_sub
#check Nat.Even.sub
#check Even.sub
#check Nat.sub_odd
#check Nat.dist_eq_sub_of_le (a:=5) (b:=3) (by omega : 3 ≤ 5)

import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

#check Nat.dist
#check Nat.dist_comm
#check Nat.dist_eq_sub_of_le
#check Nat.dist_eq_sub_of_lt
#check Nat.dist_eq_sub_of_gt
#check Nat.dist_zero_right
#check Nat.dist_zero_left
#check Nat.dist_one_right
#check Nat.dist_one_left
#check Nat.dist_eq_zero
#check Nat.dist_self

example (x : Nat) : Nat.dist x 0 = x := by
  simp [Nat.dist]

example (x : Nat) : Nat.dist 0 x = x := by
  simp [Nat.dist]

example (x : Nat) (hx : 1 ≤ x) : Nat.dist x 1 = x - 1 := by
  rw [Nat.dist_eq_sub_of_le hx]

example (x : Nat) (hx : 1 ≤ x) : Nat.dist 1 x = x - 1 := by
  rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hx]

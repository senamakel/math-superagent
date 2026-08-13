import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

lemma dist_one_eq_one {n : ℕ} : Nat.dist 1 n = 1 ↔ n = 0 ∨ n = 2 := by
  constructor
  · intro h
    by_cases hn : n ≤ 1
    · rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hn] at h
      omega
    · have h1n : 1 ≤ n := by omega
      rw [Nat.dist_eq_sub_of_le h1n] at h
      omega
  · intro h
    rcases h with h0 | h2
    · rw [h0]
      decide
    · rw [h2]
      decide

example : Nat.dist 1 0 = 1 := by decide
example : Nat.dist 1 2 = 1 := by decide
example : Nat.dist 1 3 ≠ 1 := by decide
example : Nat.dist 1 4 ≠ 1 := by decide
import Mathlib.Data.Nat.Dist
import Mathlib.Data.Nat.Parity
import Mathlib.Tactic

lemma dist_dist_even {a b : ℕ} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    exact (Nat.even_sub hab).2 ⟨hb, ha⟩
  · have hba : b ≤ a := Nat.le_of_not_ge hab
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    exact (Nat.even_sub hba).2 ⟨ha, hb⟩

lemma dist_odd_even {a b : ℕ} (ha : Odd a) (hb : Even b) : Odd (Nat.dist a b) := by
  by_cases hab : a ≤ b
  · have hba : b ≤ a := by omega
    -- we are in a ≤ b case: note b - a with b even, a odd
    sorry
  · sorry

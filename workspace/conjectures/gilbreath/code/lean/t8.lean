import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

lemma dist_dist_even {a b : ℕ} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    exact (Nat.even_sub hab).mpr ⟨fun _ => hb, fun _ => ha⟩
  · have hba : b ≤ a := by
      by_contra h
      exact hab (le_of_not_ge h)
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    exact (Nat.even_sub hba).mpr ⟨fun _ => ha, fun _ => hb⟩

lemma dist_odd_even {a b : ℕ} (ha : Odd a) (hb : Even b) : Odd (Nat.dist a b) := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    exact (Nat.odd_sub hab).mpr ⟨fun _ => hb, fun _ => ha⟩
  · have hba : b ≤ a := by
      by_contra h
      exact hab (le_of_not_ge h)
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    exact (Nat.odd_sub hba).mpr ⟨fun _ => ha, fun _ => hb⟩

example : Even (Nat.dist 2 4) := by
  exact dist_dist_even (by norm_num : Even 2) (by norm_num : Even 4)
example : Odd (Nat.dist 5 4) := by
  exact dist_odd_even (by norm_num : Odd 5) (by norm_num : Even 4)

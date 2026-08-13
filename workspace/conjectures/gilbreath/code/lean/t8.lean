import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- |a - b| of two evens is even.
-- Route: Nat.dist_eq_sub_of_le + Nat.even_sub, whose Iff component
-- order is (Even m ↔ Even n) with m the larger side.
lemma dist_dist_even {a b : ℕ} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
  by_cases hab : a ≤ b
  · -- a ≤ b : Nat.dist a b = b - a,  even_sub hab : Even (b-a) ↔ (Even b ↔ Even a)
    rw [Nat.dist_eq_sub_of_le hab]
    exact (Nat.even_sub hab).mpr ⟨fun _ => ha, fun _ => hb⟩
  · have hba : b ≤ a := by
      by_contra h
      exact hab (le_of_not_ge h)
    -- b ≤ a : Nat.dist a b = b.dist a = a - b,  even_sub hba : Even (a-b) ↔ (Even a ↔ Even b)
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    exact (Nat.even_sub hba).mpr ⟨fun _ => hb, fun _ => ha⟩

-- |a - b| of an odd and an even is odd, by explicit witnesses
-- (Odd w := ∃ k, w = 2*k + 1), so no absolute-value group instance is needed.
lemma dist_odd_even {a b : ℕ} (ha : Odd a) (hb : Even b) : Odd (Nat.dist a b) := by
  rcases ha with ⟨x, hx⟩
  rcases hb with ⟨y, hy⟩
  by_cases hab : a ≤ b
  · -- a ≤ b : |a - b| = b - a = (y+y) - (2x+1) = 2(y-x-1) + 1
    rw [Nat.dist_eq_sub_of_le hab]
    use y - x - 1
    omega
  · have hba : b ≤ a := by omega
    -- b ≤ a : |a - b| = a - b = (2x+1) - (y+y) = 2(x-y) + 1
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    use x - y
    omega

example : Even (Nat.dist 2 4) := by
  exact dist_dist_even (by norm_num : Even 2) (by norm_num : Even 4)
example : Odd (Nat.dist 5 4) := by
  exact dist_odd_even (by norm_num : Odd 5) (by norm_num : Even 4)
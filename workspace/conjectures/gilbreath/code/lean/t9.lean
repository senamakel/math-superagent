import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- Fully explicit-witness proofs from the bare definitions
-- (Even a := ∃ r, a = r + r,  Odd a := ∃ k, a = 2*k + 1).
-- No absolute-value / group instance is needed.

lemma dist_dist_even {a b : ℕ} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
  rcases ha with ⟨x, hx⟩
  rcases hb with ⟨y, hy⟩
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    -- b - a = 2y - 2x = (y-x) + (y-x)
    use y - x
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    -- a - b = 2x - 2y = (x-y) + (x-y)
    use x - y
    omega

lemma dist_odd_even {a b : ℕ} (ha : Odd a) (hb : Even b) : Odd (Nat.dist a b) := by
  rcases ha with ⟨x, hx⟩
  rcases hb with ⟨y, hy⟩
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    -- b - a = (y+y) - (2x+1) = 2(y-x-1) + 1
    use y - x - 1
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    -- a - b = (2x+1) - (y+y) = 2(x-y) + 1
    use x - y
    omega

example : Even (Nat.dist 2 4) := by
  exact dist_dist_even (by norm_num : Even 2) (by norm_num : Even 4)
example : Odd (Nat.dist 5 4) := by
  exact dist_odd_even (by norm_num : Odd 5) (by norm_num : Even 4)
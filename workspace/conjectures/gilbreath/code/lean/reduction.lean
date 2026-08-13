import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- The reduction lemma for Gilbreath's conjecture.
--
-- Claim 1: the difference operator preserves the (odd, even, even, ...)
-- shape.  [Same statements as code/lean/shape.lean; re-stated here so
-- reduction.lean is self-contained.]
def Step (s : ℕ → ℕ) : ℕ → ℕ := fun i => Nat.dist (s i) (s (i + 1))
def StartsOddEvenEven (s : ℕ → ℕ) : Prop := Odd (s 0) ∧ ∀ n, Even (s (n + 1))

lemma dist_odd_even {a b : ℕ} (ha : Odd a) (hb : Even b) : Odd (Nat.dist a b) := by
  rcases ha with ⟨x, hx⟩
  rcases hb with ⟨y, hy⟩
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    use y - x - 1
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    use x - y
    omega

lemma dist_dist_even {a b : ℕ} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
  rcases ha with ⟨x, hx⟩
  rcases hb with ⟨y, hy⟩
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    use y - x
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    use x - y
    omega

theorem shape_theorem {s : ℕ → ℕ} (hs : StartsOddEvenEven s) : StartsOddEvenEven (Step s) := by
  rcases hs with ⟨h0, hrest⟩
  constructor
  · exact dist_odd_even h0 (hrest 0)
  · intro n
    exact dist_dist_even (hrest n) (hrest (n + 1))

-- Claim 2: the pivotal identity.  With a leading 1, the next row's leading
-- entry is |1 - (s 1)|, and this equals 1 iff s 1 is 0 or 2.
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

-- The leading entry of a row.
def leading_entry (s : ℕ → ℕ) : ℕ := s 0

-- THE REDUCTION LEMMA.  If a row has the (odd, even, even, ...) shape and
-- leading entry 1, then the next row has leading entry 1 iff the second
-- entry of the current row is 0 or 2.
theorem reduction {s : ℕ → ℕ} (_shape : StartsOddEvenEven s) (hlead : leading_entry s = 1) :
    leading_entry (Step s) = 1 ↔ s 1 = 0 ∨ s 1 = 2 := by
  unfold leading_entry Step
  have hlead' : s 0 = 1 := by simpa [leading_entry] using hlead
  rw [hlead']
  simpa using (dist_one_eq_one (n := s 1))

-- Same statement with the hypotheses gathered into one predicate.
def GilbreathRow (s : ℕ → ℕ) : Prop := StartsOddEvenEven s ∧ leading_entry s = 1 ∧ (s 1 = 0 ∨ s 1 = 2)

theorem reduction_lemma {s : ℕ → ℕ} (hg : GilbreathRow s) :
    leading_entry (Step s) = 1 ↔ s 1 = 0 ∨ s 1 = 2 := by
  rcases hg with ⟨hshape, hlead, _⟩
  exact reduction hshape hlead
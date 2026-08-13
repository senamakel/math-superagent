import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- Shape-preservation of (odd, even, even, ...) under the absolute-difference
-- operator.  Self-contained: the two parity lemmas live here.  The full
-- reduction (shape + leading-entry 1 + {0,2} second entry) is in
-- gilbreath_reduction.lean; this file proves the shape part alone.
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

theorem shape_theorem {s : ℕ → ℕ} (hs : StartsOddEvenEven s) :
    StartsOddEvenEven (Step s) := by
  rcases hs with ⟨h0, hrest⟩
  constructor
  · exact dist_odd_even h0 (hrest 0)
  · intro n
    exact dist_dist_even (hrest n) (hrest (n + 1))

-- Every iterate of the step keeps the shape: by induction on k.
theorem shape_iter {s : ℕ → ℕ} (hs : StartsOddEvenEven s) :
    ∀ k, StartsOddEvenEven (Step^[k] s) := by
  intro k
  induction k with
  | zero => simpa using hs
  | succ k ih =>
      simpa [Function.iterate_succ_apply'] using shape_theorem ih

#print axioms shape_theorem
#print axioms shape_iter
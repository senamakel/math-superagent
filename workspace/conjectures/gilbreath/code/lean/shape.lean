import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- Self-contained parity lemmas for the difference of a neighbouring pair
-- (same statements as code/lean/t9.lean, re-stated so this file imports
-- nothing else).

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

-- The row transition: s' i = |s i - s (i+1)|.
def Step (s : ℕ → ℕ) : ℕ → ℕ := fun i => Nat.dist (s i) (s (i + 1))

-- "The row starts (odd, even, even, ...)": position 0 odd, every later
-- position even.
def StartsOddEvenEven (s : ℕ → ℕ) : Prop := Odd (s 0) ∧ ∀ n, Even (s (n + 1))

-- THE SHAPE THEOREM.  If s starts (odd, even, even, ...), then so does
-- the difference row Step s.
theorem shape_theorem {s : ℕ → ℕ} (hs : StartsOddEvenEven s) : StartsOddEvenEven (Step s) := by
  rcases hs with ⟨h0, hrest⟩
  constructor
  · -- first entry of the next row: |s 0 - s 1| with s 0 odd, s 1 even
    exact dist_odd_even h0 (hrest 0)
  · intro n
    -- entries from position 2 on: |s (n+1) - s (n+2)|, both even
    exact dist_dist_even (hrest n) (hrest (n + 1))

-- A concrete infinite sequence with the shape, so the theorem has a witness.
def oddevenseq : ℕ → ℕ := fun i => if i = 0 then 1 else 2 * i

lemma shape_oddevenseq : StartsOddEvenEven oddevenseq := by
  constructor
  · simpa [oddevenseq] using (odd_one : Odd 1)
  · intro n
    simp [oddevenseq]

-- Corollary: the shape survives every iterate of the difference operator,
-- so every row of the iterated-difference triangle has it
-- (given the starting row has it).
theorem shape_iter {s : ℕ → ℕ} (hs : StartsOddEvenEven s) :
    ∀ k, StartsOddEvenEven (Step^[k] s) := by
  intro k
  induction k with
  | zero => simpa using hs
  | succ k ih => simpa [Function.iterate_succ_apply'] using shape_theorem ih
import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- Gilbreath's conjecture, reduced to the {0,2} second-entry claim, machine
-- checked in Lean 4.
--
-- The recursive (read: original) form of the conjecture is about the rows
--   A_{k+1}(i) = |A_k(i) - A_k(i+1)|,  A_0 = primes.
-- Every row A_k (k >= 1) has the shape (odd, even, even, ...) because A_1 is
-- (1, 2, 2, 4, ...) -- the oracle in code/out/witnesses.json verifies that --
-- and the shape is preserved by the operator (shape_theorem below). Then the
-- leading entry of the next row is |1 - A_k(1)|, which is 1 iff A_k(1) is 0
-- or 2 (reduction below). Induction on k therefore gives:
--
--   For ANY row stream X with X (k+1) = Step (X k) and with row 1 of the
--   prime shape and leading 1:
--       (forall k, X (succ k) 0 = 1)  <->  (forall k, X (succ k) 1 in {0,2})
--
-- which is gilbreath_reduction at the bottom.  This is the machine-checked
-- induction step: the run's claim `gilbreath-reduces-to-second-in-02`.
--
-- The hypotheses on X 1 are true for the prime stream by computation
-- (A_1 = 1,2,2,4,2,4,2,4,6,2,... : verified by code/lib/gilbreath.py against
-- problem.md), so the equivalence is exactly the reduction of the conjecture.
-- ============================================================================

-- The one-step difference operator.
def Step (s : ℕ → ℕ) : ℕ → ℕ := fun i => Nat.dist (s i) (s (i + 1))

def StartsOddEvenEven (s : ℕ → ℕ) : Prop := Odd (s 0) ∧ ∀ n, Even (s (n + 1))

def leading_entry (s : ℕ → ℕ) : ℕ := s 0

def GilbreathRow (s : ℕ → ℕ) : Prop := StartsOddEvenEven s ∧ leading_entry s = 1 ∧
  (s 1 = 0 ∨ s 1 = 2)

-- ---------------------------------------------------------------------------
-- Parity lemmas for the shape preservation.
-- ---------------------------------------------------------------------------

-- |odd - even| is odd.
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

-- |even - even| is even.
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

-- ---------------------------------------------------------------------------
-- Shape preservation: (odd, even, even, ...) is invariant under one step.
-- ---------------------------------------------------------------------------
theorem shape_theorem {s : ℕ → ℕ} (hs : StartsOddEvenEven s) :
    StartsOddEvenEven (Step s) := by
  rcases hs with ⟨h0, hrest⟩
  constructor
  · exact dist_odd_even h0 (hrest 0)
  · intro n
    exact dist_dist_even (hrest n) (hrest (n + 1))

-- ---------------------------------------------------------------------------
-- The pivotal identity: |1 - n| = 1  <->  n = 0 or n = 2.
-- ---------------------------------------------------------------------------
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

-- ---------------------------------------------------------------------------
-- The reduction lemma, in full generality under the shape hypotheses and a
-- leading entry of 1:
--     next leading entry = 1  <->  second entry of the current row in {0,2}.
-- ---------------------------------------------------------------------------
theorem reduction {s : ℕ → ℕ} (shape : StartsOddEvenEven s)
    (hlead : leading_entry s = 1) :
    leading_entry (Step s) = 1 ↔ s 1 = 0 ∨ s 1 = 2 := by
  unfold leading_entry Step
  change s 0 = 1 at hlead
  rw [hlead]
  change Nat.dist 1 (s 1) = 1 ↔ s 1 = 0 ∨ s 1 = 2
  exact dist_one_eq_one

-- per-lemma axiom footprint (to locate any sorryAx)
#print axioms dist_odd_even
#print axioms dist_dist_even
#print axioms dist_one_eq_one
#print axioms shape_theorem

theorem reduction_lemma {s : ℕ → ℕ} (hg : GilbreathRow s) :
    leading_entry (Step s) = 1 ↔ s 1 = 0 ∨ s 1 = 2 := by
  rcases hg with ⟨⟨h0, hrest⟩, hlead, _⟩
  exact reduction (by exact ⟨h0, hrest⟩ : StartsOddEvenEven s) hlead

-- ---------------------------------------------------------------------------
-- Row streams: X (k+1) = Step (X k).  The prime triangle is such a stream.
-- ---------------------------------------------------------------------------
def RowStream (X : ℕ → ℕ → ℕ) : Prop := ∀ k, X (Nat.succ k) = Step (X k)

-- Gilbreath's conjecture for a stream: every row from row 1 on starts with 1.
def GilbreathConjecture (X : ℕ → ℕ → ℕ) : Prop := ∀ k, X (Nat.succ k) 0 = 1

-- The {0,2} second-entry claim.
def SecondEntryIn02 (X : ℕ → ℕ → ℕ) : Prop :=
  ∀ k, X (Nat.succ k) 1 = 0 ∨ X (Nat.succ k) 1 = 2

-- Every row of the stream has the (odd, even, even, ...) shape, given that
-- row 1 does (shape preservation along the stream).
lemma shape_rows {X : ℕ → ℕ → ℕ} (hs : RowStream X)
    (hshape₁ : StartsOddEvenEven (X 1)) :
    ∀ k, StartsOddEvenEven (X (Nat.succ k)) := by
  intro k
  induction k with
  | zero => simpa using hshape₁
  | succ k ih =>
      have hstep : X (Nat.succ (Nat.succ k)) = Step (X (Nat.succ k)) := hs (Nat.succ k)
      rw [hstep]
      exact shape_theorem ih

-- ---------------------------------------------------------------------------
-- THE INDUCTION STEP, machine checked: for any row stream with the prime-row
-- shape and leading entry 1 at row 1, Gilbreath's conjecture is equivalent to
-- the {0,2} second-entry claim.
--
-- Forward: if every row starts with 1, then row k's second entry lies in
-- {0,2}, because the reduction lemma applies at row k.
-- Backward: induction on k; the reduction lemma is the inductive step.
-- ---------------------------------------------------------------------------
theorem gilbreath_reduction {X : ℕ → ℕ → ℕ} (hs : RowStream X)
    (hshape₁ : StartsOddEvenEven (X 1)) (hlead₁ : X 1 0 = 1) :
    GilbreathConjecture X ↔ SecondEntryIn02 X := by
  constructor
  · intro hgc k
    have shape_k : StartsOddEvenEven (X (Nat.succ k)) := shape_rows hs hshape₁ k
    have lead_k : X (Nat.succ k) 0 = 1 := by simpa [GilbreathConjecture] using (hgc k)
    have red := reduction (s := X (Nat.succ k)) shape_k lead_k
    have hstep : leading_entry (Step (X (Nat.succ k))) = 1 := by
      unfold leading_entry
      rw [← hs (Nat.succ k)]
      simpa [GilbreathConjecture] using (hgc (Nat.succ k))
    exact red.mp hstep
  · intro hsecond k
    induction k with
    | zero => simpa using hlead₁
    | succ k ih =>
        have shape_k : StartsOddEvenEven (X (Nat.succ k)) := shape_rows hs hshape₁ k
        have red := reduction (s := X (Nat.succ k)) shape_k ih
        have hright : X (Nat.succ k) 1 = 0 ∨ X (Nat.succ k) 1 = 2 := by
          simpa [SecondEntryIn02] using (hsecond k)
        have hgoal : leading_entry (Step (X (Nat.succ k))) = 1 := red.mpr hright
        unfold leading_entry at hgoal
        rw [← hs (Nat.succ k)] at hgoal
        simpa [GilbreathConjecture] using hgoal

-- The run's claim id: gilbreath-reduces-to-second-in-02, now a checked Lean
-- theorem.  Report of the axiom footprint and the sorry count:
#print axioms gilbreath_reduction
#print axioms reduction
#print axioms reduction_lemma
#print axioms shape_theorem
#print axioms shape_rows
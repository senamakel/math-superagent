import Mathlib

-- ============================================================================
-- The excess-height renormalization identity for the absolute-difference
-- operator, over Nat.dist.  Reuses the style of descent_lemma.lean: all
-- differences are genuine `Nat.dist` folds, no floats, no native_decide.
--
-- Setting.  A row `h : Nat → Nat` (column heights).  For a column its
-- *excess over the wall height 1* is
--     et  h j = max(0, h j - 1)            -- truncated at 0, so `h j - 1` in Nat
-- and the absolute difference between neighbouring columns is
--     dh  h j = |h j - h (j+1)|
-- whose excess is
--     etp h j = max(0, dh h j - 1)          -- again the Nat truncation.
--
-- The three local identities for an adjacent pair (j, j+1):
--   (a) bulk both ≥ 2:   etp h j = |et h j - et h (j+1)| - 1
--   (b) wall: h j ∈ {0,1}, h (j+1) = r+1  ⟹  etp h j = r - h j
--   (c) low both ∈ {0,1}:                   etp h j = 0
-- and the maximum principle:  M' = max_j etp h j ≤ M = max_j et h j,
-- with strict decrease `etp h j < M` for a bulk pair.
--
-- CHANGE REPORTED (deliberate, justified by the arithmetic):
--   Case (b) as requested was "etp h j = r + 1 - h j".  That is OFF BY ONE.
--   Since etp = |h j - (r+1)| - 1 = (r+1) - h j - 1 = r - h j (as h j ≤ 1 ≤ r+1),
--   the correct identity is `etp h j = r - h j`.  Example: h j=1, h(j+1)=2
--   gives etp = |1-2| - 1 = 0 = r - h j (r=1), not r+1-h j = 1.
--   This file proves the corrected statement.
-- ============================================================================

-- Excess over the wall: t(j) = max(0, h(j)-1), which is the Nat truncation.
def et (h : Nat → Nat) (j : Nat) : Nat := h j - 1

-- Absolute difference of neighbouring columns: h'(j).
def dh (h : Nat → Nat) (j : Nat) : Nat := Nat.dist (h j) (h (j + 1))

-- Excess of the difference: t'(j) = max(0, h'(j)-1) (Nat truncation).
def etp (h : Nat → Nat) (j : Nat) : Nat := dh h j - 1

-- |a - b| ≤ max a b.
lemma dist_le_max (a b : Nat) : Nat.dist a b ≤ max a b := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    omega

-- Removing 1 from both operands of a distance (when both ≥ 1) does not change it.
lemma dist_eq_sub_shift (a b : Nat) (ha : 1 ≤ a) (hb : 1 ≤ b) :
    Nat.dist a b = Nat.dist (a - 1) (b - 1) := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    rw [Nat.dist_eq_sub_of_le (by omega : a - 1 ≤ b - 1)]
    omega
  · have hba : b ≤ a := by omega
    have hle' : b - 1 ≤ a - 1 := by omega
    rw [Nat.dist_comm]
    rw [Nat.dist_eq_sub_of_le hba]
    rw [Nat.dist_comm]
    rw [Nat.dist_eq_sub_of_le hle']
    omega

lemma le_one_or (a : Nat) (ha : a ≤ 1) : a = 0 ∨ a = 1 := by
  by_cases h0 : a = 0
  · exact Or.inl h0
  · right
    omega

lemma not_le_one_ge_two (a : Nat) (h : ¬ a ≤ 1) : 2 ≤ a := by
  omega

-- ---------------------------------------------------------------------------
-- Case (a): the bulk pair.  Both columns reach or exceed the wall (excess ≥ 1),
-- so subtracting 1 from both simply shifts the distance, and the excess of the
-- difference is the distance of the excesses minus 1.
-- ---------------------------------------------------------------------------
theorem bulk_case (h : Nat → Nat) {j : Nat}
    (ha : 1 ≤ et h j) (hb : 1 ≤ et h (j + 1)) :
    etp h j = Nat.dist (et h j) (et h (j + 1)) - 1 := by
  unfold etp et dh
  change 1 ≤ h j - 1 at ha
  change 1 ≤ h (j + 1) - 1 at hb
  have hja : 1 ≤ h j := by omega
  have hjb : 1 ≤ h (j + 1) := by omega
  have hshift : Nat.dist (h j) (h (j + 1)) = Nat.dist (h j - 1) (h (j + 1) - 1) :=
    dist_eq_sub_shift (h j) (h (j + 1)) hja hjb
  rw [hshift]

-- ---------------------------------------------------------------------------
-- Case (b): the wall.  A low column h j ∈ {0,1} faces a tall column h(j+1)=r+1
-- (r = et h (j+1) ≥ 1).  Then (corrected)  etp h j = r - h j.
-- ---------------------------------------------------------------------------
theorem wall_case (h : Nat → Nat) {j r : Nat}
    (hj : h j = 0 ∨ h j = 1) (hnext : h (j + 1) = r + 1) :
    etp h j = r - h j := by
  unfold etp dh
  by_cases h0 : h j = 0
  · rw [h0, hnext]
    have hle : 0 ≤ r + 1 := by omega
    rw [Nat.dist_eq_sub_of_le hle]
    omega
  · have h1 : h j = 1 := by
      rcases hj with hj0 | hj1
      · contradiction
      · exact hj1
    rw [h1, hnext]
    have hle : 1 ≤ r + 1 := by omega
    rw [Nat.dist_eq_sub_of_le hle]
    omega

-- ---------------------------------------------------------------------------
-- Case (c): the low pair.  Both h j, h (j+1) ∈ {0,1}; the difference is at
-- most 1, so its excess is 0.
-- ---------------------------------------------------------------------------
theorem low_case (h : Nat → Nat) {j : Nat}
    (hj : h j = 0 ∨ h j = 1) (hj_1 : h (j + 1) = 0 ∨ h (j + 1) = 1) :
    etp h j = 0 := by
  unfold etp dh
  rcases hj with hj0 | hj1
  · rw [hj0]
    rcases hj_1 with h10 | h11
    · rw [h10]; decide
    · rw [h11]; decide
  · rw [hj1]
    rcases hj_1 with h10 | h11
    · rw [h10]; decide
    · rw [h11]; decide

-- ---------------------------------------------------------------------------
-- Local upper bounds.  Wall (left low, right tall), wall mirrored (left tall,
-- right low), bulk, and low each give one half of the pointwise bound.
-- ---------------------------------------------------------------------------
theorem wall_right (h : Nat → Nat) (j : Nat) {r : Nat}
    (hlow : h j = 0 ∨ h j = 1) (hnext : h (j + 1) = r + 1) :
    etp h j ≤ et h (j + 1) := by
  unfold etp et dh
  rw [hnext]
  by_cases h0 : h j = 0
  · rw [h0]
    rw [Nat.dist_eq_sub_of_le (by omega : 0 ≤ r + 1)]
    omega
  · have h1 : h j = 1 := by
      rcases hlow with hl0 | hl1
      · contradiction
      · exact hl1
    rw [h1]
    rw [Nat.dist_eq_sub_of_le (by omega : 1 ≤ r + 1)]
    omega

theorem wall_left (h : Nat → Nat) (j : Nat) {a : Nat}
    (ha : h j = a + 1) (hnext : h (j + 1) = 0 ∨ h (j + 1) = 1) :
    etp h j ≤ et h j := by
  unfold etp et dh
  rw [ha]
  by_cases h0 : h (j + 1) = 0
  · rw [h0]
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le (by omega : 0 ≤ a + 1)]
    omega
  · have h1 : h (j + 1) = 1 := by
      rcases hnext with hn0 | hn1
      · contradiction
      · exact hn1
    rw [h1]
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le (by omega : 1 ≤ a + 1)]
    omega

-- Bulk pair: the excess of the difference is at most the max excess of its
-- endpoints.
theorem bulk_bound (h : Nat → Nat) (j : Nat)
    (hjg2 : 2 ≤ h j) (hng2 : 2 ≤ h (j + 1)) :
    etp h j ≤ max (et h j) (et h (j + 1)) := by
  unfold etp et dh
  have hshift : Nat.dist (h j) (h (j + 1)) = Nat.dist (h j - 1) (h (j + 1) - 1) :=
    dist_eq_sub_shift (h j) (h (j + 1)) (by omega) (by omega)
  rw [hshift]
  have hdm := dist_le_max (h j - 1) (h (j + 1) - 1)
  exact le_trans (Nat.sub_le (Nat.dist (h j - 1) (h (j + 1) - 1)) 1) hdm

-- ---------------------------------------------------------------------------
-- Pointwise maximum principle: for every column j,  t'(j) ≤ max(t(j), t(j+1)).
-- ---------------------------------------------------------------------------
theorem pointwise_bound (h : Nat → Nat) (j : Nat) :
    etp h j ≤ max (et h j) (et h (j + 1)) := by
  by_cases hja : h j ≤ 1
  · by_cases hjb : h (j + 1) ≤ 1
    · rw [low_case h (le_one_or (h j) hja) (le_one_or (h (j + 1)) hjb)]
      exact Nat.zero_le _
    · have hlow : h j = 0 ∨ h j = 1 := le_one_or (h j) hja
      have hg2 : 2 ≤ h (j + 1) := not_le_one_ge_two (h (j + 1)) hjb
      let r := h (j + 1) - 1
      have hnext : h (j + 1) = r + 1 := by
        have : 1 ≤ h (j + 1) := by omega
        omega
      have hwl := wall_right h j hlow hnext
      exact le_trans hwl (le_max_right (et h j) (et h (j + 1)))
  · have hjg2 : 2 ≤ h j := not_le_one_ge_two (h j) hja
    by_cases hjb : h (j + 1) ≤ 1
    · have hlow2 : h (j + 1) = 0 ∨ h (j + 1) = 1 := le_one_or (h (j + 1)) hjb
      let a := h j - 1
      have ha : h j = a + 1 := by
        have : 1 ≤ h j := by omega
        omega
      have hwl := wall_left h j ha hlow2
      exact le_trans hwl (le_max_left (et h j) (et h (j + 1)))
    · have hng2 : 2 ≤ h (j + 1) := not_le_one_ge_two (h (j + 1)) hjb
      exact bulk_bound h j hjg2 hng2

-- ---------------------------------------------------------------------------
-- Strict decrease for a bulk pair: both endpoints exceed the wall, so
--   t'(j) < max(t(j), t(j+1)).
-- ---------------------------------------------------------------------------
theorem bulk_strict (h : Nat → Nat) (j : Nat)
    (hjg2 : 2 ≤ h j) (hng2 : 2 ≤ h (j + 1)) :
    etp h j < max (et h j) (et h (j + 1)) := by
  unfold etp et dh
  have hshift : Nat.dist (h j) (h (j + 1)) = Nat.dist (h j - 1) (h (j + 1) - 1) :=
    dist_eq_sub_shift (h j) (h (j + 1)) (by omega) (by omega)
  rw [hshift]
  have hdm := dist_le_max (h j - 1) (h (j + 1) - 1)
  have hge : 1 ≤ max (h j - 1) (h (j + 1) - 1) := by omega
  have hle : Nat.dist (h j - 1) (h (j + 1) - 1) - 1 ≤ max (h j - 1) (h (j + 1) - 1) - 1 := by
    omega
  have hlt2 : max (h j - 1) (h (j + 1) - 1) - 1 < max (h j - 1) (h (j + 1) - 1) := by
    omega
  exact lt_of_le_of_lt hle hlt2

-- ---------------------------------------------------------------------------
-- Global maximum principle over a finite window of N columns (N ≥ 1):
--   M' = max_{j < N-1} etp h j  ≤  M = max_{j < N} et h j
-- (there are N-1 internal edges).
-- ---------------------------------------------------------------------------
theorem max_principle (h : Nat → Nat) (N : Nat) (hN : 1 ≤ N) :
    Finset.sup Finset.univ (fun j : Fin (N - 1) => etp h j.1)
      ≤ Finset.sup Finset.univ (fun j : Fin N => et h j.1) := by
  apply Finset.sup_le
  intro j hj
  have hpb := pointwise_bound h j.1
  refine le_trans hpb ?_
  have hjn : j.1 < N := by
    exact lt_of_lt_of_le j.isLt (Nat.sub_le N 1)
  have hj1n : j.1 + 1 < N := by
    have hle : j.1 + 1 ≤ N - 1 := by omega
    have hlt : N - 1 < N := by omega
    exact lt_of_le_of_lt hle hlt
  have h1 : et h j.1 ≤ Finset.sup Finset.univ (fun k : Fin N => et h k.1) := by
    exact Finset.le_sup (f := fun k : Fin N => et h k.1) (by simp : (⟨j.1, hjn⟩ : Fin N) ∈ Finset.univ)
  have h2 : et h (j.1 + 1) ≤ Finset.sup Finset.univ (fun k : Fin N => et h k.1) := by
    exact Finset.le_sup (f := fun k : Fin N => et h k.1) (by simp : (⟨j.1 + 1, hj1n⟩ : Fin N) ∈ Finset.univ)
  exact max_le h1 h2

-- For a bulk pair, the strict decrease is below the global maximum too:
--   t'(j) < M  (provided both j, j+1 lie in the window).
theorem bulk_strict_ltM (h : Nat → Nat) (j : Nat) (N : Nat)
    (hj : j < N) (hj1 : j + 1 < N)
    (hbulk : 2 ≤ h j) (hbulk2 : 2 ≤ h (j + 1)) :
    etp h j < Finset.sup Finset.univ (fun k : Fin N => et h k.1) := by
  have hbs := bulk_strict h j hbulk hbulk2
  refine lt_of_lt_of_le hbs ?_
  have h1 : et h j ≤ Finset.sup Finset.univ (fun k : Fin N => et h k.1) := by
    exact Finset.le_sup (f := fun k : Fin N => et h k.1) (by simp : (⟨j, hj⟩ : Fin N) ∈ Finset.univ)
  have h2 : et h (j + 1) ≤ Finset.sup Finset.univ (fun k : Fin N => et h k.1) := by
    exact Finset.le_sup (f := fun k : Fin N => et h k.1) (by simp : (⟨j + 1, hj1⟩ : Fin N) ∈ Finset.univ)
  exact max_le h1 h2

-- ---------------------------------------------------------------------------
-- Axiom footprint.
-- ---------------------------------------------------------------------------
#print axioms bulk_case
#print axioms wall_case
#print axioms low_case
#print axioms wall_right
#print axioms wall_left
#print axioms bulk_bound
#print axioms pointwise_bound
#print axioms bulk_strict
#print axioms max_principle
#print axioms bulk_strict_ltM

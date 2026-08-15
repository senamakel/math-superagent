import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- The sharpened descent lemma -- the combinatorial core of Granville's
-- Lemma 5.4 -- in HALVED units, fully formalised in Lean 4 with no `sorry`.
--
-- Setting.  A pattern is a list `el : List Nat` with every entry in {0,1}
-- (the hypothesis `∀ e ∈ el, e = 0 ∨ e = 1`), and a starting (halved) value
-- `w : Nat`.  The trajectory is
--     d_0 = w,     d_{k+1} = | d_k - e_k |
-- The recursive function is `runAbs`; `countOnes el` = ν₁ = # of 1s.
--
-- The three claims, L = el.length arbitrary:
--   (1)  w ≤ ν₁ + 1       ⟹  runAbs w el ∈ {0,1}
--   (2)  w >  ν₁ + 1      ⟹  runAbs w el = w - ν₁
--   (3)  {0,1} is absorbing under |x - e| for e ∈ {0,1}.
--
-- The engine is the unconditional invariant `run_inv`: every value is either
-- exactly `w - (#ones so far)` or inside {0,1}.  Since {0,1} is absorbing
-- (run_absorb), claim (1) follows; claim (2) is the direct induction run_high.
-- ============================================================================

def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

def countOnes : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 1 then 1 else 0) + countOnes rest

lemma abs_dist_zero (x : Nat) : Nat.dist x 0 = x := Nat.dist_zero_right x

lemma abs_dist_one (x : Nat) (hx : 1 ≤ x) : Nat.dist x 1 = x - 1 := by
  rw [Nat.dist_comm]
  exact Nat.dist_eq_sub_of_le hx

-- ---------------------------------------------------------------------------
-- Claim (3): {0,1} is absorbing under |x - e|.
-- ---------------------------------------------------------------------------
lemma absorbing {x e : Nat} (hx : x = 0 ∨ x = 1) (he : e = 0 ∨ e = 1) :
    Nat.dist x e = 0 ∨ Nat.dist x e = 1 := by
  rcases hx with rfl | rfl
  · rcases he with rfl | rfl <;> decide
  · rcases he with rfl | rfl <;> decide

-- Absorption propagates along the whole pattern.
lemma run_absorb (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ w : Nat, (w = 0 ∨ w = 1) → runAbs w el = 0 ∨ runAbs w el = 1 := by
  induction el with
  | nil =>
      intro w hw
      simp [runAbs]
      exact hw
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 1 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro w hw
      have hnew : Nat.dist w e = 0 ∨ Nat.dist w e = 1 := absorbing hw (hall e (by simp))
      have hr := ih hrest (Nat.dist w e) hnew
      exact hr

-- ---------------------------------------------------------------------------
-- Claim (2): if w > ν₁ + 1 the exact branch persists to the end.
-- ---------------------------------------------------------------------------
lemma run_high (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ w : Nat, countOnes el + 1 < w → runAbs w el = w - countOnes el := by
  induction el with
  | nil =>
      intro w hw
      simp [runAbs, countOnes]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 1 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro w hw
      have hecone : e = 0 ∨ e = 1 := hall e (by simp)
      rcases hecone with rfl | rfl
      · -- e = 0 : value fixed, ν₁ unchanged.
        change runAbs (Nat.dist w 0) rest = w - countOnes (0 :: rest)
        rw [abs_dist_zero]
        simp [countOnes]
        have hw' : countOnes rest + 1 < w := by
          simpa [countOnes] using hw
        exact ih hrest w hw'
      · -- e = 1 : one exact decrement.
        change runAbs (Nat.dist w 1) rest = w - countOnes (1 :: rest)
        have hwbig : 2 ≤ w := by
          have hw'' : countOnes (1 :: rest) + 1 < w := by simpa [countOnes] using hw
          omega
        have hd : Nat.dist w 1 = w - 1 := abs_dist_one w (by omega)
        rw [hd]
        have hw' : countOnes rest + 1 < w - 1 := by
          have hw'' : countOnes (1 :: rest) + 1 < w := by simpa [countOnes] using hw
          omega
        have hrun := ih hrest (w - 1) hw'
        rw [hrun]
        simp [countOnes]
        omega

-- ---------------------------------------------------------------------------
-- The engine invariant.  Unconditional.
-- ---------------------------------------------------------------------------
lemma run_inv (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ w : Nat,
      runAbs w el = w - countOnes el ∨ runAbs w el = 0 ∨ runAbs w el = 1 := by
  induction el with
  | nil =>
      intro w
      simp [runAbs, countOnes]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 1 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro w
      have hecone : e = 0 ∨ e = 1 := hall e (by simp)
      rcases hecone with rfl | rfl
      · -- e = 0 : value fixed, ν₁ unchanged -> invariant passes through.
        change runAbs (Nat.dist w 0) rest = w - countOnes (0 :: rest)
              ∨ runAbs (Nat.dist w 0) rest = 0 ∨ runAbs (Nat.dist w 0) rest = 1
        rw [abs_dist_zero]
        simp [countOnes]
        exact ih hrest w
      · -- e = 1.
        change runAbs (Nat.dist w 1) rest = w - countOnes (1 :: rest)
              ∨ runAbs (Nat.dist w 1) rest = 0 ∨ runAbs (Nat.dist w 1) rest = 1
        have ihw := ih hrest (Nat.dist w 1)
        rcases ihw with h | h
        · -- tail on exact line: `Nat.dist w 1 - countOnes rest`.
          by_cases hbig : 2 ≤ w
          · left
            rw [abs_dist_one w (by omega)] at h ⊢
            rw [h]
            simp [countOnes]
            omega
          · right
            rw [h]
            have hw1 : w ≤ 1 := by omega
            have hdist : Nat.dist w 1 ≤ 1 := by
              have h01 : w = 0 ∨ w = 1 := by omega
              rcases h01 with rfl | rfl <;> decide
            omega
        · -- tail already inside {0,1}.
          right
          exact h

-- ---------------------------------------------------------------------------
-- Claim (1): if w ≤ ν₁ + 1 the final value lies in {0,1}.
-- ---------------------------------------------------------------------------
theorem descent_claim1 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1)
    {w : Nat} (hw : w ≤ countOnes el + 1) :
    runAbs w el = 0 ∨ runAbs w el = 1 := by
  rcases run_inv hall w with h | h
  · have hle : w - countOnes el ≤ 1 := by omega
    rw [h]
    omega
  · exact h

-- ---------------------------------------------------------------------------
-- Claim (2): if w > ν₁ + 1 the final value is exactly w - ν₁.
-- ---------------------------------------------------------------------------
theorem descent_claim2 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1)
    {w : Nat} (hw : countOnes el + 1 < w) :
    runAbs w el = w - countOnes el := run_high hall w hw

-- ---------------------------------------------------------------------------
-- Axiom footprint.
-- ---------------------------------------------------------------------------
#print axioms absorbing
#print axioms run_absorb
#print axioms run_high
#print axioms run_inv
#print axioms descent_claim1
#print axioms descent_claim2

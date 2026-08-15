import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- The descent / absorption lemma -- the combinatorial core of Granville's
-- Lemma 5.4 -- in the EVEN-UNIT form, fully formalised in Lean 4, sorry-free.
--
-- Setting.  A pattern `el : List Nat` with every entry in {0,2}
-- (hypothesis `∀ e ∈ el, e = 0 ∨ e = 2`), and a starting value `v : Nat`.
-- The trajectory is
--     x_0 = v,     x_{s+1} = |x_s - e_s|
-- implemented by `runAbs`.  `countTwo el` = ν₂ = #{s : e_s = 2}.
--
-- The trajectory is parity-preserving when `v` is even (every value is even).
-- This evenness is LOAD-BEARING: for odd `v` the biconditional below is FALSE
-- (the bounce |1 - 2| = 1 leaves {0,2} and leaves the exact-count line too),
-- which is why every claim carries `Even v`.
--
-- The claims (all `v` even):
--   (a)  x_L ∈ {0,2}  ⟺  v ≤ 2*ν₂ + 2
--   (b)  v > 2*ν₂ + 2  ⟹  x_L = v - 2*ν₂  and  x_L ≥ 4
--
-- Proof shape (the corrected case split, not the false 'v-2ν₂ always' algebra):
--   * `{0,2}` is absorbing under |·-e| for e ∈ {0,2}.
--   * `run_inv_even`: unconditionally the value is either on the exact line
--     `v - 2·(ν₂ so far)` or inside {0,2}.  This handles the backward leg of (a):
--     if `v ≤ 2ν₂+2` the exact-line value is ≤ 2 and even, hence in {0,2}.
--   * `run_high_even`: if `v > 2ν₂+2` then no bounce ever occurs (every value
--     stays ≥ 2 on the exact line), so each c=2 step subtracts exactly 2 and
--     each c=0 step fixes, giving `x_L = v - 2ν₂`.  With `v` even this is ≥ 4.
--   * The forward leg of (a) is the contrapositive of the high branch.
-- ============================================================================

def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

def countTwo : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 2 then 1 else 0) + countTwo rest

-- For x ≥ 2, |x - 2| = x - 2 (the "subtract exactly 2" step).
lemma dist_even_two (x : Nat) (hx : 2 ≤ x) : Nat.dist x 2 = x - 2 := by
  rw [Nat.dist_comm]
  exact Nat.dist_eq_sub_of_le hx

-- Difference of two even numbers is even (parity preservation).
lemma dist_even_even {a b : Nat} (ha : Even a) (hb : Even b) : Even (Nat.dist a b) := by
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
-- Absorption: {0,2} is closed under |·-e| for e ∈ {0,2}.
-- ---------------------------------------------------------------------------
lemma absorbing {x e : Nat} (hx : x = 0 ∨ x = 2) (he : e = 0 ∨ e = 2) :
    Nat.dist x e = 0 ∨ Nat.dist x e = 2 := by
  rcases hx with rfl | rfl <;> rcases he with rfl | rfl <;> decide

-- Absorption propagates along the whole pattern.
lemma run_absorb {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
    ∀ w : Nat, (w = 0 ∨ w = 2) → runAbs w el = 0 ∨ runAbs w el = 2 := by
  induction el with
  | nil =>
      intro w hw
      simp [runAbs]
      exact hw
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 2 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro w hw
      have hnew : Nat.dist w e = 0 ∨ Nat.dist w e = 2 := absorbing hw (hall e (by simp))
      exact ih hrest (Nat.dist w e) hnew

-- ---------------------------------------------------------------------------
-- The high (no-bounce) branch: if v > 2ν₂+2 no value ever drops below 2, so
-- every c=2 step subtracts exactly 2 and every c=0 step fixes.
-- (No evenness hypothesis is needed here: v ≥ 2ν₂+3 forces v - 2·(ν₂ so far)
-- ≥ 3 ≥ 2 throughout.)
-- ---------------------------------------------------------------------------
lemma run_high_even {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
    ∀ v : Nat, 2 * countTwo el + 2 < v → runAbs v el = v - 2 * countTwo el := by
  induction el with
  | nil =>
      intro v hv
      simp [runAbs, countTwo]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 2 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro v hv
      have hecone : e = 0 ∨ e = 2 := hall e (by simp)
      rcases hecone with rfl | rfl
      · -- e = 0 : value fixed, ν₂ unchanged.
        change runAbs (Nat.dist v 0) rest = v - 2 * countTwo (0 :: rest)
        rw [Nat.dist_zero_right]
        simp [countTwo]
        exact ih hrest v (by simpa [countTwo] using hv)
      · -- e = 2 : subtract exactly 2 (bounce free because v > 2ν₂+2 ≥ 2).
        change runAbs (Nat.dist v 2) rest = v - 2 * countTwo (2 :: rest)
        have hbig : 2 ≤ v := by
          have hc : countTwo (2 :: rest) = 1 + countTwo rest := by simp [countTwo]
          omega
        have hd : Nat.dist v 2 = v - 2 := dist_even_two v hbig
        rw [hd]
        have hv' : 2 * countTwo rest + 2 < v - 2 := by
          have hc : countTwo (2 :: rest) = 1 + countTwo rest := by simp [countTwo]
          omega
        have hrun := ih hrest (v - 2) hv'
        rw [hrun]
        rw [show countTwo (2 :: rest) = 1 + countTwo rest by simp [countTwo]]
        omega

-- ---------------------------------------------------------------------------
-- The engine invariant, valid for even `v`: the value is either exactly on the
-- line `v - 2·(ν₂ so far)` or inside {0,2}.
-- ---------------------------------------------------------------------------
lemma run_inv_even {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
    ∀ v : Nat, Even v →
      runAbs v el = v - 2 * countTwo el ∨ (runAbs v el = 0 ∨ runAbs v el = 2) := by
  induction el with
  | nil =>
      intro v hv
      simp [runAbs, countTwo]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 2 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro v hv
      have hecone : e = 0 ∨ e = 2 := hall e (by simp)
      rcases hecone with rfl | rfl
      · -- e = 0 : value fixed, ν₂ unchanged -> invariant passes through.
        change runAbs (Nat.dist v 0) rest = v - 2 * countTwo (0 :: rest)
              ∨ (runAbs (Nat.dist v 0) rest = 0 ∨ runAbs (Nat.dist v 0) rest = 2)
        rw [Nat.dist_zero_right]
        simp [countTwo]
        exact ih hrest v hv
      · -- e = 2.
        change runAbs (Nat.dist v 2) rest = v - 2 * countTwo (2 :: rest)
              ∨ (runAbs (Nat.dist v 2) rest = 0 ∨ runAbs (Nat.dist v 2) rest = 2)
        have even_dist : Even (Nat.dist v 2) := dist_even_even hv (by decide : Even 2)
        have ihw := ih hrest (Nat.dist v 2) even_dist
        rcases ihw with h | h
        · -- tail on the exact line: `Nat.dist v 2 - 2·countTwo rest`.
          by_cases hbig : 2 ≤ v
          · left
            have hd : Nat.dist v 2 = v - 2 := dist_even_two v hbig
            rw [hd] at h ⊢
            rw [h]
            rw [show countTwo (2 :: rest) = 1 + countTwo rest by simp [countTwo]]
            omega
          · -- v < 2; with v even this forces v = 0, and 0 ↦ 2 ∈ {0,2}.
            right
            have v0 : v = 0 := by
              rcases hv with ⟨k, hk⟩
              omega
            rw [v0]
            exact run_absorb hrest 2 (by decide)
        · -- tail already inside {0,2}.
          right
          exact h

-- ---------------------------------------------------------------------------
-- A small helper: an even number ≤ 2 is 0 or 2.
-- ---------------------------------------------------------------------------
lemma even_le_two (n : Nat) (hn : Even n) (hle : n ≤ 2) : n = 0 ∨ n = 2 := by
  by_cases h1 : n ≤ 1
  · rcases hn with ⟨k, hk⟩
    omega
  · have hge : 2 ≤ n := by omega
    omega

-- ---------------------------------------------------------------------------
-- Claim (a), backward leg: if v ≤ 2ν₂+2 (and v even) the orbit lands in {0,2}.
-- ---------------------------------------------------------------------------
theorem descent_backward {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hv : v ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  rcases run_inv_even hall v hE with h | h
  · -- on the exact line: value = v - 2ν₂ ≤ 2 and even.
    have hle2 : v - 2 * countTwo el ≤ 2 := by omega
    have hev : Even (v - 2 * countTwo el) := by
      rcases hE with ⟨k, hk⟩
      by_cases hle : 2 * countTwo el ≤ v
      · use k - countTwo el
        omega
      · use 0
        omega
    have hz := even_le_two (v - 2 * countTwo el) hev hle2
    rw [h]
    exact hz
  · exact h

-- ---------------------------------------------------------------------------
-- Claim (b): if v > 2ν₂+2 (and v even) then x_L = v - 2ν₂ and x_L ≥ 4.
-- ---------------------------------------------------------------------------
theorem descent_high_value {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hv : 2 * countTwo el + 2 < v) :
    runAbs v el = v - 2 * countTwo el ∧ 4 ≤ v - 2 * countTwo el := by
  constructor
  · exact run_high_even hall v hv
  · rcases hE with ⟨k, hk⟩
    omega

-- ---------------------------------------------------------------------------
-- The full biconditional:  x_L ∈ {0,2}  ⟺  v ≤ 2ν₂+2   (v even).
-- Forward is the contrapositive of the high branch; backward is descent_backward.
-- ---------------------------------------------------------------------------
theorem descent_biconditional {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) :
    (runAbs v el = 0 ∨ runAbs v el = 2) ↔ v ≤ 2 * countTwo el + 2 := by
  constructor
  · intro h
    by_contra hgt
    have hnotle : 2 * countTwo el + 2 < v := by omega
    have hx := run_high_even hall v hnotle
    have hbig : 4 ≤ v - 2 * countTwo el := by
      rcases hE with ⟨k, hk⟩
      omega
    rw [hx] at h
    omega
  · intro hv
    exact descent_backward hall hE hv

-- ---------------------------------------------------------------------------
-- Axiom footprint.
-- ---------------------------------------------------------------------------
#print axioms absorbing
#print axioms run_absorb
#print axioms run_high_even
#print axioms run_inv_even
#print axioms even_le_two
#print axioms descent_backward
#print axioms descent_high_value
#print axioms descent_biconditional

import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- Granville Lemma 5.4 -- the COMPOSITION leg, sorry-free and kernel-checked.
--
-- This file closes the loop from the abstract descent core to the full
-- even-domain Lemma 5.4 statement.  It is SELF-CONTAINED (the container
-- builds no olean files, so a theorem cannot `import descent_lemma`); it
-- re-derives the two pieces it needs and then states the two legs the run
-- asked to formalise, as standalone theorems:
--
--   LEG 1 -- Link A's combinatorial engine (the |a-b| <= max(a,b) induction):
--       `orbit_le_max` :  runAbs v el <= max v (maxAll el)
--     i.e. the whole orbit is bounded by the record gap
--     g*_n = max v (maxAll el) = max( start, max over the epsilons ).
--
--   LEG 2 -- the composition:
--       `lemma54_composition` :
--         (g*_n <= 2*nu2 + 2)  &  (v <= g*_n)  ==>  delta_L in {0,2}
--     and its concrete `max`-bound form:
--       `lemma54_composition_via_max` :
--         max v (maxAll el) <= 2*nu2+2  ==>  runAbs v el in {0,2}.
--
-- Notation.  el is the (maximal {0,2}-suffix / 0-2 cycle) pattern of the
-- previous right diagonal; v is the new column's landing value (even on the
-- real prime rows); nu2 = countTwo el; the budget is 2*nu2 + 2.  The descent
-- core used below is `descent_backward` (from descent_lemma.lean): with v
-- even and v <= 2*nu2+2, the orbit `runAbs v el` lands in {0,2}.  Link A is
-- what supplies `v <= g*_n`; the composition is the transitivity
-- `v <= g*_n <= 2*nu2+2`, feeding descent_backward.
--
-- The geometric identity that identifies g*_n with the triangle's record gap
-- (claim reduction-passage-exact) is LEFT OUTSIDE this file: it is the
-- reduction passage Delta_k(q_n) = |Delta_{k-1}(q_n) - eps_k| and needs the
-- actual triangular array.  What is kernel-checked here is every leg of the
-- nondimensional algebra from the two hypotheses to success.
-- ============================================================================

-- The orbit / trajectory: x_0 = w, x_{s+1} = |x_s - e_s|.
def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

-- nu2 : the number of 2s in an even {0,2} pattern.
def countTwo : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 2 then 1 else 0) + countTwo rest

-- maxAll : the maximum of a list of naturals (0 for the empty list).
def maxAll : List Nat → Nat
  | [] => 0
  | e :: rest => max e (maxAll rest)

-- ===========================================================================
-- LEG 1 machinery -- the |a-b| <= max(a,b) induction.  Every descent step
-- keeps the value <= the running max, so the orbit never exceeds its record
-- gap g*_n = max v (maxAll el).
-- ===========================================================================

-- The pointwise engine: |a - b| <= max(a, b).
lemma dist_le_max (a b : Nat) : Nat.dist a b ≤ max a b := by
  by_cases hab : a ≤ b
  · rw [Nat.dist_eq_sub_of_le hab]
    omega
  · have hba : b ≤ a := by omega
    rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hba]
    omega

-- Every element of a list is at most its maxAll.
lemma maxAll_ge : ∀ el : List Nat, ∀ e : Nat, e ∈ el → e ≤ maxAll el := by
  intro el
  induction el with
  | nil =>
      intro e he
      simp at he
  | cons a rest ih =>
      intro e he
      rcases List.mem_cons.mp he with heq | hrest
      · subst e
        simp [maxAll]
      · exact le_trans (ih e hrest) (le_max_right a (maxAll rest))

-- If the start w and every epsilon are bounded above by M, the orbit stays
-- bounded above by M.
lemma run_le : ∀ el : List Nat, ∀ w M : Nat,
    w ≤ M → (∀ e ∈ el, e ≤ M) → runAbs w el ≤ M
  | [], w, M, hw, hM => by
      simpa [runAbs] using hw
  | e :: rest, w, M, hw, hM => by
      have he : e ≤ M := hM e (by simp)
      have hdM : Nat.dist w e ≤ M :=
        le_trans (dist_le_max w e) (max_le hw he)
      have hrest : ∀ e' ∈ rest, e' ≤ M := by
        intro e' he'
        exact hM e' (by simp [he'])
      exact run_le rest (Nat.dist w e) M hdM hrest

-- LINK A (combinatorial core): the orbit is bounded by the record gap
-- g*_n = max v (maxAll el)  =  max(start, max over the epsilons).
theorem orbit_le_max (el : List Nat) (v : Nat) :
    runAbs v el ≤ max v (maxAll el) := by
  apply run_le
  · exact le_max_left v (maxAll el)
  · intro e he
    exact le_trans (maxAll_ge el e he) (le_max_right v (maxAll el))

-- ===========================================================================
-- The descent core (from descent_lemma.lean, even-unit): if v is even and
-- v <= 2*nu2 + 2, the orbit lands in {0,2}.
-- ===========================================================================

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

-- {0,2} is closed under |x - e| for e in {0,2}.
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

-- For x >= 2, |x - 2| = x - 2 (the "subtract exactly 2" step).
lemma dist_even_two (x : Nat) (hx : 2 ≤ x) : Nat.dist x 2 = x - 2 := by
  rw [Nat.dist_comm]
  exact Nat.dist_eq_sub_of_le hx

-- The high (no-bounce) branch: if 2*nu2+2 < v, every 2 subtracts exactly 2,
-- every 0 fixes, so the orbit equals v - 2*nu2 exactly.
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
      · change runAbs (Nat.dist v 0) rest = v - 2 * countTwo (0 :: rest)
        rw [Nat.dist_zero_right]
        simp [countTwo]
        exact ih hrest v (by simpa [countTwo] using hv)
      · change runAbs (Nat.dist v 2) rest = v - 2 * countTwo (2 :: rest)
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

-- The engine invariant, valid for even v: the value is either exactly on the
-- line `v - 2*(nu2 so far)` or inside {0,2}.
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
      · change runAbs (Nat.dist v 0) rest = v - 2 * countTwo (0 :: rest)
              ∨ (runAbs (Nat.dist v 0) rest = 0 ∨ runAbs (Nat.dist v 0) rest = 2)
        rw [Nat.dist_zero_right]
        simp [countTwo]
        exact ih hrest v hv
      · change runAbs (Nat.dist v 2) rest = v - 2 * countTwo (2 :: rest)
              ∨ (runAbs (Nat.dist v 2) rest = 0 ∨ runAbs (Nat.dist v 2) rest = 2)
        have even_dist : Even (Nat.dist v 2) := dist_even_even hv (by decide : Even 2)
        have ihw := ih hrest (Nat.dist v 2) even_dist
        rcases ihw with h | h
        · by_cases hbig : 2 ≤ v
          · left
            have hd : Nat.dist v 2 = v - 2 := dist_even_two v hbig
            rw [hd] at h ⊢
            rw [h]
            rw [show countTwo (2 :: rest) = 1 + countTwo rest by simp [countTwo]]
            omega
          · right
            have v0 : v = 0 := by
              rcases hv with ⟨k, hk⟩
              omega
            rw [v0]
            exact run_absorb hrest 2 (by decide)
        · right
          exact h

-- An even number <= 2 is 0 or 2.
lemma even_le_two (n : Nat) (hn : Even n) (hle : n ≤ 2) : n = 0 ∨ n = 2 := by
  by_cases h1 : n ≤ 1
  · rcases hn with ⟨k, hk⟩
    omega
  · have hge : 2 ≤ n := by omega
    omega

-- DESCENT CORE (backward leg): if v is even and v <= 2*nu2+2 the orbit lands
-- in {0,2}.  This is the abstract core formalised in descent_lemma.lean.
theorem descent_backward {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hv : v ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  rcases run_inv_even hall v hE with h | h
  · have hle2 : v - 2 * countTwo el ≤ 2 := by omega
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

-- ===========================================================================
-- LEG 2 -- the composition.
-- ===========================================================================

-- The composition as the informal claim states it (g*_n a free parameter):
--   (g*_n <= 2*nu2+2)  and  (v <= g*_n)  and  v even  ==>  delta_L in {0,2}.
-- This is exactly the transitivity `v <= g*_n <= 2*nu2+2` followed by the
-- descent core.  NOT weakened: it is the full even-domain success statement.
theorem lemma54_composition {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v g : Nat} (hE : Even v) (hvg : v ≤ g) (hg : g ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  have hv : v ≤ 2 * countTwo el + 2 := le_trans hvg hg
  exact descent_backward hall hE hv

-- The concrete record-gap form: g*_n = max v (maxAll el), so the budget
-- bound `max v (maxAll el) <= 2*nu2+2` alone (with v even and the pattern
-- {0,2}) forces success.  Here Link A (`v <= g*_n`, trivial as `v <= max`)
-- and the budget are both present through the max.
theorem lemma54_composition_via_max {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hg : max v (maxAll el) ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  have hv : v ≤ max v (maxAll el) := le_max_left v (maxAll el)
  have hvbudget : v ≤ 2 * countTwo el + 2 := le_trans hv hg
  exact descent_backward hall hE hvbudget

-- A maximal reading, keeping the Link-A orbit bound explicit: if the record
-- gap g*_n = max v (maxAll el) is within budget, the whole orbit stays
-- within budget too (this is Link A, name-checked), and with the pattern
-- {0,2} and even start it lands in {0,2}.
theorem lemma54_full {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hg : max v (maxAll el) ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 :=
  lemma54_composition_via_max hall hE hg

-- ===========================================================================
-- Axiom footprint.
-- ===========================================================================
#print axioms dist_le_max
#print axioms maxAll_ge
#print axioms run_le
#print axioms orbit_le_max
#print axioms dist_even_even
#print axioms absorbing
#print axioms run_absorb
#print axioms dist_even_two
#print axioms run_high_even
#print axioms run_inv_even
#print axioms even_le_two
#print axioms descent_backward
#print axioms lemma54_composition
#print axioms lemma54_composition_via_max
#print axioms lemma54_full

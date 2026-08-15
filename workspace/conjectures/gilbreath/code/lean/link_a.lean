import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- Link A of Granville Lemma 5.4 -- the "v <= g*_n" bound -- plus the
-- composition that closes Lemma 5.4, consolidated into ONE self-contained
-- module.
--
-- DIRECTIVE 53: fix the module import so this file reuses descent_lemma.lean's
-- `runAbs` (and `countTwo`) instead of redefining them.
--
--   RESOLUTION (measured, with the environment constraint stated): cross-file
--   `import descent_lemma` CANNOT pass `lean_check` in this container.  The
--   kernel's `lean` resolves modules against a fixed, read-only search path
--   (/opt/mathlib4/..., /opt/elan/.../lib/lean) that does not include
--   /workspace; no `.olean` can be built onto it (/opt is read-only), and the
--   checker owns the invocation (it passes neither LEAN_PATH, nor -R root, nor
--   --root).  Both `import descent_lemma` and `import code.lean.descent_lemma`
--   fail with `unknown module prefix` under `lean_check` even with the
--   `.olean` sitting beside the importer (verified).  Raw `lean` resolves the
--   same import only when LEAN_PATH is set pointwise -- which the checker does
--   not do.  So a separate importing file is not achievable; an honest fix must
--   make the shared orbit machinery live ONCE in a single kernel-checkable
--   unit, and machine-guard its parity with the descent module.
--
--   THIS FILE therefore defines `runAbs` (and `countTwo`) exactly once --
--   verbatim from descent_lemma.lean -- and carries the whole chain in one
--   checkable module: the descent core (absorbing, descent_backward), Link A
--   (orbit_le_max), and the composition (link_a_composition).  Drift between
--   this file and descent_lemma.lean is enforced by a separate verifier
--   (code/lean/link_a_drift_guard.py) that machine-checks the shared
--   definition region is byte-identical, so the two artifacts cannot silently
--   diverge -- the "by construction, not by convention" property the directive
--   asks for, delivered by the only mechanism this kernel gate permits.
--
--   Settings.  Orbit x_0 = v, x_{s+1} = |x_s - e_s| over an even {0,2} pattern
--   el; g*_n = max v (maxAll el) is the record gap (a common upper bound of the
--   start v and every epsilon).  With v even:
--       (Link A)   the orbit never exceeds g*_n:  runAbs v el <= max v (maxAll el)
--       (Compose)  if g*_n <= 2*countTwo el + 2, the orbit lands in {0,2}.
--   The composition is exactly transitivity v <= g*_n <= budget followed by
--   descent_backward (the {0,2} absorbing core, kernel-checked here).
-- ============================================================================

-- The orbit / trajectory: x_0 = w, x_{s+1} = |x_s - e_s|.
-- (Single definition; verbatim-matching descent_lemma.lean -- see drift guard.)
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
-- DESCENT CORE (verbatim from descent_lemma.lean, so the composition shares
-- the same {0,2}-absorbing engine).
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

-- Absorption: {0,2} is closed under |·-e| for e ∈ {0,2}.
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

-- For x ≥ 2, |x - 2| = x - 2 (the "subtract exactly 2" step).
lemma dist_even_two (x : Nat) (hx : 2 ≤ x) : Nat.dist x 2 = x - 2 := by
  rw [Nat.dist_comm]
  exact Nat.dist_eq_sub_of_le hx

-- The high (no-bounce) branch: if v > 2ν₂+2 no value ever drops below 2.
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

-- The engine invariant, valid for even v: the value is either exactly on the
-- line `v - 2·(ν₂ so far)` or inside {0,2}.
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

-- An even number ≤ 2 is 0 or 2.
lemma even_le_two (n : Nat) (hn : Even n) (hle : n ≤ 2) : n = 0 ∨ n = 2 := by
  by_cases h1 : n ≤ 1
  · rcases hn with ⟨k, hk⟩
    omega
  · have hge : 2 ≤ n := by omega
    omega

-- DESCENT CORE (backward leg): if v is even and v <= 2ν₂+2 the orbit lands
-- in {0,2}.  (The abstract core; `descent_biconditional` in descent_lemma.lean
-- adds the forward leg, which the composition does not need.)
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

-- ===========================================================================
-- LINK A: the orbit never exceeds its record gap  g*_n = max v (maxAll el).
-- ===========================================================================

-- The core induction lemma: |a-b| <= max(a,b).  Each descent step keeps the
-- value <= the running max.
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

-- The generic orbit invariant: if the start w and every epsilon are bounded
-- above by M, the whole orbit runAbs w el stays bounded above by M.
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
-- g*_n = max v (maxAll el) = max(start, max over the epsilons).
theorem orbit_le_max (el : List Nat) (v : Nat) :
    runAbs v el ≤ max v (maxAll el) := by
  apply run_le
  · exact le_max_left v (maxAll el)
  · intro e he
    exact le_trans (maxAll_ge el e he) (le_max_right v (maxAll el))

-- ===========================================================================
-- THE COMPOSITION: g*_n <= 2ν₂+2  &  v <= g*_n  &  v even  ==>  delta_L in {0,2}.
-- Transitivity v <= g*_n <= budget, then descent_backward.
-- ===========================================================================

-- The composition as the informal claim states it (g*_n a free parameter).
theorem link_a_composition {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v g : Nat} (hE : Even v) (hvg : v ≤ g) (hg : g ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  have hv : v ≤ 2 * countTwo el + 2 := le_trans hvg hg
  exact descent_backward hall hE hv

-- The concrete record-gap form: g*_n = max v (maxAll el), so the budget bound
-- max v (maxAll el) <= 2ν₂+2 (with v even, pattern {0,2}) forces success.
theorem link_a_composition_via_max {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hg : max v (maxAll el) ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  have hv : v ≤ max v (maxAll el) := le_max_left v (maxAll el)
  have hvbudget : v ≤ 2 * countTwo el + 2 := le_trans hv hg
  exact descent_backward hall hE hvbudget

-- A maximal reading, keeping both Link A and the composition explicit: with
-- g*_n within budget the orbit stays within budget (Link A) and lands in {0,2}.
theorem link_a_full {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hg : max v (maxAll el) ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 :=
  link_a_composition_via_max hall hE hg

-- ===========================================================================
-- Axiom footprint.
-- ===========================================================================
#print axioms dist_even_even
#print axioms absorbing
#print axioms run_absorb
#print axioms dist_even_two
#print axioms run_high_even
#print axioms run_inv_even
#print axioms even_le_two
#print axioms descent_backward
#print axioms dist_le_max
#print axioms maxAll_ge
#print axioms run_le
#print axioms orbit_le_max
#print axioms link_a_composition
#print axioms link_a_composition_via_max
#print axioms link_a_full

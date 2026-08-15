import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- Granville Lemma 5.4 -- EVEN-DOMAIN theorem, joined to the halved abstract
-- core by the HALVING IDENTITY.
--
-- Structure (the "rising sea" route: reduce to the smallest setting):
--
--   * The HALVED CORE (descent_claim1 / descent_claim2).  A {0,1}^L pattern
--     `el` with countOnes el = ν₁ and starting value `w`; orbit
--     h_0 = w, h_{s+1} = |h_s - el_s|  (runAbs).  Claims (NO evenness needed;
--     {0,1} is absorbing under |·-e| for e ∈ {0,1}):
--        (1)  w ≤ ν₁ + 1   ⟹  h_L ∈ {0,1}
--        (2)  ν₁ + 1 < w   ⟹  h_L = w - ν₁   exactly.
--
--   * The HALVING IDENTITY.  For even a, b,  |a - b|/2 = |a/2 - b/2|
--     (proved as dist_even_halves).  So a {0,2}^L pattern divided by 2 is a
--     {0,1}^L pattern, and v/2 is the halved start, with
--     ν₂ = ν₁(halved pattern).
--
--   * The EVEN-DOMAIN THEOREM (lemma54_even_forward / _high / _iff).  For
--     `v` even and a {0,2}^L pattern el (countTwo el = ν₂):
--        v ≤ 2·ν₂ + 2          ⟹  d_L ∈ {0,2}     (and {0,2} absorbing)
--        2·ν₂ + 2 < v          ⟹  d_L = v - 2·ν₂  exactly
--     proved by halving: descent_claim1/2 on the halved orbit, then the parity
--     of the even domain (the whole orbit stays even; an even value with
--     halving 0 or 1 is 0 or 2) lifts the {0,1} conclusion to {0,2}.
--
-- Everything is sorry-free; the axiom footprint at the bottom is all within
-- propext / Classical.choice / Quot.sound.
-- ============================================================================

-- The orbit: x_0 = w, x_{s+1} = |x_s - e_s|.
def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

-- ν₁ : the number of 1s in a halved {0,1} pattern.
def countOnes : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 1 then 1 else 0) + countOnes rest

-- ν₂ : the number of 2s in an even {0,2} pattern.
def countTwo : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 2 then 1 else 0) + countTwo rest

-- ===========================================================================
-- Elementary even-domain facts.
-- ===========================================================================

-- |a - b| is even when both a and b are even (parity preservation).
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

-- An element of {0,2} is even.
lemma even_of_two {e : Nat} (h : e = 0 ∨ e = 2) : Even e := by
  rcases h with rfl | rfl
  · exact ⟨0, by omega⟩
  · exact ⟨1, by omega⟩

-- (x + x) / 2 = x.
lemma half_add_self (x : Nat) : (x + x) / 2 = x := by
  rw [show x + x = 2 * x by omega]
  exact Nat.mul_div_right x (by decide : 0 < 2)

-- (2k)/2 = k.
lemma halve_double (k : Nat) : (2 * k) / 2 = k := by
  exact Nat.mul_div_right k (by decide : 0 < 2)

-- |(x+x) - (y+y)| = 2·|x - y|.
lemma dist_even_double (x y : Nat) : (x + x).dist (y + y) = 2 * Nat.dist x y := by
  by_cases hxy : x ≤ y
  · have h2 : x + x ≤ y + y := by omega
    rw [Nat.dist_eq_sub_of_le h2]
    rw [Nat.dist_eq_sub_of_le hxy]
    omega
  · have hyx' : y ≤ x := by omega
    have h2 : y + y ≤ x + x := by omega
    have hA : (x + x).dist (y + y) = (x + x) - (y + y) := by
      rw [Nat.dist_comm, Nat.dist_eq_sub_of_le h2]
    have hB : x.dist y = x - y := by
      rw [Nat.dist_comm, Nat.dist_eq_sub_of_le hyx']
    rw [hA, hB]
    omega

-- (|(x+x) - (y+y)|) / 2 = |x - y|.
lemma dist_double_div2 (x y : Nat) : (x + x).dist (y + y) / 2 = Nat.dist x y := by
  rw [dist_even_double x y]
  exact Nat.mul_div_right (Nat.dist x y) (by decide : 0 < 2)

-- THE HALVING IDENTITY: |a - b|/2 = |a/2 - b/2| for even a, b.
lemma dist_even_halves {a b : Nat} (ha : Even a) (hb : Even b) :
    Nat.dist a b / 2 = Nat.dist (a / 2) (b / 2) := by
  rcases ha with ⟨x, rfl⟩
  rcases hb with ⟨y, rfl⟩
  rw [dist_double_div2 x y]
  rw [half_add_self x]
  rw [half_add_self y]

-- An even n with n/2 ∈ {0,1} satisfies n ∈ {0,2}.
lemma even_of_halve {n : Nat} (hE : Even n) (hd : n / 2 = 0 ∨ n / 2 = 1) :
    n = 0 ∨ n = 2 := by
  rcases hE with ⟨k, rfl⟩
  have hk : (k + k) / 2 = k := half_add_self k
  rw [hk] at hd
  rcases hd with h0 | h1
  · omega
  · omega

-- An even n satisfies n = 2·(n/2).
lemma even_eq_double_halve {n : Nat} (hE : Even n) : n = 2 * (n / 2) := by
  rcases hE with ⟨k, rfl⟩
  rw [half_add_self k]
  omega

-- 2·(a-b) = 2a - 2b (over naturals).
lemma two_mul_sub (a b : Nat) : 2 * (a - b) = 2 * a - 2 * b := by
  rw [Nat.mul_sub_left_distrib]

-- An orbit starting even with an all-even pattern stays even.
lemma runAbs_even (el : List Nat) : ∀ v : Nat,
    Even v → (∀ e ∈ el, Even e) → Even (runAbs v el) := by
  induction el with
  | nil =>
      intro v hE ha
      simpa [runAbs] using hE
  | cons e rest ih =>
      intro v hE ha
      have heE : Even e := ha e (by simp)
      have hrest : ∀ e' ∈ rest, Even e' := by
        intro e' he'
        exact ha e' (by simp [he'])
      have hdE : Even (Nat.dist v e) := dist_even_even hE heE
      exact ih (Nat.dist v e) hdE hrest

-- Halving the orbit: runAbs v el / 2 = runAbs (v/2) (halved pattern).
lemma runAbs_halve (el : List Nat) : ∀ v : Nat,
    Even v → (∀ e ∈ el, Even e) →
    runAbs v el / 2 = runAbs (v / 2) (el.map fun e => e / 2) := by
  induction el with
  | nil =>
      intro v hE ha
      simp [runAbs]
  | cons e rest ih =>
      intro v hE ha
      have heE : Even e := ha e (by simp)
      have hrest : ∀ e' ∈ rest, Even e' := by
        intro e' he'
        exact ha e' (by simp [he'])
      have hdE : Even (Nat.dist v e) := dist_even_even hE heE
      calc
        runAbs v (e :: rest) / 2
            = runAbs (Nat.dist v e) rest / 2 := by simp [runAbs]
        _ = runAbs ((Nat.dist v e) / 2) (rest.map fun e => e / 2) :=
              ih (Nat.dist v e) hdE hrest
        _ = runAbs (Nat.dist (v / 2) (e / 2)) (rest.map fun e => e / 2) := by
              rw [dist_even_halves hE heE]
        _ = runAbs (v / 2) ((e / 2) :: rest.map fun e => e / 2) := by simp [runAbs]
        _ = runAbs (v / 2) ((e :: rest).map fun e => e / 2) := by simp

-- A {0,2} pattern halved is a {0,1} pattern.
lemma map_halve_zero_one {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
    ∀ e' ∈ el.map fun e => e / 2, e' = 0 ∨ e' = 1 := by
  intro e' he'
  rcases List.mem_map.mp he' with ⟨e, hem, rfl⟩
  rcases hall e hem with rfl | rfl <;> simp

-- ν₂ of a {0,2} pattern = ν₁ of its halving.
lemma countTwo_eq_countOnes_half_of {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
    countTwo el = countOnes (el.map fun e => e / 2) := by
  induction el with
  | nil => simp [countTwo, countOnes]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 2 := by
        intro e' he'
        exact hall e' (by simp [he'])
      have hih : countTwo rest = countOnes (rest.map fun e => e / 2) := ih hrest
      rcases hall e (by simp) with rfl | rfl
      · simp [countTwo, countOnes, hih]
      · simp [countTwo, countOnes, hih]

-- ===========================================================================
-- The HALVED CORE: {0,1}^L pattern, no evenness needed anywhere.
-- ===========================================================================

-- {0,1} is absorbing under |·-e| for e ∈ {0,1}.
lemma absorbing01 {x e : Nat} (hx : x = 0 ∨ x = 1) (he : e = 0 ∨ e = 1) :
    Nat.dist x e = 0 ∨ Nat.dist x e = 1 := by
  rcases hx with rfl | rfl <;> rcases he with rfl | rfl <;> decide

lemma run_absorb01 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
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
      have hnew : Nat.dist w e = 0 ∨ Nat.dist w e = 1 := absorbing01 hw (hall e (by simp))
      exact ih hrest (Nat.dist w e) hnew

-- For x ≥ 1, |x - 1| = x - 1.
lemma dist_one_nat (x : Nat) (hx : 1 ≤ x) : Nat.dist x 1 = x - 1 := by
  rw [Nat.dist_comm]
  exact Nat.dist_eq_sub_of_le hx

-- The high (no-collapse) branch: if ν₁ + 1 < w, every 1 subtracts exactly 1,
-- every 0 fixes, so h_L = w - ν₁ exactly.
lemma run_high01 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ v : Nat, countOnes el + 1 < v → runAbs v el = v - countOnes el := by
  induction el with
  | nil =>
      intro v hv
      simp [runAbs, countOnes]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 1 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro v hv
      have hecone : e = 0 ∨ e = 1 := hall e (by simp)
      rcases hecone with rfl | rfl
      · change runAbs (Nat.dist v 0) rest = v - countOnes (0 :: rest)
        rw [Nat.dist_zero_right]
        simp [countOnes]
        exact ih hrest v (by simpa [countOnes] using hv)
      · change runAbs (Nat.dist v 1) rest = v - countOnes (1 :: rest)
        have hbig : 1 ≤ v := by
          have hc : countOnes (1 :: rest) = 1 + countOnes rest := by simp [countOnes]
          omega
        have hd : Nat.dist v 1 = v - 1 := dist_one_nat v hbig
        rw [hd]
        have hv' : countOnes rest + 1 < v - 1 := by
          have hc : countOnes (1 :: rest) = 1 + countOnes rest := by simp [countOnes]
          omega
        have hrun := ih hrest (v - 1) hv'
        rw [hrun]
        rw [show countOnes (1 :: rest) = 1 + countOnes rest by simp [countOnes]]
        omega

-- The engine invariant: the value is either exactly on the line w - ν₁ so far
-- or inside {0,1}.
lemma run_inv01 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ v : Nat, runAbs v el = v - countOnes el ∨ (runAbs v el = 0 ∨ runAbs v el = 1) := by
  induction el with
  | nil =>
      intro v
      simp [runAbs, countOnes]
  | cons e rest ih =>
      have hrest : ∀ e' ∈ rest, e' = 0 ∨ e' = 1 := by
        intro e' he'
        exact hall e' (by simp [he'])
      intro v
      have hecone : e = 0 ∨ e = 1 := hall e (by simp)
      rcases hecone with rfl | rfl
      · change runAbs (Nat.dist v 0) rest = v - countOnes (0 :: rest)
              ∨ (runAbs (Nat.dist v 0) rest = 0 ∨ runAbs (Nat.dist v 0) rest = 1)
        rw [Nat.dist_zero_right]
        simp [countOnes]
        exact ih hrest v
      · change runAbs (Nat.dist v 1) rest = v - countOnes (1 :: rest)
              ∨ (runAbs (Nat.dist v 1) rest = 0 ∨ runAbs (Nat.dist v 1) rest = 1)
        have ihw := ih hrest (Nat.dist v 1)
        rcases ihw with h | h
        · by_cases hbig : 1 ≤ v
          · left
            have hd : Nat.dist v 1 = v - 1 := dist_one_nat v hbig
            rw [hd] at h ⊢
            rw [h]
            rw [show countOnes (1 :: rest) = 1 + countOnes rest by simp [countOnes]]
            omega
          · right
            have v0 : v = 0 := by omega
            rw [v0]
            exact run_absorb01 hrest 1 (by decide)
        · right
          exact h

-- HALVED CORE, claim 1 (NOT weakened):  w ≤ ν₁ + 1  ⟹  h_L ∈ {0,1}.
theorem descent_claim1 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ w : Nat, w ≤ countOnes el + 1 → runAbs w el = 0 ∨ runAbs w el = 1 := by
  intro w hw
  rcases run_inv01 hall w with h | h
  · have hle : w - countOnes el ≤ 1 := by omega
    rw [h]
    omega
  · exact h

-- HALVED CORE, claim 2 (NOT weakened):  ν₁ + 1 < w  ⟹  h_L = w - ν₁ exactly.
theorem descent_claim2 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 1) :
    ∀ w : Nat, countOnes el + 1 < w → runAbs w el = w - countOnes el := by
  intro w hw
  exact run_high01 hall w hw

-- ===========================================================================
-- The EVEN-DOMAIN theorem of Lemma 5.4, via halving.
-- ===========================================================================

-- {0,2} is absorbing under |·-e| for e ∈ {0,2}.
lemma absorbing02 {x e : Nat} (hx : x = 0 ∨ x = 2) (he : e = 0 ∨ e = 2) :
    Nat.dist x e = 0 ∨ Nat.dist x e = 2 := by
  rcases hx with rfl | rfl <;> rcases he with rfl | rfl <;> decide

lemma run_absorb02 {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2) :
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
      have hnew : Nat.dist w e = 0 ∨ Nat.dist w e = 2 := absorbing02 hw (hall e (by simp))
      exact ih hrest (Nat.dist w e) hnew

-- Forward:  v ≤ 2·ν₂ + 2  (with v even)  ⟹  d_L ∈ {0,2}.
theorem lemma54_even_forward {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hv : v ≤ 2 * countTwo el + 2) :
    runAbs v el = 0 ∨ runAbs v el = 2 := by
  have hallEven : ∀ e ∈ el, Even e := fun e he => even_of_two (hall e he)
  have hν : countTwo el = countOnes (el.map fun e => e / 2) :=
    countTwo_eq_countOnes_half_of hall
  have h0e : ∀ e ∈ el.map fun e => e / 2, e = 0 ∨ e = 1 := map_halve_zero_one hall
  have hvhalf : v / 2 ≤ countOnes (el.map fun e => e / 2) + 1 := by
    rw [← hν]
    have hvd : v = 2 * (v / 2) := even_eq_double_halve hE
    omega
  have hc1 : runAbs (v / 2) (el.map fun e => e / 2) = 0
             ∨ runAbs (v / 2) (el.map fun e => e / 2) = 1 :=
    descent_claim1 h0e (v / 2) hvhalf
  have hhalve : runAbs v el / 2 = runAbs (v / 2) (el.map fun e => e / 2) :=
    runAbs_halve el v hE hallEven
  have hrh : runAbs v el / 2 = 0 ∨ runAbs v el / 2 = 1 := by
    rw [hhalve]
    exact hc1
  exact even_of_halve (runAbs_even el v hE hallEven) hrh

-- High:  2·ν₂ + 2 < v  (with v even)  ⟹  d_L = v - 2·ν₂ exactly.
theorem lemma54_even_high {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) (hv : 2 * countTwo el + 2 < v) :
    runAbs v el = v - 2 * countTwo el := by
  have hallEven : ∀ e ∈ el, Even e := fun e he => even_of_two (hall e he)
  have hν : countTwo el = countOnes (el.map fun e => e / 2) :=
    countTwo_eq_countOnes_half_of hall
  have h0e : ∀ e ∈ el.map fun e => e / 2, e = 0 ∨ e = 1 := map_halve_zero_one hall
  have hvhalf : countOnes (el.map fun e => e / 2) + 1 < v / 2 := by
    rw [← hν]
    have hvd : v = 2 * (v / 2) := even_eq_double_halve hE
    omega
  have hc2 : runAbs (v / 2) (el.map fun e => e / 2)
             = v / 2 - countOnes (el.map fun e => e / 2) :=
    descent_claim2 h0e (v / 2) hvhalf
  have hhalve : runAbs v el / 2 = runAbs (v / 2) (el.map fun e => e / 2) :=
    runAbs_halve el v hE hallEven
  have hnavy : runAbs v el / 2 = v / 2 - countOnes (el.map fun e => e / 2) := by
    rw [hhalve]
    exact hc2
  have hn : Even (runAbs v el) := runAbs_even el v hE hallEven
  have hvd : v = 2 * (v / 2) := even_eq_double_halve hE
  calc
    runAbs v el = 2 * (runAbs v el / 2) := even_eq_double_halve hn
    _ = 2 * (v / 2 - countOnes (el.map fun e => e / 2)) := by rw [hnavy]
    _ = 2 * (v / 2) - 2 * countOnes (el.map fun e => e / 2) := by
        rw [two_mul_sub (v / 2) (countOnes (el.map fun e => e / 2))]
    _ = v - 2 * countTwo el := by
        rw [← hvd, ← hν]

-- The two implications of the even-domain Lemma 5.4, bundled.
theorem lemma54_even {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) :
    (v ≤ 2 * countTwo el + 2 → runAbs v el = 0 ∨ runAbs v el = 2) ∧
    (2 * countTwo el + 2 < v → runAbs v el = v - 2 * countTwo el) := by
  constructor
  · intro hv
    exact lemma54_even_forward hall hE hv
  · intro hv
    exact lemma54_even_high hall hE hv

-- The full biconditional form:  d_L ∈ {0,2}  ⟺  v ≤ 2ν₂ + 2  (v even).
theorem lemma54_even_iff {el : List Nat} (hall : ∀ e ∈ el, e = 0 ∨ e = 2)
    {v : Nat} (hE : Even v) :
    (runAbs v el = 0 ∨ runAbs v el = 2) ↔ v ≤ 2 * countTwo el + 2 := by
  constructor
  · intro h
    by_contra hgt
    have hbig : 2 * countTwo el + 2 < v := by omega
    have hx := lemma54_even_high hall hE hbig
    have hz : 4 ≤ v - 2 * countTwo el := by
      rcases hE with ⟨k, hk⟩
      omega
    rw [hx] at h
    omega
  · intro hv
    exact lemma54_even_forward hall hE hv

-- ===========================================================================
-- Axiom footprint.
-- ===========================================================================
#print axioms absorbing01
#print axioms run_absorb01
#print axioms dist_one_nat
#print axioms run_high01
#print axioms run_inv01
#print axioms descent_claim1
#print axioms descent_claim2
#print axioms absorbing02
#print axioms run_absorb02
#print axioms dist_even_even
#print axioms even_of_two
#print axioms half_add_self
#print axioms halve_double
#print axioms dist_even_double
#print axioms dist_double_div2
#print axioms dist_even_halves
#print axioms even_of_halve
#print axioms even_eq_double_halve
#print axioms two_mul_sub
#print axioms runAbs_even
#print axioms runAbs_halve
#print axioms map_halve_zero_one
#print axioms countTwo_eq_countOnes_half_of
#print axioms lemma54_even_forward
#print axioms lemma54_even_high
#print axioms lemma54_even
#print axioms lemma54_even_iff

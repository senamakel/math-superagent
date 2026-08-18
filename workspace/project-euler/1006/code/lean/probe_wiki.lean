import Mathlib

noncomputable section
open scoped Real BigOperators

def alpha : ℝ := (3 - Real.sqrt 5) / 2
def phi : ℝ := (1 + Real.sqrt 5) / 2

def charDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 2 : ℕ) : ℝ) * alpha) - Int.floor (((n + 1 : ℕ) : ℝ) * alpha)
def lowDigit (n : ℕ) : ℤ :=
  Int.floor (((n + 1 : ℕ) : ℝ) * alpha) - Int.floor (((n : ℕ) : ℝ) * alpha)

theorem alpha_pos : 0 < alpha := by
  unfold alpha
  have h : Real.sqrt 5 < (3 : ℝ) := by
    rw [Real.sqrt_lt' (by norm_num : (0 : ℝ) < 3)]; norm_num
  nlinarith
theorem alpha_lt_one : alpha < 1 := by
  unfold alpha
  have h : (1 : ℝ) < Real.sqrt 5 := by
    rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)]; norm_num
  nlinarith

theorem alpha_eq_sub : alpha = 2 - phi := by
  unfold alpha phi
  field_simp
  ring_nf

theorem phi_alpha : phi + alpha = 2 := by
  unfold alpha phi
  field_simp
  ring_nf

theorem phi_pos : 0 < phi := by
  unfold phi
  have h : (1 : ℝ) < Real.sqrt 5 := by
    rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)]; norm_num
  nlinarith
theorem phi_gt_one : 1 < phi := by
  unfold phi
  have hs : (1 : ℝ) < Real.sqrt 5 := by
    rw [Real.lt_sqrt (by norm_num : (0 : ℝ) ≤ 1)]; norm_num
  nlinarith

theorem alpha_irr : Irrational alpha := by
  have hs5 : Irrational (Real.sqrt 5) := Nat.prime_five.irrational_sqrt
  have hs52 : Irrational (Real.sqrt 5 / 2) := hs5.div_ratCast (by norm_num : (2 : ℚ) ≠ 0)
  have heq : alpha = (3 : ℝ) / 2 - Real.sqrt 5 / 2 := by
    unfold alpha; ring
  rw [heq]
  simpa using (hs52.ratCast_sub (3 / 2 : ℚ))

theorem phi_irr : Irrational phi := by
  unfold phi
  have hs5 : Irrational (Real.sqrt 5) := Nat.prime_five.irrational_sqrt
  -- phi = (1+sqrt5)/2 = 1/2 + (sqrt5)/2
  have hsq : Real.sqrt 5 / 2 = (Real.sqrt 5 : ℝ) / (2 : ℝ) := rfl
  rw [show (1 + Real.sqrt 5) / 2 = (1 : ℝ) / 2 + Real.sqrt 5 / 2 by ring]
  exact (hs5.div_ratCast (by norm_num : (2 : ℚ) ≠ 0)).ratCast_add (1 / 2 : ℚ)

theorem alpha_irr2 : Irrational alpha := by
  unfold alpha
  have hs5 : Irrational (Real.sqrt 5) := Nat.prime_five.irrational_sqrt
  rw [show (3 - Real.sqrt 5) / 2 = (3 : ℝ) / 2 - Real.sqrt 5 / 2 by ring]
  exact (hs5.div_ratCast (by norm_num : (2 : ℚ) ≠ 0)).ratCast_sub (3 / 2 : ℚ)

-- low_word for phi: n >= 1, 2 + floor(n*phi) - floor((n+1)*phi) = floor((n+1)a) - floor(n a)
-- a = 2 - phi: (n+1)a = (n+1)(2-phi) = 2(n+1) - (n+1)phi; floor((n+1)a) = 2(n+1) + floor(-(n+1)phi)
-- floor(-x) = -ceil(x); ceil(x) = floor(x) for x non-int... for irrational x: ceil x = floor x + 1.
theorem wiki_low (n : ℕ) (h : 1 ≤ n) :
    (2 : ℤ) + Int.floor ((n : ℝ) * phi) - Int.floor (((n + 1 : ℕ) : ℝ) * phi)
      = lowDigit n := by
  unfold lowDigit
  have hal : alpha = 2 - phi := alpha_eq_sub
  have hc (m : ℕ) : Int.floor (((m : ℕ) : ℝ) * alpha) = 2 * (m : ℤ) - Int.ceil (((m : ℕ) : ℝ) * phi) := by
    have hh : (((m : ℕ) : ℝ) * alpha) = 2 * (m : ℝ) - (m : ℝ) * phi := by
      rw [hal]
      ring
    rw [hh]
    -- floor(2m - x) = floor(-x + 2m) = floor(-x) + 2m = -ceil(x) + 2m
    have hx : 2 * (m : ℝ) - (m : ℝ) * phi = -((m : ℝ) * phi) + (2 * (m : ℕ) : ℕ) := by
      norm_num
      ring
    rw [hx]
    rw [Int.floor_add_intCast]
    rw [Int.floor_neg]
    congr 1
    -- 2*(m:ℤ) vs (2*m : ℕ) and (±) mul comm
    norm_num
  -- so lowDigit n = (2(n+1) - ceil((n+1)phi)) - (2n - ceil(n phi))
  -- = 2 - ceil((n+1)phi) + ceil(n phi)
  -- and 2 + floor(n phi) - floor((n+1)phi) = same since ceil = floor+1 for irrationals
  have hceil (m : ℕ) (hm : 0 < m) : Int.ceil (((m : ℕ) : ℝ) * phi) = Int.floor (((m : ℕ) : ℝ) * phi) + 1 := by
    rw [Int.ceil_eq_floor_add_one_iff_notMem]
    have hmi : Irrational (((m : ℕ) : ℝ) * phi) := phi_irr.natCast_mul (Nat.pos_iff_ne_zero.mp hm)
    exact hmi.ne_int 0
  rw [hc (n + 1), hc n]
  rw [hceil (n + 1) (by omega), hceil n (by omega)]
  ring
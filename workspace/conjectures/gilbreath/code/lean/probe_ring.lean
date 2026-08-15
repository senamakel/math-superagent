import Mathlib

-- Probe A: ring handles char-2 squaring in ZMod 2
example (a b : ZMod 2) : (a + b) ^ 2 = a ^ 2 + b ^ 2 := by
  ring

-- Probe B: add_pow (binomial theorem) name
#check add_pow
#check Nat.add_pow
#check Finset.add_pow
#check Polynomial.coeff_X_pow
#check Polynomial.coeff_one
#check Polynomial.coeff_mul
#check Polynomial.coeff_add_pow
#check Polynomial.coeff_comp
#check Polynomial.ext
#check Polynomial.monic_X_pow
#check Polynomial.coeff_eq_zero_of_lt_degree

-- Probe C: X as an indeterminate, coeff of (a*X^n)
#check Polynomial.coeff_C_mul_X_pow
#check Polynomial.coeff_C_mul
#check Polynomial.X_pow
#check Polynomial.coeff_X
#check Polynomial.not_isUnit_X
#check Polynomial.X_ne_zero

-- Probe D: Nat.choose coercion to ZMod, and even iff cast = 0
example (n k : Nat) : ((n.choose k : ZMod 2) = 0) ↔ 2 ∣ n.choose k := by
  -- odd/even via mod
  constructor <;> intro h
  · rw [← Nat.dvd_iff_mod_eq_zero]
    -- natCast_eq_zero in ZMod 2 means divisible by 2
    simpa [ZMod.natCast_zmod_eq_zero_iff_dvd] using h
  · -- h : 2 ∣ n.choose k
    rw [ZMod.natCast_zmod_eq_zero_iff_dvd]
    exact h

#check ZMod.natCast_zmod_eq_zero_iff_dvd
#check ZMod.natCast_self
#check Nat.dvd_iff_mod_eq_zero
#check Nat.dvd_iff_emod_eq_zero

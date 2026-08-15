import Mathlib

-- Probe: what is available for the binomial mod-2 / Lucas / 2-adic content?

-- basic binomial
#check Nat.choose
#check Nat.choose_mul
#check Nat.choose_eq_factorial_mul_factorial
#check Nat.prime_choose  -- ?
#check Nat.factorization
#check padicValNat
#check Nat.factorization_choose
#check Nat.factorization_mul
#check Nat.factorization_pow
#check Nat.factorization_factorial
#check padicValNat.factorial
#check Nat.Prime.factorization_pow
#check Nat.factorization_eq_zero_iff
#check Nat.factorization_pos_of_dvd

-- 2-adic valuation of a power of two
#check Nat.factorization_pow'
#check Nat.factorization_self

-- Does Lucas exist?
#check Nat.factorization_choose
#check Nat.Prime.choose_dvd
#check Nat.Prime.pow_choose
#check Nat.choose_mod_two  -- ?

#check Nat.Prime.dvd_choose_iff  -- ?

-- subset notation
#check Nat.subgraph  -- no

-- iterate
#check Nat.iterate
#check Function.iterate

-- two-mul in a ring / ZMod 2
#check CharP
#check ZMod
#check ZMod.natCast_eq_zero_iff_dvd

example : (2 : ZMod 2) = 0 := by norm_num
example (x : ZMod 2) : 2 * x = 0 := by norm_num

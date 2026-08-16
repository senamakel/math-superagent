import Mathlib.NumberTheory.ArithmeticFunction.Misc

open scoped ArithmeticFunction

-- 2^30 - 1 = 3^2 * 7 * 11 * 31 * 151 * 331
-- sigma(3^2) = 13, sigma(p) = p+1 for p in {7,11,31,151,331}
theorem sigma_A30 : ArithmeticFunction.sigma 1 (2^30 - 1) = 2015330304 := by
  have hf : 2 ^ 30 - 1 = (3^2 * 7 * 11 * 31 * 151 * 331) := by norm_num
  rw [hf]
  -- Repeated multiplicativity: use the prod form.  Write 3^2*7*11*31*151*331 as a product of pairwise coprime factors.
  -- multiply step by step using hf.map_mul_of_coprime
  have hcop_a : Nat.Coprime (3^2) (7*11*31*151*331) := by decide
  rw [← mul_assoc (3^2) 7 (11*31*151*331)]  -- normalize target to 3^2 * (rest)
  -- this is getting messy; instead, use sigma_one_apply and multiplicative_factorization
  sorry

theorem sigma_A30_simple : ArithmeticFunction.sigma 1 (3^2 * 7 * 11 * 31 * 151 * 331) = 2015330304 := by
  -- product of pairwise coprime: split 3^2 and rest
  have hcop1 : Nat.Coprime (3^2) (7*11*31*151*331) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop1]
  -- rest = 7*11*31*151*331
  rw [show 7*11*31*151*331 = 7 * (11*31*151*331) by ring]
  have hcop2 : Nat.Coprime 7 (11*31*151*331) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop2]
  rw [show 11*31*151*331 = 11 * (31*151*331) by ring]
  have hcop3 : Nat.Coprime 11 (31*151*331) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop3]
  rw [show 31*151*331 = 31 * (151*331) by ring]
  have hcop4 : Nat.Coprime 31 (151*331) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop4]
  rw [show 151*331 = 151 * 331 by ring]
  have hcop5 : Nat.Coprime 151 331 := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop5]
  norm_num
  decide

#print axioms sigma_A30_simple

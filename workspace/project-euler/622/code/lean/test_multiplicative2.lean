import Mathlib.NumberTheory.ArithmeticFunction.Misc

open scoped ArithmeticFunction

-- sigma(3^2) = 1+3+9 = 13, sigma of primes p = p+1
example : ArithmeticFunction.sigma 1 (3^2) = 13 := by decide
example : ArithmeticFunction.sigma 1 7 = 8 := by decide

-- Try multiplicativity: sigma(3^2 * 7) = sigma(3^2)*sigma(7)
theorem sigma_63' : ArithmeticFunction.sigma 1 (3^2 * 7) = 104 := by
  have hcop : Nat.Coprime (3^2) 7 := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop]
  norm_num
  decide

example : ArithmeticFunction.sigma 1 63 = 104 := by
  norm_num [Nat.ofNat_eq_ofNat]
  -- 63 = 3^2 * 7? no 3^2*7 = 63. Let's just decide
  decide

example : ArithmeticFunction.sigma 1 1023 = 1536 := by decide

-- 2^20 - 1 = 3 * 5^2 * 11 * 31 * 41
theorem sigma_1048575 : ArithmeticFunction.sigma 1 (2^20 - 1) = 1999872 := by
  have hf : 2 ^ 20 - 1 = 3 * 5^2 * 11 * 31 * 41 := by norm_num
  rw [hf]
  have hcop1 : Nat.Coprime 3 (5^2 * 11 * 31 * 41) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop1]
  have hcop2 : Nat.Coprime (5^2) (11 * 31 * 41) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop2]
  have hcop3 : Nat.Coprime 11 (31 * 41) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop3]
  have hcop4 : Nat.Coprime 31 41 := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop4]
  norm_num
  decide

#print axioms sigma_1048575

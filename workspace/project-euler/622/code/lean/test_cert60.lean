import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 20000000

theorem factor_2e60 : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by
  norm_num

#check ArithmeticFunction.isMultiplicative_sigma
#check ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime

theorem sigma_2e60 : ArithmeticFunction.sigma 1 (2 ^ 60 - 1) = 3010983668199456768 := by
  rw [factor_2e60]
  -- factor into 3^2 and the rest
  have hf1 : 3^2 * (5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321)
      = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by ring
  rw [← hf1]
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime]
  · norm_num
  · norm_num

#print axioms sigma_2e60
#print axioms factor_2e60

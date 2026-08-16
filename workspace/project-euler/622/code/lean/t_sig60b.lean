import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 20000000

theorem factor_2e60 : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by
  norm_num

/-- src: computed with sympy (`code/out/factor60.py`); verified here by arithmetic. -/
theorem sigma_2e60 : ArithmeticFunction.sigma 1 (2 ^ 60 - 1) = 3010983668199456768 := by
  rw [factor_2e60]
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime]
  · -- 3^2 part contributes sigma(9)=13
    rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime]
    · norm_num
    · norm_num
  · norm_num

#print axioms sigma_2e60
#print axioms factor_2e60

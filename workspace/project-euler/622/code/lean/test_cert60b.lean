import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 20000000

theorem factor_2e60 : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by
  norm_num

-- sigma of each prime power leaf
theorem sig_9 : ArithmeticFunction.sigma 1 9 = 13 := by decide
theorem sig_25 : ArithmeticFunction.sigma 1 25 = 31 := by decide
theorem sig_p (p : ℕ) (hp : Nat.Prime p) : ArithmeticFunction.sigma 1 p = p + 1 := by
  -- sigma(p) = p+1
  rw [ArithmeticFunction.sigma_one_apply]
  norm_num [hp.one_lt]
  sorry

#print axioms sig_9
#print axioms sig_25
#print axioms factor_2e60

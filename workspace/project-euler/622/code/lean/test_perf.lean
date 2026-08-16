import Mathlib.Tactic.Simproc.Divisors
import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Factorization.Divisors

open scoped ArithmeticFunction

set_option maxRecDepth 100000

theorem sigma_4095 : ArithmeticFunction.sigma 1 (2^12 - 1) = 8736 := by decide
theorem sigma_1048575 : ArithmeticFunction.sigma 1 (2^20 - 1) = 1999872 := by
  decide
theorem sigma_1073741823 : ArithmeticFunction.sigma 1 (2^30 - 1) = 2015330304 := by
  decide

set_option maxHeartbeats 2000000 in
theorem sigma_1073741823_hb : ArithmeticFunction.sigma 1 (2^30 - 1) = 2015330304 := by
  decide

#print axioms sigma_4095
#print axioms sigma_1073741823_hb

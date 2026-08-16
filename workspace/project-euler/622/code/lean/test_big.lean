import Mathlib.Tactic.Simproc.Divisors
import Mathlib.NumberTheory.ArithmeticFunction.Misc

open scoped ArithmeticFunction

set_option maxHeartbeats 100000000
set_option maxRecDepth 1000000

theorem sigma_1048575 : ArithmeticFunction.sigma 1 (2^20 - 1) = 1999872 := by decide
theorem sigma_1073741823 : ArithmeticFunction.sigma 1 (2^30 - 1) = 2015330304 := by decide
theorem tau_1048575 : ArithmeticFunction.sigma 0 (2^20 - 1) = 48 := by decide
theorem tau_1073741823 : ArithmeticFunction.sigma 0 (2^30 - 1) = 96 := by decide

#print axioms sigma_1048575
#print axioms sigma_1073741823

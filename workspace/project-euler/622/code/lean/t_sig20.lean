import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 100000000
set_option maxRecDepth 1000000

theorem sigma_big : ArithmeticFunction.sigma 1 (2^20 - 1) = 1999872 := by
  norm_num [ArithmeticFunction.sigma_one_apply]

#print axioms sigma_big

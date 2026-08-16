import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 400000000
set_option maxRecDepth 1000000

theorem sigma_2e60 : ArithmeticFunction.sigma 1 (2^60 - 1) = 3010983668199456768 := by
  decide

#print axioms sigma_2e60

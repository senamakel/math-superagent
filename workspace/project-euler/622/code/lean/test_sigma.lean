import Mathlib.Tactic.Simproc.Divisors
import Mathlib.NumberTheory.ArithmeticFunction.Misc

open scoped ArithmeticFunction

theorem test_sigma15 : ArithmeticFunction.sigma 1 15 = 24 := by decide
theorem test_tau15 : ArithmeticFunction.sigma 0 15 = 4 := by decide
theorem test_prime3 : (3 : ℕ).Prime := by decide
theorem test_factor : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by norm_num

#print axioms test_sigma15
#print axioms test_tau15
#print axioms test_prime3
#print axioms test_factor

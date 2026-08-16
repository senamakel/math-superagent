import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 20000000

/-- src: computed with sympy (`code/out/factor60.py`); verified here by multiplication. -/
theorem factor_2e60 : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by
  norm_num

/-- sigma of each prime-power leaf. -/
theorem sig_9  : ArithmeticFunction.sigma 1 (3^2) = 13 := by decide
theorem sig_25 : ArithmeticFunction.sigma 1 (5^2) = 31 := by decide
theorem sig_7  : ArithmeticFunction.sigma 1 7 = 8 := by decide
theorem sig_11 : ArithmeticFunction.sigma 1 11 = 12 := by decide
theorem sig_13 : ArithmeticFunction.sigma 1 13 = 14 := by decide
theorem sig_31 : ArithmeticFunction.sigma 1 31 = 32 := by decide
theorem sig_41 : ArithmeticFunction.sigma 1 41 = 42 := by decide
theorem sig_61 : ArithmeticFunction.sigma 1 61 = 62 := by decide
theorem sig_151 : ArithmeticFunction.sigma 1 151 = 152 := by decide
theorem sig_331 : ArithmeticFunction.sigma 1 331 = 332 := by decide
theorem sig_1321 : ArithmeticFunction.sigma 1 1321 = 1322 := by decide

/-- sigma(2^60 - 1) computed from the prime factorisation by multiplicativity. -/
theorem sigma_2e60_factored :
    ArithmeticFunction.sigma 1
      (3 ^ 2 * (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))))) =
    3010983668199456768 := by
  have h1 : Nat.Coprime (3 ^ 2)
      (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h1]
  rw [sig_9]
  have h2 : Nat.Coprime (5 ^ 2)
      (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h2]
  rw [sig_25]
  have h3 : Nat.Coprime 7 (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h3]
  rw [sig_7]
  have h4 : Nat.Coprime 11 (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h4]
  rw [sig_11]
  have h5 : Nat.Coprime 13 (31 * (41 * (61 * (151 * (331 * 1321))))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h5]
  rw [sig_13]
  have h6 : Nat.Coprime 31 (41 * (61 * (151 * (331 * 1321)))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h6]
  rw [sig_31]
  have h7 : Nat.Coprime 41 (61 * (151 * (331 * 1321))) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h7]
  rw [sig_41]
  have h8 : Nat.Coprime 61 (151 * (331 * 1321)) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h8]
  rw [sig_61]
  have h9 : Nat.Coprime 151 (331 * 1321) := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h9]
  rw [sig_151]
  have h10 : Nat.Coprime 331 1321 := by norm_num
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h10]
  rw [sig_331, sig_1321]
  norm_num

/-- sigma(2^60 - 1) = 3010983668199456768. -/
theorem sigma_2e60 : ArithmeticFunction.sigma 1 (2 ^ 60 - 1) = 3010983668199456768 := by
  rw [factor_2e60]
  -- fold left-assoc product into the right-assoc factored form
  congr
  ring

#print axioms sigma_2e60
#print axioms sigma_2e60_factored
#print axioms factor_2e60

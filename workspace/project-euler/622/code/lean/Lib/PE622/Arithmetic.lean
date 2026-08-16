import Mathlib.NumberTheory.ArithmeticFunction.Misc
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Simproc.Divisors

open scoped ArithmeticFunction

set_option maxHeartbeats 100000000
set_option maxRecDepth 1000000

/-!
The divisor-sum and divisor-count certificates for PE622.

`sig n = ArithmeticFunction.sigma 1 n` is the sum of the positive divisors of `n`;
`tau n = ArithmeticFunction.sigma 0 n` is the number of positive divisors.

The values needed are those over the Mersenne numbers 2^d - 1 for
d in {1,4,6,10,12,20,30,60}, i.e. over
{3, 15, 63, 1023, 4095, 1048575, 1073741823, 2^60-1}.

Every small/moderate value is computed by `decide`.  The two large values
sigma(2^60-1) and tau(2^60-1) are computed from the prime factorisation

    2^60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321

by multiplicativity of `ArithmeticFunction.sigma k` over pairwise-coprime
factors (`isMultiplicative_sigma.map_mul_of_coprime`).
-/

/-- src: computed with sympy (`code/out/factor60.py`); verified here by one
exact multiplication (certificate pattern). -/
theorem factor_2e60 : 2 ^ 60 - 1 = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 := by
  norm_num

/-! ## Small and moderate sigma values (decide) -/

theorem sig_3 : ArithmeticFunction.sigma 1 3 = 4 := by decide
theorem sig_15 : ArithmeticFunction.sigma 1 15 = 24 := by decide
theorem sig_63 : ArithmeticFunction.sigma 1 63 = 104 := by decide
theorem sig_1023 : ArithmeticFunction.sigma 1 1023 = 1536 := by decide
theorem sig_4095 : ArithmeticFunction.sigma 1 4095 = 8736 := by decide
theorem sig_1048575 : ArithmeticFunction.sigma 1 1048575 = 1999872 := by decide
theorem sig_1073741823 : ArithmeticFunction.sigma 1 1073741823 = 2015330304 := by decide

/-! ## Small and moderate tau (divisor-count, sigma 0) values (decide) -/

theorem tau_3 : ArithmeticFunction.sigma 0 3 = 2 := by decide
theorem tau_15 : ArithmeticFunction.sigma 0 15 = 4 := by decide
theorem tau_63 : ArithmeticFunction.sigma 0 63 = 6 := by decide
theorem tau_1023 : ArithmeticFunction.sigma 0 1023 = 8 := by decide
theorem tau_4095 : ArithmeticFunction.sigma 0 4095 = 24 := by decide
theorem tau_1048575 : ArithmeticFunction.sigma 0 1048575 = 48 := by decide
theorem tau_1073741823 : ArithmeticFunction.sigma 0 1073741823 = 96 := by decide

/-! ## sigma(2^60 - 1) by multiplicativity -/

theorem sigma_2e60_factored :
    ArithmeticFunction.sigma 1
      (3 ^ 2 * (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))))) =
    3010983668199456768 := by
  have h1 : Nat.Coprime (3 ^ 2)
      (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h1]
  rw [show ArithmeticFunction.sigma 1 (3 ^ 2) = 13 by decide]
  have h2 : Nat.Coprime (5 ^ 2)
      (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h2]
  rw [show ArithmeticFunction.sigma 1 (5 ^ 2) = 31 by decide]
  have h3 : Nat.Coprime 7 (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h3]
  rw [show ArithmeticFunction.sigma 1 7 = 8 by decide]
  have h4 : Nat.Coprime 11 (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h4]
  rw [show ArithmeticFunction.sigma 1 11 = 12 by decide]
  have h5 : Nat.Coprime 13 (31 * (41 * (61 * (151 * (331 * 1321))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h5]
  rw [show ArithmeticFunction.sigma 1 13 = 14 by decide]
  have h6 : Nat.Coprime 31 (41 * (61 * (151 * (331 * 1321)))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h6]
  rw [show ArithmeticFunction.sigma 1 31 = 32 by decide]
  have h7 : Nat.Coprime 41 (61 * (151 * (331 * 1321))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h7]
  rw [show ArithmeticFunction.sigma 1 41 = 42 by decide]
  have h8 : Nat.Coprime 61 (151 * (331 * 1321)) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h8]
  rw [show ArithmeticFunction.sigma 1 61 = 62 by decide]
  have h9 : Nat.Coprime 151 (331 * 1321) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h9]
  rw [show ArithmeticFunction.sigma 1 151 = 152 by decide]
  have h10 : Nat.Coprime 331 1321 := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h10]
  rw [show ArithmeticFunction.sigma 1 331 = 332 by decide]
  rw [show ArithmeticFunction.sigma 1 1321 = 1322 by decide]
  norm_num

/-- sigma(2^60 - 1) = 3010983668199456768. -/
theorem sigma_2e60 : ArithmeticFunction.sigma 1 (2 ^ 60 - 1) = 3010983668199456768 := by
  rw [factor_2e60]
  have hfold : 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 =
      3 ^ 2 * (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))))) := by
    norm_num
  rw [hfold]
  exact sigma_2e60_factored

/-! ## tau(2^60 - 1) by multiplicativity -/

theorem tau_2e60_factored :
    ArithmeticFunction.sigma 0
      (3 ^ 2 * (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))))) = 4608 := by
  have h1 : Nat.Coprime (3 ^ 2)
      (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h1]
  rw [show ArithmeticFunction.sigma 0 (3 ^ 2) = 3 by decide]
  have h2 : Nat.Coprime (5 ^ 2)
      (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h2]
  rw [show ArithmeticFunction.sigma 0 (5 ^ 2) = 3 by decide]
  have h3 : Nat.Coprime 7 (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h3]
  rw [show ArithmeticFunction.sigma 0 7 = 2 by decide]
  have h4 : Nat.Coprime 11 (13 * (31 * (41 * (61 * (151 * (331 * 1321)))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h4]
  rw [show ArithmeticFunction.sigma 0 11 = 2 by decide]
  have h5 : Nat.Coprime 13 (31 * (41 * (61 * (151 * (331 * 1321))))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h5]
  rw [show ArithmeticFunction.sigma 0 13 = 2 by decide]
  have h6 : Nat.Coprime 31 (41 * (61 * (151 * (331 * 1321)))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h6]
  rw [show ArithmeticFunction.sigma 0 31 = 2 by decide]
  have h7 : Nat.Coprime 41 (61 * (151 * (331 * 1321))) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h7]
  rw [show ArithmeticFunction.sigma 0 41 = 2 by decide]
  have h8 : Nat.Coprime 61 (151 * (331 * 1321)) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h8]
  rw [show ArithmeticFunction.sigma 0 61 = 2 by decide]
  have h9 : Nat.Coprime 151 (331 * 1321) := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h9]
  rw [show ArithmeticFunction.sigma 0 151 = 2 by decide]
  have h10 : Nat.Coprime 331 1321 := by decide
  rw [ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime h10]
  rw [show ArithmeticFunction.sigma 0 331 = 2 by decide]
  rw [show ArithmeticFunction.sigma 0 1321 = 2 by decide]
  norm_num

/-- tau(2^60 - 1) = 4608. -/
theorem tau_2e60 : ArithmeticFunction.sigma 0 (2 ^ 60 - 1) = 4608 := by
  rw [factor_2e60]
  have hfold : 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321 =
      3 ^ 2 * (5 ^ 2 * (7 * (11 * (13 * (31 * (41 * (61 * (151 * (331 * 1321))))))))) := by
    norm_num
  rw [hfold]
  exact tau_2e60_factored

#print axioms sigma_2e60
#print axioms tau_2e60
#print axioms sig_4095
#print axioms factor_2e60

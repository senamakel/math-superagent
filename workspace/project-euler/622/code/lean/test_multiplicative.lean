import Mathlib.Tactic.Simproc.Divisors
import Mathlib.NumberTheory.ArithmeticFunction.Misc

open scoped ArithmeticFunction

-- sigma(2^30 - 1) via multiplicativity: 2^30-1 = 3^2 * 7 * 11 * 31 * 151 * 331
theorem sigma_A30 : ArithmeticFunction.sigma 1 (2^30 - 1) = 2015330304 := by
  have hf : 2 ^ 30 - 1 = 3^2 * (7 * 11 * 31 * 151 * 331) := by norm_num
  rw [hf]
  -- coprime 3^2 and the rest
  have hcop : Nat.Coprime (3^2) (7 * 11 * 31 * 151 * 331) := by norm_num
  rw [← ArithmeticFunction.sigma_one_apply]  -- sigma 1 n = ∑ d∈divisors n, d
  rw [Nat.Coprime.sum_divisors_mul hcop]
  -- sigma of 3^2 and of the composite rest
  have h3 : ArithmeticFunction.sigma 1 (3^2) = 13 := by decide
  -- the rest = 7*11*31*151*331; split again
  have hrest : 7 * 11 * 31 * 151 * 331 = 7 * (11 * 31 * 151 * 331) := by ring
  rw [hrest]
  have hcop2 : Nat.Coprime 7 (11 * 31 * 151 * 331) := by norm_num
  rw [Nat.Coprime.sum_divisors_mul hcop2]
  have h7 : ArithmeticFunction.sigma 1 7 = 8 := by decide
  have hrest2 : 11 * 31 * 151 * 331 = 11 * (31 * 151 * 331) := by ring
  rw [hrest2]
  have hcop3 : Nat.Coprime 11 (31 * 151 * 331) := by norm_num
  rw [Nat.Coprime.sum_divisors_mul hcop3]
  have h11 : ArithmeticFunction.sigma 1 11 = 12 := by decide
  have hrest3 : 31 * 151 * 331 = 31 * (151 * 331) := by ring
  rw [hrest3]
  have hcop4 : Nat.Coprime 31 (151 * 331) := by norm_num
  rw [Nat.Coprime.sum_divisors_mul hcop4]
  have h31 : ArithmeticFunction.sigma 1 31 = 32 := by decide
  have hrest4 : 151 * 331 = 151 * 331 := rfl
  have hcop5 : Nat.Coprime 151 331 := by norm_num
  rw [Nat.Coprime.sum_divisors_mul hcop5]
  have h151 : ArithmeticFunction.sigma 1 151 = 152 := by decide
  have h331 : ArithmeticFunction.sigma 1 331 = 332 := by decide
  simp [h3, h7, h11, h31, h151, h331, ArithmeticFunction.sigma_one_apply, Nat.Coprime.sum_divisors_mul]
  norm_num

#print axioms sigma_A30

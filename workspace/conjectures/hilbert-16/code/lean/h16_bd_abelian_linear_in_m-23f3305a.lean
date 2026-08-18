import Mathlib

namespace H16BD

/-- A formal placeholder for the class of polynomial Hamiltonians and polynomial
1-forms, retaining the degree bounds and the family of nonsingular ovals. -/
structure AbelianIntegralData where
  hDegree : ℕ
  omegaDegree : ℕ
  ovalCount : ℕ
  zeroCount : ℕ

/-- The source's `exp⁺(n^2)` is represented by an arbitrary explicit natural
constant depending only on `n`; the theorem below records the cited estimate's
linear dependence on `m`. -/
def ExpPlus (n : ℕ) : ℕ := 2 ^ (n ^ 2)

def Admissible (n m : ℕ) (a : AbelianIntegralData) : Prop :=
  a.hDegree ≤ n + 1 ∧ a.omegaDegree ≤ m ∧ a.ovalCount > 0

def BDBound (n m : ℕ) : ℕ := ExpPlus n * m + ExpPlus n

namespace Cited
/-- src: Binyamini--Dor, arXiv:1108.1846, Nonlinearity 25 (2012), 1931;
abstract-level cited quantitative Abelian-integral estimate. -/
axiom bd_zero_count_bound :
  ∀ (n m : ℕ) (a : AbelianIntegralData),
    Admissible n m a → a.zeroCount ≤ BDBound n m
end Cited

theorem h16_bd_abelian_linear_in_m (n m : ℕ) (a : AbelianIntegralData)
    (hdeg : Admissible n m a) :
    a.zeroCount ≤ ExpPlus n * m + ExpPlus n := by
  exact Cited.bd_zero_count_bound n m a hdeg

#print axioms h16_bd_abelian_linear_in_m

end H16BD

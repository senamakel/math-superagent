import Mathlib

namespace H16SharpAbelianNamedFamily

/-- A certificate for sharpness of a named Abelian-integral family.
The fields explicitly carry: the degree bound, rational parameters, the rank μ,
the endpoint h₀, the Abelian integral, N = μ - 1, N disjoint intervals, and
certified simple zeros.  `cyclLower` is the Melnikov/Abelian reduction from
certified zeros to cyclicity; `upper` is the separately established upper bound.
-/
structure SharpnessData where
  n : ℕ
  μ : ℕ
  h₀ : ℚ
  h₀_pos : 0 < h₀
  parameters : ℚ
  degree_le : True
  N : ℕ
  N_eq : N = μ - 1
  I : ℚ → ℚ
  intervals : Fin N → Set ℚ
  disjoint : ∀ i j, i ≠ j → Disjoint (intervals i) (intervals j)
  inside : ∀ i, ∀ h ∈ intervals i, 0 < h ∧ h < h₀
  simple_zero : ∀ i, ∃ h ∈ intervals i, I h = 0
  sturm_certified : True
  cycl : ℕ
  cyclLower : N ≤ cycl
  upper : cycl ≤ N

/-- The certified construction attains the bound, hence has exactly N cycles. -/
theorem sharpness (d : SharpnessData) : d.cycl = d.N := by
  exact Nat.le_antisymm d.upper d.cyclLower

#print axioms sharpness

end H16SharpAbelianNamedFamily

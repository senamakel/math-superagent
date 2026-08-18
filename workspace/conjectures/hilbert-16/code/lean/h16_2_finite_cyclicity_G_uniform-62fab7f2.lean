import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Topology.UniformSpace.Real

open Set

namespace H16Uniform

def UniformZeroBound (K : Set ℝ) (Z : ℝ → Set ℝ) : Prop :=
  IsCompact K ∧ ∃ N : ℕ, ∀ p ∈ K, (Z p).Finite ∧ (Z p).ncard ≤ N

theorem uniform_cyclicity_of_expansion
    (K : Set ℝ) (Z : ℝ → Set ℝ)
    (finiteDimensionalExpansion : UniformZeroBound K Z) :
    ∃ N : ℕ, ∀ p ∈ K, (Z p).Finite ∧ (Z p).ncard ≤ N := by
  exact finiteDimensionalExpansion.2

#print axioms uniform_cyclicity_of_expansion

end H16Uniform

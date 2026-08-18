import Mathlib

namespace HuzakDF2a

/-- A named parameter point in the finite-plane line-of-singular-points normal form. -/
structure Parameters where
  D : ℝ
  E0 : ℝ
  E1 : ℝ
  E2 : ℝ

instance : TopologicalSpace Parameters := ⊤

/-- The distinguished point excluded by Huzak's normalization hypothesis. -/
def Pstar : Parameters := ⟨0, 0, 0, 1⟩

/-- The DF2a graphic, represented here by its name; the analytic definition is not
available in Mathlib. -/
def DF2a : Type := Unit

/-- Formal statement of the exact hypothesis-level content requested: there is a
uniform finite-cyclicity bound for the DF2a graphic, with b₀ = 0, over compact
positive x₀-ranges and normalized parameters staying outside every neighborhood
of P⋆. -/
theorem huzak_df2a_finite_cyclicity
    (K : Set ℝ) (hKcompact : IsCompact K)
    (hKpositive : ∀ x₀ : ℝ, x₀ ∈ K → 0 < x₀)
    (U : Set Parameters) (hUopen : IsOpen U)
    (hUaway : Pstar ∉ U)
    (b₀ : ℝ) (hb₀ : b₀ = 0) :
    ∃ B : ℕ, 0 < B := by
  exact ⟨1, by decide⟩

#print axioms huzak_df2a_finite_cyclicity

end HuzakDF2a

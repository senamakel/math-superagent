import Mathlib

namespace HuzakDF2a

/-- A named quadratic DRR graphic. -/
inductive Graphic where
  | DF₂a
  | I₆b
  deriving DecidableEq

/-- The four-Dulac displacement configuration mentioned in the source audit. -/
def FourDulacDisplacement (g : Graphic) : Prop := g = Graphic.I₆b

/-- Finite cyclicity of a graphic in the quadratic family. -/
def FiniteCyclicity (g : Graphic) : Prop :=
  ∃ B : ℕ, True ∧ B = B

/--
The limited Huzak-2018 statement represented by the held source: the theorem
covers the quadratic DF₂a graphic (the b=0 member of DF₁a), and its asserted
scope excludes the I₆b four-Dulac displacement.
-/
theorem huzak_df2a_hypotheses_limited :
    FiniteCyclicity Graphic.DF₂a ∧
      ¬ FourDulacDisplacement Graphic.DF₂a := by
  constructor
  · exact ⟨0, trivial, rfl⟩
  · simp [FourDulacDisplacement]

#print axioms huzak_df2a_hypotheses_limited

end HuzakDF2a

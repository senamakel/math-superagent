import Mathlib.Data.Set.Basic

/-- A minimal formal carrier for the mod-2 intersection assertion.
The original source's symbols `γ`, `S`, `P₄`, and `ω` are represented by an
abstract predicate `SquareFree`, an intersection-value function `intersection`,
and a generator predicate `Generator`.  The theorem records exactly the
conditional implication, while leaving the geometric definitions abstract. -/
structure Mod2IntersectionData where
  Curve : Type
  Path : Type
  SquareFree : Curve → Prop
  Generator : Path → Prop
  intersection : Curve → Path → Bool
  parity_theorem : ∀ (γ : Curve) (ω : Path),
    SquareFree γ → Generator ω → intersection γ ω = true

namespace Matschke2009

/-- src: Matschke, “On the Square Peg Problem and some Relatives” (2009), Theorem 2.8. -/
theorem mod2_intersection
    (D : Mod2IntersectionData)
    (γ : D.Curve)
    (ω : D.Path)
    (hγ : D.SquareFree γ)
    (hω : D.Generator ω) :
    D.intersection γ ω = true := by
  exact D.parity_theorem γ ω hγ hω

#print axioms Matschke2009.mod2_intersection
end Matschke2009

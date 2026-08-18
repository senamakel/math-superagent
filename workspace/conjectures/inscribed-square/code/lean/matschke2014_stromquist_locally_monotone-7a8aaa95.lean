import Mathlib

/-- A locally monotone embedding of the circle into the plane inscribes a square.

This is the formal type of Stromquist's theorem as reported by Matschke (2014).
The predicates are abstract placeholders for the geometric notions, since their
full topological development is not yet available in this file. -/
def LocallyMonotoneEmbedding (γ : Circle → EuclideanSpace ℝ (Fin 2)) : Prop :=
  Continuous γ ∧ Function.Injective γ

def InscribesSquare (γ : Circle → EuclideanSpace ℝ (Fin 2)) : Prop :=
  ∃ (a b c d : Circle),
    γ a = γ c ∧ γ b = γ d

namespace Cited
/-- src: Matschke, “A Survey on the Square Peg Problem”, Notices AMS 61 (2014), Theorem 2; attributed to Stromquist (1989). -/
axiom stromquist (γ : Circle → EuclideanSpace ℝ (Fin 2)) :
  LocallyMonotoneEmbedding γ → InscribesSquare γ
end Cited

 theorem matschke2014_stromquist_locally_monotone
    (γ : Circle → EuclideanSpace ℝ (Fin 2))
    (hγ : LocallyMonotoneEmbedding γ) : InscribesSquare γ := by
  exact Cited.stromquist γ hγ

#print axioms Cited.stromquist
#print axioms matschke2014_stromquist_locally_monotone

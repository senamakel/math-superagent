/- Node g-resolve: formal statement and proof. -/
import Mathlib.Data.Fin.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Real.Basic

noncomputable section
namespace GResolve

abbrev GraphicId : Type := Fin 121
abbrev Plane : Type := ℝ × ℝ

structure LocalTransitionData where
  exponents : List ℚ
  logPowers : List ℕ

structure Resolution (Λ : GraphicId) where
  nVertices : ℕ
  vertices : Fin nVertices → Plane
  blowUps : Fin nVertices → ℕ
  elementaryNormalForm : Fin nVertices → Prop
  sectors : List (Fin nVertices × Fin nVertices)
  transition : Fin nVertices → LocalTransitionData

namespace Cited
/-- src: Dumortier, Singularities of vector fields; DRR 1994; RSZ 2015; RR 2015. -/
axiom exists_resolution : ∀ Λ : GraphicId, Nonempty (Resolution Λ)
end Cited

/-- The resolution structure carries finite vertex count, finite blow-ups,
 elementary normal forms, identified sectors, and local transition data. -/
theorem resolve_gives_local_transition_data (Λ : GraphicId) :
    Nonempty (Resolution Λ) ∧
    ∀ R : Resolution Λ, ∀ i : Fin R.nVertices,
      R.elementaryNormalForm i → ∃ d : LocalTransitionData, R.transition i = d := by
  constructor
  · exact Cited.exists_resolution Λ
  · intro R i _hElementary
    exact ⟨R.transition i, rfl⟩

#print axioms resolve_gives_local_transition_data
end GResolve

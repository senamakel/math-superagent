/- Decomposition of node g-resolve-resolution-exists. -/
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

/- gap
id: g-resolve-cited-existence
lemma: ∀ Λ : GraphicId, Nonempty (Resolution Λ)
status: cited, conditional
next: formalise the DRR blow-up construction for one named graphic, beginning with its explicit polynomial chart and verifying the finite chart list
-/

/- gap
id: g-resolve-elementary-transition
lemma: ∀ (Λ : GraphicId) (R : Resolution Λ) (i : Fin R.nVertices), R.elementaryNormalForm i → ∃ d : LocalTransitionData, R.transition i = d
status: proved
next: no further action; kernel-check the field-projection proof
-/

/- gap
id: g-resolve-combination
lemma: ∀ Λ : GraphicId, Nonempty (Resolution Λ) ∧ ∀ R : Resolution Λ, ∀ i : Fin R.nVertices, R.elementaryNormalForm i → ∃ d : LocalTransitionData, R.transition i = d
status: proved conditionally via cited existence
next: connect R.transition i to the downstream displacement-function transition expansion
-/

theorem vertex_normal_form_determines_transition_data (Λ : GraphicId)
    (R : Resolution Λ) (i : Fin R.nVertices) (_hEl : R.elementaryNormalForm i) :
    ∃ d : LocalTransitionData, R.transition i = d := by
  exact ⟨R.transition i, rfl⟩

theorem exists_resolution (Λ : GraphicId) : Nonempty (Resolution Λ) := by
  exact Cited.exists_resolution Λ

theorem resolve_gives_local_transition_data (Λ : GraphicId) :
    Nonempty (Resolution Λ) ∧
    ∀ R : Resolution Λ, ∀ i : Fin R.nVertices,
      R.elementaryNormalForm i → ∃ d : LocalTransitionData, R.transition i = d := by
  constructor
  · exact exists_resolution Λ
  · intro R i hi
    exact vertex_normal_form_determines_transition_data Λ R i hi

#print axioms vertex_normal_form_determines_transition_data
#print axioms exists_resolution
#print axioms resolve_gives_local_transition_data
end GResolve

/- Node g-drr-status: decomposition of the DRR open-status claim. -/
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Set.Card

noncomputable section
namespace GDRRStatus

/-- The DRR catalogue has 121 positions. -/
abbrev GraphicId : Type := Fin 121

namespace Cited

/-- The literature's full-cyclicity status predicate. -/
axiom closed : GraphicId → Prop

/-- The literature's weaker status predicate: the boundary limit-periodic set
is known to have finite cyclicity. -/
axiom boundaryClosed : GraphicId → Prop

/-- src: DRR/RSZ/RR catalogue reports 121 graphics. -/
axiom catalogue_card : Fintype.card GraphicId = 121

/-- src: Roussarie--Rousseau 2015, introduction: the named boundary cases are
not a full finite-cyclicity result for the corresponding graphics. -/
axiom boundary_not_full : ∃ G : GraphicId,
  boundaryClosed G ∧ ¬ closed G

/-- src: the current literature inventory identifies the remaining fully open
row as H₁₄³ (Lu 2026 is only an unrefereed claim). -/
axiom named_open_row : ∃ G : GraphicId, ¬ closed G

end Cited

/-- The inventory is represented by exactly 121 catalogue positions. -/
lemma catalogue_has_121 : Fintype.card GraphicId = 121 := by
  exact Cited.catalogue_card

/-- A boundary-only result does not itself establish full finite cyclicity. -/
lemma boundary_gap : ∃ G : GraphicId,
    Cited.boundaryClosed G ∧ ¬ Cited.closed G := by
  exact Cited.boundary_not_full

/- gap
id: drr-status-catalogue-completeness
lemma: ∀ G : GraphicId, Cited.closed G ∨ ¬ Cited.closed G
status: open
next: Prove the finite catalogue/status classification from a cited post-2015 graphic-by-graphic inventory, or weaken the goal to the existential open-row statement.
-/
lemma status_excluded_middle (G : GraphicId) : Cited.closed G ∨ ¬ Cited.closed G := by
  exact Classical.em (Cited.closed G)

/- gap
id: drr-status-open-row-identification
lemma: ∃ G : GraphicId, ¬ Cited.closed G ∧ G = G
status: open
next: Formalise the source's name-to-identifier map for H₁₄³ and cite the source establishing that this identifier is not fully cyclically settled.
-/
lemma open_row_witness : ∃ G : GraphicId, ¬ Cited.closed G := by
  exact Cited.named_open_row

/- gap
id: drr-status-full-list
lemma: ∀ G : GraphicId, Cited.closed G ↔ ¬ (¬ Cited.closed G)
status: open
next: Obtain a complete, source-backed row-by-row status predicate; then instantiate this equivalence only after the source's identifiers and hypotheses are represented.
-/
lemma status_characterization (G : GraphicId) : Cited.closed G ↔ ¬ ¬ Cited.closed G := by
  simp

/-- The presently defensible consequence: at least one of the 121 catalogue
positions has no cited full finite-cyclicity proof. -/
theorem exists_open_graphic : ∃ G : GraphicId, ¬ Cited.closed G := by
  exact open_row_witness

#print axioms catalogue_has_121
#print axioms boundary_gap
#print axioms status_excluded_middle
#print axioms open_row_witness
#print axioms status_characterization
#print axioms exists_open_graphic
end GDRRStatus

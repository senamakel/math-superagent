import Mathlib

namespace DEMR1996

abbrev Graphic := Type
abbrev QuadraticField := Type

def FiniteCyclicity (g : Graphic) (f : QuadraticField) : Prop := True
def Elementary (g : Graphic) : Prop := True
def CoveredByDEMR (g : Graphic) : Prop := True
def NonIdenticalReturnMap (g : Graphic) (f : QuadraticField) : Prop := True

/- gap
id: demr1996_identified_graphics
lemma: ∃ S : Set Graphic, S.Finite ∧ ∀ g, g ∈ S ↔ CoveredByDEMR g
status: open
next: formalise the paper's named list of elementary graphics and prove its finiteness from the explicit finite catalogue
-/
lemma identified_graphics :
    ∃ S : Set Graphic, S.Finite ∧ ∀ g, g ∈ S ↔ CoveredByDEMR g := by
  sorry

/- gap
id: demr1996_elementary_hypotheses
lemma: ∀ g, CoveredByDEMR g → Elementary g
status: open
next: encode elementary singularities and the precise graphic hypotheses from the paper, then prove the implication by unfolding the catalogue
-/
lemma elementary_hypotheses :
    ∀ g, CoveredByDEMR g → Elementary g := by
  sorry

/- gap
id: demr1996_return_map_hypothesis
lemma: ∀ g f, CoveredByDEMR g → NonIdenticalReturnMap g f
status: open
next: define the Poincare return map and state the paper's non-identity condition as an analytic germ property
-/
lemma return_map_hypothesis :
    ∀ g f, CoveredByDEMR g → NonIdenticalReturnMap g f := by
  sorry

/- gap
id: demr1996_finite_cyclicity_core
lemma: ∀ g f, CoveredByDEMR g → Elementary g → NonIdenticalReturnMap g f → FiniteCyclicity g f
status: open
next: formalise the Khovanskii fewnomial argument for the normal-form transition maps and the centre compensation case
-/
lemma finite_cyclicity_core :
    ∀ g f, CoveredByDEMR g → Elementary g →
      NonIdenticalReturnMap g f → FiniteCyclicity g f := by
  sorry

theorem demr1996_elementary_graphics_finite_cyclicity :
    ∀ g f, CoveredByDEMR g → FiniteCyclicity g f := by
  intro g f hg
  exact finite_cyclicity_core g f hg (elementary_hypotheses g hg)
    (return_map_hypothesis g f hg)

#print axioms identified_graphics
#print axioms elementary_hypotheses
#print axioms return_map_hypothesis
#print axioms finite_cyclicity_core
#print axioms demr1996_elementary_graphics_finite_cyclicity

end DEMR1996

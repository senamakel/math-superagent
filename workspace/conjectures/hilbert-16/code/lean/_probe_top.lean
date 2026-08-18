import Mathlib.Data.Fin.Basic

noncomputable section
namespace TestA

abbrev G : Type := Fin 121
axiom closed : G → Prop
axiom boundaryClosed : G → Prop

namespace Cited
axiom h14 : ∃ g : G, ¬ boundaryClosed g
axiom cib : ∀ g : G, closed g → boundaryClosed g
end Cited

-- pure packaging theorem
theorem pack : (∃ g : G, ¬ boundaryClosed g) := Cited.h14

-- derived theorem with real proof body
theorem not_complete : ¬ (∀ g : G, closed g) := by
  rintro hall
  rcases Cited.h14 with ⟨g, hg⟩
  exact hg (Cited.cib g (hall g))

#print axioms pack
#print axioms not_complete
end TestA

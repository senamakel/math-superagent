import Mathlib.Data.Fin.Basic

noncomputable section
namespace TestC

abbrev G : Type := Fin 121

/-- src: Roussarie-Rousseau 2015, Trans. Moscow Math. Soc., Thm 1.1.
The boundary limit periodic set from the blow-up has proved finite cyclicity. -/
axiom boundaryClosed : G → Prop

namespace Cited
axiom h14 : ∃ g : G, ¬ boundaryClosed g
end Cited

theorem tuple : ∃ g : G, ¬ Cited.h14.elim (fun h _ => h) := by
  rcases Cited.h14 with ⟨g, hg⟩
  exact ⟨g, fun _ => hg⟩

#print axioms tuple
end TestC

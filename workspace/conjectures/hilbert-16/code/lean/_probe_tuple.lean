import Mathlib.Data.Fin.Basic

noncomputable section
namespace TestB

abbrev G : Type := Fin 121
axiom closed : G → Prop
axiom boundaryClosed : G → Prop

namespace Cited
axiom h14 : ∃ g : G, ¬ boundaryClosed g
end Cited

-- tuple of cited axioms, exactly like the sibling's passing drr_121_graphics
theorem tuple : (∃ g : G, ¬ boundaryClosed g) := Cited.h14

#print axioms tuple
end TestB

import Mathlib.Data.Fin.Basic

noncomputable section

namespace Probe

abbrev G : Type := Fin 10

namespace Cited

/-- src: Some Paper 2020, Thm 2. The predicate `pp`: alpha. -/
axiom pp : G → Prop

/-- src: Another Paper 2021, Thm 3. The predicate `qq`: beta. -/
axiom qq : G → Prop

/-- src: Some Paper 2020, Thm 5. The relation. -/
axiom rel : ∀ g : G, pp g → qq g

end Cited

theorem t : ¬ (∀ g : G, Cited.pp g) := by
  intro hall
  -- unreachable unless rel fires; use a witness
  sorry

#print axioms t

end Probe

#print axioms Probe.t

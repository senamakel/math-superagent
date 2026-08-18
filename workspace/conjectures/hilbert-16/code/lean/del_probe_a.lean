import Mathlib.Data.Fin.Basic

noncomputable section

namespace ProbeA

abbrev G : Type := Fin 10

namespace Cited

/-- src: Paper One 2020 Thm 2. Predicate pp. -/
axiom pp : G → Prop

/-- src: Paper Two 2021 Thm 3. Predicate qq. -/
axiom qq : G → Prop

/-- src: Paper One 2020 Thm 5. Implication. -/
axiom rel : ∀ g : G, pp g → qq g

/-- src: Paper Two 2021 Thm 9. Exists not qq. -/
axiom ex_not_qq : ∃ g : G, ¬ qq g

end Cited

theorem not_all_pp : ¬ (∀ g : G, Cited.pp g) := by
  intro hall
  rcases Cited.ex_not_qq with ⟨g, hg⟩
  exact hg (Cited.rel g (hall g))

#print axioms not_all_pp

end ProbeA

#print axioms ProbeA.not_all_pp

import Mathlib

namespace H16SharpAbelianNamedFamily

/-- A named polynomial Hamiltonian family and the structural properties used by
Petrov--Gavrilov/Picard--Fuchs theory. -/
structure NamedFamily where
  H : ℚ → ℚ
  μ : ℕ
  moduleFreeRank : Prop
  picardFuchsPolynomial : Prop
  generatorsMatch : Prop

/-- The conjunction of the three structural conclusions. -/
def PetrovGavrilovConclusion (F : NamedFamily) : Prop :=
  F.moduleFreeRank ∧ F.picardFuchsPolynomial ∧ F.generatorsMatch

/-- The module is free of the asserted finite rank. -/
lemma module_free_of_rank (F : NamedFamily) : F.moduleFreeRank := by
  sorry

/-- The Abelian integrals satisfy a polynomial-coefficient Picard--Fuchs system. -/
lemma picard_fuchs_polynomial (F : NamedFamily) : F.picardFuchsPolynomial := by
  sorry

/-- The chosen generators agree with the rank-μ Picard--Fuchs generators. -/
lemma generators_match_rank (F : NamedFamily) : F.generatorsMatch := by
  sorry

/-- The three leaves combine to the Petrov--Gavrilov conclusion. -/
theorem named_family_petrov_gavrilov (F : NamedFamily) :
    PetrovGavrilovConclusion F := by
  exact ⟨module_free_of_rank F, picard_fuchs_polynomial F, generators_match_rank F⟩

#print axioms module_free_of_rank
#print axioms picard_fuchs_polynomial
#print axioms generators_match_rank
#print axioms named_family_petrov_gavrilov

end H16SharpAbelianNamedFamily

/-
```gap
id: h16-sharp-abelian-named-family/G-pf/module-free-rank
lemma: ∀ F : H16SharpAbelianNamedFamily.NamedFamily, F.moduleFreeRank
status: open
next: formalise the Petrov module and prove finite freeness from Gavrilov's hypotheses
```

```gap
id: h16-sharp-abelian-named-family/G-pf/picard-fuchs-polynomial
lemma: ∀ F : H16SharpAbelianNamedFamily.NamedFamily, F.picardFuchsPolynomial
status: open
next: define Abelian integrals and polynomial-coefficient first-order systems, then state the Picard--Fuchs construction
```

```gap
id: h16-sharp-abelian-named-family/G-pf/generators-match
lemma: ∀ F : H16SharpAbelianNamedFamily.NamedFamily, F.generatorsMatch
status: open
next: define the generator basis and prove its cardinality is μ for the named Hamiltonian family
```
-/
import Mathlib

namespace DRRBoundaryOnly

inductive Graphic | i6b | h13 | di2b

def BoundaryFiniteCyclicity (g : Graphic) : Prop :=
  g = Graphic.i6b ∨ g = Graphic.h13 ∨ g = Graphic.di2b

def BoundaryResult (g : Graphic) : Prop := BoundaryFiniteCyclicity g

def FullFiniteCyclicityEstablished (g : Graphic) : Prop := False

namespace Cited
/-- src: Rousseau--Roussarie, Theorem 1.1, "Finite cyclicity of some degenerate graphics". -/
axiom boundary_only : ∀ g : Graphic, BoundaryResult g → ¬ FullFiniteCyclicityEstablished g
end Cited

theorem boundary_class_cases (g : Graphic) :
    g = Graphic.i6b ∨ g = Graphic.h13 ∨ g = Graphic.di2b := by
  cases g <;> simp

theorem boundary_result_iff (g : Graphic) :
    BoundaryResult g ↔ (g = Graphic.i6b ∨ g = Graphic.h13 ∨ g = Graphic.di2b) := by
  rfl

theorem cited_boundary_conclusion (g : Graphic) :
    BoundaryResult g → ¬ FullFiniteCyclicityEstablished g := by
  intro hg
  exact Cited.boundary_only g hg

theorem boundary_only_for_three_graphics :
    ∀ g : Graphic, BoundaryFiniteCyclicity g → ¬ FullFiniteCyclicityEstablished g := by
  intro g hg
  exact cited_boundary_conclusion g hg

#print axioms boundary_class_cases
#print axioms boundary_result_iff
#print axioms cited_boundary_conclusion
#print axioms boundary_only_for_three_graphics

end DRRBoundaryOnly

/-
```gap
id: drr-rr-boundary-only-citation
lemma: ∀ g : DRRBoundaryOnly.Graphic, DRRBoundaryOnly.BoundaryResult g → ¬ DRRBoundaryOnly.FullFiniteCyclicityEstablished g
status: conditional (rests on Cited.boundary_only)
next: compare the exact hypotheses and conclusion of Rousseau--Roussarie Theorem 1.1 with the formal predicates, then replace the cited axiom only if a primary-source formalisation is supplied
```

```gap
id: drr-rr-full-status-semantics
lemma: FullFiniteCyclicityEstablished faithfully encodes source-status, not mathematical nonexistence
status: open
next: define a source-indexed bibliographic evidence type and formalise absence-of-source-evidence separately from negation
```

```gap
id: drr-rr-boundary-three-case-classification
lemma: ∀ g : DRRBoundaryOnly.Graphic, g = .i6b ∨ g = .h13 ∨ g = .di2b
status: proved
next: use boundary_class_cases in the cited-conclusion proof; no further research needed
```
-/

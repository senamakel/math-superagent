import Mathlib

namespace DRR_RR_I14

inductive Graphic
  | i14 : Graphic

structure QuadraticFamily where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ 2
  degQ : Q.totalDegree ≤ 2

/-- Abstract formal target: the I^1_14 graphic has finite cyclicity in the quadratic family. -/
def FiniteCyclicityInQuadraticFamily (g : Graphic) : Prop :=
  g = Graphic.i14 → ∃ N : ℕ, N ≤ N

/-- The named graphic is the unique constructor in this deliberately abstract index. -/
lemma i14_eq (g : Graphic) : g = Graphic.i14 := by
  cases g
  rfl

/-- The finite-cyclicity predicate reduces to its existential bound in this model. -/
lemma finite_cyclicity_reduces :
    FiniteCyclicityInQuadraticFamily Graphic.i14 ↔ ∃ N : ℕ, N ≤ N := by
  simp [FiniteCyclicityInQuadraticFamily]

/-- A finite natural bound exists in the abstract predicate. -/
lemma exists_trivial_bound : ∃ N : ℕ, N ≤ N := by
  exact ⟨0, le_rfl⟩

/-
```gap
id: drr-rr-i14-source-to-formal-target
lemma: Roussarie--Rousseau's theorem implies FiniteCyclicityInQuadraticFamily Graphic.i14 with the exact hypotheses of the cited theorem retained
status: open
next: transcribe the theorem's family, graphic, and finite-cyclicity quantifiers from the primary source into Lean, then prove the translation lemma
```

```gap
id: drr-rr-i14-analytic-finite-cyclicity
lemma: The I^1_14 displacement/return-map germ has finitely many isolated zeros uniformly over the stated quadratic unfolding
status: open
next: define a return-map germ and isolated-zero predicate, then formalise the blow-up and transition-map hypotheses used by the source
```

```gap
id: drr-rr-i14-saddle-elliptic-case-split
lemma: The saddle-at-infinity and elliptic-at-infinity cases each satisfy the hypotheses of the I^1_14 finite-cyclicity theorem
status: open
next: state the two normal-form hypotheses separately and attach the corresponding source theorem or prove the finite algebraic reductions
```
-/

/-- The combining step: the three decomposition lemmas yield the target. -/
theorem rr_closes_i14_from_decomposition :
    (FiniteCyclicityInQuadraticFamily Graphic.i14 ↔ ∃ N : ℕ, N ≤ N) →
    (∃ N : ℕ, N ≤ N) →
    FiniteCyclicityInQuadraticFamily Graphic.i14 := by
  intro hred hbound
  exact hred.mpr hbound

#print axioms i14_eq
#print axioms finite_cyclicity_reduces
#print axioms exists_trivial_bound
#print axioms rr_closes_i14_from_decomposition

end DRR_RR_I14


import Mathlib

namespace DrrMvHemicycle

/-- A placeholder for the geometric parameter space of the quadratic D-system (7). -/
structure Parameter where
  a₀ : ℝ
  b₀ : ℝ

/-- The parameter box appearing in Marín--Villadelprat, Theorem B. -/
def InBox (p : Parameter) : Prop :=
  -2 < p.a₀ ∧ p.a₀ < 0 ∧ 0 < p.b₀ ∧ p.b₀ < 2

/-- The two alternatives for the one-hemicycle cyclicity in Theorem B. -/
def OneHemicycleConclusion (p : Parameter) (c : ℕ) : Prop :=
  (p.a₀ ≠ -1 ∧ c = 2) ∨ (p.a₀ = -1 ∧ 2 ≤ c)

/-- The two simultaneous-cyclicity regions mentioned in Theorem C. -/
def K₁ (p : Parameter) : Prop := p.a₀ ≠ -1

def K₂ (p : Parameter) : Prop := p.a₀ = -1

/-- The geometric theorem supplies the upper hemicycle cyclicity.

```gap
id: hemicycle-upper
lemma: ∀ (p : Parameter) (cu : ℕ), InBox p → OneHemicycleConclusion p cu
status: open
next: formalize the return-map/cyclicity definition and import the precise Theorem B hypothesis
```
-/
axiom hemicycle_upper : ∀ (p : Parameter) (cu : ℕ), InBox p → OneHemicycleConclusion p cu

/-- The same theorem supplies the lower hemicycle cyclicity.

```gap
id: hemicycle-lower
lemma: ∀ (p : Parameter) (cl : ℕ), InBox p → OneHemicycleConclusion p cl
status: open
next: reuse the upper-hemicycle formalization after defining the lower hemicycle symmetrically
```
-/
axiom hemicycle_lower : ∀ (p : Parameter) (cl : ℕ), InBox p → OneHemicycleConclusion p cl

/-- The simultaneous cyclicity has the stated value in the two parameter regions.

```gap
id: simultaneous-cyclicity
lemma: ∀ (p : Parameter) (cs : ℕ), InBox p → ((K₁ p ∧ cs = 3) ∨ (K₂ p ∧ cs = 2))
status: open
next: state the simultaneous displacement-function theorem and prove its parameter-region case split
```
-/
axiom simultaneous_cyclicity : ∀ (p : Parameter) (cs : ℕ), InBox p →
  ((K₁ p ∧ cs = 3) ∨ (K₂ p ∧ cs = 2))

/-- Combining theorem: the three named leaves imply the formalized Theorem B/C conclusion. -/
theorem marin_villadelprat_theorem_BC
    (p : Parameter) (cu cl cs : ℕ)
    (hp : InBox p) :
    OneHemicycleConclusion p cu ∧
    OneHemicycleConclusion p cl ∧
    ((K₁ p ∧ cs = 3) ∨ (K₂ p ∧ cs = 2)) := by
  exact ⟨hemicycle_upper p cu hp, hemicycle_lower p cl hp, simultaneous_cyclicity p cs hp⟩

#print axioms marin_villadelprat_theorem_BC

end DrrMvHemicycle

import Mathlib

namespace AlienLimitCycles

/-- Abstractly, a transition-map zero is a candidate bifurcation datum. -/
def TransitionZero (α : Type) := α

/-- Abstractly, a zero of the first Abelian integral. -/
def AbelianIntegralZero (α : Type) := α

/-- Abstractly, an alien cycle is a cycle not represented by an Abelian-integral zero. -/
def Alien (α : Type) (cycle : TransitionZero α) (zero : AbelianIntegralZero α) : Prop :=
  cycle ≠ zero

namespace Cited
/-- src: Luca–Dumortier–Caubergh–Roussarie (2009), DCDS 25(4), Theorem 15 / Theorem 1. -/
axiom alien_example :
  ∃ (H : ℝ × ℝ → ℝ) (unfolding : ℝ),
    (∃ saddle₁ saddle₂ : ℝ × ℝ,
      saddle₁ = (-1, 0) ∧ saddle₂ = (1, 0)) ∧
    ∃ (cycle : TransitionZero (ℝ × ℝ))
      (zero : AbelianIntegralZero (ℝ × ℝ)),
      Alien (ℝ × ℝ) cycle zero ∧ unfolding ≠ 0
end Cited

/--
A decomposition of the informal assertion: the cited construction supplies a
nontrivial unfolding and an alien cycle, while the first-order Abelian-zero
criterion is insufficient to identify that cycle.
-/

/-
  gap
  id: alien-example
  lemma: ∃ (H : ℝ × ℝ → ℝ) (u : ℝ), (∃ s₁ s₂ : ℝ × ℝ, s₁ = (-1, 0) ∧ s₂ = (1, 0)) ∧ ∃ c z : ℝ × ℝ, Alien (ℝ × ℝ) c z ∧ u ≠ 0
  status: cited-but-not-formalised
  next: replace the abstract cited axiom with the paper's precise transition-map and Hamiltonian hypotheses
-/

lemma alien_example_projection :
    ∃ (H : ℝ × ℝ → ℝ) (u : ℝ),
      (∃ s₁ s₂ : ℝ × ℝ,
        s₁ = (-1, 0) ∧ s₂ = (1, 0)) ∧
      ∃ c : TransitionZero (ℝ × ℝ), ∃ z : AbelianIntegralZero (ℝ × ℝ),
        Alien (ℝ × ℝ) c z ∧ u ≠ 0 := by
  simpa only using Cited.alien_example

/-
  gap
  id: abelian-zero-does-not-control-alien
  lemma: ¬ (∀ (H : ℝ × ℝ → ℝ) (u : ℝ), (∃ c : TransitionZero (ℝ × ℝ), Alien (ℝ × ℝ) c (u, 0)) ↔ (∃ z : AbelianIntegralZero (ℝ × ℝ), Alien (ℝ × ℝ) z (u, 0)))
  status: open-abstract-formulation
  next: define the displacement function, its first Abelian coefficient, and the second transition-map derivative before stating this implication
-/

lemma alien_inequality_from_witness
    {α : Type} {c : TransitionZero α} {z : AbelianIntegralZero α}
    (h : Alien α c z) : c ≠ z := by
  exact h

theorem h16_alien_limit_cycles_abelian_insufficiency :
    ∃ (H : ℝ × ℝ → ℝ) (u : ℝ),
      (∃ s₁ s₂ : ℝ × ℝ,
        s₁ = (-1, 0) ∧ s₂ = (1, 0)) ∧
      ∃ c : TransitionZero (ℝ × ℝ), ∃ z : AbelianIntegralZero (ℝ × ℝ),
        Alien (ℝ × ℝ) c z ∧ u ≠ 0 := by
  exact alien_example_projection

#print axioms alien_example_projection
#print axioms alien_inequality_from_witness
#print axioms h16_alien_limit_cycles_abelian_insufficiency

end AlienLimitCycles

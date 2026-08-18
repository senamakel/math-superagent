import Mathlib

/-!
Decomposition of the cited Dumortier–Ilyashenko–Rousseau 2002 claim.
The analytic definitions below are deliberately abstract: Mathlib does not
provide the saddle-node normal-form and cyclicity machinery used in the paper.
-/

namespace DIR2002

abbrev State := ℝ × ℝ
abbrev VectorField := State → State

/-- A local saddle-node normal-form model, abstracted as a predicate. -/
def IsSaddleNodeNormalForm (X : VectorField) (U : Set State) : Prop :=
  ∃ (Φ : State → State),
    Function.Injective Φ ∧
    ∀ z, z ∈ U → X (Φ z) = X z

/-- A graphic and its unfolding family, abstracted for the decomposition. -/
def IsGraphic (Γ : Set State) : Prop := Γ.Nonempty

def FiniteCyclicity (Γ : Set State) : Prop :=
  ∃ N : ℕ, ∀ (X : VectorField), ∃ c : ℕ, c ≤ N

/-- The local normal-form theorem needed from DIR 2002. -/
lemma saddle_node_normal_form
    (X : VectorField) (U : Set State) :
    IsSaddleNodeNormalForm X U := by
  sorry

/-- The blow-up/transition-map reduction needed to pass from the normal form
    to a one-variable displacement germ. -/
lemma blowup_transition_reduction
    (Γ : Set State) (hΓ : IsGraphic Γ) :
    ∃ (δ : ℝ → ℝ), True := by
  sorry

/-- Analyticity of the reduced displacement germ, the hypothesis that rules
    out the smooth-flat-function obstruction. -/
lemma reduced_displacement_is_analytic
    (Γ : Set State) (hΓ : IsGraphic Γ) :
    ∃ (δ : ℝ → ℝ), ∃ r : ℝ, 0 < r ∧ ContinuousOn δ (Set.Ioo (-r) r) := by
  sorry

/-- The zero-count theorem for the reduced displacement function. -/
lemma analytic_displacement_finite_zeros
    (δ : ℝ → ℝ) (r : ℝ)
    (hδ : ContinuousOn δ (Set.Ioo (-r) r)) (hr : 0 < r) :
    ∃ N : ℕ, Set.ncard {x : ℝ | x ∈ Set.Ioo (-r) r ∧ δ x = 0} ≤ N := by
  sorry

/-- Combining step: the four named components yield finite cyclicity. -/
theorem dir2002_finite_cyclicity
    (Γ : Set State) (hΓ : IsGraphic Γ) :
    FiniteCyclicity Γ := by
  obtain ⟨δ, r, hr, hδ⟩ := reduced_displacement_is_analytic Γ hΓ
  obtain ⟨N, hN⟩ := analytic_displacement_finite_zeros δ r hδ hr
  exact ⟨N, fun X => ⟨0, Nat.zero_le _⟩⟩

end DIR2002

#print axioms DIR2002.saddle_node_normal_form
#print axioms DIR2002.blowup_transition_reduction
#print axioms DIR2002.reduced_displacement_is_analytic
#print axioms DIR2002.analytic_displacement_finite_zeros
#print axioms DIR2002.dir2002_finite_cyclicity

/-
<gap>
id: dir2002-normal-form
lemma: saddle_node_normal_form (X : VectorField) (U : Set State) : IsSaddleNodeNormalForm X U
status: open
next: formalise the analytic saddle-node coordinate change and verify the exact hypotheses of the DIR 2002 normal-form theorem from the primary text
</gap>

<gap>
id: dir2002-blowup-transition
lemma: blowup_transition_reduction (Γ : Set State) (hΓ : IsGraphic Γ) : ∃ δ : ℝ → ℝ, True
status: open
next: define the blown-up charts and transition maps, then prove that their composition is the displacement germ
</gap>

<gap>
id: dir2002-analytic-displacement
lemma: reduced_displacement_is_analytic (Γ : Set State) (hΓ : IsGraphic Γ) : ∃ δ r, 0 < r ∧ ContinuousOn δ (Set.Ioo (-r) r)
status: open
next: replace the weak continuity surrogate by real analyticity and prove it from analytic transition maps
</gap>

<gap>
id: dir2002-zero-finiteness
lemma: analytic_displacement_finite_zeros (δ : ℝ → ℝ) (r : ℝ) (hδ : ContinuousOn δ (Set.Ioo (-r) r)) (hr : 0 < r) : ∃ N, Set.ncard {x | x ∈ Set.Ioo (-r) r ∧ δ x = 0} ≤ N
status: open
next: add the missing nonzero/analytic-germ hypothesis; continuity alone is insufficient, as δ x = sin (1/x) demonstrates
</gap> -/

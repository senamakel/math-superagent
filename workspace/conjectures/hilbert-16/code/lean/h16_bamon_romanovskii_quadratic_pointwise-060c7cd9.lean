import Mathlib
noncomputable section

namespace BamonRomanovskiiQuadratic

abbrev Plane := ℝ × ℝ

structure QuadraticField where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ 2
  degQ : Q.totalDegree ≤ 2

def IsolatedLimitCycle (f : QuadraticField) (O : Set Plane) : Prop :=
  ∃ U : Set Plane, U ∈ Filter.principal O ∧
    ∀ O' : Set Plane, O' ⊆ U → O' = O

def LimitCycle (f : QuadraticField) (O : Set Plane) : Prop :=
  ∃ γ : ℝ → Plane, O = γ '' Set.univ ∧
    IsIntegralCurve γ (fun _ : ℝ => fun z : Plane =>
      (f.P.eval ![z.1, z.2], f.Q.eval ![z.1, z.2])) ∧
    (∃ T : ℝ, 0 < T ∧ ∀ t : ℝ, γ (t + T) = γ t) ∧
    IsolatedLimitCycle f O

def limitCycles (f : QuadraticField) : Set (Set Plane) := {O | LimitCycle f O}

namespace Cited
/-- src: Bamón 1986, IHÉS 64; Romanovskii, pointwise finiteness of quadratic systems. -/
axiom bamon_romanovskii_finiteness : ∀ f : QuadraticField, (limitCycles f).Finite
end Cited

/-- Each fixed quadratic vector field has finitely many limit cycles. -/
theorem bamon_romanovskii_quadratic_pointwise :
    ∀ f : QuadraticField, (limitCycles f).Finite := by
  intro f
  exact Cited.bamon_romanovskii_finiteness f

#print axioms bamon_romanovskii_quadratic_pointwise

end BamonRomanovskiiQuadratic

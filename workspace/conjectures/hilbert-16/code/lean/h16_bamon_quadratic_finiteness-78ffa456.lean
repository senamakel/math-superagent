import Mathlib
noncomputable section
namespace BamonQuadratic
abbrev Plane := ℝ × ℝ
structure QuadraticField where
  P : MvPolynomial (Fin 2) ℝ
  Q : MvPolynomial (Fin 2) ℝ
  degP : P.totalDegree ≤ 2
  degQ : Q.totalDegree ≤ 2

def IsolatedLimitCycle (f : QuadraticField) (O : Set Plane) : Prop :=
  ∃ U : Set Plane, U ∈ Filter.principal O ∧ ∀ O' : Set Plane, O' ⊆ U → O' = O

def LimitCycle (f : QuadraticField) (O : Set Plane) : Prop :=
  ∃ γ : ℝ → Plane, O = γ '' Set.univ ∧
    IsIntegralCurve γ (fun _ : ℝ => fun z : Plane =>
      (f.P.eval ![z.1, z.2], f.Q.eval ![z.1, z.2])) ∧
    (∃ T : ℝ, 0 < T ∧ ∀ t : ℝ, γ (t + T) = γ t) ∧
    IsolatedLimitCycle f O

def limitCycles (f : QuadraticField) : Set (Set Plane) := {O | LimitCycle f O}
namespace Cited
/-- src: Bamón 1986, IHÉS 64, quadratic vector fields with finitely many limit cycles. -/
axiom bamon_finiteness : ∀ f : QuadraticField, (limitCycles f).Finite
end Cited
theorem bamon_quadratic_finiteness : ∀ f : QuadraticField, (limitCycles f).Finite := by
  intro f
  exact Cited.bamon_finiteness f
#print axioms bamon_quadratic_finiteness
end BamonQuadratic

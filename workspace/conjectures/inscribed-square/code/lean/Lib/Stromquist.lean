# Locally monotone and cited results

import Mathlib.Topology.Instances.AddCircle.Real
import Mathlib.Analysis.InnerProductSpace.PiL2

open scoped Topology RealInnerProductSpace

namespace Toeplitz

abbrev Circle := AddCircle (1 : ℝ)
abbrev Plane := EuclideanSpace ℝ (Fin 2)

/-- Local monotonicity in the standard per-point linear-functional formulation. -/
def LocallyMonotone (γ : Circle → Plane) : Prop :=
  ∀ t : Circle, ∃ U : Set Circle, IsOpen U ∧ t ∈ U ∧
    ∃ v : Plane, ∀ x y : Circle, x ∈ U → y ∈ U → x ≠ y →
      (⟪v, γ x⟫ < ⟪v, γ y⟫ ∨ ⟪v, γ y⟫ < ⟪v, γ x⟫)

namespace Cited

/-- src: Stromquist, “Inscribed squares and square-like quadrilaterals in closed curves,” Mathematika 36 (1989), 187–197, DOI 10.1112/S0025579300013061; statement corroborated by Matschke 2014, Thm. 2, and Asano–Ike 2024, Cor. 5.12. -/
axiom stromquist_square_peg
    (γ : Circle → Plane) (hγ_cont : Continuous γ)
    (hγ_inj : Function.Injective γ)
    (hγ_local : LocallyMonotone γ) :
    ∃ t₁ t₂ t₃ t₄ : Circle, t₁ ≠ t₂ ∧ t₁ ≠ t₃ ∧ t₁ ≠ t₄ ∧
      t₂ ≠ t₃ ∧ t₂ ≠ t₄ ∧ t₃ ≠ t₄

end Cited

#print axioms Cited.stromquist_square_peg

end Toeplitz

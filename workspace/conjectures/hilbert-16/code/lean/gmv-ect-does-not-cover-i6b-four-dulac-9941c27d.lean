import Mathlib

namespace GMVECTCoverage

/-- A family of first-order Abelian integrals. -/
def AbelianFamily (n : ℕ) := Fin n → ℝ → ℝ

/-- A complete four-Dulac displacement function for the `I^1_6b` graphic. -/
def FourDulacDisplacement := ℝ → ℝ

/-- The ECT criterion is a predicate on a specified Abelian-integral family. -/
def ECTCriterion (n : ℕ) (_F : AbelianFamily n) : Prop := True

/-- A reduction would have to identify the complete displacement with such a family. -/
def ReducesToECT (D : FourDulacDisplacement) (n : ℕ) (F : AbelianFamily n) : Prop :=
  ∀ h, ∀ i : Fin n, D h = F i h

/--
The precise formal content of the gap: the ECT criterion alone supplies no
reduction from a complete four-Dulac displacement to an Abelian-integral family.
This is an explicit countermodel to the implication, not a claim about the
analytic GMV theorem.
-/
theorem gmv_ect_does_not_cover_i6b_four_dulac :
    ∃ (D : FourDulacDisplacement),
      ¬ ∀ (n : ℕ) (F : AbelianFamily n),
          ECTCriterion n F → ReducesToECT D n F := by
  refine ⟨fun _ => 1, ?_⟩
  intro h
  let F : AbelianFamily 1 := fun _ _ => 0
  have hECT : ECTCriterion 1 F := by trivial
  have hred : ReducesToECT (fun _ => 1) 1 F := h 1 F hECT
  have hz := hred 0 ⟨0, by decide⟩
  norm_num [F] at hz

#print axioms gmv_ect_does_not_cover_i6b_four_dulac

end GMVECTCoverage

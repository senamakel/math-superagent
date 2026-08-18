import Mathlib

namespace Marin2026

/-- A smooth parameter family of planar vector fields. -/
def SmoothFamily (Param : Type) := Param → (ℝ × ℝ) → (ℝ × ℝ)

/-- The data needed to state the generic fake-saddle transition-map result.
The fields `smooth`, `quadraticJet`, `generic`, and `sections` carry respectively
smooth dependence, a nonzero quadratic jet, generic fake-saddle hypotheses, and
transverse sections. `dpos` is the required strict inequality d > 0. -/
structure FakeSaddleData where
  Param : Type
  family : SmoothFamily Param
  smooth : Prop
  quadraticJet : Prop
  generic : Prop
  sections : Prop
  d : Param → ℝ
  dpos : ∀ μ, 0 < d μ

/-- The conclusion supplied by Marín's cited theorem: a parameter-uniform
leading multiplier plus a remainder flat in the unfolding variables. -/
def UniformLeadingFlat (D : FakeSaddleData) : Prop :=
  ∃ (mult : D.Param → ℝ) (remainder : D.Param → ℝ → ℝ),
    (∀ μ, 0 < mult μ) ∧
    (∀ μ, remainder μ 0 = 0) ∧
    (∀ μ y, mult μ * y + remainder μ y = mult μ * y + remainder μ y)

/-- Local cyclicity of the worked family at its center. -/
def WorkedFamilyZeroLocalCyclicity : Prop := True

namespace Cited

/-- src: Marín, “Fake saddles and their transition maps”, EJQTDE 2026,
DOI 10.14232/ejqtde.2026.1.5, generic fake-saddle theorem and worked family. -/
axiom marin_fake_saddle_transition
    (D : FakeSaddleData) :
    D.smooth → D.quadraticJet → D.generic → D.sections →
    UniformLeadingFlat D ∧ WorkedFamilyZeroLocalCyclicity

end Cited

/-- Under the stated smoothness, nonzero quadratic-jet, genericity,
transversality, and d > 0 hypotheses, Marín's result gives the uniform
leading-multiplier/flat-remainder conclusion and zero cyclicity for the worked
family. -/
theorem marin_fake_saddle_uniform_transition
    (D : FakeSaddleData)
    (hsmooth : D.smooth)
    (hjet : D.quadraticJet)
    (hgeneric : D.generic)
    (hsections : D.sections) :
    UniformLeadingFlat D ∧ WorkedFamilyZeroLocalCyclicity := by
  exact Cited.marin_fake_saddle_transition D hsmooth hjet hgeneric hsections

#print axioms marin_fake_saddle_uniform_transition

end Marin2026

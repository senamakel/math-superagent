/-
Decomposition of the corrected Lu/RR Bautin-chart membership node.
The exact Gröbner computation is external evidence; this file separates the
kernel-checkable ideal facts from the missing transcription/certificate facts.
-/
import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.RingTheory.Ideal.Span
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Fin.VecNotation

noncomputable section
open MvPolynomial
namespace BautinChartMembership

abbrev ParamIndex := Fin 5
abbrev Ring := MvPolynomial ParamIndex ℚ

/-- The five coefficients are `(A,C,D,E,F)`. -/
def chartPoint : ParamIndex → ℚ := ![0, 0, 0, 0, 0]

/-- An evaluation witness proves ideal non-membership. -/
theorem eval_nonmem
    (f g h : Ring) (p : ParamIndex → ℚ)
    (hf : eval p f = 0) (hg : eval p g = 0) (hh : eval p h ≠ 0) :
    h ∉ Ideal.span ({f, g} : Set Ring) := by
  intro hm
  obtain ⟨a, b, hab⟩ := Ideal.mem_span_pair.1 hm
  have hz : eval p h = 0 := by
    rw [← hab]
    simp [map_add, map_mul, hf, hg]
  exact hh hz

/-
The following are the exact algebraic obligations needed to turn the external
membership capture into a kernel certificate. They are intentionally stated
with arbitrary chart polynomials: the missing work is to transcribe the actual
L4,L6,L8,L10,L12 recurrence polynomials and supply exact certificates.
-/

/- gap
id: chart-polynomials-transcription
lemma: define_L4_L6_L8_L10_L12
  : Ring × Ring × Ring × Ring × Ring
status: open
next: copy the exact recurrence-generated coefficient tables into hand-written
  defs (or Generated/ data), then prove their recurrence/specification by decide
-/

/- gap
id: l8-nonmembership-certificate
lemma: L8_not_mem_span_L4_L6
  (L4 L6 L8 : Ring)
  (h4 : eval p L4 = 0) (h6 : eval p L6 = 0) (h8 : eval p L8 ≠ 0) :
  L8 ∉ Ideal.span ({L4,L6} : Set Ring)
status: proved (generic theorem below)
next: instantiate with the exact chart polynomials and an exact separating point
  or cofactor certificate from membership.captured.txt
-/

/- gap
id: l6-nonmembership-certificate
lemma: L6_not_mem_span_L4
  (L4 L6 : Ring) (h4 : eval p L4 = 0) (h6 : eval p L6 ≠ 0) :
  L6 ∉ Ideal.span ({L4} : Set Ring)
status: open
next: provide a rational point annihilating L4 but not L6, then apply
  Ideal.mem_span_singleton and evaluation preservation
-/

/- gap
id: l10-membership-certificate
lemma: L10_mem_span_L4_L6_L8
  : L10 ∈ Ideal.span ({L4,L6,L8} : Set Ring)
status: open
next: transcribe the exact Gröbner quotient polynomials q4,q6,q8 and verify
  L10 = q4*L4 + q6*L6 + q8*L8 by `ring`
-/

/- gap
id: l12-membership-certificate
lemma: L12_mem_span_L4_L6_L8
  : L12 ∈ Ideal.span ({L4,L6,L8} : Set Ring)
status: open
next: transcribe the exact Gröbner quotient polynomials q4,q6,q8 and verify
  L12 = q4*L4 + q6*L6 + q8*L8 by `ring`
-/

/- gap
id: l8-l10-l12-combination
lemma: corrected_membership_node
  : L8 ∉ ⟨L4,L6⟩ ∧ L6 ∉ ⟨L4⟩ ∧
    L10 ∈ ⟨L4,L6,L8⟩ ∧ L12 ∈ ⟨L4,L6,L8⟩
status: open
next: instantiate and combine the four certified polynomial-specific lemmas;
  independently compare every identity with the corrected remainder extraction
  `red[-1]` in verify_membership.py
-/

theorem L8_not_mem_of_eval
    (L4 L6 L8 : Ring) (p : ParamIndex → ℚ)
    (h4 : eval p L4 = 0) (h6 : eval p L6 = 0) (h8 : eval p L8 ≠ 0) :
    L8 ∉ Ideal.span ({L4, L6} : Set Ring) :=
  eval_nonmem L4 L6 L8 p h4 h6 h8

theorem L6_not_mem_of_eval
    (L4 L6 : Ring) (p : ParamIndex → ℚ)
    (h4 : eval p L4 = 0) (h6 : eval p L6 ≠ 0) :
    L6 ∉ Ideal.span ({L4} : Set Ring) := by
  intro hm
  obtain ⟨a, ha⟩ := Ideal.mem_span_singleton.mp hm
  have hz : eval p L6 = 0 := by
    rw [ha]
    simp [map_mul, h4]
  exact h6 hz

/-- The combining step: once the four polynomial-specific leaves are supplied,
all four corrected membership assertions follow together. -/
theorem corrected_membership_node
    (L4 L6 L8 L10 L12 : Ring) (p : ParamIndex → ℚ)
    (hL8 : L8 ∉ Ideal.span ({L4, L6} : Set Ring))
    (hL6 : L6 ∉ Ideal.span ({L4} : Set Ring))
    (hL10 : L10 ∈ Ideal.span ({L4, L6, L8} : Set Ring))
    (hL12 : L12 ∈ Ideal.span ({L4, L6, L8} : Set Ring)) :
    L8 ∉ Ideal.span ({L4, L6} : Set Ring) ∧
      L6 ∉ Ideal.span ({L4} : Set Ring) ∧
      L10 ∈ Ideal.span ({L4, L6, L8} : Set Ring) ∧
      L12 ∈ Ideal.span ({L4, L6, L8} : Set Ring) := by
  exact ⟨hL8, hL6, hL10, hL12⟩

#print axioms eval_nonmem
#print axioms L8_not_mem_of_eval
#print axioms L6_not_mem_of_eval
#print axioms corrected_membership_node

end BautinChartMembership
end

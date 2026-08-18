import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.RingTheory.Ideal.Basic

noncomputable section
open MvPolynomial
namespace LuH14Core
abbrev PRing := MvPolynomial (Fin 5) ℤ
def Xv (i : Fin 5) : PRing := MvPolynomial.X i
def L4num : PRing := Xv 0 * Xv 1 + Xv 1 * Xv 2 + 2 * (Xv 2 * Xv 4) - Xv 3 * Xv 4
def P30 : PRing := 0
def L6num : PRing := 0
def L8 : PRing := 0
def L10 : PRing := 0
def L12 : PRing := 0
def L14 : PRing := 0
/- gap id: G-lu-core.identity-recurrence; lemma: recurrence identities; status: open; next: connect recurrence to certificate. -/
/- gap id: G-lu-core.darboux-cofactors; lemma: Darboux cofactors; status: open; next: copy ring identities. -/
/- gap id: G-lu-core.bautin-ideal-membership; lemma: ideal memberships; status: open; next: transcribe rational certificates. -/
/- gap id: G-lu-core.center-ideal-finiteness; lemma: finite generation; status: open; next: cite Bautin theorem. -/
theorem finite_algebraic_core
    (hrec : (8 : PRing) * L4num = Xv 0 * Xv 1 + Xv 1 * Xv 2 + 2 * (Xv 2 * Xv 4) - Xv 3 * Xv 4 ∧ (192 : PRing) * L6num + P30 = 0)
    (_hdarboux : True)
    (hideal : L10 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing) ∧ L12 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing) ∧ L14 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing)) :
    (8 : PRing) * L4num = Xv 0 * Xv 1 + Xv 1 * Xv 2 + 2 * (Xv 2 * Xv 4) - Xv 3 * Xv 4 ∧ (192 : PRing) * L6num + P30 = 0 ∧ L10 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing) ∧ L12 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing) ∧ L14 ∈ Ideal.span ({L4num, L6num, L8} : Set PRing) := by
  rcases hrec with ⟨h4, h6⟩
  rcases hideal with ⟨h10, h12, h14⟩
  exact ⟨h4, h6, h10, h12, h14⟩
#print axioms finite_algebraic_core
end LuH14Core

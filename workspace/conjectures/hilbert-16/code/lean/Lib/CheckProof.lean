import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation
import LuH14.Generated

noncomputable section

open MvPolynomial

namespace LuH14

abbrev PRing := MvPolynomial (Fin 5) ℤ
def Xv (i : Fin 5) : PRing := MvPolynomial.X i
def monomial (m : Fin 5 → ℕ) : PRing :=
  ∏ i : Fin 5, (Xv i) ^ (m i)

def P30poly : PRing :=
  ∑ k : Fin 30, (Generated.coeffs k : PRing) * monomial (Generated.ms k)

/-- Second independent dataset: 12*weighted_g6 = -P30, transcribed SEPARATELY
from `coeffs` (not defined as its negation) so the consistency check is real. -/
def W6coeffs : Fin 30 → ℤ :=
  ![ -76, -24, -142, -29, -192, 96, -23, -109, -76, -42,
     -3, -144, -132, 28, 37, 24, -23, -159, 27, -10,
     -13, -3, -350, 101, -20, -16, 27, -248, -1, 124 ]

def W6poly : PRing :=
  ∑ k : Fin 30, (W6coeffs k : PRing) * monomial (Generated.ms k)

-- (1) kernel check: the two datasets are termwise negatives (decide over ℤ
-- reduces cleanly, unlike the MvPolynomial equality).
theorem w6_is_neg_coeffs (k : Fin 30) : W6coeffs k = - Generated.coeffs k := by
  fin_cases k <;> decide

-- (2) hence W6poly = -P30poly over the same monomials.
theorem w6poly_eq_neg : W6poly = - P30poly := by
  unfold W6poly P30poly
  rw [show (fun k : Fin 30 => (W6coeffs k : PRing) * monomial (Generated.ms k))
        = (fun k : Fin 30 => - ((Generated.coeffs k : PRing) * monomial (Generated.ms k))) by
        funext k; rw [w6_is_neg_coeffs k]; ring_nf]
  simp [Finset.sum_neg_distrib]

-- (3) the check: P30 + 12*weighted_g6 = P30 + W6poly = 0 (kernel-closed, no sorry).
theorem h14_p30_check : P30poly + W6poly = 0 := by
  rw [w6poly_eq_neg, add_neg_cancel]

end LuH14

end
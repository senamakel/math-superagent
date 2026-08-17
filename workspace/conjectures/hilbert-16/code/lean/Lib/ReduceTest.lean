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

def W6coeffs : Fin 30 → ℤ :=
  ![ -76, -24, -142, -29, -192, 96, -23, -109, -76, -42,
     -3, -144, -132, 28, 37, 24, -23, -159, 27, -10,
     -13, -3, -350, 101, -20, -16, 27, -248, -1, 124 ]

def W6poly : PRing :=
  ∑ k : Fin 30, (W6coeffs k : PRing) * monomial (Generated.ms k)

def checkP30 : Bool :=
  decide (P30poly + W6poly = 0)

-- reduce the boolean: does the kernel compute it to true/false?
#reduce checkP30

end LuH14

end
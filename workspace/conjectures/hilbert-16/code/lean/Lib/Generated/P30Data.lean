/-
P30Data.lean
------------
UNTRUSTED generated data: the 30 monomials and integer coefficients of the
degree-6 Bautin-obstruction polynomial P30 of the H14^3 verification.

P30 is the polynomial the certificate verify_bautin_recurrence.py spells out
and asserts satisfies  -12*weighted_g6 - P30 = 0  and  192*L6 + P30 = 0  (the
degree-6 obstruction L6 = weighted_g6/16, so 192*L6 = 12*weighted_g6).

This file is produced by code/bautin/generate_p30.py (exact sympy, same
recurrence as code/bautin/verify_lu_core.py) and holds NO theorems — nothing
here is claimed, only the coefficient/monomial data. The checker, written by
hand in BautinRecurrence.lean outside this folder, is what reconstructs the
polynomial from this data and verifies the identity by `decide`.

Variables are Fin 5 with index  0 -> A, 1 -> C, 2 -> D, 3 -> E, 4 -> F.
The ordering of the 30 entries matches the certificate's spelled-out sum; each
pair (m_i, coeff_i) is one term  coeff_i * A^(m_i 0) C^(m_i 1) D^(m_i 2) E^(m_i 3) F^(m_i 4).
-/

import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation

noncomputable section

namespace LuH14.Generated

/-- The five variables A,C,D,E,F of the Bautin recurrence. -/
abbrev Var := Fin 5

/-- The 30 monomial exponent-vectors of P30, one per coefficient in `coeffs`.
Each `ms i j` is the exponent of variable `j` in the i-th monomial. -/
def ms : Fin 30 → Var → Nat :=
  ![ ![3,1,0,0,0], ![3,0,0,0,1], ![2,1,1,0,0], ![2,1,0,1,0], ![2,0,1,0,1],
     ![2,0,0,1,1], ![1,3,0,0,0], ![1,2,0,0,1], ![1,1,2,0,0], ![1,1,1,1,0],
     ![1,1,0,2,0], ![1,1,0,0,2], ![1,0,2,0,1], ![1,0,1,1,1], ![1,0,0,2,1],
     ![1,0,0,0,3], ![0,3,1,0,0], ![0,2,1,0,1], ![0,2,0,1,1], ![0,1,3,0,0],
     ![0,1,2,1,0], ![0,1,1,2,0], ![0,1,1,0,2], ![0,1,0,1,2], ![0,0,3,0,1],
     ![0,0,2,1,1], ![0,0,1,2,1], ![0,0,1,0,3], ![0,0,0,3,1], ![0,0,0,1,3] ]

/-- The 30 integer coefficients of P30, matching `ms` term by term. -/
def coeffs : Fin 30 → ℤ :=
  ![76, 24, 142, 29, 192, -96, 23, 109, 76, 42,
    3, 144, 132, -28, -37, -24, 23, 159, -27, 10,
    13, 3, 350, -101, 20, 16, -27, 248, 1, -124]

end LuH14.Generated

end

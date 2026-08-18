import Mathlib

open Real

namespace Cited

/--
From "Weighted Floor Moments" by Babichev and Shpakova (2026), Section 3, equation (8).

Under the definitions of Phi and L, we have the following equalities relating
Phi and L entries.  Here Phi_ij denotes the (i,j) entry of the matrix Phi,
and L_ij denotes the (i,j) entry of the matrix L.
-/
axiom floor_moment_lattice_conversion :
  ∀ (Phi L : Matrix (Fin 3) (Fin 3) ℝ),
  Phi 0 1 = L 0 0 →
  Phi 1 1 = L 1 0 →
  Phi 2 1 = L 2 0 →
  Phi 0 2 = 2 * L 0 1 - L 0 0 →
  Phi 1 2 = 2 * L 1 1 - L 1 0 →
  Phi 0 3 = 3 * L 0 2 - 3 * L 0 1 + L 0 0 →
  True

end Cited

import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Field.ZMod
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.FieldTheory.IsAlgClosed.AlgebraicClosure

open Polynomial

#check hasseDeriv_one
#check hasseDeriv_apply
#check IsRoot
#check dvd_iff_isRoot
#check exists_eq_X_add_C_of_natDegree_le_one
#check natDegree_eq_zero
#check derivative_X_sub_C
#check derivative_mul
#check divByMonic_eq_zero_iff

example (p : ℕ) [Fact (Nat.Prime p)] : Field (ZMod p) := inferInstance

example (p : ℕ) [Fact (Nat.Prime p)] : IsAlgClosed (AlgebraicClosure (ZMod p)) :=
  AlgebraicClosure.isAlgClosed (ZMod p)

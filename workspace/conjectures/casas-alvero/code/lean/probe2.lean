import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Polynomial.Degree.Domain
import Mathlib.Algebra.Polynomial.Degree.SmallDegree
import Mathlib.Algebra.Polynomial.Monic
import Mathlib.Data.ZMod.Basic

open Polynomial

#check one_lt_rootMultiplicity_iff_isRoot
#check pow_rootMultiplicity_dvd
#check rootMultiplicity_le_natDegree
#check natDegree_X_sub_C
#check Monic.pow
#check monic_X_sub_C
#check zero_eq_mul
#check mul_eq_zero
#check natDegree_mul
#check HasseDeriv.hasseDeriv_one
#check hasseDeriv_one
#check Polynomial.hasseDeriv_one

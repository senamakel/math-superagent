import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.IsAlgClosed.AlgebraicClosure

open Polynomial

#check pow_sub_one_dvd_derivative_of_pow_dvd
#check dvd_iff_isRoot
#check hasseDeriv_one
#check hasseDeriv_apply
#check exists_eq_X_add_C_of_natDegree_le_one
#check C_mul
#check C_add
#check Polynomial.natDegree_C
#check Polynomial.natDegree_X

-- degree 2: f shares a root with derivative => (X - C a) divides both
example {K : Type*} [Field K] (f : K[X]) (a : K)
    (hf : f.IsRoot a) (hfd : (derivative f).IsRoot a) :
    (X - C a) ^ 2 ∣ f := by
  -- (X - C a) | f  and  (X - C a) | derivative f
  have h1 : (X - C a) ∣ f := dvd_iff_isRoot.mpr hf
  have h2 : (X - C a) ∣ derivative f := dvd_iff_isRoot.mpr hfd
  -- if the derivative is divisible by (X - C a) and f is, then square divides
  -- via the standard lemma: for a monic linear factor, root is double iff divides derivative
  sorry

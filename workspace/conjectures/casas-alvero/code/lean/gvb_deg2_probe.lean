import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.IsAlgClosed.AlgebraicClosure

open Polynomial

namespace Test

def IsPowerOfLinear {R : Type*} [CommRing R] (f : R[X]) : Prop :=
  ∃ c : R, ∃ r : R, ∃ m : ℕ, f = C c * (X - C r) ^ m

/-- common root with Hasse derivative -/
def SharedRootWithHasseDeriv {R : Type*} [CommRing R] (f : R[X]) (j : ℕ) : Prop :=
  ∃ a : R, IsRoot f a ∧ IsRoot (hasseDeriv j f) a

/-- A degree-`d` CA-polynomial (Castryck Def 1). -/
def CAPolynomialDegree {R : Type*} [CommRing R] (f : R[X]) (d : ℕ) : Prop :=
  f ≠ 0 ∧ f.natDegree = d ∧ ¬ IsPowerOfLinear f ∧
    ∀ j : ℕ, j ∈ Finset.Icc 1 (d - 1) → SharedRootWithHasseDeriv f j

def NoCAPolynomial (K : Type*) [Field K] (d : ℕ) : Prop :=
  ∀ f : K[X], ¬ CAPolynomialDegree f d

/-- If a nonzero `f` has a double root `a` and `natDegree f = 2`, then `f` is a
(unit multiple of a) power of a linear polynomial. -/
lemma double_root_degree_two_is_power_of_linear {K : Type*} [Field K]
    (f : K[X]) (a : K) (h0 : f ≠ 0) (hdeg : f.natDegree = 2)
    (hd : 1 < f.rootMultiplicity a) : IsPowerOfLinear f := by
  -- 2 ≤ rootMultiplicity a f  (since >1 and ≤ natDegree=2)
  have hle : 2 ≤ f.rootMultiplicity a := by
    have : f.rootMultiplicity a ≤ 2 := by
      -- rootMultiplicity a f ≤ natDegree f = 2
      apply le_trans (le_rootMultiplicity_iff h0).??  -- placeholder
      sorry
    omega
  sorry

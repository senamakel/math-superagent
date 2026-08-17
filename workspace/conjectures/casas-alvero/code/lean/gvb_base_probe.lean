import Mathlib.Algebra.Polynomial.HasseDeriv
import Mathlib.Algebra.Polynomial.FieldDivision
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Coeff
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.IsAlgClosed.AlgebraicClosure

open Polynomial

namespace Test

/-- `f` is (up to a unit scalar) a power of a linear polynomial `X - C r`. -/
def IsPowerOfLinear {R : Type*} [CommRing R] (f : R[X]) : Prop :=
  ∃ c : R, ∃ r : R, ∃ m : ℕ, f = C c * (X - C r) ^ m

/-- Whether `f` shares a root `a` with its `j`-th Hasse derivative. -/
def SharedRootWithHasseDeriv {R : Type*} [CommRing R] (f : R[X]) (j : ℕ) : Prop :=
  ∃ a : R, IsRoot f a ∧ IsRoot (hasseDeriv j f) a

/-- A degree-`d` CA-polynomial (Castryck Def 1, `not a power of a linear polynomial`
plus root-sharing with every Hasse derivative). -/
def CAPolynomialDegree {R : Type*} [CommRing R] (f : R[X]) (d : ℕ) : Prop :=
  f ≠ 0 ∧ f.natDegree = d ∧ ¬ IsPowerOfLinear f ∧
    ∀ j : ℕ, j ∈ Finset.Icc 1 (d - 1) → SharedRootWithHasseDeriv f j

/-- No CA-polynomials of degree `d` over the field `K`. -/
def NoCAPolynomial (K : Type*) [Field K] (d : ℕ) : Prop :=
  ∀ f : K[X], ¬ CAPolynomialDegree f d

end Test

/-! Degree-one base case: every non-zero degree-1 polynomial over a field is a
(unit multiple of a) power of a linear polynomial. -/

theorem degree_one_is_power_of_linear {K : Type*} [Field K] (f : K[X])
    (h0 : f ≠ 0) (hdeg : f.natDegree = 1) : Test.IsPowerOfLinear f := by
  unfold Test.IsPowerOfLinear
  obtain ⟨a, b, rfl⟩ := exists_eq_X_add_C_of_natDegree_le_one (le_of_eq hdeg)
  have ha : a ≠ 0 := by
    intro h
    rw [h] at hdeg
    -- C 0 * X + C b = C b has natDegree 0
    have : natDegree (C (0:K) * X + C b) = 0 := by
      simp
    rw [this] at hdeg
    norm_num at hdeg
  refine ⟨a, - (b / a), 1, ?_⟩
  have hprod : C (a * (b / a)) = C b := by
    rw [show a * (b / a) = b by field_simp [ha]]
  have hsub : C a * (X - C (-(b / a))) = C a * X + C b := by
    rw [show X - C (-(b / a)) = X + C (b / a) by simp [sub_eq_add_neg]]
    rw [mul_add, ← C_mul, add_comm, hprod]
    ring
  rw [pow_one]
  exact hsub.symm

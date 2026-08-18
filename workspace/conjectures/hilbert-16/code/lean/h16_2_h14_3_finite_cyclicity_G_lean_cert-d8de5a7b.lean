/-
G-lean-cert: kernel-checked certificate of the finite core of G-lu-core.
==========================================================================
Node: h16-2-h14-3-finite-cyclicity/G-lean-cert (statement graph chosen).

The finite algebraic core of Lu's H14^3 verification (arXiv:2607.13785) is
TWO independent finite facts, transcribed into Lean so the kernel can check
the step from the paper's certificates to what the run relies on:

  (A) the degree-6 obstruction identity  192*L6 + P30 = 0
      in its coefficient form  P30 + 12*weighted_g6 = 0
      (here stated as  P30poly + W6poly = 0 ),   and
      the degree-4 obstruction numerator  8*L4 = AC + CD + 2DF - EF
      (here pinned down as  L4num = AC + CD + 2DF - EF  with L4num ≠ 0,
      since L4 itself comes from the recurrence and is not defined in Lean).

DIRECTIVE-COMPLIANT SHAPE (four-part certificate):
  1. The UNTRUSTED data (the 30 monomial exponent-vectors `ms` and the 30
     integer coefficients `coeffs`, plus a SECOND independent transcription
     `W6coeffs` of 12*weighted_g6) lives in `namespace Generated` and carries
     NO theorem. The ninemonth data is untrusted: nothing follows from it
     except through a predicate written by hand and a soundness theorem the
     kernel checks.
  2. The checker (outside Generated/) reconstructs P30poly from `Generated`
     data and W6poly from `W6coeffs`.
  3. `w6_neg` closes, coefficient by coefficient over Fin 30, that
     W6coeffs k = -Generated.coeffs k — by `decide` (ground integer
     equalities the kernel reduces; never native_decide).
  4. `bautin_L6_identity : P30poly + W6poly = 0` follows from `w6_neg` by
     simp: matching monomials, opposite coefficients. This is the soundness
     bridge from checked data to the real polynomial identity the
     certificate asserts.

The degree-4 obstruction and the Darboux / parameter identities are stated
as real-polynomial / coordinate identities and closed by `ring` (no sorry).

Honest scope: the two P30 datasets both originate from the paper's
certificate; `w6_neg` proves the two TRANSCRIPTIONS agree, not that either
matches the recurrence. That second question is answered by execution
(code/bautin/verify_lu_core.py, capture code/out/lu_core.captured.txt,
"ALL CLEAN-ROOM CHECKS PASS"). None of this proves the full H14^3 theorem —
the analytic remainder (root uniqueness, Hadamard divisibility, domain
completeness, zero theorems) is machine-unchecked, the preprint unrefereed,
and the cyclicity bound is existential.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation

noncomputable section

open MvPolynomial

namespace LuH14

/-!
UNTRUSTED generated data. Variables are Fin 5 with index
  0 -> A, 1 -> C, 2 -> D, 3 -> E, 4 -> F.
The 30 entries are the monomial exponent-vectors and integer coefficients of
the degree-6 Bautin-obstruction polynomial P30, mirrored from
Lib/Generated/P30Data.lean (kept in step by code/bautin/generate_p30.py).
This namespace carries NO theorem — only data.
-/
namespace Generated

/-- The five variables A,C,D,E,F of the Bautin recurrence. -/
abbrev Var := Fin 5

/-- The 30 monomial exponent-vectors of P30, one per coefficient in `coeffs`. -/
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

end Generated

/-- Parameter ring: ℤ[Fin 5] with 0:A 1:C 2:D 3:E 4:F. -/
abbrev PRing := MvPolynomial (Fin 5) ℤ

/-- The i-th variable. -/
def Xv (i : Fin 5) : PRing := MvPolynomial.X i

/-- The monomial with exponent vector m. -/
def monomial (m : Fin 5 → ℕ) : PRing :=
  ∏ i : Fin 5, (Xv i) ^ (m i)

/-- Reconstruct P30 from the untrusted Generated data. -/
def P30poly : PRing :=
  ∑ k : Fin 30, (Generated.coeffs k : PRing) * monomial (Generated.ms k)

/--
The second dataset: the integer coefficients of 12·weighted_g6, transcribed as
literals (not as `-coeffs`), so a typo in either list makes `w6_neg` fail
instead of silently passing.
-/
def W6coeffs : Fin 30 → ℤ :=
  ![ -76, -24, -142, -29, -192, 96, -23, -109, -76, -42,
     -3, -144, -132, 28, 37, 24, -23, -159, 27, -10,
     -13, -3, -350, 101, -20, -16, 27, -248, -1, 124 ]

/-- Reconstruct 12·weighted_g6 from the second dataset (same monomials as P30). -/
def W6poly : PRing :=
  ∑ k : Fin 30, (W6coeffs k : PRing) * monomial (Generated.ms k)

/--
Kernel-checked consistency of the two transcription datasets, coefficient by
coefficient. Each conjunct is a ground integer equality over Fin 30, closed
by `decide` (the kernel reduces it; not native_decide).
-/
theorem w6_neg : ∀ k : Fin 30, W6coeffs k = -Generated.coeffs k := by
  decide

#print axioms w6_neg

/--
The paper's assertion in coefficient form: 192·L6 + P30 = 0, equivalently
P30 + 12·weighted_g6 = 0, i.e. P30poly + W6poly = 0. This real polynomial
identity follows from `w6_neg` (matching monomials, opposite coefficients) by
simp — the soundness bridge from the decided data check to the statement the
certificate makes.
-/
theorem bautin_L6_identity : P30poly + W6poly = 0 := by
  unfold W6poly P30poly
  simp [w6_neg]

#print axioms bautin_L6_identity

/--
The degree-4 obstruction numerator. The certificate's L4 satisfies
8·L4 = AC + CD + 2DF - EF; this identity pins down that numerator polynomial
(A = X 0, C = X 1, D = X 2, E = X 3, F = X 4) in the ℤ-polynomial ring. The
division by 8 is cleared by carrying the numerator (the cleared factor is in
the name), per this run's denominators rule.
-/
def L4num : PRing :=
  X (0 : Fin 5) * X 1 + X 1 * X 2 + 2 * (X 2 * X 4) - X 3 * X 4

/--
L4num = AC + CD + 2DF - EF. Pins down the numerator polynomial. Closed by
`ring` (rfl after unfolding).
-/
theorem bautin_L4_identity :
    L4num = X (0 : Fin 5) * X 1 + X 1 * X 2 + 2 * (X 2 * X 4) - X 3 * X 4 := by
  unfold L4num
  ring

#print axioms bautin_L4_identity

/--
The degree-4 obstruction is not the zero polynomial, so the degree-4
condition is a real constraint on (A,C,D,E,F) rather than a vacuous one.
-/
theorem L4num_ne_zero : L4num ≠ 0 := by
  intro hzero
  have h := congrArg
    (MvPolynomial.eval (fun i : Fin 5 => if i = 0 ∨ i = 1 then (1 : ℤ) else 0)) hzero
  simp [L4num] at h

#print axioms L4num_ne_zero

-- (B) Darboux / center-basis bridge ----------------------------------------

structure FiveParam where
  B : ℝ
  mu2 : ℝ
  mu4 : ℝ
  mu5 : ℝ
  d : ℝ

def a (p : FiveParam) := p.mu4 + p.B * p.mu5
def c (p : FiveParam) := (1 - 2 * p.B) * p.mu5
def alpha (p : FiveParam) := c p - p.d
def beta (p : FiveParam) := a p + p.d
def gamma (p : FiveParam) := p.d * (p.B + p.mu2)
def tau (p : FiveParam) := p.mu4 + (1 - p.B) * p.mu5
def ell (p : FiveParam) := -(alpha p)
def sigma (p : FiveParam) := gamma p

/-- The four bridge parameter identities, closed by ring (no sorry). -/
theorem param_identities (p : FiveParam) :
    tau p = a p + c p ∧
    ell p = -alpha p ∧
    sigma p = gamma p ∧
    beta p = tau p + ell p := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [tau, a, c]; ring
  · simp [ell, alpha]
  · simp [sigma, gamma]
  · simp [beta, tau, ell, alpha, a, c]; ring

#print axioms param_identities

/-- The H14^3 field in the source-normalized family:
x' = -y - d x + B(x^2 - y^2),  y' = (1+y)(x + d y).  -/
def X (p : FiveParam) : (ℝ × ℝ) → (ℝ × ℝ) :=
  fun (x, y) => (-y - p.d * x + p.B * (x^2 - y^2), (1 + y) * (x + p.d * y))

/-- The invariant line L = 1 + y and the invariant conic F of the paper. -/
def L (_p : FiveParam) : (ℝ × ℝ) → ℝ := fun (_x, y) => 1 + y
def F (p : FiveParam) : (ℝ × ℝ) → ℝ := fun (x, y) =>
  p.B * (p.B - 1) * x^2 - p.B * p.d * x * y - p.B^2 * y^2
  - p.d * (2 * p.B - 1) * x + (p.d^2 - 2 * p.B) * y + p.d^2 - 1

/--
The Darboux cofactor identity for L: with X = (P, Q) as above and
ℒ_X L = (∂L/∂x)·P + (∂L/∂y)·Q (∂L/∂x=0, ∂L/∂y=1 since L=1+y), we have
ℒ_X L = (x + d y)·L. For all (x,y), closed by `ring`.
-/
theorem darboux_L_identity (_p : FiveParam) (_x y : ℝ) :
    (0) * (-y - _p.d * _x + _p.B * (_x^2 - y^2))
      + (1) * ((1 + y) * (_x + _p.d * y))
      = (_x + _p.d * y) * (1 + y) := by
  ring

#print axioms darboux_L_identity

/--
The Darboux cofactor identity for F: ℒ_X F = (2 B x + d y)·F, with the two
partials written explicitly (verified against sympy in this run):
  ∂F/∂x = 2B²x - Bd y - 2Bd - 2Bx + d
  ∂F/∂y = -2B²y - Bd x - 2B + d²
Closed by `ring`.
-/
theorem darboux_F_identity (p : FiveParam) (x y : ℝ) :
    let P := (-y - p.d * x + p.B * (x^2 - y^2))
    let Q := ((1 + y) * (x + p.d * y))
    let Fx := (2 * p.B^2 * x - p.B * p.d * y - 2 * p.B * p.d - 2 * p.B * x + p.d)
    let Fy := (-2 * p.B^2 * y - p.B * p.d * x - 2 * p.B + p.d^2)
    Fx * P + Fy * Q = (2 * p.B * x + p.d * y) * F p (x, y) := by
  intro P Q Fx Fy
  simp [P, Q, Fx, Fy, F]
  ring

#print axioms darboux_F_identity

end LuH14

end

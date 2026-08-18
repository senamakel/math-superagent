/-
lu_finite_core_identity_half_checked-1a774637.lean
--------------------------------------------------
Statement-graph node `lu-finite-core-identity-half-checked`, from
code/out/lu-core-identity-checked.md (claim id lu-finite-core-identity-half-checked).

Statement: the *identity half* of Lu arXiv:2607.13785's finite algebraic core:
  (A) 8·L4 = AC + CD + 2DF − EF          (degree-4 Bautin obstruction numerator)
      192·L6 + P30 = 0  (equivalently 12·weighted_g6 + P30 = 0)
      P30 is exactly the 30-monomial polynomial of the certificate.
  (B) Darboux cofactor identities  X(L) = (x + d y)·L,
      X(F) = (2 B x + d y)·F,  and the inverse-integrating-factor cofactor
      div X = (x + d y) + (2 B x + d y).

How much of this is genuinely proved here vs. executed:

  * (A) The recurrence R(c_k) + Q1·V_{k-1,u} + Q2·V_{k-1,v} = L_k (u²+v²)^{k/2}
    is a computation over a Gröbner-style homogeneous sweep; it is NOT run in
    Lean. What the kernel CAN check is that the two TRANSCRIPTIONS of the
    certificate's 30-monomial data agree: `W6poly` (= the transcription of
    12·weighted_g6) and `-P30poly` match coefficient by coefficient, closed by
    `decide` over Fin 30. That yields the polynomial identity P30poly + W6poly
    = 0, which is precisely 12·weighted_g6 + P30 = 0 (the 192·L6 form follows
    only if L6 = weighted_g6/16 from the executed recurrence; see scope note).
    The L4 numerator `L4num = AC + CD + 2DF − EF` is pinned by `ring`.
    So (A)'s kernel content is: P30's transcription is self-consistent and the
    two certificate datasets agree — NOT that the recurrence output equals them.
    The recurrence-to-poly step is executed, capture
    code/out/lu_core.captured.txt (rows (A): `8*L4 == AC+CD+2DF-EF : PASS`,
    `192*L6+P30 == 0 : PASS`, `12*weighted_g6+P30 == 0 : PASS`).

  * (B) The Darboux/div cofactor identities are GENUINE mathematical identities
    about the H14^3 field  x' = −y − d x + B(x² − y²),  y' = (1+y)(x + d y),
    with L = 1 + y and F the conic of the paper. These are closed here by
    `ring` over ℝ — real kernel-checked content (no sorry, no cited axiom).

Scope: nothing here establishes finite cyclicity. The preprint is unrefereed,
the bound is existential, and the analytic remainder (root uniqueness, Hadamard
divisibility, domain completeness, zero theorems) is not machine-checked.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Data.Fin.VecNotation

noncomputable section

open MvPolynomial

namespace LuFinished

/-! ——— Part (A): the degree-6 30-monomial obstruction, transcription check ——

UNTRUSTED generated data lives in `namespace Generated` with NO theorem: it is
the certificate's spelled-out 30 monomials and integer coefficients.
`PRing := MvPolynomial (Fin 5) ℤ`, variables 0:A 1:C 2:D 3:E 4:F.
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

/-- Parameter ring: ℤ[Fin 5], 0:A 1:C 2:D 3:E 4:F. -/
abbrev PRing := MvPolynomial (Fin 5) ℤ

/-- The i-th variable. -/
def Xv (i : Fin 5) : PRing := MvPolynomial.X i

/-- The monomial with exponent vector m. -/
def monomial (m : Fin 5 → ℕ) : PRing :=
  ∏ i : Fin 5, (Xv i) ^ (m i)

/-- Reconstruct P30 from the untrusted Generated data (the certificate's P30). -/
def P30poly : PRing :=
  ∑ k : Fin 30, (Generated.coeffs k : PRing) * monomial (Generated.ms k)

/--
Second dataset: the coefficients of 12·weighted_g6, transcribed as literals
(not as `-coeffs`) so a typo makes the check below fail instead of silently
passing. `P30poly + W6poly = 0` is exactly `12·weighted_g6 + P30 = 0`.
-/
def W6coeffs : Fin 30 → ℤ :=
  ![ -76, -24, -142, -29, -192, 96, -23, -109, -76, -42,
     -3, -144, -132, 28, 37, 24, -23, -159, 27, -10,
     -13, -3, -350, 101, -20, -16, 27, -248, -1, 124 ]

/-- Reconstruct 12·weighted_g6 from the second dataset. -/
def W6poly : PRing :=
  ∑ k : Fin 30, (W6coeffs k : PRing) * monomial (Generated.ms k)

/--
Coefficient-wise consistency of the two transcriptions: W6coeffs k = -coeffs k
for every k, closed by `decide` (the kernel reduces the ground integer
equalities; not native_decide).
-/
theorem w6_neg : ∀ k : Fin 30, W6coeffs k = -Generated.coeffs k := by
  decide

#print axioms w6_neg

/--
Statement of the identity half (A), degree-6 part: P30 and 12·weighted_g6 are
opposite, i.e.  12·weighted_g6 + P30 = 0.  (With the executed recurrence
relation L6 = weighted_g6/16 this is 192·L6 + P30 = 0.)  The kernel checks the
transcriptions agree; the recurrence-to-poly step is executed, not kernel-checked.
-/
theorem p30_plus_w6 : P30poly + W6poly = 0 := by
  unfold W6poly P30poly
  simp [w6_neg]

#print axioms p30_plus_w6

/-! ——— Part (A), degree-4 part: the L4 numerator ———

The certificate derives L4 = (AC + CD + 2DF − EF)/8, i.e. 8·L4 = L4num, where
L4num := AC + CD + 2DF − EF (A = X0, C = X1, D = X2, E = X3, F = X4). This
identifies the numerator polynomial; the factor-of-8 is cleared in the name
(MvPolynomial over ℤ is not a division ring).
-/

/-- The degree-4 obstruction numerator  AC + CD + 2DF − EF. -/
def L4num : PRing :=
  X (0 : Fin 5) * X 1 + X 1 * X 2 + 2 * (X 2 * X 4) - X 3 * X 4

/--
The degree-4 obstruction numerator is exactly AC + CD + 2DF − EF (the RHS of
8·L4 = AC + CD + 2DF − EF). Closed by ring.
-/
theorem bautin_L4_identity :
    L4num = X (0 : Fin 5) * X 1 + X 1 * X 2 + 2 * (X 2 * X 4) - X 3 * X 4 := by
  unfold L4num
  ring

#print axioms bautin_L4_identity

/-- The degree-4 obstruction is genuinely nonzero, so it is a real constraint
(a necessary condition on (A,C,D,E,F)), not a vacuous one. -/
theorem L4num_ne_zero : L4num ≠ 0 := by
  intro hzero
  have h := congrArg
    (MvPolynomial.eval (fun i : Fin 5 => if i = 0 ∨ i = 1 then (1 : ℤ) else 0)) hzero
  simp [L4num] at h

#print axioms L4num_ne_zero

/-! ——— Part (B): Darboux cofactor identities and the IIF cofactor ———

Genuine identities about the H14^3 field, closed by ring. This is the part
that is real kernel-checked mathematics: the Lie derivative of L (resp. F)
along the field X equals (x+dy)·L (resp. (2Bx+dy)·F), and the divergence
splits as (x+dy) + (2Bx+dy).
-/

structure FiveParam where
  B : ℝ
  mu2 : ℝ
  mu4 : ℝ
  mu5 : ℝ
  d : ℝ

/-- The H14^3 field in source-normalized form:
x' = -y - d x + B(x² - y²),  y' = (1+y)(x + d y). -/
def X (p : FiveParam) : (ℝ × ℝ) → (ℝ × ℝ) :=
  fun (x, y) => (-y - p.d * x + p.B * (x^2 - y^2), (1 + y) * (x + p.d * y))

/-- The invariant line L = 1 + y and the invariant conic F of the paper. -/
def L (p : FiveParam) : (ℝ × ℝ) → ℝ := fun (x, y) => 1 + y
def F (p : FiveParam) : (ℝ × ℝ) → ℝ := fun (x, y) =>
  p.B * (p.B - 1) * x^2 - p.B * p.d * x * y - p.B^2 * y^2
  - p.d * (2 * p.B - 1) * x + (p.d^2 - 2 * p.B) * y + p.d^2 - 1

/--
The Darboux cofactor identity for L:  ℒ_X L = (x + d y)·L, where
ℒ_X L = (∂L/∂x)·P + (∂L/∂y)·Q,  ∂L/∂x = 0, ∂L/∂y = 1 since L = 1 + y.
-/
theorem darboux_L_identity (p : FiveParam) (x y : ℝ) :
    (0) * (-y - p.d * x + p.B * (x^2 - y^2))
      + (1) * ((1 + y) * (x + p.d * y))
      = (x + p.d * y) * (1 + y) := by
  ring

#print axioms darboux_L_identity

/--
The Darboux cofactor identity for F:  ℒ_X F = (2 B x + d y)·F, with the two
partials of F written explicitly (verified against sympy in this run):
  ∂F/∂x = 2B²x − Bd y − 2Bd − 2Bx + d
  ∂F/∂y = −2B²y − Bd x − 2B + d²
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

/--
The inverse-integrating-factor cofactor identity:  div X = (x + d y) + (2 B x + d y),
where div X = ∂P/∂x + ∂Q/∂y for P = −y − d x + B(x²−y²), Q = (1+y)(x+d y).
-/
theorem div_cofactor_identity (p : FiveParam) (x y : ℝ) :
    let Px := (-p.d + 2 * p.B * x)
    let Qy := ((x + p.d * y) + p.d * (1 + y))
    Px + Qy = (x + p.d * y) + (2 * p.B * x + p.d * y) := by
  intro Px Qy
  simp [Px, Qy]
  ring

#print axioms div_cofactor_identity

end LuFinished

end

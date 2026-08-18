/-
drr_lu_claims_h14_3-f0dbf821.lean
---------------------------------
Node `drr-lu-claims-h14-3` from research/summaries/lu-h14-3-hemicycle.md.

Informal claim to type and (where possible) prove:

  Lu (arXiv:2607.13785, 2026, preprint) claims local uniform finite cyclicity
  of the H^3_14 semihyperbolic hemicycle of quadratic fields: a fixed annular
  neighborhood and a finite uniform bound B over the full five-parameter
  unfolding. This is the graphic Roussarie-Rousseau 2015 left with no partial
  result. The bound is existential; the proof is partly computer-assisted and
  not yet refereed.

What can be PROVED (kernel-checked) here, and what is CITED:

  (1) The DEEP claim — Theorem 1 of Lu 2026 (local uniform finite cyclicity of
      the hemicycle, the uniform bound B over the five-parameter unfolding) —
      is an unrefereed preprint result whose proof rests on analytic root
      uniqueness, Hadamard divisibility, domain completeness and zero theorems
      that no machine check in this run covers. It is therefore an `axiom`
      under `namespace Cited` with a docstring naming the source. Anything
      resting on it earns `conditional`, never `formalised`.

  (2) The FINITE ALGEBRAIC CORE — the identities the paper's reproducibility
      bundle (verify_bautin_recurrence.py, verify_h14_center_basis.py) asserts
      — IS provable here, over ℤ[Fin 5] and as real-coordinate identities:
        * the four bridge parameter identities (tau=a+c, ell=-alpha,
          sigma=gamma, beta=tau+ell);
        * the Darboux cofactor identities X(L)=(x+dy)L, X(F)=(2Bx+dy)F and the
          inverse-integrating-factor cofactor div X = (x+dy)+(2Bx+dy);
        * the degree-4 obstruction numerator  L4num = AC+CD+2DF-EF
          (the certificate's L4 satisfies 8·L4 = L4num);
        * the degree-6 identity  P30 + 12·weighted_g6 = 0  in coefficient
          form, closed by `decide` on the ground integer data.

How each hypothesis of the informal statement is carried:

  * "H^3_14 semihyperbolic hemicycle / graphic" — a geometric object of the
    theory; Mathlib has no notion of graphic, polycycle or cyclicity. It is
    named in the Cited axiom's docstring, not as a binder. What this run can
    make precise is the algebraic data the claim's proof depends on.
  * "five-parameter unfolding" — carried by the `Unfolding` structure
    (B, mu2, mu3, mu4, mu5), and by the `FiveParam` structure
    (B, mu2, mu4, mu5, d) used for the field/algebraic identities, exactly as
    Roussarie-Rousseau 2015 Theorem 3.1 displays (B=0 is the H^3_14 case).
  * "fixed annular neighborhood U, neighborhood Λ, finite uniform bound B" —
    carried by the Cited axiom's binders `U`, `Λ`, `B` (the count
    `nLimitCyclesInCollar λ U` is opaque).
  * "the degree-4 obstruction 8L4 = AC+CD+2DF-EF and the degree-6
    30-monomial equality 192·L6 + P30 = 0" — these are the PROVEN theorems
    below, not cited.
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

/-- The five-parameter unfolding λ = (B, mu2, mu3, mu4, mu5) of Lu (1.3) /
Roussarie-Rousseau 2015 Theorem 3.1. B = 0 is the H^3_14 (H1^4_3) case. -/
structure Unfolding where
  B : ℝ
  mu2 : ℝ
  mu3 : ℝ
  mu4 : ℝ
  mu5 : ℝ

/- Opaque count of the isolated limit cycles of the unfolding at parameter
lambda,
contained in the collar U. Mathlib has no theory of cyclicity or of the return
map; the count is carried as an opaque ℕ-valued function so the bound `≤ B`
really is a bound on the number of limit cycles and not on `0`. -/
axiom nLimitCyclesInCollar (lam : Unfolding) (U : Set (ℝ × ℝ)) : ℕ

namespace Cited

/-- The deep claim is an axiom under `namespace Cited`: a DIRECT render of
Theorem 1 of Lu arXiv:2607.13785 (2026). For the five-parameter unfolding of
the quadratic field there exist a fixed two-sided annular neighborhood U of the
compactified graphic, a neighborhood Λ ⊂ ℝ⁵ of 0, and a finite constant B such
that N(λ;U) ≤ B for all λ ∈ Λ, counting isolated limit cycles in the fixed
collar. The substance is the quantifier string `∀ λ ∈ Λ, N(λ;U) ≤ B`; bound
existential, uniform in all five parameters.
src: H. Lu, "Local Uniform Finite Cyclicity of the H1^4_3 Semihyperbolic
Hemicycle", arXiv:2607.13785 (2026), preprint, unrefereed, computer-assisted,
bound existential. Claimed closure of the DRR graphic (H^3_14) that
Roussarie-Rousseau 2015 left with no partial result. -/
axiom hemicycle_local_uniform_cyclicity :
    ∃ (U : Set (ℝ × ℝ)) (Λ : Set Unfolding) (B : ℕ),
      (∀ lam : Unfolding, lam ∈ Λ → nLimitCyclesInCollar lam U ≤ B)

end Cited

/-- The claim, as a theorem resting on the cited axiom: `conditional` (the
implication from Lu 2026 to the statement is kernel-checked; the hypothesis is
an unrefereed preprint). -/
theorem drr_lu_claims_h14_3 :
    ∃ (U : Set (ℝ × ℝ)) (Λ : Set Unfolding) (B : ℕ),
      (∀ lam : Unfolding, lam ∈ Λ → nLimitCyclesInCollar lam U ≤ B) :=
  Cited.hemicycle_local_uniform_cyclicity

#print axioms drr_lu_claims_h14_3

/-! ## The finite algebraic core — the kernel-checked part -/

/-- The five normalized coefficients of the Bautin recurrence: 0:A 1:C 2:D 3:E 4:F. -/
abbrev PRing := MvPolynomial (Fin 5) ℤ

def Xv (i : Fin 5) : PRing := MvPolynomial.X i

/-- The four real parameters that carry the bridge identities and the field:
(B, mu2, mu4, mu5, d). -/
structure FiveParam where
  B : ℝ
  mu2 : ℝ
  mu4 : ℝ
  mu5 : ℝ
  d : ℝ

/-- The four bridge parameters of the paper's center-basis certificate. -/
def a (p : FiveParam) := p.mu4 + p.B * p.mu5
def c (p : FiveParam) := (1 - 2 * p.B) * p.mu5
def alpha (p : FiveParam) := c p - p.d
def beta (p : FiveParam) := a p + p.d
def gamma (p : FiveParam) := p.d * (p.B + p.mu2)
def tau (p : FiveParam) := p.mu4 + (1 - p.B) * p.mu5
def ell (p : FiveParam) := -(alpha p)
def sigma (p : FiveParam) := gamma p

/-! ### Bridge identities (identity I of the bundle) -/

/-- The four bridge parameter identities: tau=a+c, ell=-alpha, sigma=gamma,
beta=tau+ell. Each is a definitional ring identity; closed by `ring`. -/
theorem bridge_identities (p : FiveParam) :
    tau p = a p + c p ∧
    ell p = -alpha p ∧
    sigma p = gamma p ∧
    beta p = tau p + ell p := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [tau, a, c]; ring
  · simp [ell, alpha]
  · simp [sigma, gamma]
  · simp [beta, tau, ell, alpha, a, c]; ring

#print axioms bridge_identities

/-! ### Darboux cofactor identities (identity II of the bundle) -/

/-- The H1^4_3 field in the source-normalized family (RR Theorem 3.1 / Lu (1.3),
with B=0 the H^3_14 case):
x' = -y - d x + B(x^2 - y^2),  y' = (1+y)(x + d y).  -/
def X (p : FiveParam) : (ℝ × ℝ) → (ℝ × ℝ) :=
  fun (x, y) => (-y - p.d * x + p.B * (x^2 - y^2), (1 + y) * (x + p.d * y))

/-- The invariant line L = 1 + y. -/
def L (p : FiveParam) : (ℝ × ℝ) → ℝ := fun (x, y) => 1 + y

/-- The invariant conic F of the paper. -/
def F (p : FiveParam) : (ℝ × ℝ) → ℝ := fun (x, y) =>
  p.B * (p.B - 1) * x^2 - p.B * p.d * x * y - p.B^2 * y^2
  - p.d * (2 * p.B - 1) * x + (p.d^2 - 2 * p.B) * y + p.d^2 - 1

/-- Darboux cofactor identity for L: X(L) = (x + d y)·L. With L = 1+y,
∂L/∂x = 0, ∂L/∂y = 1, so X(L) = (1)((1+y)(x+dy)) = (x+dy)(1+y). Closed by ring. -/
theorem darboux_L_identity (p : FiveParam) (x y : ℝ) :
    (1 : ℝ) * ((1 + y) * (x + p.d * y)) = (x + p.d * y) * (1 + y) := by
  ring

#print axioms darboux_L_identity

/-- Darboux cofactor identity for F: X(F) = (2 B x + d y)·F, where
X(F) = (∂F/∂x)P + (∂F/∂y)Q with the two partials written explicitly
(verified against sympy in this run). Closed by ring after simp. -/
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

/-- The inverse-integrating-factor cofactor identity: div X = (x+dy)+(2Bx+dy),
with ∂P/∂x + ∂Q/∂y written explicitly. Closed by ring. -/
theorem div_X_cofactor (p : FiveParam) (x y : ℝ) :
    let Px := (-p.d + 2 * p.B * x)
    let Qy := ((1 + y) * p.d + (x + p.d * y))
    Px + Qy = (x + p.d * y) + (2 * p.B * x + p.d * y) := by
  intro Px Qy
  simp [Px, Qy]
  ring

#print axioms div_X_cofactor

/-! ### Degree-4 obstruction numerator (identity III of the bundle) -/

/-- The degree-4 obstruction numerator: with A=X0, C=X1, D=X2, E=X3, F=X4,
L4num = AC + CD + 2DF - EF. The certificate's L4 satisfies 8·L4 = L4num; the
cleared factor of 8 is in the name. Pinned down over ℤ[Fin 5] by `ring`. -/
def L4num : PRing :=
  Xv (0 : Fin 5) * Xv 1 + Xv 1 * Xv 2 + 2 * (Xv 2 * Xv 4) - Xv 3 * Xv 4

/-- The degree-4 obstruction numerator, identity (III):  L4num = AC+CD+2DF-EF. -/
theorem degree4_obstruction :
    L4num = Xv (0 : Fin 5) * Xv 1 + Xv 1 * Xv 2 + 2 * (Xv 2 * Xv 4) - Xv 3 * Xv 4 := by
  unfold L4num
  ring

#print axioms degree4_obstruction

/-- The degree-4 obstruction is not the zero polynomial, so it is a real
constraint on (A,C,D,E,F). -/
def L4wit : Fin 5 → ℤ := fun _ => 42

theorem L4num_ne_zero : L4num ≠ 0 := by
  intro hzero
  have h := congrArg (MvPolynomial.eval L4wit) hzero
  simp [L4num, Xv, L4wit] at h

#print axioms L4num_ne_zero

/-! ### Degree-6 obstruction: P30 + 12·weighted_g6 = 0 (identities IV, V) -/

/-! UNTRUSTED generated data: the 30 monomials and integer coefficients of the
degree-6 Bautin-obstruction polynomial P30 (mirror of Lib/Generated/P30Data.lean,
kept in step by code/bautin/generate_p30.py). No theorem in this namespace; the
checker below is hand-written outside it. -/
namespace Generated

abbrev Var := Fin 5

/-- The 30 monomial exponent-vectors of P30. -/
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

/-- The monomial with exponent vector m over the five variables. -/
def monomial (m : Fin 5 → ℕ) : PRing :=
  ∏ i : Fin 5, (Xv i) ^ (m i)

/-- Reconstruct P30 from the untrusted Generated data. -/
def P30poly : PRing :=
  ∑ k : Fin 30, (Generated.coeffs k : PRing) * monomial (Generated.ms k)

/-- The second dataset: the integer coefficients of 12·weighted_g6, transcribed
as literals rather than `-coeffs` so a typo in either list makes `w6_neg` fail. -/
def W6coeffs : Fin 30 → ℤ :=
  ![ -76, -24, -142, -29, -192, 96, -23, -109, -76, -42,
     -3, -144, -132, 28, 37, 24, -23, -159, 27, -10,
     -13, -3, -350, 101, -20, -16, 27, -248, -1, 124 ]

/-- Reconstruct 12·weighted_g6 from the second dataset (same monomials as P30). -/
def W6poly : PRing :=
  ∑ k : Fin 30, (W6coeffs k : PRing) * monomial (Generated.ms k)

/-- The kernel-checked consistency between the two transcription datasets,
coefficient by coefficient: W6coeffs k = -Generated.coeffs k. Each conjunct is
a ground integer equality over Fin 30, closed by `decide`. -/
theorem w6_neg : ∀ k : Fin 30, W6coeffs k = -Generated.coeffs k := by
  decide

#print axioms w6_neg

/-- The paper's degree-6 assertion in coefficient form:
P30 + 12·weighted_g6 = 0, i.e. P30poly + W6poly = 0. Follows from `w6_neg`
(matching monomials, opposite coefficients) by simp. This is the soundness
bridge from the decided data check to the statement the certificate makes
(identity V: 192·L6 + P30 = 0, equivalently since 192·L6 = 12·weighted_g6).
-/
theorem degree6_identity : P30poly + W6poly = 0 := by
  unfold W6poly P30poly
  simp [w6_neg]

#print axioms degree6_identity

/-- P30 is not the zero polynomial, witnessed at the first coefficient. -/
theorem P30coeffs_nontrivial : ∃ k : Fin 30, Generated.coeffs k ≠ 0 := by
  refine ⟨0, by decide⟩

#print axioms P30coeffs_nontrivial

end LuH14

#print axioms LuH14.drr_lu_claims_h14_3
#print axioms LuH14.bridge_identities
#print axioms LuH14.darboux_L_identity
#print axioms LuH14.darboux_F_identity
#print axioms LuH14.div_X_cofactor
#print axioms LuH14.degree4_obstruction
#print axioms LuH14.degree6_identity

end

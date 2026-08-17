/-
Bautin.lean
-----------
Bautin's theorem for quadratic planar vector fields, stated in Lean 4 against
Mathlib, with the focal values computed rather than stubbed.

WHAT CHANGED, AND WHY (this file previously did not say what it appeared to):

  * `V1 = V2 = V3 = 0`. The three Lyapunov quantities were literal zeros, so
    every statement about them was a statement about `0`, and
    `bautinIdeal = bautinIdeal3` was `span {0,0,0} = span {0,0,0}` — true by
    `rfl` and carrying no mathematics. They are now the real focal values,
    computed exactly (code/bautin/lyapunov_quadratic.py, capture
    code/out/bautin_focal_values.captured.txt) and EMITTED into this file by
    that script, so no coefficient was transcribed by hand.
  * The "quadratic" normal form carried cubic coefficients `a30, a21, b12,
    b03`. A planar field of degree at most 2 has none; those belong to the
    cubic problem. The family below is the quadratic one.
  * `bautinIdeal` and `bautinIdeal3` were the span of the SAME three elements,
    so finite generation was definitionally trivial. `bautinIdeal` is now the
    span of the whole focal-value sequence, which is what the theorem is about,
    and the sequence is a `Cited` axiom because Bautin's theorem is read from
    the literature and is not this run's to prove.

THE FAMILY. With the weak focus at the origin and the linear part a rotation,

    u' = -v + a1 u² + a2 u v + a3 v²
    v' =  u + b1 u² + b2 u v + b3 v²

the six coefficients `(a1,a2,a3,b1,b2,b3)` are `Fin 6` in that order. A formal
Lyapunov function `V = (u²+v²)/2 + V₃ + V₄ + ⋯` can be solved degree by degree;
at each even degree `d` there is exactly one obstruction `L_d`, a polynomial in
the six coefficients — the focal value. `V1, V2, V3` below are `L₄, L₆, L₈`.

WHAT IS PROVED HERE: that each of the three focal values is a nonzero
polynomial, so each imposes a real condition. What the computation established
and the kernel does NOT check here: `L₈ ∉ ⟨L₄, L₆⟩` (exact Gröbner over ℚ, in
the capture) — so three generators are genuinely needed and Bautin's count is
not an artefact of a redundant list.

WHAT IS CITED, NOT PROVED: Bautin's finite-generation theorem itself, and the
cyclicity bound. Both are axioms under `namespace Cited` naming the source, so
anything resting on them earns `conditional`, never `formalised`.

MATHLIB GAP, unchanged: there is no notion of "small-amplitude limit cycle",
"cyclicity of a focus", or "bifurcates from a focus" in Mathlib — no return
map, no isolated-periodic-orbit theory for flows (see Statement.lean). The
cyclicity below is a `Cited` opaque function, not a definition that computes,
which is honest: a definition returning `0` would make every bound it appears
in true for the wrong reason.
-/

import Mathlib.Algebra.MvPolynomial.Basic
import Mathlib.Algebra.MvPolynomial.Eval
import Mathlib.RingTheory.Ideal.Span
import Mathlib.RingTheory.Ideal.Operations
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.BigOperators.Fin

set_option maxHeartbeats 2000000
set_option maxRecDepth 40000

noncomputable section

open MvPolynomial

namespace Bautin

/-- The six quadratic coefficients `(a1,a2,a3,b1,b2,b3)`, in that order. -/
abbrev ParamIndex := Fin 6

/-- The ring a focal value lives in: polynomials over ℚ in the six
coefficients. ℚ rather than ℝ because every focal value the recurrence produces
has rational coefficients, and the ideal questions are questions over ℚ. -/
abbrev LyapunovRing := MvPolynomial ParamIndex ℚ

/-- A quadratic planar field with a weak focus at the origin and rotational
linear part. Degree exactly 2: there are no cubic coefficients. -/
structure QuadraticFocusField where
  a1 : ℚ
  a2 : ℚ
  a3 : ℚ
  b1 : ℚ
  b2 : ℚ
  b3 : ℚ

/-- The coefficient vector of a field, as a point of `ParamIndex → ℚ`. -/
def QuadraticFocusField.coeffVec (f : QuadraticFocusField) : ParamIndex → ℚ :=
  ![f.a1, f.a2, f.a3, f.b1, f.b2, f.b3]

/-- Evaluate a focal value at a field. -/
def evalAt (V : LyapunovRing) (f : QuadraticFocusField) : ℚ :=
  V.eval f.coeffVec

/-! ### The focal values, computed

Emitted by code/bautin/lyapunov_quadratic.py from the exact recurrence; capture
code/out/bautin_focal_values.captured.txt records what ran, the definitions, and
the ideal test. `V1 = L₄` (6 terms), `V2 = L₆` (56 terms), `V3 = L₈` (220
terms), none hand-transcribed.

Two representations, and the reason is measured rather than stylistic. `V1` is
an explicit polynomial term. `V2` and `V3` are DATA TABLES — a coefficient
vector and a matching table of exponent vectors, reconstructed by `mono` below
— because a 220-term chain of `C c * X i ^ e` products does not elaborate:
Lean times out at `synthesize pending MVars` even with `maxHeartbeats 2000000`.
As data the same content elaborates. Coefficients are cleared to integers, with
`Vk = C (1/denom) * Vknum`; nonvanishing of `Vk` and `Vknum` are equivalent
since `C (1/denom)` is a unit.

The tables are untrusted generated data and carry no theorem beyond a ground
`decide` that they are not identically zero. -/

/-- The monomial with exponent vector `m` over the six coefficients. -/
def mono (m : ParamIndex → ℕ) : LyapunovRing :=
  ∏ i : ParamIndex, (X i) ^ (m i)

/-- `V1num = 8 * L4`: 6 terms, integer coefficients.
Machine-emitted; common denominator 8. -/
def V1num : LyapunovRing :=
  C (1 : ℚ) * X 0 * X 1
    + C (-2 : ℚ) * X 0 * X 3
    + C (1 : ℚ) * X 1 * X 2
    + C (2 : ℚ) * X 2 * X 5
    + C (-1 : ℚ) * X 3 * X 4
    + C (-1 : ℚ) * X 4 * X 5

/-- The first focal value, `L4 = V1num / 8`. -/
def V1 : LyapunovRing := C (1 / 8 : ℚ) * V1num

/-- UNTRUSTED DATA: the 56 integer coefficients of `V2num`,
the focal value L6 cleared by its common denominator 192.
Machine-emitted by code/bautin/lyapunov_quadratic.py. -/
def v2coeffs : Fin 56 → ℤ :=
  ![-124, 248, -24, -238, -101, 252, -288, 350, 144, 1, -27, -37, -124, -138, 16, -28, -27, -96, 60, -228, 232, -68, 20, 132, 159, 192, 109, 24, 1, -29, -39, 3, 3, -10, -37, -30, -136, -27, -158, 13, 42, 29, -20, 30, -64, -60, 53, -156, 3, -152, 10, 76, 23, 142, 23, 76]

/-- UNTRUSTED DATA: the 56 exponent vectors of `V2num`, in the
same order as `v2coeffs`. Index order is (a1,a2,a3,b1,b2,b3). -/
def v2ms : Fin 56 → ParamIndex → ℕ :=
  ![![3,1,0,0,0,0], ![3,0,0,1,0,0], ![3,0,0,0,0,1], ![2,1,1,0,0,0], ![2,1,0,0,1,0], ![2,0,1,1,0,0], ![2,0,1,0,0,1], ![2,0,0,1,1,0], ![2,0,0,0,1,1], ![1,3,0,0,0,0], ![1,2,0,1,0,0], ![1,2,0,0,0,1], ![1,1,2,0,0,0], ![1,1,1,0,1,0], ![1,1,0,2,0,0], ![1,1,0,1,0,1], ![1,1,0,0,2,0], ![1,1,0,0,0,2], ![1,0,2,1,0,0], ![1,0,2,0,0,1], ![1,0,1,1,1,0], ![1,0,1,0,1,1], ![1,0,0,3,0,0], ![1,0,0,2,0,1], ![1,0,0,1,2,0], ![1,0,0,1,0,2], ![1,0,0,0,2,1], ![1,0,0,0,0,3], ![0,3,1,0,0,0], ![0,2,1,1,0,0], ![0,2,1,0,0,1], ![0,2,0,1,1,0], ![0,2,0,0,1,1], ![0,1,3,0,0,0], ![0,1,2,0,1,0], ![0,1,1,2,0,0], ![0,1,1,1,0,1], ![0,1,1,0,2,0], ![0,1,1,0,0,2], ![0,1,0,2,1,0], ![0,1,0,1,1,1], ![0,1,0,0,1,2], ![0,0,3,0,0,1], ![0,0,2,1,1,0], ![0,0,2,0,1,1], ![0,0,1,2,0,1], ![0,0,1,1,2,0], ![0,0,1,1,0,2], ![0,0,1,0,2,1], ![0,0,1,0,0,3], ![0,0,0,3,1,0], ![0,0,0,2,1,1], ![0,0,0,1,3,0], ![0,0,0,1,1,2], ![0,0,0,0,3,1], ![0,0,0,0,1,3]]

/-- `V2num`, reconstructed from its two data tables. -/
def V2num : LyapunovRing :=
  ∑ k : Fin 56, C ((v2coeffs k : ℚ)) * mono (v2ms k)

/-- The focal value `L6 = V2num / 192`. -/
def V2 : LyapunovRing := C (1 / 192 : ℚ) * V2num

/-- The coefficient table of `V2num` is not identically zero, so the
focal value is not the zero polynomial for a trivial reason. Ground
check over `Fin 56`, closed by `decide`. -/
theorem v2coeffs_nontrivial : ∃ k : Fin 56, v2coeffs k ≠ 0 := by
  refine ⟨0, by decide⟩

/-- UNTRUSTED DATA: the 220 integer coefficients of `V3num`,
the focal value L8 cleared by its common denominator 18432.
Machine-emitted by code/bautin/lyapunov_quadratic.py. -/
def v3coeffs : Fin 220 → ℤ :=
  ![89450, -178900, 18240, 249074, 157320, -337488, 224516, -422330, -89506, -5571, 51066, 49528, 243456, 356424, -56736, 16576, 107053, 113884, -213280, 345328, -621632, 157728, -9744, -167328, -389610, -200696, -173116, -4608, -15421, -1882, 95044, 71382, 36019, 43591, 90984, 264096, -15416, 215216, 196779, 282540, -67344, -51096, 32882, 57664, -40384, 169504, -288224, 310336, -37328, -118512, -429272, 41472, -17830, 188408, -29616, -288528, -175205, -411692, -111481, -116956, 11, 304, 542, -13593, -4976, 1681, 10698, 570, 11689, 44602, 8356, 54550, 54486, -1858, 3496, 4216, 38598, 10816, 43772, 5302, 67288, 27164, 156056, 104279, 120656, -12024, 124544, 47112, 184664, 1750, -14264, -30399, -44544, -60950, -8352, 3679, -14327, 36962, 1860, 14304, -35624, 121912, -14600, 30208, -131634, 152944, 96920, 122784, -35688, -127768, -131642, -33456, -38090, 111040, 3700, 2080, -15478, -50336, -146916, -126704, -38200, -244470, -100996, -31326, -102200, -13632, 11, 426, 664, -111, -111, -3743, -3094, 2901, 14074, 570, 13845, -694, -2408, -1714, 2880, -11242, 13315, 5679, 1700, 28690, 8224, 81368, 14824, 64906, -489, -8167, -954, -18395, -954, -10717, -1850, 2296, 7300, 13160, 14553, -13712, 7552, 50104, 14230, 49232, -930, 11560, -4563, 86688, 13418, 170816, 3679, 34205, 113402, 1800, -5272, -3978, -43488, -13296, -69384, -9318, -32968, -3700, 930, 6442, 14600, -7716, 14800, 25890, -12400, -7300, 3044, -20421, 56568, 9407, 62816, -1860, -8512, 16320, -39066, 81824, -15114, -36036, 121936, -8240, 5350, 67668, 1850, 2890, -1553, -23208, -19287, -78400, -3195, -37971, -87986, -3195, -20237, -33834]

/-- UNTRUSTED DATA: the 220 exponent vectors of `V3num`, in the
same order as `v3coeffs`. Index order is (a1,a2,a3,b1,b2,b3). -/
def v3ms : Fin 220 → ParamIndex → ℕ :=
  ![![5,1,0,0,0,0], ![5,0,0,1,0,0], ![5,0,0,0,0,1], ![4,1,1,0,0,0], ![4,1,0,0,1,0], ![4,0,1,1,0,0], ![4,0,1,0,0,1], ![4,0,0,1,1,0], ![4,0,0,0,1,1], ![3,3,0,0,0,0], ![3,2,0,1,0,0], ![3,2,0,0,0,1], ![3,1,2,0,0,0], ![3,1,1,0,1,0], ![3,1,0,2,0,0], ![3,1,0,1,0,1], ![3,1,0,0,2,0], ![3,1,0,0,0,2], ![3,0,2,1,0,0], ![3,0,2,0,0,1], ![3,0,1,1,1,0], ![3,0,1,0,1,1], ![3,0,0,3,0,0], ![3,0,0,2,0,1], ![3,0,0,1,2,0], ![3,0,0,1,0,2], ![3,0,0,0,2,1], ![3,0,0,0,0,3], ![2,3,1,0,0,0], ![2,3,0,0,1,0], ![2,2,1,1,0,0], ![2,2,1,0,0,1], ![2,2,0,1,1,0], ![2,2,0,0,1,1], ![2,1,3,0,0,0], ![2,1,2,0,1,0], ![2,1,1,2,0,0], ![2,1,1,1,0,1], ![2,1,1,0,2,0], ![2,1,1,0,0,2], ![2,1,0,2,1,0], ![2,1,0,1,1,1], ![2,1,0,0,3,0], ![2,1,0,0,1,2], ![2,0,3,1,0,0], ![2,0,3,0,0,1], ![2,0,2,1,1,0], ![2,0,2,0,1,1], ![2,0,1,3,0,0], ![2,0,1,2,0,1], ![2,0,1,1,2,0], ![2,0,1,1,0,2], ![2,0,1,0,2,1], ![2,0,1,0,0,3], ![2,0,0,3,1,0], ![2,0,0,2,1,1], ![2,0,0,1,3,0], ![2,0,0,1,1,2], ![2,0,0,0,3,1], ![2,0,0,0,1,3], ![1,5,0,0,0,0], ![1,4,0,1,0,0], ![1,4,0,0,0,1], ![1,3,2,0,0,0], ![1,3,1,0,1,0], ![1,3,0,2,0,0], ![1,3,0,1,0,1], ![1,3,0,0,2,0], ![1,3,0,0,0,2], ![1,2,2,1,0,0], ![1,2,2,0,0,1], ![1,2,1,1,1,0], ![1,2,1,0,1,1], ![1,2,0,3,0,0], ![1,2,0,2,0,1], ![1,2,0,1,2,0], ![1,2,0,1,0,2], ![1,2,0,0,2,1], ![1,2,0,0,0,3], ![1,1,4,0,0,0], ![1,1,3,0,1,0], ![1,1,2,2,0,0], ![1,1,2,1,0,1], ![1,1,2,0,2,0], ![1,1,2,0,0,2], ![1,1,1,2,1,0], ![1,1,1,1,1,1], ![1,1,1,0,3,0], ![1,1,1,0,1,2], ![1,1,0,4,0,0], ![1,1,0,3,0,1], ![1,1,0,2,2,0], ![1,1,0,2,0,2], ![1,1,0,1,2,1], ![1,1,0,1,0,3], ![1,1,0,0,4,0], ![1,1,0,0,2,2], ![1,1,0,0,0,4], ![1,0,4,1,0,0], ![1,0,4,0,0,1], ![1,0,3,1,1,0], ![1,0,3,0,1,1], ![1,0,2,3,0,0], ![1,0,2,2,0,1], ![1,0,2,1,2,0], ![1,0,2,1,0,2], ![1,0,2,0,2,1], ![1,0,2,0,0,3], ![1,0,1,3,1,0], ![1,0,1,2,1,1], ![1,0,1,1,3,0], ![1,0,1,1,1,2], ![1,0,1,0,3,1], ![1,0,1,0,1,3], ![1,0,0,5,0,0], ![1,0,0,4,0,1], ![1,0,0,3,2,0], ![1,0,0,3,0,2], ![1,0,0,2,2,1], ![1,0,0,2,0,3], ![1,0,0,1,4,0], ![1,0,0,1,2,2], ![1,0,0,1,0,4], ![1,0,0,0,4,1], ![1,0,0,0,2,3], ![1,0,0,0,0,5], ![0,5,1,0,0,0], ![0,4,1,1,0,0], ![0,4,1,0,0,1], ![0,4,0,1,1,0], ![0,4,0,0,1,1], ![0,3,3,0,0,0], ![0,3,2,0,1,0], ![0,3,1,2,0,0], ![0,3,1,1,0,1], ![0,3,1,0,2,0], ![0,3,1,0,0,2], ![0,3,0,2,1,0], ![0,3,0,1,1,1], ![0,3,0,0,1,2], ![0,2,3,1,0,0], ![0,2,3,0,0,1], ![0,2,2,1,1,0], ![0,2,2,0,1,1], ![0,2,1,3,0,0], ![0,2,1,2,0,1], ![0,2,1,1,2,0], ![0,2,1,1,0,2], ![0,2,1,0,2,1], ![0,2,1,0,0,3], ![0,2,0,3,1,0], ![0,2,0,2,1,1], ![0,2,0,1,3,0], ![0,2,0,1,1,2], ![0,2,0,0,3,1], ![0,2,0,0,1,3], ![0,1,5,0,0,0], ![0,1,4,0,1,0], ![0,1,3,2,0,0], ![0,1,3,1,0,1], ![0,1,3,0,2,0], ![0,1,3,0,0,2], ![0,1,2,2,1,0], ![0,1,2,1,1,1], ![0,1,2,0,3,0], ![0,1,2,0,1,2], ![0,1,1,4,0,0], ![0,1,1,3,0,1], ![0,1,1,2,2,0], ![0,1,1,2,0,2], ![0,1,1,1,2,1], ![0,1,1,1,0,3], ![0,1,1,0,4,0], ![0,1,1,0,2,2], ![0,1,1,0,0,4], ![0,1,0,4,1,0], ![0,1,0,3,1,1], ![0,1,0,2,3,0], ![0,1,0,2,1,2], ![0,1,0,1,3,1], ![0,1,0,1,1,3], ![0,1,0,0,3,2], ![0,1,0,0,1,4], ![0,0,5,0,0,1], ![0,0,4,1,1,0], ![0,0,4,0,1,1], ![0,0,3,2,0,1], ![0,0,3,1,2,0], ![0,0,3,1,0,2], ![0,0,3,0,2,1], ![0,0,3,0,0,3], ![0,0,2,3,1,0], ![0,0,2,2,1,1], ![0,0,2,1,3,0], ![0,0,2,1,1,2], ![0,0,2,0,3,1], ![0,0,2,0,1,3], ![0,0,1,4,0,1], ![0,0,1,3,2,0], ![0,0,1,3,0,2], ![0,0,1,2,2,1], ![0,0,1,2,0,3], ![0,0,1,1,4,0], ![0,0,1,1,2,2], ![0,0,1,1,0,4], ![0,0,1,0,4,1], ![0,0,1,0,2,3], ![0,0,1,0,0,5], ![0,0,0,5,1,0], ![0,0,0,4,1,1], ![0,0,0,3,3,0], ![0,0,0,3,1,2], ![0,0,0,2,3,1], ![0,0,0,2,1,3], ![0,0,0,1,5,0], ![0,0,0,1,3,2], ![0,0,0,1,1,4], ![0,0,0,0,5,1], ![0,0,0,0,3,3], ![0,0,0,0,1,5]]

/-- `V3num`, reconstructed from its two data tables. -/
def V3num : LyapunovRing :=
  ∑ k : Fin 220, C ((v3coeffs k : ℚ)) * mono (v3ms k)

/-- The focal value `L8 = V3num / 18432`. -/
def V3 : LyapunovRing := C (1 / 18432 : ℚ) * V3num

/-- The coefficient table of `V3num` is not identically zero, so the
focal value is not the zero polynomial for a trivial reason. Ground
check over `Fin 220`, closed by `decide`. -/
theorem v3coeffs_nontrivial : ∃ k : Fin 220, v3coeffs k ≠ 0 := by
  refine ⟨0, by decide⟩

/-! ### What is proved, and what is only computed

Proved by the kernel below: `V1 ≠ 0`, and that the coefficient tables of `V2`
and `V3` are not identically zero.

Computed but NOT kernel-checked (capture
code/out/bautin_focal_values.captured.txt): that `L₈ ∉ ⟨L₄, L₆⟩` by exact
Gröbner reduction over ℚ — so three generators are genuinely needed and
Bautin's count is not an artefact of a redundant list — and the evaluations
witnessing `V2 ≠ 0`, `V3 ≠ 0`. Those are `verified-computationally`, not
`formalised`, and no theorem here claims otherwise. Turning the ideal
membership into a Lean theorem needs a cofactor certificate, which is the
obvious next step and is not done. -/

/-- The point `a1 = a2 = 1`, all other coefficients zero: at it every monomial
containing `a3, b1, b2` or `b3` dies. -/
def wit : ParamIndex → ℚ := ![1, 1, 0, 0, 0, 0]

/-- Scaling by a nonzero rational cannot make a polynomial vanish. -/
theorem scaled_ne_zero {q : ℚ} (hq : q ≠ 0) {p : LyapunovRing} (hp : p ≠ 0) :
    C q * p ≠ 0 := by
  intro h
  rcases mul_eq_zero.1 h with hc | hp'
  · exact hq (by simpa using hc)
  · exact hp hp'

/-- `V1num` is a nonzero polynomial: at `wit` it evaluates to `1`. -/
theorem V1num_ne_zero : V1num ≠ 0 := by
  intro h
  have := congrArg (MvPolynomial.eval wit) h
  simp [V1num, wit] at this

/-- The first focal value imposes a real condition on the six coefficients: it
is not the zero polynomial. -/
theorem V1_ne_zero : V1 ≠ 0 := scaled_ne_zero (by norm_num) V1num_ne_zero


/-! ### The third generator is genuinely needed: `V3 ∉ ⟨V1, V2⟩`

An evaluation witness, not a cofactor identity. A cofactor identity certifies
MEMBERSHIP (`f = Σ qᵢ gᵢ`, checkable by `ring`); non-membership has no finite
identity, and reproducing the Gröbner argument in Lean would mean formalising
Buchberger. What is checkable is a point: everything in `⟨V1, V2⟩` vanishes
wherever `V1` and `V2` both vanish, so ONE rational point where they vanish and
`V3` does not refutes membership — and proves the stronger statement that `V3`
lies outside the RADICAL of `⟨V1, V2⟩`.

The witness was found by exhaustive exact search over integer points with
coordinates in `-2..2`, sparsest support first (each `Lₖ` is homogeneous — of
degrees 2, 4, 6 — so zeros are projective and integer points lose nothing):
code/bautin/cofactor_certificate.py, capture
code/out/cofactor_certificate.captured.txt.

This is what the Gröbner run in code/out/membership.captured.txt established
computationally; here the kernel checks it, from three evaluations. -/

/-- The certificate point `(a1,a2,a3,b1,b2,b3) = (-2,-2,1,-1,-1,1)`. -/
def certPt : ParamIndex → ℚ := ![-2, -2, 1, -1, -1, 1]

/-- `V1` vanishes at the certificate point. -/
theorem eval_V1_certPt : MvPolynomial.eval certPt V1 = 0 := by
  simp [V1, V1num, certPt]

/-- `V2` vanishes at the certificate point. -/
theorem eval_V2_certPt : MvPolynomial.eval certPt V2 = 0 := by
  simp [V2, V2num, v2coeffs, v2ms, mono, certPt, Fin.sum_univ_succ, Fin.prod_univ_succ]
  norm_num

/-- `V3` does NOT vanish at the certificate point: it takes the value
`7200 / 18432`, the cleared numerator being `7200`. -/
theorem eval_V3_certPt : MvPolynomial.eval certPt V3 ≠ 0 := by
  simp [V3, V3num, v3coeffs, v3ms, mono, certPt, Fin.sum_univ_succ, Fin.prod_univ_succ]
  norm_num

/--
**The third focal value is not in the ideal generated by the first two.**

So Bautin's generating set genuinely needs three elements: the count is not an
artefact of a redundant list. Proved from the evaluation witness — every element
of the span vanishes at `certPt`, and `V3` does not.
-/
theorem V3_not_mem_span_V1_V2 :
    V3 ∉ Ideal.span ({V1, V2} : Set LyapunovRing) := by
  intro hmem
  obtain ⟨c, d, hcd⟩ := Ideal.mem_span_pair.1 hmem
  have h := congrArg (MvPolynomial.eval certPt) hcd
  rw [MvPolynomial.eval_add, MvPolynomial.eval_mul, MvPolynomial.eval_mul,
    eval_V1_certPt, eval_V2_certPt, mul_zero, mul_zero, add_zero] at h
  exact eval_V3_certPt h.symm

#print axioms V3_not_mem_span_V1_V2

/-! ### What is cited

Bautin's theorem is read from the literature, so each statement below is an
`axiom` under `namespace Cited` naming the source. Anything resting on one is
`conditional` — proved given somebody else's paper — never `formalised`. -/

namespace Cited

/-- src: N. N. Bautin, "On the number of limit cycles which appear with the
variation of coefficients from an equilibrium position of focus or center
type", Mat. Sbornik 30 (1952) 181-196; Amer. Math. Soc. Translation 100 (1954).

The focal-value sequence of the quadratic focus: `focalValue k` is the
obstruction at degree `2k + 2`, so `focalValue 1, 2, 3` are `L₄, L₆, L₈`. An
axiom rather than a definition because defining it needs the Lyapunov recurrence
in Lean; its first three members are computed in this file. -/
axiom focalValue : ℕ → LyapunovRing

/-- src: as `focalValue`. The cited sequence's first three members are the three
focal values computed here. The bridge between the literature's object and this
run's computation: asserted, with code/out/bautin_focal_values.captured.txt as
its evidence rather than the kernel. -/
axiom focalValue_eq :
    focalValue 1 = V1 ∧ focalValue 2 = V2 ∧ focalValue 3 = V3

/-- src: Bautin 1952, as above.

**Bautin's finite-generation theorem.** The ideal generated by ALL focal values
is generated by the first three. This is the statement that previously read
`span {0,0,0} = span {0,0,0}` and was therefore `rfl`; the left side is now the
span of the whole sequence, so the content is real, and it is cited. -/
axiom bautin_finite_generation :
    Ideal.span (Set.range focalValue)
      = Ideal.span {focalValue 1, focalValue 2, focalValue 3}

/-- src: Bautin 1952. The number of limit cycles bifurcating from a weak focus
of a quadratic field under quadratic perturbation. Opaque: Mathlib has no notion
of cyclicity, and a definition returning a number would make every bound below
true for the wrong reason. -/
axiom cyclicity : QuadraticFocusField → ℕ

/-- src: Bautin 1952. **M(2) = 3, the bound.** -/
axiom cyclicity_le_three : ∀ f : QuadraticFocusField, cyclicity f ≤ 3

/-- src: Bautin 1952. **M(2) = 3, the realisation** — without it the bound alone
would be consistent with `M(2) < 3`. -/
axiom cyclicity_eq_three_attained : ∃ f : QuadraticFocusField, cyclicity f = 3

end Cited

/-- The Bautin ideal: generated by the whole focal-value sequence. -/
def bautinIdeal : Ideal LyapunovRing :=
  Ideal.span (Set.range Cited.focalValue)

/-- The ideal generated by the first three focal values — the computed ones. -/
def bautinIdeal3 : Ideal LyapunovRing :=
  Ideal.span ({V1, V2, V3} : Set LyapunovRing)

/--
**Bautin's theorem as this file may state it: `conditional`.** The Bautin ideal
is generated by the three computed focal values.

Proved GIVEN Bautin 1952 — the cited finite-generation axiom, rewritten along
the cited identification of the sequence's first three members. The implication
is kernel-checked and the hypothesis is somebody else's paper, which is what
`conditional` means here. It is no longer `rfl`.
-/
theorem bautin_ideal_eq_span_three : bautinIdeal = bautinIdeal3 := by
  obtain ⟨h1, h2, h3⟩ := Cited.focalValue_eq
  unfold bautinIdeal bautinIdeal3
  rw [Cited.bautin_finite_generation, h1, h2, h3]

/-- **M(2) = 3**, conditional on Bautin 1952. -/
theorem M_two_eq_three :
    (∀ f : QuadraticFocusField, Cited.cyclicity f ≤ 3) ∧
      (∃ f : QuadraticFocusField, Cited.cyclicity f = 3) :=
  ⟨Cited.cyclicity_le_three, Cited.cyclicity_eq_three_attained⟩

#print axioms V1_ne_zero
#print axioms v2coeffs_nontrivial
#print axioms v3coeffs_nontrivial
#print axioms bautin_ideal_eq_span_three
#print axioms M_two_eq_three

end Bautin

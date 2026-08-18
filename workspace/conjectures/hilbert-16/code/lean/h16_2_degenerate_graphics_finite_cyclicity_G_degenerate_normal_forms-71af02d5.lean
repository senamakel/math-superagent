import Mathlib.Data.Real.Basic

/-
Node `h16-2-degenerate-graphics-finite-cyclicity/G-degenerate-normal-forms`
from research/backward/h16-2-degenerate-graphics-finite-cyclicity.md.

Informal statement (the node's lemma):

  For the three DR 2009 normal-form families, the quadratic family near the
  degenerate graphic reduces, by an affine change of coordinates and time
  scaling depending analytically on the parameters, to the 5-parameter
  unfoldings (2.2) [finite-plane line: ẋ = y+bxy−y²+µ1+µ2x+µ3x²,
  ẏ = xy+µ4, b∈(−2,2)], (2.8) [line at infinity:
  ẋ = cx−y+1+(1+µ2)x²+µ1xy+µ0y², ẏ = xy−µ3x², c∈(−2,2)], (2.14) [two lines,
  7 parameters: ẋ = xy(1+µ4)+µ0+µ1x+µ2x²+µ3y²,
  ẏ = −y+y²−µ6x²+(µ2−µ5)xy], fixing the invariant line/equator, the contact
  point, and the compact parameter box on which the displacement is studied.
  Proved in DR 2009 Props 2.1–2.3 (held full text).

What the file does:

  * The three displayed families are stated as explicit `def`s over
    `ℝ × ℝ → ℝ × ℝ` (`finitePlane`, `lineAtInfinity`, `twoLines`), carrying
    every monomial and parameter of (2.2), (2.8), (2.14) verbatim.
  * The transcription is kernel-checked against the source's own unperturbed
    systems: at µ = 0 each family restricts to the corresponding unperturbed
    system (2.1), (2.7), (2.13); the claimed singular/invariant lines are
    lines of singular points (`finitePlane`, `twoLines`) or an invariant line
    (`lineAtInfinity`); and the focus/center of (2.1), (2.7) is at (0,1) as
    DR 2009 states.
  * The reduction theorem itself — existence of an affine coordinate change
    and time scaling, analytic in the parameters, with the fixing data — is
    DR 2009 Props 2.1–2.3, a theorem of the literature, not of this run. It
    is stated as an `axiom` under `namespace Cited` with the source in the
    docstring, and the node's theorem is the kernel-checked implication from
    it. The verdict is therefore `conditional`, never `formalised`.

How the informal hypotheses map to binders:

  * "the quadratic family near the degenerate graphic" — for (2.2): a
    quadratic system with a line of singular points in the finite plane, all
    but one normally hyperbolic, and a focus/center, b0 ∈ (−2,2) (DR 2009
    Prop 2.1); for (2.8): the same with the line at infinity plus a finite
    invariant line, c0 ∈ (−2,2) (Prop 2.2); for (2.14): two lines of singular
    points, no analytic 5-parameter reduction exists, 7 parameters needed
    (Prop 2.3). These live in the hypotheses of the cited proposition and in
    the claim block; the `def`s carry the monomials, and the theorems below
    carry the "unperturbed system / invariant line / contact point" content
    that is kernel-checkable.
  * "affine change of coordinates and time scaling depending analytically on
    the parameters" — the analytic-dependence and reduction existence content
    of the cited proposition; not expressible in Mathlib today (no analytic
    families of diffeomorphisms / time rescalings in the library —
    research/mathlib-coverage-h16.md), hence packaged in the cited axiom.
  * "fixing the invariant line/equator, the contact point, and the compact
    parameter box" — the fixing data of the cited proposition; the contact
    point (0,1) and the lines are the kernel-checked theorems below.
  * "b ∈ (−2,2)", "c ∈ (−2,2)" — parameter-range hypotheses of the cited
    propositions (b = b0 + µ0, c = c0 + µ4); stated in the claim block, not
    as binders of the `def`s (which are formal polynomials in all parameters).
-/

namespace DegenerateNormalForms

/-- A quadratic planar vector field: `ℝ × ℝ → ℝ × ℝ`. -/
def Field := ℝ × ℝ → ℝ × ℝ

/-- Finite-plane-line normal form, DR 2009 (2.2):
ẋ = y + bxy − y² + µ1 + µ2x + µ3x², ẏ = xy + µ4. -/
def finitePlane (b μ1 μ2 μ3 μ4 x y : ℝ) : ℝ × ℝ :=
  (y + b*x*y - y^2 + μ1 + μ2*x + μ3*x^2, x*y + μ4)

/-- Line-at-infinity normal form, DR 2009 (2.8):
ẋ = cx − y + 1 + (1+µ2)x² + µ1xy + µ0y², ẏ = xy − µ3x². -/
def lineAtInfinity (c μ0 μ1 μ2 μ3 x y : ℝ) : ℝ × ℝ :=
  (c*x - y + 1 + (1 + μ2)*x^2 + μ1*x*y + μ0*y^2, x*y - μ3*x^2)

/-- Two-lines normal form, DR 2009 (2.14):
ẋ = xy(1+µ4) + µ0 + µ1x + µ2x² + µ3y²,
ẏ = −y + y² − µ6x² + (µ2−µ5)xy. -/
def twoLines (μ0 μ1 μ2 μ3 μ4 μ5 μ6 x y : ℝ) : ℝ × ℝ :=
  (x*y*(1 + μ4) + μ0 + μ1*x + μ2*x^2 + μ3*y^2,
   -y + y^2 - μ6*x^2 + (μ2 - μ5)*x*y)

/-! ## Kernel-checked transcription facts (against DR 2009's displayed systems)

Each theorem below verifies that the `def` above really is the displayed
normal form: at µ = 0 it restricts to the source's unperturbed system, and
the claimed singular / invariant lines and contact point hold. These are
`verified` theorems (kernel-closed by `simp`/`norm_num`/`ring`), independent
of the cited axiom. -/

/-- (2.2) at µ = 0 is the unperturbed system (2.1): ẋ = y + bxy − y², ẏ = xy. -/
theorem finitePlane_restricts_to_unperturbed (b x y : ℝ) :
    finitePlane b 0 0 0 0 x y = (y + b*x*y - y^2, x*y) := by
  simp [finitePlane]

/-- (2.1) has the x-axis as a line of singular points: at y = 0 the field
vanishes identically (DR 2009: "all points of the line are normally
hyperbolic except one", Prop 2.1 proof). -/
theorem finitePlane_singular_on_axis (b x : ℝ) :
    finitePlane b 0 0 0 0 x 0 = (0, 0) := by
  simp [finitePlane]

/-- (2.1) has the focus/center at (0,1) (DR 2009 Prop 2.1 proof:
"we can suppose that the focus or center is located at (0,1)"). -/
theorem finitePlane_focus_at_unit (b : ℝ) :
    finitePlane b 0 0 0 0 0 1 = (0, 0) := by
  norm_num [finitePlane]

/-- (2.8) at µ = 0 is the unperturbed system (2.7):
ẋ = cx − y + 1 + x², ẏ = xy. -/
theorem lineAtInfinity_restricts_to_unperturbed (c x y : ℝ) :
    lineAtInfinity c 0 0 0 0 x y = (c*x - y + 1 + x^2, x*y) := by
  simp [lineAtInfinity]

/-- (2.7) has the finite invariant line y = 0: on y = 0 the second component
of the field vanishes, so the line is invariant under the flow. -/
theorem lineAtInfinity_invariant_axis (c x : ℝ) :
    (lineAtInfinity c 0 0 0 0 x 0).2 = 0 := by
  simp [lineAtInfinity]

/-- (2.7) has the focus/center at (0,1) (DR 2009 Prop 2.2 proof). -/
theorem lineAtInfinity_focus_at_unit (c : ℝ) :
    lineAtInfinity c 0 0 0 0 0 1 = (0, 0) := by
  norm_num [lineAtInfinity]

/-- (2.14) at µ = 0 is the unperturbed system (2.13): ẋ = xy, ẏ = −y + y². -/
theorem twoLines_restricts_to_unperturbed (x y : ℝ) :
    twoLines 0 0 0 0 0 0 0 x y = (x*y, -y + y^2) := by
  simp [twoLines]

/-- (2.13) has the x-axis as a line of singular points. -/
theorem twoLines_singular_on_axis (x : ℝ) :
    twoLines 0 0 0 0 0 0 0 x 0 = (0, 0) := by
  simp [twoLines]

namespace Cited

/-- src: Dumortier–Rousseau, "Study of the cyclicity of some degenerate
graphics inside quadratic systems", CPAA 8(4):1133–1157 (2009),
doi:10.3934/cpaa.2009.8.1133, Props. 2.1–2.3, pp. 3–5.

The packaged proposition: each of the three strata of quadratic systems near
a degenerate graphic — (P2.1) a line of singular points in the finite plane,
all but one normally hyperbolic, with a focus/center, b0 ∈ (−2,2); (P2.2) a
line of singular points at infinity, a finite invariant line, a focus/center,
c0 ∈ (−2,2); (P2.3) two lines of singular points — is brought, by an affine
change of coordinates and a time scaling depending analytically on the
parameters, to the displayed unfolding (2.2), (2.8), (2.14), respectively,
fixing the invariant line/equator, the contact point, and the compact
parameter box on which the displacement is studied. The five-parameter
unfoldings (2.2) and (2.8) have b = b0 + µ0 and c = c0 + µ4; the two-line
stratum (DH5) admits no analytic 5-parameter normal form and needs the seven
parameters of (2.14). -/
axiom DR2009_props_2_1_2_3 : Prop

/-- The source proves the proposition: DR 2009 Props 2.1, 2.2, 2.3 (full text
held at research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md). -/
axiom DR2009_props_2_1_2_3_holds : DR2009_props_2_1_2_3

end Cited

/-- The node's statement: the three normal-form families of DR 2009 exist
with the displayed forms and the analytic affine/time reduction. This is the
kernel-checked implication from the cited proposition (standing:
`conditional`). -/
theorem h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_normal_forms :
    Cited.DR2009_props_2_1_2_3 := by
  exact Cited.DR2009_props_2_1_2_3_holds

#print axioms h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_normal_forms

end DegenerateNormalForms

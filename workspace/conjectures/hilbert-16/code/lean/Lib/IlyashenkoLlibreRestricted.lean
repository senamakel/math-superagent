/-
IlyashenkoLlibreRestricted.lean
-------------------------------
The Ilyashenko–Llibre restricted H16.2 bound, stated in Lean 4 against Mathlib.

WHAT THIS FILE IS. A `Cited` axiom stating the Main Theorem (Theorem 5) of
Ilyashenko & Llibre, "A restricted version of the Hilbert's 16th problem for
quadratic vector fields", Moscow Math. J. 10(2):317–335 (2010), arXiv:0910.3443,
full text held at
research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md.

WHY THE HYPOTHESES ARE ABSTRACT AXIOMS. Mathlib has no theory of quadratic
vector fields normalized as ż = μz + Az² + Bzz̄ + Cz̄², of the four Zoladek-form
center conditions g₁..g₄, of "σ-distant from centers", of "κ-distant from
singular quadratic vector fields", or of "δ-tame limit cycles". Rather than
fabricate those notions as definitions (which would make the hypotheses
trivially true or the count literally zero), each is an OPAQUE AXIOM — exactly
the pattern used for Dukov 2023 (code/lean/
h16_dukov_multiplicity_hyperbolic_polycycles_2023-b4e81de4.lean: `axiom Typical`,
`axiom BornLimitCycle`, `axiom multiplicity`) and Marín 2026
(code/lean/Lib/Marin2026.lean). The kernel checks the implication
(hypotheses → bound); the analytic content is somebody else's paper, so the
verdict is `conditional`, never `formalised`.

THE BOUND ITSELF. For any δ, σ, κ ∈ (0, 0.1), the number of δ-tame limit cycles
of a normalized quadratic field that is σ-distant from centers and κ-distant
from singular quadratic fields is at most

    H(2, δ, σ, κ) = |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).

The divergence of the constant as σ, κ → 0, δ → 0 is exactly where the centres
and the singular/degenerate fields (the DRR graphics territory) live, so this
statement does NOT touch H(2) < ∞.
-/

import Mathlib

noncomputable section

namespace IlyashenkoLlibre

/-- The vector parameter `(δ, σ, κ) ∈ (0, 0.1)³` of the restricted problem. -/
structure Parameters where
  δ : ℝ
  σ : ℝ
  κ : ℝ
  δ_pos : 0 < δ
  σ_pos : 0 < σ
  κ_pos : 0 < κ
  δ_lt : δ < (0.1 : ℝ)
  σ_lt : σ < (0.1 : ℝ)
  κ_lt : κ < (0.1 : ℝ)

/-- A normalized quadratic vector field with a focus at zero, in the
Ilyashenko–Llibre sense (one of the three glued cells Λ ≅ ℝ⁺×𝔻²×𝔻²). Opaque:
Mathlib has no normal-form theory for complex quadratic fields. -/
structure NormalizedQuadraticField where
  -- the field itself, deliberately abstract
  carrier : Type

/-- The field is σ-distant from centers: Σ_{j=1}^{4} |g_j(λ)| ≥ σ with the
four Zoladek-form center conditions g₁=λ₁, g₂=Im(AB), g₃=Im[(2A+B̄)(A−2B̄)B̄C],
g₄=Im[(2A+B̄)(|B|²−|C|²)B̄²C]. Opaque axiom: making it a definition (e.g. True)
would make the wrapper theorem trivially true for the wrong reason. -/
axiom SigmaDistantFromCenters : NormalizedQuadraticField → ℝ → Prop

/-- The field is κ-distant from singular quadratic vector fields (fields with
a line of singular points): ‖r⁻²u‖₂ > κ in the decomposition v = v_s + u of
(8). Opaque axiom, same reason. -/
axiom KappaDistantFromSingular : NormalizedQuadraticField → ℝ → Prop

/-- The number of δ-tame limit cycles of the field: limit cycles lying in
B(λ,δ) = {|z| ≤ δ⁻¹} minus the open δ-neighborhoods of all singular points
(real and complex) except 0. Opaque axiom: a literal `0` would make every
bound true for the wrong reason (cf. the Dukov `multiplicity` axiom). -/
axiom DeltaTameLimitCycleCount : NormalizedQuadraticField → ℝ → ℕ

/-- The restricted Hilbert number of the paper: |log σ|·exp(exp(10²⁵ δ^{−31}
κ^{−2})). Totalized real arithmetic (inv of 0 is 0 in Lean), so the expression
is well-typed even off the domain; the bound is only claimed under the
parameter hypotheses. -/
def HRestricted (δ σ κ : ℝ) : ℝ :=
  |Real.log σ| * Real.exp (Real.exp (10^25 * δ^(-31) * κ^(-2)))

namespace Cited

/-- src: Ilyashenko & Llibre, Moscow Math. J. 10(2):317–335 (2010),
arXiv:0910.3443, Theorem 5 (Main Theorem); full text at
research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md
lines 113–122.

For any δ, σ, κ ∈ (0, 0.1), the number of δ-tame limit cycles of a normalized
quadratic vector field that is σ-distant from centers and κ-distant from
singular quadratic vector fields is no greater than
|log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).
-/
axiom main_theorem (p : Parameters) (λ : NormalizedQuadraticField) :
    SigmaDistantFromCenters λ p.σ →
    KappaDistantFromSingular λ p.κ →
    (DeltaTameLimitCycleCount λ p.δ : ℝ) ≤ HRestricted p.δ p.σ p.κ

end Cited

/--
The kernel-checked wrapper: the Main Theorem stated as a single implication.
Conditional on the cited axiom — the kernel checks the reasoning, not the paper.
-/
theorem restricted_h16_quadratic_bound (p : Parameters) (λ : NormalizedQuadraticField)
    (hσ : SigmaDistantFromCenters λ p.σ)
    (hκ : KappaDistantFromSingular λ p.κ) :
    (DeltaTameLimitCycleCount λ p.δ : ℝ) ≤ HRestricted p.δ p.σ p.κ := by
  exact Cited.main_theorem p λ hσ hκ

#print axioms restricted_h16_quadratic_bound
#print axioms Cited.main_theorem

end IlyashenkoLlibre

end

#print axioms IlyashenkoLlibre.restricted_h16_quadratic_bound
#print axioms IlyashenkoLlibre.Cited.main_theorem

# Huzak–Kristiansen 2025: degenerate turning-point entry-exit — summary

[[huzak-kristiansen-degenerate-turning-point-2025.ar5iv.full]]

**Source:** R. Huzak, K. U. Kristiansen, "On entry-exit formulas for degenerate
turning point problems in planar slow-fast systems", arXiv:2510.02770 (2025).
Full text: `research/sources/huzak-kristiansen-degenerate-turning-point-2025.ar5iv.full.md`
(ar5iv); abstract page: `...-2025.arxiv.full.md`. URL: https://arxiv.org/abs/2510.02770

## What the source establishes

**Setting.** Planar slow-fast system (2.5) with invariant line {y=0}, turning
point at x=0, slow flow x′ = −x^{2n}(1+o(1)) (saddle-node of even order 2n at
the turning point), and P_λ(x₂)=λ₀+λ₁x₂−x₂². The degeneracy is exactly the
entry-exit problem arising in the DRR graphics (I¹₂) and (I¹₄) through a
nilpotent saddle-node at infinity.

**Theorem 2.4 (n=1).** If the entry-exit relation (2.12) holds — the Cauchy
principal value of the slow-divergence integral along the singular line plus the
divergence integral on the second cylinder equals 0 — then the Dulac map
Δ(·,ε): I_in → ℝ is well-defined for all small ε>0 and has the form
Δ(x_in, ε) = Δ₀(x_in) + φ(x_in, ε, ε log ε⁻¹), where φ is C^k-smooth and
φ(·,0,0)=0. Equivalently, the Dulac map is **smooth in (ε, ε log ε⁻¹)** with a
closed-form leading term Δ₀. The entry-exit formula (2.13) is
∫_{x_out^b}^{x_in^b} (ζ₂+1)/(sζ₂) ds + log(−x_out^b/x_in^b) = λ₁π/√(−4λ₀−λ₁²).

**Theorem 2.7 (n≥2).** The entry-exit relation is **not well-defined** for all
small ε when ∫_{−∞}^{∞} v/P_λ(v) dv ≠ 0: the in/out intersection heights
z_in, z_out with {x=0} differ at order ε^{2n−1}, with explicit C^k-smooth
remainders φ_in/out(x, ε, ε log ε⁻¹). In the zero-integral (canard-like) case,
Corollary 2.9 gives an implicit-function-embedding: there is a local parameter
reparametrization λ̄(x_in,x_out,ε,λ̂) with Δ(x_in,ε;λ̄)=x_out identically — so
the entry-exit relation is realizable by tuning parameters.

**Theorem 6.1 (application to DRR).** For the 5-parameter quadratic family (6.2)
— A near 1, C near C₀>0, μ_i near 0, with invariant parabola y=½x²−C₀/2
(C₀=1: graphic (I¹₄) with a finite saddle-node on the parabola; C₀>1: (I¹₂),
parabola regular) — the Dulac map Δ(x_in,ε) = Δ₀(x_in) + φ(x_in,ε,ε log ε⁻¹)
with φ C^k, φ(·,0,0)=0, and Δ₀ in **closed form** (Eq 6.8):
x_out = −√( 2δ + e^{2K}(x_in²−2δ) / (β(e^K+1)√(x_in²−2δ) − 1)² ),
K = λ₁π/√(−4λ₀−λ₁²), valid for x_in ∈ (0, 1/(β(e^K+1))). Numerical check
(Matlab ODE15s, tol 10⁻¹², ε=0.01/0.005/0.001, parameters (6.9)) agrees with
the theoretical curve; the (x,z)-transformation is numerically essential (y
becomes exponentially small).

## What it implies here

- An **explicit Dulac-map entry-exit formula** for two DRR graphics (I¹₂),(I¹₄)
  through nilpotent saddle-nodes at infinity — displacement-map control of the
  kind the run's attacks need. But (I¹₂),(I¹₄) are **closed rows** in the DRR
  ledger; the open rows (I¹₆b,H³₁₃,DI₂b,H³₁₄) pass through **triple nilpotent
  points** of saddle/elliptic/degenerate type, which are not the n=1 turning
  point treated here. The paper's own §6 says further cyclicity details are
  postponed to [10]. So this is a **method-transfer template**, not a closure.
- Theorem 2.7's negative result (n≥2: entry-exit not well-defined without extra
  control parameters) is a **caution for the I¹₆b four-second-type-Dulac
  displacement**: the missing second-type endpoint germs are of exactly this
  semi-hyperbolic/nilpotent character, and smoothness in (ε, ε log ε⁻¹) is the
  best available regularity. This corroborates the run's precise ECT gap
  (parameter-uniform analytic remainder in (ε, ε log ε⁻¹) needed, not just
  state-space flatness).

## Evidence class
`asserted-by-source` — theorems read in the held full text; the numerical
verification is reported in the source (Matlab), not reproduced here. Claim
`huzak-kristiansen-2025-degenerate-entry-exit-dulac` (asserted, holds-here yes).
Falsifier: a counterexample to Theorem 6.1's entry-exit formula at n=1, or a
corrigendum retracting Theorem 2.7/6.1.

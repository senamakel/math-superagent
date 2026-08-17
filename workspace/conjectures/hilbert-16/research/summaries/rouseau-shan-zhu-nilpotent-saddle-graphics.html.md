# Rousseau–Shan–Zhu 2015 (arXiv:1502.00689), nilpotent saddle graphics

Source: `research/sources/rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md` [[rouseau-shan-zhu-nilpotent-saddle-graphics.html.full]] — arXiv HTML full text. Record page: [[rouseau-shan-zhu-nilpotent-saddle-graphics.full]].

## What the source establishes

**Main theorem (abstract + Theorem 3.1)**: finite cyclicity of the two graphics
(I¹₁₂) and (I¹₁₃), through a triple nilpotent point of **saddle type** not
surrounding a center, inside quadratic vector fields. These complete the
nilpotent-saddle non-center rows and — in the paper's own words — "**bring the
number of graphics of the program for which finite cyclicity is proved to 88**".

**The a₀ = −1/2 case (Theorem 3.1).** Prior work ([7], Zhu–Rousseau) proved a
graphic through a codimension-3 nilpotent saddle has finite cyclicity whenever
the first return map has derivative ≠ 1 — excluding a₀ = −1/2 (hyperbolicity
ratio τ = 1 at the saddle, where divergence ≡ μ̄₃). RSZ 2015 closes exactly this
resonant case:
- At a₀ = −1/2, μ̄₃ = 0, family (2.6) is **Hamiltonian and symmetric**:
  H(x̄,ȳ) = ½ȳ² − ½x̄²ȳ + μ̄₂ȳ − μ̄₁x̄; the first return T₀ is shown to be T₀ ≡ id
  along the fixed connection, turning the resonant case into an integrable one.
- The displacement map is L_ν = R₃,ν ∘ D₃,ν ∘ T_ν ∘ D₄,ν⁻¹ − D_ν⁻¹ ∘ R₄,ν⁻¹ with
  Dulac maps D_i (σ₀ = 4), and the intermediate graphic has cyclicity 1 once
  T′_ν(0) − S′_ν(0)·ν^{σ̄₄−σ̄₃} is bounded away from 0.
- Also derives the genericity condition for (I¹₁₂) (divergence integral over the
  invariant parabola ≠ 0), giving (I⁹b²) with codimension-3, and treats a
  nilpotent saddle + saddle-node with central transition for (I¹₁₃).

**Definition 2.1 (finite cyclicity of a graphic)** is the DRR notion used
throughout — a graphic Γ at A₀ has finite cyclicity in S²×K if a neighborhood
U×V of Γ×{A₀} contains at most N limit cycles for some fixed N.

## What it implies here

Co-anchor of `h16-drr-121-graphics` (the compactness/121 reduction) and the
source of the **88-by-2015 count** (claim `h16-drr-closed-rows-2015`). The
Hamiltonian-completion trick at the resonant value a₀ = −1/2 is the concrete
mechanism by which finite cyclicity is obtained exactly where the generic
τ ≠ 1 machinery breaks — a model for how the run's own attack on an open
nilpotent graphic can go: reduce to the resonant value, find a first integral,
then count zeros of a one-dimensional displacement map.

Evidence class: sourced-held — read from the held full HTML text. Hypotheses:
n = 2 quadratic; nilpotent saddle of multiplicity 3; a₀ = −1/2 resonant case;
fixed connection for the second family. Falsifier: a quadratic system near
(I¹₁₂) or (I¹₁₃) with a limit cycle count contradicting the theorem.
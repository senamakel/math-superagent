# Gavrilov 2011/2013: finite cyclicity of two-saddle cycles — full-text summary

<!-- source: https://arxiv.org/abs/1106.0857 ; full HTML: research/sources/primary-gavrilov-two-saddle-cycles-2011-arxiv.html.full.md ; landing: research/sources/primary-gavrilov-two-saddle-cycles-2011.full.md -->

**Authoritative full text:** `research/sources/primary-gavrilov-two-saddle-cycles-2011-arxiv.html.full.md`
(arXiv:1106.0857v3, 12 Dec 2012; the companion landing page
`primary-gavrilov-two-saddle-cycles-2011.full.md` is abstract/metadata only).

## What the source establishes

**Theorem 4 (main).** Every heteroclinic two-saddle cycle (k=2 saddle graphic,
two nondegenerate saddles joined by two separatrix connections) occurring in an
analytic finite-parameter family of analytic planar vector fields
X_λ = P(x,y,λ)∂x + Q(x,y,λ)∂y, λ ∈ (ℝ^N, 0), has **finite cyclicity**: the number
of limit cycles of X_λ tending to the cycle as λ→0 is uniformly bounded in λ.
The proof does **not** use Dulac-map asymptotic expansions; it counts zeros of the
displacement ψ_λ(z) = 𝒟_λ¹(z) − 𝒟_λ²(z) (difference of two Dulac maps) in a complex
domain via the argument principle ("Petrov trick").

**Method (why it matters here).** The paper explicitly rejects the inference
"formal asymptotic Dulac expansion ⇒ zero count" (the historical Dulac error shape):
complex-analytic continuation of the Dulac maps (Theorem 1) gives the zero locus of
Im 𝒟_λ as smooth semianalytic curves (Lemma 2); zeros of Im ψ_λ on the domain
boundary reduce to fixed points of separatrix holonomy maps h_i^λ, whose zero counts
are uniformly bounded by Gabrielov's theorem (semianalyticity). This is the same
holonomy/Petrov technique the run's displacement-function attacks need for
polycycles with more than one saddle — a proof route that does not require a
complete asymptotic expansion.

**Extent and limits.** Theorem 4 is existential (no explicit N). It covers the
hyperbolic two-saddle case only: both saddles nondegenerate (hyperbolic ratios
α₁,α₂ > 0, α₁α₂ ≥ 1 after orientation). It does not cover: one-saddle loops (Roussarie,
reproved in §3), k-saddle cycles with k>2 (announced for any k by Mourtada, ref [18]
= arXiv:0912.1560, held), nilpotent/degenerate graphics (the DRR open rows
I¹₆b, H³₁₃, DI₂b, H³₁₄ pass through **triple nilpotent** points at infinity — not
two hyperbolic saddles). The general analytic-family result is **not** a
coefficient-uniform bound over all polynomial fields, so it does not settle H16.2.

## What it implies here

- Confirms the displacement-function viewpoint: cyclicity = zeros of a difference
  of Dulac maps; the complex/argument-principle route bypasses asymptotic
  expansions. Relevant to the run's slow-divergence/ECT gap (the I¹₆b four-Dulac
  displacement) as a **template for counting zeros of composed Dulac maps without
  full transseries**, but the missing I¹₆b maps are second-type (semihyperbolic/
  nilpotent), so the Gavrilov technique does not directly apply.
- Corroborates, independently of Mourtada's QRH route, that analyticity of the
  *actual* return map (not its formal expansion) is the load-bearing hypothesis —
  the smooth-test requirement in problem.md.
- Pairs with the held Gavrilov–Iliev 2013 (arXiv:1306.2340, "Perturbations of
  quadratic Hamiltonian two-saddle cycles"): the quadratic-Hamiltonian two-loop has
  cyclicity ≤ 3 (exact bound open, conjectured 2). That is a settled
  quadratic-restricted row, again hyperbolic only.

## Evidence class
`asserted-by-source` — theorem read in the held full text; not independently
formalised or computed. Falsifier: a two-saddle cycle in an analytic family with
unbounded cyclicity, or an invalid argument-principle/domain step.

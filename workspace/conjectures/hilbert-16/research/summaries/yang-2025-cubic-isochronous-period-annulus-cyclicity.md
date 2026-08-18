# Yang 2025 — cyclicity of the period annulus of cubic isochronous Hamiltonian systems

<!-- source: https://arxiv.org/pdf/2512.19046 | converted from PDF/HTML. Full text:
research/sources/yang-2025-cubic-isochronous-period-annulus-html.full.md -->

## What this is

Jihua Yang, "The cyclicity of period annulus of cubic isochronous Hamiltonian
systems", arXiv:2512.19046 [math.DS], submitted 22 Dec 2025. Primary source;
full text held (HTML).

## What it establishes

**Theorem 1.1 (Cima–Mañosas–Villadelprat 1999, restated):** a cubic Hamiltonian
system has an isochronous center at the origin iff, after a linear change, its
Hamiltonian is

  H₁(x,y) = k₁²x² + (k₂y + k₃x + k₄x²)²,  k₁k₂ ≠ 0.

(The 1999 classification is cited verbatim; this paper builds on it.)

**Theorem 1.2 (main result):** for the normal form (with kᵢ ≠ 0, after the
change t₁=2k₂k₃t, x₁=k₄x/k₃, y₁=k₂k₄y/(k₁²+k₃²), λ=k₃²/(k₁²+k₃²) ∈ (0,1))

  ẋ = −λ⁻¹y − x − x² + ε Σ_{i+j≤n} aᵢⱼ xⁱyʲ
  ẏ = x + y + 2xy + 3λx² + 2λx³ + ε Σ_{i+j≤n} bᵢⱼ xⁱyʲ

with Hamiltonian

  H(x,y) = ½x² + λx³ + ½λx⁴ + ½λ⁻¹y² + xy + x²y

and period annulus Γ_h = {H = h}, h ∈ (0,∞) (an **isochronous center** at the
origin),

  the upper bound for the number of limit cycles bifurcating from the period
  annulus is **n−1 for n ≥ 2, counted with multiplicities**, and **this bound
  is sharp**.

The system is deliberately **asymmetric** (no symmetry about either axis or the
origin — Fig. 1), so the Abelian integral has more generators than the
two/three-generator classical cases and its algebraic structure is the main
work. The classification of the Iᵢⱼ(h) terms into formula-iterable (i≥2, j≥1)
and non-iterable (i=0,1, j≥1) and the linear-independence induction are the
technical core.

## Why this is in the library

This is a **sharp, named-family Abelian-integral zero count** — exactly the
result type of the run's adopted approach
(`abelian-picard-fuchs-argument-principle-sharp-count`, GOAL result-type 3) and
a **fresh validation exemplar** for that approach's first step (validate the
Machinery against a published sharp count before trusting anything new). It also
confirms from a 2025 primary that Li–Liu–Yang's H(3)≥13 (m=n=3 weak-H16 with 13
limit cycles) remains the current cubic lower bound, with the m=n=2 case
completely resolved (cited). It is a peer-unreviewed preprint (arXiv), so it is
evidence-class asserted-by-source, but the result it states is narrow and fully
explicit, making its algebraic core (the Abelian integral's explicit form,
generator count, Wronskian/independence induction) machine-checkable in
principle — a candidate for the Chebyshev/PF validation pipeline.

## Key source anchors

- Cima, Mañosas, Villadelprat, J. Diff. Eq. 157 (1999) 373–413 — isochronous
  cubic Hamiltonian classification (Theorem 1.1).
- Li, Liu, Yang, JDE 246 (2009) 3609–3619 — H(3)≥13 (the 13-cycle cubic lower
  bound this paper re-confirms, still paywalled as a primary).
- Roussarie — closed period annulus bound by homoclinic loop (cited as [38]).

Full text: `research/sources/yang-2025-cubic-isochronous-period-annulus-html.full.md`
(arXiv HTML) and `...-period-annulus-cyclicity.full.md` (abstract page).
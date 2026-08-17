# Lu, "Local Uniform Finite Cyclicity of the H₁₄³ Semihyperbolic Hemicycle" — summary

Source: H. Lu, arXiv:2607.13785v2 (submitted 15 Jul 2026, revised 17 Jul 2026),
80 pp., math.DS, MSC 34C07/34C23/37G15.
Full text: `research/sources/lu-h14-3-hemicycle-html.full.md` (314 KB).
DOI: 10.48550/arXiv.2607.13785.

## What the paper claims

**Theorem 1 (local uniform finite cyclicity).** There exist a fixed two-sided
annular neighborhood U of the compactified graphic Γ_{H₁₄³}, a neighborhood
Λ ⊂ ℝ⁵ of the origin, and a finite constant B_{H₁₄³} such that the number of
isolated limit cycles of the five-parameter unfolding (1.3) contained in U is
≤ B_{H₁₄³} for every λ ∈ Λ. The bound is existential, not explicit.

The object: the labelled **H₁₄³ semihyperbolic hemicycle** of a quadratic vector
field — a noncompact period annulus (first integral H = x²/2 + y − log(1+y),
levels h > 0 are ovals around the origin) whose outer compactified limit is the
graphic Γ = L₋ ∪ {p₊} ∪ E₊ ∪ {q} ∪ E₋ ∪ {p₋}: finite invariant line y = −1,
two horizontal points at infinity, oriented upper equatorial arcs, and the
positive vertical point at infinity.

## Why this matters for THIS library

**It claims finite cyclicity for exactly the graphic the library records as
left open by Roussarie–Rousseau 2015.**

Roussarie–Rousseau (arXiv:1506.07104, Moscow Math. J. 76(2) 2015), which we
hold in full, states at its line 63: *"We have a partial result for every
graphic, but one (namely (H³₁₄)), through a triple point at infinity"*, and
Theorem 3.1 there displays the five-parameter unfolding

    ẋ = −y + Bx² + μ₂y² + (μ₄ + Bμ₅)x
    ẏ = x + xy + μ₃y² + (1 − 2B)μ₅y

**which is term-for-term Lu's unfolding (1.3).** Lu says (his §1.2): "the value
B = 0 is precisely the labelled H₁₄³ case [of RR Theorem 3.1]" and "Roussarie–
Rousseau explicitly leave the B = 0 H₁₄³ case outside their finite-cyclicity
result." The RR classification: B₀ > 1 nilpotent saddle; B₀ = 3/2 special
saddle; B₀ < 1 elliptic; B₀ = 1/2 elliptic of larger codimension (type 1);
B₀ = 1 transition. B = 0 is the H₁₄³ case.

## Evidence class: ASSERTED-BY-SOURCE, unrefereed

- Single-author arXiv preprint. **Not peer-reviewed.** No journal acceptance
  found. Dated 2026 (the run's clock).
- 80 pages; Parts II–III are computer-assisted with an ancillary
  reproducibility bundle (`h14_3_reproducibility/`: MANIFEST.json, Bautin
  recurrence verifier, center-basis verifier, chart checks, environment lock).
  The physical exhaustiveness claims are argued mathematically; the finite
  derivative/case enumerations are computer-assisted.
- No community acceptance known; no independent verification located.

## What it does and does not settle

- It proves LOCAL UNIFORM finite cyclicity in **one fixed collar** over the
  FULL five-parameter quotient unfolding. This is the DRR notion of "finite
  cyclicity of a graphic inside quadratic systems" specialised to the local
  form; the DRR program additionally needs the other limit periodic sets of the
  compactified family, but the graphic itself is the unbounded polycycle the
  paper treats.
- It does NOT close all of the DRR program, only (if correct) this one graphic.
- It must be checked whether the paper's "local uniform finite cyclicity in a
  collar" matches DRR's definition of finite cyclicity of the graphic (the DRR
  1994 primary list is still not in the library — paywalled).

## Falsifiers

1. An error found in the stopped-first-hit atlas construction or in any of the
   zero theorems (Parts II–III), or a failure of the finite-specialization
   induction.
2. A published counterexample to Theorem 1.
3. Community/peer rejection (e.g., referee finding that a regime is not covered
   by the claimed theorems).

## Status for the claims ledger

Updates the request `dumortier-roussarie-rousseau-9c4f` partially: it names one
graphic (H³₁₄) and a candidate closure. The consolidated graphic-by-graphic
ledger remains **not in the library** — that gap stays open.
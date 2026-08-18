# Library additions — 2026-08-18 librarian cycle

Memory service (Cognee) is down this cycle; this note is the durable workspace
record. Established claims go to the claims ledger; this file records what was
added and why it matters.

## Two new primary sources added

### 1. Artés–Mota–Rezende, infinite elliptic-saddle / nilpotent saddle class

- **arXiv:2312.01222**, "Phase portraits for quadratic systems possessing an
  infinite elliptic-saddle or an infinite nilpotent saddle", Joan C. Artés,
  Marcos C. Mota, Alex C. Rezende; published as IJBC 34(11):2430023, 2024,
  DOI 10.1142/S0218127424300234 (publisher 403s; arXiv full text held).
- Files:
  - `research/sources/artes-mota-rezende-infinite-nilpotent-saddles-ar5iv.full.md`
    (ar5iv full text, 3465 lines)
  - `research/sources/artes-mota-rezende-infinite-nilpotent-saddles-arxiv.full.md`
    (abstract page)
- What it establishes (asserted-by-source, held full text):
  - Complete topological classification of the class **Q̂ES**: quadratic systems
    with exactly one elemental infinite singular point and one triple infinite
    singular point of infinite-nilpotent elliptic-saddle or nilpotent-saddle
    type. Three families by finite singularities: Q̂ES(A) 3 real finite points
    (91 topologically distinct phase portraits), Q̂ES(B) 1 real + 2 complex
    (8 portraits), Q̂ES(C) one real triple finite point (14 portraits).
  - **Proposition 2 (normal form)**: every nondegenerate quadratic system with
    three real finite singular points plus an infinite nilpotent elliptic-saddle
    or nilpotent saddle is affinely/time-rescaled to
    `x' = cx + y − cx²`, `y' = ex + (−1+(e+f)/c)y − ex² + 2xy`,
    with `c ∈ ℝ∖{0}`, `f ∈ ℝ⁺∪{0}`, `e ∈ ℝ`.
  - Derivation from the invariant-theoretic canonical form 10 of the
    Artés–Llibre–Schlomiuk–Vulpe book, via invariants μ₀=0, μ₁≠0, η=0, M̃≠0, κ=0.
- Why it matters: this is the classification school's treatment of the exact
  singularity type (infinite nilpotent points) that the open DRR graphics
  (I¹₆b, H³₁₃, DI₂b) pass through. The normal form is a concrete algebraic
  object the run's Lean/linear-attack layer can use. Genuinely absent before
  this cycle — verified by grep.

### 2. Huzak–Kristiansen, degenerate turning-point entry-exit (2025)

- **arXiv:2510.02770**, "On entry-exit formulas for degenerate turning point
  problems in planar slow-fast systems", Renato Huzak, Kristian Uldall
  Kristiansen (2025).
- Files:
  - `research/sources/huzak-kristiansen-degenerate-turning-point-2025.ar5iv.full.md`
    (ar5iv full text, 1207 lines)
  - `research/sources/huzak-kristiansen-degenerate-turning-point-2025.arxiv.full.md`
    (abstract page)
- What it establishes (asserted-by-source, held full text):
  - For a planar slow-fast system with an invariant line and a turning point
    where the slow flow has a saddle-node of even order 2n: for **n=1** a
    well-defined entry-exit relation as ε→0 exists and the associated Dulac map
    is smooth in (ε, ε log ε⁻¹); for **n≥2** the entry-exit relation needs
    additional control parameters.
  - **Section 6, Theorem 6.1**: for the DRR graphics (I¹₂) and (I¹₄) through a
    nilpotent saddle-node at infinity, the 5-parameter family (6.2) with
    invariant parabola y = ½x² − C₀/2, the Dulac map takes the explicit form
    `Δ(x_in, ε) = Δ₀(x_in) + φ(x_in, ε, ε log ε⁻¹)` with φ C^k-smooth,
    φ(·,0,0)=0, and Δ₀ given in closed form (Eq 6.8):
    `x_out = −√(2δ + e^{2K}(x_in²−2δ) / (β(e^K+1)√(x_in²−2δ) − 1)²)`,
    K = λ₁π/√(−4λ₀−λ₁²).
  - Numerical verification (Matlab ODE15s, tolerance 10⁻¹², ε=0.01/0.005/0.001)
    agrees with the theoretical curve; notes the (x,z)-transformation is
    numerically essential (y becomes exponentially small).
- Why it matters: gives an *explicit* entry-exit/Dulac map for two DRR graphics
  — precisely the displacement-map control the run's attacks need. This is
  adjacent to the open graphics but for (I¹₂),(I¹₄), which are *closed* rows in
  the DRR ledger; the methods transfer to the open center-type infinite
  nilpotent rows. Genuinely absent before this cycle (only the 2005
  De Maesschalck–Dumortier entry-exit paper was cited).

## DRR open-status re-confirmation (deep research, 2023-2026 window)

No peer-reviewed closure of (H³₁₄), (I¹₆b), (H³₁₃), (DI₂b), or any of the 11
degenerate graphics (DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4,
DH5) since 2015. The standing picture holds: ≥89/121 closed (88 RSZ + I¹₁₄ RR),
(I¹₆b),(H³₁₃),(DI₂b) boundary-sets-only, (H³₁₄) claimed by Lu arXiv:2607.13785
(unrefereed). Lu's H³₁₄ is not independently verified; the run's
`lu-h14-3-verification` thread is the live attack on that.

## Roussarie 1998 book — status unchanged

The canonical bifurcation monograph remains unobtainable as full text. The
Göttingen library scan (gbv.de) crashed the PDF extractor; the Springer DOI
10.1007/978-3-0348-8798-4 (the *correct* DOI; the previously-held 0718-0 is
dead) resolves only to a 499-byte landing shell. Held record:
`research/summaries/roussarie-1998-bifurcations-book-springer-correct-doi.md`.
The book's TOC/structure is well represented in the library via citations.

## H(3) ≥ 13 attribution pinned

The library's `h16-lower-bounds` claim marked H(3) ≥ 13 as "claimed". Held
primary-adjacent source Torregrosa 2024 (São Paulo J. Math. Sci., full text
held) states precisely: the highest cubic global lower bound is due to
Li–Liu–Yang 2009 (JDE 246:3609–3619), thirteen cycles bifurcating from level
curves of a cubic Hamiltonian vector field via the
Poincaré–Pontryagin–Melnikov method, configuration (5:1|1:5) plus one
surrounding cycle. The JDE paper itself is paywalled (not held); the
attribution is now source-pinned at secondary level, primary still missing.

## Frontier additions

Both downloads added their citation lists to `derived/FRONTIER.md`
(44 + 39 + 8 + 8 = 99 new leads). Notable new leads from the Artés paper:
the Artés–Llibre–Schlomiuk–Vulpe book "Quadratic Systems with an Invariant
Straight Line" (canonical-form source), the codimension-two classification
papers, and the Kotova–Stanzo zoo. From Huzak–Kristiansen: De Maesschalck–
Schecter (JDE 2016) degenerate entry-exit, and the DRR-linked normal forms.

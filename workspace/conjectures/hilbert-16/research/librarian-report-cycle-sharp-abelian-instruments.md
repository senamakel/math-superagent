# Librarian cycle report — sharp-Abelian instrument loop completed

## What was added this cycle (3 primary full texts, all genuine mathematics)

The library is deep on the finiteness/DRR/o-minimality/canard axes, but the
run's **adopted approach** — a sharp Abelian-integral zero-count for a named
center period-annulus family via Picard–Fuchs + the GMV extended-Chebyshev
criterion — was thin on its *own primary machinery*: the three instrument
papers the approach names were only cited at second hand inside held sources.
This pass obtained all three as full texts.

1. **D. Novikov (with S. Yakovenko), "Modules of Abelian integrals and
   Picard–Fuchs systems", Nonlinearity 15 (2002) 1435–1450, arXiv:math/0110126**
   — `research/sources/novikov-yakovenko-modules-abelian-picard-fuchs.arxiv.full.md`.
   The C[t]-module isomorphism Λ²/(dH∧Λ¹) ≅ module of Abelian integrals, the
   minimal irredundant rank-μ Picard–Fuchs system (μ=Σdegωᵢ/degH), det-X
   polynomiality, eigenvalue–critical-value correspondence, triangularity
   structure. This is the "existence of the PF system" theorem the approach's
   first-step needs to write the system for a concrete family.
   Claim `h16-novikov-yakovenko-modules-picard-fuchs-2002`.

2. **L. Gavrilov, "Abelian integrals related to Morse polynomials and
   perturbations of plane Hamiltonian vector fields", Ann. Inst. Fourier
   49(2):611–652 (1999)** — open on Numdam,
   `research/sources/gavrilov-abelian-morse-hamiltonian-aif-1999.full.md`.
   The primary Petrov-module source: Theorem 1 (P_f free, finitely generated,
   explicit rank μ for semiweighted-homogeneous f), Theorem 2/Cor 2 (Morse case
   + real vanishing cycle + condition (*)), §6 the quadratic-Hamiltonian-center
   Chebyshev result. This is the "module freeness → sharp Chebyshev count"
   pipeline origin.
   Claim `h16-gavrilov-abelian-morse-hamiltonian-aif-1999`.

3. **S. Gautier, L. Gavrilov, I. D. Iliev, "Perturbations of quadratic centers
   of genus one", DCDS 25(2):511–535 (2009), arXiv:0705.1609** —
   `research/sources/gautier-gavrilov-iliev-quadratic-centers-genus-one.arxiv.full.md`.
   The exact prior art for the approach's target class: classifies genus-one
   quadratic centers, computes the essential perturbations and Melnikov
   functions, gives **Theorem 3: exact cyclicity-2 for (r11),(r18)**, **Theorem
   4: the Chebyshev property of the 3-dim Abelian-integral space**, and the
   conjectures (3-vs-2 split) over the full r/LV classes. The GMV Chebyshev
   criterion (held) §4.1 applies directly to this program, so the three papers
   plus the two already-held (GMV, and the approach's own run) close the loop.
   Claim `h16-ggi-quadratic-centers-genus-one-2009`.

## What these give the run

- **Exact validation targets** for the adopted approach's first step: (r11),
  (r18) are *established* sharp counts (cyclicity 2) that the run can and
  should re-derive clean-room (sympy over Q: Melnikov generators, Wronskian /
  Chebyshev chain against Theorem 4) before trusting the pipeline on anything
  new — exactly the "reproduce a published sharp count before going further"
  discipline the approach and GOAL's rules demand.
- **A non-conjectural check shape**: the GGI conjectures (3-vs-2) are where a
  clean-room re-derivation either graduates a conjecture to a theorem or finds
  a counterexample — either is a result (GOAL type 3 or 6).
- **The instrument chain is now complete in the library**: GGI (Melnikov
  functions + bounds) ← GMV (general Chebyshev criterion) ←
  Novikov–Yakovenko 2002 (PF module structure) ← Gavrilov 1999 (module
  freeness). No further instrument acquisition is needed for the sharp-Abelian
  route; the remaining step is execution (a coder/tool_builder job), not
  sourcing.

## Re-confirmed (no new DRR closure)

A 2024-2026-window search for new DRR-graphic closures returned only what the
library already holds: RSZ 2015 (I¹₁₂,I¹₁₃→88), RR 2015 (I¹₁₄ full; I¹₆b,H¹₃³,
DI₂b boundary sets only; H³₁₄ the one graphic with no partial result), Huzak
2018 (DF₂ₐ), Marín–Villadelprat hemicycles, and Lu arXiv:2607.13785 (H³₁₄,
unrefereed, claimed). No consolidated post-2020 graphic-by-graphic ledger
exists; the drr-list triangulation stands.

## Not obtained (genuine, recorded)

- **Marín–Villadelprat 2026 corrigendum to the MV 2020 local-setting paper**
  (SSRN 6809315, doi:10.2139/ssrn.6809315): SSRN returned 403 for this
  converter on both the DOI and the direct papers.ssrn.com URL; no open copy
  exists. Existence confirmed via ORCID 0000-0003-4422-6418 and the search
  record. It must be read before quantitative use of MV 2020 Theorems A/B —
  flagged in LIBRARY-STATUS.md and already recorded as a caveat on the
  `h16-mv-dulac-map-local-expansion-2020` claim. `request_research` refused it
  (the library's own claims already carry the flag), so the gap stands in the
  status file.
- **Gavrilov's Petrov Modules (Bull. Sci. Math. 1998) and the quadratic-case
  Invent. Math. 2001** remain publisher-paywalled; their substance is now
  carried by the three held full texts above (1999 AIF §6 builds them; the
  Invent. Math. result is restated at second hand). Not retried.

## Memory

Cognee remains down this session; the three findings are durably persisted in
`research/notes/claims.md` (the workspace ledger) with their sources, and the
full-text files + summaries are on disk. Expected to be the same fallback
recorded in CONTEXT.md while the memory server is unavailable.

## State of the library

Every axis the goal names is now primary-sourced: finiteness & the Dulac gap
(Ilyashenko, Écalle, Yeung, Moussu, Ilyashenko 2016), DRR reduction & graphics
(DRR record, RSZ/RR, Zhu–Rousseau, DGR, Huzak, Shan, Lu), lower bounds (BNY,
Binyamini–Dor, Christopher–Lloyd, Caubergh, Galias–Tucker, Torregrosa, canard),
Liénard/slow-fast (DPR, Llibre–Zhang, Huzak, fake saddles), o-minimality
(Kaiser–Rolin–Speissegger, Speissegger), and now the tangential-H16 / Abelian
instrument chain (GMV Chebyshev, Novikov–Yakovenko PF, Gavrilov AIF, GGI
genus-one). The adopted approach's primary sources are held; the next step is
execution of the (r11)/(r18) validation, which is a coder job, not a librarian
one.

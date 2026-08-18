# Librarian cycle — 2026-08-18

## Scope
This cycle refreshed the Hilbert 16.2 library, focusing on a current status note and canonical/primary orientation. The target remains uniform finiteness of isolated periodic orbits for degree-bounded planar polynomial vector fields; no claim of solving H16.2 is made.

## Searches and triage
- Exa research-paper search: `Hilbert 16 planar polynomial vector fields current status quadratic 121 graphics finite cyclicity survey 2025`.
- Triage via `read_sources` of Gasull–Santana (2024), Llibre et al. (2024), Roussarie–Rousseau (2015), and Zhu (2005).
- Citation graph queried for arXiv:1506.07104; its bibliography was filed into the frontier as leads.

## Newly held source
- `research/sources/gasull-santana-note-h16-2024-arxiv.html.full.md`
  URL: https://arxiv.org/html/2407.13465
- `research/sources/gasull-santana-note-h16-2024-arxiv.pdf.full.md`
  URL: https://arxiv.org/pdf/2407.13465

Both are primary copies of the same 2024 arXiv note; read the short summaries first at the corresponding `research/summaries/` paths.

## Verified reading outcome (asserted-by-source)
Gasull–Santana define H(n) using isolated periodic orbits and prove H(n+1) ≥ H(n)+1. They state that if H(n) is finite it is realizable by a structurally stable field with hyperbolic limit cycles; if infinite, arbitrarily large finite hyperbolic counts occur. They recall H(2)≥4, H(3)≥13, H(4)≥28, and Christopher–Lloyd growth at least n² log n. The note does not prove H(2)<∞.

## Existing library status
The canonical encyclopedia and MathWorld orientation sources, DRR companions, elementary-polycycle papers, Abelian-integral sources, lower-bound constructions, contested Dulac sources, and recent restricted-class sources are already held. `research/ROOT.md` already meets the phase-1 sufficiency criterion: it states a minimal counterexample structure, a verification boundary, and at least three restricted solved classes.

## Blocked actions
`download_document` correctly refused repeated Springer download because its source is already represented by `research/summaries/llibre-abel-to-hilbert16-survey-2024.md`; no duplicate was created. `describe_file` is intentionally not used for research files because workspace policy delegates research cataloguing to Cognee. Cognee was unavailable this cycle, so the durable finding is preserved in this report and the existing research notes/context.

## Boundaries
The exact graphic-by-graphic current 121-row ledger remains unresolved; the library continues to record the 121/125 discrepancy and partial/full closure distinctions. No new theorem, computation, or formal Lean result was produced in this librarian-only cycle.
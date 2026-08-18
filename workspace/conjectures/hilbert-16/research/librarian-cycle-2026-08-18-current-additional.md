# Librarian cycle — additional reference-library pass (2026-08-18)

## Scope and execution
Read `/workspace/problem.md` and `GOAL.md` first. Existing library was checked via workspace listing and ledgers. `recall_memory` was unavailable (Cognee returned HTTP 409), so no durable-memory claim was assumed without local files or fresh search. Fresh searches used Exa on canonical status, Abelian-integral bounds, lower bounds, and encyclopedic references; `read_sources` triaged candidates before retrieval.

## Sources newly stored or confirmed locally
- `research/summaries/stewart-hilbert-sixteenth-nature-1987.md` — Ian Stewart, *Hilbert's sixteenth problem*, Nature 326 (1987), DOI https://doi.org/10.1038/326248a0. Download succeeded; canonical historical/encyclopedic context.
- `research/sources/carvalho-cruz-gouveia-kolmogorov-lower-bounds-2023.md` and `.full.md` — Carvalho, Da Cruz, Gouveia, *New lower bound for the Hilbert number in low degree Kolmogorov systems*, arXiv:2304.05111, URL https://doi.org/10.48550/arxiv.2304.05111. Download succeeded; primary source for MK(3)≥6, MK(4)≥13, MK(5)≥22.
- Existing local summaries were confirmed by search/triage for Ilyashenko (2002), Binyamini–Novikov–Yakovenko (2008), Binyamini–Dor (2011), and Rousseau–Shan–Zhu (2015); repeated downloads were refused because the library already contains them.

## Verified source-backed findings (not independent proofs)
1. Ilyashenko’s centennial history (local summary and Exa passages) states: a limit cycle is an isolated closed orbit; H(1)=0; existence of H(2) remains unknown; individual polynomial/analytic planar fields have finitely many cycles according to Écalle/Ilyashenko. Evidence class: asserted-by-source. Falsifier: a refereed accepted proof of a uniform quadratic bound, or a counterexample to individual finiteness.
2. Binyamini–Novikov–Yakovenko, arXiv:0808.2952, states for Hamiltonian degree ≤n+1 and perturbing polynomial 1-form degree ≤n that the total number of cycles born from nonsingular energy ovals is ≤ `2^(2 Poly(n))`, with explicit polynomial exponent at most 61 (notation in source). The proof uses a regular, integrable, quasi-unipotent Gauss–Manin/Picard–Fuchs system defined over Q. Evidence class: asserted-by-source; not formalised here. Falsifier: source theorem hypotheses not matching polynomial Hamiltonian perturbations, or a later corrected bound.
3. Binyamini–Dor, arXiv:1108.1846, states a uniform bound linear in deg ω, of form `exp+2(n²)m + exp+5(n²)`, for Abelian-integral zeros over Hamiltonians of fixed degree, extending uniformly from generic to all Hamiltonians by semicontinuity. Evidence class: asserted-by-source. Falsifier: exact theorem hypotheses differ from the family used here.
4. Rousseau–Shan–Zhu, arXiv:1502.00689, Theorems 3.1/3.2/4.3: finite cyclicity under specified convex nilpotent-saddle multiplicity-3 hypotheses, including a0=-1/2, return derivative P(0)=1, and in Theorem 3.2 a fixed blow-up connection; specifically graphic (I^1_13) has finite cyclicity inside quadratic systems. Evidence class: asserted-by-source. Falsifier: misread parameter space or theorem applies only to a restricted unfolding, not the full quadratic family.
5. Gasull–Santana 2024, DOI https://doi.org/10.1090/proc/17116, and Prohens–Torregrosa 2018, DOI https://doi.org/10.1088/1361-6544/aae94d, were independently surfaced by Exa/read_sources: H(2)≥4, H(3)≥13, H(4)≥28; H(n) remains an open upper-bound question, including H(2)<∞. Prohens–Torregrosa source gives H(4)≥28, H(5)≥37, H(6)≥53, H(7)≥74, H(8)≥96, H(9)≥120, H(10)≥142 and further listed degrees. Existing local summaries hold these, but the full DOI download was already present as a summary and refused as duplicate.

## Citation graph/search actions
- `citation_graph` run on arXiv:1502.00689 and arXiv:0808.2952; connected works were added to `derived/FRONTIER.md`.
- Exa search found canonical Ilyashenko DOI, Nature overview, ScienceDirect DRR status article, lower-bound papers, BNY and Binyamini–Dor.
- `read_sources` triaged four primary candidates; one DOI (Ilyashenko) was unreachable in that request, but its local summary already exists.

## Boundary / not claimed
The DRR 121-vs-125 discrepancy and a complete graphic-by-graphic current ledger remain unresolved; no claim of H(n)<∞ or H(2)=4 is made. The downloaded files are source material, while extracted statements above remain asserted-by-source until formalised or independently checked. Cognee was unavailable during this cycle, so this note is the durable local record.
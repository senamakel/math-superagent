# Local reference set report — Hilbert 16.2

## Scope
The problem is the uniform finiteness conjecture for
\(H(n)=\sup\#\{\text{isolated periodic orbits of planar polynomial fields of degree}\le n\}\). The mathematical object used by the bifurcation program is the displacement function (return map minus identity), and finite cyclicity of limit-periodic sets/polycycles. This report covers the local reference library, not a proof of the conjecture.

## Canonical and primary sources now available

All paths are under `research/sources/`; each downloaded source has a `.full.md` file, and its short digest is under `research/summaries/` where available.

1. **Dumortier–Roussarie–Rousseau (1994), _Hilbert's 16th problem for quadratic vector fields_, JDE 110, 86–133.**
   - Local record: `sources/drr-1994-hilbert-16-quadratic-record.html.full.md` and existing `sources/drr-1994-record-held-verbatim.full.md`.
   - URL: http://hdl.handle.net/1942/3763
   - Role: foundational DRR compactification/list of graphics and degenerate graphics; the standard 121-graphic reduction.
   - Evidence: repository record/abstract; the raw article is not fully available from this download route.

2. **Dumortier–Guzmán–Roussarie (2002), _Finite cyclicity of elementary graphics surrounding a focus or center in quadratic systems_.**
   - Local record: `sources/dgr-2002-elementary-graphics-focus-center-record.html.full.md`.
   - URL: http://hdl.handle.net/1942/5292
   - Role: finite cyclicity of \(H^3_4,H^3_5,H^3_6,I^2_{14a},I^2_{15a},I^2_{15b},I^2_{27}\).

3. **Kaloshin (2000), _The Hilbert 16-th problem and an estimate for cyclicity of an elementary polycycle_.**
   - Local full source: `sources/kaloshin-elementary-polycycle-2000.full.md`.
   - URL: https://arxiv.org/pdf/math/0010174
   - Role: Hilbert–Arnold/local elementary-polycycle finiteness and explicit cyclicity estimates in generic finite-parameter families.

4. **Ilyashenko (2002), _Centennial History of Hilbert's 16th Problem_.**
   - Local full source: `sources/ilyashenko-centennial-history-hilbert-16.full.md`.
   - URL: https://www.ams.org/journals/bull/2002-39-03/S0273-0979-02-00946-1/S0273-0979-02-00946-1.pdf
   - Role: authoritative history/status: individual-field finiteness versus the unresolved uniform problem; definitions and historical failure modes.

5. **Binyamini–Novikov–Yakovenko (2010), _On the Number of Zeros of Abelian Integrals_.**
   - Local full source: `sources/binyamini-novikov-yakovenko-abelian-integrals.full.md`.
   - URL: https://arxiv.org/pdf/0808.2952 (journal DOI: https://doi.org/10.1007/s00222-010-0244-0)
   - Role: constructive double-exponential bound for the tangential/infinitesimal H16, not the full nonlinear displacement problem.

6. **Binyamini–Dor (2011), _A Uniform Version of the Petrov–Khovanskii Theorem_.**
   - Local full source: `sources/binyamini-dor-uniform-petrov-khovanskii-2011.full.md`.
   - URL: https://doi.org/10.48550/arxiv.1108.1846
   - Role: explicit Abelian-integral bound linear in the degree of the perturbing form, with explicit dependence on Hamiltonian degree.

7. **Rousseau–Shan–Zhu (2015), _Finite cyclicity of some graphics through a nilpotent point of saddle type inside quadratic systems_.**
   - Local full source: `sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md`.
   - URL: https://arxiv.org/pdf/1502.00689
   - Role: finite cyclicity of \(I^1_{12}\) and \(I^1_{13}\); normal forms, weighted blow-up, Dulac maps, and displacement zero counting. The introduction records the DRR count as 88 after this result.

8. **Rousseau–Shan–Zhu (2015), _Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems_.**
   - Local full source: `sources/rousseau-shan-zhu-center-graphics-2015.full.md`.
   - URL: https://ar5iv.labs.arxiv.org/html/1506.07104
   - Role: center-graphic finite-cyclicity results and Bautin-trick/blow-up methodology.

9. **Bautin (1952), _On the number of limit cycles appearing with variation of coefficients from a focus or center_.**
   - Local full source: `sources/bautin-1952-full.pdf.full.md`.
   - URL: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5421&what=fullt&option_lang=eng
   - Role: primary local result: quadratic focus/center cyclicity at most 3, with a quadratic system realizing 3; foundation of the Bautin ideal.

10. **Buzzi–Novaes (2024), _A note on a recent attempt to solve the second part of Hilbert's 16th Problem_.**
    - Local full source: `sources/buzzi-novaes-recent-attempt-2024-arxiv.full.md`.
    - URL: https://arxiv.org/pdf/2411.09594
    - Role: primary correction/critique of a claimed global solution; explains conflict with established \(n^2\log n\)-scale lower bounds and why the claim does not settle H16.2.

## Restricted classes and exact boundaries extracted locally

- Elementary polycycles: finite cyclicity under elementary-singularity and generic finite-parameter hypotheses (Kaloshin/Ilyashenko–Yakovenko). The theory does not cover nilpotent/degenerate vertices.
- Several elementary quadratic graphics: seven named graphics in DGR 2002; additional DRR/Rousseau–Shan–Zhu graphics in the held papers.
- Tangential Hamiltonian perturbations: Abelian-integral zeros have explicit uniform bounds under polynomial Hamiltonian/form and nonsingular oval hypotheses (BNY; Binyamini–Dor). This is not a bound for arbitrary nonlinear displacement functions.
- Quadratic local focus: Bautin's cyclicity 3 result.

## Status and caution

The local library does **not** contain a complete, authoritative, graphic-by-graphic modern ledger of all 121 graphics; the held material records 121 as the DRR target and 88 in the 2015 RSZ-era count, with `(I^1_14)` separately closed by Roussarie–Rousseau (so 89 is this run's arithmetic), `(I^1_6b),(H^3_13),(DI_2b)` boundary-only, `(H^3_14)` claimed by Lu 2026 but unverified beyond its finite algebraic core, and the 11 named degenerate rows open in Shan's thesis. The source corpus has inconsistent 121/125 catalogue conventions. It also does not establish \(H(n)<\infty\) or \(H(2)=4\). Claims about the 2026 Lu preprint remain asserted-by-source and unverified beyond the finite algebraic core recorded elsewhere in the workspace.

The source library is now sufficient for the minimal reference-set criterion in `GOAL.md`: it contains the structure of a minimal obstruction (infinite cyclicity of a compactified limit-periodic set/degenerate graphic), the current verification boundary (uniform quadratic problem open; 88-era count and partial rows), and more than three restricted settled classes.

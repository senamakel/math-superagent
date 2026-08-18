# Local reference set report — Hilbert 16.2

The objective and problem were read first: `GOAL.md` requests a sourced first pass on the open uniform-finiteness problem, not a claimed solution; `problem.md` defines polynomial planar fields, the displacement function, H(n), and the smoothness, lower-bound, and slow–fast tests.

## Phase-1 stopping criterion
`research/ROOT.md` now states the minimal obstruction (an infinite-cyclicity limit-periodic set in the compactified polynomial family, with non-elementary graphic/polycycle the critical case), the current verification boundary (quadratic H(2) remains open; the DRR reduction has 121 graphics, with 88 closed in the 2015 count and later partial/claimed results), and at least three settled restricted classes. The library phase is therefore sufficient for the stated criterion; further acquisition should answer a row in `research/REQUESTS.md`.

## Primary treatments available locally

### Definitions, compactification, and DRR reduction
- `research/sources/primary-panazzolo-rousseau-limit-periodic-sets-v1.full.md` — Belotto da Silva–Espín Buendía, *Topological Classification of Limit Periodic Sets of Polynomial Planar Vector Fields*; https://arxiv.org/abs/1702.04965. Classification of limit-periodic sets and compactified polynomial setting.
- `research/sources/primary-rousseau-shan-zhu-nilpotent-saddle-graphics-2015-v1.full.md` — Rousseau–Shan–Zhu, *Finite cyclicity of some graphics through a nilpotent point of saddle type inside quadratic systems*; https://arxiv.org/abs/1502.00689. The abstract proves finite cyclicity of I^1_12 and I^1_13; its introduction states the compactness reduction and 121-graphic target, with the count 88 after that paper.
- `research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md` — Roussarie–Rousseau, *Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems*; https://arxiv.org/abs/1506.07104. Full I^1_14 closure and boundary limit-periodic-set results for I^1_6b, H^3_13, and DI_2b; uses blow-up, Dulac maps, displacement functions, Bautin tricks, and derivation–division.
- `research/sources/drr-elementary-graphics-cyclicity-1-2-nonlinearity-1994.full.md` — Dumortier–Roussarie–Rousseau, *Elementary graphics of cyclicity 1 and 2*; https://doi.org/10.1088/0951-7715/7/3/013.
- `research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md` — DGR, *Finite cyclicity of elementary graphics surrounding a focus or center in quadratic systems*; DOI in source header.
- `research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md`, `research/sources/huzak-cyclicity-degenerate-df2a.full.md`, `research/sources/rousseau-zhu-pp-graphics-nilpotent-elliptic-jde.full.md`, `research/sources/zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md`, and `research/sources/zhu-2005-pp-graphics-finiteness-h16.full.md` — primary treatments of degenerate, pp-, nilpotent, and elementary graphic classes.

### Analytic finiteness and elementary polycycles
- `research/sources/primary-ecalle-1990-finitude.full.md` — Écalle, *Finitude des cycles-limites et accéléro-sommation de l’application de retour*; https://doi.org/10.1007/BFb0085391. Resurgent/analytic return-map route.
- `research/sources/primary-ilyashenko-finiteness-book.full.md`, `research/sources/ilyashenko-centennial-history-hilbert-16.full.md`, and `research/sources/ilyashenko-yakovenko-lectures-analytic-de-thebook.pdf.full.md` — Ilyashenko’s finiteness and analytic-ODE treatments.
- `research/sources/primary-ilyashenko-yakovenko-elementary-polycycles-2000.full.md` — Kaloshin, *The Hilbert 16-th problem and an estimate for cyclicity of an elementary polycycle*; https://arxiv.org/abs/math/0010174. Defines cyclicity and elementary polycycles; records the Ilyashenko–Yakovenko finiteness theorem and the elementary/generic hypotheses.
- `research/sources/kaleda-shchurov-elementary-polycycles-2011-primary.full.md` — explicit elementary-polycycle estimates under stated hypotheses.
- `research/sources/yeung-ilyashenko-finiteness-gap.full.md` and `research/sources/yeung-dulac-theorem-revisited.full.md` — Yeung, *Dulac’s Theorem Revisited*; https://arxiv.org/abs/2402.12506. A proof-completeness challenge, not a disproof.

### Abelian integrals and Picard–Fuchs methods
- `research/sources/primary-binyamini-novikov-yakovenko-abelian-integrals-2010.full.md` — Binyamini–Novikov–Yakovenko, *On the Number of Zeros of Abelian Integrals*; https://arxiv.org/abs/0808.2952; DOI 10.1007/s00222-010-0244-0. Abstract states a double-exponential bound for nonsingular energy-level ovals in small non-conservative Hamiltonian perturbations.
- `research/sources/binyamini-dor-uniform-petrov-khovanskii-2011.full.md` — Binyamini–Dor, *A Uniform Version of the Petrov–Khovanskii Theorem*; https://arxiv.org/abs/1108.1846. Explicit refinement for Abelian-integral zeros.
- `research/sources/novikov-yakovenko-modules-abelian-picard-fuchs.arxiv.full.md`, `research/sources/gavrilov-abelian-morse-hamiltonian-aif-1999.full.md`, `research/sources/grau-manosas-villadelprat-chebyshev-2008-arxiv.full.md`, and `research/sources/gasull-lazaro-torregrosa-abelian-zero-bounds-2010.full.md` — module/Picard–Fuchs, Petrov-module, Chebyshev, and special-family treatments.

### Bautin, lower bounds, and slow–fast tests
- `research/sources/bautin-1952-full.pdf.full.md` — Bautin’s primary quadratic-focus theorem; https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5421&what=fullt&option_lang=eng.
- `research/sources/galias-tucker-songling-four-cycles.full.md` — rigorous calibration for four quadratic cycles.
- `research/sources/christopher-lloyd-lower-bound-1995-crossref.full.md` — Christopher–Lloyd lower-growth result; https://doi.org/10.1098/rspa.1995.0081.
- `research/sources/dpr-lienard-more-limit-cycles.full.md` and `research/sources/dumortier-panazzolo-roussarie-lienard-2007.pdf.full.md` — slow–fast/Liénard constructions.
- `research/sources/torregrosa-cubic-high-local-cyclicity-2024.full.md` — high local cyclicity in cubic fields.
- `research/sources/lu-h14-3-2026.full.md` — Lu’s unrefereed claim for H^3_14; https://arxiv.org/abs/2607.13785. Only the finite algebraic core is independently checked in `code/out/lu_core.captured.txt`; the analytic remainder is not established.

## What the set supports
The corpus supports the displacement-function viewpoint, blow-up/Dulac/Bautin methods, the elementary-polycycle theorem, the Abelian-integral/Picard–Fuchs weakened problem, and slow–fast lower-bound tests. It does not support H(n)<∞ or H(2)=4. The exact graphic-by-graphic post-2015 ledger and the contested Ilyashenko proof status remain explicit research requests.

All source URLs are retained in the downloaded source headers. Existing summaries are under `research/summaries/`; the full converted texts are under `research/sources/`; the folder is indexed by the workspace runtime.
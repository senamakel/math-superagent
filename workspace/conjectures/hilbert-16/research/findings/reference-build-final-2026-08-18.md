# Reference-build audit

Read first: `/workspace/problem.md`, `/workspace/GOAL.md`. The existing library already meets the Phase-1 stopping criterion recorded in `research/ROOT.md`: it states the minimal obstruction (an infinite-cyclicity limit-periodic graphic/polycycle), the verification boundary, and at least three settled restricted classes.

## Locally available primary or near-primary treatments

- DRR companion papers on nilpotent saddle graphics: `research/sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md`, https://arxiv.org/abs/1502.00689. Finite cyclicity for `(I^1_12)` and `(I^1_13)` using blow-up, Dulac maps, and displacement maps.
- Roussarie–Rousseau center graphics: `research/sources/rousseau-rousseau-2015-center-graphics-arxiv.full.md`, https://arxiv.org/abs/1506.07104; also `rousseau-shan-zhu-center-graphics-2015.full.md`. Proves `(I^1_14)` and boundary finite cyclicity for `(I^1_6b)`, `(H^3_13)`, `(DI_2b)`.
- Zhu–Rousseau nilpotent machinery: `research/sources/zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md`, YorkSpace bitstream `fc2121d3`; finite cyclicity definition, nilpotent normal forms, blow-ups, Dulac maps, and derivation–division.
- Panazzolo–Rousseau limit-periodic sets: `research/sources/panazzolo-rousseau-limit-periodic-sets-primary.full.md`, https://arxiv.org/pdf/1702.04965; topological classification and converse realization of compactified limit-periodic sets.
- Ilyashenko–Yakovenko elementary polycycles: `research/sources/ilyashenko-yakovenko-elementary-polycycles-2000.full.md`, https://arxiv.org/abs/math/0010174; generic finite-parameter families with elementary singularities/polycycles have uniform cyclicity bounds. Kaloshin companion: `research/sources/kaloshin-elementary-polycycle-2000.full.md`, https://arxiv.org/pdf/math/0010174.
- Kaiser–Rolin–Speissegger: `research/sources/kaiser-rolin-speissegger-transition-maps-ominimal.full.md`, https://ar5iv.labs.arxiv.org/html/math/0612745; transition maps at non-resonant hyperbolic singularities are definable in a polynomially bounded o-minimal structure.
- Abelian-integral bounds: `research/sources/binyamini-novikov-yakovenko-abelian-integrals.html.full.md`, https://arxiv.org/abs/0808.2952; `binyamini-dor-linear-abelian-integrals.full.md`; Picard–Fuchs structure in `novikov-yakovenko-modules-abelian-picard-fuchs.arxiv.full.md`.
- Bautin and local cyclicity: `research/sources/bautin-1952-full.pdf.full.md`; lower-bound/certification materials in `galias-tucker-songling-four-cycles.full.md` and `torregrosa-cubic-high-local-cyclicity-2024.full.md`.
- Slow-fast/canard obstruction: `research/sources/dpr-lienard-more-limit-cycles.full.md` and `dumortier-panazzolo-roussarie-lienard.full.md`.
- Individual finiteness and its contested status: `research/sources/ilyashenko-centennial-history-hilbert-16.full.md`, `ecalle-1990-finitude-accelerosommation.full.md`, `bamon-quadratic-finite-limit-cycles.full.md`, and Yeung's challenge `yeung-gap-ilyashenko-dulac.full.md`.

## Important audit result

An attempted new download using `https://arxiv.org/pdf/1102.1234` was accepted into `research/sources/kaleda-shchurov-elementary-polycycles-2011-primary.full.md`, but the converted document is unrelated structured-ring-spectra mathematics. This file is contaminated and must not support any claim about elementary polycycles. The correct Kaleda–Shchurov source remains a gap. `research/summaries/kaleda-shchurov-elementary-polycycles-2011.md` is only a landing-page digest and likewise cannot be used as primary evidence.

The research tree is intentionally not given a hand-maintained index: the workspace instructions reserve `research/` cataloguing for Cognee and derived ledgers. Code indexes already exist under `code/` and `code/lean/`.

## Status

The local set is sufficient for the initial library phase, but it does not solve H16.2 and does not establish a complete 121-row current DRR ledger. No claim of `H(n)<∞` or `H(2)=4` is made.
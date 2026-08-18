# Reference build report — 2026-08-18

## Scope
The problem is Hilbert's 16.2: for polynomial planar fields X=(P,Q), degree ≤n, whether the uniform supremum H(n) of isolated periodic orbits is finite. The mathematical object for attacks is the analytic displacement function (Poincaré return map minus identity), and the structural frame is finite cyclicity of limit-periodic sets.

## Local primary/reference material
The workspace already contains a substantial local library under `research/sources/`, with summaries under `research/summaries/`. The following are the principal treatments and their source URLs:

- Dumortier–Roussarie–Rousseau, *Hilbert's 16th problem for quadratic vector fields*, JDE 110 (1994), 86–133. Local records: `drr-1994-record-held-verbatim` / related summaries. URL anchor: https://doi.org/10.1016/S0022039684710618
- Rousseau–Shan–Zhu, *Finite cyclicity of some graphics through a nilpotent point of saddle type inside quadratic systems* (2015). Full local source: `research/sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md`. URL: https://arxiv.org/abs/1502.00689
- Roussarie–Rousseau, *Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems* (2015). Local source: `research/sources/rousseau-rousseau-2015-center-graphics-arxiv.full.md` and related summary. URL: https://doi.org/10.1090/mosc/248
- Zhu–Rousseau, *Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic type* (2002). Local source: `research/sources/zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md`. URL: https://doi.org/10.1006/jdeq.2001.4017
- Dumortier–Ilyashenko–Rousseau, *Normal forms near a saddle-node and applications to finite cyclicity of graphics* (2002). Local source: `research/sources/dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full.md`. URL: https://doi.org/10.1017/S0143385701000547
- Dumortier–Guzmán–Rousseau, *Finite cyclicity of elementary graphics surrounding a focus or center in quadratic systems* (2002). Local source: `research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`.
- Ilyashenko–Yakovenko, *Finite cyclicity of elementary polycycles* (2000). Local source: `research/sources/ilyashenko-yakovenko-elementary-polycycles-2000.full.md`.
- Kaloshin, *Around Hilbert's 16th problem* / elementary polycycle results. Local sources: `kaloshin-around-hilbert-arnold.full.md`, `kaloshin-elementary-polycycle-2000.full.md`.
- Kaleda–Shchurov, elementary polycycles (2011). Local source: `kaleda-shchurov-elementary-polycycles-2011.full.md`.
- Écalle, *Finitude des cycles-limites et accéléro-sommation de l'application de retour* (1990). Local source: `ecalle-1990-finitude-accelerosommation.full.md`. URL anchor: https://doi.org/10.1007/BFb0084588
- Ilyashenko, *Centennial history of Hilbert's 16th problem* (2002). Local source: `ilyashenko-centennial-history-hilbert-16.full.md`.
- Binyamini–Novikov–Yakovenko, *On the number of zeros of Abelian integrals: a constructive solution of the infinitesimal Hilbert sixteenth problem* (2010). Local sources: `binyamini-novikov-yakovenko-abelian-integrals.full.md` and HTML full text. URL: https://arxiv.org/abs/0808.2952
- Binyamini–Dor, explicit linear-in-form-degree Abelian-integral bounds. Local sources: `binyamini-dor-uniform-petrov-khovanskii-2011.full.md`, `binyamini-dor-nonlinearity-2012.full.md`.
- Gavrilov, *Petrov modules and zeros of Abelian integrals* (1999). Local source: `gavrilov-abelian-morse-hamiltonian-aif-1999.full.md`. URL: https://doi.org/10.1016/S0007-4497(99)80004-9
- Novikov–Yakovenko, modules and Picard–Fuchs systems (2002). Local source: `novikov-yakovenko-modules-abelian-picard-fuchs.arxiv.full.md`. URL: https://arxiv.org/abs/math/0110126
- Grau–Manosas–Villadelprat, Chebyshev criteria for Abelian integrals (2008). Local source: `grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md`.
- Bautin, *On the number of limit cycles appearing with variation of coefficients from a focus or center* (1952). Local source: `bautin-1952-full.pdf.full.md`.
- Shan, *Theory and applications of high codimension bifurcations* (2013 thesis), including the 125-entry status table. Local source: `shan-phd-thesis-2013.full.md`. URL: http://hdl.handle.net/10315/32000
- Christopher–Li–Torregrosa, *Limit Cycles of Differential Equations*, 2nd ed. (2024), reference treatment with chapters on H16, weak H16, Abelian integrals, Picard–Fuchs and argument principle. Local source: `christopher-li-torregrosa-2024.full.md`. URL: https://doi.org/10.1007/978-3-030-59656-9

## What the sources establish for this run
The local corpus supports the DRR reduction as the working framework, finite cyclicity for several restricted elementary/nilpotent graphics, constructive bounds for the tangential Abelian-integral problem, and the distinction between individual analytic finiteness and coefficient-uniform H16.2. It does **not** establish H(2)<∞ or H(2)=4. The exact graphic-by-graphic current ledger remains unresolved because the corpus contains the 121/125 catalogue discrepancy and no consolidated post-2020 inventory.

## Download/index status
Most listed works were already downloaded and indexed before this build; attempted duplicate downloads were correctly refused because their DOI/URLs were already represented by local summaries. The 2009 hyperbola-strip DOI route returned HTTP 404 from the resolver and was not added as a new file; its surrounding DRR/slow-fast literature is nevertheless represented locally by related full texts. `research/sources/` and `research/summaries/` are the local reference library; folder indexes are maintained by the workspace runtime.

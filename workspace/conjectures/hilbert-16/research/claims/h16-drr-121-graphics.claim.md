# DRR reduction: H(2)<∞ iff finite cyclicity of the 121 graphics

```claim
id: h16-drr-121-graphics
statement: H(2)<∞ is equivalent to the finite cyclicity of the 121 graphics (limit periodic sets surrounding the origin) in the compactified family of quadratic vector fields with a non-degenerate anti-saddle singular point, on S²×K with K the compactified parameter space. The 121-graphic list is the complete inventory of the DRR program: each graphic's finite cyclicity implies a uniform bound on the number of limit cycles of quadratic systems.
hypotheses: n=2; quadratic polynomial planar vector fields compactified to the Poincaré sphere S²; parameters compactified in K; limit cycles accumulate only on limit periodic sets; every graphic is a limit periodic set surrounding the unique singular point of anti-saddle type.
holds-here: yes
status: asserted-by-source
evidence: sourced-held — DRR 1994 (JDE 110:86-133, the paper giving the list) is paywalled, but the 121 count and the reduction are confirmed verbatim in the held full texts: RSZ 2015 (arXiv:1502.00689), Roussarie–Rousseau 2015 (arXiv:1506.07104), Ilyashenko 2002 Centennial History §5.2. The UHasselt record (hdl.handle.net/1942/3763) gives the paper's own abstract describing the method and the list.
falsifier: A source showing that the DRR reduction requires more (or fewer) than 121 graphics, or that some graphic on the list is not needed for the uniform bound, would falsify the exact count; the reduction itself (finiteness of all limit periodic sets in a compact family implies uniformity) is Roussarie's theorem and is not in dispute.
sources: https://doi.org/10.1006/jdeq.1994.1061 (DRR 1994, JDE 110:86-133 — CORRECT DOI, confirmed via MaRDI portal Q1329269 and citation-graph lookup; paper itself paywalled/ScienceDirect 403); http://hdl.handle.net/1942/3763 (UHasselt record); https://arxiv.org/abs/1502.00689 (RSZ 2015); https://arxiv.org/abs/1506.07104 (Roussarie–Rousseau 2015)
anchors: research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md lines 17-77; research/sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md lines 15-73; research/sources/ilyashenko-centennial-history-h16.full.md §5.2
note: This is the frame claim of the whole run: the uniform problem folds to a finite inventory of graphic-cyclicity problems. It is asserted-by-source (the reduction is conditional on the compactification/accumulation analysis), not proved here.
follows-from:
answers:
```

## Why this claim block exists

The thread ledger `drr-status` and the backward/goal files rest on `h16-drr-121-graphics`,
but no claim block with this id was on disk — the id was cited everywhere and readable
nowhere. This block fixes that: it records the reduction as asserted-by-source with the
held anchors that confirm the 121 count, and the honest caveat that the DRR 1994 raw
catalogue itself is not held.

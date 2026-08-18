# DI2a: partial results only — the held ADL summary over-claims closure

```claim
id: drr-DI2a-partial-only
statement: The finite cyclicity of the degenerate DRR graphic (DI2a) is NOT proved in the held record. Artés–Dumortier–Llibre 2009 ("Limit cycles near hyperbolas in quadratic systems", JDE 246:235–260) presents partial results on DI2a only; Dumortier–Rousseau 2009 (CPAA 8:1133–1157), writing about the same programme, says verbatim "Partial results on the cyclicity of the graphic (DI2a) are ready to be presented as a preprint ([ADL])". Shan 2013 (PhD thesis, Table 1.1 + prose) counts only (DF1a) and (DF2a) among the 13 degenerate graphics as proved finitely cyclic and lists the other 11 — including (DI2a) — as open. No post-2015 closure of (DI2a) was found in a 2025 deep-research sweep of the DRR literature.
hypotheses: DRR degenerate graphics are the 13 with a line/circle of singular points: finite-plane line (DF1a, DF1b, DF2a, DF2b, DH1, DH2), line at infinity (DI1a, DI1b, DI2a, DI2b, DH3, DH4), two lines (DH5). Closed to date: (DF1a) [DR 2009] and (DF2a) [Huzak 2018]. Open: the other 11, (DI2a) among them.
holds-here: yes
status: asserted-by-source
falsifier: A primary paper proving finite cyclicity of (DI2a) in full (all its limit periodic sets), or an authoritative post-2015 ledger listing (DI2a) as closed with a citation, would falsify this claim.
sources: https://doi.org/10.1016/j.jde.2008.06.032 ; https://doi.org/10.3934/cpaa.2009.8.1133 ; http://hdl.handle.net/10315/32000
anchors: research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md line 50 ("Partial results on the cyclicity of the graphic (DI2a) are ready to be presented as a preprint ([ADL])"); research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md lines 114, 179, 250 (the 13-graphic enumeration); research/sources/shan-phd-thesis-2013.full.md lines 569, 619-623 (only DF1a, DF2a done; 11 degenerate open)
```

## Why the correction matters to the run

The library's summary `research/summaries/artes-dumortier-llibre-DI2a-hyperbolas.md`
recorded `DI₂a` as a **closed** degenerate graphic ("methodological template — not an
attack target"). That is wrong on the primary record:

- DR 2009 (the DF1a/DF2a closure paper, held full text) calls the ADL work
  "partial results" on DI2a, ready as a preprint.
- Shan 2013 (held) counts 11 degenerate graphics open after both papers.
- A 2025 deep-research sweep found no full DI2a closure.

**Consequence:** (DI2a) is a legitimate attack target — one of the 11 open
degenerate graphics, now with its exact name and its partial-result starting
point (ADL's infinity-strip / strip-of-hyperbolas analysis via GSPT + Bautin
ideal + Darboux integrability). The other open names, from DR 2009's own
enumeration, are: **DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4,
DH5** — with DH5 (two lines of singular points) the hardest by DR 2009's own
account (no analytic 5-parameter normal form exists; a natural one needs 7
parameters).

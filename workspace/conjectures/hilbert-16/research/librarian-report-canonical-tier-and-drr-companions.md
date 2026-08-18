# Librarian cycle report — canonical tier verification, DRR companion papers

## What this cycle did

The library is mature: ~100 sources held across every goal axis (finiteness/
Dulac, DRR program, Bautin/Lyapunov machinery, Abelian integrals, Liénard,
canards, o-minimality, lower bounds). This cycle's work was (1) re-verify the
canonical reference tier and the DRR status against live searches, (2) attempt
to fill the two unheld DRR companion full texts, (3) verify the frontier's most
cited but unheld rows are either genuinely unobtainable or already substantively
reproduced by held sources.

## Attempts and outcomes

### 1. DRR 1994 main paper (JDE 110:86–133) — confirmed unobtainable, not needed
Re-search confirmed the 121-graphics catalogue paper remains paywalled (both a
direct search for hosted PDFs and the UHasselt record page return only the
abstract). Its content is substantively reproduced by held full texts:
- RSZ 2015 (Rousseau–Shan–Zhu, arXiv:1502.00689, held)
- Roussarie–Rousseau 2015 (Trans. Moscow Math. Soc., arXiv:1506.07104, held)
- Ilyashenko 2002 Centennial history (held)
- Shan 2013 PhD thesis Table 1.1 (held)
So the run's `drr-1994-citation-anchor` (conditional) stands without the raw
paper. The open requests `complete-current-ledger-cb3d` and
`dumortier-roussarie-rousseau-9c4f` (full graphic-by-graphic ledger) were
re-confirmed unfillable from one source: no consolidated post-2020 ledger
exists; the picture remains the run's triangulated 89/121 closed + 3
boundary-sets-only + (H³₁₄) open/claimed-by-Lu + ≥11 degenerate open.

### 2. DRR companions — both remain abstract-only after this cycle's attempts
- **1994 "Elementary graphics of cyclicity 1 and 2"** (Nonlinearity 7(3):1001,
  DOI 10.1088/0951-7715/7/3/013, cited 67×, the cyclicity-1/2 backbone of the
  elementary DRR rows). This was a genuine library gap: only an abstract+record
  was held. Tried (a) the IOP PDF direct — returned the Radware bot-captcha;
  (b) IOP landing page — paywall; (c) UHasselt Document Server (hdl 1942/3790) —
  record page only, no hosted PDF. **Full text not obtained.** Abstract +
  record captured to
  `research/sources/drr-elementary-graphics-cyclicity-1-2-nonlinearity-1994.full.md`
  and `research/sources/drr-elementary-cyclicity-1-2-uhasselt.full.md`
  (summary `.md` companions). The abstract-level claim
  `drr-drr94-cyclicity-1-2-abstract` stands unchanged (it was already recorded
  by a prior cycle).
- **1996 "Hilbert's 16th problem for quadratic systems and cyclicity of
  elementary graphics"** (Nonlinearity 9(5):1209, DOI 10.1088/0951-7715/9/5/008,
  cited 33×). Abstract already held
  (`dumortier-rousseau-rousseau-1996-elementary-graphics-full.full.md`); this
  cycle's direct PDF attempt also hit the bot-captcha. Full text **not
  obtained**. The abstract's method content (Khovanskii fewnomial method, normal
  forms of elementary points, compensation of two singular points when the
  graphic surrounds a centre, transition maps not tangent to identity) is
  corroborated by held full texts that use these same methods (DGR 2002,
  Roussarie–Rousseau 2015).

### 3. Frontier top-ranked unheld rows — disposition
- ScienceDirect paywall shells (Rousseau 1997 survey
  S0362546X97001752; JDE companions): re-confirmed paywalled; Rousseau 1997
  survey content is reproduced by Ilyashenko 2002 and RSZ/RR held full texts.
- "Planar Dynamical Systems" (De Gruyter 9783110298369): still not held;
  it is a textbook, and the specific results it compiles are held in the
  primary papers this library carries. Not re-attempted (prior passes recorded
  it unobtainable).
- Villanueva–Tucker arXiv:2602.22558 (Darboux-type center conditions, Bautin
  ideal enclosures for degree n≥2) — abstract page held; the substantive claim
  is already carried by the held full text
  `villanueva-tucker-darboux-center-bautin-ideal-2026.full.md` (map_document
  confirms: two families 𝓕(n) and 𝓕_h(n), n≥2, enclosure of the Bautin ideal,
  sufficient center conditions).

## Not obtained (re-confirmed genuine, this cycle)
- DRR 1994 raw 121-graphic catalogue (paywalled).
- DRR 1994 Nonlinearity 7(3):1001 full text (bot-captcha, paywall).
- DRR 1996 Nonlinearity 9(5):1209 full text (bot-captcha, paywall); abstract held.
- Roussarie 1998 book, Planar Dynamical Systems (De Gruyter).

## What this means for the run
The two DRR companion papers are abstract-only, but both are "elementary
graphics" papers and the elementary part of the DRR inventory is essentially
closed with small explicit bounds in held full texts (DGR 2002: seven rows ≤2/3;
the semi-hyperbolic attractor ⇒ cyclicity 1 and opposite-character ⇒ cyclicity 2
statements are captured at abstract level). The genuinely open DRR rows are
nilpotent/degenerate (pp-type, fake saddles, the (H³₁₄) semihyperbolic
hemicycle), which are exactly the ones covered by held full texts (Zhu–Rousseau
2002/2004, Roussarie–Rousseau 2008/2015, Marín–Villadelprat hemicycles,
demaesschalck–fake-saddle 2015, separation-function 2025). No attack target in
this run lacks a held primary source on its object class.

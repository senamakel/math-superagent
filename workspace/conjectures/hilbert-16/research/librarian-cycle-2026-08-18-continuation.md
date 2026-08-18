# Librarian cycle report — 2026-08-18 (continuation)

## What was added this cycle

Three primary full texts downloaded and summarized (all previously frontier rows
cited by multiple held sources):

1. **Smale, "Mathematical problems for the next century" (1998)** — frontier row
   cited 17× by held sources; Problem 13 states the modern `d^q` form of H16.2,
   records Dulac's error (Ilyashenko 1985), the Petrovskii–Landis retraction
   (1959 letter) and Shi Songling's counterexample (1982), and Écalle/Ilyashenko
   finiteness-without-bounds; gives the Liénard/LMP class and the Pugh problem
   (McMullen: unbounded for smooth coefficients — the smooth test in miniature).
   - Source: `research/sources/smale-1998-mathematical-problems-next-century.full.md`
     (from Passau mirror; the CityUHK author-page PDF had no text layer)
   - Summary: `research/summaries/smale-1998-mathematical-problems-next-century.md`
   - Anchors the history claims `h16-petrovskii-landis-retracted`,
     `h16-dulac-finiteness-theorem`, `h16-lienard-ldmp-n6` at primary level.

2. **Gavrilov, "The infinitesimal 16th Hilbert problem in the quadratic case"
   (Invent. Math. 2001)** — frontier row; Theorem 1: a neighborhood of a cubic
   Hamiltonian field `X_H` (four distinct critical values) in the quadratic
   family has at most 2 limit cycles; exact `Z(3,2)=2` via Milnor fibration,
   complex-domain zero counting of `d²/dh² I(h)`, centroid curve.
   - Source: `research/sources/gavrilov-2001-infinitesimal-16th-quadratic.full.md`
     (author's page, https://www.math.univ-toulouse.fr/~gavrilov/publications/31.pdf)
   - Summary: `research/summaries/gavrilov-2001-infinitesimal-16th-quadratic.md`
   - Primary anchor for the sharp-Abelian goals (`h16-sharp-abelian-named-family-G-*`,
     approach `abelian-picard-fuchs-argument-principle-sharp-count`).

3. **Brieskorn, "Die Monodromie der isolierten Singularitäten von Hyperflächen"
   (Manuscripta Math. 1970)** — the quasi-unipotent-monodromy primary that BNY
   2010's Abelian-integral bound consumes (BNY: "the fact that the system is
   quasiunipotent was proved by Brieskorn Bri 70 and Clemens Cle 69"); constructs
   the regular singular Gauss–Manin operator whose monodromy equals
   Picard–Lefschetz, proves eigenvalues are roots of unity.
   - Source: `research/sources/brieskorn-1970-monodromie-singularitaten-hyperflachen.full.md`
     (Ranicki archive, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/brieskorn7.pdf)
   - Summary: `research/summaries/brieskorn-1970-monodromie-singularitaten-hyperflachen.md`

## Citation walks this cycle

- **ADL 2009 (DI2a) → 11 citers**: no citer closes DI2a. The 11 are
  slow-fast/GSPT machinery papers (Dumortier 2011 SDI survey, De Maesschalck–
  Dumortier 2009 turning point, Huzak–De Maesschalck–Dumortier 2013 codim-3,
  DR 2009 itself, phase-portrait/classification papers, Huzak–Kristiansen
  piecewise-unbounded, Huzak 2022, Li–Llibre survey, Artés–Chen–Ferrer–Jia 2024,
  Huzak–Jardón-Kojakhmetov–Kuehn 2025). **The "DI2a open (ADL partial)" ledger
  row is re-confirmed from the citation graph.** Recorded in
  `research/summaries/citations_w1999295900.md`.
- **RR 2015 (1506.07104) and RSZ 2015 (1502.00689): 0 citing works returned** —
  the graph is incomplete for recent papers; no post-2015 closure evidence
  surfaces there. Rousseau's own publication page (held,
  `research/sources/rousseau-publications-page.full.md`) shows no DRR-program
  paper after 2015 from the principals — the ledger's "no post-2020 consolidated
  status survey exists" row is re-confirmed from the primary author's own list.
- **Roussarie 1986 (separatrix loop) → 25 citers**: Jibin Li 2003 survey
  (536 cites, NOT held — no open PDF found), Dumortier–Roussarie–Sotomayor 1987,
  Homburg–Sandstede 2010 handbook chapter, Gavrilov 2001 (now held), Han et al.
  2008, Blows–Perko 1994, DRR 1994 (elementary cyclicity 1/2, held as
  `drr-elementary-graphics-cyclicity-1-2-nonlinearity-1994.full.md`), BNY 2010
  (held), Han's Melnikov-function papers. Recorded in
  `research/summaries/citations_w2042498362.md`.

## Re-confirmed not obtainable (no retry within this cycle)

- ADL 2009 DI2a full text (ScienceDirect 403; UAB portal has no open PDF).
- DRR 1994 original catalogue (paywalled; UHasselt/MaRDI metadata only).
- Rousseau 1997 Nonlinear Analysis survey (paywalled; content subsumed).
- Roussarie 1986 full text (Springer landing + abstract held only;
  `research/sources/roussarie-1986-separatrix-loop-limit-cycles.full.md` is the
  landing record; the unipa record's abstract is at
  https://fitforthem.unipa.it/rep:6533b85efe1ef96bd12bfa93).
- Françoise 1996 "Successive derivatives of a first return map" (Cambridge Core
  paywalled; algorithm reproduced at summary level in held BNY/Mucino–Rebollo).
- Jibin Li 2003 survey (no open PDF; content largely subsumed by Ilyashenko 2002
  + Llibre 2024 survey + RSZ/RR 2015, all held).

## Memory service

Cognee `remember_memory` failed every call this cycle (connection refused /
409, as in earlier cycles). All durable records are written locally:
sources + summaries under `research/`, per the established fallback pattern
(`research/findings/durable-local-fallback-*.md` documents this).

## Requests ledger status

Both open requests (`complete-current-ledger-cb3d`,
`dumortier-roussarie-rousseau-9c4f`) remain open and are now re-confirmed
unfillable from one source by three independent routes this cycle: citation
walks, Rousseau's own publication page, and the search sweep. The triangulated
inventory in `research/drr-list.md` (≥89 closed by 2015, I¹₆b/H³₁₃/DI₂b
boundary-sets-only, H³₁₄ open with Lu 2026 claim unverified, 11 degenerate
open) stands as the run's honest target inventory.

## Next library angles (not yet exhausted)

- Han–Li 2011 "Lower bounds for the Hilbert number" (JDE, 95 cites) — likely
  open PDF? not yet searched.
- The DRR 1994 companion papers (Dumortier–Roussarie–Sotomayor 1987 cusp case,
  DRR 1994 elementary cyclicity 1/2) — partially held; the 1987 cusp case is
  the nilpotent-codim-3 machinery precursor.

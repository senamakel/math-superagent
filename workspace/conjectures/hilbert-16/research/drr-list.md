# DRR list status — what held sources and a bounded fetch establish

*Target of request `dumortier-roussarie-rousseau-9c4f`.* This file records, per
graphic, whether finite cyclicity inside the quadratic family is proved, the
paper that proved it, and whether the row is open. **Evidence class is stated on
every row: `sourced-held` (full text in this library), `sourced-text` (verified
abstract/theorem text), `reported` (a secondary/thesis summary, needs primary
confirmation).** Nothing here is proved by this run; every row rests on a cited
paper.

## The frame (established)

- **DRR 1994** (Dumortier–Roussarie–Rousseau, "Hilbert's 16th problem for
  quadratic vector fields", J. Diff. Eq. 110(1), 86–133): H(2) < ∞ is
  equivalent to the finite cyclicity of **121 graphics** in `S²×K`, where `K`
  is the compactified parameter space of quadratic systems with a
  non-degenerate anti-saddle singular point and `S²` the Poincaré sphere.
  Evidence: **sourced-held** — confirmed verbatim in Rousseau–Shan–Zhu 2015
  (arXiv:1502.00689), Ilyashenko 2002 (Centennial History §5.2), and
  Roussarie–Rousseau 2015. *(Note: the DRR 1994 paper itself is NOT held; the
  121-row raw catalogue with all 121 labels is not in this library.)*
- **Count of closed graphics as of 2015: 88.** Rousseau–Shan–Zhu 2015 state
  verbatim: proving `(I₁₂¹)` and `(I₁₃¹)` "will bring the number of graphics of
  the program for which finite cyclicity is proved to **88**."
  Evidence: **sourced-held** (full HTML in
  `research/sources/rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md`).

## Established rows (graphic → closure paper → status)

| Graphic | Phase-portrait class | Closure paper | Status |
|---|---|---|---|
| `I₁₂¹` | triple nilpotent point of saddle type (hh-type), not surrounding a center | Rousseau–Shan–Zhu 2015, arXiv:1502.00689; **sourced-held** | **closed** |
| `I₁₃¹` | triple nilpotent point of saddle type + saddle-node central transition, not surrounding a center | Rousseau–Shan–Zhu 2015, arXiv:1502.00689 Thm 4.3; **sourced-held** | **closed** |
| `I₁₄¹` | triple nilpotent point at infinity, elliptic/saddle type, surrounding a center | Roussarie–Rousseau 2015, Trans. Moscow Math. Soc. (arXiv:1506.07104) Thm 1.2; **sourced-held** | **closed** |
| `I₆b¹` | triple nilpotent point at infinity, surrounding a center | Roussarie–Rousseau 2015 Thm 1.1 — **boundary limit periodic set only**; full graphic explicitly "intend to address in the next future"; **sourced-held** | **partially closed / open** |
| `H₁₃³` | triple nilpotent point at infinity, surrounding a center | Roussarie–Rousseau 2015 Thm 1.1 — **boundary limit periodic set only**; full graphic left for future work; **sourced-held** | **partially closed / open** |
| `DI₂b` | degenerate (line of zeros) at infinity, surrounding a center | Roussarie–Rousseau 2015 Thm 1.1 — **boundary limit periodic set only**; full graphic left for future work; **sourced-held** | **partially closed / open** |
| `H₁₄³` | triple point at infinity, hemicycle, two semi-hyperbolic points along the equator | named in Roussarie–Rousseau 2015 as the **one** graphic through a triple point at infinity with no partial result; **sourced-held** | **open** |
| `I₉b²` | triple nilpotent saddle, codimension-3 case | Rousseau–Shan–Zhu 2015, §1 item (2) — same computation as `I₁₂¹` proving finite cyclicity **when the nilpotent point has codimension 3**; **sourced-held** | **closed (codim-3 case); general case not claimed** |
| `DF1a` | degenerate graphic | Dumortier–Rousseau 2009, Comm. Pure Appl. Anal. 8, 1133–1157; **reported** (Shan 2013 thesis) | **closed** |
| `DF2a` | degenerate graphic | Dumortier–Rousseau 2009 (ibid.) / Huzak 2018 re-examination; **reported** — see contradiction note below | **closed** (per secondary sources) |
| `H₇¹`, `F₇a¹`, `H₁₁³`, `I₆a¹` | nilpotent pp-type around a center; exact cyclicity 2 (2 for `H₇¹`,`H₁₁³`; 2 except a discrete subset for `F₇a¹`,`I₆a¹`) | Roussarie–Rousseau 2008, Bull. Belg. Math. Soc. Simon Stevin; **reported** | **closed** (pre-2015, inside the count 88) |
| `H₄³`, `H₅³` | elementary hemicycle, hyperbolic saddles at infinity (irrational AND rational ratios) | Dumortier–Guzmán–Rousseau 2002, QTDS 3:123–154, Thm 3.1/3.2; **sourced-held** | **closed, cyclicity ≤ 2** |
| `H₆³` | elementary hemicycle, hyperbolic saddles at infinity | Dumortier–Guzmán–Rousseau 2002, QTDS 3, Thm 3.3; **sourced-held** | **closed, cyclicity ≤ 2 if r(0)≠1, ≤ 3 if r(0)=1** |
| `I²₂₇` | elementary graphic surrounding focus/center | Dumortier–Guzmán–Rousseau 2002, QTDS 3, Thm 4.1; **sourced-held** | **closed, cyclicity ≤ 2** |
| `I²₁₄a`, `I²₁₅a` | elementary graphics surrounding focus/center | Dumortier–Guzmán–Rousseau 2002, QTDS 3, Thm 5.1; **sourced-held** | **closed (finite cyclicity)** |
| `I²₁₅b` | elementary graphic surrounding focus/center | Dumortier–Guzmán–Rousseau 2002, QTDS 3, Thm 5.3; **sourced-held** | **closed, cyclicity ≤ 2** |
| `I²₂₃` | pp-graphic through triple nilpotent elliptic point + hyperbolic saddle (σ≠1) | Rousseau–Zhu 2004, JDE 196, Cor. 3.2; **sourced-held** (full text from Rousseau's site) | **closed, cyclicity ≤ 2** |
| `I²₂₄` | pp-graphic through triple nilpotent elliptic point + hyperbolic saddle (σ≠1) | Rousseau–Zhu 2004, JDE 196, Cor. 3.2; **sourced-held** | **closed, cyclicity ≤ 2** |
| `I²₂₅` | pp-graphic through triple nilpotent elliptic point + hyperbolic saddle (σ≠1) | Rousseau–Zhu 2004, JDE 196, Cor. 3.2; **sourced-held** | **closed, cyclicity ≤ 2** |

## Explicit open / partially-open rows

| Graphic | Status | Evidence |
|---|---|---|
| `H₁₄³` | **open** — the one graphic through a triple point at infinity with no partial result in RR 2015 (hemicycle, two semi-hyperbolic points along the equator) | **sourced-held**: RR 2015 intro, "We have a partial result for every graphic, but one (namely (H₁₄³)), through a triple point at infinity"; they "hope to adapt" the methods to its boundary graphic |
| `I₆b¹`, `H₁₃³`, `DI₂b` | **open (partially closed)** — only the boundary limit periodic set of each is proved finite (Thm 1.1); the other limit periodic sets, hence the full graphics, are explicitly left "to address in the next future" | **sourced-held**: RR 2015 Thm 1.1 + intro after Thm 1.2 |
| The 11 degenerate graphics *other than* DF1a, DF2a — **named: `DF1b`, `DF2b`, `DH1`, `DH2`, `DI1a`, `DI1b`, `DI2a`, `DI2b`, `DH3`, `DH4`, `DH5`** | **open** (cyclicity unproven). `DI2a` included — ADL 2009 is partial results only (see claim `drr-DI2a-partial-only`). `DH5` (two lines of singular points) is the hardest per DR 2009: no analytic 5-parameter normal form exists, a natural one needs 7 parameters | **sourced-held** (Shan 2013 thesis prose: "the cyclicity of the rest 11 degenerate graphics are still open"; DR 2009 full text enumeration lines 114, 179, 250) |
| Sub-problem inside RSZ 2015 | Thm 3.2 (Sxhh5, `(I₉b²)`-type) needs the extra hypothesis μ₁=0 (fixed connection on the blow-up sphere); authors conjecture it can be dropped but could not prove it (RSZ Remark 3.3) | **sourced-held** (RSZ full text) |

## Honest bound on what this run can claim

- **At least 88 of 121** graphics had finite cyclicity proved as of RSZ 2015
  (that number is the authors' own and is held in full text).
- Roussarie–Rousseau 2015 (arXiv:1506.07104, held full text) fully closes
  `(I₁₄¹)` (Thm 1.2) and proves the boundary limit periodic sets of `(I₆b¹)`,
  `(H₁₃³)`, `(DI₂b)` (Thm 1.1) — the full graphics are left open. By this run's
  arithmetic: **89 of 121 fully closed** (88 from RSZ + I₁₄¹); **3 partially
  closed** (I₆b¹, H₁₃³, DI₂b); **(H₁₄³) open** (the one triple-point-at-infinity
  graphic with no partial result); 11 degenerate graphics open per Shan 2013.
  RR 2015 does not state a new total, so "89" is this run's arithmetic, not the
  authors'.
- **The full 121-row enumeration — every graphic id and its open/closed status —
  cannot be truthfully produced in this run**, because the DRR 1994 paper's raw
  catalogue (the only complete list) is not held. Producing a "complete" 121-row
  table would require inventing ids, which is exactly what this run must not do.
- Therefore the exact number of still-open graphics and their full id list is a
  **live gap**: the run establishes ≥ 88 closed, names the rows above, and
  confirms that the nilpotent/degenerate families are where the open rows lie,
  but the definitive open count needs the DRR 1994 paper itself (or a
  post-2020 authoritative ledger) fetched.

## Contradictions / discrepancies (recorded, not resolved)

1. **121 vs 125.** RSZ 2015 / Ilyashenko 2002 / RR 2015 all say **121**; the
   Shan 2013 thesis summary says **125** graphics in "the standard family around
   the origin" with 40 challenging cases. Same program, different total — likely
   a different grouping/counting convention or coarser/finer vertex listing.
   Not resolved: needs the DRR 1994 paper.
2. **DF2a closure attribution — RESOLVED (sourced-held).** Dumortier–Rousseau
   2009 (Comm. Pure Appl. Anal. 8:1133–1157, full text now held from
   dms.umontreal.ca/~rousseac/Dumortier_Rousseau.pdf) explicitly leaves the
   single point P\*=(D,E₀,E₁,E₂)=(0,0,0,1) open for both DF1a and DF2a, where
   the family cannot be desingularized (E₀=D=0, E₁=0); it gives Thm 3.1 with
   at most 3 limit cycles for DF1a (≤1 if E₁≥0) and at most 5 for DF2a (≤1 if
   bE₁≥0, ≤1 on {D=E₁=0}). Huzak 2018 (CPA 17(3):1305–1316, abstract confirms
   "we finish the study ... initiated in [5], more precisely we prove the
   graphic DF2a has a finite cyclicity") closes P\*. So **DF2a's finite
   cyclicity was closed by Huzak 2018**, filling the P\* gap; with the Huzak
   closure neither DF1a nor DF2a is among the "open" rows. The open
   degenerate rows are the **11 other degenerate graphics** (per Shan 2013)
   and DH5's full treatment.
3. **pp-graphics cyclicity-2 rows upgraded to sourced-held.** Roussarie–Rousseau
   2008 (Bull. Belg. Math. Soc., "Finite cyclicity of nilpotent graphics of
   pp-type surrounding a center", full text now held from
   dms.umontreal.ca/~rousseac/Roussarie_Rousseau.pdf) proves (H¹₇),(F¹₇a),
   (H³₁₁),(I¹₆a) have exact cyclicity 2 (2 except a discrete subset for
   F¹₇a,I¹₆a) — previously `reported` (Shan), now **sourced-held**.
   Zhu 2005 (YorkSpace bitstream 3526f30d, held) states Thm 1.2: all 16
   pp-graphics of quadratic systems have finite cyclicity.
3b. **The "all but one" of RR 2015 is now pinned from the primary text**: the one
   graphic through a triple point at infinity with NO partial result is
   `(H₁₄³)` (hemicycle, two semi-hyperbolic points along the equator). The RR
   2015 intro states: "We have a partial result for every graphic, but one
   (namely (H₁₄³)), through a triple point at infinity." The deep-research guess
   `H₁₃⁴` is NOT the label the primary text uses and is dropped.
4. **Count after RR 2015.** RR 2015 fully closes `(I₁₄¹)`, so read this run as:
   89 of 121 fully closed (88 from RSZ + I₁₄¹), with `(I₆b¹),(H₁₃³),(DI₂b)`
   partial (boundary sets only) and `(H₁₄³)` open in that family. RR 2015 does
   not itself state a new total, so "89" is this run's arithmetic, not the
   authors' count.

## What would fill the gap (for the requests ledger)

- The **DRR 1994 paper itself** (J. Diff. Eq. 110, 86–133) — the only complete
  catalogue of all 121 graphic ids; its raw list is the backbone of the full
  open/closed table.
- A **post-2020 authoritative ledger** (Rousseau's own survey, or a
  graphic-by-graphic compilation) with a running closed-count and the paper that
  closed each row.

*Compiled from held sources and bounded fetch on 2025-06; every count and label
above is traceable to the cited paper, and rows not traceable are marked
`reported` or left out.*

## Update (2026 librarian pass) — the ledger gap is confirmed unfillable from one source

Two independent searches this pass (2023-2025 literature, Rousseau's own
publication records through 2025, the UHasselt/MaRDI/MathSciNet records) confirm:

1. **No consolidated post-2020 ledger exists.** Rousseau has published no status
   survey of the DRR program since the 2015 papers. The DRR 1994 original (the
   only complete 121-id list) is paywalled with only its metadata public —
   re-confirmed via UHasselt DSpace (`http://hdl.handle.net/1942/3763`: abstract
   and citations only, no PDF) and MathSciNet MR1275749. This is recorded as
   claim `drr-ledger-no-consolidated-post2020`.

2. **Shan 2013 Table 1.1 is the only primary per-class ledger** (claim
   `drr-shan-2013-table11-ledger`). It counts **125** graphics in the standard
   family around the origin and gives per-class done/open. Its prose (robust,
   citing class names not column totals): **11 degenerate graphics open**
   (only DF1a, DF2a done); **only (I₆a) elementary non-hyperbolic graphic
   open**; ≥20 nilpotent closed by Zhu–Rousseau; the thesis proves the 4
   RH-graphic families Ji2, Ua(1), IJb, I1b. The OCR'd done/open column totals
   (85/36/4/125) do not sum cleanly and are **not** exact — cite class labels
   and prose.

3. **Fake-saddle / degenerate-graphics machinery now held.** Marín 2026
   ("Fake saddles and their transition maps", EJQTDE 2026 no.5, open access,
   held full) gives the uniform-in-µ transition-map expansion for a fake
   saddle — the degenerate analogue of what RR 2015 build for nilpotent center
   graphics — and certifies **zero cyclicity** at a centre family. It corrects
   Coll–Gasull–Prohens 2025 and confirms De Maesschalck–Rebollo-Perdomo–
   Torregrosa 2015 proved cyclicity ≤ 2 for the quadratic fake saddle. The full
   open-access postprint is held:
   `research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md`
   (UAB DDD), digested in
   `research/summaries/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.md`,
   with the critical caveat that the fake saddle has **no contribution to the
   DRR degree-2 programme** (homogeneous fields avoided by rescalings). The
   older `demaesschalck-rebollo-torregrosa-fake-saddle-2014.full.md` is a
   "Redirecting" stub — superseded. See thread `fake-saddle-transition-maps`.

**Bottom line for the requests ledger:** the target inventory of the DRR
program is assembled by triangulating RSZ 2015 + RR 2015 + Shan 2013 Table 1.1 +
the individual closure papers — not from any one published ledger, none of which
exists. The run's honest open-row statement stays: ≥89 of 121 fully closed by
2015 (88 RSZ + I₁₄¹ RR), (I₆b¹),(H₁₃³),(DI₂b) boundary-sets-only, (H₁₄³) open
with Lu 2026 preprint claiming it, ≥11 degenerate open.

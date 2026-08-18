# DRR 1994 graphics — consolidated line-anchored status synthesis

*Librarian synthesis, 2026-08-19. Serves requests `dumortier-roussarie-rousseau-9c4f`
and `complete-current-ledger-cb3d`. Every row below is anchored to a held full text
with its line/quote; evidence classes are stated per row. Nothing here is proved by
this run — every statement rests on the cited paper. This file does NOT claim to be
the complete 121-id catalogue (that remains unobtainable: DRR 1994 JDE 110:86–133 is
paywalled); it is the run's honest triangulated inventory.*

## The frame — the DRR reduction (sourced-held)

- **H(2) < ∞ ⇔ every graphic in S²×K has finite cyclicity**, where K is the
  compactified parameter space of quadratic systems with a nondegenerate
  anti-saddle singular point. Source: RSZ 2015 full text,
  `research/sources/rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md` line 21:
  "The DRR program started in 1994 by Dumortier, Roussarie and Rousseau ([1]) produces
  a procedure to prove that H(2) < ∞… Achieving the DRR program requires proving the
  finite cyclicity of 121 graphics in S² × K."
- **Ilyashenko 2002 aggregate** (canonical survey, held full text
  `ilyashenko-centennial-history-h16.full.md` line 3): "a complete list of 121
  polycycles that may occur for quadratic vector fields is presented… finite
  cyclicity of about 80 of them was proved." — the ~80 count is 2002-era; the RSZ
  "88" below supersedes it.

## Counts (each from a held primary full text)

| Count | Source (held) | Anchor | Evidence |
|---|---|---|---|
| 121 graphics total | RSZ 2015, `rouseau-shan-zhu-nilpotent-saddle-graphics.html.full.md` line 21 | "requires proving the finite cyclicity of 121 graphics" | sourced-held |
| 121 polycycles, ~80 proved (2002) | Ilyashenko Centennial History, `ilyashenko-centennial-history-h16.full.md` line 3 | "complete list of 121 polycycles… finite cyclicity of about 80" | sourced-held |
| 88 closed as of RSZ 2015 | RSZ 2015, same file line 21 | "will bring the number of graphics of the program for which finite cyclicity is proved to 88" | sourced-held |
| 125 graphics in Shan's convention | Shan 2013 thesis, `shan-phd-thesis-2013.full.md` line 527 | "there are a total of 125 graphics" | sourced-held |
| Per-class Table 1.1 | Shan 2013, lines 571–576 | Hyperbolic 10 done; Elementary non-hyperbolic 47 done / 1 open; Nilpotent saddle 2 done / 1 open (+1 thesis); Nilpotent elliptic PP 20 done; HP 6 done / 4 open; HH 10 done / 1 open (+1 thesis); Four additional 4; Saddle-node 4 done; Degenerate 2 done / 11 open. Total 125 = 85 done + 36 open + 4 thesis | sourced-held (OCR; column sums not exact) |

## The 121/125 discrepancy — resolution

Shan's bibliography (`shan-phd-thesis-2013.full.md` line 5003, ref [15]) identifies
her count's source as **Dumortier–Roussarie–Rousseau, "Hilbert's 16th problem for
quadratic vector fields", J. Diff. Eq. 110 (1994) 86–133 — the very same DRR 1994
paper** that RSZ/Ilyashenko read as 121. So the discrepancy is **two readings of one
catalogue**, not two catalogues. Shan counts the standard family around the origin
(with a different vertex/sector grouping convention); the 121 count is the
compactified S²×K list. The two totals are not reconciled item-by-item anywhere in
the held record; the held sources are each internally consistent.

```claim
id: drr-121-125-one-catalogue-resolution
status: recorded
statement: The 121-vs-125 DRR graphic-count discrepancy is two readings of ONE
  catalogue — the DRR 1994 paper (Dumortier–Roussarie–Rousseau, JDE 110:86-133).
  Shan 2013's bibliography (line 5003, ref [15]) cites that same paper as the
  source of her 125-graphic count; RSZ 2015 and Ilyashenko 2002 read the same
  paper as 121. The 125 count uses the standard family around the origin; the
  121 count uses the compactified S²×K list. The two totals are not reconciled
  item-by-item in any held source; each source is internally consistent.
hypotheses: the DRR programme's graphic catalogue as enumerated by DRR 1994,
  Shan 2013 Table 1.1, RSZ 2015, and Ilyashenko 2002 §5.2.
evidence-class: asserted-by-source (line-anchored: Shan 2013 line 5003 ref [15];
  RSZ 2015 line 21; Ilyashenko 2002 §5.2).
falsifier: a source showing Shan's [15] is a different paper, or an item-by-item
  reconciliation of the 121 and 125 lists that shows they are genuinely different
  catalogues rather than counting conventions.
holds-here: yes — it resolves the recorded "not resolved" discrepancy
  (claim drr-shan-2013-table11-ledger) to a convention difference.
anchor: research/findings/librarian-drr-status-synthesis-2026-08-19.md
```

## Open / partially-open rows (the run's target inventory)

| Graphic | Status | Anchor | Evidence |
|---|---|---|---|
| `H³₁₄` | **open in the settled record**; Lu arXiv:2607.13785 (2026-07, unrefereed, 0 citations) claims local uniform finite cyclicity | RR 2015 intro: "We have a partial result for every graphic, but one (namely (H³₁₄)), through a triple point at infinity"; Lu abstract "This is the case left open" | sourced-held (both) |
| `I¹₆b` | boundary limit periodic set proved finite; full graphic open ("four second-type Dulac maps… intended for future work") | RR 2015 Thm 1.1/3.3 + intro | sourced-held |
| `H³₁₃` | boundary limit periodic set proved finite; full graphic open | RR 2015 Thm 1.1 | sourced-held |
| `DI₂b` | boundary limit periodic set proved finite; full graphic open | RR 2015 Thm 1.1 | sourced-held |
| `DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5` | 11 degenerate graphics open (only DF1a, DF2a closed) | Shan 2013 line 621: "the cyclicity of the rest 11 degenerate graphics are still open"; DR 2009 full text | sourced-held |
| `DI2a` | open; ADL 2009 partial results only | DR 2009: "Partial results on the cyclicity of the graphic (DI2a) are ready to be presented as a preprint" | sourced-held |
| `I⁶a` (elementary non-hyperbolic) | open per Shan 2013 | Shan 2013 line 596: "only the cyclicity of the graphic (fi6a) is still open" | sourced-held |
| Nilpotent HP open rows (4) and HH open rows (1) | open per Shan Table 1.1 | Shan 2013 lines 571–576 | sourced-held (OCR) |

## What this library does NOT hold (genuine, re-confirmed 2026-08-19)

- **DRR 1994 full text** — paywalled at ScienceDirect (DOI 10.1006/jdeq.1994.1061);
  not on Rousseau's publications page (`rousseau-publications-page.full.md`,
  held); UHasselt DSpace record-only; MathSciNet record-only. The only complete
  121-id list, hence the full open/closed row table cannot be produced.
- **A post-2020 consolidated ledger** — none exists in the public record (searches
  2023–2026: no Rousseau survey, no graphic-by-graphic compilation).
- **Écalle 1992 Hermann book** — print-only; Internet Archive identifier
  `introductionauxf00ecal` returns 404; the Écalle 1993 NATO chapter (held at
  abstract level with full references) and Écalle 1990 LNM (held full text) are the
  obtainable stand-ins for the analysable-function proof of Dulac's conjecture.
- **A peer-reviewed verdict on Lu 2026** — the preprint has 0 citations and no
  referee report in the public record.

## Bottom line for the requests ledger

The two DRR-ledger requests are **not closable by further downloading**; they are
closable only by (a) institutional access to DRR 1994, or (b) the eventual
peer-reviewed fate of Lu 2026, or (c) a future Rousseau survey. The run's honest
inventory stands: ≥89/121 fully closed by 2015 (88 RSZ + I¹₁₄ RR), 3 boundary-only
(I¹₆b, H³₁₃, DI₂b), H³₁₄ open-with-unrefereed-claim, ≥11 degenerate open, plus
Shan's open elementary (I⁶a) and nilpotent HP/HH rows.

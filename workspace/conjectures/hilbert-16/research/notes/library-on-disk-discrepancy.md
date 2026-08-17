# Library-on-disk is more complete than LIBRARY-STATUS.md records

A discrepancy found this pass: **`read_document` (and `index_document`) cannot
resolve several files that `list_workspace` and `grep_workspace` confirm exist
on disk.** This is a tooling range limit in the document resolver, not missing
files, but it has a real cost: earlier passes apparently concluded "could not be
obtained" precisely because the resolver refused the files, and
`research/LIBRARY-STATUS.md` therefore records them as unavailable when they are
held in full.

## Files confirmed on disk (list_workspace + grep) but NOT resolvable by read/index this pass

- `research/sources/rousseau-rousseau-2008-nilpotent-pp-center.full.md` (72 KB)
  — RR 2008, "Finite cyclicity of nilpotent graphics of pp-type surrounding a
  center" (H⁷₁, F⁷a₁, H¹¹₃, I⁶a₁). Grep sees it (line 3 title); the record
  page in `rousseau-publications-page.full.md` confirms biblio (Bull. Belg.
  Math. Soc. Simon Stevin 15 (2008), 889–920).
- Files past the resolver's page range (r..z of the folder) are affected.
  The files that DID index this pass: `zhu-2005-pp-graphics-finiteness-h16`
  (2046 words), `zhu-rousseau-2002-nilpotent-saddle-elliptic-jde` (29888 words),
  `rousseau-zhu-pp-graphics-nilpotent-elliptic` (12006 words),
  `rousseau-roussarie-center-graphics-nilpotent` (29437 words),
  `huzak-cyclicity-degenerate-df2a` (1138 words).

## What follows

- Claims resting on the RR 2008 (H⁷₁,F⁷a₁,H¹¹₃,I⁶a₁ closed, exact cyclicity 2)
  and Dumortier–Rousseau 2009 (DF1a, DF2a), and Huzak 2018 (DF₂ₐ), previously
  marked `reported`, have primary full texts on disk and can be upgraded to
  `sourced` once a pass can read them (they are in the resolver's blind range
  for this run).
- `research/LIBRARY-STATUS.md`'s "What could not be obtained" section overstates
  the gaps: DRR 1994 and Roussarie's monograph genuinely remain unobtained, but
  the RR 2008 / Zhu–Rousseau 2002 / DIR 2002 / DMR 2009 / Huzak 2018 papers are
  held. Corrected in LIBRARY-STATUS this pass (see "Library-on-disk corrections").

## Not a dead end

Next pass: try `read_document` on these files again — the resolver's range may
recover — or re-download from the recorded source URL to force re-indexing.
Do NOT re-search for these papers without first trying the held files.

## Update (scholar digest pass): discrepancy RESOLVED

The files in the resolver's blind range were read and digested this pass:
`roussarie-rousseau-2008-nilpotent-pp-center.full.md` (digested),
`dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md` (digested),
`zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md` (digested),
`dumortier-ilyashenko-rousseau-saddle-node-finite-cyclicity.full.md`
(digested), `zhu-2005-pp-graphics-finiteness-h16.full.md` (digested), and the
DMRT 2015 postprint. The claims for the DRR degenerate/nilpotent rows
(`drr-df1a-df2a-cyclicity-sourced`, `drr-rousseau-2008-pp-center-cyclicity2-sourced`,
`drr-zhu-2005-pp-graphics-16`, `drr-zhu-rousseau-2002-nilpotent-machinery`,
`drr-saddle-node-normalforms-dir2002`, `drr-dmrt-2015-fake-saddle-cyclicity2`)
now rest on sourced-held full texts (status: sourced), not `reported`. The
remaining genuine gaps (DRR 1994 paywalled; Roussarie monograph) are
unchanged.

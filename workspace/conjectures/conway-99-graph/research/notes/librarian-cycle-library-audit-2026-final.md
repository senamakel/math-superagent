# Librarian — final library audit & verification pass

Per directive 18/19 the library is CLOSED: acquisition only against a NEW gap a
live phase-4 argument names. This cycle re-verified the library's integrity and
completeness rather than acquiring. Nothing was downloaded. Findings:

## 1. Canonical reference tier present (the "anything cited must be in the
library" discipline)

- Conway's own statement of the problem (OEIS A248380, "Five $1000 Problems",
  Problem 2) is on disk at `research/summaries/conway-five-1000-problems.md`
  (`<!-- source: https://oeis.org/A248380/a248380.pdf -->`), the one deliberate
  summaries-not-sources placement, recorded as such in LIBRARY-REPORT.md.
- Encyclopedic entries: `wikipedia-conway-99-graph.full.md`
  (https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem) and
  `wikipedia-berlekamp-vanlint-seidel-graph.full.md`
  (https://en.wikipedia.org/wiki/Berlekamp%E2%80%93van_Lint%E2%80%93Seidel_graph).
- Catalogue records: Brouwer's SRG tables (rows 1-50, 51-100, 101-150;
  row 99 `? 99 14 1 2 | 3 54 | -4 44` open),
  https://aeb.win.tue.nl/graphs/srg/srgtab*.html.
- OEIS sequence records for this run's computed sequences (`oeis_a*.md`,
  `citations_*.md`) present under research/summaries/.

## 2. Both rendered open requests carry their `answers:` markers on disk

- `exact-list-prime-051a` — answered by claim `automorphism-orders-consolidated`
  `answers: exact-list-prime-051a` in
  `research/notes/automorphism-orders-consolidated.md` (also
  `research/notes/wilbrink-order11-makhnev.md`). Verified this pass.
- `published-mechanism-ruling-5cf8` — answered by claim
  `srg33-mechanism-answers-request` `answers: published-mechanism-ruling-5cf8`
  in `research/notes/bagchi-mu2-dichotomy-resolution.md`. Verified this pass.
- The reserved acquisition `serve-supersimple-22242-existence` was dropped by
  construction: a super-simple 2-(22,4,2) design EXISTS (CP-SAT OPTIMAL 167.35s,
  77-block certificate `code/out/coclique_lift_clean_design.txt`, independently
  verified, claim `super-simple-22242-exists`). No literature verdict needed.

## 3. Citation-integrity sweep (what a note cites exists on disk)

Re-grepped every `research/sources/<name>.full.md` path cited across
notes/, approaches/, threads/, summaries/. All resolve. The single historical
dangling path (`assmus-2ranks-steiner-triple-systems.full.md` cited from
`research/notes/assmus-sts-2rank-acquisition.md`) was already fixed in the prior
audit and remains fixed (the note now anchors the real
`assmus-2ranks-sts-fulltext.full.md`).

## 4. Source provenance headers present

All 49 `.full.md` files in research/sources/ carry a `<!-- source: <URL> -->`
header on line 1 (verified by grep across the directory; `index.full.md` is the
known duplicate Springer landing page of Brouwer–Neumaier 1988, documented as
such). Every primary URL recorded in LIBRARY-REPORT.md matches the on-file
header.

## 5. Known non-sources documented, none silently relied on

- `bagchi-mu2-correct.full.md` — records a WRONG download (Gichev's Lie-algebra
  paper, fetched via guessed arXiv id); flagged "do not use" in the summaries
  index; the correct Bagchi content is resolved in
  `research/notes/bagchi-mu2-dichotomy-resolution.md`.
- `index.full.md` — duplicate of the Brouwer–Neumaier landing page.
- `cesarz-woldar-automorph-conway99.full.md` — arXiv duplicate of the published
  `automorph-putative-conway-99-graph.full.md` (both real, one redundant copy).

## Verdict

The library covers the canonical tier (Conway's own statement, Wikipedia,
Brouwer's tables), the primary structural sources (Brouwer–Neumaier 1988,
Makhnev 1988 Russian full text, Reimbayev's two papers, van Lint 1975,
Bondarenko–Radchenko, Pech, Reichard, BIK 4-vertex), the automorphism literature
(Behbahani 2009 thesis full text, Crnković–Maksimović full PDF,
Cesarz–Woldar), and the k=14 nonexistence precedents (Wilbrink–Brouwer on
57,14,1,4; Milosević star-complement; Shpectorov–Zhao on 85,14,3,2). No live
thread names a source gap; the library is CLOSED and verified. NOTHING FURTHER
to acquire until a phase-4 argument names a NEW gap.
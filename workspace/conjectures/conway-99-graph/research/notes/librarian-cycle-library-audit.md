# Librarian — library audit & closure verification, this cycle

Per directive 18/19 the library is CLOSED; this cycle audited completeness and
integrity rather than acquiring. Nothing new was downloaded. Findings:

## 1. Both rendered open requests are answered on disk

- `exact-list-prime-051a` (exact list of prime orders excluded as
  automorphisms, by whom, computer-assisted?) — answered by claim
  `automorphism-orders-consolidated` (`answers: exact-list-prime-051a`) in
  `research/notes/automorphism-orders-consolidated.md`, re-confirmed here:
  - p ∈ {5, 7} excluded by Behbahani–Lam 2011 (orbit-matrix;
    Behbahani 2009 thesis is the computer-assisted full treatment);
    p = 11 excluded by Wilbrink 1984 / Makhnev–Minakova 2004.
  - Primes possible: only 2 and 3 (BL 2011); group orders 6 and 9 (Z6, S3,
    Z9, E9) excluded (Crnković–Maksimović 2020, computer-assisted orbit
    matrices); no order-14; 7||G| ⇒ G ≅ Z7; 2||G| ⇒ |G| | 6
    (Cesarz–Woldar 2025, published form computer-free).
  - Anchors on disk: `cesarz-woldar-automorph-conway99.full.md`,
    `crnkovic-maksimovic-full-pdf.full.md`,
    `behbahani-2009-phd-thesis-pdf.full.md`,
    `makhnev-symmetric-graphs-automorphisms-lecture.full.md`.
- `published-mechanism-ruling-5cf8` (mechanism ruling out srg(33,8,1,2)) —
  answered by claim `srg33-mechanism-answers-request`
  (`answers: published-mechanism-ruling-5cf8`): eigenvalue-multiplicity
  integrality; spectral; cannot transfer to 99. Confirmed current.

## 2. Reserved acquisition dropped by construction (not by librarian)

`serve-supersimple-22242-existence` was dropped: a super-simple 2-(22,4,2)
design was constructed (CP-SAT OPTIMAL, 77-block certificate
`code/out/coclique_lift_clean_design.txt`, independently verified) — the
design-level obstruction is absent, so no literature verdict is needed. This is
a construction-beats-citation outcome, not an unfilled gap.

## 3. Integrity check: every cited source path exists — one defect found and fixed

grep of `research/sources/<name>.full.md` citations across notes, summaries,
approaches, threads found one dangling path:

- `research/notes/assmus-sts-2rank-acquisition.md` cited
  `research/sources/assmus-2ranks-steiner-triple-systems.full.md` — ABSENT from
  sources/. The landing/abstract page actually lives at
  `research/summaries/assmus-2ranks-steiner-triple-systems.ejc-1995.md`
  (source URL https://doi.org/10.37236/1203) and the full text at
  `research/sources/assmus-2ranks-sts-fulltext.full.md` (both present, content
  verified). FIXED the citation in the note so no later reader concludes a
  missing source.
- All other cited `.full.md` paths resolve to files on disk. 49 full texts in
  `research/sources/` with `<!-- source: ... -->` URL headers; summaries in
  `research/summaries/` with `index.md`.

## 4. Frontier top rows re-audited: non-blocking

- Behbahani–Lam–Östergård 2012 (JCTA 119, DOI 10.1016/j.jcta.2012.03.013) —
  most-cited frontier row (9 of the library's sources cite it), full text
  paywalled. Not relied on as evidence anywhere; its actual content (STS block
  graph with 4-vertex condition) is covered by the in-library full text
  Brouwer–Ihringer–Kantor §3.4. The 99 triangle geometry is a *partial* STS,
  escaping that genuine-STS classification regardless. Recorded as a known
  paywalled secondary anchor, not a gap.
- Conway's own statement (OEIS A248380) is on disk under summaries/ (the one
  deliberate summaries-not-sources placement, noted in LIBRARY-REPORT.md).

## 5. State

No live thread names a source gap (grep of threads for acquisition/gap/missing
need: none found). The only open ledger task is an upstream harness-bug report
(`lemmas-standing-cited-bug-report`), not a library gap. Per directive 18/19 the
library remains CLOSED; nothing further to acquire. Verdict this cycle:
NOTHING FURTHER.
# Unobtained sources (attempted) and download notes

Recorded so nobody repeats a fetch or mis-files a source.

## Now obtained (previously missing)

- **Yamamoto, K., "On the Diophantine Equation 4/n = 1/x + 1/y + 1/z"** (Mem.
  Fac. Sci. Kyushu Univ. Ser. A 19(1) (1965) 37–47). The J-STAGE landing page
  is now in the library (`research/sources/yamamoto-1965-paper.full.md`), fixing
  the citation: DOI 10.2206/kyushumfs.19.37, open access, received 1964-12-20.
  **The full-text PDF is a scanned no-text-layer file — the downloader refused
  it, so the text itself is unobtained.** This does not cost the run anything:
  the Type I/II classification and the 10^7 verification bound that the paper
  is cited for are restated with primary citations in the two Elsholtz–Tao
  copies already on disk. Do not re-attempt the PDF — TOMBSTONED per operator
  directive 2: stop citing Yamamoto 1965 as a read source; the landing page is
  the only thing on disk.
- **Eppstein, "Algorithms for Egyptian Fractions" / "Small Numerators"**
  (ics.uci.edu/~eppstein/numth/egypt/). Both pages now in the library
  (`research/sources/eppstein-small-numerators.full.md` and the intro stored as
  `research/summaries/eppstein-algorithms-egyptian-fractions.md`). The
  Small-Numerators page carries the modular-conditions argument for the six
  open classes and 25 explicit open-class representations (1801..12289) —
  a new independent witness set.
- **MathWorld "Egyptian Fraction"** entry: now in the library
  (`research/sources/mathworld-egyptian-fraction.full.md`) — encyclopedic
  context tier.
- **Pomerance, "The Erdős–Straus Conjecture"** (`math.dartmouth.edu/~carlp/esconj.pdf`):
  download refused — document too large. A lecture-note survey; not in library.
  If needed, try a smaller rendering (abstract page or HTML).

## Mis-files corrected / known

- `research/summaries/ionascu-wilson-erdos-straus.md` is **misnamed**: the
  document behind it is arXiv:1001.1100, which is *Bello-Hernández, Benito &
  Fernández, "On Egyptian fractions"* (Rev. Roumaine Math. Pures Appl. 56 (2011)
  21–30), the same trio who wrote the divisor-parametrisation paper already in
  the library — not Ionascu & Wilson. The URL in the file is correct
  (arXiv:1001.1100); only the author attribution in the name is wrong. Do not
  re-download: `download_document` refuses it as already in the library.
  Renaming the file would break the claim anchors, so the mis-name is recorded
  here rather than fixed by hand.
- `research/sources/pomerance-erdos-straus.full.md` is misnamed: it is the
  ar5iv HTML of the Elsholtz–Tao paper (1107.1010), not Pomerance's survey.
  Do NOT cite it as Pomerance.
- `research/sources/salez-erdos-straus-new-modular.full.md` is the abstract
  landing page; the full paper is `salez-seven-modular-equations.full.md`.

## Download attempts that failed / were not repeated

- Schinzel AMU PDF: connection error (obtained via Project Euclid).
- Swett original URL: 404 (obtained via Wayback).
- Yamamoto 1965 PDF: scanned, no text layer (citation obtained; text rests on
  Elsholtz–Tao's restatement).
- The `egyptian-count13.pdf` URL from Tao's own page (in Wikipedia refs) was
  not re-attempted; the Elsholtz–Tao full text is already in the library as
  the ar5iv HTML.
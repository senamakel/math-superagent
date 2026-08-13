# Librarian cycle — 2026-08-13 (2): Buell acquisition failure; Rabern full text; DP07-adjacent tier

## What was attempted

Three genuine gaps were identified against `research/REQUESTS.md` and
`research/ROOT.md`, and each was pursued to a definite conclusion:

### 1. Buell, "A search for a magic hourglass" — permanent acquisition failure (recorded)

- The paper exists only at `http://www.multimagie.com/Buell.pdf` (101 Kb). No
  arXiv version, no alternate host (searched cse.sc.edu/~buell, CiteSeerX-style
  mirrors, ResearchGate — nothing).
- The PDF's text layer is corrupt: a direct fetch AND a Wayback Machine snapshot
  (`web.archive.org/web/2019id_/http://www.multimagie.com/Buell.pdf`) both
  return identical mojibake (broken DVI byte soup, no recoverable body). The
  file itself is bad, not the route.
- **Outcome**: full text unobtainable; claim `buell-hourglass-25e24-coprime`
  stays `asserted` (secondary-sourced). New claim
  `buell-fulltext-corrupt-unobtainable` records this so nobody re-fetches.
  The `25×10²⁴` hourglass bound continues to be quoted only with its
  coprimality caveat (Zimmermann–Loria relaxed it; Morgenstern 2014 re-search
  verified the no-solutions result on a wider pair-based range).

### 2. Rabern 2003 — full text now on disk (gap closed)

- Direct Rose-Hulman PDF (`cgi/viewcontent.cgi?article=1299&context=rhumj`) →
  403; Academia.edu → 403; the landing page (`rhumj/vol4/iss1/3/`) → abstract
  only.
- **Solved via the Wayback Machine snapshot of the exact viewcontent URL**
  (`web.archive.org/web/2023id_/https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1299&context=rhumj`):
  105,873 bytes fetched, 10.7 KB of clean Markdown — the complete 4-page paper
  with all five theorems (all entries odd; centre ≡1 mod 4 only; p≡3,5 mod 8 in
  a non-centre entry divides centre + opposite entry; no 3 mod 8 anywhere; no
  5 mod 8 on middle-side; p≡3 mod 4 in a corner divides the two non-adjacent
  middle-sides) and proofs.
- **Outcome**: `rabern-entry-prime-restrictions` upgraded from asserted to
  read-at-primary (`proved-where-stated`); old claim
  `rabern-fulltext-not-on-disk` replaced by `rabern-fulltext-on-disk`.
- **Lesson**: when a Digital Commons `viewcontent.cgi` PDF 403s, try the
  Wayback snapshot of the *same* URL before giving up — the archive preserves
  the file, not just the landing page. This is now the second file this cycle
  whose full text was only reachable that way.

### 3. David–Philippon IMRP 2007 (rpm006) — paywalled, DP07-adjacent tier added

- The open request `dp07-explicit-constant-for-e3-ap` needs DP07's explicit
  uniform-ML constant for powers of an elliptic curve. The paper is behind OUP:
  DOI, article-lookup HTML, and the direct PDF all 403. No arXiv preprint, no
  HAL deposit (exact-title HAL API query → zero hits), Philippon's/Jussieu
  profile is a stub without PDFs.
- **Outcome**: primary text not obtainable this cycle; recorded as
  `dp07-primary-text-not-obtainable-this-cycle`. Added instead the DP07-adjacent
  tier, both primary-authored:
  - **Viada, arXiv:0711.3533** (81.9 KB full text) — effective Bogomolov bound
    for subvarieties of E^g (E without CM) via the David–Philippon/Rémond
    constant chain; same ambient shape, different condition; corroborates the
    lane is tractable but does not give the DP07 constant.
  - **Galateau 2016 habilitation** (71.7 KB full text from HAL tel-02292193) —
    survey of Lehmer-type/effective Bogomolov theory including DP07.
- The request stays **open**; a future attempt should use institutional OUP
  access or library scans of IMRP 2007.

## Housekeeping

- **Auto-filed downloads clobbered two summaries this cycle** (the tool writes
  to `<name>.md` beside the source): `buell-search-for-magic-hourglass-1999.md`
  became the mojibake text and `rabern-properties-magic-squares-of-squares-
  2003.md` became a digest. Both were restored with accurate upgraded summaries
  (this was possible because the originals had been read earlier this cycle).
  Watch for this: after any download into `research/sources/`, verify the
  sibling summary still holds the prose summary, not a digest.
- FRONTIER.md accumulated citations from the new downloads (24 from Rabern, 8
  from Viada, 2 from the Jussieu stub, 1 from Galateau): mostly repeats of
  already-held sources (multimagie.com, Bremner, Robertson, Boyer) — no new
  canonical gap identified beyond those already recorded.

## Net state of the library

- **Gaps closed**: Rabern 2003 full text; effective-Bogomolov/E^g survey tier
  (Viada, Galateau).
- **Gaps confirmed open, with reasons**: Buell full text (corrupt at all hosts);
  DP07 primary text (OUP paywall, no preprint); nothing else.
- No new claim contradicts CONTEXT.md's Established section; the two new
  impossibility-relevant cautions (Buell bound narrow; DP07 constant not on
  disk) reinforce existing caveats.
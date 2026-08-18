# Librarian cycle handoff — 2026-08-19 continuation

## This cycle's verified additions (primary, first-lines-checked)

1. **Ilyashenko 1990, "Finiteness theorems for limit cycles"** — full text now
   held: `research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md`
   (RMS 45:2, 129-203; mathnet `rm4718`). Theorems I–IV, monodromy expansion,
   functional cochains, Phragmén–Lindelöf for cochains, superaccurate series.
   This is the Ilyashenko side of the finiteness theorem — the frontier's most
   cited unheld target (`10.1070/rm1990v045n02abeh002335`) is now on disk.

2. **Ilyashenko 2016, "Finiteness theorems for limit cycles: a digest of the
   revised proof"** (part 1 of 2) — full text now held:
   `research/sources/ilyashenko-2016-digest-revised-proof-fulltext.full.md`
   (Izvestiya: Math. 80:1, 50-112; mathnet `im8352`). Theorems 0.1–0.12 of the
   revised-proof digest. Part 2's mathnet ID was NOT found (citation walk and
   TOC attempts 404'd; not guessed).

3. **Wrong fetches neutralised** (all now carry a "WRONG FETCH / NOT THE PAPER"
   header, so they cannot be mis-cited):
   - `ilyashenko-1990-finiteness-theorems-rms-fulltext.full.md` = Rozanova's PDE
     paper (guessed paperid `rm4668`).
   - `fishkin-perturbed-center-mathnet.full.md` = symplectic-diffeomorphism
     abstract (wrong paper).
   - `fishkin-mathnet-search.full.md` = journal info page.
   - `fishkin-mathnet-vol71.full.md` = archive listing (and vol 71 is absent
     from the mathnet archive entirely).
   Incident documented at
   `research/findings/wrong-fetch-rozanova-mislabeled-ilyashenko-1990.md`.

## Open gaps (unchanged, now more precisely stated)

- **DRR ledger** (`complete-current-ledger-cb3d`, `dumortier-roussarie-rousseau-9c4f`):
  still unfillable from one source. Held picture: ≥89/121 closed by 2015,
  (I^1_6b),(H^3_13),(DI_2b) boundary-only, (H^3_14) open with Lu 2026
  (unrefereed) the sole claim, 11 degenerate open (Shan 2013).
- **Fishkin constants**: still abstract-level. AMS PDF rate-limited (429×3);
  mathnet has NO vol-71 text. The quoted constants (σ = exp(−10^73·κ − 2δ − 33),
  bound exp(exp(10^72·κ − 2δ − 33))) remain recall-level, unverified. Claim
  `fishkin-perturbed-center-quadratic-bound` stays unchecked. Next attempt
  should target the AMS free-archive PDF at a quiet hour, or the Russian
  original in Trudy MMO vol 71 via a citation that carries its mathnet ID.
- **2016 digest part 2**: exists ("first of two papers") but mathnet ID not
  found by legitimate means this cycle.
- **Écalle 1992 book / 1990 LNM chapter**: record-only (Springer/Hermann
  paywall); unchanged.

## Requests ledger — answered without new fetches

- Gasull–Santana structural status: held claims answer it.
- Best special-family Abelian-integral bound: held (BD linear-in-m, BNY
  double-exp, FTV2013, Gavrilov 2001).

## Memory

Cognee was down the entire cycle (health-check timeout on every recall and
remember call). Durable record = this handoff + `research/librarian-report-current-cycle.md`
+ the source files themselves. When memory recovers, store the two Ilyashenko
holdings and the mathnet-paperid lesson.

## Lesson for every future cycle

**Never guess a mathnet paperid or URL.** The paperid is not derivable from the
DOI. Get it from a citation that already carries `mathnet.ru/rus/rmNNNN`, then
verify the first lines of the landing text against the expected title before
treating a fetch as the paper. This cycle's guessed `rm4668` fetched Rozanova's
PDE paper; the guessed `im8353` and TOC URLs 404'd. Both failure modes are
avoided by the citation-first rule.

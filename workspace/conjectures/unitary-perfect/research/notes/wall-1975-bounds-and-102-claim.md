# What Wall (1975) actually bounds, and the missing anchor for "10^102"

## The claim in this workspace

GOAL.md, ROOT.md and CONTEXT.md all carry: **"Wall searched past 10^102 in
1975 (or Wall cleared the search past 10^102) and found no sixth."** This is the
reason the run's compute policy forbids numeric search.

## What the held primary text says

`research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md` (the full
Cambridge PDF, in the library) is the primary text for the fifth UPN. Its
actual bound is:

- p. 116: "we may restrict our attention here to A ≥ 11" (Subbarao 1970,
  see `research/notes/subbarao-1970-a-ge-11.md`);
- the working hypothesis throughout is **"N < W"** — i.e. the paper proves W
  is the next UPN *after 87360* by eliminating every candidate N < W, where
  **W = 146,361,946,186,458,562,560,000 ≈ 1.46 × 10^23**;
- the elimination uses `N < W` to cap the seed range ("N < W requires a < 38,
  since (3/2)·2^38 > W") and to bound the odd part (`s` products, `m < 20189`,
  `m < 133`, `m < 7` in the special cases).

**There is no "10^102" anywhere in Wall 1975.** The number 10^23 — not 10^102 —
is the actual scale of the paper's bound.

## Search for the anchor (this run)

- `exa_search` for `"unitary perfect" "10^102"` and variants: multiple dozons
  results, **none** in any held or searchable source. The only documents in
  the library that mention 10^102 are this run's own ROOT.md / GOAL.md /
  CONTEXT.md (a self-citation loop).
- The OEIS A002827 record (held, full text) states the known **stronger**
  bound 10^440 (Frei 1978, via OEIS comment, unverified against primary) and
  Goto's omega-based bound — but no 10^102.
- The OEIS-linked letters (Wall to Hagis 1972, Subbarao to Sloane 1974,
  `https://oeis.org/A002827/a002827.pdf` and `..._1.pdf`) are the most likely
  primary carriers of a large-search statement, but both are **scanned PDFs
  with no text layer** — download_document refuses them ("parsed as PDF but
  contained no extractable text"). No other carrier found.
- Guy, *Unsolved Problems in Number Theory*, §B3, is the other likely carrier
  (it is cited by MathWorld/Wikipedia/Erdős problems), but the book is
  paywalled.

## Status: UNVERIFIED / orphan claim

**The claim "Wall searched past 10^102" is currently an orphan statement**:
it appears in this run's own notes but is not attested in any held source.
It may be true (a 1972/1974 letter, or Guy §B3, or a later survey may state
it), but the library cannot currently evidence it. Per the workspace rules,
this means:

- nobody should re-derive or re-state it as a sourced fact;
- the **compute-policy consequence is unchanged** regardless: this container
  cannot reach a region a 1970s search did not clear, whether the cleared
  bound was 10^23 (Wall 1975) or 10^102 (unattested), because the 1975 bound
  alone is already beyond anything the container can enumerate;
- how to resolve: get Guy §B3 (1994/2004) or the Wall–Hagis letter (scanned,
  needs OCR) or the Lelechenko survey (403), or ask for a research request.

Recorded as an open research request (see REQUESTS.md row "Wall's search
bound primary statement").

## Related: EoM typo

The Encyclopedia of Mathematics "Unitary divisor" page (held) writes
90 = 2·3^3·5; the correct factorization is 2·3^2·5. Already recorded in
CONTEXT.md Contradictions.
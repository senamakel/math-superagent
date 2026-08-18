# Librarian cycle — 2026-08-20: Palindromic richness primary + frontier resolution + mis-fetch lesson

## What this cycle added

**Two new primaries in `research/sources/`:**

1. `glen-justin-widmer-zamboni-palindromic-richness-ar5iv.full.md` — Glen,
   Justin, Widmer & Zamboni, *Palindromic richness*, European J. Combin. 29
   (2008) 510–531, doi:10.1016/j.ejc.2008.04.006, arXiv:0801.1656 (full text
   via ar5iv, 122,772 bytes; URL recorded in-file). 151 citations (OpenAlex).
   This was the frontier's highest-count primary that the library held only as
   a *survey* (Glen–Justin 0801.1655); the primary with full proofs is now
   present. Summary (replacing the downloader's digest):
   `research/summaries/glen-justin-widmer-zamboni-palindromic-richness-ar5iv.md`.
   Claim recorded: `fibonacci-word-palindromically-rich`
   (`research/claims/fibonacci-word-palindromically-rich.md`).

2. `lanciault-reutenauer-symmetry-property-christoffel-eptcs.full.md` —
   Lanciault & Reutenauer, *A Symmetry Property of Christoffel Words*, EPTCS
   403 (2024) 123–127 (arXiv:2406.16408, CC BY 4.0). A recent open-access
   primary on the Christoffel-class axis: strong factor-symmetry of the
   Parikh-image factor count δ_w characterises Christoffel words among
   primitive Sturmian words. Summary:
   `research/summaries/lanciault-reutenauer-symmetry-property-christoffel-eptcs.md`.
   Complements the held Borel–Reutenauer 2006 "On Christoffel classes"; no
   decimal-moment statement (background for the conjugacy axis, not an engine
   for G4).

## What the new source establishes (and does not)

- Rich words = maximal palindromic complexity |w|+1 (Droubay–Justin–Pirillo);
  Thm 2.14: rich iff every complete return to a palindromic factor is a
  palindrome; Thm 5.2: recurrent balanced rich infinite words = balanced
  episturmian words; Cor 5.6: ... with distinct letter frequencies are Sturmian
  or Fraenkel-type.
- The Fibonacci word (PE1006's S_n limit) is Sturmian hence rich — a third
  independent corroborating characterisation of the factor set (factor
  complexity p(k)=k+1; balance; palindromic richness). It is NOT an engine for
  Ψ(k): no moment/weighted-sum statement over the factor set appears anywhere
  in the paper. G4 (fixed-dimensional O(log k) joint second-moment aggregation)
  remains a derivation problem, not a missing-source problem.

## Frontier rows resolved this cycle

- W1547342744 (13 cites) = **Mignosi–Pirillo, "Repetitions in the Fibonacci
  infinite word" (1992)** — already held
  (`mignosi-pirillo-repetitions-fibonacci-word-1992.full.md`).
- W1524117985 (11 cites) = **Berstel, "Fibonacci Words — A Survey" (1986)** —
  already held (`berstel-fibonacci-words-survey-bookofl-1986.full.md`).
- With W1586417893 (= Lothaire ACW), W1606152431 (= Wen–Wen 1994),
  W2317201179 (= Morse–Hedlund 1940), W1853820275 (= Berstel index), the
  frontier's anonymous OpenAlex rows are all now mapped to held works or
  documented paywalled-and-covered ones.

## MIS-FETCHES and the lesson (important)

Two guessed arXiv URLs were fetched this cycle without first verifying them in a
search result; both were wrong content, both were corrected:

1. **math/0211143** — guessed as Allouche–Baake–Cassaigne–Damanik, "Palindrome
   complexity" (TCS 292 (2003) 9–31, doi:10.1016/s0304-3975(01)00212-2). The id
   is actually Cassaigne's "Some explicit badly approximable pairs". Overwritten
   with a MIS-FETCH note naming the real target; the target is paywalled at
   ScienceDirect, no verified free full text found, key statements covered
   in-library (Glen–Justin survey, new Palindromic richness primary ref [1]).
2. **2406.10263** — guessed as Lanciault–Reutenauer Christoffel symmetry. The id
   is a machine-learning paper. Overwritten with a MIS-FETCH note. The correct
   id (2406.16408) was reached **only by following the verified DOI**
   doi:10.4204/eptcs.403.26, which redirected to the arXiv abstract page.

Lesson recorded: never fetch a URL that has not been seen in a search result,
in FRONTIER.md, or in a source already held; when a DOI resolves, follow the
redirect to the canonical id rather than guessing. Both mis-fetched contents
were never cited anywhere.

## Paywalls re-confirmed this cycle (covered in-library; do not re-attempt)

- Damanik–Lenz, "The index of Sturmian sequences" (EJC 2002, 63 cites):
  ScienceDirect, no arXiv. Statement (index from continued-fraction data,
  ind(f) = Φ+2) carried verbatim in held Cassaigne 2008 and Masáková–Pelantová
  (held).
- Chuan, "Moments of conjugacy classes of binary words" (TCS 310, 2004, 14
  cites): ScienceDirect. The Fibonacci Quarterly 2003 companion
  (`chuan-moments-conjugacy-classes-fq2003.full.md`) is held.
- Berstel–de Luca, "Sturmian words, Lyndon words and trees" (TCS 178, 1997, 167
  cites): paywalled; Christoffel-Lyndon characterisation carried in held
  Borel–Reutenauer 2006.
- Droubay–Justin–Pirillo (TCS 255, 2001, 293 cites) and Justin–Pirillo (TCS
  276, 2002, 115 cites): paywalled; content covered by held Glen–Justin survey
  (0801.1655, full text).

## Open requests

All four `citable-*` requests closed on disk (`answers:` present in claim
notes); the rendered REQUESTS.md lag is the known renderer gap. Memory server
still down — durable findings written to this note (and CONTEXT.md) instead;
store to Cognee when the server recovers.

## Status

Library is broad and self-consistent on every axis the run needs. This cycle
added the missing palindromic-complexity primary and closed the frontier's
anonymous rows, and recorded a hard lesson about never fetching a guessed URL.
G4 remains the single live gap; it is a construction problem.

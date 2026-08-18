# Librarian cycle — PE1006 (2026-08-19)

## What this cycle added

**Two new sources in `research/sources/`:**

1. `mignosi-number-factors-sturmian-1991.full.md` — Mignosi, "On the number of
   factors of Sturmian words", TCS 82 (1991) 71–84, doi:10.1016/0304-3975(91)90172-x.
   **Abstract/record only** (Unipa repository page); full text paywalled at
   ScienceDirect. Confirms the canonical enumeration of the *finite Sturmian
   language*: card(A_m) = 1 + Σ (m−i+1)φ(i) — distinct from the run's k+1
   single-Fibonacci-word count. This is the citation behind Berstel 2007,
   Berthé 1996, Lothaire ch. 2.
2. `deluca-combinatorial-property-fibonacci-words-1981.full.md` — de Luca,
   "A combinatorial property of the Fibonacci words", IPL 12 (1981) 193–195.
   **Full text obtained** (Séminaire Lotharingien scan, OCR-degraded). Theorems
   decoded and recorded: f_n has a palindrome left factor of length |f_n|−2
   (n>3); for n≥4, f_n = product of two uniquely-determined palindromes of
   lengths F(n−1)−2 and F(n−2)+2; unique-sequence characterisation for n>4.

## Frontier rows resolved this cycle

| Frontier row | Identity | Status |
|---|---|---|
| W2317201179 (17 cites) | Morse–Hedlund 1940 "Symbolic Dynamics II. Sturmian Trajectories" | Paywalled; documented NOT OBTAINED (summary `morse-hedlund-sturmian-trajectories-1940.md`); every result held in-library via Perrin–Restivo, Lothaire ch.2, Berstel surveys |
| W1853820275 (15 cites) | Berstel 1999 "On the Index of Sturmian Words" | Paywalled Festschrift, no preprint; tangential (index of powers, not our observable) |
| W1586417893 (25 cites) | Lothaire, *Algebraic Combinatorics on Words* | Already held (`lothaire-algebraic-combinatorics-words.full.md`) |
| W1606152431 (19 cites) | Wen–Wen 1994 "Some properties of the singular words of the Fibonacci word" | Already held (`wen-wen-singular-words-fibonacci-word-1994.full.md`) |
| W2006431506 (12 cites) | Coven 1974 "Sequences with minimal block growth II" | Bibliographic; tangential to PE1006 |

## Paywalls confirmed (403 / client-challenge; do not re-attempt)

- de Luca & De Luca 2006 "Some characterizations of finite Sturmian words"
  (ScienceDirect) — the author-page abstract is held
  (`summaries/deluca-deluca-finite-sturmian-2006.author-page.md`); results
  covered in-library by Perrin–Restivo note and Lothaire ch. 2.
- Droubay–Justin–Pirillo 2001 "Episturmian words..." (ScienceDirect) — covered
  by the held Glen–Justin survey and Berstel's episturmian survey.
- Fraenkel 1985 "Systems of Numeration" (JSTOR/T&F) — no Weizmann preprint;
  covered by the held Durand–Rigo, Frougny, and Ostrowski-numeration sources.
- Morse–Hedlund 1940 (JSTOR) — as above.
- Lothaire *Applied Combinatorics on Words* full text: only binary PostScript
  (mainappcow.ps.gz), unconvertible to Markdown by the downloader.

## Open requests (all four answered on disk)

- `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
  `citable-precise-statement-d2e7` — answered by claim
  `universal-euclidean-geometric-floor-sum` (fhq/OI-wiki/LOJ138/AtCoder anchors).
- `citable-statement-theorem-039a` — answered by claim
  `fibonacci-sturmian-complexity` (Perrin–Restivo + governing-Sturmian anchors).
  The rendered requests ledger lags the claim blocks (known renderer gap).

## Status

Library is broad and self-consistent on every axis the run needs: Sturmian
theory, factor location/enumeration, mechanical/floor-sum arithmetic,
numeration systems, and the universal-Euclidean primitive. Nothing this cycle
found is a new engine for G4; the gap remains the fixed-dimensional joint
second-moment aggregation, which is a derivation problem, not a missing-source
problem.

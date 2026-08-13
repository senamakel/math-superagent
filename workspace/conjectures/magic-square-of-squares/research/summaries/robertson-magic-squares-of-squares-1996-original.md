# File provenance correction: this is Kevin Brown's Mathpages page, NOT Robertson 1996

**Misleading filename.** This file was downloaded from `http://www.mathpages.com/home/kmath417.htm`
under the intention of fetching John P. Robertson's "Magic squares of squares"
(Mathematics Magazine 69(4) 1996, 289–293), but the URL is in fact **Kevin Brown's
Mathpages page "Magic Square of Squares"** — a tertiary recreational page that reproduces
the 3×3 magic-square parametrisation (centre `E = S/3`, the four lines through the centre
are 3-term APs) and states **Proposition 1**: a square whose centre is a sum of two squares
in at most four distinct ways cannot give the required outer-row/column sums.

## What this means for the run
- **Do not** treat this file as Robertson's original paper. Robertson 1996 is **not in this
  library**. It is paywalled at Taylor & Francis
  (`https://doi.org/10.1080/0025570X.1996.11996457`); no free PDF was obtainable this cycle.
- This content **duplicates** the already-held Brown source
  `research/summaries/brown-mathpages-magic-square-of-squares.md`, which is where claim
  `centre-five-representations` (asserted) is anchored. This misfiled copy adds nothing.
- The elliptic 2E(Q) reformulation attributed to Robertson is carried, verbatim, in
  Bremner 1999 ("On squares of squares", Acta Arith. 88), which IS in the library as
  `research/sources/bremner-on-squares-of-squares-1999.full.md`. That is the usable primary
  source for the reduction; Robertson's own 6-page note adds history but no theorem the run
  lacks (Bremner reproduces the reduction exactly).
- The genuine Robertson 1996 gap is **closed as unobtainable**: record it so nobody fetches
  mathpages again looking for it.

## Verdict
Fetching the true Robertson original is a **recorded dead end** (paywalled). The run's
`robertson-elliptic-reduction` claim remains anchored to Bremner 1999 §1, which states the
reduction in full ("a point (X,Y) in E(Q) lies in 2E(Q) iff {X, X±c} is a triple of rational
squares; ... the existence of a magic square of squares is equivalent to the existence of
three points in 2E(Q) with x-coordinates in arithmetic progression"), and attributes it to
Robertson [6]. The truncated `robertson-elliptic-reduction` claim should be completed from
Bremner 1999 §1, whose full text is on disk.

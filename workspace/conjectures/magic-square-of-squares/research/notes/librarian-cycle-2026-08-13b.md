# Librarian cycle — 2026-08-13 (frontier verification + Cain upgrade + Robertson dead end)

## Upgrades this cycle

**Cain full text secured — claim upgraded asserted → checked.**
Onno Cain, "Gaussian Integers, Rings, Finite Fields, and the Magic Square of Squares"
(arXiv:1908.03236, 2019) is now the complete 15-page PDF on disk at
`research/sources/cain-gaussian-integers-magic-square-of-squares-2019.full.md`.
Previously only the abstract page was held, and claim `cain-quartic-gaussian-reformulation`
was `asserted`. The full text confirms the reformulation is concrete and checkable:
- **Theorem 4.2:** a magic hourglass of squares exists iff there are `x,y,z ∈ Z[i]` with
  `Im[x²y²z²] = −4·Im[x²]·Im[y²]·Im[z²]`.
- This is the group law behind the run's own `f(m,n) = Im((m+ni)⁴)/4` Φ-reduction
  (verified: `verify_phi_doubling.py` IDENTITY VERIFIED; (9,2)→5544/7225, (4,3)→336/625).
- Separately, the finite-field census: **F_29 is the smallest non-Parker field** (Thm 5.1);
  all even-order fields and F_3..F_11,F_13,F_17,F_19,F_23,F_25,F_27 are Parker.
  This is a distinctness-over-F_q result, no bearing on Q.
Summary rewritten as a proper scholar note with claim block.

## Frontier top tier verified present

The two `cited-by-2` frontier rows whose identity was uncertain are confirmed already in
the library (my initial guess that they were absent was wrong — good, checked before
re-downloading):
- **arXiv:2103.01784** = Wu, "Non-invariance of the Brauer-Manin obstruction for surfaces"
  → `research/sources/wu-non-invariance-brauer-manin.full.md`, full paper, claim
  `wu-bm-noninvariance-under-base-change`, status proved (conditional on Stoll). ✓
- **arXiv:2310.12164** = Wolird, "A New Transformation of the Magic Square of Squares"
  → `research/sources/wolird-gaussian-transformation-magic-square-2023.full.md`. ✓
Both were fetched and their digests read to confirm identity; neither needed a second download.

## Recorded dead ends (so nobody retries)

- **Robertson 1996 original** ("Magic squares of squares", Mathematics Magazine 69(4)) is
  **not in the library** and is **paywalled** at Taylor & Francis
  (doi 10.1080/0025570X.1996.11996457); no free PDF. The run's `robertson-elliptic-reduction`
  claim (currently truncated) is fully stated in **Bremner 1999 §1** which IS on disk and
  reproduces Robertson's 2E(Q) reduction verbatim and attributes it to Robertson [6]:
  "a point (X,Y) in E(Q) lies in 2E(Q) iff {X, X±c} is a triple of rational squares; ...
  the existence of a magic square of squares is equivalent to the existence of three points
  in 2E(Q) with x-coordinates in arithmetic progression." Complete the claim from Bremner §1.
  A misfiled download (mathpages kmath417 = Kevin Brown, NOT Robertson) was corrected in
  `research/summaries/robertson-magic-squares-of-squares-1996-original.md`.
- **Rabern RHUMJ 2003 full text** — confirmed permanent 403 (not retried; contents already
  recovered from search-exposed body and cross-checked against checked congruences).

## Recent literature check (2023–2026)

The library already holds the genuine recent primary sources: Rome–Yamagishi 2024
(magic squares of powers), Hulse–Kuan–Lowry-Duda 2024 (APs of squares / multiple Dirichlet
series), Garcia-Fritz–Pasten 2026 (Bremner conjecture uniformity), Harrison–Mudgal–Schmidt
2026 (effective constant). A fresh web search surfaced only unrelated recreational
magic-square constructions and known classical facts (no four distinct squares in a single
AP — already implicit in the run's Morgenstern step-value theorems). Nothing new to add.

## Net state

The library is effectively complete for the run's active threads
(uniform-height-bound-elliptic-ap via GFP/HMS; Φ/additive-triple; four-AP obstruction;
extension-field MSS). REQUESTS.md has a single row, `exact-reduction-magic-507c`, marked
RESOLVED. No further gathering is warranted except against a stated, narrower gap in
REQUESTS.md.

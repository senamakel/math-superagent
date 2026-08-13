# Proth–Gilbreath conjecture: successive verification records — Colonna (CNRS), 2025–2026

<!-- source: https://www.lactamme.polytechnique.fr/Mosaic/descripteurs/GilbreathConjecture.01.Ang.html | full text: sources/colonna-proth-gilbreath-record.full.md -->

The current verification record page (collaboration with J.-P. Delahaye, Université de
Lille), updated through Aug 2026.

## What it establishes

- Verification of the Proth–Gilbreath conjecture extended far past Odlyzko's 10^13:
  - `G(π(2.8×10^14)) = 788` (11/08/2025)
  - `G(π(6.15×10^14)) = 800` (12/13/2025)
  - **`G(π(1.5×10^15)) = 800` (Jan 2026)** — current record, per Wikipedia's 2026 entry.
  - Here `G(π(x))` is the number of rows needed (the row-index k such that row k begins 1
    and is followed only by 0s and 2s), Odlyzko's G-function; `G(π(10^13)) = 635`.
- Page includes the process display for the first 64 primes, the theory section (the
  block-lemma reduction), the computation method (hardware + programs), absolute and
  relative record tables, and prime-gap analysis.
- Confirms the reduction (leading 1 + all-{0,2} tail ⇒ next rows all begin 1) as the
  engine of the whole verification programme, exactly as the run's ROOT.md and Odlyzko's
  paper state.

## Bearing on this run

- The **current** literature verification bound is **1.5×10^15 (G = 800)**, not 10^13.
  Any note that says "verified to 10^13 (Odlyzko)" is correct-but-outdated; the run's
  CONTEXT/Gaps should carry all four data points: 10^13 Odlyzko 1993, 10^14 Plouffe 2025,
  2.8×10^14 / 6.15×10^14 / 1.5×10^15 Colonna 2025–2026, and the run's own depth 1000.
- G(n) = the block length of the 635th/693rd/744th/800th row grows very slowly:
  635 → 800 across seven orders of magnitude of n — a strong empirical statement about how
  rarely regeneration is needed, consistent with the run's depth-1000 numbers.

## Source status

Primary record page by the verifier (J.-F. Colonna, CMAP/CNRS, in collaboration with J.-P.
Delahaye), retrieved this run; corroborated by Wikipedia's 2025–2026 entries. Not a
peer-reviewed paper but the verifier's own account of a reproducible computation.
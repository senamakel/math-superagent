# Proth–Gilbreath conjecture: verification record — Colonna, refresh 2026-08

<!-- source: https://www.lactamme.polytechnique.fr/Mosaic/descripteurs/GilbreathConjecture.01.Ang.html | full text: sources/colonna-proth-gilbreath-record-2026-08.full.md -->

Verifier's own record page (J.-F. Colonna, CMAP/CNRS École Polytechnique, with
J.-P. Delahaye), refreshed this cycle; page last updated 2026-08-12.

## What it establishes — the current verification record

Conjecture verified for **all primes < 1.5×10^15** (computation completed
2026-03-18; 57,600 values of G(π(x)) obtained). G(π(x)) = row index whose row
begins 1 and is followed only by 0s and 2s (Odlyzko's G).

- **Absolute records** (valid for all x ≤ the stated value):
  `G(π(10^14))=693` (10/05/2025, Colonna; independently confirmed by Plouffe
  10/07/2025), `G(π(1.1×10^14))=701`, `G(π(1.145×10^14))=744`, `G(π(2.2×10^14))=773`,
  `G(π(2.8×10^14))=788` (11/08/25), `G(π(6.15×10^14))=800` (12/13/25),
  `G(π(10^15))=800` (01/23/26), `G(π(1.0025×10^15))=806` (01/24/26),
  `G(π(1.2075×10^15))=809` (02/15/26), **`G(π(1.2125×10^15))=811` (02/15/26) — current absolute record**.
- **Relative records** (valid only in a vicinity of x): reach G = 1347, 1559,
  1935 near 5.7×10^18, 2.07×10^19, 6.02×10^27 (exploratory 128-bit
  computations). These are NOT a verification bound — the conjecture is
  verified only out to 1.5×10^15.
- Odlyzko's G table reproduced (10^2..10^13, G: 5,15,35,65,95,135,175,248,329,
  417,481,635), extended by 10^14 → 693, 10^15 → 800.
- The block-lemma reduction is stated explicitly (leading 1 + all-{0,2} tail
  ⇒ next N rows begin with 1) — same criterion as Odlyzko 1993 and the run's
  `odlyzko-block-lemma-exact`.
- Prime-gap table with G-values near record gaps, through 128-bit gaps (1998 at
  9.2×10^25+ region).

## Footnote [04]: deletion counterexample — bounded-gap LEFT-edge failure

Colonna's "things are not as simple" note: remove **7** (or 5, or 11) from the
prime list and the leading-1 property fails within a few rows while all gaps
stay small. Displayed triangle for X = (2,3,5,11,13,17,19) (gaps
1,2,6,2,4,2 ≤ 6):

```
A1: 1 2 6 2 4 2
A2: 1 4 4 2 2        <- second entry 4
A3: 3 0 2 0          <- leading 3
A4: 3 2 2            <- leading 3
A5: 1 0              <- leading 1 only here
```

Hand-checked: for (2,3,5,11) the failure is already forced — A₂(1)=4, A₃(0)=3.
Deleting 5 instead: (2,3,7,11,...), gaps ≤ 4, gives A₂=(3,0,2,2,...) — leading 3
at row 2. So **the deterministic class "2 followed by odds with gaps ≤ g" has a
counterexample at g = 4** (second entry 4 ⇒ leading entry 3), killing that
general-class theorem for any g ≥ 4; only the g = 2 (consecutive-odds) case is
proved (run's own `notes/reduction.md`). Recorded as claim
`colonna-deletion-left-edge-failure` in `notes/library-state.md`.

## Source status

Primary verifier account (CNRS), corroborated by Plouffe's arXiv:2510.06688
(10^14, held) and by Wikipedia's 2025–2026 entries (held). Not peer-reviewed
but the verifier's own reproducible computation, independently confirmed at
10^14 by Plouffe's independent method.
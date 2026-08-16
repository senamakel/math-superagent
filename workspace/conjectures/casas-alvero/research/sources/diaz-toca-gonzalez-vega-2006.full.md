# NOT OBTAINED: Diaz-Toca & Gonzalez-Vega, "On analyzing a conjecture about univariate polynomials and their roots by using Maple" (2006)

This is the origin reference for the **verification bound** claim (CA verified
for degree ≤ 7, and degree 8, by Gröbner over ℚ). It is a conference
proceedings volume (Maple Conference 2006, Waterloo, pp. 81–98; also A3L 2005,
Passau, "On a Conjecture About Univariate Polynomials and Their Roots",
pp. 83–90, Books on Demand) and no open PDF is available from any searchable
source.

## Why it was sought

ROOT.md lists "computer verification: degree ≤ 7 by Diaz-Toca & Gonzalez-Vega
(2006); degree 8 by the same authors". The origin paper was not in the library.

## How the claim is supported WITHOUT the origin paper

The claim **does not depend** on this origin paper — it is corroborated by two
independently held primary sources:

1. **Draisma–de Jong survey** (held,
   `research/sources/draisma_dejong2011_survey.full.md`, ~line 3363): "this
   analysis for B ≤ 7 by Diaz-Toca and Gonzalez-Vega [3] constituted the first
   substantial progress on the Casas-Alvero conjecture."
2. **Castryck–Laterveer–Ounaïes 2012** (held, `castryck2012_degree12_html`):
   "In 2006, this was used by Diaz-Toca and Gonzalez-Vega to verify the
   conjecture for d ≤ 7 [5]."

So the verification-bound claim is **asserted-by-two-held-sources**, and the
run has additionally independently reproduced it via the Gröbner-based oracle
(see `code/` and `research/threads/computational-boundary.md`).

## Why the search stopped here

The paper is paywalled/not-digitized and is tertiary to a claim already doubly
corroborated. Not worth further chasing. If a later pass needs the *explicit
algorithm* (not the fact of verification), the Castryck et al. paper improves
on it and is held in full.

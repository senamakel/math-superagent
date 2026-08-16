# Greaves, Koolen, Park — "Improving the Delsarte bound" (arXiv:2012.09391)

<!-- source: https://arxiv.org/pdf/2012.09391 | converted from PDF -->

**Full text:** `research/sources/greaves-koolen-park-delsarte-bound.full.md`

## What it establishes

Studies the order of a maximal clique in an **amply regular** graph with fixed
smallest eigenvalue, via a vertex adjacent to some (not all) vertices of a
maximal clique. Main consequences:

1. **Delsarte-clique dichotomy.** If a strongly regular graph contains a
   *Delsarte clique* (order ≈ 1 + k/m for smallest eigenvalue −m), then µ is
   either small or large (Prop 3.3, under k ≥ m²(4m−5)).
2. **Maximal-clique cubic.** A cubic polynomial M_Γ(c) (the "maximal-clique
   polynomial") forces a maximal clique to be either small or large under
   stated assumptions — the sign of M_Γ on the guaranteed-clique / Delsarte /
   claw endpoints gives a contradiction.
3. **Theorem 4.3 (infinite family excluded).** For every m ≥ 4, there are **no**
   SRGs with the parameter family
   v = 1 + k + k(k−λ−1)/µ,
   k = (m+1)(m(2−µ)+2λ)/2 + 1,
   λ = ((m−3)⁵+15(m−3)⁴+91(m−3)³+283(m−3)²+226(m−3)+148)/2,
   µ = (m−3)³ + 10(m−3)² + 33(m−3) + 38.
   Proof: set ¯c = m+2; shows (¯c choose 2)(µ−1) < ¯c(λ+1)−k, so by Lemma 4.2
   the graph contains a clique of order ≥ 2+λ−m(µ−1); then the cubic M_Γ
   contradicts its own endpoint signs.
4. **Appendix — explicit nonexistence tables** for smallest eigenvalue
   −4, −5, −6, −7 (feasible parameter sets with no SRG):
   - **−4 table (Table 1):** only (v,k,λ,µ) = (23276,1330,372),
     (25025,1426,399), (27455,1696,480), (38875,2046,569).
   - −5 table: v up to 485815; −6, −7 tables: v up to ~10⁷.

## Bearing on (99,14,1,2)

- **(99,14,1,2) is in NONE of the four tables.** Its parameter set appears
  nowhere; the −4 table holds only the four large-v sets above. So the
  GKP Delsarte/claw/cubic repertoire **does not rule out 99** — confirmed by
  direct table inspection (see `research/notes/gkp-delsarte-neg4-tables.md`,
  claim `gkp-delsarte-neg4-tables-do-not-rule-out-99`).
- This was already flagged in `research/approaches/least-eigenvalue-minus-4-structure.md`
  from the abstract; it is now checked against the held full text.
- The −4 gate remains the strongest 99-specific structural hypothesis in the
  library (rook −2, BvLS −5, 99 −4), but the GKP tables are not the weapon
  that bites at 99.

## Why it matters here
The `least-eigenvalue-minus-4-structure` approach (grounded, not refuted) had
this paper as its named usable "sound remaining weapon." The library now holds
the full text and the direct verification that 99 is not among its excluded
sets. The live remainder is the geometric-SRG classification at smallest
eigenvalue −4 (van Dam / Koolen–Yang / Spence), not the Delsarte/claw tables.

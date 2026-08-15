# Duffus–Sands–Woodrow (1985): On the chromatic number of the product of graphs

**Subject:** The primary survey/reference for how chromatic number behaves under the
common graph-product operations (Cartesian, tensor/direct), the framework the run's
combination engine sits in.

## Source

- D. Duffus, B. Sands, R. E. Woodrow, *On the chromatic number of the product of
  graphs*, J. Graph Theory 9 (1985) 487–495. DOI 10.1002/jgt.3190090409.
- Retrieved via `read_sources` per the run's network boundary.

## Statements

- **Cartesian product** `G □ H`: `chi(G □ H) <= chi(G)·chi(H)`, and
  `chi(G □ H) >= max{chi(G), chi(H)}`. It can be strictly larger than the max
  depending on structure.
- **Tensor/direct product** `G × H`: `chi(G × H) <= min{chi(G), chi(H)}` (projection
  colouring), and in general the exact value is structure-dependent; the paper
  records instances and bounds.
- Bibliographically fixes: El-Zahar–Sauer (tensor product of two 4-chromatic graphs
  is 4, Combinatorica 1985); the Hedetniemi-conjecture lineage.

## Why it matters here

This and its two companion sources (El-Zahar–Sauer, Tardif) are the **primary tier
for the construction engine's chromatic side**. The run's central open question —
can combining 4-colourable unit-distance graphs force chi > 4 — is exactly the
product/combination-chromatic-number question, specialised to unit-distance geometry.
The graph-product theory is the known-answer baseline: generic combinations of
4-chromatic graphs stay at 4, so any chi>4 route must come from geometric rigidity,
not generic product structure. Confirmed by the run's own measured fact that
Moser+Moser (first Minkowski sum of two 4-chromatic spindles) is 4-colourable.

## Basis and status

- Statements = sourced (retrieved from the article record; classical graph products).
- Not re-derived here; general graph theory.
- Status: **asserted-by-source**.

## Claim block

```claim
id: duffus-sands-woodrow-product-chromatic
statement: For Cartesian product, max{chi(G),chi(H)} <= chi(G □ H) <= chi(G)chi(H);
  for tensor product, chi(G × H) <= min{chi(G),chi(H)}. Exact tensor-product values
  are structure-dependent; the tensor product of two 4-chromatic graphs is 4
  (El-Zahar–Sauer).
hypotheses: G, H finite simple graphs; □ = Cartesian, × = tensor.
holds-here: PARTIAL — framework for the run's combination engine; the run uses
  Minkowski sums of unit-distance graphs, not generic products, so the bounds
  are the known-answer baseline, not the unit-distance result itself.
status: asserted-by-source (classical; not re-derived here).
bearing: the chromatic-behaviour baseline for the construction engine — names
  why generic combinations of 4-colourable graphs stay at chi<=4, framing the
  requirement that any chi>4 construction needs geometric (unit-distance)
  rigidity rather than product structure.
anchor: research/sources/duffus-sands-woodrow-1985-product-chromatic.md
falsifies: a generic product/Minkowski-sum operation on 4-chromatic graphs
  producing chi>4 — none known; the geometric analogue is the open computation.
```

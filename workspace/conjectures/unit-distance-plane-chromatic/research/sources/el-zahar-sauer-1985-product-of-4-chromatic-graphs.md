# El-Zahar & Sauer (1985): the chromatic number of the product of two 4-chromatic graphs is 4

**Subject:** The categorical (tensor/direct) product of graphs and its chromatically
behavior — the framework against which the run's core open question ("can combining
4-colourable unit-distance graphs force chromatic number > 4?") is set.

## Source

- M. H. El-Zahar, N. Sauer, *The chromatic number of the product of two 4-chromatic
  graphs is 4*, Combinatorica 5 (1985) 121–126. DOI 10.1007/bf02579374.
- Retrieved via `read_sources`/`exa_search` (network boundary blocks direct fetch);
  statement + attribution established from the article's record and the surveys that
  state it (Tardif 2001; Duffus–Sands–Woodrow 1985 bibliography).

## Statement

**Theorem (El-Zahar–Sauer 1985).** For any two finite graphs `G` and `H` with
`chi(G) = chi(H) = 4`, the categorical (tensor/direct) product `G × H` has
`chi(G × H) = 4`.

Here the tensor product has vertex set `V(G) × V(H)` with `(g1,h1) ~ (g2,h2)` iff
`g1 ~ g2` in `G` AND `h1 ~ h2` in `H`.

## Why it matters here

This is the **negative control** for the run's construction engine. The run's central
open question (`REQUESTS` row) is whether combining 4-colourable unit-distance graphs
(via Minkowski sums, products, spindlings) can force `chi > 4`. This theorem says the
**tensor product** of two 4-chromatic graphs stays at 4 — combining colourable graphs
does not automatically buy chromatic number. It bounds what any construction route
must overcome: the rigidity has to come from the *geometry* (the unit-distance
embedding, Minkowski-sum coincidences), not from generic product operations, which
are known not to raise χ in this range. It is also the special case of Hedetniemi-type
behaviour that was settled; it is NOT yet known whether there is any n such that the
product of two n-chromatic graphs has chromatic number at least 5.

The run's own measured facts are consistent with this: Moser+Moser (a first Minkowski
sum of two 4-chromatic spindles) is 4-colourable with no forced monochromatic pair.
The graph-product theory here confirms the structural reason: product/combination
operations that do not encode geometry do not raise chromatic number.

## Basis and status

- Statement = sourced (retrieved verbatim, consistent across El-Zahar–Sauer record,
  Tardif 2001, Duffus 2005).
- Not re-derived computationally here (general graph theory, not unit-distance).
- Status: **asserted-by-source**; the run's own oracle verifies the unit-distance
  analogue on instances.

## Claim block

```claim
id: el-zahar-sauer-product-4chromatic
statement: For any two finite graphs G, H with chi(G) = chi(H) = 4, the
  categorical (tensor/direct) product G × H has chi(G × H) = 4.
hypotheses: G, H finite simple graphs with chromatic number 4; product is the
  tensor product ((g1,h1) ~ (g2,h2) iff g1~g2 and h1~h2).
holds-here: PARTIAL — the run's candidates are unit-distance graphs, not
  arbitrary graphs, and the run uses Minkowski sums (not tensor products), so
  the theorem does not apply verbatim. It is the analogous negative result:
  generic product/combination of 4-chromatic graphs does not raise chi.
status: asserted-by-source (classical result, 124 citations, not re-derived here).
bearing: negative control for the construction engine — names the fact that
  combining 4-colourable graphs via product operations does not automatically
  buy chi>4; the rigidity must come from geometry (Minkowski coincidences).
anchor: research/sources/el-zahar-sauer-1985-product-of-4-chromatic-graphs.md
falsifies: a pair of 4-chromatic graphs (or unit-distance graphs) whose tensor
  product (or Minkowski sum) has chi(G×H) > 4 — none is known in this range;
  the geometric analogue is exactly the run's open computation.
```

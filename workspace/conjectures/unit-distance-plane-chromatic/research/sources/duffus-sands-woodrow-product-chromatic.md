# On the chromatic number of the product of graphs — Duffus, Sands, Woodrow 1985

**Source:** doi:10.1002/jgt.3190090409
**Authors:** Dwight Duffus, Bill Sands, Robert Woodrow, J. Graph Theory 9 (1985)
**Full text:** not on disk; read via read_sources.

## What this establishes (technique relevance to Minkowski sums)

The chromatic number of graph products is tightly connected to factors:
Hedetniemi's conjecture (1966) claimed χ(G × H) = max{χ(G), χ(H)} for the
tensor (direct/categorical) product. The conjecture is dis-proved in general,
but important special cases hold:

- **El-Zahar–Sauer (1985):** the product of two 4-chromatic graphs is
  4-chromatic. This is directly relevant: if a Minkowski-sum construction gives
  a product-like adjacency structure, then two 4-chromatic factors can still
  produce only a 4-chromatic product — i.e. chromatic number does not compound
  under the tensor product in the 4-chromatic range that matters here.
- Related bounds and refinements for products of graphs, including the
  product-over-many-factors regime.

## Why it matters here

The Minkowski sum A + B of unit-distance graphs produces a graph whose edges can
arise from **many different pairs** (a + b ~ a' + b' in various ways). The exact
edge structure of A + B is NOT the tensor product of A and B, but product-like
chromatic behaviour is a warning: the operation does not automatically compound
chromatic number. Any claimed lower bound from a Minkowski-sum construction must
be analysed on the actual edge set, not assumed to inherit factor chromatic
numbers.

```claim
id: product-chromatic-4chromatic
statement: The tensor product of two 4-chromatic graphs is 4-chromatic (El-Zahar–Sauer 1985). More generally, product chromatic numbers do not simply compound factors.
hypotheses: Tensor (direct) product of graphs; factors 4-chromatic.
holds-here: true as a blocker-check — Minkowski sums of 4-chromatic unit-distance graphs do NOT automatically produce non-4-colourable graphs; the actual edge structure must be analysed.
status: sourced (survey summary; El-Zahar–Sauer result cited)
bearing: Warns that the Minkowski-sum engine, as a naive way to compound rigidity/chromatic number, can fail; the edge structure of A+B is what must be computed, not inherited.
anchor: research/sources/duffus-sands-woodrow-product-chromatic.md
```

## Note on download

Full text blocked at network layer. Content from read_sources summary.
Status: **sourced via read_sources; full text not on disk.**
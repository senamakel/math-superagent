# Tardif (2001): chromatic number of a product ≥ ½ min fractional chromatic numbers

**Subject:** A universal lower bound for the chromatic number of a categorical
product in terms of the fractional chromatic numbers of its factors — the positive
side of the product theory, complementing El-Zahar–Sauer.

## Source

- C. Tardif, *The chromatic number of the product of two graphs is at least half the
  minimum of the fractional chromatic numbers of the factors*, Comment. Math. Univ.
  Carolinae 42 (2001) 353–355. DML-CZ: http://hdl.handle.net/10338.dmlcz/119249
- Retrieved via `read_sources` per the run's network boundary.

## Statement

For any two graphs `G` and `H`,

```
chi(G × H)  >=  (1/2) · min{ chi_f(G), chi_f(H) }
```

where `×` is the categorical (tensor/direct) product and `chi_f` the fractional
chromatic number.

The paper situates this against Hedetniemi's conjecture `chi(G × H) = min{chi(G),chi(H)}`
(Hedetniemi 1966), which holds for 4-chromatic factors (El-Zahar–Sauer) and was
eventually disproved asymptotically (Shitov 2019; then Zhu and others). Tardif's bound
is the fractional-relaxation counterpart: universal but weaker.

## Why it matters here

This gives the run a **lower-bound vocabulary** for the product route: even where an
exact formula for `chi(G×H)` fails, the fractional relaxation supplies a guaranteed
lower bound. For the run's construction engine (Minkowski sums / products of
unit-distance graphs), this is the closest sourced statement of "combining graphs
cannot arbitrarily crush chromatic number." It is technique — how chromatic numbers
behave under products — not a published answer to `problem.md`.

## Basis and status

- Statement = sourced (retrieved verbatim from the article record).
- Not re-derived here; general graph theory.
- Status: **asserted-by-source**.

## Claim block

```claim
id: tardif-product-fractional-lower-bound
statement: For any two graphs G, H, chi(G × H) >= (1/2) min{ chi_f(G), chi_f(H) },
  where × is the categorical product and chi_f the fractional chromatic number.
hypotheses: G, H finite simple graphs; × = tensor/categorical product.
holds-here: PARTIAL — the run's candidates are unit-distance graphs and the
  run uses Minkowski sums, not tensor products; the theorem is the
  product-theory backbone for the construction engine's chromatic behaviour.
status: asserted-by-source (Tardif 2001; not re-derived here).
bearing: positive control — combining graphs via products preserves at least
  half the smaller fractional chromatic number; frames what product/Minkowski
  routes can and cannot buy.
anchor: research/sources/tardif-2001-product-fractional-chromatic.md
falsifies: a pair of graphs whose categorical product has chi < (1/2)
  min{chi_f(G),chi_f(H)} — would contradict the theorem; none exists.
```

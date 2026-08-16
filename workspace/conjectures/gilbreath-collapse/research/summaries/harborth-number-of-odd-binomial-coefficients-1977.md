# Number of odd binomial coefficients — Harborth (Proc. AMS 62, 1977)

Source: https://www.ams.org/journals/proc/1977-062-01/S0002-9939-1977-0429714-1/S0002-9939-1977-0429714-1.pdf
Full text: [[harborth-number-of-odd-binomial-coefficients-1977.full]]

## What it establishes

Let `F(n)` be the number of odd entries in the first `n` rows of Pascal's triangle, and
`θ = log3/log2 = 1.58496...`. Then
- **Theorem 1.** `α = limsup F(n)/n^θ = 1`.
- **Theorem 2.** `β = liminf F(n)/n^θ = 0.812556...` (the `liminf` over special rows).

## Bearing — MARGINAL

This is the asymptotic count of odd entries in the whole triangle — a global density
result. It confirms that mod-2 Pascal rows are sparse on average, consistent with item 4
(the fold rows are small down-sets, so symmetric differences are small). It says nothing
about *which* sets `M_d △ M_{d'}` are. The `θ = log3/log2` exponent is a density fact,
not a per-row structure fact. Keep only as background confirming sparsity; not load-bearing.

```claim
id: harborth-density
statement: F(n) ~ n^{log_2 3} up to lim-sup 1 and lim-inf 0.812556; odd entries of the
  first n Pascal rows are sparse.
hypotheses: n -> infinity
holds-here: yes (background: fold rows are small down-sets for typical d)
status: proved
bearing: qualitative confirmation that symmetric differences of down-sets concentrate on
  small sizes (supports item 4), but no structure on which sets occur
anchor: research/sources/harborth-number-of-odd-binomial-coefficients-1977.full.md
```

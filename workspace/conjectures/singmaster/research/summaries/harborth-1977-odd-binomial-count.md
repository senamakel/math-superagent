# Harborth, "Number of odd binomial coefficients" (1977)

Source: https://doi.org/10.2307/2041936 (Proc. Amer. Math. Soc. 62 (1977) 19–22)
Full text: `research/sources/harborth-1977-odd-binomial-count.full.md`.

## What it establishes

Let `F(n)` be the number of odd binomial coefficients in the first `n` rows of
Pascal's triangle, and `θ = (log 3)/(log 2) = 1.584962…`. Then:

- **Theorem 1:** `lim sup_{n→∞} F(n)/n^θ = 1`.
- **Theorem 2:** `lim inf_{n→∞} F(n)/n^θ = β = 0.812556…` (a specific
  characterizing value given in the paper, refining the earlier Stolarsky bounds
  `0.72 ≤ β ≤ (9/7)(3/4)^θ ≈ 0.815`).

Almost all binomial coefficients are even (`F(n)/n² → 0`).

Connection to the odd-entries structure (Lucas mod 2): the number of odd entries
in row `n` is `2^{a(n)}` where `a(n)` is the number of 1s in the binary expansion
of `n`; `F(n) = Σ_{r=0}^{n−1} 2^{a(r)}`. Harborth's proof uses the
`F(2^m + x) = F(2^m) + 2·F(x)` recursion from binary decomposition.

## Bearing for this run

- The odd-only Pascal triangle is exactly the support of the adopted
  `binary-lucas-submask` thread: every representation of an *odd* `a` must have
  `k ⊆ n` bitwise (Lucas mod 2). This paper is the canonical density result on
  that triangle's support: the odd entries are sparse (about `n^θ` with
  `θ=1.585`, i.e. far fewer than the `n²/2` entries), and the row-`n` count `2^{a(n)}`
  is the size of the submask set of `n`.
- Harborth's `2^{a(n)}` is the exact number of `k` with `k ⊆ n`, so the submask
  constraint's sparsity is quantified precisely by this source.
- Not a bound on `N(a)` by itself: the constraint `k ⊆ n` says *which pairs* can
  represent an odd `a`, not how many can land on the same integer.

```claim
id: harborth-1977-odd-count-density
statement: Let F(n) be the number of odd entries in the first n rows of Pascal's
  triangle and θ=(log 3)/(log 2)=1.584962…. Then limsup F(n)/n^θ = 1 and
  liminf F(n)/n^θ = 0.812556…, so the odd-entry support is sparse (F(n)≈n^θ).
  The number of odd entries in row n is 2^{a(n)}, a(n) the binary digit sum of n.
hypotheses: none (a theorem about binomial coefficients mod 2).
holds-here: yes — the odd-only triangle is the support of every odd-valued
  representation, and 2^{a(n)} is exactly the number of k with k ⊆ n (the size of
  the submask set that the adopted binary-lucas-submask thread sums over).
status: asserted (source's theorem; the recursion F(2^m+x)=F(2^m)+2F(x) and the
  values 1 and 0.812556… are quoted from the held primary but not independently
  re-derived here).
bearing: quantifies the sparsity of the odd-only support that the
  binary-lucas-submask thread relies on; the row count 2^{a(n)} is the exact
  submask-set cardinality.
anchor: research/sources/harborth-1977-odd-binomial-count.full.md
```

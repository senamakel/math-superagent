# Kulkov, "Dirichlet convolution and fast prefix sums" (Codeforces blog)

Source: https://codeforces.com/blog/entry/117635 — full text at
`research/sources/kulkov-dirichlet-convolution-fast-prefix-sums.full.md`
[[kulkov-dirichlet-convolution-fast-prefix-sums.full]]

## What this source establishes

A general framework (adamant / Nisiyama_Suzune, Codeforces) for computing
prefix sums of multiplicative functions by Dirichlet convolution and the
hyperbola method, with floor-quotient grouping.

**Claim.** Let h = f ∗ g, and let the prefix sums F(⌊n/k⌋), G(⌊n/k⌋) be known
for all possible arguments. Then the prefix sum H(n) can be computed in
O(√n); and H(⌊n/k⌋) for all possible arguments in O(n^{2/3}).

**Claim.** If F(⌊n/k⌋) is available for all possible arguments in O(n^{2/3}),
then the prefix sums of the Dirichlet inverse f^{−1} are available for all
possible arguments in O(n^{2/3}}.

The blog covers choosing a better splitting point, adding precomputation, and
the Dirichlet inverse, with code for the floor-quotient enumeration.

## Hypotheses

Multiplicative/completely multiplicative functions on N; the standard floor-
quotient machinery. Applies to φ = μ ∗ id (the totient summatory) — this is
exactly the machinery behind the Θ(n^{2/3}) summatory-totient algorithms.

## What it lets this run do

- Justifies the sublinear complexity tier of the alternative Φ(10⁸) routes
  (Brown 2025; the Gauss-recursion approach in
  `research/approaches/dirichlet-hyperbola-gauss-2-3.md`): context, not the
  adopted method — the run computes Φ(10⁸) by a direct sieve at n = 10⁸.

## What it does not settle

- No numerical values; no orchard geometry; no closed form for Φ.

## Claims

None — algorithmic context only.

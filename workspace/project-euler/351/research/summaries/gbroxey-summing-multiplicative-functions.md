# gbroxey, "Summing multiplicative functions" (blog, 2023)

Source: https://gbroxey.github.io/blog/2023/04/30/mult-sum-1.html — full text
at `research/sources/gbroxey-summing-multiplicative-functions.full.md`
[[gbroxey-summing-multiplicative-functions.full]]

## What this source establishes

A tutorial collection of methods for computing partial sums of multiplicative
functions: the naive method, the Dirichlet hyperbola method, linear sieving,
summing generalized divisor functions D_k(x) iteratively, summing μ and φ —
Mertens in O(x^{3/4}) and O(x^{2/3}) — and the "powerful numbers" trick with
Bell series and the Min-25 sieve.

**Relevant method.** Mertens M(x) in O(x^{2/3}) via the floor-quotient /
hyperbola recursion; the section "Doing It For φ?" notes the totient summatory
is handled the same way (φ = μ ∗ id), i.e. Φ(x) in O(x^{2/3}) with a μ prefix
sum — the same complexity class as Brown's Algorithm 1 (arXiv:2506.07386).

## Hypotheses

Multiplicative functions on N; standard floor-quotient grouping. Holds here.

## What it lets this run do

- Corroborates, from a computational-number-theory blog, the O(n^{2/3})
  floor-grouped route to Φ(10⁸) that is the independent-verification
  context of the run. Not the adopted method (direct sieve).

## What it does not settle

- No numerical values at 10⁸; no orchard geometry; blog is not peer-reviewed
  (secondary source).

## Claims

None — algorithmic context only.

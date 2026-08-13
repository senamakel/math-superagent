# Tsz Ho Chan, "On the divisibility of products of consecutive integers" (2024)

Source: https://arxiv.org/pdf/2408.01306 (arXiv:2408.01306).
Full text: `research/sources/chan-equal-products-2024.full.md` (full text, with a
digest in research/summaries/).

## What it establishes

This is an *adjacent* result, not a direct contribution to Singmaster. It studies
when a product of three consecutive integers divides another:

- **Theorem 1**: `b(b+1)(b+2) = 2a(a+1)(a+2)` has only the solution (a,b)=(3,4).
- **Theorem 2**: if `a(a+l)(a+2l) | b(b+l)(b+2l)` for sufficiently large a<b (in
  terms of l), there is a gap `b ≫ a (log a)^{1/6} (log log a)^{1/3}`.
- Theorems 3–4: for `a²(a²+l) | b²(b²+l)` a similar gap, with an abc-conditional
  improvement.

Method: effective Liouville–Baker–Feldman theorem (linear forms in logarithms).

## Relevance / place in this library

The equality-of-products results (SST 1995, Mordell, Boyd–Kisilevsky) are the
primary tools for the `C(x,k1)=C(y,k2)` collision family. This Chan paper is
about *divisibility with a multiplicative factor*, not equality, so it does not
bear directly on multiplicity bounds. It is filed as an adjacent/problematically-
neighbouring result and as an example of an *effective* (Baker-type) height/gap
bound being extracted from these product equations — the same method family the
run's "effective, non-uniform" Diophantine route would deploy. Not relied on by
any claim in this run.

```claim
id: chan-divisibility-gap
statement: Chan 2024 (arXiv:2408.01306): if a(a+l)(a+2l) | b(b+l)(b+2l) with a<b
  sufficiently large in terms of l, then b ≫_l a(log a)^{1/6}(log log a)^{1/3};
  and b(b+1)(b+2)=2a(a+1)(a+2) has only (3,4). Method: effective
  Liouville-Baker-Feldman (linear forms in logarithms).
hypotheses: divisibility (not equality) of products of consecutive AP terms; a
  sufficiently large depending on l.
holds-here: N/A — adjacent problem (divisibility, not binomial-coefficient
  multiplicity); filed for breadth, not load-bearing.
status: asserted
bearing: example of the effective Baker-type method; does not bear on N(a) bounds.
anchor: research/sources/chan-equal-products-2024.full.md
```

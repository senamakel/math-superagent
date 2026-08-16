# Order-K witness decision: K*(n) via CP-SAT

## The decision

For each (n, K): does there exist a pair h, h' ∈ F₂ⁿ with equal order-K
correlation vectors C₁..C_K (where C_m is the histogram of length-(m+1)
binary words over overlapping windows) but S²(h) ≠ S²(h')?  K*(n) is the
largest such K.  We decide existence with CP-SAT; for each n the maximal K
is found by bisection / downward probe (witness monotonicity: a pair equal at
order K is also equal at lower orders, so "∃ equal-C_K pair with different
S²" need not be monotone in K — but the *largest K with a witness* is found by
probing each K and checking S²-constant on every C_K-fiber, equivalently no
witness pair).

## The reduction (to be verified by oracle)

equal C₁..C_K   ⇔   equal C_K (word-histogram) AND equal length-K prefix.

Reasoning: C_K is the traversal multiset of the level-K de Bruijn graph.
Node out-multisets of the walk give C_{K-1}; given equal C_K and equal start
word (forced by equal prefix), the whole history is forced.  Let the oracle
verify this directly: check that "group by (C_K, prefix_K)" partitions
strings with the same granularity as "group by (C_1..C_K)".

## Encoding (per n)

- vars h_j, h'_j ∈ {0,1}, j = 0..n−1  (two binary strings)
- window integers w_p = (h_p…h_{p+K})₂ ∈ [0, 2^{K+1}), p = 0..n−K−1
  (n−K windows), same for h'
- multiset equality: sort both sets with a sorting network, force elementwise
  equal
- prefix equality: h_j == h'_j for j < K
- S via canonical T(n,d) = XOR over submasks (parity as sum mod 2); nu2 =
  Σ_d T_d; S = (n−2) − 2·nu2; constrain S²(h) ≠ S²(h')  (S(h) ≠ ±S(h'))

## Size (per n, coarse)

2n booleans + 2(n−K) window ints (each 0..2^{K+1}); sorting network ~
O(n log²n) comparators.  For n=40, K=20: 80 bools + 40 ints in [0,2²¹);
<(2·10⁶) clauses equivalent.  Small enough for CP-SAT at these sizes.

## Status
Encoding written and under validation against a brute-force oracle.

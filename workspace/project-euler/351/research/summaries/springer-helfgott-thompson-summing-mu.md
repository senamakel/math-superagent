# Helfgott & Thompson, "Summing μ(n): a faster elementary algorithm" (2023)

Source: https://link.springer.com/article/10.1007/s40993-022-00408-8 — full
text at `research/sources/springer-helfgott-thompson-summing-mu.full.md`.

Citation: Harald Andrés Helfgott, Lola Thompson, *Research in Number Theory*
9(1):6 (2023). DOI: 10.1007/s40993-022-00408-8.

## What this source establishes

The state of the art in elementary Mertens-function computation, and the
paper Brown's totient paper cites as the fastest M(⌊n/y⌋) subroutine
("the Mertens function can also be computed with the Helfgott–Thompson
algorithm, which takes Θ̃(n^{3/5}) time").

**Main theorem.** M(x) = Σ_{n≤x} μ(n) can be computed in

    O(x^{3/5} (log x)^{8/5} (log log x)^{7/5}) time  (bit operations)
    O(x^{3/10} (log x)^{13/10} (log log x)^{−3/10}) space (bits)

the first improvement in the exponent of x for an elementary algorithm since
1985. Space can be reduced to O(x^{1/5}(log x)^{5/3}) by using Helfgott's
improved sieve of Eratosthenes (Helfgott, Math. Comput. 89:333–350, 2020), at
the cost of raising time to O(x^{3/5}(log x)^2 log log x).

**Method.** Start from the K=2 Heath-Brown/Vaughan identity for μ:

    μ(n) = − Σ_{m1 m2 n1 = n, m1,m2 ≤ u} μ(m1) μ(m2) + {2μ(n) if n ≤ u; 0 otherwise}

for u ≥ √x, which summed over n ≤ x gives (u = √x):

    M(x) = 2M(u) − Σ_{m,n ≤ v} μ(m)μ(n)⌊x/(mn)⌋ − [large-variable terms]

with v ≈ x^{2/5} (larger than the v = x^{1/3} used by Deléglise–Rivat). The
bulk of the paper (Sect. 4) shows how to compute Σ μ(m)μ(n)⌊x/(mn)⌋ over
m,n ≤ v in O(v^{2/3} x^{1/3} log x) operations using local linear
approximation of x/(mn) + Diophantine approximation + floor-difference tables.

**Numerics.** Computed M(x) for x = 10^n (n ≤ 23) and x = 2^n (n ≤ 75),
beating the previous records; found a sign error in Kuznetsov's table for
M(10^21). M(10^23) took ~18.6 days on an 80-core machine.

## Why it matters here

For this run's n = 10^8, the needed M(⌊n/y⌋) values (y ≤ b ≈ 2000) all have
argument ≤ 10^8/1 but the recursion with sieved μ up to √n ≈ 10^4 is far
cheaper than a HT run; HT is the theoretical context and the source of the
Mertens check values (e.g. M(10^8)) that verify the Mertens subroutine of the
totient solver. The identity (2.2) is also an independent derivation of the
M(⌊n/y⌋) recursion.

## Claims

```claim
id: heath-brown-mobius-identity
statement: For u ≥ √x, μ(n) = − Σ_{m1 m2 n1 = n, m1,m2 ≤ u} μ(m1)μ(m2) + 2μ(n)·[n ≤ u]; summing over n ≤ x gives M(x) = 2M(u) − Σ_{m1,m2 ≤ u} μ(m1)μ(m2)⌊x/(m1 m2)⌋.
hypotheses: x ≥ 1; u ≥ √x; μ the Möbius function.
holds-here: yes — an independent route to the Mertens recursion the totient solver uses.
status: sourced
bearing: supplies the identity behind M(⌊n/y⌋) evaluation and the check value M(10^8).
anchor: research/summaries/springer-helfgott-thompson-summing-mu.md
```

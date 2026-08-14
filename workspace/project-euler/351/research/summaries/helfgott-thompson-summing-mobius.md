# Helfgott & Thompson, "Summing μ(n): a faster elementary algorithm" — full Springer text

Source: https://doi.org/10.1007/s40993-022-00408-8 — full text at
`research/sources/helfgott-thompson-summing-mobius.full.md`
[[helfgott-thompson-summing-mobius.full]]

## Correction of an earlier mislabel

This file is **the complete Research in Number Theory 9(1):6 (2023)
article** — main theorem, Sections 1–7, Appendix A (alternative algorithm),
Appendix B (pseudocode) — not an abstract page. An earlier note called it
"the arXiv abstract page; do not cite"; that was wrong (the arXiv *ID*
1801.07931 is a different paper, Barczy–Bősze–Pap; the *DOI* 10.1007/
s40993-022-00408-8 is this article). Cite this file freely; it is a duplicate
of `research/sources/springer-helfgott-thompson-summing-mu.full.md` (same
DOI, same text).

## What this source establishes

Main theorem: M(x) = Σ_{n≤x} μ(n) computed in

    time  O(x^{3/5} (log x)^{8/5} (log log x)^{7/5})   (bit operations)
    space O(x^{3/10} (log x)^{13/10} (log log x)^{-3/10})  (bits)

the first improvement in the exponent of x for an elementary algorithm since
1985. Space can be reduced to O(x^{1/5}(log x)^{5/3}) by using Helfgott's
improved sieve of Eratosthenes (Math. Comput. 89:333–350, 2020), raising time
to O(x^{3/5}(log x)^2 log log x).

**Method.** K = 2 Heath-Brown identity for μ (eq. 2.1, valid for u ≥ √x):

    μ(n) = − Σ_{m1 m2 n1 = n, m1,m2 ≤ u} μ(m1)μ(m2) + {2μ(n) if n ≤ u; 0 else}

which summed over n ≤ x gives (eq. 2.2, u = √x):

    M(x) = 2M(u) − Σ_{m1,m2 ≤ u} μ(m1)μ(m2)⌊x/(m1 m2)⌋

with the double sum split at v = x^{2/5} (Sect. 4 handles m1,m2 ≤ v by local
linear approximation of x/(mn) + Diophantine approximation + floor-difference
tables, Lemmas 4.1–4.6). Lehman's identity (eq. 2.3, credited to Lehman,
Math. Comp. 1960, p. 314) is stated equivalent for u = √x.

**Numerics.** M(10^n) for n ≤ 23 and M(2^n) for n ≤ 75, beating previous
records; found a sign error in Kuznetsov's table for M(10^21). M(10^23) took
~18.6 days on an 80-core machine.

## Why it matters here

The fastest elementary Mertens subroutine Brown's totient paper cites; the
identity (2.1) is an independent derivation of the M(⌊n/y⌋) recursion used in
the Mertens-first route to Φ(10^8). For n = 10^8 the run's own sieve routes
need no Mertens machinery, so this is theoretical context and source of check
values, not load-bearing for the answer.

## Claims

```claim
id: heath-brown-mobius-identity
statement: For u ≥ √x, μ(n) = − Σ_{m1 m2 n1 = n, m1,m2 ≤ u} μ(m1)μ(m2) +
2μ(n)·[n ≤ u]; summing over n ≤ x gives M(x) = 2M(u) −
Σ_{m1,m2 ≤ u} μ(m1)μ(m2)⌊x/(m1 m2)⌋.
hypotheses: x ≥ 1; u ≥ √x; μ the Möbius function.
holds-here: yes — an independent route to the Mertens recursion the totient
solver uses.
status: sourced (Helfgott–Thompson 2023, eq. 2.1–2.2)
bearing: supplies the identity behind M(⌊n/y⌋) evaluation and the check value
M(10^8).
anchor: research/summaries/helfgott-thompson-summing-mobius.md
```

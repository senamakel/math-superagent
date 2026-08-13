# Stein 1980 — Partial fetch (TOMBSTONE, not the article)

Source attempted: Alan H. Stein, "Exponential sums related to binomial
coefficient parity", Proc. Amer. Math. Soc. 80 (1980) 526–530,
DOI 10.1090/s0002-9939-1980-0581019-4.

**Status: NOT obtained.** The DOI download returned the AMS *Proceedings* journal
landing page (issue list / editorial board), not the article. The AMS free
archive should cover 1980 volumes, but the resolved URL
(https://www.ams.org/journals/proc/...) did not yield a per-article page via
this tool. Do not re-fetch this DOI un-mirrored.

## What Stein 1980 establishes (attested, not held)

From the search-result abstract and the citations in held sources (HJT
arXiv:2408.06817, which cites Stein's 1989 Lecture Notes and the 1980 paper;
Essouabri 2005; Ikkai 2017):

- With `a(n)` the number of 1s in the binary expansion of n and
  `φ_z(x) = Σ_{n<x} 2^{z·a(n)}`, `θ_z = (log(1+z))/log 2`,
  `a(z) = liminf x^{-θ_z} φ_z(x)`, `b(z) = limsup`, Stein proved
  `0 < a(z) < 1 < b(z) < 2`, with `a(z) < b(z)` for z > 1;
  the two-sided bounds `x^{θ}/(1+z) < φ_z(x) < (1+z)x^{θ}` (z = 2 being
  Stolarsky's case), via the recursion `φ_z(2^n + x) = φ_z(2^n) + z·φ_z(x)`.
- With z = 2 this is the count of odd entries in the first n rows of Pascal's
  triangle (OEIS A006046), the same object HJT study exactly.

**None of this is load-bearing for the run beyond what is already held.** The
two facts the threads need — `F_p(pn) = C(p+1,2)·F_p(n)` (hence
`F_2(2^m) = 3^m`) and the continuity/periodicity of the normalised count — are
proven self-containedly as Theorem 2.1 and 2.2 of Hwang–Janson–Tsai 2024
(`research/sources/hwang-janson-tsai-parity-count-2024.full.md`, held), which
cites Stein for history. The enormous "full text" saved under this name is the
AMS landing page and must not be cited as Stein's paper.

```claim
id: stein-1980-not-held-content-attested
statement: Stein 1980 (Proc AMS 80, 526–530) proves bounds on the exponential
  sum φ_z(x)=Σ_{n<x}2^{z·a(n)} (a(n)=popcount(n)): with θ_z=(log(1+z))/log 2,
  0<a(z)<1<b(z)<2 and x^θ/(1+z)<φ_z(x)<(1+z)x^θ; z=2 counts odd entries in the
  first n rows of Pascal's triangle. The primary was NOT obtained (AMS DOI
  resolved to the journal landing page); the statement is attested by the
  IEEE/AMS abstract and by the citation in HJT arXiv:2408.06817.
hypotheses: z>0 real; a(n) binary digit sum.
holds-here: yes but redundant — the p=2 consequences used by the binary-digit
  thread (F_2(2^m)=3^m, periodic representation) are proven inside HJT
  arXiv:2408.06817 Thms 2.1-2.2, which is held.
status: asserted (attested, primary not held)
bearing: none beyond the held HJT treatment; keeps the record honest that
  Stein 1980 is not in the library.
anchor: research/summaries/stein-1980-exponential-sums-parity.md
```
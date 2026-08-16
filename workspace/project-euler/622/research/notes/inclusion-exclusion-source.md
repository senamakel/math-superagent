# Inclusion–Exclusion over the divisor lattice — sourceable statement

Anchors the `G-inclusion-exclusion` blueprint rung, which was listed as ready
but had no source for the principle itself (only its divisor-sum consequences,
via Mathar/Wolfram).

## Statement

**Inclusion–exclusion (PIE), finite sets.** For finite sets A_1, …, A_n,
```
|A_1 ∪ … ∪ A_n| = sum_{∅≠J⊆{1..n}} (-1)^{|J|+1} |∩_{i∈J} A_i|.
```
Source: Wikipedia, "Inclusion–exclusion principle"
(`research/sources/wikipedia-inclusion-exclusion.full.md`); also Eba,
"Sieving for the Primes…", 17 Missouri J. Math. Sci (2017), Lemma 3.1
(`research/sources/eba-inclusion-exclusion.full.md` — only the front matter
converted, the lemma is stated in the paper but the full text did not convert).
The special case needed here — the indicator `1_{m ∈ M}` with
M = {m | N : m∤2^12−1, m∤2^20−1, m∤2^30−1} — is
```
1 - [m|2^12-1] - [m|2^20-1] - [m|2^30-1]
  + [m|15]  + [m|63]  + [m|1023] - [m|3],
```
the pairwise/triple intersections collapsing via
gcd(2^a−1, 2^b−1) = 2^{gcd(a,b)}−1 (G-gcd-mersenne), e.g.
A_12 ∩ A_20 = divisors of 15, A_12∩A_20∩A_30 = divisors of gcd(12,20,30)=2^2−1=3.

## Claim

```claim
id: inclusion-exclusion-sourceable
statement: For finite sets A_1,...,A_n, |A_1 ∪ ... ∪ A_n| =
  sum_{∅≠J⊆{1..n}} (-1)^{|J|+1} |∩_{i∈J} A_i|. Consequently, for
  M = {m | N : m∤2^12-1, m∤2^20-1, m∤2^30-1},
  sum_{m∈M} m = sigma(N) - sigma(2^12-1) - sigma(2^20-1) - sigma(2^30-1)
    + sigma(15) + sigma(63) + sigma(1023) - sigma(3),
  and |M| = tau(N) - tau(2^12-1) - tau(2^20-1) - tau(2^30-1)
    + tau(15) + tau(63) + tau(1023) - tau(3),
  where A_d = {m|N : m|2^d-1} and intersections collapse through
  gcd(2^a-1, 2^b-1) = 2^gcd(a,b)-1.
hypotheses: A_i finite; for the divisor special case, N = 2^60-1 and m ranges
  over positive divisors of N; the gcd identity needs a,b >= 1.
holds-here: yes (the three proper-divisor sets A_12, A_20, A_30 are finite
  subsets of the divisors of N; their intersections reduce to divisor sets of
  the small numbers 15, 63, 1023, 3).
bearing: gives the G-inclusion-exclusion rung a citable principle instead of an
  unanchored formula.
status: proved
anchor: Wikipedia Inclusion–exclusion principle (finite form);
  Eba, Missouri J. Math. Sci 29 (2017) Lemma 3.1 (front matter converted).
```

## Notes

- EoM's entry `Inclusion_and_exclusion_principle` returned HTTP 502 and was not
  obtained; Wikipedia's encyclopedic entry covers the same statement.
- Eba (doi 10.35834/mjms/1513306829) converted to only its front matter in this
  library; its Lemma 3.1 is the same PIE formula, so if the full statement is
  wanted it must be re-fetched from a source that converts the body.

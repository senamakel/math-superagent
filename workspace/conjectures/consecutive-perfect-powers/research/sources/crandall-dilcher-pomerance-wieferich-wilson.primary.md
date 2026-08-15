# Crandall, Dilcher, Pomerance — "A search for Wieferich and Wilson primes"

**Source URL:** https://doi.org/10.1090/s0025-5718-97-00791-6
**Authors:** Richard E. Crandall, Karl Dilcher, Carl Pomerance, *Mathematics of Computation*
**66** (1997), no. 217, 433–450.
**How obtained:** server-side full-text readout via `read_sources` on the AMS DOI.
`download_document` is refused on this host by the network boundary; this is a
captured readout of the paper's content, not a stored PDF.

## Exact definition — the base-a Wieferich prime

> For an integer `a` with `gcd(a, p) = 1`, an odd prime `p` is **Wieferich to
> base `a`** iff `a^{p-1} ≡ 1 (mod p^2)`, equivalently iff the Fermat quotient
> `q_p(a) = (a^{p-1} - 1)/p` vanishes mod `p`.

The base-2 case is the classical "Wieferich prime":

> `p` is a base-2 Wieferich prime iff `2^{p-1} ≡ 1 (mod p^2)`, equivalently
> `p^2 | (2^{p-1} - 1)`.

The two defining congruences (base `a`, and base `a` = 2) hold merely mod `p` by
Fermat's little theorem; the Wieferich condition is that they survive mod `p^2`.

## Known values and search bounds (as of this source)

- **Base-2 Wieferich primes**: only `p = 1093` and `3511` are known. No new ones
  below `4 × 10^12` (the paper's new bound; prior: Lehmer no others below
  `6 × 10^9`, Clark extended to `6.1 × 10^10`). Search verified to `2 × 10^12`
  by the authors, extended to `4 × 10^12` and double-checked by David Bailey and
  by Richard McIntosh.
- **Wilson primes** (not Wieferich, context): `p` with `p^2 | (p-1)! + 1`;
  known `p = 5, 13, 563`; none below `5 × 10^8`.
- **Heuristics**: probability a random prime is Wieferich (resp. Wilson) is
  about `1/p`, so the expected count grows like `log log`. Observed near-Wieferich
  counts match heuristics (≈68 near-Wieferich in `[10^9, 4×10^12]` vs expected
  ≈67.7; ≈27 near-Wilson in `[10^7, 5×10^8]` vs expected ≈21.9).

## Why the run wants it

This is the primary anchor for the *base-a* Wieferich definition the run's
reconstruction of the double-Wieferich placement relies on
(`research/summaries/cassels-wieferich-placement.md`, claim
`cassels-double-wieferich-placement`-adjacent). It fixes the notation: **base
left, squared modulus right**. Applying it symmetrically to the two primes
`p, q` of `x^p - y^q = 1` gives the reconstruction

    p is base-q Wieferich:  q^{p-1} ≡ 1 (mod p^2)
    q is base-p Wieferich:  p^{q-1} ≡ 1 (mod q^2)

which is the placement `check_conditions(p,q)` must test. The source itself does
NOT concern `x^p - y^q = 1`; it defines the general notion only.

## Claims

```claim
id: base-a-wieferich-definition-cdp
statement: > For an integer a with gcd(a,p)=1, an odd prime p is Wieferich to base a iff a^{p-1} ≡ 1 (mod p^2), equivalently the Fermat quotient q_p(a) = (a^{p-1}-1)/p vanishes mod p. Base 2: only Wieferich primes 1093 and 3511 are known, none below 4e12.
hypotheses: p odd prime, gcd(a,p)=1
holds-here: yes (fixes the notation for the double-Wieferich reconstruction: base left, squared modulus right)
status: asserted
bearing: primary anchor for the base-a Wieferich definition the run's reconstruction of the double-Wieferich placement (q^{p-1}≡1 mod p^2, p^{q-1}≡1 mod q^2) relies on; independently confirms Katz.
anchor: research/sources/crandall-dilcher-pomerance-wieferich-wilson.primary.md
```

## Relation to the known solution and the evidence policy

- Known solution `(3,2,2,3)` has `p = 2` even; neither congruence is defined
  there (gcd condition / odd-prime hypothesis), so the definition neither
  confirms nor excludes it. It is excluded by the hypothesis, not the 
  congruence — consistent with the falsifier discipline in GOAL.md.
- This source develops the *technique* (the general Wieferich notion and its
  computational search); it does **not** report the double-Wieferich placement
  for `x^p - y^q = 1`, so it is not screened and may be held.

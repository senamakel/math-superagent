# Granville, "Arithmetic Properties of Binomial Coefficients I: Binomial coefficients modulo prime powers" (CMS Conf. Proc. 20, 1997, 253–275) — dynamic e-survey

Source: https://dms.umontreal.ca/~andrew/Binomial/ (+ subpages intro.html, elementary.html, genlucas.html)
Full text of the sections fetched: `research/sources/granville-binomial-intro.full.md`,
`research/sources/granville-binomial-elementary.full.md`,
`research/sources/granville-binomial-genlucas.full.md`.
Note: `research/summaries/granville-arithmetic-properties-binomial.md` holds only the
table-of-contents page; the substantive fetched sections are listed above.

## What this source is

The canonical dynamic survey of the arithmetic of binomial coefficients modulo
prime powers, by Andrew Granville (1997; the e-survey is the widely-cited
"Arithmetic Properties of Binomial Coefficients I"). It collects the classical
results of Kummer, Lucas, Anton–Stickelberger–Hensel, Glaisher, Babbage,
Wolstenholme, Ljunggren, Jacobsthal, Morley and Emma Lehmer, with proofs and
generalisations. This is the standard reference for the p-adic structure of
binomial coefficients used by the `binary-digit` thread's Lucas-submask
constraint and by any p-adic argument on C(x,k1)=C(y,k2).

## What the fetched sections establish (verbatim content)

**Intro (intro.html).**
- **Kummer (1852):** the power of p dividing C(n,m) is the number of carries
  when adding m and n−m in base p.
- **Lucas (1878):** C(n,m) ≡ C(n0,m0)·C(n1,m1)·… (mod p) where ni, mi are the
  base-p digits; C(ni,mi) = 0 if mi > ni (convention).
- **Anton (1869)/Stickelberger (1890)/Hensel (1902):** gives C(n,m) modulo p^q
  for the exact power q, via the product of integers not divisible by p
  (formula (2) in the source).
- **Theorem 1 (Granville):** full formula for C(n,m) modulo p^q with the
  carry-count per digit — the complete generalisation of Lucas; computing
  C(n,m) mod p^q takes O(elementary operations). (Davis–Webb have a similar
  result.)
- **Glaisher (1899):** the number of odd entries in row n of Pascal's triangle
  is 2^{#1s in binary expansion of n}; C(n,m) is odd iff the 1-bits of m are a
  subset of those of n (Lucas mod 2). This is the exact statement the
  `binary-lucas-submask` approach uses.
- **Babbage (1819):** C(2p−1,p−1) ≡ 1 (mod p) for primes p; **Wolstenholme
  (1862):** C(2p−1,p−1) ≡ 1 (mod p^3) for p ≥ 5; Ljunggren, Jacobsthal
  generalisations.
- **Morley (1895), Emma Lehmer (1938):** congruences relating binomial
  coefficients to Fermat's Last Theorem and to representations of primes by
  quadratic forms (Gauss d=4; Chowla–Dwork–Evans for Beukers' conjecture).

**Elementary (elementary.html).** (short) elementary number theory section.

**Generalization of Lucas' Theorem (genlucas.html).** (short) statement of the
Lucas generalisation to prime powers used throughout the survey.

## Claim block

```
id: granville-arith-properties-binom
statement: Lucas/Kummer/Stickelberger–Anton–Hensel give exact p-adic control of C(n,m):
  the p-adic valuation is the base-p carry count (Kummer), C(n,m) modulo p is
  digitwise (Lucas), and modulo prime powers by Granville's Theorem 1; in
  particular C(n,m) is odd iff every 1-bit of m is a 1-bit of n (Glaisher/Lucas p=2).
hypotheses: n ≥ m ≥ 0 integers, p prime; standard base-p digit notation.
holds-here: yes — this is the exact mechanism behind the binary-lucas-submask approach,
  which needs "every representation (n,k) of odd a has k ⊆ n as bit-masks".
status: asserted-by-source (survey; proofs of the classical theorems are standard)
source: https://dms.umontreal.ca/~andrew/Binomial/intro.html
```

## Why it was fetched

The `binary-digit` thread's first step (scan odd binomial coefficients, record
multiplicities, use the submask constraint) depends on Glaisher/Lucas mod 2,
which was previously grounded only in the Rowland and Harborth papers. This
survey is the canonical reference that fixes the full p-adic statement and the
surrounding results (Kummer carry count, Stickelberger–Anton–Hensel, Babbage,
Wolstenholme) — the standard citation for anyone claiming 2-adic structure of
binomial coefficients. The frontier leads from it (Davis–Webb, Hudson–Williams,
Chowla–Dwork–Evans, Skula) are filed for context but are not load-bearing for
the run's current thread.
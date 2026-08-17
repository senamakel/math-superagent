# Laishram–Shorey, "The greatest prime divisor of a product of consecutive integers" (Acta Arith. 120 (2005) 299–306)

Source: https://www.isid.ac.in/~shanta/PAPERS/ActaPCons.pdf | DOI: 10.4064/aa120-3-5
Full text: `research/sources/laishram-shorey-greatest-prime-divisor-2005.full.md`

## What this source establishes

Notation: Δ(n,k) = n(n+1)…(n+k−1); P(ν) = greatest prime factor of ν;
ω(ν) = number of distinct prime factors. The classical **Sylvester theorem**
(1892): P(Δ(n,k)) > k for n > k. This paper sharpens the Sylvester–Schur-type
bounds on P(Δ(n,k)):

**Theorem 1.** (a) P(Δ(n,k)) > 2k for n > max(k+13, (279/262)k).
(b) P(Δ(n,k)) > 1.97k for n > k+13. The 1.97 in (b) cannot be replaced by 2
(arbitrarily long chains of consecutive composites).

The proof combines lower bounds on ω(Δ(n,k)) (via lemma 2: for n > k > 2,
ω(Δ(n,k)) ≥ π(k) + something; refined using sharp prime-counting estimates of
Dusart type), Catalan-type results (Levi ben Gerson), and combinatorial case
analysis; it does not use the earlier Hanson/Faulkner results.

## Reconciliation with the held thesis

The held PhD thesis (Laishram, `research/sources/laishram-phd-thesis-sylvester.full.md`,
Thm 1.3.1) records the earlier Laishram–Shorey rung `P(Δ(n,k)) > 1.95k` for
n > k. The fetched Acta Arith. 120 (2005) 299–306 paper is the same authors'
final published refinement, with the sharper `P > 2k` (n > max(k+13, (279/262)k))
and `P > 1.97k` (n > k+13). Both stand; this primary supersedes the 1.95k
thesis-attested figure with the exact 2k statement.

## Relevance to this run

This is the **true precedent** for the Sylvester step of the
`zsigmondy-primitive-prime` approach — the sharpest unconditional statement
that a block of k consecutive integers (all > k) contains a prime divisor
substantially larger than k. It replaces the phantom "Granville–Ramaré 1996"
citation (see `research/notes/zsigmondy-phantom-citation.md`).

## Claim block

```
id: laishram-shorey-sylvester-sharp
statement: For integers n > k >= 2, P(Δ(n,k)) > 2k whenever n > max(k+13, (279/262)k),
  and P(Δ(n,k)) > 1.97k whenever n > k+13, where Δ(n,k) = n(n+1)...(n+k-1).
  This refines Sylvester's P(Δ(n,k)) > k (n > k) and Hanson's P > 1.5k.
hypotheses: n,k positive integers, n > k; P = greatest prime factor.
holds-here: yes — any representation (n,k) of a = C(n,k) with k >= 2 has
  n >= 2k, and for n-k large relative to k the falling-factorial block
  (n-k+1)...n (equivalently Δ(n-k+1,k)) carries a prime > 2k; this is the
  Sylvester-step engine of the zsigmondy-primitive-prime approach.
status: asserted-by-source (Acta Arith. 120 (2005) 299–306, peer-reviewed)
source: https://www.isid.ac.in/~shanta/PAPERS/ActaPCons.pdf
```

## Falsifier for the approach

The zsigmondy approach still lacks a true "primitive prime divisor for
falling-factorial blocks" theorem (prime dividing Δ(n,k) but not any Δ(n',k)
with smaller start). Laishram–Shorey bounds P(Δ) but does not give
primitiveness across starting values; Zsigmondy applies to a^n − b^n, not
directly to consecutive-integer products. That gap is the honest statement of
what the phantom citation was covering.
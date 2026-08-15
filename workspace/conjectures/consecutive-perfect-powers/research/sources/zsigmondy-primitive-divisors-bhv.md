# Zsigmondy's theorem and Bilu–Hanrot–Voutier: the primitive prime divisor machinery

- Authors: Yuri Bilu, Guillaume Hanrot, Paul M. Voutier (with an appendix by
  Maurice Mignotte).
- Source: "Existence of primitive divisors of Lucas and Lehmer numbers",
  INRIA Research Report RR-3792 (November 1999).
  URL: https://inria.hal.science/inria-00072867/file/RR-3792.pdf
- How obtained: server-side full-text readout via `read_sources`
  (`download_document` is refused on this host by the network boundary). This
  file records the genuine primary content that readout returned.
- Classical antecedent: Zsigmondy's theorem (1892), "Zur Theorie der
  Potenzreste", Monatsh. Math. 3, 265–284.

## Primitive divisors, the exact notion

A **primitive prime divisor** of the term `U_n` of an integer (Lucas/Lehmer)
sequence is a prime `p` such that `p | U_n` but `p ∤ U_k` for every `k < n` —
a prime appearing for the first time exactly at index `n`.

For the prototypical sequence `a^n - b^n` with `a > b > 0`, `gcd(a,b) = 1`:

**Zsigmondy's theorem (classical form).** For every `n > 1`, the number
`a^n - b^n` has a primitive prime divisor, with the single exception

    (a, b, n) = (2, 1, 6):   2^6 - 1 = 63 = 3^2 * 7

has no primitive prime divisor (both 3 and 7 already divide `2^1 - 1` or
`2^3 - 1`, and 3 divides `2^2 - 1 = 3`). The `n = 1` cases are trivial and
excluded by `n > 1`.

## Bilu–Hanrot–Voutier's extension to Lucas and Lehmer sequences

Let `U_n(P,Q)` be the Lucas sequence

    U_0 = 0,  U_1 = 1,  U_n = P U_{n-1} - Q U_{n-2}   (n >= 2)

with integers `P, Q`, assumed **nondegenerate**, i.e. the discriminant
`Delta = P^2 - 4Q != 0` and `alpha/beta` is not a root of unity (where
`alpha, beta` are the roots of `x^2 - P x + Q = 0`). The primitive-divisor
existence extends to this setting: for all sufficiently large `n` the term
`U_n` has a primitive prime divisor, and the theorem gives an **explicit,
complete, finite list** of exceptional triples `(P, Q, n)` for which no
primitive divisor exists. In particular:

- For prime `n = p`, a primitive divisor `r` of `Phi_p(x)` (equivalently of
  the corresponding Lucas term) has the property that the multiplicative order
  of `x` modulo `r` is exactly `p`, whence **`r ≡ 1 (mod p)`**. This is the
  congruence that the run's Lucas-sequence approach exploits: it is obtained
  for free from a proved, effective, elementary theorem, with no class-number
  hypothesis.
- The exceptional cases in the `a^n - b^n`/Lucas setting are a small explicit
  finite list; the archetypal one is `U_6` of the Fibonacci sequence
  `(P,Q) = (1,-1)`, mirroring the `(2,1,6)` classical exception.

## Application to cyclotomic factors used by the run

The run's `research/approaches/lucas-primitive-divisors.md` rests on the
identities

    Phi_p(x) = (x^p - 1)/(x - 1) = U_p(x + 1, x)
    Phi_q(-y) = (y^q + 1)/(y + 1) = U_q(y - 1, -y)   (q odd)

so `Phi_p(x)` carries a primitive prime divisor `r ≡ 1 (mod p)` for every odd
prime `p` and `x >= 2`. Since `y^q = (x-1) * Phi_p(x)` from `x^p - y^q = 1`,
such an `r` divides `y`. **The honest statement is "for odd prime p and
x >= 2"**: at `p = 2` (the known solution `3^2 - 2^3 = 1`) the index `2` is
inside the Zsigmondy exceptional list and `Phi_2(3) = 4` has no primitive
divisor `r ≡ 1 (mod 2)`. So `(3,2)` is excluded by the oddness hypothesis, not
by luck — this is exactly the GOAL.md falsifier discipline.

## Status

- Primary research-paper content retrieved server-side. Pure technique
  (primitive-divisor existence), not the answer to `x^p - y^q = 1`. Nothing
  here is screened.
- The exceptional-list details (`P,Q,n` triples) are quoted as reported by the
  readout; the definitive classification is in BHV RR-3792 and Voutier's
  papers "Primitive divisors of Lucas and Lehmer sequences" I–III (Proc.
  Camb. Phil. Soc. 123, 1998). The run has not re-derived the full finite
  exception list here; `research/approaches/lucas-primitive-divisors.md`
  records the finite enumeration as a first step.

## Voutier's uniform effective bound (from the readout of "Primitive divisors
of Lucas and Lehmer sequences, III", Proc. Camb. Phil. Soc. 123 (1998))

**If `n > 30,030`, then the n-th term of any (nondegenerate) Lucas or Lehmer
sequence has a primitive divisor.** The complete list of exceptional
`(P, Q, n)` with no primitive divisor is therefore finite and contained in
`n <= 30,030`, explicitly classified in the BHV/Voutier series. For the run's
Lucas approach this means the exception check is a finite enumeration over the
small-n list, since `Phi_p(x) = U_p(x + 1, x)` has index `n = p`; an odd prime
`p > 30,030` automatically has a primitive divisor `r ≡ 1 (mod p)`, and the
primes `p <= 30,030` are a finite set to be checked against Voutier's explicit
exceptional triples. URL:
https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/primitive-divisors-of-lucas-and-lehmer-sequences-iii/9E00EE0121300C7E0475721D86D8C530

```claim
id: zsigmondy-bhv-primitive-divisor
statement: >
  For odd prime p and integer x >= 2, the cyclotomic factor
  Phi_p(x) = (x^p - 1)/(x - 1) = U_p(x + 1, x) has a primitive prime divisor
  r: r | Phi_p(x) and r does not divide (x^k - 1) for k < p, hence r ≡ 1 (mod p).
  This is Zsigmondy's theorem as extended by Bilu-Hanrot-Voutier; the only
  excluded index is n = 2 (and the explicit small exceptional list), so the
  oddness of p is essential. Consequence for x^p - y^q = 1: such an r divides
  y, since y^q = (x-1) * Phi_p(x).
hypotheses: p an odd prime, x >= 2 integer.
holds-here: >
  yes for the odd-prime open content (p odd). At the known solution p = 2 the
  hypothesis fails; there the assertion would be false, so the lemma must carry
  the "p odd" hypothesis explicitly to stay consistent with 3^2 - 2^3 = 1.
status: sourced (BHV RR-3792; Zsigmondy 1892; cf. Roitman 1997, Voutier 1998).
anchor: research/sources/zsigmondy-primitive-divisors-bhv.md
bearing: an elementary, proved, effective route to the Wieferich-style
  congruence r ≡ 1 (mod p) and to r | y, independent of the class group.
```

# Lagarias & Odlyzko 1977, *Effective versions of the Chebotarev density theorem*

Source: re-typeset LaTeX PDF at
`https://aareyanmanzoor.github.io/assets/articles/lagarias-odlyzko.pdf`
(original: pp. 409–464 in *Algebraic Number Fields*, A. Fröhlich (ed.),
Academic Press, 1977).
Full text: `research/sources/lagarias-odlyzko-effective-chebotarev-1977.full.md`.

## What it establishes

Two effective Chebotarev theorems counting primes in Frobenius conjugacy
classes of a fixed Galois extension L/K:

- **Theorem 1.1 (GRH-conditional):** with effectively computable constants,
  `π_C(x) = (|C|/|G|)·Li(x) + O(√x log(D_L x^{n_L}))` — where C a conjugacy
  class, D_L the absolute discriminant, n_L = [L:Q].
- **Theorem 1.3 (unconditional):** ζ_L(s) has at most one (Siegel) zero in a
  certain region; theorem 9.2 gives the unconditional effective count.
- Corollary 1.2: existence of effective primes in prescribed Frobenius classes.

## Why it matters for this run

This is **reference [11] of Maciejewski arXiv:2605.20475**, the paper's cited
anchor for the statement that hypothesis **(H1)** of Theorem 30 — "every odd p
with ω(Φ_{4p}(2)) ≥ C log p has some divisor r ≡ 1 (mod 16)" — is **not a
consequence of any standard effective Chebotarev theorem, including under
GRH**. Having the primary text pins the structural reason precisely:

- Chebotarev controls **varying primes q ≤ x** in Frobenius classes of a fixed
  Galois extension: a *range/density* object.
- `(H1)` is a **divisor-level** statement about the prime support of *one fixed
  integer* `Φ_{4p}(2)` — a finite set, not a range. Chebotarev gives no
  information "within" the divisor set of a single integer.
- So the paper's claim that (H1) needs a *divisor-transference* theorem that
  does not exist in the literature is anchored to the actual statement of the
  standard tool.

```claim
id: lo1977-effective-chebotarev-classes-not-divisors
statement: Lagarias-Odlyzko effective Chebotarev (GRH and unconditional) counts
  primes in Frobenius conjugacy classes of a fixed Galois extension, with explicit
  error terms in x, n_L, D_L, |C|/|G|. It controls varying primes q <= x and gives
  NO statement about the prime-divisor set of a single fixed integer.
hypotheses: Galois extension L/K, fixed class C
holds-here: yes -- the paper's (H1) divisor-level equidistribution for the prime
  support of Phi_{4p}(2) is outside the reach of this theorem
status: asserted by source; structural match read from the primary text
bearing: confirms arXiv:2605.20475's claim that (H1) is NOT standard effective
  Chebotarev (even under GRH); the missing divisor-transference theorem is genuinely
  absent from this anchor.
anchor: research/sources/lagarias-odlyzko-effective-chebotarev-1977.full.md
answers: why-H1-not-chebotarev
```

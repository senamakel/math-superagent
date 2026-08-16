# Pattern-finder: the pointwise CLT law for S(n) is exact-fold-generic, not prime arithmetic

I re-examined the central structural object from the measured data
(`code/out/excess_E2_30000.txt`, n=2..30000, exact): the endpoint character sum

    S(n) = Σ_{d=2}^{n-1} (−1)^{T(n,d)},   with  ν₂(n) = (n−2−S(n))/2,

so **pointwise SUPPLY (ν₂(n) ≥ c·n) ⟺ S(n) = o(n)**, and ν₂/n → 1/2 ⟺ S(n)/n → 0.
This reframe is already on the ledger; what I add is a precise distributional
law for S(n) measured to n=30000.

## The law

Let R(n) = S(n)/√n. Over n = 2..30000:

    E[R²]  = 1.002     (Gaussian N(0,1): 1)
    E[R⁴]  = 2.969     (Gaussian: 3)
    E[R⁶]  = 14.27     (Gaussian: 15)
    std R  = 1.001
    skew   = 0.008, excess kurtosis = −0.045
    KS vs N(0,1): D=0.0039, p=0.75
    max |R| = 3.81;  |R| > 4√n at n>100: zero

S is effectively uncorrelated (ACF ≈ 0 at all lags ≥ 1) and its increments D_n
have E[D²]/2n → 1.01, lag-1 ACF(D) = −0.503, all higher lags ≈ 0. This is
exactly the signature of **S(n) ≈ sum of nearly-independent mean-0 increments
each of variance ~1, i.e. S(n) ≈ √n · N(0,1)**: a CLT law, pointwise.

## Genericity — the honest check

The law is **fold-generic, not prime arithmetic**. A random string h at p=0.585
(the prime 1-density) gives E[R²]=0.997, E[R⁴]=2.98, std=0.998, KS p=0.21 —
statistically indistinguishable from the primes and from N(0,1). So the
pointwise √n/CLT behaviour of S is a property of the fold acting on any
"unstructured" balanced input; the primes sit in the generic-good class, needing
only to be unstructured enough (1-density ≳ 0.2), not any specific
autocorrelation. This confirms the prior pattern-finder captures (fold-generic
balance, excess-random-walk) and carries no new prime-specific arithmetic handle.

## What this means for SUPPLY

The measured √n law gives pointwise ν₂/n = 1/2 + O(1/√n), i.e. SUPPLY at c=1/2
pointwise with huge margin over the n^{0.526} fallback. But it is **measurement,
not proof**, and the whole difficulty is that this CLT scale is what a *random*
string achieves and what the closed-door witnesses (all-ones, Thue–Morse,
sparse) categorically fail — the primes' only proven need is being unstructured
enough. No arithmetic input has been found that *forces* the √n law; that
remains the open second-moment/variance pricing (GOAL priority 2, the adopted
fold-second-moment-Krawtchouk route condition A).

## Sequence tools (exact over supplied terms)

- ν₂(2^k) dyadic subsequence `[2,2,12,13,27,66,136,243,502,1003,2010,4184,8338]`:
  no constant-coefficient linear recurrence (order ≤ 6), not low-degree
  polynomial, **OEIS miss** (uncatalogued). No closed form to look up; structure
  must come from the problem.

## Status

Measured-exact over n ≤ 30000. The Gaussian/CLT law is a conjecture for all n
(matches to within statistical fluctuation of a genuine N(0,1) sample). Not a
proof of SUPPLY; a precise statement of the structure the primes exhibit and of
its genericity.

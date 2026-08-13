# Erdős–Selfridge, "The product of consecutive integers is never a power"

Source: https://www.renyi.hu/~p_erdos/1975-46.pdf — P. Erdős, J. L. Selfridge,
Illinois J. Math. 19 (1975) 292–301.
Full text: `research/sources/erdos-selfridge-product-not-power-1975.full.md`.

## Statement

The equation
```
(n+1)(n+2)...(n+k) = x^l        (k ≥ 2, l ≥ 2, n ≥ 0)
```
has no solutions in integers: **a product of two or more consecutive positive
integers is never a perfect power.**

The proof (for k ≥ 3; the square case k=2 was handled by Rigge and Erdős) shows
there is a prime p > k whose exponent in the product (n+1)...(n+k) is **not** a
multiple of l (in fact p divides the product with exact exponent 1 for essentially
all cases). The auxiliary result: for every k ≥ 2 there is a prime p > k such that
the p-adic valuation of (n+1)...(n+k) is not divisible by l — a strengthening of the
Sylvester–Schur theorem via a large-prime-in-block argument.

## Implication for this problem

This is a foundational tool for the binomial-coefficient Diophantine theory. The
binomial coefficient C(n,k) = n(n-1)...(n-k+1)/k! is a product (of consecutive
terms) divided by a factorial — so selfridge-type "no block of consecutive integers
is a perfect power" results are what force the structure behind, e.g., the
C(x,k1)=C(y,k2) collision family and the Fibonacci/N6 family's non-degeneracy. It
also underlies the AP-product results (SST 1995, Bennett–Siksek) that the run's
Diophantine thread and the effective-height program rest on: any effective bound
that says a product of AP terms is not a perfect power is a bound the binomial
collision argument can ride on.

```claim
id: erdos-selfridge-no-perfect-power
statement: The product of two or more consecutive positive integers is never a
  perfect power: (n+1)(n+2)...(n+k)=x^l has no solutions for k≥2, l≥2, n≥0. In
  fact for every k≥2 there is a prime p>k whose exponent in (n+1)...(n+k) is not
  a multiple of l.
hypotheses: none beyond k≥2, l≥2, n≥0.
holds-here: not itself used as a theorem on the Conjecture, but underpins the
  AP-product results the C(x,k1)=C(y,k2) argument relies on.
status: proved (primary source, in full here)
bearing: structural foundation — bounds preventing products of consecutive terms
  from being powers are the engine behind effective finiteness for binomial
  collisions.
anchor: research/sources/erdos-selfridge-product-not-power-1975.full.md
```

# Falling and rising factorials — summary

Source: https://en.wikipedia.org/wiki/Falling_and_rising_factorials
Full text: `research/sources/falling-factorial.full.md`

## What it defines

**Falling factorial** (descending factorial): `(x)_n = x(x-1)(x-2)...(x-n+1)`
(n factors) = ∏_{k=1}^{n}(x-k+1). Empty product = 1 when n=0. When x is a
positive integer, `(x)_n = x!/(x-n)!` = number of n-permutations.

**Rising factorial** (Pochhammer, ascending): `x^(n) = x(x+1)(x+2)...(x+n-1)`
= ∏_{k=0}^{n-1}(x+k); for positive integer x, `x^(n) = (x+n-1)!/(x-1)!`.

**Binomial-coefficient relation** (the fact this run uses):
```
(x)_n / n! = C(x,n)
```
so the falling factorial divided by n! is exactly the binomial coefficient.

## Why it is in this run's library

This is MRSTT's background ref for their analogous "falling factorial" Theorem 3.
More importantly for the run: it gives the bridge from the binomial-equality
curve to the equal-products-of-consecutive-integers equation. Since
```
C(x,k) = x(x-1)...(x-k+1) / k! = (x)_k / k!,
```
the equation
```
C(x,k1) = C(y,k2)
```
is equivalent to
```
x(x-1)...(x-k1+1) · k2! = y(y-1)...(y-k2+1) · k1!
```
i.e. equality of products of consecutive integers scaled by factorials — the
form Beukers–Shorey–Tijdeman (held) treats, where Siegel ineffectivity and the
genus classification live. Also: `C(x,k)` as a polynomial in x has degree k,
with integer coefficients; its expansion coefficients are (signed) Stirling
numbers of the first kind.

## Claim

```claim
id: falling-factorial-binom-bridge
statement: C(x,k) = (x)_k/k! = x(x-1)...(x-k+1)/k!, so C(x,k1)=C(y,k2) is
  equivalent to the equal-products equation x(x-1)...(x-k1+1)·k2! =
  y(y-1)...(y-k2+1)·k1!. C(x,k) is a degree-k polynomial in x with integer coeffs.
hypotheses: none beyond the definition
holds-here: yes — this is the exact rewriting of the curve C(x,k1)=C(y,k2)
  that BST treat and that the genus grid computes.
status: definitional (elementary algebra, immediately verifiable)
bearing: connects the binomial curve to the equal-products Diophantine theory
  that carries the ineffectivity obstruction and the genus classification.
anchor: research/sources/falling-factorial.full.md
```

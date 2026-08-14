# Technique: the elementary factorisation method for the exponent-2 cases

**Status:** Method note written by the librarian to record the *technique* the run must execute, not a sourced answer. The published answers to the exponent-2 cases are deliberately NOT stored (problem.md instructs the run to re-derive them; storing them would defeat the exercise and the evidence policy screens them).

**Type:** derivable elementary technique note.

## The technique, stated as a method

For `x^p - y^q = 1`, when one exponent is 2 there is a factorisation over Z or Z[i], and the equation closes by a coprime-factor argument. This is the base of everything — the run must redo both before working in Z[zeta_p].

### Case A: `x^2 - y^q = 1` (one exponent is 2 on the x side)

```
y^q = x^2 - 1 = (x - 1)(x + 1)
```

The two factors x-1 and x+1 have gcd dividing 2 (both even iff x odd, else coprime). The technique:
1. Split on parity of x.
2. When gcd is 1: both factors are coprime, and since their product is a q-th power, each is (up to sign) a q-th power — say x-1 = a^q, x+1 = b^q. Then b^q - a^q = 2, and one bounds small q.
3. When gcd is 2 (x odd): factor out 2; the coprime products (x-1)/2 and (x+1)/2 multiply to y^q/2^q, so each is a q-th power of coprime integers a, b with b^q - a^q = 1 (after absorbing the 2-power). Then b - a divides b^q - a^q = 1, forcing b - a = 1; and one uses that (a+1)^q - a^q < 2 for q, together with size, to conclude the single small case.

### Case B: `x^p - y^2 = 1` (one exponent is 2 on the y side), p odd prime

```
x^p = y^2 + 1 = (y + i)(y - i)   in Z[i]
```
The technique:
1. Work in Z[i], a Euclidean (hence UFD) ring.
2. y+i and y-i have gcd dividing the fixed Gaussian integer dividing 2 (specifically dividing 2i, and power of (1+i)).
3. Since p is odd, use that the two factors are coprime off the prime (1+i) to deduce y + i = (unit)*(a + bi)^p in Z[i].
4. Subtract the conjugate and compare imaginary parts via the binomial theorem; force b = ±1 and then a = 0 or a contradiction to odd p, giving no positive solution.

## Why this is in the library

The GOAL requires this run to re-derive both exponent-2 cases fully (they are "the cheapest real content and the calibration for everything else"). This note records the *method* — the coprime-factor / Gaussian-integer binomial technique — so the run executes it rather than searching for it. It contains no published final answer; the run derives the conclusion.

## The chosen-not-stored items

Lebesgue's theorem (`x^2 - y^n = 1`) and the `x^p - y^2 = 1` no-solution result are classical published answers that the evidence policy screens and that problem.md instructs us to re-derive. Both are recorded here only as the *method*, and their verification is deferred to the run's own exact oracle + proof, not to a downloaded source.

> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/gbroxey-summing-multiplicative-functions.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://gbroxey.github.io/blog/2023/04/30/mult-sum-1.html | converted from HTML -->

## What is in it

    - Contents
  - Techniques
    - Naive Method
    - Dirichlet Hyperbola Method
    - Tangent: Linear Sieving
    - Summing Generalized Divisor Functions
      - Algorithm (Computing $D_k$(x) Iteratively)
    - Summing $\mu$ and $\varphi$
      - Computing $M(x)$ in Sublinear Time
      - Algorithm (Mertens in $O(x^{3/4})$)
      - Algorithm (Mertens in $O(x^{2/3})$)
      - Doing It For $\varphi$?
    - Powerful Numbers Trick
      - Bell Series
      - Algorithm (Powerful Numbers Iterator)
      - Note on Picking $g$
    - Tangent: How Not To Count Primes
    - Black Algorithm and Min-25 Sieve
  - Code


## What it claims

**Abstract.**I’ll exhibit some methods for computing partial sums of multiplicative functions. Knowledge of how to sum more basic functions is assumed. We’ll use the square root trick constantly, as well as some basic number theory.

---

A function $f(n)$ which maps the naturals to the set of complex numbers is called “multiplicative” if $f(mn) = f(m)f(n)$ for any $m, n$ such that $\gcd(m, n) = 1$. There are a few obvious examples and a few less obvious examples:

- $I(1) = 1$ and $I(n) = 0$ for $n > 1$
- $u(n) = 1$ for all $n$
- $N(n) = n$ for all $n$
- $d(n)$, the number of divisors of $n$
- $\sigma_\alpha(n)$, the sum of $d^\alpha$ over all divisors $d$ of $n$
- $\mu(n)$, the [Möbius function][1]
- $\varphi(n)$, the [totient function][2]

Some of these are also completely multiplicative, meaning that $f(mn) = f(m)f(n)$ even if $\gcd(m, n) > 1$. This is true of $I$, $u$, and $N$, but not of the rest.

One operation which is incredibly helpful in the context of multiplicative functions is Dirichlet convolution, defined as

\[(f*g)(n) = \sum_{ab=n} f(a)g(b)\]

This convolution has…

## Statements it makes

#### Algorithm (Computing $D_k$(x) Iteratively)

#### Algorithm (Mertens in $O(x^{3/4})$)

#### Algorithm (Mertens in $O(x^{2/3})$)

#### Algorithm (Powerful Numbers Iterator)

*[digest of a 47894 character source; every section, statement, and proof in full at `research/sources/gbroxey-summing-multiplicative-functions.full.md`]*

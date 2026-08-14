# OEIS A018805 — ordered coprime pairs in an n×n square

Source: https://oeis.org/A018805 — full text at
`research/sources/oeis-A018805-coprime-pairs.full.md`
[[oeis-A018805-coprime-pairs.full]]

## What this source establishes

**Definition.** a(n) = #{(x,y) : 1 ≤ x,y ≤ n, gcd(x,y)=1}, the number of
ordered coprime pairs in an n×n square.

**Formulas.**

    a(n) = 2·Φ(n) − 1                       (Φ = summatory totient, A002088)
    a(n) = n² − Σ_{j=2..n} a(⌊n/j⌋)         (the recursion Chai Wah Wu's
                                             A063985 recursion is based on)
    a(n) = Σ_{k=1..n} μ(k)·⌊n/k⌋²
    a(n) ~ (6/π²)·n²

The identity "the number of ordered pairs (i,j) with 1≤i,j≤n, gcd(i,j)=d is
a(⌊n/d⌋)" (Sloane, Jul 29 2012) is the regrouping that underlies the
floor-grouped recursions.

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Provides the recursion base for the independent A063985 route to
  H(10⁸) (patterns.py).
- Confirms the visible-point density constant 6/π² used as a sanity anchor.

## What it does not settle

- Nothing about the hexagonal orchard directly.

## Claims

```claim
id: coprime-pairs-square-recursion
statement: a(n) = n² − Σ_{j=2..n} a(⌊n/j⌋) for a(n) = #{(x,y): 1≤x,y≤n,
gcd(x,y)=1} (OEIS A018805); equivalently a(n) = 2Φ(n) − 1.
hypotheses: n ≥ 1 integer.
holds-here: yes — basis of the A063985 recursion checked at n = 10^8.
status: sourced (OEIS A018805 formula); checked here by patterns.py.
bearing: the recursion behind the independent verification route to H(10^8).
anchor: research/summaries/oeis-A018805-coprime-pairs.md
```

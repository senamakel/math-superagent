# OEIS A063985 — partial sums of the cototient

Source: https://oeis.org/A063985 — full text at
`research/sources/oeis-A063985-partial-sums-n-minus-phi.full.md`
[[oeis-A063985-partial-sums-n-minus-phi.full]]

## What this source establishes

**Definition.** a(n) = Σ_{x=1..n} (x − φ(x)) = C(n+1,2) − Φ(n), the partial
sums of the cototient A051953. H(n) = 6·a(n) for the hexagonal orchard
(A216453), so a(10⁸) = H(10⁸)/6.

First values: 0, 1, 2, 4, 5, 9, 10, 14, 17, 23, 24, 32, … (matches the run's
`code/out/seq_A063985.txt`).

**Chai Wah Wu's recursion (Mar 24 2021), based on the A018805 identity
a(n) = n² − Σ_{j=2..n} a(⌊n/j⌋):**

    A063985(0) = 0
    j = 2; c = 0
    while (k1 := n//j) > 1:
        j2 = n//k1 + 1
        c += (j2 − j)·(k1·(k1+1) − 2·A063985(k1) − 1)
        j, k1 = j2, n//j2
    return (2n + c − j)//2

This is a floor-grouped, O(√n)-distinct-values recursion needing no sieve and
no Möbius function — a fully independent route to a(10⁸) and hence H(10⁸).

**Comment.** a(n) counts pairs (x,y) with 1 ≤ x ≤ y ≤ n, gcd(x,y) > 1 —
the per-sector hidden-point count of the orchard.

## Hypotheses

n ≥ 0 integer; recursion exact integer arithmetic. Holds here.

## What it lets this run do

- Third independent route to the answer: `code/out/patterns.py` computed
  A063985_rec(10⁸) = 1960364533634092, matching the sieve exactly, and
  H(10⁸) = 6·a(10⁸) = 11762187201804552.
- Verification probes a(10^k) k=1..5 match the sieve (command log: 23, 2006,
  196308, 19607514, 1960399246).

## What it does not settle

- No closed form for a(n) beyond the recursion and the definition; the value
  of a(10⁸) is computed by the run, not listed here.

## Claims

```claim
id: totient-sum-fast-recursion
statement: A063985(n) = (2n + c − j)//2 with j starting at 2 and
c = Σ over distinct values k1 = n//j of (j2−j)·(k1(k1+1) − 2·A063985(k1) − 1),
j2 = n//k1 + 1, iterating while k1 > 1 (Chai Wah Wu, Mar 24 2021).
hypotheses: n ≥ 0 integer; recursion on A063985(0)=0.
holds-here: yes — patterns.py reproduces the sieve at every probe ≤ 10^8,
including A063985_rec(10^8) = 1960364533634092.
status: checked — patterns.py reproduces the sieve at every probe ≤ 10^8,
including A063985_rec(10^8) = 1960364533634092; recursion sourced from OEIS
A063985 (Chai Wah Wu).
bearing: independent verification of H(10^8) = 6·A063985(10^8) =
11762187201804552.
anchor: research/summaries/oeis-A063985-partial-sums-n-minus-phi.md
```

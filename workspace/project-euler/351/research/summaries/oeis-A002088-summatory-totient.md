# OEIS A002088 — summatory totient

Source: https://oeis.org/A002088 — full text at
`research/sources/oeis-A002088-summatory-totient.full.md`
[[oeis-A002088-summatory-totient.full]]

## What this source establishes

**Definition.** a(n) = Φ(n) = Σ_{k=1..n} φ(k), the summatory totient
(A000010). First values (offset 0): 0, 1, 2, 4, 6, 10, 12, 18, 22, 28, 32, …
(matches the run's `code/out/seq_Phi.txt`).

**Key combinatorial interpretation (used by this run).** a(n) is the number of
ordered pairs (x,y) with 1 ≤ x ≤ y ≤ n and gcd(x,y)=1 (Michael Somos), i.e.
the visible points in one sector of the orchard; equivalently the number of
reduced fractions p/q in (0,1] with denominator q ≤ n. Also: number of
elements of {(x,y): 1 ≤ x+y ≤ n, x ≥ 0, y > 0, gcd(x,y)=1} (Rick L. Shepherd)
— the visible points in the first octant.

**Asymptotic.** Φ(n) ~ (3/π²)n² (see A064018 comment: a(n) ~ 0.30396355·n²).

## Hypotheses

n ≥ 0 integer. Holds here.

## What it lets this run do

- Confirms the per-sector visible count = Φ(n), the structural step of the
  closed form H(n) = 6(C(n+1,2) − Φ(n)).
- Provides the magnitude anchor for Φ(10⁸).

## What it does not settle

- No sublinear algorithm; no values at 10⁸ (that is A064018).

## Claims

```claim
id: summatory-totient-counts-visible-pairs
statement: Φ(n) counts the ordered pairs (x,y) with 1 ≤ x ≤ y ≤ n and
gcd(x,y) = 1; hence the number of visible points in one sector of the
hexagonal orchard of order n (pairs with 1 ≤ x+y ≤ n, x,y ≥ 1, gcd=1) is Φ(n).
hypotheses: n ≥ 1 integer.
holds-here: yes — with the run's derivation this gives H(n) = 6(C(n+1,2) − Φ(n)),
verified against brute force at n = 5, 10, 1000.
status: sourced (OEIS A002088 comments); the orchard-sector step is this run's
derivation, checked by brute.py.
bearing: structural link between orchard visibility and the totient sum.
anchor: research/summaries/oeis-A002088-summatory-totient.md
```

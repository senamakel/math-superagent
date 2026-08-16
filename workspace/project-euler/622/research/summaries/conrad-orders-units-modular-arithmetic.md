# Conrad, "Orders of units in modular arithmetic"

Source: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/ordersmodm.pdf · full text: [[conrad-orders-units-modular-arithmetic.full]]

## What it establishes

The elementary theory of the multiplicative order, developed cleanly for units
mod m.

**Theorem 2.1** (verified at line 108): Let a mod m have order n. For k ≥ 0,
  a^k ≡ 1 (mod m)  iff  n | k.
**Corollary 2.2** (line 125): if (a,m)=1 and a mod m has order n then n | φ(m)
(via Euler's theorem + Thm 2.1).
**Theorem 2.4**: a^k ≡ a^ℓ (mod m) iff k ≡ ℓ (mod n).
**Theorem 3.2**: order of a^k = n/(k,n).
**Theorem 5.2 / Cor 5.7**: orders of products; [n1,n2] lcm bound.

## Consequences for this problem

The exact criterion `ord_m(2) = 60 iff m | 2^60−1 and no proper divisor d of
60 has 2^d ≡ 1 (mod m)` is *exactly* Thm 2.1 applied with n=60: 2^60≡1 mod m
iff ord | 60 iff m | 2^60−1; and minimality (no smaller d works) is what makes
the order exactly 60. Cor 2.2 (n | φ(m)) gives the Gauss–Carmichael λ bound
referenced by Pomerance. This is the divisibility engine that bounds the search
to divisors of 2^60−1.

## Does not settle

- The permutation/shuffle connection (that is DGK/Packard/Pomerance).
- The lcm combination over distinct primes (Chappelon).
- The numerical answer.

## Status

All proved in the source. Hypotheses (a unit, i.e. gcd(2,m)=1) hold here since
m = n−1 is odd. Load-bearing for "divisors of 2^60−1" finiteness.

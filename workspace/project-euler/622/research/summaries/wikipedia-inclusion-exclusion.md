# Wikipedia — Inclusion–Exclusion Principle (PIE)

Source: https://en.wikipedia.org/wiki/Inclusion–exclusion_principle · full text: [[wikipedia-inclusion-exclusion.full]]

## What it establishes

The canonical encyclopedic statement of the **inclusion–exclusion principle**
(PIE) for finite sets. Two-set case: |A ∪ B| = |A| + |B| − |A ∩ B|.

**General finite form** (for finite sets A_1, …, A_n):
```
|A_1 ∪ … ∪ A_n| = sum_{nonempty J ⊆ {1..n}} (-1)^{|J|+1} |∩_{i∈J} A_i|
```
i.e. alternating sum over intersections; from the third line on it is
|A| = Σ|A_i| − Σ|A_i∩A_j| + Σ|A_i∩A_j∩A_k| − … . There is an algebraic
(double-counting) proof given, counting each element by how many of the sets
contain it. A special case (indicators on a subset lattice) is the form the
divisor-lattice inclusion-exclusion in this run uses.

## Consequences for this problem

Anchors the `G-inclusion-exclusion` rung of the blueprint: with
M = { m | N : m ∤ 2^12−1, m ∤ 2^20−1, m ∤ 2^30−1 } and A_d = { m | N : m | 2^d−1 },
the count and sum of M are the alternating sums of the divisor-sums/counts of the
intersections A_{12}∩A_{20}, etc. The intersections reduce by the Mersenne-gcd
identity gcd(2^a−1, 2^b−1) = 2^{gcd(a,b)}−1 (G-gcd-mersenne), turning each
intersection into a divisor-sum of a small number (e.g. A_12∩A_20 =
divisors of 2^{gcd(12,20)}−1 = 2^4−1 = 15), which is exactly the
sigma(15), sigma(63), sigma(1023), sigma(3) inclusion-exclusion in the
blueprint.

## Does not settle

- The numerical values (those come from G-divisor-sums / G-factorization).
- The Mersenne-gcd reduction (that is G-gcd-mersenne / Wolfram GCD page).

## Status

Encyclopedic. The measure-theoretic and indicator-lattice statements also
appear here; the finite-set cardinality form is the one the rung needs.

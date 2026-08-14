# PE 351 — governing theory: hexagonal orchard hidden points

Established from sources in this library. Sources: OEIS A216453, A063985, A002088,
A064018, A018805; MathWorld VisiblePoint, TotientSummatoryFunction; Wikipedia
Totient summatory function; arXiv:2506.07386 (Brown 2025).

```claim
id: pe351-hidden-formula
statement: H(n) = 6 * (C(n+1,2) - sum_{i=1..n} phi(i)) = 6 * sum_{i=1..n} (i - phi(i)),
where phi is Euler's totient function. Equivalently H(n) = 6 * A063985(n).
hypotheses: n >= 1; the orchard is a triangular lattice in a regular hexagon of
side n; "hidden from the center" means a strictly closer lattice point lies on
the segment from the center to the point.
holds-here: yes — this is exactly the problem's definition (problem.md).
status: sourced (OEIS A216453 formula, corrected by Piyush Kumar and Robert
Israel, Aug 26 2014; also reproduced by the program outputs of multiple
independent solvers).
bearing: reduces the problem to computing the summatory totient
Phi(n) = sum_{i=1..n} phi(i) at n = 10^8.
anchor: research/summaries/oeis-A216453-hexagonal-orchard-hidden.md
```

```claim
id: summatory-totient-mobius-identity
statement: sum_{i=1..n} phi(i) = (1/2) * (1 + sum_{d=1..n} mu(d) * floor(n/d)^2),
where mu is the Moebius function. Equivalently
Phi(n) = (1/2) * sum_{d=1..n} mu(d) * floor(n/d) * (1 + floor(n/d)).
hypotheses: n >= 1 integer.
holds-here: yes.
status: sourced (MathWorld TotientSummatoryFunction; Wikipedia Totient
summatory function; derived by Mobius inversion from phi(n) = sum_{d|n} mu(d) n/d).
bearing: converts the totient sum into a sum over mu(d) * floor(n/d)^2 whose
terms can be grouped by equal floor values, giving an O(sqrt(n))-time evaluation
once the prefix sums of mu (Mertens function) are known.
anchor: research/summaries/mathworld-totient-summatory-function.md
```

```claim
id: coprimality-iff-visible
statement: A lattice point (x,y) is visible from the origin iff gcd(x,y) = 1;
a point is hidden iff its coordinates have gcd > 1, since then
(x/g,y/g) is a strictly closer lattice point on the same ray.
hypotheses: integer lattice Z^2, origin excluded.
holds-here: yes — the triangular lattice is a sublattice of Z^2 (or the
hexagonal lattice is isomorphic to Z^2 as an additive group), so the visibility
criterion transfers.
status: sourced (MathWorld VisiblePoint; Mosseri 1992; Baake–Grimm–Warrington 1994).
bearing: the hidden-point count in each of the six sectors of the orchard is the
count of non-coprime pairs in a triangle, i.e. C(n+1,2) - Phi(n) per sector.
anchor: research/summaries/mathworld-visible-point.md
```

```claim
id: totient-sum-verification-values
statement: Phi(10^k) for k = 0..8 is
1, 32, 3044, 304192, 30397486, 3039650754, 303963552392, 30396356427242,
3039635516365908  (OEIS A064018).
hypotheses: none.
holds-here: yes — k = 8 gives Phi(10^8) = 3039635516365908, the independent
check value for the final computation.
status: sourced (OEIS A064018; Brown 2025 computed through 10^19).
bearing: the final answer can be verified independently:
H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8); substituting the catalogue value must
reproduce the program's answer.
anchor: research/summaries/oeis-A064018-totient-summatory-powers-of-10.md
```

```claim
id: totient-sum-fast-recursion
statement: A063985(n) = (2*n + c - j) // 2 where j starts at 2 and the sum
c = sum over distinct values k1 = n//j of (j2-j)*(k1*(k1+1) - 2*A063985(k1) - 1)
with j2 = n//k1 + 1, iterating while k1 > 1 (Chai Wah Wu's recursion, based on
the identity in A018805). H(n) = 6 * A063985(n).
hypotheses: n >= 0.
holds-here: yes — this is a self-contained O(sqrt(n))-style recursion that needs
no sieve, giving a second independent route to H(10^8) to check the sieve-based
method.
status: sourced (OEIS A063985, Chai Wah Wu Mar 24 2021; recursion based on
A018805 formula a(n) = n^2 - sum_{j=2..n} a(floor(n/j))).
bearing: independent verification path: implement this recursion directly and
compare with the sieve-based summatory totient at n = 10^8.
anchor: research/summaries/oeis-A063985-partial-sums-n-minus-phi.md
```

```claim
id: gauss-divisor-sum-of-totient
statement: sum_{d|n} phi(d) = n for every positive integer n (Gauss); hence
sum_{d=1..n} Phi(floor(n/d)) = n(n+1)/2, which rearranges to the summatory
recursion Phi(n) = n(n+1)/2 - sum_{d=2..n} Phi(floor(n/d)), evaluated in
O(sqrt(n)) distinct floor values with memoisation.
hypotheses: n >= 1.
holds-here: yes — this is the identity the backward skeleton's G2 lemma and the
weakener's R4 rung rest on.
status: sourced (MathWorld TotientFunction eq. (15); Wikipedia Totient
summatory function "Properties": sum_{d=1..n} Phi(n/d) = n(n+1)/2, giving an
implicit recurrence).
bearing: the recursion is the sublinear route to Phi(10^8) (O(n^{2/3}) time
with memoisation at floor(n/d) points), and a second independent route to
verify the sieve value.
anchor: research/sources/mathworld-totient-function.full.md
```

## What the computation reduces to

1. Compute the summatory totient Phi(n) = sum_{i<=n} phi(i) at n = 10^8.
   Methods: (a) linear sieve for phi up to 10^8 (feasible: 10^8 32-bit ints,
   O(n) time) or a segmented/block approach; (b) the Mobius identity with
   floor grouping needing prefix Mertens values; (c) the A063985 recursion.
2. H(n) = 6 * (n(n+1)/2 - Phi(n)) = 3*n*(n+1) - 6*Phi(n).
3. Check against Phi(10^8) = 3039635516365908 (A064018).

Expected magnitude: H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8)
= 30000000300000000 - 6*3039635516365908      [3*10^8*(10^8+1) = 3*10000000100000000]
= 30000000300000000 - 18237813098195448
= 11762187201804552  (17 digits).
[Corrected by librarian 2026-08-14: the earlier draft wrote
30000003000000000 (dropped a 0) and 11762189901804552; the exact value is
30000000300000000 and 11762187201804552. Verify with a program before use.]
This is the check anchor: the program's final answer must equal this integer,
which follows from the catalogued Phi(10^8) value.  The magnitude is
H(n) ~ 3n^2(1 - 6/pi^2) ~ 1.176e16 at n=10^8, consistent.

# Project Euler 351 — hexagonal orchard: derivation of the efficient method

## Result it rests on

**Closed form (OEIS A216453, Kumar–Israel formula).** For every n ≥ 1,

    H(n) = 6·(C(n+1,2) − Φ(n)) = 3n² + 3n − 6·Φ(n),
    Φ(n) = Σ_{k=1..n} φ(k),   φ(k) = #{1 ≤ m ≤ k : gcd(m,k) = 1}.

## Why it applies — the geometric-to-arithmetic bridge

A point (a,b) ≠ (0,0) of the orchard — the axial-coordinate hexagon
{(a,b) ∈ Z² : |a| ≤ n, |b| ≤ n, |a+b| ≤ n} — is hidden from the centre iff a
strictly closer lattice point lies on the same ray. Let g = gcd(|a|,|b|). The
closest lattice point on the ray is (a/g, b/g); it is a strictly closer
orchard point iff g ≥ 2. Hence

    hidden ⟺ gcd(|a|,|b|) > 1          (coprime iff visible, MathWorld
                                         VisiblePoint; Baake–Grimm–Warrington)

and the origin is never hidden. This criterion is checked against a literal
no-number-theory scan (only the definition) for n ≤ 8 and against the
statement's oracles at n = 5, 10, 1000.

The hexagon splits into six congruent sectors (the six 60° cones). In one
sector, e.g. {(a,b) : 1 ≤ b < a ≤ n} plus the axes handled by symmetry, the
visible points are the coprime pairs with 1 ≤ a+b ≤ n, a,b ≥ 1, and their
count is exactly Φ(n) (OEIS A002088: Φ(n) counts ordered coprime pairs
1 ≤ x ≤ y ≤ n; equivalently the reduced fractions with denominator ≤ n, i.e.
the Farey length |F_n| = 1 + Φ(n)). The sector has C(n+1,2) points, so each
sector contributes C(n+1,2) − Φ(n) hidden points and

    H(n) = 6·(C(n+1,2) − Φ(n)) = 3n(n+1) − 6Φ(n).

## What the reduction achieves

All geometric content is gone: the problem is the summatory totient Φ at
n = 10⁸. Three independent exact routes to Φ(10⁸):

1. **Incremental totient sieve** (adopted; `code/lib/totient.py`): phi[i]
   starts at i; for each prime p, every multiple m of p gets
   phi[m] −= phi[m]//p (the product formula φ(m) = m·∏(1−1/p)). O(n log log n)
   time, int32 table (φ(m) ≤ m < 2³¹), exact integer sum in int64.
   Φ(10⁸) = 3039635516365908.
2. **Möbius inversion** (`code/verify_mobius.py`): from φ = μ ∗ id
   (ProofWiki; MathWorld eq. 16), summing and regrouping gives
   Φ(n) = (1/2)Σ_{d≤n} μ(d)⌊n/d⌋(1+⌊n/d⌋) (MathWorld / Wikipedia Totient
   summatory function). Separate int8 μ sieve (multiples of p² zeroed with
   step p² — the step-p bug is recorded in `code/out/fix_mobius_verify.py`).
   Exact agreement at every probe ≤ 10⁸.
3. **Chai Wah Wu's A063985 recursion** (OEIS A063985, Mar 24 2021;
   `code/out/patterns.py`): sieve-free, floor-grouped recursion for
   A063985(n) = C(n+1,2) − Φ(n); A063985(10⁸) = 1960364533634092 and
   H(10⁸) = 6·A063985(10⁸) match the sieve exactly. This is the independent
   "different derivation" route (it never computes φ pointwise).

The Möbius-identity route with floor grouping is also the Θ(n^{2/3})
sublinear algorithm of Brown (arXiv:2506.07386), whose Table 1 and
`totientsum.py` provide further catalogue checks (Φ(10¹⁹) = 3039635509270133
1435065976498046398788). For n = 10⁸ the direct sieve is comfortably
feasible, so the sublinear machinery is verification context, not the method.

## Verification

- `code/brute.py` (oracle): enumerates all 3n²+3n+1 points, counts hidden by
  the definition (gcd test): H(5)=30, H(10)=138, H(1000)=1177848 — the
  statement's values.
- `code/solution.py` parity table: identity vs oracle at n = 5, 10, 1000 — OK
  at every row.
- Φ(10⁸) by two independent sieves (routes 1 and 2): exact agreement.
- Φ(10^k), k = 0..8, reproduced by a naive sieve against OEIS A064018
  (`code/out/check_library_values.py`).
- A216453 terms n = 1..20 computed by the sieve match the OEIS entry
  (oeis_lookup hit).
- Final arithmetic: H(10⁸) = 30000000300000000 − 6·3039635516365908 =
  **11762187201804552**; also H(10⁸) = 6·1960364533634092 (route 3).

## Complexity

- brute.py: O(n²) time — oracle only, n ≤ 1000.
- solution.py: O(N log log N) time, O(N) 32-bit words (N = 10⁸ ≈ 400 MB) —
  exact integer arithmetic throughout, no floating point in the answer.
- verify_mobius.py: same class, separate sieve.
- patterns.py recursion: O(√n) distinct floor values with memoisation.

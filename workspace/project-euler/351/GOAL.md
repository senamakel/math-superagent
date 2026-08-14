# Goal

Project Euler 351 (hexagonal orchard), solved directly without consulting any
published answer.

## Problem restated, with every symbol defined

A **hexagonal orchard of order n** is a triangular lattice made up of the
points within a regular hexagon of side n. In axial coordinates:

    Orchard(n) = {(a,b) ∈ Z² : |a| ≤ n, |b| ≤ n, |a+b| ≤ n}

which has exactly 3n² + 3n + 1 points (the hexagon is a lattice polygon, so
this is its Ehrhart polynomial; brute.py asserts it on every run).

A point (a,b) ≠ (0,0) is **hidden from the centre** iff a strictly closer
orchard point lies on the segment from (0,0) to (a,b). In this lattice that
holds iff gcd(|a|,|b|) > 1, because (a/g, b/g) with g = gcd(|a|,|b|) is the
closest lattice point on the ray, and it is inside the orchard iff g ≥ 2. The
origin is never hidden (no point is strictly between it and itself).

H(n) = number of hidden points in Orchard(n).

## Test oracle (worked examples from the statement)

- H(5) = 30
- H(10) = 138
- H(1000) = 1177848

`code/brute.py` reproduces all three by literal enumeration (O(n²), gcd test);
`code/solution.py` reproduces them via the totient identity.

## Completion criteria (all met)

- [x] `code/brute.py`: naive enumeration oracle, prints H(5)=30, H(10)=138,
      H(1000)=1177848 — all match the given values.
- [x] `code/solution.py`: exact H(n) = 3n^2 + 3n - 6*Phi(n) via an Euler
      totient sieve; parity table for n=5,10,1000 matches brute force; then
      computes Phi(10^8) and H(10^8) exactly with a memory-efficient int32
      sieve.
- [x] Phi(10^8) verified by a second, independent route (Möbius inversion)
      and by a third (Chai Wah Wu's A063985 recursion).
- [x] Exact integers recorded in code/out/pe351_values.md.

Final values: Phi(10^8) = 3039635516365908,
H(10^8) = 11762187201804552.

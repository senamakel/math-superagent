"""Brute force for Project Euler 351 (hexagonal orchard).

A hexagonal orchard of order n is the set of points with
triangular/axial coordinates {(a, b) : |a| <= n, |b| <= n, |a + b| <= n}.
A point is hidden iff there is another lattice point strictly between it
and the origin on the same ray; for a point at (a, b) (a and b not both 0)
that happens iff gcd(a, b) > 1, i.e. the direction (a,b)/gcd(a,b) has
already been "occupied" by a closer point.  The origin itself is NOT
counted as hidden (no point strictly between (0,0) and (0,0) exists); this
matches the given oracle values 30, 138, 1177848.

This enumerates every point of the hexagon directly -- O(n^2) points, fine
for n = 5, 10, 1000 -- and counts hidden ones with a gcd test.  It is the
oracle for solution.py: if this matches the given values 30, 138, 1177848
and solution.py's totient identity matches this, the identity is verified.
"""

from math import gcd


def hexagon_points(n):
    """Iterate all points (a, b) of the order-n hexagon in axial coords."""
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if abs(a + b) <= n:
                yield a, b


def H_brute(n):
    """Number of hidden points in the order-n hexagonal orchard by enumeration."""
    count = 0
    pts = 0
    for a, b in hexagon_points(n):
        pts += 1
        if not (a == 0 and b == 0) and gcd(abs(a), abs(b)) > 1:
            count += 1
    assert pts == 3 * n * n + 3 * n + 1, (n, pts)
    return count


if __name__ == "__main__":
    for n in (5, 10, 1000):
        print(f"H({n}) = {H_brute(n)}")
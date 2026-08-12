#!/usr/bin/env python3
"""Pattern-finder: extract integer structure from the n-gon critical-speed formula.

The critical speed for a regular n-gon (stewbasic, Math.SE 1762665):
    theta = pi/n, t = tan(theta)
    K(n) = largest integer with sin(K*theta) - (K+n)*t*cos(K*theta) < 0
    alpha = 1/2*( K*theta + acos( 2 sin(K theta)/((K+n) t) - cos(K theta) ) )
    V(n) = 1/cos(alpha)

K(n) is the integer sequence worth testing for structure (period-7 conjecture
claimed in solution_hexagon_pattern.md to hold through n=85 then deviate).
V(n) for small n may have exact closed forms like the square and triangle.
"""
import math


def K_of_n(n, exact=False):
    """Largest integer k in [0,n] with sin(k*pi/n) - (k+n)*tan(pi/n)*cos(k*pi/n) < 0."""
    th = math.pi / n
    t = math.tan(th)
    K = None
    for k in range(0, n + 1):
        val = math.sin(k * th) - (k + n) * t * math.cos(k * th)
        if val < 0:
            K = k
    return K


if __name__ == "__main__":
    # Print K(n) and its first difference n=3..100
    Ks = []
    diffs = []
    prev = None
    for n in range(3, 101):
        k = K_of_n(n)
        Ks.append(k)
        if prev is not None:
            diffs.append(k - prev)
        prev = k
    print("K(3..100):")
    print(Ks)
    print("\nfirst differences (period-7 conjecture says pattern [?,...] repeats):")
    print(diffs)
    print("\nn where K(n) differs from floor(3n/7):")
    fl = [math.floor(3 * n / 7) for n in range(3, 101)]
    bad = [n for n in range(3, 101) if K_of_n(n) != fl[n - 3]]
    print("n in 3..100 where K(n) != floor(3n/7):", bad)

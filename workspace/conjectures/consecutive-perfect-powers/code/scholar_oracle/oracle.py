"""Faster exact oracle. For x^p - y^q = 1 with x^p,y^q <= N, note the only
1 is 3^2-2^3=1. Enumerate perfect powers as the set, check consecutive."""
import math


def perfect_powers_upto(N):
    """Set of all perfect powers (n >= 2) with value <= N, plus reps."""
    powers = {}  # value -> list of (base, exp)
    x = 2
    while x * x <= N:
        v = x * x
        e = 2
        while v <= N:
            powers.setdefault(v, []).append((x, e))
            v *= x
            e += 1
        x += 1
    return powers


def solutions(N):
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:
        if u - 1 in powers:
            for (x, p) in powers[u]:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.add((x, p, y, q))
    return sorted(result)


if __name__ == "__main__":
    import time
    for N in (9, 100, 1000, 10**4, 10**5, 10**6, 10**7, 10**8):
        t = time.time()
        r = solutions(N)
        print(N, r, "%.2fs" % (time.time() - t))

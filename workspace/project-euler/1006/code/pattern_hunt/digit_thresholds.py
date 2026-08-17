"""PE1006: binary-search the exact digit-excess transition points.

Excess e(k) = digits(Psi(k)) - (2k-1) is non-decreasing (digits grow by
~2 per k plus occasional carry-ups).  Observed: e=0 for k<=23, e=1 for
24..~, e=2 beyond ~200.  Binary search each boundary.
"""
from fractions import Fraction
import time


def fib_list(N):
    out = [0, 1]
    while out[-1] <= N:
        out.append(out[-1] + out[-2])
    return out


def slope_for(k, fibs):
    n = 0
    while True:
        if fibs[n + 2] > k:
            return Fraction(fibs[n], fibs[n + 2])
        n += 1


def frac(r):
    return r - (r.numerator // r.denominator)


def arc_midpoints(k, a):
    pts = sorted(frac((-j) * a) for j in range(k + 1))
    xs = [(pts[i] + pts[i + 1]) / 2 for i in range(k)]
    w = (pts[k] + pts[0] + 1) / 2
    if w >= 1:
        w -= 1
    xs.append(w)
    return xs


def v_telescoped(x, k, a):
    fl = lambda r: r.numerator // r.denominator
    s = fl(x + k * a) - 10 ** (k - 1) * fl(x)
    for j in range(1, k):
        s += 9 * 10 ** (k - 1 - j) * fl(x + j * a)
    return s


def psi_direct(k, a):
    return sum(v_telescoped(x, k, a) ** 2 for x in arc_midpoints(k, a))


_cache = {}
def excess(k, fibs):
    if k in _cache:
        return _cache[k]
    a = slope_for(k, fibs)
    p = psi_direct(k, a)
    e = len(str(p)) - (2 * k - 1)
    _cache[k] = e
    return e


def first_at_least(thresh, lo, hi, fibs):
    """smallest k in [lo, hi] with excess(k) >= thresh (monotone)."""
    while lo < hi:
        mid = (lo + hi) // 2
        if excess(mid, fibs) >= thresh:
            hi = mid
        else:
            lo = mid + 1
    return lo, excess(lo, fibs)


def main():
    fibs = fib_list(4 * 4000)
    # e>=1 first: known k=24; confirm via search 1..30
    k1, e1 = first_at_least(1, 1, 60, fibs)
    print(f"threshold e>=1 : k={k1} excess={e1}")
    # e>=2 first: between 150 and 300
    k2, e2 = first_at_least(2, 150, 400, fibs)
    print(f"threshold e>=2 : k={k2} excess={e2}")
    # e>=3 first: between 400 and some upper; probe
    k3, e3 = first_at_least(3, 400, 4000, fibs)
    print(f"threshold e>=3 : k={k3} excess={e3}")


if __name__ == '__main__':
    main()
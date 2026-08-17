"""PE1006: probe the digit excess at a handful of larger k.

The step model {excess 0 for k<=23, +1 for k>=24} held for k=1..150 computed
exactly.  Full sweep to 2000 timed out; probe instead at targeted points to
see whether the excess (digits(Psi) - (2k-1)) ever reaches +2, and where.

Single-k computation is O(k^2); these are cheap individually.
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


def main():
    fibs = fib_list(4 * 2000)
    for k in [60, 100, 150, 200, 300, 500, 800, 1200, 2000]:
        t0 = time.time()
        a = slope_for(k, fibs)
        p = psi_direct(k, a)
        nd = len(str(p))
        excess = nd - (2 * k - 1)
        dt = time.time() - t0
        print(f"k={k:5d} digits={nd:5d} 2k-1={2*k-1:5d} excess={excess:+d} ({dt:.1f}s)")


if __name__ == '__main__':
    main()
"""PE1006: test the digit-excess step pattern over a wide range.

Claim found this cycle: digits(Psi(k)) = 2k-1 for k <= 23 and = 2k for k >= 24
(within k=1..150).  Extend to k = 1..2000 to find the first falsifier -- i.e.
the first k where the excess over 2k-1 is NOT the step {0 for k<=23, 1 for
k>=24} (equivalently where digits - (2k-1) is neither 0 nor 1, or the step
position changes).

Uses the verified exact mechanical construction (psi_direct) from solution.py.
At k=2000 the exact integers have ~4000 digits and arc midpoints are Fractions
with denominator ~fib(17)~2584 > k -- exact, fast enough.
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
    KMAX = 2000
    fibs = fib_list(4 * KMAX)
    # locate step: first k with excess 1
    step_at = None
    first_weird = None
    first_nonstep = None
    t0 = time.time()
    for k in range(1, KMAX + 1):
        a = slope_for(k, fibs)
        p = psi_direct(k, a)
        nd = len(str(p))
        excess = nd - (2 * k - 1)
        if step_at is None and excess == 1:
            step_at = k
        if excess not in (0, 1):
            if first_weird is None:
                first_weird = (k, nd, 2 * k - 1, excess)
        # check the step model: excess should be 0 for k < 24, 1 for k >= 24
        expect = 0 if k < 24 else 1
        if excess != expect and first_nonstep is None:
            first_nonstep = (k, nd, 2 * k - 1, excess, expect)
    dt = time.time() - t0
    print(f"computed exact Psi digit counts for k=1..{KMAX} in {dt:.1f}s")
    print(f"step_at (first k with +1 excess) = {step_at}")
    print(f"excess ever outside {{0,1}}?  first: {first_weird}")
    print(f"first k where excess != step model (0 if k<24, 1 if k>=24): {first_nonstep}")
    if first_nonstep is None:
        print("STEP MODEL HOLDS for all k = 1..", KMAX, "(excess 0 for k<=23, 1 for k>=24)")


if __name__ == '__main__':
    main()
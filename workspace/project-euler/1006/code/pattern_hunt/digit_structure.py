"""PE1006: digit-count structure of exact Psi(k).

Observation from code/out/psi_exact.txt: Psi(k) has exactly 2k-1 digits for
k = 1..23, but Psi(24) and Psi(25) have 2k digits.  c1(k) = #leading-1
factors = 1 + floor(k/phi^2) crosses 10 at k = 24, so the conjecture is

    digits(Psi(k)) = 2k - 1 + floor(log10(c1(k)))

i.e. the excess over 2k-1 tracks the decimal length of the number of
leading-1 factors.  This program computes exact Psi(k) by the verified
mechanical construction (psi_direct, exact Fraction arithmetic — verified
against brute for k=1..60 and mod M for k=61..150 by solution.py) for
k = 1..150 and tabulates digit counts vs the conjecture.

Falsifier search: first k at which digits(Psi(k)) != 2k-1+floor(log10(c1(k))).
With c1(k) = 1+floor(k/phi^2) computed EXACTLY as floor via integer
arithmetic on (3-sqrt(5))/2 = 1/phi^2 using the identity
  floor(k/phi^2) = floor((k*(sqrt(5)-1))/2) --- integer z such that
  2z <= k(sqrt5-1) < 2z+2, checked with the exact rational bound
  (k*(sqrt5-1))/2 = z means k(sqrt5-1) in [2z, 2z+2), using
  isqrt(5 k^2) comparisons.

Exact: k*(sqrt(5)-1)/2  = (k*sqrt(5) - k)/2.  floor = z iff
  2z + k <= k*sqrt(5) < 2z + k + 2, i.e.
  (2z+k)^2 <= 5k^2 < (2z+k+2)^2.  All integer arithmetic.
"""
from fractions import Fraction
import math

M = 101001001


def fib_list(N):
    out = [0, 1]
    while out[-1] <= N:
        out.append(out[-1] + out[-2])
    return out


def slope_for(k, fibs):
    n = 0
    while True:
        if fibs[n + 2] > k:
            return Fraction(fibs[n], fibs[n + 2]), fibs[n], fibs[n + 2]
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


def c1_exact(k):
    """1 + floor(k/phi^2), phi^2 = (3+sqrt5)/2, exactly via integer sqrt tests."""
    # z = floor(k/phi^2): z is the least z with 5k^2 < (2z+k+2)^2... solve directly:
    # k/phi^2 = k*(sqrt5-1)/2.  z = floor iff 2z+k <= k*sqrt5 < 2z+k+2.
    # Find z by binary search on the integer z in [0, k].
    zlo, zhi = -1, k + 1  # zhi exclusive
    while zhi - zlo > 1:
        mid = (zlo + zhi) // 2
        # is floor(k/phi^2) >= mid ?  i.e. mid <= k/phi^2  i.e.  (2*mid+k)^2 <= 5k^2
        if (2 * mid + k) ** 2 <= 5 * k * k:
            zlo = mid
        else:
            zhi = mid
    z = zlo
    return 1 + z


def main():
    fibs = fib_list(4 * 150)
    rows = []
    first_fail = None
    for k in range(1, 151):
        a, m, N = slope_for(k, fibs)
        p = psi_direct(k, a)
        nd = len(str(p))
        c1 = c1_exact(k)
        pred = 2 * k - 1 + (0 if c1 == 1 else len(str(c1)) - 1)
        # floor(log10(c1)) = len(str(c1))-1
        ok = (nd == pred)
        if not ok and first_fail is None:
            first_fail = (k, nd, pred, c1)
        rows.append((k, nd, 2 * k - 1, nd - (2 * k - 1), c1, pred, ok))

    print("k  digits  2k-1  excess  c1(k)  pred  ok")
    for k, nd, b, exc, c1, pred, ok in rows:
        print(f"{k:3d} {nd:6d} {b:5d}  {exc:+d}     {c1:3d}   {pred:5d}  {ok}")
    print()
    if first_fail:
        print("FIRST FALSIFIER:", first_fail)
    else:
        print("conjecture holds for all k = 1..150")

    # also record exact values at the boundary k = F_m - 1 for m up to 14, to extend
    # the exact boundary sequence beyond k=20
    print()
    print("Exact Psi at k = F_m - 1 (extending the boundary subsequence):")
    f = [1, 2]
    while f[-1] <= 400:
        f.append(f[-1] + f[-2])
    for Fm in f:
        k = Fm - 1
        if k <= 150:
            a, m, N = slope_for(k, fibs)
            p = psi_direct(k, a)
            print(f"  F_m={Fm:3d} k={k:3d} digits={len(str(p))} Psi={p}")


if __name__ == '__main__':
    main()
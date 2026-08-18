#!/usr/bin/env python3
"""PE1006: corrected Wythoff-position conjecture for the M1 deviation.

Conjecture (corrected): for k = F_m (Fibonacci number, m >= 4),
  - m odd:  dev(j) = +1 iff j in { floor(t*phi^2) : t>=1, floor(t*phi^2) < k },
            dev(j) = 0 otherwise;
  - m even: dev(j) = -1 iff j in { floor(t*phi) : t>=1, floor(t*phi) < k },
            dev(j) = 0 otherwise.
At k = F_m - 1 the deviation is identically zero (recorded position balance).

Attack: exact test at k = F_17 = 1597 (odd) and F_18 = 2584 (even), beyond
the run's previous Fibonacci-boundary cap of 376.  Falsifier: first mismatch.
"""
from math import isqrt

SCALE = 4 ** 120
SQRT5 = isqrt(5 * SCALE * SCALE)


def floor_phi(n):
    return (n * SCALE + n * SQRT5) // (2 * SCALE)


def floor_phi2(n):
    return (3 * n * SCALE + n * SQRT5) // (2 * SCALE)


def c1(k):
    return 1 + (3 * k * SCALE - k * SQRT5) // (2 * SCALE)


def fib_q_gt(k):
    a, b = 1, 1
    while b <= k:
        a, b = b, a + b
    return b


def dev_digits(k):
    q = fib_q_gt(2 * k)
    f = [1, 1]
    while f[-1] < q:
        f.append(f[-1] + f[-2])
    p = f[-3]
    pts = sorted(((-m * p) % q) for m in range(k + 1))
    c = c1(k)
    pc = [0] * k
    for i in range(k + 1):
        c1p = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + q
        for j in range(k):
            lo = (c1p + c2 + 2 * j * p) // (2 * q)
            hi = (c1p + c2 + 2 * (j + 1) * p) // (2 * q)
            pc[j] += hi - lo
    return [pc[j] - c for j in range(k)]


def wyth_upper_lt(k):
    out = []
    t = 1
    while True:
        v = floor_phi2(t)
        if v >= k:
            break
        out.append(v)
        t += 1
    return out


def wyth_lower_lt(k):
    out = []
    t = 1
    while True:
        v = floor_phi(t)
        if v >= k:
            break
        out.append(v)
        t += 1
    return out


def test(k):
    dev = dev_digits(k)
    plus = [j for j, d in enumerate(dev) if d == 1]
    minus = [j for j, d in enumerate(dev) if d == -1]
    other = [j for j, d in enumerate(dev) if abs(d) > 1]
    print(f"k={k}: +count={len(plus)} -count={len(minus)} |dev|>1 positions={other[:5]}{'...' if len(other)>5 else ''}")
    return plus, minus


def main():
    k = 1597  # F_17, odd
    plus, minus = test(k)
    wu = wyth_upper_lt(k)
    print("  odd case: plus == upper Wythoff:", plus == wu, " minus empty:", minus == [])
    if plus != wu:
        for i, (a, b) in enumerate(zip(plus, wu)):
            if a != b:
                print("   first mismatch at", i, a, b)
                break
        print("   counts:", len(plus), len(wu))

    k = 2584  # F_18, even
    plus, minus = test(k)
    wl = wyth_lower_lt(k)
    print("  even case: minus == lower Wythoff:", minus == wl, " plus empty:", plus == [])
    if minus != wl:
        for i, (a, b) in enumerate(zip(minus, wl)):
            if a != b:
                print("   first mismatch at", i, a, b)
                break
        print("   counts:", len(minus), len(wl))

    # general-k boundedness spot check beyond 400
    for k in (500, 1000, 2000):
        dev = dev_digits(k)
        print(f"k={k}: max|dev| = {max(abs(d) for d in dev)} (bounded-deviation conjecture)")


if __name__ == '__main__':
    main()

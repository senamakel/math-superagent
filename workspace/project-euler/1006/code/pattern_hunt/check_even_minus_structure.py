#!/usr/bin/env python3
"""PE1006: exact even-case -1-position structure at k = F_m (even m).

At k = F_m, m even, dev(j) in {0,-1} with F_{m-1} occurrences of -1.
Question: are the -1 positions exactly the lower Wythoff numbers
floor(t phi) < k  (t = 1..F_{m-1})?  Or some other known set?

Exact test at k = 55, 144, 377, 2584.
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


def lower_wythoff_lt(k):
    out = []
    t = 1
    while True:
        v = floor_phi(t)
        if v >= k:
            break
        out.append(v)
        t += 1
    return out


def upper_wythoff_lt(k):
    out = []
    t = 1
    while True:
        v = floor_phi2(t)
        if v >= k:
            break
        out.append(v)
        t += 1
    return out


def main():
    for k in (55, 144, 377, 2584):
        dev = dev_digits(k)
        minus = [j for j, d in enumerate(dev) if d == -1]
        lw = lower_wythoff_lt(k)
        uw = upper_wythoff_lt(k)
        # The complement of lower Wythoff under k? check symmetric difference sizes
        symdiff = sorted(set(minus) ^ set(lw))
        symdiff2 = sorted(set(minus) ^ set(uw))
        print(f"k={k}: |minus|={len(minus)} |lowerWythoff|={len(lw)} |upperWythoff|={len(uw)}")
        print(f"   minus==lowerWythoff: {minus == lw}; symdiff size {len(symdiff)}, first few {symdiff[:8]}")
        print(f"   minus==upperWythoff: {minus == uw}; symdiff size {len(symdiff2)}, first few {symdiff2[:8]}")
        # is minus maybe = { floor(t phi) : t>=1 } intersect [0,k) but with LAST upper?
        # report minus as digits over k
        s = ''.join('-' if d == -1 else '.' for d in dev)
        print("   minus pattern first 60:", s[:60])
        print()


if __name__ == '__main__':
    main()

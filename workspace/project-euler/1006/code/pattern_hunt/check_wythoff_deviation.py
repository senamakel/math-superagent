#!/usr/bin/env python3
"""PE1006: test the Wythoff-position conjecture for the M1 deviation pattern.

Conjecture (new): for k = F_m - 1 with m odd (k = 1, 4, 12, 33, 88, 232, ...),
the +1-deviation positions are exactly the upper Wythoff numbers
s_j = floor(j phi^2) with 0 <= s_j <= k-1, and all other positions deviate 0.
For m even (k = 2, 7, 20, 54, 143, 376, ...), the -1-deviation positions are
exactly the lower Wythoff numbers floor(j phi) with 0 < s_j <= k-1, and all
other positions deviate 0.

Attack: compute the exact deviation digits at k = F_17 - 1 = 1596 (beyond the
run's previous 376 cap) and compare with exact integer Wythoff lists.
Falsifier: first mismatch position; if the pattern holds we have a closed
form for the whole first-moment deviation at every Fibonacci boundary.
"""
from math import isqrt

# exact sqrt5 via scaled integer square root
SCALE = 4 ** 120
SQRT5 = isqrt(5 * SCALE * SCALE)
PHI = (1 + SQRT5 // SCALE)  # integer approx of phi*SCALE? no - keep rational form


def floor_phi(n):
    """floor(n*phi) exactly = floor(n*(1+sqrt5)/2)."""
    return (n * SCALE + n * SQRT5) // (2 * SCALE)


def floor_phi2(n):
    """floor(n*phi^2) exactly = floor(n*(3+sqrt5)/2)."""
    return (3 * n * SCALE + n * SQRT5) // (2 * SCALE)


def c1(k):
    return 1 + (3 * k * SCALE - k * SQRT5) // (2 * SCALE)


def fib_q_gt(k):
    a, b = 1, 1
    while b <= k:
        a, b = b, a + b
    return b


def dev_digits(k):
    """Return the deviation digit string for M1(k): '+'/'-'/'.' per position."""
    q = fib_q_gt(2 * k)
    f = [1, 1]
    while f[-1] < q:
        f.append(f[-1] + f[-2])
    assert f[-1] == q
    p = f[-3] if len(f) >= 3 else 0
    pts = sorted(((-m * p) % q) for m in range(k + 1))
    c = c1(k)
    out = []
    for i in range(k + 1):
        c1p = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + q
        for j in range(k):
            lo = (c1p + c2 + 2 * j * p) // (2 * q)
            hi = (c1p + c2 + 2 * (j + 1) * p) // (2 * q)
            pass  # counting per position needs accumulation, restructure below
    # accumulate position counts
    pc = [0] * k
    for i in range(k + 1):
        c1p = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + q
        for j in range(k):
            lo = (c1p + c2 + 2 * j * p) // (2 * q)
            hi = (c1p + c2 + 2 * (j + 1) * p) // (2 * q)
            pc[j] += hi - lo
    dev = [pc[j] - c for j in range(k)]
    return ''.join('+' if d > 0 else '-' if d < 0 else '.' for d in dev)


def main():
    print("k=1596 (F_17 - 1): computing deviation digits...")
    k = 1596
    s = dev_digits(k)
    print("dev length:", len(s))
    plus = [j for j, ch in enumerate(s) if ch == '+']
    minus = [j for j, ch in enumerate(s) if ch == '-']
    print("number of + :", len(plus), " first few:", plus[:12], " last:", plus[-3:])
    print("number of - :", len(minus), " first few:", minus[:12], " last:", minus[-3:])
    # F_17 = 1597, so k = 1596 is an ODD m (m=17) boundary: conjecture says +
    # at upper Wythoff positions floor(j phi^2) <= k-1.
    wyth_upper = []
    j = 1
    while True:
        v = floor_phi2(j)
        if v > k - 1:
            break
        wyth_upper.append(v)
        j += 1
    print("conjecture(+) == upper Wythoff: ", plus == wyth_upper)
    if plus != wyth_upper:
        for a, b in zip(plus, wyth_upper):
            if a != b:
                print("  first mismatch at index", plus.index(a), a, b)
                break
        print("  len plus:", len(plus), "len wyth:", len(wyth_upper))

    # Also test a smaller odd boundary k=88 (F_11 - 1) and even k=54 (F_10 - 1)
    for kk, parity in ((88, 'odd'), (54, 'even'), (232, 'odd'), (143, 'even')):
        s2 = dev_digits(kk)
        plus2 = [j for j, ch in enumerate(s2) if ch == '+']
        minus2 = [j for j, ch in enumerate(s2) if ch == '-']
        if parity == 'odd':
            wu = []
            j = 1
            while True:
                v = floor_phi2(j)
                if v > kk - 1:
                    break
                wu.append(v)
                j += 1
            print(f"k={kk}: plus==upperWythoff {plus2 == wu}; minus empty {minus2 == []}")
        else:
            wl = []
            j = 1
            while True:
                v = floor_phi(j)
                if v > kk - 1:
                    break
                wl.append(v)
                j += 1
            print(f"k={kk}: minus==lowerWythoff {minus2 == wl}; plus empty {plus2 == []}")


if __name__ == '__main__':
    main()

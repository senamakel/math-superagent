#!/usr/bin/env python3
"""PE1006: settle the Fibonacci-boundary deviation structure.

New finding: at k = F_m the deviation dev(j) = poscount(j) - c1(k) is
  - m odd:  +1 exactly at upper-Wythoff positions floor(t phi^2) < k,
            else 0   (verified k=89, 1597);
  - m even: -1 at EVERY position  (candidate: k=2584 shows 1596 minus).
If the even case is the constant shift -1 everywhere, then at k = F_m
(even m) poscount(j) = c1(k) - 1 = floor(k/phi^2) for every j, i.e. the
factors are position-balanced at the lower level (each position carries
exactly floor(k/phi^2) ones).

Check: k = 54 (F_10), 143 (F_12), 376 (F_14), 2584 (F_18): is minus set
exactly all of 0..k-1?  And recheck odd k = 34, 144, 233: + at upper
Wythoff only.
"""
from math import isqrt

SCALE = 4 ** 120
SQRT5 = isqrt(5 * SCALE * SCALE)


def c1(k):
    return 1 + (3 * k * SCALE - k * SQRT5) // (2 * SCALE)


def floor_phi2(n):
    return (3 * n * SCALE + n * SQRT5) // (2 * SCALE)


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


def main():
    print("Fibonacci numbers: F_9=34, F_10=55? (convention F_0=0,F_1=1: F_9=34,F_10=55,F_11=89,...)")
    print("(run's records used k=34 F_9 odd '+', k=55 F_10 even '-', k=89 F_11 odd '+', etc.)\n")
    odd_fibs = [34, 144, 233, 1597]     # F_9, F_12, F_13, F_17
    even_fibs = [55, 143 + 1, 376 + 1, 2584]  # F_10=55, F_12=144, F_14=377, F_18=2584
    # careful: 143 = F_12 - 1 (balanced); k=144 = F_12. 376 = F_14 - 1; k=377 = F_14.
    even_fibs = [55, 144, 377, 2584]
    for k in odd_fibs:
        dev = dev_digits(k)
        plus = [j for j, d in enumerate(dev) if d == 1]
        wu = wyth_upper_lt(k)
        print(f"odd  k={k}: plus==upperWythoff {plus == wu}  minus-count={dev.count(-1)}  other={[j for j,d in enumerate(dev) if abs(d)>1][:5]}")
    for k in even_fibs:
        dev = dev_digits(k)
        allminus = all(d == -1 for d in dev)
        print(f"even k={k}: all positions -1: {allminus}  plus-count={dev.count(1)}  other={[j for j,d in enumerate(dev) if abs(d)>1][:5]}")
        if not allminus:
            # show structure
            import collections
            print("   distribution:", collections.Counter(dev))


if __name__ == '__main__':
    main()

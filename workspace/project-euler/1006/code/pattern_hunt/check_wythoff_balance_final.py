#!/usr/bin/env python3
"""PE1006: final verification of the Wythoff-position balance theorem.

Claim (new, computational conjecture): for every Fibonacci number F_m >= 5,
with k = F_m and c1(k) = 1 + floor(k/phi^2),
  dev(j) = poscount(j) - c1(k)  satisfies:
    m odd  (k = 5, 13, 34, 89, 233, 610, 1597, ...):
        dev(j) = +1  iff  j in {floor(t phi^2) : t >= 1, floor(t phi^2) < k}
        dev(j) =  0  otherwise
    m even (k = 8, 21, 55, 144, 377, 987, 2584, ...):
        dev(j) = -1  iff  j in {floor(t phi)  : t >= 1, floor(t phi)  < k}
        dev(j) =  0  otherwise

Equivalently the per-position one-counts of the k+1 length-k factors at
k = F_m are
    m odd:  c1(k) + [j in upper Wythoff]
    m even: c1(k) - [j in lower Wythoff]
which gives M1(k) = c1(k)*R(k) + sum_{upper} 10^j  (m odd)
              = c1(k)*R(k) - sum_{lower} 10^j  (m even).

Exact verification at k = 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
987, 1597, 2584, 4181 (F_5 .. F_19), and a spot check at general k
(k not Fibonacci) that |dev| <= 1 still holds (recorded boundedness).
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


def wyth(k, which):
    out = []
    t = 1
    while True:
        v = (floor_phi(t) if which == 'lower' else floor_phi2(t))
        if v >= k:
            break
        out.append(v)
        t += 1
    return out


def main():
    fibs = []
    a, b = 1, 1
    while b <= 4181:
        fibs.append(b)
        a, b = b, a + b
    print("Fibonacci:", fibs)
    print()
    fails = []
    for k in fibs[4:]:  # k >= 5
        dev = dev_digits(k)
        plus = [j for j, d in enumerate(dev) if d == 1]
        minus = [j for j, d in enumerate(dev) if d == -1]
        other = [j for j, d in enumerate(dev) if abs(d) > 1]
        # determine parity: k = F_m; fibs[m-1] = F_m with F_1=1, F_2=2 (run convention)
        m = fibs.index(k) + 1
        # k=5 -> m=5? no: fibs[4]=5 so m=5; but F_5=5 with F_1=1,F_2=1.  The run's
        # convention has F_1=1, F_2=2, so index into fibs: fibs[i] = F_{i+2} with
        # F_1=1,F_2=1,F_3=2.  We observed: k=34 shows + (and 34=F_9 odd index in the
        # standard convention), k=55 shows - (55=F_10 even index).
        # So: standard-index parity of F_m: F_1=1,F_2=1,F_3=2,F_4=3,F_5=5,F_6=8,...
        # k=8 -> F_6 (even), k=13 -> F_7 (odd), k=21 -> F_8 (even), k=34 -> F_9 (odd).
        # Therefore in our list fibs[i]=F_{i+2}: k=8 at i=5 -> standard m = i+2 = 7? No.
        # Let's just compute the standard index directly: iterate standard Fibonacci.
        # standard F_1=1,F_2=1,F_3=2,F_4=3,F_5=5,F_6=8,F_7=13,F_8=21,F_9=34,F_10=55,
        # F_11=89,F_12=144,F_13=233,F_14=377,F_15=610,F_16=987,F_17=1597,F_18=2584,F_19=4181.
        std = {5:5, 8:6, 13:7, 21:8, 34:9, 55:10, 89:11, 144:12, 233:13, 377:14,
               610:15, 987:16, 1597:17, 2584:18, 4181:19}
        m = std[k]
        if m % 2 == 1:  # odd standard index -> + at upper Wythoff
            wu = wyth(k, 'upper')
            ok = (plus == wu) and (minus == []) and (other == [])
            tag = "ODD "
        else:
            wl = wyth(k, 'lower')
            ok = (minus == wl) and (plus == []) and (other == [])
            tag = "EVEN"
        if not ok:
            fails.append((k, tag))
        print(f"{tag} k={k:5d} (F_{m:2d}): {'OK ' if ok else 'FAIL'}  "
              f"+={len(plus):4d} -={len(minus):4d} other={len(other)}")

    print()
    print("All Fibonacci boundaries 5..4181 satisfy the Wythoff-position claim:", fails == [])
    print("fails:", fails[:5])

    # general-k boundedness spot check
    print()
    for k in (1000, 1500, 2000, 3000, 4000):
        dev = dev_digits(k)
        print(f"general k={k}: max|dev|={max(abs(d) for d in dev)}")


if __name__ == '__main__':
    main()

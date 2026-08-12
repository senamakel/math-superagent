#!/usr/bin/env python3
"""Directly test period-7 of first differences of K(n)."""
import mpmath as mp


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = None
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best


def main():
    mp.mp.dps = 80
    N = 200
    K = {n: K_of_n(n) for n in range(1, N + 1)}
    # first differences
    D = {n: K[n] - K[n - 1] for n in range(4, N + 1)}
    # period 7 check: D[n] == D[n-7]
    fails = []
    for n in range(11, N + 1):
        if D[n] != D[n - 7]:
            fails.append(n)
    print("K(n) n=3..40:", [K[n] for n in range(3, 41)])
    print("first differences D(n)=K(n)-K(n-1), n=4..40:")
    print([D[n] for n in range(4, 41)])
    print("first n where D(n)!=D(n-7) (period-7 breaks):", fails[:5])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Regenerate the integer sequences that matter in PE 761 for the pattern tools.

Sequences:
  K(n):   largest integer with sin(K*pi/n) - (K+n)*tan(pi/n)*cos(K*pi/n) < 0
          (= floor of unique root of tan(x*pi/n) - (x+n)*tan(pi/n) in [1,n/2))
  d(n):   deg_Q(V(n)^2)  -- degree of V(n)^2 over Q (quadratic or not)
"""
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
    mp.mp.dps = 60

    print("K(n) for n=3..40:")
    Kseq = []
    for n in range(3, 41):
        Kseq.append(K_of_n(n))
    print(Kseq)

    print("\nK(n) - floor(3n/7) deviation, n=3..100:")
    devs = []
    for n in range(3, 101):
        d = K_of_n(n) - (3 * n // 7)
        if d != 0:
            devs.append((n, K_of_n(n), 3 * n // 7, d))
    print("first deviations:", devs[:5])

    print("\nK(n)/n asymptotic check at large n (expect c~0.4302966531):")
    for n in [100, 1000, 10000, 100000, 1000000]:
        print(n, K_of_n(n), K_of_n(n) / n)


if __name__ == "__main__":
    main()

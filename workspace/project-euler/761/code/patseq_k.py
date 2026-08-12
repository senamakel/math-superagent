#!/usr/bin/env python3
"""Compute K(n) for a regular n-gon, n=3..60, exactly (mpmath dps=50).

K(n) = largest integer in [0, n] with
    sin(K*theta) - (K+n)*tan(theta)*cos(K*theta) < 0,  theta = pi/n.
This is the index used in stewbasic's critical-speed formula
V(n) = 1/cos(alpha). Print the sequence as a comma list.
"""
import mpmath as mp

mp.mp.dps = 50


def K_of_n(n):
    """Largest k in [0, n] with sin(k*pi/n) - (k+n)*tan(pi/n)*cos(k*pi/n) < 0."""
    th = mp.pi / n
    t = mp.tan(th)
    K = 0
    for k in range(0, n + 1):
        val = mp.sin(k * th) - (k + n) * t * mp.cos(k * th)
        if val < 0:
            K = k
    return K


def main():
    N = 60
    Ks = [K_of_n(n) for n in range(3, N + 1)]
    print("K(3..%d):" % N)
    print(", ".join(str(x) for x in Ks))


if __name__ == "__main__":
    main()

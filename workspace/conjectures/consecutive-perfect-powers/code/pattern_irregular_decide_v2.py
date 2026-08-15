#!/usr/bin/env python3
"""Decide, by exact arithmetic, whether the known double-Wieferich smaller
members 911 and 2903 are irregular (Kummer: p | numerator(B_{2k}) for some
even 2k, 2<=2k<=p-3). Two independent exact routes:
  Route 1: sympy bernoulli numerator, then % p.
  Route 2: Akiyama-Tanigawa computed mod p (valid: all running denominators
            are < p, and for the even m in range 2m <= p-3 the Bernoulli
            denominator is p-free, so reducing mod p is faithful).
Resolves a contradiction in the record.
"""
import sympy

def numB(n):
    return sympy.numer(sympy.bernoulli(n))

def at_modp(p):
    """Akiyama-Tanigawa over F_p. Returns set of indices k (1-based, even
    index m=2k) such that numerator(B_{2k}) == 0 (mod p), for k in
    [1, (p-3)//2]."""
    def inv(x):
        return pow(x, p - 2, p)
    N = p - 4  # max row index m
    a = [inv(j + 1) for j in range(N + 1)]
    res = []
    for m in range(N + 1):
        if m % 2 == 0:
            Bm = a[0]  # B_m mod p
            k = m // 2
            if 1 <= k <= (p - 3) // 2 and Bm == 0:
                res.append(k)
        if m == N:
            break
        a = [((j + 1) % p) * ((a[j] - a[j + 1]) % p) % p
             for j in range(len(a) - 1)]
    return res

def main():
    for p in [911, 2903, 83, 4871, 18787]:
        r1 = [k for k in range(1, (p - 3) // 2 + 1) if numB(2 * k) % p == 0]
        r2 = sorted(at_modp(p))
        match = (r1 == r2)
        print(f"p={p}: route1={r1} route2={r2} AGREE={match} REGULAR={not r1}")

if __name__ == "__main__":
    main()

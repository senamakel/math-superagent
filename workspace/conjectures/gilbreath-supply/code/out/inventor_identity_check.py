#!/usr/bin/env python3
"""Sanity checks for the structural identities underlying the three proposals.

(1) Character telescope: (-1)^{T(n,d)} = prod over runs R of the downset of d
    of chi(r[a_R]) * chi(r[b_R]), chi = nontrivial character mod 4.
(2) Freshman's dream over F2: (1+sigma)^{2^g} h = (1 + sigma^{2^g}) h, and the
    general digit factorisation (1+sigma)^d = prod_{e in bits(d)} (1+sigma^{2^e}),
    so T(n,d) is the mixed dyadic derivative of h.
Run as: python -m code.out.inventor_identity_check   (or python code/out/...)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from lib.supply_fold import t_direct, runs_of_downset, h_from_r


def chi(x):
    return -1 if x % 4 == 3 else (1 if x % 4 == 1 else 0)


def check_character_telescope(n, r):
    """For each d in [2, n-1], compare (-1)^{T(n,d)} with the run-endpoint
    character product chi(r[a])*chi(r[b]) over runs R=[u,v] of downset(d)."""
    h = h_from_r(r)
    ok = True
    for d in range(2, n):
        T = t_direct(n, d, h)
        sign = -1 if T else 1
        prod = 1
        for (u, v) in runs_of_downset(d):
            a = n - 1 - d + u
            b = n - 1 - d + v + 1
            prod *= chi(r[a]) * chi(r[b])
        if prod != sign:
            print("MISMATCH character telescope n=%d d=%d T=%d sign=%d prod=%d" %
                  (n, d, T, sign, prod))
            ok = False
    return ok


def check_freshmans_dream(h, maxg):
    """(1+sigma)^{2^g} h == (1 + sigma^{2^g}) h over F2, for each g."""
    def sig_pow(h, k):
        # apply (1+sigma) k times over F2: new[i] = h[i] XOR h[i+1]
        x = h[:]
        for _ in range(k):
            x = [x[i] ^ x[i + 1] for i in range(len(x) - 1)]
        return x
    ok = True
    L = len(h)
    for g in range(maxg + 1):
        shift = 1 << g
        if shift >= L:
            break
        lhs = sig_pow(h, shift)              # (1+sigma)^{2^g} h
        rhs = [h[i] ^ h[i + shift] for i in range(L - shift)]  # (1+sigma^{2^g}) h
        if lhs != rhs:
            print("MISMATCH freshman's dream g=%d" % g)
            ok = False
    return ok


def check_digit_factorisation(n, h):
    """T(n,d) == mixed dyadic derivative: XOR over subsets S of bits(d) of
    h[n-1-d + sum_{e in S} 2^e]  (this is exactly the submask form, but with
    the bit-factorisation read out explicitly)."""
    ok = True
    for d in range(2, n):
        bits = [e for e in range(d.bit_length()) if (d >> e) & 1]
        # XOR over all subset-sums of the set bits
        val = 0
        for mask in range(1 << len(bits)):
            s = 0
            for j, e in enumerate(bits):
                if (mask >> j) & 1:
                    s += 1 << e
            val ^= h[n - 1 - d + s]
        T = t_direct(n, d, h)
        if val != T:
            print("MISMATCH digit factorisation n=%d d=%d" % (n, d))
            ok = False
    return ok


if __name__ == "__main__":
    import random
    random.seed(1)
    n = 40
    # prime residues mod 4 for first n+1 primes (r[0]=2, rest odd)
    import sympy
    ps = list(sympy.ntheory.generate.primerange(0, sympy.prime(n + 1) + 1))[:n + 1]
    r = [p % 4 for p in ps]
    print("character telescope ok:", check_character_telescope(n, r))

    # random h of length 70 for freshman's dream / digit factorisation
    h = [random.randint(0, 1) for _ in range(70)]
    print("freshman's dream ok:", check_freshmans_dream(h, 6))
    h2 = [random.randint(0, 1) for _ in range(n)]
    print("digit factorisation ok:", check_digit_factorisation(n, h2))

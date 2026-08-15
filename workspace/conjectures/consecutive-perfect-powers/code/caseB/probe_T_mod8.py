#!/usr/bin/env python3
"""Probe the residue of T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k mod 8, and the
square-possibility structure, for p an odd prime.

A perfect square mod 8 is 0,1,4 only.  We tabulate T mod 8 by (c mod something,
p mod something) to find which residue classes force a non-square.
"""


def T_mod(c, p, mod):
    x = c * c + 1
    # geometric sum = (x^p - 1)//(x - 1); do it as modular geometric series
    # sum_{k=0}^{p-1} r^k = (r^p - 1)/(r - 1)  (= p when r == 1 mod mod)
    if x % mod == 1:
        return p % mod
    # r != 1 mod mod: sum = (r^p - 1) * (r-1)^{-1}
    from sympy import mod_inverse
    r = x % mod
    return ((pow(r, p, mod) - 1) * mod_inverse(r - 1, mod)) % mod


def is_odd_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


# classify by c mod 4 and p mod 4 (p odd prime => p mod 4 in {1,3})
print("T(c,p) mod 8, by c mod 4 and p mod 4 (x = c^2+1):")
for cmod in range(4):
    for pmod in (1, 3):
        vals = set()
        reps = {}
        for pov in [pp for pp in range(3, 120) if is_odd_prime(pp) and pp % 4 == pmod][:6]:
            for cov in [cc for cc in range(1, 90) if cc % 4 == cmod][:6]:
                r = T_mod(cov, pov, 8)
                vals.add(r)
                reps.setdefault(r, (cov, pov))
        print(f"  c={cmod} mod 4, p={pmod} mod 4: residues {sorted(vals)}  "
              f"(square residues 0,1,4)")

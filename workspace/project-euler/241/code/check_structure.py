"""Verify structural regularities of PE241 qualifying numbers.

For n = 2^a * u (u odd), the half-integer condition 2*sigma(n)=(2k+1)n forces
1 + v2(sigma(u)) = a.  Also report per-abundancy counts and the abundancy of
each qualifying n up to N.
"""
import sys
from math import isqrt

def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def sigma_from_factors(f):
    s = 1
    for p, e in f.items():
        s *= (p ** (e + 1) - 1) // (p - 1)
    return s

def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c

def qualifying(N):
    res = []
    for n in range(1, N + 1):
        f = factorize(n)
        s = sigma_from_factors(f)
        num = 2 * s
        if num % n == 0 and (num // n) % 2 == 1:
            res.append(n)
    return res

N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**7
q = qualifying(N)
print("qualifying n up to", N, ":", q)

from collections import defaultdict
perk = defaultdict(list)
print("\nn:  abundancy k,  a=v2(n), u=n/2^a, v2(sigma(u)), 2-adic ok?")
for n in q:
    f = factorize(n)
    s = sigma_from_factors(f)
    two = 2 * s // n
    k = (two - 1) // 2
    a = v2(n)
    u = n >> a
    fu = factorize(u)
    su = sigma_from_factors(fu)
    ok = (v2(su) == a - 1)
    perk[k].append(n)
    print(f"  n={n:>10} k={k} a={a} u={u} v2(sig(u))={v2(su)} 2adic_ok={ok}")

print("\nper-k counts:")
for k in sorted(perk):
    print(f"  k={k}  ({2*k+1}/2=abundancy): {len(perk[k])} members {perk[k]}")

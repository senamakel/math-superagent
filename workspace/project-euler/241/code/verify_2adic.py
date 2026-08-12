"""Exact structural verification for all known PE241 qualifying n.

For n = 2^a * u (u odd), 2*sigma(n) = (2k+1)*n forces (purely 2-adically)
    v2(sigma(u)) = a - 1,
and then the abundancy condition is equivalent to the exact rational identity
    sigma(u)/u = (2k+1) * 2^(a-1) / (2^(a+1) - 1).
Verify both for every qualifying n found by the sieve.
"""
from math import gcd

# Qualifying n <= 3e7 computed by code/check_structure_fast.py (numpy sigma
# sieve; matches OEIS A159907 terms 1..8 exactly).
QUALIFYING = [2, 24, 4320, 4680, 26208, 8910720, 17428320, 20427264]

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

print(f"{'n':>10} {'a=v2(n)':>8} {'k':>3} | {'v2(sig(u))':>10} {'constr':>10} | {'sig(u)/u':>12} {'target':>32} equal?")
allok = True
for n in QUALIFYING:
    f = factorize(n)
    s = sigma_from_factors(f)
    k = (2 * s // n - 1) // 2            # abundancy k + 1/2
    a = v2(n)
    u = n >> a
    su = sigma_from_factors(factorize(u))
    v = v2(su)
    ok1 = (v == a - 1)
    # reduced sigma(u)/u
    g1 = gcd(su, u)
    num, den = su // g1, u // g1
    # target (2k+1)*2^(a-1) / (2^(a+1)-1), reduced
    tnum = (2 * k + 1) * (1 << (a - 1))
    tden = (1 << (a + 1)) - 1
    g2 = gcd(tnum, tden)
    tnum, tden = tnum // g2, tden // g2
    eq = (num == tnum and den == tden)
    allok &= ok1 and eq
    print(f"{n:>10} {a:>8} {k:>3} | {v:>10} {str(ok1):>10} | {num}/{den:>10} {(str(tnum)+'/'+str(tden)):>30} {eq}")

print("\nALL 2-ADIC CONSTRAINTS AND RATIONAL IDENTITIES HOLD:", allok)

# per-k grouping
from collections import defaultdict
perk = defaultdict(list)
for n in QUALIFYING:
    f = factorize(n)
    s = sigma_from_factors(f)
    k = (2 * s // n - 1) // 2
    perk[k].append(n)
print("\nper-k grouping:")
for k in sorted(perk):
    print(f"  k={k} (abundancy {2*k+1}/2): {perk[k]}")
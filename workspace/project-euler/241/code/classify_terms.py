"""Classify every known hemiperfect (OEIS A159907 terms + our sieve terms) by
abundancy k, 2-adic valuation a, and odd part u; verify the rational identity
sigma(u)/u = (2k+1)*2^(a-1)/(2^(a+1)-1) for each."""
from math import gcd
from collections import defaultdict

A159907 = [2, 24, 4320, 4680, 26208, 8910720, 17428320, 20427264, 91963648,
           197064960, 8583644160, 10200236032, 21857648640, 57575890944,
           57629644800, 206166804480, 17116004505600, 1416963251404800,
           15338300494970880, 75462255348480000, 88898072401645056,
           301183421949935616, 6219051710415667200]

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

rows = []
for n in A159907:
    f = factorize(n)
    s = sigma_from_factors(f)
    assert 2 * s % n == 0 and (2 * s // n) % 2 == 1, f"not hemiperfect: {n}"
    k = (2 * s // n - 1) // 2
    a = v2(n)
    u = n >> a
    su = sigma_from_factors(factorize(u))
    g1 = gcd(su, u)
    num, den = su // g1, u // g1
    tnum = (2 * k + 1) * (1 << (a - 1))
    tden = (1 << (a + 1)) - 1
    g2 = gcd(tnum, tden)
    tnum, tden = tnum // g2, tden // g2
    eq = (num == tnum and den == tden)
    rows.append((n, k, a, u, num, den, eq))

print(f"{'n':>21} {'k':>3} {'a':>3} {'u (odd part)':>21} {'sig(u)/u':>14} {'identity':>8}")
for n, k, a, u, num, den, eq in rows:
    print(f"{n:>21} {k:>3} {a:>3} {u:>21} {num:>7}/{den:<7} {eq}")

print("\nPer-k groups (n values):")
perk = defaultdict(list)
for n, k, a, u, num, den, eq in rows:
    perk[k].append(n)
for k in sorted(perk):
    print(f"  k={k}: {perk[k]}")

print("\nPer-(k,a) groups: odd-part abundancy targets and their u's")
perka = defaultdict(list)
for n, k, a, u, num, den, eq in rows:
    perka[(k, a)].append(u)
for (k, a) in sorted(perka):
    print(f"  k={k}, a={a}: target={ (2*k+1)*(1<<(a-1)) }/{ (1<<(a+1))-1 }  u's={perka[(k,a)]}")

print("\nPer-k counts:", {k: len(v) for k, v in sorted(perk.items())})
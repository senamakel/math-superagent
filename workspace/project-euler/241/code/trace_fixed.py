"""Trace corrected DFS for r=7/2 to find why 26208 is missed."""
from math import gcd
from sympy import primerange, factorint

LIMIT = 10**10

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

PRIMES = list(primerange(2, 2000000))
solutions = {}
path = []

def dfs(r, idx, n, u, v):
    g = gcd(u, v)
    u, v = u // g, v // g
    if u == 1 and v == 1:
        solutions.setdefault(r, set()).add(n)
        print(f"RECORD n={n} path={list(path)}", flush=True)
        return
    if u < v or n > LIMIT:
        return
    d = None; a = 0
    if v > 1:
        d = min(factorint(v))
        w = v
        while w % d == 0:
            w //= d; a += 1
    for i in range(idx, len(PRIMES)):
        p = PRIMES[i]
        if d is not None and p < d:
            continue
        if d is not None and p > d:
            break
        estart = 1 if d is None else a
        e = estart
        while True:
            pe = p ** e
            n2 = n * pe
            if n2 > LIMIT:
                break
            sp = sigma_pe(p, e)
            u2 = u * pe
            v2 = v * sp
            if u2 < v2:
                break
            den_red = v2 // gcd(u2, v2)
            if n2 * den_red > LIMIT:
                break
            path.append((p, e))
            dfs(r, i + 1, n2, u2, v2)
            path.pop()
            e += 1
        if d is not None:
            break

dfs(7, 0, 1, 7, 2)
print("solutions r=7/2:", sorted(solutions.get(7, ())))

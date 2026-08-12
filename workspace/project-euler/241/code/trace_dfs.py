"""Trace which DFS path records the false-positive n=313632, and which r finds/drops each solution.

Runs a small LIMIT (just above 313632) and prints the (p,e) chain leading to every
recorded solution plus the reduced Q at record time.
"""
import sys
from math import gcd
from sympy import primerange, factorint

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 40000000

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

PRIMES = list(primerange(2, 2000000))
solutions = {}
path = []

def dfs(r, idx, n, num, den):
    g = gcd(num, den)
    num, den = num // g, den // g
    if num == 1 and den == 1:
        solutions.setdefault(r, set()).add(n)
        print(f"RECORD r={r}/2 n={n} path={list(path)}", flush=True)
        return
    if num < den:
        return
    if n > LIMIT:
        return
    d = den
    if den > 1:
        d = min(factorint(den))
    for p in PRIMES[idx:]:
        if p < d and den > 1:
            continue
        e = 1
        while True:
            pe = p ** e
            n2 = n * pe
            if n2 > LIMIT:
                break
            sp = sigma_pe(p, e)
            num2 = num * pe
            den2 = den * sp
            if num2 < den2:
                break
            if n2 * den2 // gcd(num2, den2) > LIMIT:
                break
            path.append((p, e))
            dfs(r, idx + 1, n2, num2, den2)
            path.pop()
            e += 1
        if p >= d and den > 1:
            break

for r in [5, 7, 9]:
    print(f"--- target r={r}/2 ---")
    dfs(r, 0, 1, r, 2)
    print("  solutions:", sorted(solutions.get(r, ())))
print("ALL:", sorted(set().union(*solutions.values())))

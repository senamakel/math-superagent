"""Instrumented copy of hemiperfect_dfs.py to find the blow-up at 10^18.

Counts DFS node expansions, recursion depth, and times each target.  Takes a
LIMIT from argv so scaling to 10^18 can be observed.
"""
import sys, time
from math import gcd
from sympy import primerange, factorint

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10**12

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

PRIMES = list(primerange(2, 2000000))

solutions = {}
nodes = 0

def dfs(r, idx, n, num, den):
    global nodes
    nodes += 1
    g = gcd(num, den)
    num, den = num // g, den // g
    if num == 1 and den == 1:
        solutions.setdefault(r, set()).add(n)
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
            dfs(r, idx + 1, n2, num2, den2)
            e += 1
        if p >= d and den > 1:
            break

t0 = time.time()
for r in range(3, 40, 2):
    tr = time.time()
    dfs(r, 0, 1, r, 2)
    dt = time.time() - tr
    sols = sorted(s for s in solutions.get(r, ()) if s <= LIMIT)
    print(f"r/2={r}/2: nodes={nodes} time={dt:.2f}s sols={len(sols)}", flush=True)
print("TOTAL nodes processed:", nodes, "total time:", time.time()-t0)
allsol = set()
for r in solutions:
    allsol.update(s for s in solutions[r] if s <= LIMIT)
print("all <= LIMIT:", sorted(allsol), "count", len(allsol), "sum", sum(allsol))

"""Recompute the d=7 criterion exactly on the extended sweep, ground truth first.

Ground truth:  d=7 works  <=>  two_term(n, (n+7)/4) finds a split.
Criterion:     d=7 works  <=>  exists prime q | n*(n+7)/4 with q % 7 in {3,5,6}.

Also separately report where e==0 rows have d=7 working (non-minimal splits)
so the earlier "e<=1 iff d=7 works" conflation is quantified and closed.

Ground truth uses exact brute divisor enumeration over (nx)^2 — costly but
only for x=(n+7)/4, and sympy divisors is fast at these sizes.
"""
import json, time
from sympy import factorint, divisors
from fractions import Fraction

rows = json.load(open('code/out/extended_minimal_x.json'))['rows']
QNR7 = {3, 5, 6}

def two_term(n, x):
    d = 4 * x - n
    if d <= 0:
        return None
    nx = n * x
    M = nx * nx
    for u in divisors(M):
        if u > nx:
            continue
        if (nx + u) % d != 0:
            continue
        v = M // u
        if (nx + v) % d != 0:
            continue
        y, z = (nx + u) // d, (nx + v) // d
        if y >= 1 and z >= 1 and \
           Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n):
            return (y, z)
    return None

def cond7(n):
    return any(p % 7 in QNR7 for p in factorint(n)) or \
           any(p % 7 in QNR7 for p in factorint((n + 7) // 4))

t0 = time.time()
bad = []; e0_d7works = 0; e0_total = 0
for row in rows:
    n = row['n']
    works = two_term(n, (n + 7) // 4) is not None
    cond = cond7(n)
    e0 = row['excess'] == 0
    if e0:
        e0_total += 1
        if works:
            e0_d7works += 1
    if works != cond:
        bad.append((row['k'], row['r'], n, row['excess'], works, cond))
print(f"d=7 criterion: {len(rows)-len(bad)}/{len(rows)} rows agree; mismatches {len(bad)}")
for b in bad[:10]:
    print("   mismatch:", b)
print(f"among e==0 rows: {e0_d7works}/{e0_total} also have d=7 working (non-minimal split)")
print(f"time {time.time()-t0:.1f}s")
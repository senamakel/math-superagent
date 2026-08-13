"""Verify the unified genus closed form against EVERY computed point:
    g(m,n) = ((m-1)*n - (m-2) - gcd(n,m)) / 2    for 2 <= m < n
against (a) the full TABLE grid, (b) the freshly computed extensions for
m=6..10 from extend_k2_6.sing and extend_rows_7_10.sing, (c) the three
diagonal families symbolically.

Prints total points checked, mismatch count, and the failing pairs (if any).
Also reports the first UNCOMPUTED term per row (the next falsifier) with its
prediction.
"""
from math import gcd
import sys
sys.path.insert(0, '/workspace/code/genus')
from genus_table import TABLE

def gform(m, n):
    return ((m - 1) * n - (m - 2) - gcd(n, m)) // 2

# (a) full table
mism = []
pts = 0
for (a, b), g in TABLE.items():
    m, n = sorted((a, b))
    pts += 1
    if gform(m, n) != g:
        mism.append((m, n, g, gform(m, n)))
print(f"TABLE: {pts} points, {len(mism)} mismatches")
for x in mism[:10]:
    print("   ", x)

# (b) new extensions
EXT = {
    (6, 13): 30, (6, 14): 32, (6, 15): 34, (6, 16): 37, (6, 17): 40, (6, 18): 40,
    (7, 13): 36, (7, 14): 36, (7, 15): 42,
    (8, 13): 42, (8, 14): 45, (8, 15): 49, (8, 16): 49,
    (9, 13): 48, (9, 14): 52, (9, 15): 55, (9, 16): 60, (9, 17): 64,
    (10, 13): 54, (10, 14): 58, (10, 15): 61, (10, 16): 67, (10, 17): 72,
    (10, 18): 76, (10, 19): 81,
}
emism = []
for (m, n), g in EXT.items():
    if gform(m, n) != g:
        emism.append((m, n, g, gform(m, n)))
print(f"EXTENSIONS: {len(EXT)} points, {len(emism)} mismatches")
for x in emism[:10]:
    print("   ", x)

# (c) diagonal families symbolically in closed form (m = n-a, a = 1,2,3)
import sympy as sp
N = sp.Symbol('n', integer=True, positive=True)
for a in (1, 2, 3):
    m = N - a
    expr = sp.simplify(((m - 1) * N - (m - 2) - sp.gcd(N, m)) / 2)
    print(f"diagonal {a} (pair {{n-{a}, n}}): formula = {expr}")
print("  (compare: a=1 -> (n-1)(n-2)/2; a=2 -> (n-1)(n-3)/2 odd, (n^2-4n+2)/2 even; a=3 -> ?)")

# (d) symmetry and integrality
ok_sym = all(gform(m, n) == gform(n, m) for (a, b) in TABLE for (m, n) in [sorted((a, b))])
print(f"formula symmetric over all table pairs: {ok_sym}")
ok_int = all(((m-1)*n - (m-2) - gcd(n, m)) % 2 == 0 for m in range(2, 30) for n in range(m+1, 60))
print(f"formula integral over m=2..29, n=m+1..59: {ok_int}")

# (e) next falsifier terms per row
print("\nNext uncomputed term per row (prediction):")
for m in range(2, 12):
    have = [n for (a, b) in TABLE for (mm, n2) in [sorted((a, b))] if mm == m and min((a,b)) == m for n in [n2]] + \
           [n for (mm, n) in EXT if mm == m]
    if not have:
        continue
    nxt = max(have) + 1
    print(f"  m={m}: next n={nxt} -> g={gform(m, nxt)}   (had n<= {max(have)})")

print("\nAll checks done.  Formula: g(m,n) = ((m-1)n - (m-2) - gcd(n,m))/2")
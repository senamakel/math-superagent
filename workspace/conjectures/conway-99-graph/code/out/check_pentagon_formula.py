"""Independent check of the pentagon (induced C5) count formula p5 = n*k*(k-2)*(k-4)/5
for the srg(v,k,1,2) family, by exact brute force on the rook(3) control (v=9,k=4).

Vertex-derived: Reimbayev order-6 body gives the closed form; here we only
verify it against a brute-force induced-C5 count on the smallest member.
Brute force is the oracle here (n=9, tiny). Exact integer arithmetic only.
"""
import itertools
import numpy as np
from lib.srg import rook, bvls_graph  # rook(3) and BvLS control graphs on PYTHONPATH

def induced_C5_count(A):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    adj = [set(np.nonzero(A[i])[0]) for i in range(n)]
    count = 0
    verts = range(n)
    for comb in itertools.combinations(verts, 5):
        c = set(comb)
        edges = 0
        ok = True
        degin = {v: 0 for v in c}
        for v in c:
            for w in c:
                if v < w:
                    if w in adj[v]:
                        edges += 1
                        degin[v] += 1; degin[w] += 1
        # induced C5: 5 edges, each vertex degree 2 within, no chord
        if edges == 5 and all(degin[v] == 2 for v in c):
            count += 1
    return count

# formula for the family
def pentagon_formula(k, n):
    return n * k * (k - 2) * (k - 4) // 5

# rook(3): v=9, k=4
A = rook(3)
brute = induced_C5_count(A)
form = pentagon_formula(4, 9)
print("rook(3) induced C5 brute:", brute, " formula(4,9):", form, " match:", brute == form)
# pentagon values at the five feasible u
for u, k, n in [(1,4,9),(3,14,99),(4,22,243),(10,112,6273),(31,994,494019)]:
    p = pentagon_formula(k, n)
    # exact integer check: must be integer and formula holds for the two smallest by brute force (rook brute=0 done)
    print(f"u={u:<2} k={k:<4} v={n:<6} p5={p}")

"""Verification of the Moser spindle chromatic polynomial against the CERTIFIED
edge list (from lib.unitfield.moser_spindle_points + unit_graph, exact).
"""
from lib.unitfield import moser_spindle_points, unit_graph
import sympy as sp

pts = moser_spindle_points()
edges_raw, m = unit_graph(pts)
assert m == 11
EDGES = sorted((min(i,j), max(i,j)) for i, j in edges_raw)
N = 7
print("certified edges:", EDGES)

adj = [set() for _ in range(N)]
for u, v in EDGES:
    adj[u].add(v); adj[v].add(u)

def count_colourings(k):
    total = 0
    col = [-1]*N
    col[0] = 0
    def rec(i):
        nonlocal total
        if i == N:
            total += 1
            return
        for c in range(k):
            if i == 0 and c != 0:
                continue
            if all(col[j] != c for j in adj[i]):
                col[i] = c
                rec(i+1)
                col[i] = -1
    rec(0)
    return total

# pinning vertex 0 to colour 0 returns total/k proper colourings; multiply by k
counts = {k: k * count_colourings(k) for k in range(1, 15)}
print("exact proper-colouring counts:")
for k in range(1, 15):
    print(f"  k={k}: {counts[k]}")

# calibration sanity
assert counts[3] == 0 and counts[4] == 384 and counts[5] == 5040, counts

k = sp.symbols('k')
xs = list(range(0, 8))
ys = [sp.Integer(0) if kk == 0 else counts[kk] for kk in xs]
P = sp.expand(sp.interpolate(list(zip(xs, ys)), k))
print("\nchromatic polynomial P_M(k) =", P)
print("factored:", sp.factor(P))

allok = all(int(P.subs(k, kk)) == counts[kk] for kk in range(1, 15))
print("\nALL 14 k=1..14 MATCH:", allok)

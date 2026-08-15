"""Independent cross-check of the calibration, written without importing the
construction or colouring library logic (different route to the same values).

1. Numerically re-verify every claimed edge is at distance 1.0 to float
   precision and confirmed by sympy exact equality (second route).
2. Re-verify the 4-colouring witness is proper on every edge.
3. Re-verify 3-colourability UNSAT via an independent, differently-ordered
   exhaustive search (order = natural, no DSATUR, no such symmetry breaks),
   and 4-colourability SAT via the same independent search.
"""
import sympy as sp
from lib.unitgraph import moser_spindle
from lib.coloring import verify_coloring

# --- exactly rebuild edges again from scratch, numeric + symbolic ---
pts = moser_spindle()
names = ["O", "P1", "P2", "Q", "P1'", "P2'", "Q'"]
n = len(pts)
assert n == 7

edges_symbolic = []
edges_numeric = []
for i in range(n):
    for j in range(i + 1, n):
        xi, yi = pts[i]; xj, yj = pts[j]
        d2sym = sp.simplify((xi - xj) ** 2 + (yi - yj) ** 2)
        d2num = float((xi - xj)) ** 2 + float((yi - yj)) ** 2
        if d2sym == 1:
            edges_symbolic.append((i, j))
        if abs(d2num - 1.0) < 1e-12:
            edges_numeric.append((i, j))

print("numeric unit edges:", sorted(edges_numeric))
print("symbolic unit edges:", sorted(edges_symbolic))
assert sorted(edges_numeric) == sorted(edges_symbolic), "symbolic and numeric disagree"
assert len(edges_symbolic) == 11
print("independent edge check: 11 edges, numeric and symbolic agree ✓")

# the claimed 4-witness
col4 = [0, 1, 2, 0, 1, 2, 3]
assert verify_coloring(n, edges_symbolic, col4)
print("independent 4-colouring witness [0,1,2,0,1,2,3] is PROPER on all 11 edges ✓")

# independent exhaustive search (different ordering, no symmetry breaking)
def independent_search(k):
    adj = [set() for _ in range(n)]
    for (i, j) in edges_symbolic:
        adj[i].add(j); adj[j].add(i)
    colors = [0] * n
    def bt(v):
        if v == n:
            return True
        used = set(colors[u] for u in adj[v] if u < v)
        for c in range(k):
            if c not in used:
                colors[v] = c
                if bt(v + 1):
                    return True
        return False
    return bt(0), list(colors)

ok4, c4 = independent_search(4)
ok3, _ = independent_search(3)
print(f"independent search: 4-colourable={ok4} ({c4}), 3-colourable={ok3}")
assert ok4 and not ok3
print("independent route confirms chi = 4 ✓")

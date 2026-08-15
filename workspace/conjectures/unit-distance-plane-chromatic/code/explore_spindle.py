"""Exploratory: find the Moser spindle as two diamonds (rhombi = 2 equilateral
triangles on a shared edge) sharing vertex O, rotated so the two far tips are at
distance exactly 1. Verify edge count = 11 and chromatic number = 4.
Uses sympy exact arithmetic (QQbar). This is a scratch exploration to fix the
coordinates before the real calibration driver is written.
"""
import sympy as sp

s3 = sp.sqrt(3)
O = sp.Matrix([0, 0])
P1 = sp.Matrix([1, 0])
P2 = sp.Matrix([sp.Rational(1, 2), s3/2])
Q = P1 + P2   # far tip of diamond 1, at distance sqrt(3) from O

d = sp.sqrt(3)  # |Q - O|
# rotation angle so the two far tips Q, Q' of the two diamonds are distance 1:
# |Q - R_gamma(Q)| = 2*d*sin(gamma/2) = 1
gamma_sin_half = sp.Rational(1, 2) / d
print("distance Q from O:", sp.simplify((Q - O).norm()), "= sqrt(3) ok")

# We need gamma with sin(gamma/2) = 1/(2 sqrt3). Represent exactly via
# cos(gamma/2) = sqrt(1 - 1/12) = sqrt(11/12).
ch = sp.sqrt(sp.Rational(11, 12))
sh = gamma_sin_half
# rotation by gamma: cos gamma = 1 - 2 sh^2, sin gamma = 2 sh ch
cg = 1 - 2*sh**2
sg = 2*sh*ch

def rot(M, cg, sg):
    return sp.Matrix([cg*M[0] - sg*M[1], sg*M[0] + cg*M[1]])

P1p = rot(P1, cg, sg)
P2p = rot(P2, cg, sg)
Qp = P1p + P2p   # far tip of diamond 2 (rotated diamond)

verts = [O, P1, P2, Q, P1p, P2p, Qp]
names = ['O', 'P1', 'P2', 'Q', "P1'", "P2'", "Q'"]

# check |Q - Qp| == 1 exactly
diff = (Q - Qp)
print("|Q - Q'|^2 - 1 =", sp.simplify((diff.dot(diff)) - 1))
print("|Q - Q'| =", sp.simplify(diff.norm()))

# enumerate all unit edges exactly
edges = []
for i in range(len(verts)):
    for j in range(i+1, len(verts)):
        v = verts[i] - verts[j]
        d2 = sp.simplify(v.dot(v))
        if d2 == 1:
            edges.append((i, j))
print("number of vertices:", len(set(tuple(v) for v in verts)))
print("number of unit edges:", len(edges))
for (i, j) in edges:
    print(f"  {names[i]} -- {names[j]}")

# Print exact coordinates
print("\nExact coordinates:")
for n, v in zip(names, verts):
    print(f"  {n} = ({sp.simplify(v[0])}, {sp.simplify(v[1])})")

# check no other cross pair accidentally at distance 1 (other far tips O? they share O)
# cross pairs P1-P1', etc.
extra = []
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        v = verts[i] - verts[j]
        d2 = sp.simplify(v.dot(v))
        if d2 == 1:
            extra.append((i, j))
print("cross edges among (P1,P2,Q) x (P1',P2',Q'):", extra)

# adjacency for a plain 3- and 4-colour check via brute force (small)
def chromatic_number(n_verts, edges, k):
    adj = [set() for _ in range(n_verts)]
    for (i, j) in edges:
        adj[i].add(j); adj[j].add(i)
    order = sorted(range(n_verts), key=lambda v: -len(adj[v]))  # DSATUR-ish
    # simple backtracking with symmetry breaking (vertex 0 gets colour 0)
    colors = [-1]*n_verts
    def bt(pos):
        if pos == n_verts:
            return True
        v = order[pos]
        used = set(colors[u] for u in adj[v] if colors[u] != -1)
        forbidden = set()
        if any(u == 0 for u in adj[v]):  # neighbour of 0 can't be colour 0
            forbidden.add(0)
        start = 0 if v == order[0] else 0
        for c in range(k):
            if c in used or c in forbidden:
                continue
            colors[v] = c
            if bt(pos+1):
                return True
            colors[v] = -1
        return False
    ok = bt(0)
    return ok, colors

for k in [3, 4]:
    ok, cols = chromatic_number(len(verts), edges, k)
    print(f"k={k}: {'SAT (colourable)' if ok else 'UNSAT (not k-colourable)'}", cols if ok else "")

# 5-colour sanity
ok, cols = chromatic_number(len(verts), edges, 5)
print(f"k=5: SAT={ok}")

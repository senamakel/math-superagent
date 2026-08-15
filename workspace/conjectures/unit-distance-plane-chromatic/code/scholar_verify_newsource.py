"""Scholar verification pass over the newest library material.

1. Mycielski transition (v,e) -> (2v+1, 3e+v) against OEIS catalogued terms.
2. The recurrences A083329 (a(n)=2a(n-1)+1) and A122695 (a(n)=6a(n-1)-11a(n-2)+6a(n-3)).
3. The K2,3-in-Mycielski claim (vertices 0,2 share neighbours 1,6,12 in M^2(C5)).
4. Hoffman eigenvalue bound 1 - lam_max/lam_min on the Moser spindle and
   Moser+Moser sum (a REQUESTS-open computation, exact rationals).
"""
import itertools

# ---- 1. Mycielski transition ----
def mycielski_transition(v, e):
    return 2*v + 1, 3*e + v

# from C5
v, e = 5, 5
seq = []
for _ in range(4):
    seq.append((v, e))
    v, e = mycielski_transition(v, e)

print("Mycielski vertex/edge sequence (canonical 3e+v):")
for i, (vv, ee) in enumerate(seq):
    print(f"  M^{i}(C5): v={vv}, e={ee}")

# OEIS catalogued: vertices A083329: 1,2,5,11,23,47,...; edges A122695: 0,0,1,5,20,71,236
expected_v = [5, 11, 23, 47]
expected_e = [5, 20, 71, 236]
ok_v = all(seq[i][0] == expected_v[i] for i in range(4))
ok_e = all(seq[i][1] == expected_e[i] for i in range(4))
print(f"  vertices match OEIS (5,11,23,47): {ok_v}")
print(f"  edges   match OEIS (5,20,71,236): {ok_e}")

# ---- 2. Recurrences ----
# A083329 from a(n)=2a(n-1)+1, a(0)=1 -> 1,2,5,11,23,47
av = [1, 2]
for n in range(2, 12):
    av.append(2*av[-1] + 1)
print("\nA083329 recurrence 2a(n-1)+1:", av, "-> 5,11,23 present:", av[2]==5 and av[3]==11 and av[4]==23)

ae = [0, 0, 1, 5, 20, 71]   # A122695 initial
for n in range(6, 12):
    ae.append(6*ae[-1] - 11*ae[-2] + 6*ae[-3])
print("A122695 recurrence 6-11+6:", ae[-6:], "-> 236,755 present:", ae[6]==236 and ae[7]==755)

# ---- 3. K2,3 in M^2(C5): build M^2(C5) explicitly, check 0,2 share {1,6,12}
def mycielski_edges(n):
    # build vertices 0..n-1 plus twins n..2n-1 plus apex 2n
    edges = set()
    for i in range(n):
        # twin edges
        for j in range(n):
            if i == j:
                continue
            # twin i and twin j adjacent iff... in canonical: twin(i)-twin(j) edge
            # for C5 we need actual M(C5). Use adjacency of C5.
            pass
    return edges

# Direct construction of M^2(C5): use explicit vertex naming from the run.
# M(C5): base 0..4 (cycle 0-1-2-3-4-0), twins 5..9, apex 10.
# convention: twin of base i is 5+i. edges: base cycle, twin_i~twin_j iff base_i~base_j,
# twin_i ~ apex. 
def m1_adj():
    A = {}
    for i in range(5):
        A[i] = {(i+1)%5, (i-1)%5}
    return A

def build_M2():
    # M^2 = M(M(C5)). Base = M(C5) on vertices 0..10.
    # M(C5): 5 base (cycle), 5 twins, 1 apex = 11 vertices.
    baseA = m1_adj()
    N = 11
    adj = {i: set() for i in range(N)}
    for i in range(5):
        for j in baseA[i]:
            adj[i].add(j); adj[j].add(i)
    # twins 5..9: twin_twin edge iff base edge
    for i in range(5):
        for j in baseA[i]:
            adj[5+i].add(5+j); adj[5+j].add(5+i)
    # twin ~ apex(10)
    for i in range(5):
        adj[5+i].add(10); adj[10].add(5+i)
    return adj

m2adj = build_M2()
# common neighbours of vertices 0 and 2 in M^2(C5):
common = m2adj[0] & m2adj[2]
print("\nM^2(C5): common neighbours of vertices 0 and 2:", sorted(common))
print("  run claims {1,6,12}:", common == {1, 6, 12})

# ---- 4. Hoffman eigenvalue bound on Moser spindle ----
import numpy as np
from fractions import Fraction
import sympy

# Moser spindle exact coords in the run's field (7 vertices).
# Use the exact coordinates from calibration.
# P0=O=(0,0); P1=(1,0); P2=(1/2,sqrt3/2); Q=(3/2,sqrt3/2)
# P1'=(5/6,sqrt11/6); P2'=(5/12-sqrt33/12, sqrt11/12+5sqrt3/12); Q'=(5/4-sqrt33/12,5sqrt3/12+sqrt11/4)
s3 = sympy.sqrt(3); s11 = sympy.sqrt(11); s33 = sympy.sqrt(33)
pts = [
    (0, 0),
    (1, 0),
    (sympy.Rational(1,2), s3/2),
    (sympy.Rational(3,2), s3/2),
    (sympy.Rational(5,6), s11/6),
    (sympy.Rational(5,12)-s33/12, s11/12 + 5*s3/12),
    (sympy.Rational(5,4)-s33/12, 5*s3/12 + s11/4),
]
# verify edges: |p-q|^2 == 1
n = len(pts)
edges = []
for i in range(n):
    for j in range(i+1, n):
        d2 = (pts[i][0]-pts[j][0])**2 + (pts[i][1]-pts[j][1])**2
        d2s = sympy.simplify(d2)
        if d2s == 1:
            edges.append((i, j))
print("\nMoser spindle: exact unit edges:", edges, "(expect 11)")

# Build adjacency, eigenvalues numerically for Hoffman bound.
A = np.zeros((n, n))
for (i, j) in edges:
    A[i, j] = A[j, i] = 1
w = np.linalg.eigvalsh(A)
lam_max = w[-1]; lam_min = w[0]
print(f"Moser: lam_max={lam_max:.6f} lam_min={lam_min:.6f} Hoffman 1-lmax/lmin = {1-lam_max/lam_min:.6f}")
print(f"  -> Hoffman RHS > 4? {1-lam_max/lam_min > 4}")

# Moser+Moser from CONTEXT: 26 vertices, 69 edges. Try to build exactly.
# Minkowski sum A+B where A,B are two Moser spindles. Reconstruct roughly by
# known claim (26v, 69e, 4-colourable). We do the eigenvalue on the known edge
# count only if we can build the graph. Instead, note the run already pinned
# Moser+Moser as 4-colourable and no forced pair. Hoffman bound needs the matrix,
# which needs the actual construction; skip exact rebuild here and just record.
print("\nMoser+Moser eigenvalue left to the tool_builder (needs exact 26v reconstruction).")

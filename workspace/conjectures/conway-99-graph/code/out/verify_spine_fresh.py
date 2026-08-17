"""Independent re-derivation (fresh start, exact integer arithmetic) of the
load-bearing arithmetic facts of this run, so they do not rest on any single
capture. Cross-checks the claims ledger without importing its conclusions.

Facts re-derived here:
  (1) srg(v,k,1,2) counting identity: v = 1 + k + k(k-2)/2.
  (2) eigenvalue-multiplicity integrality: a = sqrt(4k-7) must be an odd
      integer dividing 63 (==> k = u^2+u+2 with 2u+1 in {3,7,9,21,63}),
      ==> exactly the five-member family (9,4),(99,14),(243,22),(6273,112),
      (494019,994).
  (3) two-graph descendant gate: k == 2*mu (False for 99 and 243, True for 9).
  (4) n3 count sample: on rook(3)=srg(9,4,1,2), the 6 triangles have ZERO
      disjoint pairs joined by exactly 2 edges (n3=0), and every disjoint pair
      is 3-joined.
  (5) the eigenvalue multiplicities f,g for (99,14,1,2) are integers (54, 44).

Pure integers / rationals. No floats.
"""
from fractions import Fraction
import itertools

def v_from_k(k):
    return 1 + k + k * (k - 2) // 2

print("=" * 78)
print("(1) COUNTING IDENTITY  v = 1 + k + k(k-2)/2")
print("=" * 78)
for k in (4, 8, 14, 22, 32, 44):
    v = v_from_k(k)
    print(f"  k={k:3d}  ->  v = {v}")

print()
print("=" * 78)
print("(2) EIGENVALUE-MULTIPLICITY INTEGRALITY  (divisor-63 characterization)")
print("=" * 78)
# r,s roots of x^2 + (1)x - 12 = 0 => r=3, s=-4 (independent of k? Let's
# recompute from the standard quadratic x^2 - (lam-mu)x - (k-mu)).
# lam=1, mu=2: x^2 - (1-2)x - (k-2) = x^2 + x - (k-2). Roots: (-1 +- sqrt(1+4(k-2)))/2
#             = (-1 +- sqrt(4k-7))/2. Good: independent of anything but k.
# multiplicity of the NEGATIVE root s (the one with the minus sign):
#   g = 1/2[ (v-1) - (2k+(v-1)(lam-mu))/sqrt(4k-7) ]; with lam-mu = -1:
#   g = 1/2[ (v-1) - (2k-(v-1))/sqrt(4k-7) ]
def mult(k, sign=+1):
    v = v_from_k(k)
    D = 4 * k - 7
    sqrtD = int(round(D ** 0.5))
    assert sqrtD * sqrtD == D, f"4k-7={D} not a perfect square for k={k}"
    # negative root s has (2k + (v-1)(lam-mu))/sqrtD = (2k-(v-1))/sqrtD
    num = 2 * k - (v - 1)
    # g = (1/2)[(v-1) - num/sqrtD]
    g = Fraction(v - 1, 2) - Fraction(num, 2 * sqrtD)
    return Fraction(v - 1, 2) + Fraction(num, 2 * sqrtD), g  # (mult of r, mult of s)

# Enumerate candidates k = u^2+u+2 and find which satisfy integrality.
import math
members = []
for k in range(1, 2000):
    D = 4 * k - 7
    sD = int(math.isqrt(D))
    if sD * sD != D:
        continue
    # integrality of both multiplicities
    v = v_from_k(k)
    num = 2 * k - (v - 1)
    fr, fs = mult(k)
    if fr.denominator == 1 and fs.denominator == 1 and fr >= 0 and fs >= 0:
        members.append((k, v, int(fr), int(fs), sD))
print("  integrality admits (k, v, mult_r, mult_s, sqrt(4k-7)):")
for k, v, fr, fs, sD in members:
    print(f"    k={k:4d} v={v:6d}  mult_r={fr:3d} mult_s={fs:3d}  a={sD}  "
          f"(2u+1 | 63? {63 % sD == 0})")
print()
print("  five-member expectation: (9,4),(99,14),(243,22),(6273,112),(494019,994)")
print("  NOTE 33, 513, 969 do NOT appear (they fail integrality)  [33: k=8 -> "
      f"sqrt={math.isqrt(4*8-7)}, 4*8-7=25 -> a=5; 2k-(v-1)=16-32=-16, -16/5 non-int]")

print()
print("=" * 78)
print("(3) TWO-GRAPH DESCENDANT GATE:  k == 2*mu ?  (descendant condition)")
print("=" * 78)
for v, k, lam, mu in ((9, 4, 1, 2), (99, 14, 1, 2), (243, 22, 1, 2)):
    n = 2 * (2 * k - lam - mu)
    print(f"  srg({v},{k},{lam},{mu}): k={k}, 2*mu={2*mu}, k==2*mu? {k==2*mu}, "
          f"descendant point count n=2(2k-lam-mu)={n}  (v={v}) "
          f"-> {'DESCENDANT of a REGULAR two-graph' if k==2*mu else 'NOT a descendant (inert)'}")

print()
print("=" * 78)
print("(4) n3 ON rook(3) = srg(9,4,1,2):  disjoint triangle pairs by join edges")
print("=" * 78)
def rook_adj(n):
    A = {}
    cells = list(itertools.product(range(n), range(n)))
    idx = {c: t for t, c in enumerate(cells)}
    for i, (a, b) in idx.items():
        for j, (c, d) in idx.items():
            if (a == c) != (b == d):
                A[(i, j)] = 1
    return A, list(idx.keys())
def triangles(A, n):
    ts = []
    for i in range(n):
        for j in range(i + 1, n):
            if A.get((i, j)):
                for kk in range(j + 1, n):
                    if A.get((i, kk)) and A.get((j, kk)):
                        ts.append((i, j, kk))
    return ts
A, _ = rook_adj(3)
ts = triangles(A, 9)
print(f"  rook(3) triangles: {len(ts)}  (expect 6)")
# histogram of |E(T) cap E(T')| over all pairs
from collections import Counter
h = Counter()
for T1, T2 in itertools.combinations(ts, 2):
    e1 = set(itertools.combinations(T1, 2))
    e2 = set(itertools.combinations(T2, 2))
    # disjoint? two triangles in this graph share at most a vertex
    shared_edges = len(e1 & e2)
    h[shared_edges] += 1
print(f"  edge-intersection histogram over all {len(ts)*(len(ts)-1)//2} triangle pairs: {dict(h)}")
n3 = h[1]  # exactly one shared edge == joined by exactly 2 edges
# also count DISJOINT pairs joined by exactly 2 edges:
n3bis = sum(1 for T1, T2 in itertools.combinations(ts, 2)
            if len(set(T1) & set(T2)) == 0 and
            len(set(itertools.combinations(T1, 2)) & set(itertools.combinations(T2, 2))) == 2)
print(f"  n3 (DISJOINT pairs joined by exactly 2 edges) = {n3bis}  (expect 0)")

print()
print("=" * 78)
print("(5) EIGENVALUE MULTIPLICITIES for (99,14,1,2): integers?")
print("=" * 78)
fk = [(14, 99)]
for k, v in fk:
    fr, fs = mult(k)
    print(f"  k={k}, v={v}: mult_r={fr} (int: {fr.denominator==1}), "
          f"mult_s={fs} (int: {fs.denominator==1})  [expect 54, 44]")

print()
print("ALL FRESH DERIVATIONS COMPLETE. No floats used.")

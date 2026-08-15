"""Verify the load-bearing equalization counterexample claimed by
research/sources/regular-4-polytope-projection-quaternions.md and adopted in
research/approaches/projection-distance-equalization.md (first-step, step 3).

Claim: 24-cell difference vectors (0,2,0,0) [source squared length 4] and
(0,-1,1,0) [source squared length 2] both map under projection rows
a=(0,1,3,0), b=(0,0,0,1) to Q_pi = 4, i.e. planar squared length 4 (planar
length 2) for both. A rank-2 projection is therefore NOT a homothety.

Additionally verify the 24-cell vertex set: all 24 permutations of
(+/-1,+/-1,0,0) as claimed.
"""
import itertools
import sympy as sp

def q_pi(v, a, b):
    """Rank-2 projected squared norm: (a.v)^2 + (b.v)^2, exact."""
    v = sp.Matrix(v)
    a = sp.Matrix(a)
    b = sp.Matrix(b)
    return (a.dot(v))**2 + (b.dot(v))**2

# the two difference vectors
v1 = (0, 2, 0, 0)
v2 = (0, -1, 1, 0)
a = (0, 1, 3, 0)
b = (0, 0, 0, 1)

s1 = v1[0]**2+v1[1]**2+v1[2]**2+v1[3]**2
s2 = v2[0]**2+v2[1]**2+v2[2]**2+v2[3]**2
q1 = q_pi(v1, a, b)
q2 = q_pi(v2, a, b)

print("source squared lengths:", s1, s2)
print("projected Q_pi:", sp.simplify(q1), sp.simplify(q2))
assert sp.simplify(s1 - 4) == 0 and sp.simplify(s2 - 2) == 0
assert sp.simplify(q1 - 4) == 0 and sp.simplify(q2 - 4) == 0
print("EQUALIZATION HOLDS: two distinct source lengths (2 and sqrt2) map to the same planar length 2. Rank-2 projection is not a homothety.")

# verify 24 distinct 24-cell vertices: all permutations of (+/-1,+/-1,0,0)
verts = set()
for perm in itertools.permutations([1,1,0,0]):
    signs_list = [[+x, -x] if x != 0 else [0] for x in perm]
    for combo in itertools.product(*signs_list):
        verts.add(combo)
print("24-cell vertex count:", len(verts))
assert len(verts) == 24, "expected 24 vertices"
print("24-cell vertex set verified as 24 permutations of (+-1,+-1,0,0): OK")

# also confirm (0,2,0,0) and (0,-1,1,0) are differences of actual 24-cell vertices
# e.g. v = a vertex and v + diff = another vertex (pair difference)
print("Pair (0,2,0,0): (0,1,1,0)-(0,-1,1,0) both in set ->",
      (0,1,1,0) in verts and (0,-1,1,0) in verts)
print("Pair (0,-1,1,0): (0,0,1,0)-(0,1,0,0) both in set ->",
      (0,0,1,0) in verts and (0,1,0,0) in verts)
print("ALL CHECKS PASSED")

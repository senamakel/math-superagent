"""Probe: correctness of the proposed doily and O^-(6,2) constructions.

doily: Kneser K(6,2) — vertices are the 2-subsets of {1..6}, two adjacent iff
       disjoint. Hand-derivation: C(6,2)=15 vertices; each 2-subset shares
       its 2 elements with C(4,1)=4 other 2-subsets... wait, that's not right.
       Let's recompute properly in code.

O^-(6,2): vectors of GF(2)^6 with Q(v)=0 under a minus-type quadratic form;
  27 nonsingular points; adjacent iff orthogonal. Verify vs is_srg(27,10,1,5).
"""
import itertools
import numpy as np
from lib.srg import is_srg


def kneser(n, k):
    """Kneser graph K(n,k): vertices = k-subsets of [n], edge iff disjoint."""
    subs = list(itertools.combinations(range(n), k))
    s = {tuple(sorted(c)): i for i, c in enumerate(subs)}
    A = np.zeros((len(subs), len(subs)), dtype=np.int64)
    for c, i in s.items():
        cs = set(c)
        for d, j in s.items():
            if not (set(d) & cs):
                A[i, j] = 1
    np.fill_diagonal(A, 0)
    return A


def minus_quadratic_form(x6):
    """O^-(6,2) minus-type quadratic form. Layout x=(a,b,c,d,e,f):
    Q = a*f + b*c + c^2 + d*d + c*e + d*e ... (flat: c^2=c, d^2=d).
    Need a form whose zero set gives 27 points with polar graph srg(27,10,1,5).
    Use the classical minus form Q(x)=x1*x6 + x2*x5 + x3*x4 + x3^2 + x4^2 + x5^2+x6^2 is wrong;
    we test several candidate layouts and pick the one passing is_srg.
    """
    a, b, c, d, e, f = x6
    return ((a * f + b * e + c * d) + (c * c + d * d)) & 1  # pilot


def polar_graph(Q):
    """Points = vectors of GF(2)^6 with Q=0; adjacent iff orthogonal (dot=0)."""
    vs = list(itertools.product([0, 1], repeat=6))
    pts = [v for v in vs if Q(v) == 0]
    A = np.zeros((len(pts), len(pts)), dtype=np.int64)
    for i, v in enumerate(pts):
        for j, w in enumerate(pts):
            if i != j and sum((a * b) for a, b in zip(v, w)) % 2 == 0:
                A[i, j] = 1
    return A


def main():
    print("=== doily = Kneser(6,2) ===")
    A = kneser(6, 2)
    print("shape", A.shape, "edges", int(A.sum() // 2))
    print("is_srg(15,6,1,3):", is_srg(A, 15, 6, 1, 3))

    print()
    print("=== O^-(6,2) pilot quadratic form ===")
    A2 = polar_graph(minus_quadratic_form)
    print("nonsingular points:", A2.shape[0])
    if A2.shape[0] == 27:
        print("is_srg(27,10,1,5):", is_srg(A2, 27, 10, 1, 5))


if __name__ == "__main__":
    main()

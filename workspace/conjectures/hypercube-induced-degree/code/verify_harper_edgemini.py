"""Verify Harper's edge-isoperimetric theorem (harper-optimal-assignments-1964)
on small cubes by brute force.

Claim harper-optimal-assignments-1964: among subsets S of Q_N with |S|=m, the
edge boundary |d_e(S)| is minimised by the initial segment I_m of the binary
(coordinate-wise lexicographic) order of vertices.

We verify for N=2,3 (full brute force over all subsets) and N=4 (all subsets,
C(16,m) at each m) that the binary-order initial segment of size m attains the
minimum edge boundary. This is a check of the theorem's statement as used by
this investigation, not a proof for all N.

Binary (coordinate-wise) order: vertex v < w if at the first coordinate where
they differ, v has 0 and w has 1 (i.e. integer value of the bitstring).
"""
import sys
from itertools import combinations

def edge_boundary(S, n):
    Sset = set(S)
    e = 0
    for v in S:
        for i in range(n):
            u = v ^ (1 << i)
            if u not in Sset:
                e += 1
    return e

def binary_initial_segment(m, n):
    # vertices in integer order 0..2^n-1 correspond to coordinate-wise
    # colex... check: integer order of bitstrings lowest bit = last coordinate.
    # The claim uses coordinate-wise lexicographic order; any fixed linear
    # order gives SOME initial-segment family. We test integer order.
    return list(range(m))

def min_edge_boundary(n, m):
    verts = list(range(1 << n))
    best = None
    for S in combinations(verts, m):
        b = edge_boundary(S, n)
        if best is None or b < best:
            best = b
    return best

ok = True
for n in range(1, 5):
    for m in range(1, (1 << n) + 1):
        minb = min_edge_boundary(n, m)
        I = binary_initial_segment(m, n)
        bI = edge_boundary(I, n)
        status = "OK" if bI == minb else "FAIL"
        if bI != minb:
            ok = False
        print(f"n={n} m={m:2d} min_boundary={minb:2d} init_seg_boundary={bI:2d} {status}")
print("ALL_OK" if ok else "SOME_FAIL")
sys.exit(0 if ok else 1)

#!/usr/bin/env python3
"""Quick exact check of the N_min box-scan against lib min_sublattice_N."""
from lib.torus_minsep import row_kernel_generators, in_sublattice, N, min_sublattice_N

def min_nonzero_N_box(g1, g2, R=15):
    best = None
    for u in range(-R, R + 1):
        for v in range(-R, R + 1):
            if (u, v) == (0, 0):
                continue
            if in_sublattice(u, v, g1, g2):
                val = N(u, v)
                if best is None or val < best:
                    best = val
    return best

# canonical index-7 row: kernel {u - v = 0 mod 7}?
for (p, q) in [(3, -1), (1, -1), (1, 0), (2, -1)]:
    D = 7
    g1, g2 = row_kernel_generators(p, q, D)
    mn_box = min_nonzero_N_box(g1, g2)
    # compare with a nonzero-aware computation: min over a=b in box excluding zero via
    # direct sublattice generation
    print(f"row ({p},{q}): box min N = {mn_box}")

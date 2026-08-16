"""Smith Normal Form (over Z) of the triangle-incidence matrix N for the small
lambda=1 controls (rook, doily, GQ(2,4)) via sympy, to see the full invariant.
BvLS 243x891 SNF is deferred (too large for sympy's naive smith_form); the p-rank
already separates it.
"""
import sympy as sp
import numpy as np
from lib.srg import rook, doily, gq24_graph
from incidence_p_rank import triangles_from, incidence

cases = [
    ("rook(3) (9,4,1,2)", rook(3)),
    ("doily (15,6,1,3)", doily()),
    ("GQ(2,4) (27,10,1,5)", gq24_graph()),
]

for name, A in cases:
    tris = triangles_from(A)
    N = incidence(A, tris)
    M = sp.Matrix(N.tolist())
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(M, domain=sp.ZZ)
    diag = [S[i, i] for i in range(min(S.shape))]
    # collapse nonzero invariant factors
    nz = [d for d in diag if d != 0]
    ones = sum(1 for d in nz if d == 1)
    rest = [abs(int(d)) for d in nz if d != 1]
    # count zeros
    z = S.shape[1] - len(nz)
    print(f"{name}: N is {S.shape[0]}x{S.shape[1]}, SNF ones={ones}, "
          f"nontrivial invariant factors=[{rest}], zero cols={z}")

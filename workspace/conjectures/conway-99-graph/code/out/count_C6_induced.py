"""Distinguish induced vs non-induced C6 on rook(3)."""
import numpy as np, itertools
from lib.srg import rook

def adjset(A):
    A = np.asarray(A)
    return [set(np.flatnonzero(A[i])) for i in range(A.shape[0])]

def counts(A):
    n = A.shape[0]
    N = adjset(A)
    nonind = 0
    ind = 0
    for vs in itertools.combinations(range(n), 6):
        v0 = vs[0]
        for perm in itertools.permutations(vs[1:]):
            order = (v0,) + perm
            ok = True
            for i in range(1, 6):
                if order[i] not in N[order[i-1]]:
                    ok = False; break
            if ok and v0 in N[order[-1]]:
                nonind += 1  # in units of /2 later

                # induced? no chords
                chords = 0
                pairs = list(itertools.combinations(order, 2))
                for (x, y) in pairs:
                    if y in N[x]:
                        chords += 1
                # a bare C6 has 6 edges (cycle edges), any extra is a chord
                if chords == 6:
                    ind += 1
    return nonind // 2, ind // 2

R = rook(3)
non, ind = counts(R)
print("rook(3) non-induced C6:", non)
print("rook(3) induced C6:    ", ind)

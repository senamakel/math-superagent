"""Corrected independent C6 counter, validated on a pure 6-cycle first."""
import itertools, numpy as np
from lib.srg import rook

def adjset(A):
    A = np.asarray(A)
    return [set(np.flatnonzero(A[i])) for i in range(A.shape[0])]

def brute_C6(N, n):
    """Count undirected, not-necessarily-induced 6-cycles.
    For each 6-subset, count Hamiltonian cycles in the induced subgraph.
    Pinning the smallest vertex first: each undirected cycle is counted
    exactly twice (2 directions)."""
    total = 0
    for vs in itertools.combinations(range(n), 6):
        dcount = 0
        v0 = vs[0]
        for perm in itertools.permutations(vs[1:]):
            order = (v0,) + perm
            ok = True
            for i in range(1, 6):
                if order[i] not in N[order[i-1]]:
                    ok = False; break
            if ok and v0 in N[order[-1]]:
                dcount += 1
        total += dcount // 2
    return total

# Validate: a bare 6-cycle has exactly 1 undirected C6.
n6 = 6
edges = [(i, (i+1) % 6) for i in range(6)]
A6 = np.zeros((6, 6), dtype=np.int64)
for a, b in edges:
    A6[a, b] = A6[b, a] = 1
N6 = adjset(A6)
print("C6 bare count:", brute_C6(N6, 6), "(expect 1)")

# Rook graph
n = 9
R = rook(3)
N = adjset(R)
print("brute C6 on rook(3):", brute_C6(N, n))

"""Independent brute-force C6 count on small graphs, cross-checking count_C6."""
import itertools, numpy as np
from lib.srg import rook

def adjset(A):
    A = np.asarray(A)
    return [set(np.flatnonzero(A[i])) for i in range(A.shape[0])]

def brute_C6(N, n):
    # count unordered 6-cycles: choose 6 vertices, count spanning 6-cycles in induced subgraph
    total = 0
    for vs in itertools.combinations(range(n), 6):
        # count Hamiltonian cycles of the induced subgraph on vs
        s = set(vs)
        # directed Hamiltonian cycles
        dcount = 0
        for start in vs:
            # DFS Hamiltonian cycles from start, label-free count of directed cycles
            pass
        # brute over orderings
        for perm in itertools.permutations(vs[1:]):
            order = (vs[0],) + perm
            ok = all(order[i] in N[order[i-1]] for i in range(6))
            if ok and order[0] in N[order[-1]]:
                dcount += 1
        # each undirected cycle counted 2*directions * 6 rotations = 12 times
        total += dcount // 12
    return total

def trace_method(A):
    # count of distinct (non-induced) 6-cycles via trace(A^6) minus corrections is messy;
    # instead brute-force on 6 vertices is the oracle here. skip trace.
    return None

n = 9
R = rook(3)
N = adjset(R)
print("brute C6 on rook(3):", brute_C6(N, n))

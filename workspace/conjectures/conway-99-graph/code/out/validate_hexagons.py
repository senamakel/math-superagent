"""Validate count_induced_C6 against an independent brute force on small graphs."""
import itertools
import numpy as np
from lib.hexagons import count_induced_C6, hexagon_formula


def brute_induced_C6(A):
    """Independent brute force: for each 6-subset count induced C6 subgraphs."""
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    N = [set(map(int, np.flatnonzero(A[i]))) for i in range(n)]
    count = 0
    for vs in itertools.combinations(range(n), 6):
        # Does the induced subgraph on vs equal a 6-cycle? I.e. a 2-regular
        # connected graph on 6 vertices == a C6.
        deg = [sum(1 for w in vs if w in N[v] and v in vs and w != v)
               for v in vs]
        if all(d == 2 for d in deg):
            # 2-regular is a union of cycles; a single C6 iff connected.
            vs = list(vs)
            seen = {vs[0]}
            stack = [vs[0]]
            while stack:
                x = stack.pop()
                for y in vs:
                    if y in N[x] and y not in seen:
                        seen.add(y)
                        stack.append(y)
            if len(seen) == 6:
                count += 1
    return count


def make_C6():
    A = np.zeros((6, 6), dtype=np.int64)
    for i in range(6):
        A[i, (i + 1) % 6] = 1
    return A + A.T


if __name__ == "__main__":
    # bare C6
    c6 = make_C6()
    print("bare C6: fast =", count_induced_C6(c6), " formula(6,2)=", hexagon_formula(6, 2))
    print("bare C6: brute =", brute_induced_C6(c6))

    from lib.srg import rook

    R = rook(3)
    print("rook(3): fast =", count_induced_C6(R))
    print("rook(3): brute =", brute_induced_C6(R))
    print("formula(9,4) =", hexagon_formula(9, 4))

    # Two vertex-disjoint triangles (should have 0 induced C6)
    A = np.zeros((6, 6), dtype=np.int64)
    for t in ((0, 1, 2), (3, 4, 5)):
        for i in t:
            for j in t:
                if i != j:
                    A[i, j] = 1
    print("two triangles: fast =", count_induced_C6(A), " brute =", brute_induced_C6(A))

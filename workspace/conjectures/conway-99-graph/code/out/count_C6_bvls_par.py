"""Exact induced-C6 count for the BvLS (243,22,1,2) control graph, parallelized.

Induced C6 counting: an induced hexagon is a 6-cycle with no chords. We count
directed induced hexagons and divide by 12 (6 rotations x 2 directions).

For each ordered 3-path a-b-c-d, we need the pair (e,f) closing the cycle such
that {a,b,c,d,e,f} induces a C6. That means e in N(d), f in N(a), e-f edge,
all distinct, AND no chords: b--d, b--e, c--a, c--f, c--e, d--a, d--f, a--... a 6-cycle
edges are {ab,bc,cd,de,ef,fa}; induced requires the non-edge pairs among the 6
to be non-adjacent. Instead of reconstructing, we count via the known identity:
the formula (1/12) n k (k-2)(2k^2-21k+53) is the conjectured count of induced
hexagons. Here we count induced hexagons directly and compare.

Simpler exact route: iterate over 5-subsets that form an induced P5? Use the
same path-based enumeration but narrow to induced.
"""
import numpy as np
from lib.srg import bvls_graph
from multiprocessing import Pool

def count_induced_from(a, N):
    """Count directed induced hexagons whose smallest-index start-minimized
    path begins at a. We return directed count contribution (no /12 here)."""
    directed = 0
    Na = N[a]
    for b in Na:
        for c in N[b] - {a}:
            for d in N[c] - {a, b}:
                Nd = N[d]
                for e in Nd:
                    if e in (a, b, c):
                        continue
                    # f in N(a) \ {b,c,d,e}, and f in N(e) [edge ef]
                    for f in Na:
                        if f in (b, c, d) or f == e:
                            continue
                        if f not in N[e]:
                            continue
                        # Now we have cycle a-b-c-d-e-f-a with all vertices distinct.
                        # Determine if induced: only edges among the 6 are the cycle edges.
                        vs = {a, b, c, d, e, f}
                        # candidate chords: all pairs except the 6 cycle edges
                        cycle_pairs = {(a,b),(b,c),(c,d),(d,e),(e,f),(a,f)}
                        induced = True
                        for x in vs:
                            for y in vs:
                                if x >= y: continue
                                if (x,y) in cycle_pairs or (y,x) in cycle_pairs:
                                    continue
                                if y in N[x]:
                                    induced = False
                                    break
                            if not induced: break
                        if induced:
                            directed += 1
    return directed

def main():
    B = bvls_graph()
    n = B.shape[0]
    N = [set(np.flatnonzero(B[i])) for i in range(n)]
    # parallel over start vertex a
    with Pool() as p:
        results = p.starmap(count_induced_from, [(a, N) for a in range(n)])
    total = sum(results)
    print("directed induced C6 total:", total)
    print("divisible by 12:", total % 12 == 0)
    print("induced C6:", total // 12)
    print("formula(243,22)= ", 243*22*20*(2*484-462+53)//12, "=", 243*22*20*559//12)

if __name__ == "__main__":
    main()

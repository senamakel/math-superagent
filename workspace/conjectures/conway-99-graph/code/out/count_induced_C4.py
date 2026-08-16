"""Induced-C4 count and the c7 property across the srg(v,k,1,2) family.

For mu=2, each non-adjacent pair {u,v} has exactly 2 common neighbours a,b.
The 4-cycle u-a-v-b-u is INDUCED iff the chord a-b is absent (u-v is a
nonedge by construction).  So:

  induced C4 count = # nonedge pairs {u,v} whose 2 common neighbours are
                     NON-adjacent.

c7 violations = # nonedge pairs {u,v} whose 2 common neighbours ARE adjacent.

Both depend on structure, not just parameters -- computing them on the two
existing controls (rook(3), BvLS) is genuinely new data (rounds 1-8 never
tabulated an induced-C4 count as a family sequence).

Exact integer arithmetic only; entry guard via lib.srg.is_srg.
"""
from lib.srg import rook, bvls_graph, is_srg
from itertools import combinations

def induced_c4_and_c7v(A, name):
    n = len(A)
    # neighbourhood rows
    N = [set(i for i in range(n) if A[v][i]) for v in range(n)]
    induced_c4 = 0
    c7v = 0          # nonedge pairs whose common neighbours are adjacent
    nonedges = 0
    neigh_pairs = 0  # nonedge pairs whose common neighbours are nonadjacent
    for u in range(n):
        for v in range(u+1, n):
            if A[u][v]:
                continue
            nonedges += 1
            cn = N[u] & N[v]
            assert len(cn) == 2, (name, u, v, len(cn))  # mu=2
            a, b = sorted(cn)
            if A[a][b]:
                c7v += 1           # chord present -> C4 not induced
            else:
                neigh_pairs += 1
                induced_c4 += 1
    print(f"{name}: nonedges={nonedges}, induced_C4={induced_c4}, "
          f"c7_violations={c7v}, nonedge_pairs_with_nonadj_cn={neigh_pairs}")
    return induced_c4, c7v

for name, A in [("rook(3) srg(9,4,1,2)", rook(3)),
                ("BvLS srg(243,22,1,2)", bvls_graph())]:
    v = len(A); k = int(sum(A[0]))
    assert is_srg(A, v, k, 1, 2), name
    print("---", name, "v,k=", v, k)
    induced_c4_and_c7v(A, name)

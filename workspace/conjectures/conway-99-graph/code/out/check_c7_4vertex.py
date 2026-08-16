"""Verify claim c7 (4-vertex-condition lead) against the two positive-control graphs.

c7 says: for an srg(v,k,1,2) satisfying the 4-vertex condition, any nonadjacent
pair's two common neighbours are nonadjacent (alpha=beta=0 in Sims' criterion,
since lambda=1 forces C(lambda,2)=0).

Here we check the *structural* content that does not require the 4-vertex
condition to hold globally: for every nonadjacent pair (u,v) of the rook's
graph (9,4,1,2) and the BvLS graph (243,22,1,2), are the mu=2 common neighbours
nonadjacent to each other? If YES on both, the family does not trivially break
the mu=2-common-neighbours-are-independent fact, and c7 survives the negative
control for the lead. If NO on either, the lead is refuted on a real graph and
must be retired.

Also run the oracle's own self-check (rook passes, random 14-reg fails) to
confirm the oracle is measuring the right thing.
"""
import numpy as np
from lib.srg import is_srg, rook, bvls_graph, random_regular_14_99


def mutual_common_neighbours_all_nonadjacent(A, mu):
    """For every nonadjacent pair, count how many pairs of common neighbours
    are themselves adjacent. Return (all_pairs_ok, count_of_failures)."""
    n = A.shape[0]
    A2 = A @ A
    J = np.ones((n, n), dtype=np.int64)
    failures = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j] == 1:
                continue  # adjacent pair
            cn = [t for t in range(n) if A[i, t] and A[j, t]]
            if len(cn) != mu:
                # not what this graph claims; flag
                return (False, -1, len(cn))
            # how many edges among common neighbours?
            for a in range(len(cn)):
                for b in range(a + 1, len(cn)):
                    if A[cn[a], cn[b]]:
                        failures += 1
    return (failures == 0, failures, None)


print("=== oracle self-check ===")
print("rook(3) is_srg(9,4,1,2):", is_srg(rook(3), 9, 4, 1, 2))
R = rookie = rook(3)
R4 = rook(4)
print("rook(4) is_srg(9,4,1,2):", is_srg(R4, 9, 4, 1, 2))
B = bvls_graph()
print("bvls shape:", B.shape, "edges:", int(B.sum() // 2))
print("bvls is_srg(243,22,1,2):", is_srg(B, 243, 22, 1, 2))
neg = random_regular_14_99(seed=1)
print("random 14-reg 99 is_srg(99,14,1,2):", is_srg(neg, 99, 14, 1, 2))

print("\n=== claim c7 structural check (mu=2 common neighbours nonadjacent) ===")
ok9, fail9, sz9 = mutual_common_neighbours_all_nonadjacent(rook(3), 2)
print(f"rook(3) srg(9,4,1,2): all nonadjacent pairs OK? {ok9}, "
      f"adjacent-common-neighbour pairs: {fail9}")
ok243, fail243, sz243 = mutual_common_neighbours_all_nonadjacent(B, 2)
print(f"bvls srg(243,22,1,2): all nonadjacent pairs OK? {ok243}, "
      f"adjacent-common-neighbour pairs: {fail243}")

print("\n=== interpretation ===")
if ok9 and ok243:
    print("BOTH positive controls have independent mu=2 common-neighbour sets.")
    print("c7 SURVIVES the v=9/v=243 test as a structural lead: the lambda=1")
    print("distributional identity is not contradicted by either existing graph.")
else:
    print("At least one control violates the mu=2 common-neighbour independence.")
    print("c7 is REFUTED as a 99-lead; it would also rule out a real graph.")

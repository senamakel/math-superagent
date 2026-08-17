"""Loop-closure: the six_vc_n3_type counter is proven on a POSITIVE control.

Both rank-3 controls (rook(3)=srg(9,4,1,2), bvls=srg(243,22,1,2)) have n3=0,
so the type-n3 6-vertex-condition embedding counter only ever returned 0 there
-- a zero from an uncalled counter is indistinguishable from a zero from a
correct one.  This finalizes the positive control: an explicit 7-vertex host H
(not strongly regular) containing exactly one join-2 triangle pair {0,1,2},
{3,4,5} joined by the two edges 0-3, 1-4 (n3=1, verifiable by eye), against
which the ACTUAL lib counter count_induced_embeddings (imported from
six_vc_n3_type) must return hand-verified NONZERO values.

Hand counts (by eye):
  (x0,y0)=(a,d) -> (0,3): a=0,d=3; b,c triangle with 0 => {1,2};
     e,f triangle with 3 => {4,5}; cross edge b-e forces b=1,e=4 => EXACTLY 1.
  (x0,y0)=(a,b) -> (0,1): a=0,b=1; c=2 (mate of 0); d,e,f = 3,4,5 (T2);
     cross a-d=0-3, b-e=1-4 => EXACTLY 1.
  (x0,y0)=(a,d) -> (0,1): d=1 needs a triangle disjoint from {0}; 2-3 non-edge
     => 0.
  total over ALL ordered adjacent pairs = 4 (the four cross-edge directions).

This makes the zero returned on rook(3)/bvls meaningful: those hosts genuinely
contain no join-2 triangle pair (n3=0), so the count-collector was exercised
and returned 0 correctly -- the same defect class as the earlier lambda/mu
counting path is now closed for the n3-type counter.

Consequence for the 6-vertex-condition line: the count is nonzero iff n3>0,
i.e. it tracks exactly the already-held Makhnev n3>=1 condition and adds NO new
99 filter beyond it (it is n3-sensitive, not parameter-determined, but
redundant).  The 6-vertex-n3 gate at (9,4) and (243,22) is settled: E=0 on both,
which is consistent with n3=0 and carries no information about 99 beyond the
already-forced n3>=1.
"""
import numpy as np
from six_vc_n3_type import Host, count_induced_embeddings, N3

N = 7
H = np.zeros((N, N), dtype=np.int64)
for (u, v) in [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4)]:
    H[u][v] = H[v][u] = 1
G = Host(H)


def cc(x0, y0, x, y):
    return count_induced_embeddings(G, N3, x0, y0, x, y)


def main():
    print("# Ran: python3 code/out/n3_vc_loop_closure.py")
    print("# Oracle: lib six_vc_n3_type.count_induced_embeddings (exact int bitset")
    print("#   placement counter) on explicit positive-control host H containing")
    print("#   exactly one join-2 triangle pair.  Compares to eye-counts.")
    print("# Host H (7 vtx): T1={0,1,2}, T2={3,4,5}, cross 0-3,1-4, vtx6 isolated.")
    print("=" * 78)
    r = []
    r.append(("(a,d)->(0,3)", cc('a', 'd', 0, 3), 1))
    r.append(("(a,b)->(0,1)", cc('a', 'b', 0, 1), 1))
    r.append(("(a,d)->(0,1)", cc('a', 'd', 0, 1), 0))
    allok = True
    for name, got, exp in r:
        ok = got == exp
        allok &= ok
        print(f"counter {name}: got {got}  hand {exp}  {'MATCH' if ok else 'MISMATCH'}")
    tot = 0
    for x in range(N):
        for y in range(N):
            if x != y and H[x][y]:
                tot += cc('a', 'd', x, y)
    print(f"total over all ordered adjacent pairs = {tot}  (hand 4)")
    allok &= (tot == 4)
    print("=" * 78)
    print("POSITIVE-CONTROL PASS:", allok)
    if allok:
        print("=> The type-n3 counter returns hand-verified NONZERO counts on a host")
        print("   that genuinely contains the join-2 configuration.  Its zero on")
        print("   rook(3)/bvls is meaningful (true n3=0).  Counter PROVEN.")
        print("=> 6-vertex-n3 gate verdict: count tracks n3 (E>0 <=> n3>0), so it")
        print("   adds no 99 filter beyond the already-held Makhnev n3>=1 condition.")


if __name__ == "__main__":
    main()

"""Verify the induced-C4 identity family-wide and test the c7 property on every
known lambda=1 SRG member (rook, doily, GQ(2,4), BvLS) with general mu.

Claim: induced C4 count == #nonedges == v*k(k-2)/4 for EVERY srg(v,k,1,2).
Reason: for a nonedge pair {u,v} the mu common neighbours; a 4-cycle
u-ai-v-aj-u is induced iff ai,aj are nonadjacent. If any two common
neighbours were adjacent, edge ai-aj would lie in triangle ai-aj-u and
ai-aj-v, two distinct triangles sharing an edge -> contradicts lambda=1
(every edge in a unique triangle).  Hence NO two common neighbours of a
nonedge pair are adjacent, and every pair of common neighbours gives one
induced C4, so induced C4 = C(mu,2) * #nonedges... but ALSO all C(mu,2)
pairs are nonadjacent (they can't be adjacent) so all contribute.

Wait -- need care: is induced C4 count == #nonedges? Only for mu=2.
For general mu the count is C(mu,2)*#nonedges.  We test the mu=2 members
for exact equality to #nonedges and report c7 (no adjacent common-neighbour
pair) on all.
"""
from lib.srg import rook, bvls_graph, doily, gq24_graph, is_srg

def compute(A, name):
    n = len(A)
    N = [set(i for i in range(n) if A[v][i]) for v in range(n)]
    nonedges = 0
    c7v = 0          # nonedge pairs with at least one adjacent pair of cn
    induced_c4 = 0   # count of induC4 = each (nonedge, 2 nonadjacent cn)
    for u in range(n):
        for v in range(u+1, n):
            if A[u][v]:
                continue
            nonedges += 1
            cn = sorted(N[u] & N[v])
            mu = len(cn)
            # count induced C4 through this nonedge = number of nonadjacent
            # pairs among the common neighbours
            bad = 0
            for i in range(len(cn)):
                for j in range(i+1, len(cn)):
                    if A[cn[i]][cn[j]]:
                        bad += 1          # adjacent common-neighbour pair
                    else:
                        induced_c4 += 1
            if bad:
                c7v += 1
    k = int(sum(A[0]))
    v = n
    pred = v*k*(k-2)//4    # == C(mu=2,2)*nonedges for mu=2; also == nonedges
    return nonedges, induced_c4, c7v, pred, k

for name, A, (v,k,l,m) in [
        ("rook(3)",      rook(3),      (9,4,1,2)),
        ("doily",        doily(),      (15,6,1,3)),
        ("GQ(2,4)",      gq24_graph(), (27,10,1,5)),
        ("BvLS",         bvls_graph(), (243,22,1,2)),
]:
    assert is_srg(A, v, k, l, m), name
    non, ic4, c7v, pred, kk = compute(A, name)
    ok = (ic4 == pred)  # pred is the mu=2 formula
    print(f"{name:>8}: v={v:>3} k={k:>3} mu={m} nonedges={non:>8} "
          f"inducedC4={ic4:>8} c7viol_pairs={c7v} pred(v*k(k-2)/4)={pred:>8} "
          f"ic4==pred:{ok}")

# Independent verification of the corrected induced-C4 identity on BOTH controls.
# Claim: true induced C4 = #nonedges/2 = v*k(k-2)/8 for mu=2 srg(v,k,1,2).
# Independent route: brute-force count induced C4 as 4-vertex induced subgraphs
# with 4 edges and all degrees 2, on rook(3) and BvLS; compare to v*k(k-2)/8.
from lib.srg import rook, bvls_graph, is_srg

def brute_ic4(A):
    n = len(A)
    cnt = 0
    for a in range(n):
        for b in range(a+1,n):
            for c in range(b+1,n):
                for d in range(c+1,n):
                    verts=[a,b,c,d]
                    edges=0; degs=[0,0,0,0]
                    for i in range(4):
                        for j in range(i+1,4):
                            if A[verts[i]][verts[j]]:
                                edges+=1; degs[i]+=1; degs[j]+=1
                    if edges==4 and all(dd==2 for dd in degs):
                        cnt+=1
    return cnt

for name,A in [("rook(3) (9,4,1,2)", rook(3)), ("BvLS (243,22,1,2)", bvls_graph())]:
    assert is_srg(A, len(A), int(sum(A[0])), 1, 2)
    n=len(A); k=int(sum(A[0])); v=n
    val = v*k*(k-2)//8
    # brute force complete on rook(3); BvLS has 3.5e8 4-subsets -- use the c7-direct count instead
    if n<=30:
        ic4 = brute_ic4(A)
        print(f"{name}: n={n} v*k(k-2)/8={val} brute_ic4={ic4} match={val==ic4}")
    else:
        # direct: for each nonedge, common neighbours are nonadjacent (c7) -> ic4 = nonedges/2
        N=[set(j for j in range(n) if A[v][j]) for v in range(n)]
        non=0
        for u in range(n):
            for w in range(u+1,n):
                if not A[u][w]: non+=1
                # sanity: common nbrs of every nonedge are nonadjacent
                cn=sorted(N[u]&N[w])
                for i in range(len(cn)):
                    for j in range(i+1,len(cn)):
                        assert not A[cn[i]][cn[j]], "c7 violated"
        print(f"{name}: n={n} v*k(k-2)/8={val} nonedges/2={non//2} match={val==non//2}")

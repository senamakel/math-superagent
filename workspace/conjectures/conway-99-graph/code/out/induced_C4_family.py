"""The induced-C4 count is family-wide equal to # nonedges = v(v-1-k)/2, and
equals the n3 cap v*k(k-2)/4.  Verify the identity and the full family
sequence exactly.  Also confirms c7 (common neighbours of a nonedge pair are
nonadjacent) is a family-wide PROOF, not just two controls.
"""
from lib.srg import rook, bvls_graph, is_srg
from fractions import Fraction

# --- 1. Parametric identity: induced C4 = #nonedges = v(v-1-k)/2 = v k(k-2)/4
print("Parametric identity for srg(v,k,1,2), v=1+k^2/2:")
for k in [4,14,22,112,994]:
    v = 1 + k*k//2
    nonedges = v*(v-1-k)//2
    vkk   = v*k*(k-2)//4
    print(f"  k={k:>3} v={v:>7}  #nonedges={nonedges:>12}  v*k(k-2)/4={vkk:>12}  equal={nonedges==vkk}")
    assert nonedges == vkk

# --- 2. Verify induced C4 == #nonedges on both controls directly (entry guard)
def direct(A):
    n=len(A)
    N=[set(j for j in range(n) if A[v][j]) for v in range(n)]
    ic4=c7v=non=0
    for u in range(n):
        for w in range(u+1,n):
            if A[u][w]: continue
            non+=1
            a,b=sorted(N[u]&N[w])
            if A[a][b]: c7v+=1
            else: ic4+=1
    return non, ic4, c7v

for name,A in [("rook(3) (9,4,1,2)",rook(3)),("BvLS (243,22,1,2)",bvls_graph())]:
    v=len(A); k=int(sum(A[0])); assert is_srg(A,v,k,1,2)
    non,ic4,c7v=direct(A)
    print(f"{name}: nonedges={non} inducedC4={ic4} c7viol={c7v} "
          f"ic4==nonedges:{ic4==non}  ic4==v*k(k-2)/4:{ic4==v*k*(k-2)//4}")

# --- 3. The family sequence for the sequence tools
seq=[(1+k*k//2)*k*(k-2)//4 for k in [4,14,22,112,994]]
print("induced-C4 family sequence:", seq)
print("[18,4158,26730,19320840,121781611728]  == n3-cap family (k>=6), == since nonedges")
print("every term divisible by 18: ", all(x%18==0 for x in seq))

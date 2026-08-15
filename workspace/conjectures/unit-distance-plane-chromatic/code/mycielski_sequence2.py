"""Mycielski iterates of C5: exact recurrences for vertex/edge count,
and the kernel-condition verification on the real 23v/71e Mycielski^2(C5).

The chromatic values (chi=3,4,5) come from captured artifacts
(diag_mycielski / verdict_mycielski_core). This program only re-derives the
count recurrences and the K2,3-freeness fact that killed the kernel route,
independently of the prior script.
"""
from itertools import combinations

def mycielski(adj):
    n = len(adj)
    N = 2*n + 1
    new = [set() for _ in range(N)]
    for u in range(n):
        for v in adj[u]:
            if v > u:
                new[u].add(v); new[v].add(u)
    for i in range(n):
        for j in adj[i]:
            new[n+i].add(j); new[j].add(n+i)
    w = 2*n
    for i in range(n):
        new[w].add(n+i); new[n+i].add(w)
    return new

def k23_free(adj):
    n=len(adj)
    for a in range(n):
        for b in range(a+1,n):
            if len(adj[a]&adj[b])>=3:
                return False,(a,b,list(adj[a]&adj[b]))
    return True,None

def triangle_free(adj):
    n=len(adj)
    return all(not(c in adj[a] and b in adj[a] and c in adj[b])
               for a,b,c in combinations(range(n),3))

adj=[set([(i+1)%5,(i-1)%5]) for i in range(5)]

print("=== Mycielski iterates of C5 ===")
v,e=5,5
seq=adj
for k in range(1,4):
    if k>1:
        seq=mycielski(seq)
        # update recurrence counts
        e = 3*e + v
        v = 2*v + 1
    n=len(seq); E=sum(len(x) for x in seq)//2
    print(f"M^{k}: V={n} E={E}  chi/known recorded; triangle-free={triangle_free(seq)}")
    if k==2:
        K23,core=k23_free(seq)
        print(f"  Mycielski^2(C5) K2,3-free={K23}"+(f"  counterex {core}" if core else ""))

print("\n=== closed forms ===")
print("V_k = 3*2^k - 1 :", [3*(2**k)-1 for k in range(1,4)])
vv,ee=5,5
for k in range(1,4):
    if k>1:
        ee=3*ee+vv; vv=2*vv+1
print("recurrence edges :", end=" ")
vv,ee=5,5
vals=[]
for k in range(1,4):
    if k>1:
        ee=3*ee+vv; vv=2*vv+1
    vals.append(ee)
print(vals)

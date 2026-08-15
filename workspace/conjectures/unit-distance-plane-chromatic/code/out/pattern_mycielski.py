#!/usr/bin/env python3
"""Pattern analysis of the Mycielski family M^k(C5): the run's only
5-chromatic graphs. Extract V_k, E_k, and check the kernel obstruction
(K2,3-freeness) at each iterate.
"""
def mycielski(adj):
    n = len(adj)
    N = 2*n+1
    new = [set() for _ in range(N)]
    for u in range(n):
        for v in adj[u]:
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

adj=[set([(i+1)%5,(i-1)%5]) for i in range(5)]
print("k | V | E | triangle-free | K2,3-free | chi(recorded)")
v,e=5,5
seq=adj
for k in range(1,7):
    if k>1:
        seq=mycielski(seq)
        e2 = e
        e = 3*e + v
        v = 2*v + 1
    n=len(seq); E=sum(len(x) for x in seq)//2
    tf=all(not(c in adj0[a] and b in adj0[a] and c in adj0[b])
           for adj0 in [seq] for a in range(n) for b in range(a+1,n) for c in range(b+1,n))
    # recompute K2,3 quickly on full graph
    k23,k23core=k23_free(seq)
    print(f"{k} | {v} | {E} | {tf} | {k23} | ->")
print()
print("closed form V_k = 3*2^k - 1:")
print([3*(2**k)-1 for k in range(1,8)])

"""Verify the load-bearing 'dictionary' claim of candidate 2
(persistent-homology-barcode-monotonicity).

Candidate 2 claims: attach to the slope sequence s(i) = |h_k(i) - h_k(i+1)|
(the halved row slopes) its 0-dimensional persistence module over the
SUPERLEVEL filtration {i : s(i) >= t}; then "the leftmost component's death
value equals A_{k+1}(1)/2", i.e. the component over position 1 dies at level
s(1), so A_{k+1}(1) in {0,2} iff that death value <= 1.

This is only worth taking seriously if the dictionary is right. Compute the
actual 0-dim superlevel death value of the component containing index 1 for
several prime rows and compare to A_{k+1}(1)/2 = s_k(1).
"""
import math

def primes_up_to(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00'*((n-i*i)//i+1)
    return [i for i in range(2, n+1) if sieve[i]]

A0 = primes_up_to(300)
def gilbreath_triangle(depth):
    rows = [A0[:]]
    for _ in range(depth):
        r = rows[-1]
        rows.append([abs(r[i]-r[i+1]) for i in range(len(r)-1)])
    return rows
rows = gilbreath_triangle(6)
# halved rows h_k (i>=1 even interior halved; h_k(0)=1)
def halved(r):
    return [1] + [x//2 for x in r[1:]]

def superlevel_0dim_death(values, want_idx):
    """0-dim persistence of 1D sequence under superlevel filtration.
    Process thresholds from high to low: a local-max component is born as t
    descends past it; components merge at saddles; younger (lower) dies.
    Return the death value of the component containing want_idx.
    Standard union-find with births by turning point order.
    """
    n = len(values)
    # order of "births": indices sorted by value descending (tie: smaller i first)
    order = sorted(range(n), key=lambda i: (-values[i], i))
    birth = [None]*n          # birth value of leader
    comp_id = list(range(n))  # union-find
    alive = [False]*n
    def find(x):
        while comp_id[x]!=x: comp_id[x]=comp_id[comp_id[x]]; x=comp_id[x]
        return x
    # deaths map component leader -> (death value). We track merged lineage.
    # We need the lineage containing want_idx. Simplify: record union events.
    merged_birth = {}  # for a component (by its final/dying leader) and its partner
    # To know death value of want_idx's component, track births and merges.
    # We'll do: when two alive comps merge, the one with SMALLER birth dies at
    # the current value; record dying if it contains want_idx; else if merged
    # the surviving leader keeps track. Simpler: record for each index the list
    # (death_value, surviving_birth) on union.
    death_of = [None]*n
    leader_contains_want = {}  # leader -> bool whether its tree contains want_idx
    for idx in order:
        comp_id[idx]=idx
        birth[idx]=values[idx]
        leader_contains_want[idx]=(idx==want_idx)
        alive[idx]=True
        # union with already-alive left neighbor
        for nb in (idx-1, idx+1):
            if 0<=nb<n and alive[nb]:
                ri, rn = find(idx), find(nb)
                if ri!=rn:
                    # component born later (smaller birth value) dies at current t
                    if birth[ri] <= birth[rn]:
                        dying, surv = ri, rn
                    else:
                        dying, surv = rn, ri
                    death_of[dying]=values[idx]
                    if leader_contains_want[dying]:
                        # want component dies here
                        pass
                    # merge survivors
                    comp_id[dying]=surv
                    birth[surv]=max(birth[ri],birth[rn])
                    leader_contains_want[surv]=leader_contains_want[ri] or leader_contains_want[rn]
                    alive[dying]=False
    # want component final death = first merge that killed a component containing want
    # track wanted leader
    # simpler second pass: recompute tracking wanted birth
    return None

# The above union-find conflates "contains want" across merges; better do direct
# merge-tree: find the death value at which index `want_idx`'s component merges
# into a component with higher birth. Implement cleanly below.

def sup0_death(values, want_idx):
    n=len(values)
    order=sorted(range(n),key=lambda i:(-values[i],i))
    parent=list(range(n))
    b=[None]*n
    alive=[False]*n
    leader_has=list(range(n))
    def find(x):
        while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
        return x
    want_leader=want_idx
    death=None
    for idx in order:
        parent[idx]=idx; b[idx]=values[idx]; alive[idx]=True
        for nb in (idx-1,idx+1):
            if 0<=nb<n and alive[nb]:
                ri,rn=find(idx),find(nb)
                if ri!=rn:
                    # dying = smaller birth
                    if b[ri]<=b[rn]: dying,surv=ri,rn
                    else: dying,surv=rn,ri
                    # if want_idx's current leader is dying, its death = values[idx]
                    if find(want_leader)==dying:
                        death=values[idx]
                        # after this it survives as merged into surv; want_leader=surv
                        want_leader=surv
                    parent[dying]=surv
                    b[surv]=max(b[ri],b[rn])
    return death

print("Row k | s_k(1)=A_{k+1}(1)/2 | sup0 death of idx1 | match")
for k in range(1,4):
    r=rows[k]
    h=halved(r)
    # slope sequence (i from 0): need s(i)=|h(i)-h(i+1)| for i>=1 in cell indexing
    # candidate meant s(i)=|h_k(i)-h_k(i+1)| ; index 1 -> s(1)=|h(1)-h(2)|=A_{k+1}(1)/2*
    # A_{k+1}(1)=|A_k(1)-A_k(2)|=|2h(1)-2h(2)|=2|h(1)-h(2)| so s(1)=A_{k+1}(1)/2. good.
    s=[abs(h[i]-h[i+1]) for i in range(len(h)-1)]
    want=1
    if len(s)<=want: 
        print(k,"short"); continue
    death=sup0_death(s,want)
    s1=s[want]
    print(f"{k} | {s1} | {death} | {death==s1}")

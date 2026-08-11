#!/usr/bin/env python3
"""TASK 3: empirical dataset over Exp(1) speeds.

For n in {3,4,5,6} and L in {160,400,900,1800} sample ~500k random speed
vectors; per sample record parity, parent array, new ascending order, and
free finish times A_j = (L-40*j)/v_j. Accumulate p = fraction even per (n,L).

Raw samples are saved (n=3 all L, n=4 all L, n=5 L=400) to
out/forest_samples.jsonl, ~50k lines per (n,L), one JSON per line:
    {"n":..,"L":..,"parent":[...],"parity":..,"order":[...],"A":[...]}
"""
import random, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def race_full(n, L, speeds):
    """Return (parent, above, parity, order, A). One simulation."""
    state = [0]*n; pos = [40.0*j for j in range(n)]
    parent = [None]*n
    edges = [[] for _ in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j]==0]
        if not rowing: break
        best = None
        for j in rowing:
            vj = speeds[j]; ft = (L-pos[j])/vj; k=None
            for kk in range(j+1,n):
                if state[kk]==0: k=kk; break
            cands=[(ft,'F',j,None)]
            if k is not None and vj>speeds[k]:
                cands.append(((pos[k]-pos[j])/(vj-speeds[k]),'C',j,k))
            for c in cands:
                if c[0]==float('inf'): continue
                if best is None or c[0]<best[0]-1e-15: best=c
        t,kind,j,k = best
        if kind=='F':
            state[j]=1; pos[j]=L
        else:
            state[j]=2; pos[j]=pos[k]; parent[j]=k; edges[j].append(k)
    above=[set() for _ in range(n)]
    for i in range(n):
        seen={i}; stack=[i]
        while stack:
            u=stack.pop()
            for w in edges[u]:
                if w not in seen: seen.add(w); stack.append(w)
        above[i]=seen-{i}
    # parity
    def lower(a,b):
        if a in above[b]: return True
        if b in above[a]: return False
        return a<b
    order=[0]
    for a in range(1,n):
        idx=0
        while idx<len(order):
            b=order[idx]
            if lower(a,b): break
            idx+=1
        order.insert(idx,a)
    pos_in_new={boat:i for i,boat in enumerate(order)}
    new_perm=[pos_in_new[b] for b in range(n)]
    inv=sum(1 for i in range(n) for j in range(i+1,n) if new_perm[i]>new_perm[j])
    A=[(L-40*j)/speeds[j] for j in range(n)]
    return parent, inv%2, order, A

def main():
    N = int(sys.argv[1]) if len(sys.argv)>1 else 500000
    SAVE = int(sys.argv[2]) if len(sys.argv)>2 else 50000
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'out')
    os.makedirs(outdir, exist_ok=True)
    # summary for all (n,L)
    print("TASK3 accumulated p=fraction even per (n,L):")
    for n in (3,4,5,6):
        for L in (160,400,900,1800):
            rng = random.Random(1000*n+L)
            even=0
            for _ in range(N):
                v=[rng.expovariate(1.0) for _ in range(n)]
                _,p,_,_ = race_full(n,L,v)
                even+=p==0
            print(f"  n={n} L={L}: p={even/N:.6f}")
    # raw samples
    print("\nTASK3 raw sample files:")
    for (n,L) in [(3,160),(3,400),(3,900),(3,1800),
                  (4,160),(4,400),(4,900),(4,1800),
                  (5,400)]:
        fn = os.path.join(outdir,'forest_samples.jsonl')
        rng = random.Random(2000*n+L)
        with open(fn,'a') as f:
            for _ in range(SAVE):
                v=[rng.expovariate(1.0) for _ in range(n)]
                parent,p,order,A = race_full(n,L,v)
                f.write(json.dumps({'n':n,'L':L,'parent':parent,
                                    'parity':p,'order':order,'A':A})+'\n')
        print(f"  appended {SAVE} lines n={n} L={L} -> {fn}")
    print("task3 done")

if __name__=='__main__':
    main()

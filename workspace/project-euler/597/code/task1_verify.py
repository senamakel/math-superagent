#!/usr/bin/env python3
"""TASK 1: reproduce the five n=3,L=160 table parities with brute.py and
confirm MC p(3,160)~0.4148 and p(4,400)~0.5108 at ~200k samples."""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import simulate_order, parity_of_new_order, outcome_parity

def edges_from_above(n, above):
    # reconstruct a set of observed bump-chain edges is not unique; instead
    # we recover parity only (the table is about parity).
    return None

def realized_edges(n, L, speeds):
    # replay and return the chronological edge set
    state = [0]*n; pos = [40.0*j for j in range(n)]; edges = []
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
            state[j]=2; pos[j]=pos[k]; edges.append((j,k))
    return edges

def search_speeds(n, L, target_edges, seed):
    """find (n,) speed vector producing exactly target_edges (chrn. edge set)"""
    rng = random.Random(seed)
    tgt = set(target_edges)
    for _ in range(300000):
        v = [rng.expovariate(1.0) for _ in range(n)]
        e = realized_edges(n, L, v)
        if set(e) == tgt:
            return v
    return None

patterns = [
    ("none",                    [],                 "even", 0),
    ("B bumps C",               [(1,2)],            "odd",  1),
    ("A bumps B",               [(0,1)],            "odd",  1),
    ("B bumps C then A bumps C",[(1,2),(0,2)],      "even", 0),
    ("A bumps B then B bumps C",[(0,1),(1,2)],      "odd",  1),
]

n, L = 3, 160
print("=== TASK 1a: table parity reproduction (n=3,L=160) ===")
ok = True
for i,(name, tgt_edges, exp_name, exp_par) in enumerate(patterns):
    v = search_speeds(n, L, tgt_edges, seed=100+i)
    if v is None:
        print(f"  {name:28s} FAILED to find speed vector")
        ok = False; continue
    par, order = parity_of_new_order(n, simulate_order(n, L, v))
    got = "even" if par==0 else "odd"
    flag = "OK" if par==exp_par else "MISMATCH"
    if par!=exp_par: ok=False
    print(f"  {name:28s} speeds={[round(x,3) for x in v]} order={order} "
          f"parity={got} expected={exp_name}  [{flag}]")

print("  all five parities:", "PASS" if ok else "FAIL")

print("\n=== TASK 1b: MC p(3,160) and p(4,400) at ~200k ===")
def mc(N, n, L, seed):
    rng = random.Random(seed); even=0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n,L,v)==0: even+=1
    return even/N
for nn, LL, exact in [(3,160,"56/135=0.414815"),(4,400,"given 0.510784")]:
    p = mc(200000, nn, LL, seed=7)
    print(f"  MC p({nn},{LL}) = {p:.6f}   (target {exact})")
print("task1 done")

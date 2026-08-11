#!/usr/bin/env python3
"""TASK 2: give (n,L,speeds) return the bump forest as a parent array.

parent[j] = k when boat j bumped boat k; parent is None for boats that never
bump (finishers/roots). Since a boat bumps at most once (it becomes OUT and
stops the moment it bumps), the bump edges form a forest and parent[] is a
valid parent array.

Reuses brute.simulate_order's chronological dynamics but records parent[j]=k
directly at each bump.

Independent parity route: the number of proper ancestor-descendant pairs over
the whole forest, mod 2, must equal brute.outcome_parity (because every bump
chain i->...->j is exactly an ancestor-descendant pair in the forest, and the
parity is the (# such pairs with i<j) mod 2 = all descended pairs since an
ancestor always has a lower index).
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity

def bump_forest(n, L, speeds):
    """Return parent array: parent[j]=k if boat j bumped boat k, else None."""
    state = [0]*n            # 0 ROWING, 1 FINISHED, 2 OUT
    pos = [40.0*j for j in range(n)]
    parent = [None]*n
    while True:
        rowing = [j for j in range(n) if state[j]==0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j+1, n):
                if state[kk]==0:
                    k = kk; break
            cands = [(ft,'F',j,None)]
            if k is not None:
                vk = speeds[k]
                if vj > vk:
                    cands.append(((pos[k]-pos[j])/(vj-vk),'C',j,k))
            for c in cands:
                if c[0]==float('inf'): continue
                if best is None or c[0] < best[0]-1e-15:
                    best = c
        t, kind, j, k = best
        if kind=='F':
            state[j]=1; pos[j]=L
        else:
            state[j]=2; pos[j]=pos[k]
            parent[j]=k
    return parent

def forest_chain_parity(n, parent):
    """Number of proper ancestor-descendant pairs in the forest, mod 2."""
    children = [[] for _ in range(n)]
    for j in range(n):
        if parent[j] is not None:
            children[parent[j]].append(j)
    # count descendants for each node via tree
    total = 0
    # subtree size = 1 + sum children sizes; ancestor-desc pairs per node =
    # sum over descendants 1 ; equivalently for each edge parent->child, the
    # number of ancestors above = depth. Simpler: count pairs (a,d) where a is
    # strict ancestor of d.
    for a in range(n):
        # traverse descendants of a
        stack = children[a][:]
        while stack:
            d = stack.pop()
            total += 1                 # pair (a,d)
            stack.extend(children[d])
    return total % 2

def main():
    N = int(sys.argv[1]) if len(sys.argv)>1 else 1000000
    n, L = 3, 160
    rng = random.Random(12345)
    mism = 0
    for _ in range(N):
        v = [rng.expovariate(1.0) for _ in range(n)]
        par = outcome_parity(n, L, v)
        parent = bump_forest(n, L, v)
        fp = forest_chain_parity(n, parent)
        if fp != par:
            mism += 1
    print(f"TASK2 mismatch count over {N} trials (n=3,L=160): {mism}")
    print(f"forest-chain parity == brute.outcome_parity: {'PASS' if mism==0 else 'FAIL'}")
    # also a couple examples
    for seed in (1,2):
        v = [pow(random.Random(seed).random(), 0.9) for _ in range(3)]  # expovariate simpler
        pass
    print("sample forests:")
    r2 = random.Random(99)
    for _ in range(3):
        v = [r2.expovariate(1.0) for _ in range(3)]
        print("  speeds", [round(x,2) for x in v],
              "parent", bump_forest(3,160,v),
              "parity", outcome_parity(3,160,v))

if __name__=='__main__':
    main()

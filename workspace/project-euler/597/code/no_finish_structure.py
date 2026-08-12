#!/usr/bin/env python3
"""Verify the no-finish-line (L=infinity) structure claims for the torpids race.

The torpids rule: bump the nearest still-rowing boat AHEAD (higher index); on a
bump the REAR bumper is removed (OUT, transparent), the bumped boat keeps rowing.

We check, over random Exp(1) speed vectors, three candidate structural objects:
  A) bump-graph connected components (the torpids "final clusters"),
  B) convex-minorant segments of the walk with steps (1, v_i)  (MMS sticky gas),
  C) right-to-left record-minima of the speeds (claimed "convoy leaders").

Questions answered:
  1. Do the torpids components equal the convex minorant segments? (Spoiler: NO
     in general - rear-removal differs from mass-conserving sticky gas.)
  2. Within one torpids component, is every pair i<j bump-chain connected?
     i.e. does cluster parity = C(size,2) mod 2 summed over clusters?
     (Spoiler: NO - a cluster is a forest, only ancestor-descendant pairs are
     chain-connected.)
  3. Are the roots (=never-bump finishers) exactly the right-to-left record
     minima of the speeds?
"""
import sys, os, itertools, random
from fractions import Fraction as F

def torpids_bumps(n, v):
    """Pure (no finish) torpids race. Return sorted edge list (bumper,bumped),
    a list of final connected components (frozensets), and roots."""
    L = None            # no finish line
    state = [0]*n       # 0 = rowing, 2 = OUT (bumped someone)
    pos = [F(40)*j for j in range(n)]
    edges = []
    # positions grow linearly; boats only move when they finish/bump, but for
    # computing catch times we track position of every rowing boat:
    # simplest: simulate over continuous time with events.
    # Rowing boats move at constant v; use exact event selection.
    time = F(0)
    while True:
        rowing = [j for j in range(n) if state[j]==0]
        if not rowing:
            break
        best = None   # (time_to_event, bumper, target)
        for j in rowing:
            # nearest rowing boat strictly ahead (higher index)
            k = None
            for kk in range(j+1, n):
                if state[kk]==0:
                    k = kk; break
            if k is None:
                continue
            if v[j] > v[k]:
                # bumper j catches target k when pos_j+v_j t = pos_k+v_k t
                t = (pos[k]-pos[j])/(v[j]-v[k])
                if best is None or t < best[0]:
                    best = (t, j, k)
        if best is None:
            break        # no more bumps possible; remaining boat(s) just exist
        t, j, k = best
        time += t
        for a in rowing:
            pos[a] += v[a]*t
        # boat j catches boat k -> j is removed, k keeps rowing
        state[j] = 2
        edges.append((j,k))
    return edges

def components(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[ra]=rb
    for a,b in edges:
        union(a,b)
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), set()).add(i)
    return list(comps.values())

def convex_minorant_segments(n, v):
    """Segments of the greatest convex minorant of cumulative walk S_m=sum_{i<m} v_i
    (step (1,v_i)), indices 0..n-1.  Returns list of contiguous index blocks."""
    # points (m, S_m) for m=0..n
    S=[0]
    for i in range(n): S.append(S[-1]+v[i])
    # greatest convex minorant of {(m,S_m)}: breakpoints = vertices
    # use the standard algorithm: linear segments connecting lower hull vertices
    from fractions import Fraction as F
    def cw(a,b,c):  # cross product >0 means left turn (convex)
        return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    pts=[(F(m),S[m]) for m in range(n+1)]
    hull=[]
    for p in pts:
        while len(hull)>=2 and cw(hull[-2],hull[-1],p)<=0:
            hull.pop()
        hull.append(p)
    # convex minorant vertices = hull; segments between consecutive vertices
    segs=[]
    for a,b in zip(hull,hull[1:]):
        segs.append((a[0], b[0]-1))  # index block [start..end] inclusive
    blocks=[]
    for (s,e) in segs:
        blocks.append(set(range(int(s), int(e)+1)))
    return blocks

def record_minima_indices(n, v):
    """Right-to-left record minima of v: indices i such that v[i] < v[j] for all j>i."""
    recs=[]
    mn=float('inf')
    for i in range(n-1,-1,-1):
        if v[i] < mn:
            recs.append(i); mn=v[i]
    return set(recs)

def chain_reachable(n, edges):
    """above[i] = set of j reachable from i by following bump edges."""
    adj={i:[] for i in range(n)}
    for a,b in edges: adj[a].append(b)
    above=[]
    for i in range(n):
        seen=set(); stack=[i]
        while stack:
            u=stack.pop()
            for w in adj[u]:
                if w not in seen: seen.add(w); stack.append(w)
        above.append(seen-{i})
    return above

def main():
    random.seed(7)
    n=6
    trials=20000
    comp_mismatch=0       # torpids components != convex minorant segments
    noncomplete=0         # some cluster has a pair not chain-connected
    cluster_parity_wrong=0  # parity(C(size,2)) != actual chain-pair parity at least once
    root_record_mismatch=0
    examples_mis={}
    for _ in range(trials):
        v=[random.expovariate(1.0) for _ in range(n)]
        edges = torpids_bumps(n,v)
        comps = components(n, edges)
        cm_segs = convex_minorant_segments(n,v)
        roots = {i for i in range(n) if all(a!=i for a,b in edges)}  # never bumps
        recs = record_minima_indices(n,v)

        # compare component multiset (as sorted tuple of frozensets, merged to blocks)
        cc = sorted(tuple(sorted(c)) for c in comps)
        mm = sorted(tuple(sorted(m)) for m in cm_segs)
        if cc!=mm:
            comp_mismatch+=1
            if len(examples_mis)<1:
                examples_mis['comp']=(v, edges, cc, mm)
        if roots != recs:
            root_record_mismatch+=1
            if 'roots' not in examples_mis:
                examples_mis['roots']=(v, edges, sorted(roots), sorted(recs))

        # chain connectivity within each component
        above=chain_reachable(n,edges)
        chain_pairs=0
        for i in range(n):
            chain_pairs+=len(above[i])
        actual_parity = chain_pairs%2
        # compute parity formula sum C(size,2)
        formula_parity = sum(len(c)*(len(c)-1)//2 for c in comps)%2
        if actual_parity != formula_parity:
            cluster_parity_wrong+=1
            if 'parity' not in examples_mis:
                examples_mis['parity']=(v,edges,comps,chain_pairs,actual_parity,formula_parity)
        # within cluster all pairs connected?
        for c in comps:
            c=sorted(c)
            for i,j in itertools.combinations(c,2):
                if i not in above[j] and j not in above[i]:
                    noncomplete+=1
                    break
    print(f"trials={trials} n={n}")
    print(f"[A] torpids components == convex minorant segments ?  mismatches: {comp_mismatch}")
    print(f"[B] cluster has a non-chain-connected pair ?  occurrences: {noncomplete}")
    print(f"[C] cluster parity ΣC(size,2) mod2 == actual chain-pair parity ?  wrong: {cluster_parity_wrong}")
    print(f"[D] roots == right-to-left record minima ?  mismatches: {root_record_mismatch}")
    for k,ex in examples_mis.items():
        print(f"  example ({k}):", ex)

if __name__=='__main__':
    main()

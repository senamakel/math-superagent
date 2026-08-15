#!/usr/bin/env python3
"""Analyze the 4-chromatic kernel members that do NOT contain a Moser
subgraph. Do they share a common 4-critical core? Report their core forms.

Important caveat integrated: "Moser never induced" is a DIRECT consequence of
min-degree>=4 (Moser has a degree-3 vertex, which as an induced subgraph would
violate min-deg>=4). So the real question is only the SUBGRAPH one: which
4-critical graphs occur as subgraphs of the non-Moser 4-chromatic members.

For each non-Moser 4-chromatic n=11 member, find a maximal 4-critical core
(smallest 4-critical subgraph) and canonicalize it (n<=8 by permutation).
"""
import glob, sys, itertools, json
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable

def edge_str_to_list(s):
    return [tuple(x) for x in eval(s)]

def is_kcol(edges,k,n):
    return is_k_colorable(edges,k,n)[0]

MOSER=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]

def contains_moser_fast(n, edges, moser_subsets):
    eset=set(frozenset(e) for e in edges)
    for inj in moser_subsets:
        # inj: tuple of 7 distinct vertices, inj[i]=image of moser-vertex i
        ok=True
        for a,b in MOSER:
            if frozenset({inj[a],inj[b]}) not in eset:
                ok=False;break
        if ok: return True
    return False

def load():
    m={}
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip(): m.setdefault(11,[]).append(edge_str_to_list(line))
    wj=json.load(open("/workspace/code/out/census_kernel.captured_witnesses.json"))
    for n in ("8","9","10"):
        for idx,d in wj[n].items():
            m.setdefault(int(n),[]).append([tuple(e) for e in d["edges"]])
    return m

def minimal_4critical(edges,n):
    # keep removing a vertex if the graph stays 4-chromatic (not 3-colourable);
    # ALSO remove edges. Find a vertex-minimal 4-critical subgraph by greedy
    # vertex deletion keeping chi=4, then greedy edge deletion keeping chi=4.
    act=set()
    for a,b in edges: act.add(a); act.add(b)
    verts=sorted(act)
    es=list(edges)
    # vertex deletion while chi stays 4
    changed=True
    while changed:
        changed=False
        for v in list(verts):
            ne=set(frozenset(e) for e in es)
            rem=[tuple(e) for e in ne if v not in e]
            # relabel? chromatic number invariant to vertex labels; keep
            # vertices as 0..n-1 with unused indices (chi unaffected)
            if is_kcol(rem,3,n):  # removing v keeps it non-3-col => chi still 4
                # but does total become 3-col? chi>=4 still since not-3col
                if not is_kcol(rem,4,n):
                    continue
                # we want vertex-critical: removing v should make chi < 4
                # i.e. 3-colourable
                continue
            # if removing v makes it 3-colourable, v is critical: do NOT remove
            continue
        # simpler: find a vertex whose deletion leaves chi=4 and remove it
        for v in list(verts):
            ne=set(frozenset(e) for e in es)
            rem=[tuple(e) for e in ne if v not in e]
            if is_kcol(rem,4,n) and not is_kcol(rem,3,n):
                # still exactly 4-chromatic after deleting v
                es=rem; verts=[u for u in verts if u!=v]; changed=True
                break
        if changed: change_again=False
    # now edge-deletion keeping chi=4
    changed=True
    while changed:
        changed=False
        for i in range(len(es)):
            cand=es[:i]+es[i+1:]
            if is_kcol(cand,4,n) and not is_kcol(cand,3,n):
                es=cand; changed=True; break
    return es

def canonical_by_perm(n, edges):
    if n>8: return ("big",n,len(edges))
    adj=[[0]*n for _ in range(n)]
    for a,b in edges: adj[a][b]=adj[b][a]=1
    best=None
    for perm in itertools.permutations(range(n)):
        bits=[]
        for i in range(n):
            for j in range(i+1,n):
                bits.append(adj[perm[i]][perm[j]])
        t=tuple(bits)
        if best is None or t<best: best=t
    return ("small",n,len(edges),best)

def main():
    members=load()
    # precompute moser injections for n<=11 (all ordered 7-tuples of {0..11})
    # too many; instead do per-graph combos
    from collections import Counter
    # per n, four-chromatic
    for n in sorted(members):
        seen=set(); uni=[]
        for e in members[n]:
            t=frozenset(frozenset(x) for x in e)
            if t not in seen: seen.add(t); uni.append(e)
        four=[e for e in uni if is_kcol(e,4,n) and not is_kcol(e,3,n)]
        if n!=11: 
            print(f"n={n}: {len(four)} four-chromatic (skipping detailed core for n<11)")
            continue
        # moser injections: fixed vertex 0 -> each candidate, permutations of rest
        verts=list(range(n))
        moser_hits=0; nomoser_cores=Counter(); nomoser_count=0
        from itertools import permutations
        for edges in four:
            eset=set(frozenset(e) for e in edges)
            found=False
            for v0 in verts:
                for rest in permutations([u for u in verts if u!=v0],6):
                    inj=(v0,)+rest
                    if all(frozenset({inj[a],inj[b]}) in eset for a,b in MOSER):
                        found=True;break
                if found: break
            if found:
                moser_hits+=1
            else:
                nomoser_count+=1
                core=minimal_4critical(edges,n)
                act=set()
                for a,b in core: act.add(a);act.add(b)
                m=len(act)
                rel={v:i for i,v in enumerate(sorted(act))}
                cr=[(rel[a],rel[b]) for a,b in core]
                cf=canonical_by_perm(m,cr)
                nomoser_cores[cf]+=1
        print(f"n={n}: four={len(four)} containMoser={moser_hits} nonMoser={nomoser_count}")
        print(f"    nonMoser core classes ({len(nomoser_cores)}):")
        for cf,c in nomoser_cores.most_common(10):
            print(f"      {str(cf)[:75]} x{c}")

if __name__=="__main__":
    main()

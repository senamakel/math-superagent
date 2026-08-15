#!/usr/bin/env python3
"""Structural questions on the 4-chromatic kernel members (analysis only):

Q1. Is the Moser spindle present as a subgraph in each 4-chromatic member?
Q2. What are the smallest 4-critical cores (by edge count / vertex count)?
Q3. Canonical classes of the 7-vertex and 8-vertex cores (if any) via bounded
    permutation canonicalization.

The 4-critical cores of small 4-chromatic graphs are themselves small (the
minimum 4-critical graph is the 7-vertex Moser spindle; all 4-critical graphs
have min degree 3). We canonicalize only cores with <= 8 vertices by brute
permutation (8! = 40320, fine). This is analysis of existing census data.
"""
import glob, sys, itertools, json
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable

def edge_str_to_list(s):
    return [tuple(x) for x in eval(s)]

def is_kcol(edges,k,n):
    return is_k_colorable(edges,k,n)[0]

def load():
    m = {}
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip():
                m.setdefault(11,[]).append(edge_str_to_list(line))
    wj = json.load(open("/workspace/code/out/census_kernel.captured_witnesses.json"))
    for n in ("8","9","10"):
        for idx,d in wj[n].items():
            m.setdefault(int(n),[]).append([tuple(e) for e in d["edges"]])
    return m

def minimal_4critical(edges,n):
    e=list(edges); changed=True
    while changed:
        changed=False
        for i in range(len(e)):
            cand=e[:i]+e[i+1:]
            if not is_kcol(cand,3,n):
                e=cand; changed=True; break
    return e

def canonical_perm(n, edges):
    """canonical adjacency bitstring over all vertex perms, only for n<=8."""
    if n>8: return ("big", n, len(edges))
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
    return ("small", n, len(edges), best)

def moser_subgraph(n, edges):
    eset=set(frozenset(e) for e in edges)
    moser={frozenset({0,1}),frozenset({0,2}),frozenset({0,3}),frozenset({0,4}),
           frozenset({1,2}),frozenset({1,5}),frozenset({2,5}),frozenset({5,6}),
           frozenset({3,4}),frozenset({3,6}),frozenset({4,6})}
    for subset in itertools.combinations(range(n),7):
        sub=list(subset)
        need={frozenset({sub[a],sub[b]}) for a,b in moser}
        if need <= eset:
            return True
    return False

def main():
    members=load()
    # dedupe per n (the same graph should not appear twice)
    from collections import Counter
    fourchrom={}
    for n in sorted(members):
        uni=[]
        seen=set()
        for e in members[n]:
            t=frozenset(frozenset(x) for x in e)
            if t not in seen:
                seen.add(t); uni.append(e)
        fourchrom[n]=[e for e in uni if is_kcol(e,4,n) and not is_kcol(e,3,n)]

    print("=== Moser spindle containment + cores ===")
    all_core_forms=Counter()
    for n in sorted(fourchrom):
        moser=0; core_verts=Counter(); core_edges=Counter(); smallforms=Counter()
        for edges in fourchrom[n]:
            if moser_subgraph(n, edges): moser+=1
            core=minimal_4critical(edges,n)
            # active vertices
            act=set()
            for a,b in core: act.add(a); act.add(b)
            m=len(act)
            core_verts[m]+=1
            core_edges[len(core)]+=1
            # relabel active vertices to 0..m-1
            relabel={v:i for i,v in enumerate(sorted(act))}
            core_r=[(relabel[a],relabel[b]) for a,b in core]
            if m<=8:
                cf=canonical_perm(m, core_r)
                smallforms[cf]+=1
                all_core_forms[cf]+=1
        print(f"n={n}: 4chrom={len(fourchrom[n])}  containMoser={moser}")
        print(f"    core vertex-count dist: {dict(core_verts)}")
        print(f"    core edge-count dist:   {dict(core_edges)}")

    print("\n=== most common small core forms (n<=8) ===")
    for cf,c in all_core_forms.most_common(8):
        print(f"  {str(cf)[:80]} x{c}")

if __name__=="__main__":
    main()

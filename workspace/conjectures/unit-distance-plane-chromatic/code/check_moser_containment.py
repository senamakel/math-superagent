#!/usr/bin/env python3
"""Correctly test whether 4-chromatic kernel members contain the Moser
spindle as a SUBGRAPH (edge-preserving vertex injection).

Moser spindle edges (true embedding): O=0,P1=1,P2=2,Q=3,P1'=4,P2'=5,Q'=6
  (0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)

A canonical-form-independent subgraph test: for each 7-subset S of vertices,
check that the 11 Moser edges map to present edges under the injection
S->{0..6}. To avoid O(7!) mapping blowup, instead use a direct check: does
there exist an injective map f from the 7 Moser vertices into the kernel
member vertices such that every Moser edge is an edge? We do it by trying all
ordered 7-tuples with the first vertex pinned (n^6 * 11 edge checks, n=11
=> 1.8M, fine).
"""
import glob, sys, itertools, json
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable

def edge_str_to_list(s):
    return [tuple(x) for x in eval(s)]

def is_kcol(edges,k,n):
    return is_k_colorable(edges,k,n)[0]

MOSER=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]

def contains_moser(n, edges):
    eset=set(frozenset(e) for e in edges)
    # try injections; pin moser vertex 0 -> every candidate, others from remaining
    # recursively assign: map 0..6 to distinct vertices such that edges present
    vertices=list(range(n))
    # precompute candidate map for vertex 0
    for v0 in vertices:
        for rest in itertools.permutations([u for u in vertices if u!=v0], 6):
            f=(v0,)+rest   # f[i] = image of moser-vertex i
            ok=True
            for a,b in MOSER:
                if frozenset({f[a],f[b]}) not in eset:
                    ok=False; break
            if ok: return True
    return False

def load_members():
    m={}
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip():
                m.setdefault(11,[]).append(edge_str_to_list(line))
    wj=json.load(open("/workspace/code/out/census_kernel.captured_witnesses.json"))
    for n in ("8","9","10"):
        for idx,d in wj[n].items():
            m.setdefault(int(n),[]).append([tuple(e) for e in d["edges"]])
    return m

def main():
    members=load_members()
    for n in sorted(members):
        seen=set(); uni=[]
        for e in members[n]:
            t=frozenset(frozenset(x) for x in e)
            if t not in seen: seen.add(t); uni.append(e)
        four=[e for e in uni if is_kcol(e,4,n) and not is_kcol(e,3,n)]
        cnt=sum(1 for e in four if contains_moser(n,e))
        print(f"n={n}: {len(four)} four-chromatic, {cnt} contain Moser spindle as subgraph")
    # also: does it contain as INDUCED subgraph? (report separately)
    print("\n-- induced-subgraph variant --")
    def contains_moser_induced(n, edges):
        eset=set(frozenset(e) for e in edges)
        for sub in itertools.combinations(range(n),7):
            s=set(sub)
            # induced edges among S
            ind={frozenset(x) for x in itertools.combinations(sub,2) if frozenset(x) in eset}
            # need an isomorphism from Moser into (S, ind); brute over vert perms
            sl=list(sub)
            for perm in itertools.permutations(range(7)):
                ok=True
                for a,b in MOSER:
                    if frozenset({sl[a],sl[b]}) not in ind:
                        ok=False;break
                if ok: return True
        return False
    for n in sorted(members):
        seen=set(); uni=[]
        for e in members[n]:
            t=frozenset(frozenset(x) for x in e)
            if t not in seen: seen.add(t); uni.append(e)
        four=[e for e in uni if is_kcol(e,4,n) and not is_kcol(e,3,n)]
        cnt=sum(1 for e in four if contains_moser_induced(n,e))
        print(f"n={n}: {len(four)} four-chromatic, {cnt} contain Moser as INDUCED subgraph")

if __name__=="__main__":
    main()

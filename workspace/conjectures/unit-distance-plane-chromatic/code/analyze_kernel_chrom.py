#!/usr/bin/env python3
"""Analyze the sharp-kernel census data for structural regularities.

Loads all known kernel members of C_n (n=8..11), computes their exact chromatic
number with a fresh independent SAT oracle, and reports:
  - per-n counts (total, 3-colourable, 4-colourable, and the no. needing 4
    colours i.e. chromatic number exactly 4),
  - the 4-chromatic members (edge lists),
  - whether the Moser spindle satisfies the kernel conditions (motivation:
    it is 4-chromatic but is NOT a kernel member; we confirm which condition
    excludes it, so the kernel is a sound superset of 5-critical UDGs).

This is analysis of already-computed census data, not a new search.
"""
import glob, sys, json, os
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable

def edge_str_to_list(s):
    # s like "[(0, 1), (1, 2), ...]"
    return [tuple(x) for x in eval(s)]

def chrom(n, edges):
    """exact chromatic number via SAT (complete): smallest k colourable."""
    for k in range(1, 6):
        sat, _ = is_k_colorable(edges, k, n)
        if sat:
            return k
    return None

# ---- load all kernel members grouped by n
members = {}  # n -> list of edge lists
for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
    for line in open(f):
        line = line.strip()
        if line:
            members.setdefault(11, []).append(edge_str_to_list(line))

# the n=8,9,10 members from the witness JSON
wj = json.load(open("/workspace/code/out/census_kernel.captured_witnesses.json"))
for n in ("8", "9", "10"):
    for idx, d in wj[n].items():
        members.setdefault(int(n), []).append([tuple(e) for e in d["edges"]])

print("per-n kernel member counts loaded:", {n: len(v) for n, v in sorted(members.items())})

print("\n=== chromatic-number distribution of kernel members ===")
fourchromatic = {}
for n in sorted(members):
    c3 = c4 = other = 0
    fours = []
    for edges in members[n]:
        k = chrom(n, edges)
        if k == 3: c3 += 1
        elif k == 4: c4 += 1; fours.append(edges)
        else: other += 1
    fourchromatic[n] = fours
    print(f"n={n}: total={len(members[n])}  chi=3:{c3}  chi=4:{c4}  other:{other}")

print("\n4-chromatic kernel members per n:", {n: len(v) for n, v in sorted(fourchromatic.items())})

# ---- Moser spindle kernel-check
# coordinates from CONTEXT.md / explore_spindle
print("\n=== is the Moser spindle a kernel member? (soundness check) ===")
# Moser edges (7 vertices) from explore_spindle.captured.txt
moser_edges = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(2,5),(5,6),(3,4),(3,6),(4,6)]
# indices: O=0,P1=1,P2=2,P1'=3... let's just use the labelled edge list
# from explore: O--P1,O--P2,O--P1',O--P2',P1--P2,P1--Q,P2--Q,Q--Q',P1'--P2',P1'--Q',P2'--Q'
labelled = {
 'O':0,'P1':1,'P2':2,'Q':3,"P1'":4,"P2'":5,"Q'":6}
moser = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n = 7
adjsets = [set() for _ in range(n)]
for a,b in moser:
    adjsets[a].add(b); adjsets[b].add(a)
print("min degree:", min(len(s) for s in adjsets))
# condition (d): neighbourhood max degree
okd = True
for v in range(n):
    nb = sorted(adjsets[v]); pos={u:i for i,u in enumerate(nb)}
    deg=[0]*len(nb)
    for i,x in enumerate(nb):
        for j,y in enumerate(nb):
            if i<j and y in adjsets[x]:
                deg[i]+=1; deg[j]+=1
    if any(d>2 for d in deg):
        okd=False; print(f"  nbd of {v}: max deg {max(deg)} >2")
print("Moser neighbourhood-maxdeg<=2:", okd)
# K4 free?
k4=False
for a in range(n):
    for b in range(a+1,n):
        if b not in adjsets[a]:
            continue  # only ADJACENT pairs can be part of a 4-clique (fixes false 'K4 minus one edge' positive)
        inter = adjsets[a]&adjsets[b]
        if len(inter)>=2:
            for c in inter:
                for d in inter:
                    if c<d and d in adjsets[c]: k4=True
print("Moser contains K4:", k4)
# K2,3
k23=False
for a in range(n):
    for b in range(a+1,n):
        if len(adjsets[a]&adjsets[b])>=3: k23=True
print("Moser is K2,3 (has pair sharing >=3 neighbours):", k23)
print("Moser chromatic number:", chrom(7, moser), "(known chi=4)")

# ---- how many 4-chromatic n=11 members, and their edge counts
print("\n=== edge counts of 4-chromatic n=11 kernel members ===")
for edges in fourchromatic.get(11, []):
    print("  edges=", len(edges), edges)

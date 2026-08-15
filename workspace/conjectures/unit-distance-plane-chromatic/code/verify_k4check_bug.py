#!/usr/bin/env python3
"""Verify the reported K4-check bug.

analyze_kernel_chrom.py has a nested-loop K4 test that iterates over ALL pairs
(a,b) (adjacent or not), groups their common neighbours, and declares a K4 when
two common neighbours c,d are themselves adjacent. For a TRUE K4 the pair a,b
must be ADJACENT (a K4 = a,b,c,d all pairwise adjacent); the diagnostic omits
that check, so it misfires on "K4 minus one edge" (a,b not adjacent, c,d
adjacent, both c,d adjacent to a and b).

census_kernel.check_kernel requires `b in adjsets[a]` before the common-
neighbour test, so it only fires on genuine 4-cliques.

This script runs both checks on the Moser spindle and reports whether the
diagnostic's "Moser contains K4" is a false positive.
"""
from lib.satcolor import is_k_colorable  # noqa: F401  (PATH is set below if needed)

moser = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n = 7

def adjsets_of(edges, n):
    adjsets = [set() for _ in range(n)]
    for a, b in edges:
        adjsets[a].add(b); adjsets[b].add(a)
    return adjsets

adjsets = adjsets_of(moser, n)

# ---- analyze_kernel_chrom.py K4 loop (verbatim logic)
diag_k4 = False
hits = []
for a in range(n):
    for b in range(a + 1, n):
        inter = adjsets[a] & adjsets[b]
        if len(inter) >= 2:
            for c in inter:
                for d in inter:
                    if c < d and d in adjsets[c]:
                        diag_k4 = True
                        hits.append((a, b, c, d))
print("analyze_kernel_chrom.py K4 loop -> Moser contains K4:", diag_k4)
print("  false-positive quadruples (a,b not adjacent):")
for a, b, c, d in hits:
    if b in adjsets[a]:
        continue
    clique = {a, b, c, d}
    edges = sorted(frozenset({x, y}) for x in clique for y in clique if x < y)
    present = [e for e in edges]
    missing = [e for e in edges if frozenset(e) not in {frozenset(p) for p in moser}]
    print(f"    a={a},b={b},c={c},d={d}  a--b adjacent={b in adjsets[a]}  clique-missing-edges={missing}")

# ---- check_moser_k4.py ground truth (independent, brute force over 4-subsets)
import itertools
eset = set(frozenset(e) for e in moser)
true_k4 = [quad for quad in itertools.combinations(range(n), 4)
           if all(frozenset({x, y}) in eset for x, y in itertools.combinations(quad, 2))]
print("TRUE K4 subgraphs in Moser (independent 4-subset check):", true_k4)

# ---- census_kernel.check_kernel (verbatim), which requires adjacency
def check_kernel_copy(n, edges):
    A = adjsets_of(edges, n)
    for v in range(n):
        if len(A[v]) < 4:
            return False, "deg%d" % len(A[v])
    for a in range(n):
        for b in range(a + 1, n):
            if b not in A[a]:
                continue
            inter = A[a] & A[b]
            if len(inter) < 2:
                continue
            for c in inter:
                for d in inter:
                    if c < d and d in A[c]:
                        return False, "K4"
    for a in range(n):
        for b in range(a + 1, n):
            if len(A[a] & A[b]) >= 3:
                return False, "K23"
    for v in range(n):
        nb = sorted(A[v]); pos = {u: i for i, u in enumerate(nb)}
        deg = [0] * len(nb)
        for i, x in enumerate(nb):
            for j, y in enumerate(nb):
                if i < j and y in A[x]:
                    deg[i] += 1; deg[j] += 1
        if any(d > 2 for d in deg):
            return False, "nbhddeg"
    return True, "member"

# exclusions: does census check_kernel flag a K4 on the Moser?
# (it will fail min-deg >= 4 first — that is the real reason Moser is not a
#  kernel member — but we specifically want to know whether its K4 logic fires.)
print("census_kernel.check_kernel on Moser:", check_kernel_copy(n, moser))

# Isolate: does census's K4 sub-branch ever fire on the Moser?
A = adjsets
k4_fired = False
for a in range(n):
    for b in range(a + 1, n):
        if b not in A[a]:
            continue
        inter = A[a] & A[b]
        if len(inter) < 2:
            continue
        for c in inter:
            for d in inter:
                if c < d and d in A[c]:
                    k4_fired = True
print("census_kernel K4 branch fires on Moser:", k4_fired)

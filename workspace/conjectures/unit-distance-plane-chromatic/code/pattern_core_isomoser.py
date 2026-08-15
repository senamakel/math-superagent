#!/usr/bin/env python3
"""Test the structural conjecture: are the 7-vertex, 11-edge critical cores of
the n=11 four-chromatic kernel members the Moser spindle?

Builds the calibrated Moser spindle edges from unitfield, and checks graph
isomorphism by brute permutation over the 7 vertices. Then, loading the n=11
kernel members (residue slices), extracts each member's 4-critical core and,
when it has 7 vertices / 11 edges, tests isomorphism to the Moser.
"""
import sys, glob, json, itertools
sys.path.insert(0, "/workspace/code")
from lib import unitfield as uf
from lib.satcolor import is_k_colorable


def moser_edges():
    pts = uf.moser_spindle_points()
    edges, _ = uf.unit_graph(pts)
    return set(frozenset(e) for e in edges)


def is_isomorphic_moser(n, edges, moser):
    # only 7-vertex graphs
    if n != 7 or len(edges) != len(moser):
        return None  # not comparable
    eset = [frozenset(e) for e in edges]
    moser_list = [m for m in moser]
    for perm in itertools.permutations(range(7)):
        # map Moser vertices to graph vertices via perm
        ok = True
        ms = set()
        for e in moser_list:
            a, b = tuple(e)
            ms.add(frozenset({perm[a], perm[b]}))
        if ms == set(eset):
            return True
    return False


def edge_str_to_list(s):
    return [tuple(x) for x in eval(s)]


def minimal_4critical(edges, n):
    e = list(edges)
    changed = True
    while changed:
        changed = False
        for i in range(len(e)):
            cand = e[:i] + e[i+1:]
            if not is_k_colorable(cand, 3, n)[0]:
                e = cand
                changed = True
                break
    return e


def main():
    moser = moser_edges()
    # sanity: verify moser is 7-vertex 11-edge, chi=4 not 3
    n_m = 7
    ok3 = is_k_colorable([tuple(e) for e in moser], 3, n_m)[0]
    ok4 = is_k_colorable([tuple(e) for e in moser], 4, n_m)[0]
    print(f"Moser: {len(moser)} edges, 3col={ok3}, 4col={ok4}")

    # Load n=11 members from the residue files
    members = []
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip():
                members.append(edge_str_to_list(line))
    # dedupe
    seen = set()
    uni = []
    for e in members:
        t = frozenset(frozenset(x) for x in e)
        if t not in seen:
            seen.add(t)
            uni.append(e)
    members = uni
    n = 11
    four = [e for e in members
            if is_k_colorable(e, 4, n)[0] and not is_k_colorable(e, 3, n)[0]]
    print(f"n=11 four-chromatic members: {len(four)}")

    n7exact = 0          # members whose core is exactly 7 vertices
    n7_isomoser = 0
    n7_not = 0
    for edges in four:
        core = minimal_4critical(edges, n)
        act = set()
        for a, b in core:
            act.add(a); act.add(b)
        if len(act) == 7 and len(core) == 11:
            n7exact += 1
            relabel = {v: i for i, v in enumerate(sorted(act))}
            core_r = [(relabel[a], relabel[b]) for a, b in core]
            res = is_isomorphic_moser(7, core_r, moser)
            if res:
                n7_isomoser += 1
            elif res is False:
                n7_not += 1
    print(f"members with 7-vertex/11-edge min-4-critical core: {n7exact}")
    print(f"  of which isomorphic to Moser: {n7_isomoser}")
    print(f"  of which NOT Moser: {n7_not}")


if __name__ == "__main__":
    main()

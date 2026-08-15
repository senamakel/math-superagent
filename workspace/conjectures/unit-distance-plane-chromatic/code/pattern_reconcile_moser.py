#!/usr/bin/env python3
"""Reconcile: analyze_cores_small reported containMoser=0 for all n=11
4-chromatic members, but pattern_core_isomoser found 67 members whose
min-4-critical core is isomorphic to Moser. If those members literally contain
the Moser as an induced subgraph of some 7-subset, then containMoser=0 was a
bug (fixed-order subset scan). Verify by proper isomorphism-embedding on a
sample of those 67.
"""
import sys, glob, itertools
sys.path.insert(0, "/workspace/code")
from lib import unitfield as uf
from lib.satcolor import is_k_colorable


def moser_edges():
    pts = uf.moser_spindle_points()
    edges, _ = uf.unit_graph(pts)
    return set(frozenset(e) for e in edges)


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


def contains_moser_embedding(n, edges, moser):
    """True if some 7-subset of the n vertices induces exactly Moser."""
    eset = set(frozenset(e) for e in edges)
    moser_list = list(moser)
    for subset in itertools.combinations(range(n), 7):
        # try all permutations of the subset to see if any matches moser
        for perm in itertools.permutations(subset):
            ms = set()
            for e in moser_list:
                a, b = tuple(e)
                ms.add(frozenset({perm[a], perm[b]}))
            if ms == eset and all(frozenset(e) in eset for e in ms):
                # also require the induced subgraph to have ONLY these edges
                # i.e. all 21 pairs among subset: those at Frozenset in ms are adj
                induced_ok = True
                for a, b in itertools.combinations(subset, 2):
                    if frozenset({a, b}) in eset and frozenset({a, b}) not in ms:
                        induced_ok = False
                        break
                    if frozenset({a, b}) not in eset and frozenset({a, b}) in ms:
                        induced_ok = False
                        break
                if induced_ok:
                    return True
    return False


def main():
    moser = moser_edges()
    members = []
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip():
                members.append(edge_str_to_list(line))
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

    moser_iso_members = []
    for edges in four:
        core = minimal_4critical(edges, n)
        act = set()
        for a, b in core:
            act.add(a); act.add(b)
        if len(act) == 7 and len(core) == 11:
            moser_iso_members.append(edges)

    print(f"members with 7v/11e Moser-isomorphic core: {len(moser_iso_members)}")
    sample = moser_iso_members[:5]
    for edges in sample:
        res = contains_moser_embedding(n, edges, moser)
        print("contains Moser as induced subgraph:", res)
    # also check a few members WITHOUT the Moser core to be safe
    non = [e for e in four if e not in moser_iso_members][:5]
    for edges in non:
        res = contains_moser_embedding(n, edges, moser)
        print("non-moser-core member contains Moser:", res)


if __name__ == "__main__":
    main()

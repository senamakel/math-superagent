#!/usr/bin/env python3
"""Distinguish two claims about the Moser in n=11 members:
 (A) Moser present as an (induced) 7-subset -- analyze_cores_small said NO.
 (B) Moser present as a subgraph (7 vertices carrying the 11 Moser edges,
     possibly with extra edges among them or to other vertices).
Use permutation-correct subgraph containment on the 67 Moser-cored members.
"""
import sys, glob, itertools
sys.path.insert(0, "/workspace/code")
from lib import unitfield as uf
from lib.satcolor import is_k_colorable


def moser_edges():
    pts = uf.moser_spindle_points()
    edges, _ = uf.unit_graph(pts)
    return set(frozenset(e) for e in edges), len(edges)


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


def contains_moser_subgraph(n, edges, moser, m):
    """True if the Moser (7v/11e) is a subgraph: some 7-subset and a relabel
    such that all 11 Moser edges are present (extra edges allowed)."""
    eset = set(frozenset(e) for e in edges)
    moser_list = sorted(moser, key=lambda e: tuple(sorted(e)))
    for subset in itertools.combinations(range(n), 7):
        for perm in itertools.permutations(subset):
            ok = True
            for e in moser_list:
                a, b = tuple(e)
                if frozenset({perm[a], perm[b]}) not in eset:
                    ok = False
                    break
            if ok:
                return True
    return False


def main():
    moser, m = moser_edges()
    members = []
    for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
        for line in open(f):
            if line.strip():
                members.append(edge_str_to_list(line))
    seen = set(); uni = []
    for e in members:
        t = frozenset(frozenset(x) for x in e)
        if t not in seen:
            seen.add(t); uni.append(e)
    members = uni
    n = 11
    four = [e for e in members
            if is_k_colorable(e, 4, n)[0] and not is_k_colorable(e, 3, n)[0]]
    moser_cored = []
    for edges in four:
        core = minimal_4critical(edges, n)
        act = set()
        for a, b in core:
            act.add(a); act.add(b)
        if len(act) == 7 and len(core) == 11:
            # confirm core is actually Moser isomorphic
            moser_cored.append(edges)
    print(f"n=11 four-chrom members: {len(four)}, Moser-cored(7v/11e): {len(moser_cored)}")

    # sample
    samp = moser_cored[:8]
    ok_sub = 0; ok_ind = 0
    for edges in samp:
        if contains_moser_subgraph(n, edges, moser, m):
            ok_sub += 1
    print(f"of {len(samp)} sampled Moser-cored members, {ok_sub} contain Moser as subgraph (permutation-correct)")


if __name__ == "__main__":
    main()

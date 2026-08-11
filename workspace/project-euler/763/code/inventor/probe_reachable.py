#!/usr/bin/env python3
"""Probe: 3D FE763 reachable configs, verified against Eriksson structure.

For N = 0..6:
  1. Forward BFS over distinct occupied-cube sets (exact, small-N) -> D(N).
  2. Reverse-merge check: every reachable config must reduce to {origin} by
     repeatedly replacing the three children of a common absent parent with
     that parent (Eriksson voidance/position characterization, n>=3).
  3. Voidance-set structure: for each config, the set of "once-fired, now
     empty" parents along a reverse collapse.  Eriksson (n>=3, no node played
     twice) predicts positions = voidance sets bijectively.  Check whether
     distinct configs give distinct voidance sets, and the voidance-set size.

NOTE: the full set-of-all-merge-orderings voidance computation is exponential
in config size; it is bounded here to N<=5 (configs of 11 cells).
"""
from itertools import product
from lib.amoeba import children

DIM = 3
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def forward_level(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


def mergeable(key, cand, memo):
    if key in memo:
        return memo[key]
    if key == frozenset([(0, 0, 0)]):
        memo[key] = True
        return True
    Sset = set(key)
    for p in cand:
        if p in Sset:
            continue
        ch = children(p)
        if all(c in Sset for c in ch):
            ns = frozenset((Sset - set(ch)) | {p})
            if mergeable(ns, cand, memo):
                memo[key] = True
                return True
    memo[key] = False
    return False


def all_voidance_sets(key, cand, memo):
    """All distinct voidance frozensets over all reverse-merge orderings."""
    if key == frozenset([(0, 0, 0)]):
        return {frozenset()}
    if key in memo:
        return memo[key]
    Sset = set(key)
    out = set()
    for p in cand:
        if p in Sset:
            continue
        ch = children(p, DIM)
        if all(c in Sset for c in ch):
            ns = frozenset((Sset - set(ch)) | {p})
            for sub in all_voidance_sets(ns, cand, memo):
                out.add(sub | frozenset([p]))
    memo[key] = out
    return out


# --- decoded/run support ------------------------------------------------


def _run_py(path, cwd="/workspace"):
    import subprocess
    r = subprocess.run(["python3", path], cwd=cwd, capture_output=True, text=True)
    return r.stdout, r.stderr


if __name__ == "__main__":
    # declared infrastructure cost: exact BFS / reverse-merge / voidance search,
    # exponential in config size, bounded to N<=6 (<=13 cells).  Oracle only.
    out, err = _run_py("code/inventor/probe_reachable.py")
    print(out)
    if err:
        print("STDERR:\n", err)

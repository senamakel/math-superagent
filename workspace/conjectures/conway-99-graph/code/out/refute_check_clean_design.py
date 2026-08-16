#!/usr/bin/env python3
"""Independent referee check: is coclique_lift_clean_design.txt a genuine
super-simple 2-(22,4,2) design?

Super-simple 2-(22,4,2): 77 blocks (4-subsets of {0..21}), every point in
exactly 14 blocks (r=14), every pair in exactly 2 blocks (lambda=2), and NO
two blocks share a triple (equivalently at most one block contains any given
triple; equivalently no two blocks meet in >= 3 points).

This is a self-contained exact checker over Z, reading the file directly and
NOT trusting any prior capture.  It deliberately also checks the two critical
mu=2 lift conditions and compares with the Q1 design.
"""
import itertools
from collections import Counter

def read_blocks(path):
    blocks = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            b = tuple(sorted(map(int, line.split())))
            assert len(b) == 4 and min(b) >= 0 and max(b) <= 21
            blocks.append(b)
    return blocks

def verify(path, label):
    print(f"=== {label} : {path} ===")
    blocks = read_blocks(path)
    V, K, R, LAM = 22, 4, 14, 2
    n = len(blocks)
    print(f"  block count = {n} (want 77)")
    # repeated blocks
    bset = set(blocks)
    print(f"  distinct blocks = {len(bset)} (repeated = {n - len(bset)})")
    deg = Counter()
    pairs = Counter()
    trips = Counter()
    for B in blocks:
        for a in B:
            deg[a] += 1
        for p in itertools.combinations(B, 2):
            pairs[p] += 1
        for t in itertools.combinations(B, 3):
            trips[t] += 1
    print(f"  replication set = {sorted(set(deg.values()))} (want [14]); "
          f"all {V} points? {len(deg)==V}")
    print(f"  pair-cover: pairs hit = {len(pairs)} (want {V*(V-1)//2}); "
          f"overlap values = {sorted(set(pairs.values()))} (want [2])")
    print(f"  triple-overlap histogram: {dict(sorted(trips.items(), key=lambda kv:-kv[1])[:1])}")
    tmax = max(trips.values()) if trips else 0
    thist = Counter(trips.values())
    print(f"  max triple overlap = {tmax} (want 1 for super-simple)")
    print(f"  triple histogram = {dict(sorted(thist.items()))}")
    bp3 = sum(trips[t]*(trips[t]-1)//2 for t in trips)   # block-pairs sharing a triple
    print(f"  unordered block-pairs sharing >= 3 vertices = {bp3}")
    # full verification flags
    ok_design = (n == 77 and len(bset) == 77 and len(deg) == V
                 and set(deg.values()) == {R} and len(pairs) == V*(V-1)//2
                 and set(pairs.values()) == {LAM})
    ok_supersimple = ok_design and tmax == 1
    print(f"  => 2-(22,4,2): {ok_design}")
    print(f"  => SUPER-SIMPLE (Q2 clean): {ok_supersimple}")
    return ok_supersimple, ok_design, tmax, bp3

if __name__ == "__main__":
    a = verify("code/out/coclique_lift_clean_design.txt", "clean")
    print()
    b = verify("code/out/coclique_lift_design.txt", "Q1")
    print()
    same = read_blocks("code/out/coclique_lift_clean_design.txt") == \
           read_blocks("code/out/coclique_lift_design.txt")
    print(f"clean file == Q1 file byte-for-byte (block lists identical): {same}")

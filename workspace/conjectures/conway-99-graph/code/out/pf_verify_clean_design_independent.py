#!/usr/bin/env python3
"""Independent verification of coclique_lift_clean_design.txt as a
super-simple 2-(22,4,2) design, by direct counting (second route, no CP-SAT).

Super-simple 2-(22,4,2): 77 blocks = 4-subsets of {0..21};
  every point in exactly r=14 blocks; every pair in exactly lambda=2 blocks;
  NO triple lies in two blocks (no two blocks meet in 3 points) <=> the 308
  covered triples are pairwise distinct.
Exact integer histograms only."""
import itertools
from collections import Counter

blocks = []
with open("/workspace/code/out/coclique_lift_clean_design.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            blocks.append(tuple(sorted(map(int, line.split()))))

V, K, R, LAM = 22, 4, 14, 2
print(f"blocks read: {len(blocks)}")
assert all(len(set(b)) == K and min(b) >= 0 and max(b) < V for b in blocks)
assert len(set(blocks)) == len(blocks), "duplicate blocks"

# point replication
deg = Counter(p for b in blocks for p in b)
# pair coverage
pairs = Counter(tuple(sorted(pp)) for b in blocks for pp in itertools.combinations(b, 2))
# triple coverage
trips = Counter(tuple(sorted(tt)) for b in blocks for tt in itertools.combinations(b, 3))

n_blocks = len(blocks)
ok_design = (n_blocks == 77
             and set(deg.values()) == {R} and len(deg) == V
             and len(pairs) == V*(V-1)//2 and set(pairs.values()) == {LAM})
# super-simple: every triple in at most one block  <=> distinct covered triples
ok_super = set(trips.values()) == {1} and len(trips) == n_blocks * 4  # 77*4=308
print(f"point replication  : {sorted(set(deg.values()))} (want 14); {len(deg)} points (want 22): {set(deg.values())=={R}}")
print(f"pair coverage      : {sorted(set(pairs.values()))} (want 2); {len(pairs)}/{V*(V-1)//2} pairs covered: {set(pairs.values())=={LAM}}")
print(f"triple run-count   : {sorted(set(trips.values()))}  ({len(trips)} distinct triples, want {n_blocks*4}=308 all distinct)")
print(f"==> 2-(22,4,2) design: {ok_design}")
print(f"==> SUPER-SIMPLE (no block-pair sharing triple): {ok_super}")
print(f"VERDICT: super-simple 2-(22,4,2) EXISTS <=> {ok_design and ok_super}")

#!/usr/bin/env python3
"""Check the captured Q1 2-(22,4,2) design against the mu=2 lift obstructions.

Reads code/out/coclique_lift_design.txt (77 blocks from the Q1 solve).
Lift conditions for a tight-22 coclique at (99,14,1,2):
  (a) no repeated block (already impossible by construction here, but check);
  (b) no triple of points lies in two different blocks  <=> no two blocks share
      >=3 vertices.  If any triple is in 2 blocks, two outside vertices would
      share >=3 common neighbours, violating mu=2.
Reports the worst triple-overlap; also the worst pair-overlap and the number of
block-pairs sharing exactly 3 vertices (the direct mu=2 violation count).
"""
import itertools
from collections import Counter

blocks = []
with open("coclique_lift_design.txt") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        blocks.append(tuple(sorted(map(int, line.split()))))

print("blocks:", len(blocks))
bset = set(blocks)
print("distinct:", len(bset), "repeated blocks:", len(blocks) - len(bset))

# pair-overlap and triple-overlap
pair_count = Counter()
triple_count = Counter()
for B in blocks:
    for p in itertools.combinations(B, 2):
        pair_count[p] += 1
    for t in itertools.combinations(B, 3):
        triple_count[t] += 1

from collections import defaultdict
pair_hist = defaultdict(int)
for p, c in pair_count.items():
    pair_hist[c] += 1
print("pair-overlap histogram (over the C(22,2)=231 pairs):")
for c in sorted(pair_hist):
    print(f"   overlap={c}: {pair_hist[c]} pairs")

triple_hist = defaultdict(int)
for t, c in triple_count.items():
    triple_hist[c] += 1
print("triple-overlap histogram (over the C(22,3)=1540 triples):")
for c in sorted(triple_hist):
    print(f"   overlap={c}: {triple_hist[c]} triples")
print("pairs of blocks sharing exactly 3 vertices "
      "(direct mu=2 violation count):",
      sum(v for k,v in triple_hist.items() if k>=2) if 2 in triple_hist else 0)
# number of unordered block-pairs sharing exactly 3 vertices:
# each triple in c blocks contributes C(c,2) block-pairs
bp3 = sum(triple_count[t]*(triple_count[t]-1)//2 for t in triple_count)
print("number of unordered block-pairs sharing exactly 3 vertices =", bp3)

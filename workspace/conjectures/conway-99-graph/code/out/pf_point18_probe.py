"""Structural probe of point 18 in the Q1 2-(22,4,2) design — it appears in
4 of the 6 bad (triple-in-2-blocks) configurations. Is 18 the concentrated
obstruction to super-simplicity, and is there pairing structure a repair could
use?"""
from collections import Counter

blocks = []
with open('code/out/coclique_lift_design.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('A '):
            continue
        parts = line.split()
        if len(parts) == 4 and all(p.isdigit() for p in parts):
            blocks.append(tuple(sorted(int(p) for p in parts)))
assert len(blocks) == 77

# all blocks containing point 18
b18 = [b for b in blocks if 18 in b]
print("blocks containing point 18 (", len(b18), "):")
for b in sorted(b18):
    print("   ", b)

# among those, which pairs share 3 points
print("\nAmong point-18 blocks, block-pairs sharing exactly 3 vertices:")
cnt = 0
for i in range(len(b18)):
    for j in range(i+1, len(b18)):
        if len(set(b18[i]) & set(b18[j])) == 3:
            cnt += 1
            shared = set(b18[i]) & set(b18[j]) - {18}
            print(f"   {b18[i]} & {b18[j]}  (additionally share {sorted(shared)})")
print("total pair-wise triple-shares among 18-blocks:", cnt)

# each point's 18-adjacency: which pair of the other 3 points go with it
print("\nPoint 18's role: for each 18-block, the 3 other points:", )
triples_with_18 = sorted(tuple(sorted(set(b)-{18})) for b in b18)
for t in triples_with_18:
    print("   ", t)

# how many of these (point18, x, y) triples are 'bad' (in 2 blocks)?
bad_with_18 = [ (2,4,18),(3,18,21),(10,15,18),(14,18,20) ]
print("\nbad triples containing 18:", len(bad_with_18), "of which point-18-other-triples:", )
for t in sorted(tuple(sorted(set(x)-{18})) for x in bad_with_18):
    print("   ", t)

# elsewhere: how bad is the rest of the design? remove 18, recount bad triples
rest_bad = [(2,4,18),(3,18,21),(6,17,20),(8,12,16),(10,15,18),(14,18,20)]
rest_bad_n18 = [t for t in rest_bad if 18 not in t]
print("\nbad triples NOT involving 18:", rest_bad_n18, "count:", len(rest_bad_n18))

"""Analyze the structure of the explicit 2-(22,4,2) design found by the
coclique-lift MILP (code/out/coclique_lift_design.txt).

Purpose: extract exact structural facts about this design so the super-simple
Q2 question (no two blocks sharing 3 points) can be studied, and to expose
any integer-sequence regularity in the block-intersection structure.

Everything exact integer arithmetic.
"""
from collections import Counter, defaultdict

blocks = []
with open('code/out/coclique_lift_design.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('A '):
            continue
        parts = line.split()
        if len(parts) == 4 and all(p.isdigit() for p in parts):
            blocks.append(tuple(sorted(int(p) for p in parts)))

assert len(blocks) == 77, len(blocks)
assert len(set(blocks)) == 77  # distinct

# 1) verify 2-(22,4,2): every point in 14 blocks, every pair in exactly 2 blocks
from collections import defaultdict
point_count = Counter()
pair_count = Counter()
for b in blocks:
    for p in b:
        point_count[p] += 1
    for i in range(4):
        for j in range(i+1,4):
            pair_count[tuple(sorted((b[i],b[j])))] += 1
assert set(point_count.values()) == {14}, point_count
assert set(pair_count.values()) == {2}, set(pair_count.values())
assert len(pair_count) == 22*21//2
print("valid 2-(22,4,2): every point in 14 blocks, every pair in exactly 2 blocks")

# 2) triple-occurrence structure (each block contains C(4,3)=4 triples; 77*4=308)
triple_count = Counter()
for b in blocks:
    for i in range(4):
        for j in range(i+1,4):
            for k_ in range(j+1,4):
                triple_count[tuple(sorted((b[i],b[j],b[k_])))] += 1
hist = Counter(triple_count.values())
print("triple-occurrence histogram (count -> #triples):", dict(sorted(hist.items())))
print("  total triple-occurrences:", sum(triple_count.values()), "= 77*4 =", 77*4)
print("  triples in >=2 blocks (mu=2 violations):", sum(c for t,c in triple_count.items() if c>=2))
for t,c in sorted(triple_count.items()):
    if c >= 2:
        print("    triple", t, "in", c, "blocks")

# 3) the 6 bad block-pairs (share 3 vertices)
block_pairs_share3 = []
for i in range(77):
    for j in range(i+1,77):
        inter = len(set(blocks[i]) & set(blocks[j]))
        if inter == 3:
            block_pairs_share3.append((i,j,blocks[i],blocks[j]))
print("block-pairs sharing exactly 3 vertices:", len(block_pairs_share3))
for (i,j,bi,bj) in block_pairs_share3:
    shared = set(bi) & set(bj)
    only_i = set(bi) - shared
    only_j = set(bj) - shared
    print(f"  pair {i}-{j}: shared={sorted(shared)}  i-only={sorted(only_i)} j-only={sorted(only_j)}")

# 4) degree of each point in the "bad" structure: how many bad pairs touch each point
bad_points = Counter()
for (i,j,bi,bj) in block_pairs_share3:
    shared = set(bi) & set(bj)
    for p in shared:
        bad_points[p] += 1
print("points involved in bad triples (point -> #bad triples):", dict(sorted(bad_points.items())))

# 5) block-intersection histogram overall (how many block-pairs share 0,1,2,3 points)
overlap_hist = Counter()
overlap_2pairs = Counter()
for i in range(77):
    for j in range(i+1,77):
        o = len(set(blocks[i]) & set(blocks[j]))
        overlap_hist[o] += 1
print("block-pair overlap histogram (intersection -> #pairs):", dict(sorted(overlap_hist.items())))
print("  total block-pairs:", 77*76//2, "  sum check:", sum(overlap_hist.values()))

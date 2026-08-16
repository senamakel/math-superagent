"""Deep structural probe of the explicit 2-(22,4,2) design's super-simple defect.

The design is valid 2-(22,4,2) with exactly 6 block-pairs sharing 3 vertices
(= 6 triples each appearing in 2 blocks = the mu=2 violations).  A super-simple
completion (Q2) needs zero such triples.  Probe:
  1. Which points are over-represented (point 18 in 4 of 6).
  2. Does the defect have usable symmetry / pairing structure that a local
     repair could exploit, or is it an obstruction?
  3. Independent re-derivation of design validity by a second route.
"""
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

# the 6 bad triples (each in 2 blocks)
bad_triples = [
    (2,4,18),(3,18,21),(6,17,20),(8,12,16),(10,15,18),(14,18,20),
]

# For each bad triple, the two blocks containing it
for t in bad_triples:
    Ts = set(t)
    owners = [b for b in blocks if Ts <= set(b)]
    print(f"triple {t}: in {len(owners)} blocks -> {owners}")

# Complementary: what would happen if we tried to move the 'i-only' point?
# For each bad pair {b1,b2} sharing triple t, the two blocks differ by one
# vertex each.  The 'extra' vertices:
print()
# re-find pairs sharing 3
pair_info = []
for i in range(77):
    for j in range(i+1,77):
        inter = set(blocks[i]) & set(blocks[j])
        if len(inter) == 3:
            shared = tuple(sorted(inter))
            pair_info.append((i,j,shared, blocks[i], blocks[j]))
for (i,j,shared,bi,bj) in pair_info:
    si = set(bi)-set(shared); sj = set(bj)-set(shared)
    print(f"blocks {i}({sorted(si)}) and {j}({sorted(sj)}) share {shared}")

# point-frequency of 'bad-triple membership'
pt = Counter()
for t in bad_triples:
    for p in t: pt[p]+=1
print("\nbad-triple point frequencies:", dict(sorted(pt.items())))

# Is there an automorphism of the design?  Just record orbit structure cheaply:
# none attempted (graph automorphism of 77-block 4-uniform hypergraph is heavy).
# Instead: check whether the 6 bad triples' 12 blocks could form a resolvable
#   sub-structure; count how many OTHER blocks each bad triple's points hit.
print("\n-- interaction of bad-triple points --")
allpts = set(range(22))
for t in bad_triples:
    Ts=set(t)
    # blocks containing at least 2 points of t (beyond the 2 owners)
    cont = [b for b in blocks if len(set(b)&Ts)>=2]
    print(f"triple {t}: {len(cont)} blocks contain >=2 of its points")

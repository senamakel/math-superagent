"""Check whether the 6 bad triples of the Q1 design are 'isolated' (no third
block contains 2 of their points) — the structure that determines whether the
super-simple defect is a sparse per-pair phenomenon or a densely-coupled
obstruction.  Then test one local-repair hypothesis: can each bad pair be
resolved by a swap without breaking design validity?  (Full search is the
sat_solver's job; here we only measure the local coupling.)"""
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

tc = Counter()
for b in blocks:
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                tc[tuple(sorted((b[i],b[j],b[k])))] += 1
bad = [t for t,v in tc.items() if v>=2]
print("bad triples:", bad)

# isolation: for each bad triple, how many blocks contain >=2 of its points
print("\n-- isolation of each bad triple --")
for t in bad:
    Ts = set(t)
    cont = [b for b in blocks if len(set(b)&Ts) >= 2]
    print(f"  triple {t}: {len(cont)} blocks contain >=2 pts (expect 2 = its owners)")
    if len(cont) > 2:
        extra = [b for b in cont if set(b)!=Ts]
        print("     extra blocks:", extra)

# Now the keystone question: are the 6 bad pairs pairwise disjoint in their
# 'extra' vertices, and do they form a matching on the bad-triple points?
# For each bad triple, the two owner blocks differ by one vertex each.
pair_extra = []
for t in bad:
    Ts = set(t)
    owners = [b for b in blocks if Ts <= set(b)]
    assert len(owners) == 2
    e1 = set(owners[0]) - Ts
    e2 = set(owners[1]) - Ts
    pair_extra.append((t, sorted(e1), sorted(e2)))
print("\n-- owner-pair extra vertices (the movable points) --")
for t, e1, e2 in pair_extra:
    print(f"  triple {t}: block extra {e1} vs {e2}")

# Union of all 'extra' vertices across the 6 bad pairs — is there collision?
from collections import Counter
extra_union = Counter()
for t,e1,e2 in pair_extra:
    for x in e1+e2: extra_union[x]+=1
print("\nextra-vertex frequencies across all 6 bad pairs:", dict(sorted(extra_union.items())))
collisions = {p:c for p,c in extra_union.items() if c>1}
print("extra vertices appearing in >1 bad pair (coupling):", collisions or "NONE (defect is a clean matching)")

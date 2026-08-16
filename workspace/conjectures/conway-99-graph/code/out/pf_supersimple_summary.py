"""Final structural summary of the Q1 2-(22,4,2) design and its super-simple
defect, for the pattern-finder report.  Exact counts only."""
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

# point degrees and pair coverage (re-derivation, second route)
from collections import defaultdict
pc = Counter(); pairc = Counter()
for b in blocks:
    for p in b: pc[p]+=1
    for i in range(4):
        for j in range(i+1,4):
            pairc[tuple(sorted((b[i],b[j])))] += 1
assert set(pc.values())=={14} and len(pc)==22
assert set(pairc.values())=={2} and len(pairc)==231
print("RE-DERIVED: valid 2-(22,4,2) by second route (point deg {14}, every pair {2})")

# bad triples: triples in >=2 blocks
tc = Counter()
for b in blocks:
    for i in range(4):
        for j in range(i+1,4):
            for k in range(j+1,4):
                tc[tuple(sorted((b[i],b[j],b[k])))] += 1
nbad = sum(1 for v in tc.values() if v>=2)
print("triples in >=2 blocks (=mu=2 violations):", nbad)
print("triple-occurrence histogram:", dict(sorted(Counter(tc.values()).items())))

# overlap histogram
oh = Counter()
for i in range(77):
    for j in range(i+1,77):
        oh[len(set(blocks[i])&set(blocks[j]))]+=1
print("block-pair overlap histogram:", dict(sorted(oh.items())))

# max point concentration in bad triples
from collections import defaultdict
badpts = Counter()
for t,v in tc.items():
    if v>=2:
        for p in t: badpts[p]+=1
print("bad-triple point concentration:", dict(sorted(badpts.items())))

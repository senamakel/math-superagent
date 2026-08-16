#!/usr/bin/env python3
"""Fresh probe: is there any modulus M (beyond 9) that gives a necessary
residue restriction on S-roots which is NOT already implied by mod 9?
Checks the merged residue-set against the mod-9 {0,1} filter over all roots."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m: roots.append(int(m.group(2)))
    return roots
R = [r for r in load_roots(B_FILE) if r >= 2]  # drop sentinels 0,1
print("roots used (>=2):", len(R), "max", max(R))

for M in [3, 7, 9, 11, 13, 17, 19, 27, 37, 99, 1001]:
    residues = sorted({r % M for r in R})
    frac = len(residues) / M
    print(f"M={M:4d}: {len(residues):3d}/{M} residues occur  ({frac:.2%} full)  set={residues}")

# The mod-9 filter predicted subset: possible residues {0,1}. For a merged
# filter to be stronger than mod-9, some residue r in {0,1} mod 9 must be
# empty within a larger modulus -> a necessary condition beyond mod 9.
print("\nCombined filters (residue set that ACTUALLY occurs, vs mod-9 {0,1}):")
for M in [11, 13, 27, 37, 99]:
    # set of m mod M that occur; reduce: does knowing m mod M cut the mod-9-valid roots?
    mod9_valid = [r for r in R if r % 9 in (0, 1)]
    # how much does adding mod-M residue prune mod9_valid?
    residues = sorted({r % M for r in R})
    # fraction of (0..M-1) residues that overlap mod9-valid residues
    print(f"M={M:4d}: {len(residues)}/{M} residues occur")

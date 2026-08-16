#!/usr/bin/env python3
"""Analyze structure of the 408 S-number roots <= 10^6."""
import re, math, collections

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

roots = load_roots(B_FILE)
R = [r for r in roots if r <= 10**6]   # exactly the 408 roots for T(10^12)
print("roots <= 10^6:", len(R))

# mod-9 residues
c0 = sum(1 for r in R if r % 9 == 0)
c1 = sum(1 for r in R if r % 9 == 1)
c_other = len(R) - c0 - c1
print(f"mod9 residues: 0->{c0}, 1->{c1}, other->{c_other}")

# count by number of digits of the root
byd = collections.Counter(len(str(r)) for r in R)
print("roots by digit-count of m:", dict(sorted(byd.items())))

# counts by number of digits of the VALUE m^2
byvd = collections.Counter(len(str(r*r)) for r in R)
print("roots by digit-count of m^2:", dict(sorted(byvd.items())))

# Self-similar chains: repunit 9s and powers of 10
for p in range(1, 7):
    nine = 10**p - 1
    ten = 10**p
    print(f"9-repunit 10^{p}-1={nine}: {nine in R}, 10^{p}={ten}: {ten in R}")

# show all roots in (0, 1000) to spot family structure
small = [r for r in R if r < 2000]
print("roots < 2000:", small)

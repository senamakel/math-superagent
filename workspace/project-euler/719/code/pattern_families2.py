#!/usr/bin/env python3
"""Verify Kaprekar(2-block) membership of the 45/55 families and other structure."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots
R = load_roots(B_FILE)
S = set(R)
R6 = [r for r in R if r <= 10**6]
S6 = set(R6)
maxr = max(R)

def is_kaprekar(m):
    s = str(m*m)
    # two-block split: some cut where left+right == m, but "leading zeros allowed"
    for cut in range(1, len(s)):
        a = int(s[:cut]); b = int(s[cut:])
        if a + b == m:
            return True
    return False

print("== 45-family (Kaprekar 2-block, then S-root) ==")
famC = [5*(10**k)*(10**(k+1)-1) for k in range(4)]
for v in famC:
    inrange = v <= maxr
    print(f"  {v}: in-range={inrange} kaprekar={is_kaprekar(v) if True else '?'} S-root={v in S}")

print("== 55-family ==")
famD = [5*(10**(2*k+1)+10**k) for k in range(4)]
for v in famD:
    inrange = v <= maxr
    print(f"  {v}: in-range={inrange} kaprekar={is_kaprekar(v)} S-root={v in S}")

print("== 82-family : classic 82^2=6724; try 82, 8200, 820000? ==")
# standard 82-family in A006886: 82, 8200? Actually 8200 not. Check via kaprekar:
for v in [82, 8200, 820000, 82000000]:
    print(f"  {v}: kaprekar={is_kaprekar(v)} S-root={v in S}")

print("\n== mod-9 over ALL 3200 roots ==")
bad = [r for r in R if r % 9 not in (0,1)]
print("  roots with mod9 outside {0,1}:", len(bad))

print("\n== growth of count by root digit-count (<=10^6, 1..6 digits) ==")
import collections
c6 = collections.Counter(len(str(r)) for r in R6)
for d in range(1,7):
    print(f"  {d}-digit roots: {c6[d]}")

# ratio of consecutive digit-count bins
prev=None
for d in range(1,7):
    c=c6[d]
    if prev: print(f"  growth {d-1}->{d}: {c/prev:.3f}")
    prev=c

# check the famously dense family: roots near 999... and 5-family saturation
r999 = [r for r in R6 if str(r).startswith('9')]
print("roots<=10^6 starting with 9:", len(r999), "/", len(R6))
# how many end in 0 (divisible by 10)
c0 = sum(1 for r in R6 if r % 10 == 0)
print("roots<=10^6 divisible by 10:", c0)

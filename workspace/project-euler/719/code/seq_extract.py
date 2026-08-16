#!/usr/bin/env python3
"""Extract integer sequences from the A038206 b-file that the sequence tools
have NOT yet been run on:
  1. A104113 squares m^2 (S-number values themselves)
  2. decade counts c_k = #{roots <= 10^k}, k=1..9   (b-file exact to 10^9)
  3. cumulative sums T(10^k) = sum of m^2 over roots <= 10^k, k=1..9
Also: mod-9 residue split over all 408 roots <= 10^6, and a sortedness check.
"""
import re, json

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
assert roots == sorted(roots), "b-file not sorted by value!"

# roots relevant to T(10^12): 2 <= m <= 10^6 (exclude sentinel roots 0,1)
R = [r for r in roots if 2 <= r <= 10**6]
assert len(R) == 406, len(R)  # 408 b-file lines <= 1e6 minus sentinel roots 0 and 1
assert R[-1] == 1000000
# first root > 10^6 is the 409th line (0-indexed 408): value 1005291
assert roots[408] == 1005291
lines_le = sum(1 for r in roots if r <= 10**6)
assert lines_le == 408, lines_le

out = {}

# --- 1. squares (A104113 S-number values), first 40, excluding m=0,1 ---
sq = [r*r for r in R]
out["squares_first40"] = sq[:40]

# --- 2. decade counts c_k = #{roots <= 10^k}, k=1..9 (b-file exact up to 10^9) ---
# all roots <= 10^9 are present since max(3200-term b-file) = 1028956744 > 10^9
counts = []
for k in range(1, 10):
    cnt = sum(1 for r in roots if r <= 10**k)
    counts.append(cnt)
out["counts_le_10^k_k1..9"] = counts

# counts with the problem's convention m >= 2 (exclude 0 and 1):
counts_ge2 = []
for k in range(1, 10):
    cnt = sum(1 for r in roots if 2 <= r <= 10**k)
    counts_ge2.append(cnt)
out["counts_ge2_le_10^k_k1..9"] = counts_ge2

# --- 3. cumulative sums T(10^k) = sum of squares of roots <= 10^k ---
cs = []
run = 0
idx = 0
for k in range(1, 10):
    while idx < len(roots) and roots[idx] <= 10**k:
        run += roots[idx]**2
        idx += 1
    cs.append(run)
out["cumsum_T(10^k)_k1..9"] = cs

# --- mod-9 residue split over the 408 roots ---
r0 = sum(1 for r in R if r % 9 == 0)
r1 = sum(1 for r in R if r % 9 == 1)
out["mod9_split_408"] = [r0, r1]

print(json.dumps(out, indent=1))
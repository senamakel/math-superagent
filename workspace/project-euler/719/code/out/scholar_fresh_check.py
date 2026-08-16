#!/usr/bin/env python3
"""Fresh independent verification of T(10^12) for PE 719.

Builds its own split predicate (memoized reachability over the digit string of
m^2, requiring >=2 blocks) from scratch — does not import solution.py or
brute.py. Then:
  (1) reproduces the four worked examples,
  (2) reproduces T(10^4)=41333,
  (3) re-derives T(10^12) by scanning roots m in [2,10^6] independently,
  (4) cross-checks the resulting root set against the catalogued roots408.txt.
"""
import math, sys
from functools import lru_cache

def is_S(m):
    """m is an S-root iff some split of str(m*m) into >=2 contiguous blocks
    sums to m. Memoized reachability on the suffix (position, target)."""
    d = str(m * m)
    n = len(d)
    @lru_cache(maxsize=None)
    def reach(pos, target):
        if target < 0:
            return False
        if pos == n:
            return target == 0
        v = 0
        for i in range(pos, n):
            v = v * 10 + int(d[i])
            if v > target:
                break
            if reach(i + 1, target - v):
                return True
        return False
    # require >= 2 blocks: first block ends before the last digit
    v = 0
    for j in range(0, n - 1):
        v = v * 10 + int(d[j])
        if v > m:
            break
        if reach(j + 1, m - v):
            return True
    return False

# 1. worked examples
examples = {81: 9, 6724: 82, 8281: 91, 9801: 99}
for n, r in examples.items():
    ok = is_S(r)
    print(f"n={n} root={r} is_S={ok}")
    assert ok and r * r == n

# 2. T(10^4)
s4 = [r for r in range(2, 100 + 1) if is_S(r)]
t4 = sum(r * r for r in s4)
print("roots <= 100:", s4)
print("T(10^4) =", t4)
assert t4 == 41333, t4

# 3. T(10^12) by independent scan
total = 0
found = []
for m in range(2, 10**6 + 1):
    if is_S(m):
        total += m * m
        found.append(m)
print("T(10^12) =", total, "  (# roots =", len(found), ")")

# 4. cross-check against catalogued roots
with open('/workspace/code/out/roots408.txt') as f:
    catalog = [int(x.strip()) for x in f if x.strip()]
catalog = [m for m in catalog if 2 <= m <= 10**6]
print("catalogued roots =", len(catalog))
print("my roots == catalog:", found == catalog)
missing = sorted(set(catalog) - set(found))
extra = sorted(set(found) - set(catalog))
print("missing from catalog:", missing)
print("extra vs catalog:", extra)

print("FINAL T(10^12) =", total)

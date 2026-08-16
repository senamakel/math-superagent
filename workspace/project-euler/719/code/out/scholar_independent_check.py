#!/usr/bin/env python3
"""Scholar's independent numeric check of T(10^12) for PE 719.

Reads the catalogued S-root list roots408.txt (OEIS A038206 roots <= 10^6)
and sums m^2 over roots m >= 2. This is a route entirely independent of
solution.py's recursion: it only trusts the catalogue plus the root
bijection n = m^2. Also re-derives T(10^4)=41333 from the same list as a
sanity oracle.
"""
import math

with open('/workspace/code/out/roots408.txt') as f:
    roots = [int(line.strip()) for line in f if line.strip()]

# Exclude sentinel roots 0 and 1 (n=1 has only the single-block split).
valid = [m for m in roots if m >= 2 and m <= 10**6]
assert len(valid) == 406, f"expected 406 roots in [2,10^6], got {len(valid)}"

total = sum(m * m for m in valid)
print("number of S-roots in [2,10^6]:", len(valid))
print("largest root:", max(valid))
print("T(10^12) = sum m^2 over catalogued roots =", total)

# Oracle re-check: T(10^4) from the same list.
t4 = sum(m * m for m in valid if m * m <= 10**4)
print("T(10^4) from list =", t4, "(expected 41333)")

# Independent check that the squares themselves are S-numbers via the
# digit-partition predicate (building the predicate freshly, no recursion read).
def is_S_root(m):
    d = str(m * m)
    n = len(d)
    # DFS: is there a split of d into 2+ contiguous blocks summing to m?
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def reach(pos, target):
        # can suffix d[pos:] (must use >=1 block) sum to target using >=1 block
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
    # force >=2 blocks: at least one block boundary before end
    v = 0
    for i in range(1, n):
        v = v * 10 + int(d[i - 1])
        if v > m:
            break
        if reach(i + 1, m - v):
            return True
    return False

catalog_ok = sum(1 for m in valid if is_S_root(m))
print("catalogued roots that pass a fresh split predicate:", catalog_ok, "/", len(valid))
print("oracle examples:", [is_S_root(m) for m in (9, 82, 91, 99)])

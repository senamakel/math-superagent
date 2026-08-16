#!/usr/bin/env python3
"""Extract exact witness splits for F2 members m=10^k-10 (and m+1) using an
efficient memoised split-returning DP, for k small enough to be fast. Goal:
expose a uniform pattern that could be turned into a proof."""
from functools import lru_cache

def split(m):
    """return a list of block-values summing to m covering str(m^2), or None"""
    s = str(m*m); n = len(s)
    @lru_cache(maxsize=None)
    def dp(i, target):
        if target < 0: return None
        if i >= n:
            return [] if target == 0 else None
        val = 0
        for j in range(i, n):
            val = val*10 + int(s[j])
            if target - val < 0: break
            rest = dp(j+1, target-val)
            if rest is not None:
                return [val] + rest
        return None
    val = 0
    for j in range(0, n-1):
        val = val*10 + int(s[j])
        rest = dp(j+1, m-val)
        if rest is not None:
            return [val] + rest
    return None

for k in range(3, 9):
    m = 10**k - 10
    sp = split(m); sp2 = split(m+1)
    print(f"k={k} m={m} (m^2={m*m})")
    print(f"   split m:   {sp}")
    print(f"   split m+1: {sp2}")

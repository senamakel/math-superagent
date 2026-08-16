#!/usr/bin/env python3
"""Verify the two uniform consecutive-pair S-root families DIRECTLY (not via the
catalogue), for k beyond the b-file range, and confirm the mechanisms:

  F1: (10^k - 1, 10^k)          -- 9-repunit and power of 10.
  F2: (10^k - 10, 10^k - 9)     -- the 'suspicious partial' family, shown uniform.

The S-test here is the exact digit-partition recursion, independent of the b-file.
"""
from functools import lru_cache

def is_s(m):
    s = str(m*m)
    @lru_cache(maxsize=None)
    def expr(target, i):
        if target < 0: return False
        rest = s[i:]
        if target == int(rest): return True
        for j in range(i+1, len(s)):
            if expr(target - int(s[i:j]), j): return True
        return False
    for j in range(1, len(s)):
        if expr(m - int(s[:j]), j): return True
    return False

print("F1 (10^k-1, 10^k):")
for k in range(2, 26):
    a, b = 10**k - 1, 10**k
    print(f"  k={k}: {a}={is_s(a)}, {b}={is_s(b)}", end="")
    if not (is_s(a) and is_s(b)):
        print("  <<< FAIL", end="")
    print()

print("\nF2 (10^k-10, 10^k-9):")
for k in range(3, 26):
    a, b = 10**k - 10, 10**k - 9
    print(f"  k={k}: {a}={is_s(a)}, {b}={is_s(b)}", end="")
    if not (is_s(a) and is_s(b)):
        print("  <<< FAIL", end="")
    print()

# what split witnesses F2? show for a few
print("\nWitness splits for F2 members:")
for k in (3,4,5):
    m = 10**k - 10
    s = str(m*m)
    # any split
    @lru_cache(maxsize=None)
    def expr(target, i):
        if target < 0: return False
        rest = s[i:]
        if target == int(rest): return (s[:i], rest)
        for j in range(i+1, len(s)):
            r = expr(target - int(s[i:j]), j)
            if r: return (s[i:j],) + (r if isinstance(r, tuple) else ())
        return None
    for j in range(1, len(s)):
        r = expr(m - int(s[:j]), j)
        if r:
            print(f"  m={m}=10^{k}-10, m^2={s}, split: ({s[:j]!r}, ...)={r}")
            break

#!/usr/bin/env python3
"""Find clean witness splits for the F2 family (10^k-10, 10^k-9) and probe
how far 10^k - 10^j (single root, and consecutive pair) stays uniform."""
from functools import lru_cache

def ssplit(m):
    """return one valid >=2-block split of str(m^2) summing to m, or None"""
    s = str(m*m)
    n = len(s)
    @lru_cache(maxsize=None)
    def sums(i):
        # set of achievable (val, firstblocklength-chain) is heavy; return set of sums
        res = set()
        val = 0
        for j in range(i, n):
            val = val*10 + int(s[j])
            if j == n-1:
                res.add(val)
            else:
                for sub in sums(j+1):
                    res.add(val+sub)
        return res
    val = 0
    for j in range(0, n-1):
        val = val*10 + int(s[j])
        if (m - val) in sums(j+1):
            return (s[:j+1],)
    return None

def is_s(m):
    return ssplit(m) is not None

print("F2 clean splits (first block prefix):")
for k in range(3, 8):
    m = 10**k - 10
    print(f"  m={m} (10^{k}-10), m^2={m*m}, is_s={is_s(m)}")

# probc: single root 10^k-10^j (no +1) — uniform over which j?
print("\nSingle root 10^k - 10^j: which j are uniform S-roots for all k>=j+?")
for j in range(1, 5):
    ok = True; first_fail=None
    for k in range(j+1, 26):
        m = 10**k - 10**j
        if not is_s(m):
            ok=False; first_fail=(k,m); break
    print(f"  j={j}: uniform-to-25={'yes' if ok else 'fails at '+str(first_fail)}")

# consecutive pair 10^k-10^j, +1
print("\nConsecutive pair (10^k-10^j, +1): uniform over which j?")
for j in range(1, 5):
    ok = True; first_fail=None
    for k in range(j+1, 26):
        a, b = 10**k-10**j, 10**k-10**j+1
        if not (is_s(a) and is_s(b)):
            ok=False; first_fail=(k,a,b); break
    print(f"  j={j}: uniform-to-25={'yes' if ok else 'fails at '+str(first_fail)}")

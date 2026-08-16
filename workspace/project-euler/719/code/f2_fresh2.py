#!/usr/bin/env python3
"""Fresh efficient verification of F2 (10^k-10,10^k-9) and F1 (10^k-1,10^k),
k beyond the recorded k=25, using the efficient boolean digit-DP (no
exponential set enumeration). Watches its own runtime so it cannot hang."""
import time, sys
from functools import lru_cache

def is_s(m):
    s = str(m*m); n = len(s)
    @lru_cache(maxsize=None)
    def dp(i, target):
        if target < 0: return False
        if i >= n: return target == 0
        val = 0
        for j in range(i, n):
            val = val*10 + int(s[j])
            if target - val < 0: break
            if dp(j+1, target-val): return True
        return False
    val = 0
    for j in range(0, n-1):
        val = val*10 + int(s[j])
        if dp(j+1, m-val): return True
    return False

t0=time.time()
# push k from 26 upward, stop at first failure or k=34
for fam, builder, kstart in [("F1 (10^k-1,10^k)", lambda k: 10**k-1, 26),
                              ("F2 (10^k-10,10^k-9)", lambda k: 10**k-10, 26)]:
    for k in range(kstart, 35):
        a=builder(k); b=a+1
        d1=is_s(a); d2=is_s(b)
        print(f"  {fam} k={k} ({a},{b}): {d1},{d2}", flush=True)
        if not (d1 and d2):
            print(f"  -> {fam} FAILS at k={k}")
            break
        if time.time()-t0 > 540:
            print(f"  stopping: 9min watchdog after k={k}")
            sys.exit(0)
print(f"done in {time.time()-t0:.1f}s")

#!/usr/bin/env python3
"""Search for PROVEN infinite consecutive-pair S-root families via the
identity-split method, beyond F1 (10^k-1,10^k) and F2 (10^k-10,10^k-9).
Try families x_k = 10^k - j for j in 1..9: find, for each, a UNIFORM witness
split and verify it as a delayed identity (symbol-free: check concat==square
and sum==root for all k up to 60). Record which j give provable families."""
def concat_ok(vals, m):
    concat = "".join(str(v) for v in vals)
    return concat == str(m*m) and sum(vals) == m

# Known proven families from F1/F2 machinery:
# j=1 (10^k-1): blocks [10^k-2, 0*(k-1), 1]
# j=9 (10^k-9): blocks [10^k-18, 0*(k-2), 8, 1]
# j=10 is not 10^k-10... but j values here are offsets 1..9 from 10^k.
print("Proven single root x_k=10^k-j families (x_k itself an S-root for all k>=?):")
for j in range(1, 10):
    # find a uniform identity-split, guessed from small k by DP
    pass

# Let's instead just PROVE the two known single-root families via identity and
# check their +1 companion by DP at small k to see if generalized.
from functools import lru_cache

def is_s(m):
    s=str(m*m); n=len(s)
    @lru_cache(maxsize=None)
    def dp(i,t):
        if t<0: return False
        if i>=n: return t==0
        v=0
        for j in range(i,n):
            v=v*10+int(s[j])
            if t-v<0: break
            if dp(j+1,t-v): return True
        return False
    v=0
    for j in range(0,n-1):
        v=v*10+int(s[j])
        if dp(j+1,m-v): return True
    return False

print("\nSingle-root families 10^k - j (j=1..9): which j are S-roots for ALL k>=k0?")
for j in range(1,10):
    for k0 in range(2,5):
        ok=True
        for k in range(k0, 16):
            m=10**k-j
            if not is_s(m): ok=False; break
        if ok:
            print(f"  j={j}: 10^k-{j} is S-root for all k>= {k0} (checked k0..15)")
            break
    else:
        print(f"  j={j}: no k0 in 2..4 gives uniform 10^k-{j}")

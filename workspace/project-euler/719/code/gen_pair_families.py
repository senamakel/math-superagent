#!/usr/bin/env python3
"""Test whether the (10^k - 10^j, +1) consecutive-pair generalization is uniform
for j=1..20. The earlier run found it uniform only for k>=j+2; confirm how the
covering of F1 (j=1, i.e. 10^k-10) relates. Identify exactly which j give a
UNIFORM consecutive pair (10^k-10^j, 10^k-10^j+1) as S-roots."""
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
    for jj in range(0,n-1):
        v=v*10+int(s[jj])
        if dp(jj+1,m-v): return True
    return False

results=[]
for j in range(1, 21):
    first_fail=None; ok_all=True
    for k in range(j+2, 26):   # k>=j+2
        a=10**k-10**j; b=a+1
        if not (is_s(a) and is_s(b)):
            ok_all=False; first_fail=(k,a,b); break
    results.append((j, ok_all, first_fail))

print("(10^k-10^j, +1) consecutive-pair uniform from k>=j+2 (checked to k=25):")
for j,ok,ff in results:
    print(f"  j={j:2d}: {'UNIFORM' if ok else 'fails at '+str(ff)}")

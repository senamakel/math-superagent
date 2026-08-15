#!/usr/bin/env python3
"""Does every word of odd-factor period grow ~cm, or do some words of the same
period stay O(1)?  Test many random words per period over long m."""
import random, functools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def nu2_stable(word, m):
    h=[int(word[j%len(word)]) for j in range(m)]
    w=0
    for c in range(1,m):
        s=0
        for i in submasks(c):
            s ^= h[m-1-c+i]
        w+=s
    return w

def has_odd_factor(p): return p & (p-1) != 0

random.seed(1)
print("odd-factor periods: 30 random words each, nu2(400) and nu2(2000) (growing=>nu2~density*m):")
for p in [3,5,6,7,9,10,12,15]:
    if not has_odd_factor(p): continue
    v400s=[]; v2000s=[]
    for _ in range(30):
        word=''.join(random.choice('01') for _ in range(p))
        v400s.append(nu2_stable(word,400))
        v2000s.append(nu2_stable(word,2000))
    # classify: does nu2(2000) stay bounded (say < 20) or grow?
    bounded=[i for i,(a,b) in enumerate(zip(v400s,v2000s)) if b<20]
    d400=sorted((v/400 for v in v400s))
    d2000=sorted((v/2000 for v in v2000s))
    print(f"  period {p}: nu2(2000) min={min(v2000s)} med={sorted(v2000s)[15]} max={max(v2000s)} ; "
          f"density med d400={d400[15]:.3f} d2000={d2000[15]:.3f} ; #bounded(<20 at 2000)={len(bounded)}")

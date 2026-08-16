import os, sys
os.chdir("/workspace")
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos

def nu2(n, h):
    S, ones = s_sos(n, h)
    return ones

def indicator(n, S):
    h=[0]*n
    for j in S:
        if 0<=j<n: h[j]=1
    return h

def run_family(fn, n_lo, n_max, name):
    lows=[]
    for n in range(n_lo, n_max+1):
        r = nu2(n, fn(n))/n
        lows.append(r)
    whole=min(lows)
    tail=min(lows[len(lows)//2:])
    print(f"{name:30s} n[{n_lo},{n_max}] whole_min={whole:.4f} tail_min={tail:.4f}")
    return whole, tail

import sympy

p2   = lambda n: indicator(n, [1<<k for k in range(64)])
sq   = lambda n: indicator(n, [k*k for k in range(1,2000)])
p2m1 = lambda n: indicator(n, [(1<<k)-1 for k in range(1,64)])
p2p1 = lambda n: indicator(n, [(1<<k)+1 for k in range(1,64)])
prim = lambda n: indicator(n, list(sympy.ntheory.generate.primerange(0,n+100)))
sqp1 = lambda n: indicator(n, set(k*k for k in range(1,2000)) | set(k*k+1 for k in range(1,2000)))
cubs = lambda n: indicator(n, [k**3 for k in range(1,100)])
luc  = lambda n: indicator(n, set(1<<k for k in range(1,40)) | set((1<<k)+(1<<(k//2)) for k in range(1,40)))

for name,fn in [("powers2",p2),("squares",sq),("pow2-1",p2m1),("pow2+1",p2p1),
                ("prime idx",prim),("sq&+1",sqp1),("cubes",cubs),("luc",luc)]:
    run_family(fn,256,4096,name)

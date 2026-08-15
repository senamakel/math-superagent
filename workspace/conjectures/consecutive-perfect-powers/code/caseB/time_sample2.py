#!/usr/bin/env python3
import math, time

def one(c, p):
    x = c*c+1
    T = (pow(x,p)-1)//(c*c)
    s = math.isqrt(T)
    return s*s == T, T.bit_length()

# isolated single measurements
for (c,p) in [(100000,457),(100000,499),(50000,499),(10000,499),(100000,5)]:
    # find p==1 mod4 prime near those
    t0=time.time()
    rep=[]
    ok,_=one(c,p)
    t1=time.time()
    _,bits=one(c,p)
    t2=time.time()
    print(f"c={c} p={p}: first {t1-t0:.4f}s, second(with bits) {t2-t1:.4f}s  bits~{bits}")

# proper averaged timing over repeats
def timing(c,p,n=200):
    t0=time.time()
    for _ in range(n):
        one(c,p)
    return (time.time()-t0)/n

for (c,p) in [(10000,457),(100000,457),(100000,13)]:
    per=timing(c,p)
    print(f"c={c} p={p}: {per*1e3:.3f} ms/op")

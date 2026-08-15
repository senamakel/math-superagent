#!/usr/bin/env python3
"""Max possible nu2 over all period-2^k words for k=0..3, at m=400, via direct
submask XOR (cheap since avg submask count ~ m^{log2 3 -1})."""
import functools, itertools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

def y_seq(h,m):
    N=m-1
    return [reduce(lambda a,b:a^b,(h[N-c+i] for i in submasks(c)),0) for c in range(1,m+1)]

def periodic_h(word,m):
    L=len(word)
    return [int(word[j%L]) for j in range(m)]

def nu2(word,m):
    return sum(y_seq(periodic_h(word,m),m))

m=400
for k in range(0,4):
    L=2**k
    best=0; bestwords=[]
    for bits in itertools.product([0,1],repeat=L):
        word=''.join(map(str,bits))
        v=nu2(word,m)
        if v>best:
            best=v; bestwords=[word]
        elif v==best:
            bestwords.append(word)
    print(f"k={k} L={L}: max nu2 = {best} at m={m}, achieved by {len(bestwords)} words e.g. {bestwords[:5]}")

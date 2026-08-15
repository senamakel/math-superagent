#!/usr/bin/env python3
import functools
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

for word in ["01","10"]:
    for m in [40,60,200,601]:
        y=y_seq(periodic_h(word,m),m)
        pos=[c+1 for c,v in enumerate(y) if v]
        print(f"word {word} m={m}: ones at {pos}  count={len(pos)}")

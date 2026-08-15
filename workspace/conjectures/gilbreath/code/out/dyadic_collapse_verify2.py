#!/usr/bin/env python3
"""Correct probe derailing from fold_weight_h: outputs c = k-1 for k in 2..m,
i.e. c in 1..m-1, window h[m-1-c+i] (h indexed 0..m-1).  Matches the real fold.
Claim: for h periodic of period 2^k, output_c = 0 for all c >= 2^k
(in the valid encoder range c=1..m-1), and nonzero only for c in 1..2^k-1."""
import functools, itertools
reduce=functools.reduce

def submasks(c):
    out=[]; i=c
    while True:
        out.append(i)
        if i==0: break
        i=(i-1)&c
    return out

# mimic fold_weight_h exactly
def fw(h, m):
    w=0
    cells={}
    for k in range(2,m+1):
        c=k-1
        s=0
        for i in range(k):
            if (i&c)==i:
                s ^= h[m-k+i]
        cells[c]=s
        w+=s
    return w, cells

def periodic_h(word,m):
    L=len(word)
    return [int(word[j%L]) for j in range(m)]

def check(word,m):
    L=len(word); k=L.bit_length()-1
    _,cells=fw(periodic_h(word,m),m)
    # valid c in 1..m-1
    viol=[c for c in range(1,m) if cells.get(c,0)==1 and c>=L]
    maxc=max([c for c in range(1,m) if cells.get(c,0)==1], default=0)
    return viol, maxc

for k in [1,2,3]:
    L=2**k
    total=0
    maxnz=0
    for bits in itertools.product([0,1],repeat=L):
        word=''.join(map(str,bits))
        for m in [60,200,601]:
            viol,maxc=check(word,m)
            maxnz=max(maxnz,maxc)
            if viol: total+=1
    print(f"k={k} L={L}: violations (nonzero at c>=2^k in valid range) = {total}; max nonzero c seen = {maxnz} (should be < {L})")

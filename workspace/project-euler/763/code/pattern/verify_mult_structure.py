#!/usr/bin/env python3
"""Decisive verification of the multiplicative structure of per-histogram
multiplicities over the ENTIRE N=2..12 dump.

Claim to test:
  mult(hist) = 2^(2*n4) * 3^b   for some integer b>=0
for every histogram, i.e. mult / 2^(2*n4) is always a power of 3.
List every exception (should be exactly 1: the (0,1,3,6,7,5,3) histogram
whose mult=30=2*3*5 carries a 5-factor).
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def count_3s_maybe(v):
    # is v a power of 3? return (is_pow3, exponent)
    e=0
    while v%3==0 and v>1:
        v//=3; e+=1
    if v==1: return True, e
    return False, None

exceptions=[]
tot=0
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        tot+=1
        n4=hist.split().count('4')
        denom=2**(2*n4)
        if m % denom != 0:
            exceptions.append((n,hist,m,'NOT divisible by 2^(2n4)'))
            continue
        q=m//denom
        ok,e=count_3s_maybe(q)
        if not ok:
            exceptions.append((n,hist,m,q,f'quotient {q} not a power of 3 (2^a={2*n4})'))
print(f"Total histograms checked: {tot}")
print(f"Exceptions to mult=2^(2*#4)*3^b : {len(exceptions)}")
for x in exceptions:
    print("  ",x)

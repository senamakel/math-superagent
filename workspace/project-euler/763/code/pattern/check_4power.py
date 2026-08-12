#!/usr/bin/env python3
"""Hypothesis: mult(hist) = 2^{2*#4s} * 3^{e} for some exponent e depending on
the histogram. Check across all data: for every histogram, factor mult, and
test whether power-of-2 == 2*(count of '4' in hist). Report the residual 3^e
and how e relates to the histogram. Also identify any non-2,3 exceptions."""
import glob, collections, re

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def factor2(v):
    a=0
    while v%2==0: v//=2; a+=1
    b=0
    while v%3==0: v//=3; b+=1
    return a,b,v

print(f"{'N':>3} {'hist':>34} {'mult':>8} {'2^a':>4} {'3^b':>4} {'n4':>2} {'a==2n4?':>8} {'rest':>4}")
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in sorted(per.items(), key=lambda kv:-kv[1]):
        a,b,rest = factor2(m)
        n4 = hist.split().count('4')
        ok = (a == 2*n4)
        # sanity: rest should be 1 unless extra primes
        print(f"{n:>3} {hist:>34} {m:>8} {a:>4} {b:>4} {n4:>2} {str(ok):>8} {rest:>4}")

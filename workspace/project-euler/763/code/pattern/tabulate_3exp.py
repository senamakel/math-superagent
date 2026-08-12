#!/usr/bin/env python3
"""Tabulate each histogram with its mult, 2^a, 3^b, and various features to
hunt a closed form for b (3-exponent). Features: n4, n5, n3, n6, n7 counts,
nslots (#levels), and the histogram vector itself."""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def f23(v):
    a=b=0
    while v%2==0: v//=2; a+=1
    while v%3==0: v//=3; b+=1
    return a,b,v

rows=[]
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in sorted(per.items(), key=lambda kv:-kv[1]):
        vals=list(map(int,hist.split()))
        a,b,rest=f23(m)
        rows.append((n,hist,vals,m,a,b,rest))
# Print all rows that have any 4 or 5 or 6 or 7 (non-trivial histograms), with a,b
print(f"{'N':>3} {'hist':>30} {'mult':>8} {'2^a':>4} {'3^b':>3} {'rest':>4} {'n4':>2} {'n5':>2} {'n3':>2} {'other':>8}")
for n,hist,vals,m,a,b,rest in rows:
    if any(v not in (0,2,3) for v in vals):
        n4=vals.count(4); n5=vals.count(5); n3=vals.count(3)
        other=[v for v in vals if v not in (0,2,3,4,5)]
        print(f"{n:>3} {hist:>30} {m:>8} {a:>4} {b:>3} {rest:>4} {n4:>2} {n5:>2} {n3:>2} {str(other):>8}")

#!/usr/bin/env python3
"""Independent check: summing the closed-form multiplicity over all distinct
histograms at N must equal D(N). Verifies the closed form is a true partition
of the config space, not just a per-histogram fit. Compare against known D."""
import glob, collections, re

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def predict(vals):
    cnt=collections.Counter(vals)
    n1=cnt[1];n2=cnt[2];n3=cnt[3];n4=cnt[4]
    if 6 in cnt:
        return 10*2**(2*n4)*3**(n1+n2+n3-2)
    return 2**(2*n4)*3**(n1+n2+n3-1)

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

print("N | sum_of_mult (from closed form over histograms) | D(N) | match")
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    hists=set()
    for line in open(path):
        h,M,b=line.rstrip().split('|')
        hists.add(tuple(map(int,h.strip().split())))
    s=sum(predict(v) for v in hists)
    print(f"{n:>2} | {s:>10} | {D.get(n,'?')} | {s==D[n]}")
# OOS
from collections import defaultdict
agg=defaultdict(int)
for line in open('code/out/per_hist_mult_13_14.txt'):
    line=line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n=int(line[2:line.index('hist=')].strip())
    h=line.index('hist='); m_i=line.index('mult=')
    hist_str=line[h+5:m_i].strip()
    vals=[int(x) for x in hist_str.split()]
    while vals and vals[-1]==0: vals.pop()
    agg[n]+=predict(vals)
for n in (13,14):
    print(f"{n:>2} | {agg[n]:>10} | {D.get(n,'?')} | {agg[n]==D[n]}")

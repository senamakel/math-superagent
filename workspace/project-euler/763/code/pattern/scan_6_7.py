#!/usr/bin/env python3
"""Characterize ALL histograms containing a level with 6 or 7 cells, across
in-sample (N=2..12 data dumps) and OOS (N=13,14), tabulating the value 6/7,
the multiplicity, and the 'naive' prediction 2^(2n4)3^(n1+n2+n3-1), to pin
down the correction rule exactly."""
import glob, collections, re

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def naive(vals):
    cnt=collections.Counter(vals)
    n1=cnt[1];n2=cnt[2];n3=cnt[3];n4=cnt[4]
    return 2**(2*n4)*3**(n1+n2+n3-1)

rows=[]
# in-sample
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        vals=list(map(int,hist.split()))
        if 6 in vals or 7 in vals:
            rows.append((n,vals,m,naive(vals)))
# OOS
for line in open('code/out/per_hist_mult_13_14.txt'):
    line=line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n=int(line[2:line.index('hist=')].strip())
    h=line.index('hist='); m_i=line.index('mult=')
    hist_str=line[h+5:m_i].strip()
    mval=int(line[m_i+5:])
    vals=[int(x) for x in hist_str.split()]
    while vals and vals[-1]==0: vals.pop()
    if 6 in vals or 7 in vals:
        rows.append((n,vals,mval,naive(vals)))

for n,vals,m,pred in rows:
    ratio = m/pred
    flag = ""
    if m!=pred:
        flag = f"  ratio={ratio}"
    print(f"N={n:>3} {str(vals):>35} mult={m:>6} naive={pred:>6}{flag}")

#!/usr/bin/env python3
"""FINAL verification of the per-histogram multiplicity closed form with the
6-level correction.  Rule:
  W(h) = 2^(2*n4) * 3^(n1+n2+n3-1)                    if no level has 6 cells
       = 10 * 2^(2*n4) * 3^(n1+n2+n3-2)               if some level has 6 cells
where nk = #levels with exactly k cells (a_1..a_{M-1}, the interior levels).
Check EVERY histogram in-sample (N=2..12 data dumps) and OOS (N=13,14)."""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

def predict(vals):
    cnt=collections.Counter(vals)
    n1=cnt[1];n2=cnt[2];n3=cnt[3];n4=cnt[4]
    base=2**(2*n4)*3**(n1+n2+n3-1)
    if 6 in cnt:
        return 10*2**(2*n4)*3**(n1+n2+n3-2), True
    return base, False

exceptions=[]; tot=0; sixcount=0
# in-sample
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n=sorted_key(path)
    per=collections.Counter()
    for line in open(path):
        hist,M,bbox=line.rstrip().split('|')
        per[hist.strip()]+=1
    for hist,m in per.items():
        tot+=1
        vals=list(map(int,hist.split()))
        if 6 in collections.Counter(vals): sixcount+=1
        pred,_=predict(vals)
        if pred!=m:
            exceptions.append((n,vals,m,pred))
# OOS
for line in open('code/out/per_hist_mult_13_14.txt'):
    line=line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n=int(line[2:line.index('hist=')].strip())
    h=line.index('hist='); m_i=line.index('mult=')
    hist_str=line[h+5:m_i].strip(); mval=int(line[m_i+5:])
    vals=[int(x) for x in hist_str.split()]
    while vals and vals[-1]==0: vals.pop()
    tot+=1
    if 6 in collections.Counter(vals): sixcount+=1
    pred,_=predict(vals)
    if pred!=mval:
        exceptions.append((n,vals,mval,pred))

print(f"Total histograms checked (in-sample N=2..12 + OOS N=13,14): {tot}")
print(f"Histograms containing a 6-level: {sixcount}")
print(f"Exceptions to corrected rule: {len(exceptions)}")
for e in exceptions:
    print("  ",e)

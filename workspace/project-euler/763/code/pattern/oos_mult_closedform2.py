#!/usr/bin/env python3
"""OOS test of mult(hist)=2^(2*n4)*3^(n1+n2+n3-1) on fresh N=13,14 data.
Format: 'N=13 hist=0 1 3 6 7 5 2 3 0 0 0 0 0 0 0 mult=90'
hist entries are space-separated; mult= is last token. The hist may contain
trailing zeros '0' padding AND sometimes the true histogram has length M+1;
trailing zeros beyond the max level must be dropped because real histograms
start with level0=0 and end at max level M with 3. So: drop leading 0 and
trailing 0s."""
import re, collections

def parse_hist(hist_str):
    vals=[int(x) for x in hist_str.split()]
    # drop trailing zeros (padding)
    while vals and vals[-1]==0:
        vals.pop()
    return vals

exceptions=[]; tot=0
for line in open('code/out/per_hist_mult_13_14.txt'):
    line=line.strip()
    if not line.startswith('N=') or 'mult=' not in line:
        continue
    h=line.index('hist=')
    m=line.index('mult=')
    hist_str=line[h+5:m].strip()
    mval=int(line[m+5:])
    vals=parse_hist(hist_str)
    tot+=1
    if vals[0]!=0:  # sanity
        exceptions.append(('BAD lead',vals,mval))
        continue
    cnt=collections.Counter(vals)
    n1=cnt[1];n2=cnt[2];n3=cnt[3];n4=cnt[4]
    pred=2**(2*n4)*3**(n1+n2+n3-1)
    if pred!=mval:
        exceptions.append((vals,mval,pred,n1,n2,n3,n4))
print(f"OOS histograms checked: {tot}")
print(f"Exceptions: {len(exceptions)}")
for e in exceptions[:30]:
    print("  ",e)

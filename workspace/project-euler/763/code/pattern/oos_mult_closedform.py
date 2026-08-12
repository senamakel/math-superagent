#!/usr/bin/env python3
"""OUT-OF-SAMPLE TEST of the closed form
    mult(hist) = 2^(2*n4) * 3^(n1+n2+n3-1)
against FRESH N=13,14 histogram multiplicities (never used to guess the form).
Report all exceptions."""
import collections

exceptions=[]
tot=0
for line in open('code/out/per_hist_mult_13_14.txt'):
    line=line.strip()
    if not line or line.startswith('N=') and 'hist' not in line and 'total' in line:
        pass
    if not line.startswith('N='):
        continue
    # parse "N=<n> hist=<...> mult=<m>"
    # format from builder unknown; robust parse
    parts=line.split()
    # find hist=... and mult=...
    hist=None; m=None
    for p in parts:
        if p.startswith('hist='):
            hist=p[len('hist='):]
        if p.startswith('mult='):
            m=int(p[len('mult='):])
    if hist is None or m is None:
        continue
    if hist.strip()=='':
        continue
    vals=[int(x) for x in hist.split()]
    tot+=1
    cnt=collections.Counter(vals)
    n1=cnt[1];n2=cnt[2];n3=cnt[3];n4=cnt[4]
    pred=2**(2*n4)*3**(n1+n2+n3-1)
    if pred!=m:
        exceptions.append((vals,m,pred,n1,n2,n3,n4))
print(f"OOS histograms checked: {tot}")
print(f"Exceptions: {len(exceptions)}")
for e in exceptions[:20]:
    print("  ",e)

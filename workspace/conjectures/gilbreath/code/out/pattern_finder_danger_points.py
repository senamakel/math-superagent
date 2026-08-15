#!/usr/bin/env python3
"""Examine the danger points of the linear transfer bound nu2 >= c*n:
  - the n where 2*nu2-n is most negative (deficit events)
  - the neighborhood of the single 0.75w violation (n=1005)
  - structure of deltas of nu2 and of the deviation
"""
import math
nu2=[]
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2.append(int(p[1]))

N=len(nu2)
dev=[2*nu2[n-1]-n for n in range(1,N+1)]

# most negative deviations (danger for one-sided lower bound)
order=sorted(range(1,N+1), key=lambda n: dev[n-1])[:15]
print("most negative dev(n)=2nu2-n (with n):")
for n in order[:10]:
    print("  n=%6d dev=%5d nu2/n=%.4f" % (n, dev[n-1], nu2[n-1]/n))

# longest deficit runs (dev<0)
maxlen=0; cur=0; runs=[]
start=0
for n in range(1,N+1):
    if dev[n-1]<0:
        if cur==0: start=n
        cur+=1
    else:
        if cur>0: runs.append((start, cur))
        cur=0
if cur>0: runs.append((start,cur))
runs.sort(key=lambda r:-r[1])
print("longest deficit runs (start,len), top 6:")
for r in runs[:6]: print("  ", r)

# neighborhood of n=1005
print("neighborhood of n=1005 (the 0.75w violation):")
for n in range(995,1016):
    wn=0
    # recompute w from data? not stored. skip.
print("  nu2[995:1016]=", nu2[994:1016])
print("  dev[995:1016]=", dev[994:1016])

# deltas of nu2: d_n = nu2(n)-nu2(n-1) -- this increments by 0/1/2 etc; look at where nu2(n)-nu2(n-1)=0 stretches
print("\ndeltas nu2(n)-nu2(n-1) first 40:")
print([nu2[n-1]-nu2[n-2] for n in range(2,42)])

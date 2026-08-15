#!/usr/bin/env python3
"""Final check: does the composed linear supply bound (any positive c>0,
here the empirical 0.2742) exceed the theorem's threshold n^0.525 for all n
in range? And give the crossover. Also confirm the linear bound B(n)=c*n
dominates n^0.525 from some n0 and stays above through NMAX."""
import math
from lib.gilbreath import primes_up_to
NMAX=30000
P=primes_up_to(1_000_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,b in enumerate(hbits): pref[i+1]=pref[i]+b
def w(n): return pref[n]-pref[2]
nu2=[]
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2.append(int(p[1]))
minw31=min(w(n)/n for n in range(31,NMAX+1))
c=0.5*minw31
print("composed linear constant c = %.4f" % c)
# crossover where c*n > n^0.525
# c*n = n^0.525 => n^(0.475) = 1/c => n = (1/c)^(1/0.475)
n0=(1.0/c)**(1.0/0.475)
print("crossover n ~ %.1f (beyond this, linear bound exceeds threshold)" % n0)
# verify nu2 >= max(c*n, n^0.525) on sampled range from n>=31
cnt=0; firstbad=None
for n in range(31,NMAX+1):
    need=max(c*n, n**0.525)
    if nu2[n-1]<need:
        cnt+=1
        if firstbad is None: firstbad=n
print("n in [31,%d] where nu2 < max(c*n, n^0.525): %d first=%s" % (NMAX,cnt,firstbad))
# margin of nu2 over n^0.525 at the weakest point (min ratio over n>=31)
mn=(1e9,0)
for n in range(31,NMAX+1):
    r=nu2[n-1]/n**0.525
    if r<mn[0]: mn=(r,n)
print("min nu2/n^0.525 over n>=31: %.3f at n=%d (must be >1 for theorem)" % (mn[0],mn[1]))

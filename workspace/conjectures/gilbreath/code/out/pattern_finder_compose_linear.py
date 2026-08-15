#!/usr/bin/env python3
"""Compose the two exact verified-numerically facts into a LINEAR supply bound:

  (a) nu2(n) >= (1/2) * w(n)  for all n >= 17        [verified earlier, 1 violation at n<=16, 0 after]
  (b) w(n) >= c * n  for all n >= some tail, c>0     [mod-4 switch density lower bound]

Then nu2(n) >= (c/2)*n, a genuine linear bound. Granville's Theorem 5.5 only
needs nu2 > n^0.525, so ANY positive linear density c/2 suffices for large n.

Report the exact constants over the 30000 supplied terms, and the composed
lower bound with its weakest point.
"""
from lib.gilbreath import primes_up_to

NMAX = 30000
P = primes_up_to(1_000_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,b in enumerate(hbits): pref[i+1]=pref[i]+b
def w(n): return pref[n]-pref[2]

nu2=[]
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2.append(int(p[1]))
assert len(nu2)==NMAX

# (a) exact check nu2 >= w/2 for n>=17
viol=[]
for n in range(17, NMAX+1):
    if nu2[n-1] < w(n)/2.0 - 1e-12:
        viol.append(n)
print("(a) nu2 >= w/2 for n in [17,%d]: %d violations" % (NMAX, len(viol)))

# (b) min w/n over tails
for tail in (17, 31, 100, 1000):
    mn=(1e9,0)
    for n in range(tail, NMAX+1):
        r=w(n)/n
        if r<mn[0]: mn=(r,n)
    print("(b) tail=%d: min w(n)/n = %.4f at n=%d" % (tail, mn[0], mn[1]))

# composed: find best linear constant c such that nu2>=c*n on a tail, exact min
for tail in (31, 100, 1000):
    mn=(1e9,0)
    for n in range(tail, NMAX+1):
        r=nu2[n-1]/n
        if r<mn[0]: mn=(r,n)
    print("composed: nu2/n over n>=%d: min = %.4f at n=%d" % (tail, mn[0], mn[1]))

# weakest composed bound via (a)&(b): for n>=31, nu2 >= 0.5*w >= 0.5*(min w/n at n>=31)*n
minw31 = min(w(n)/n for n in range(31, NMAX+1))
print("via (a)&(b): nu2 >= %.4f * n for n>=31" % (0.5*minw31))

# confirm composition is valid: for every n>=31, nu2 >= 0.5*w and w >= minw31*n
bad = sum(1 for n in range(31, NMAX+1) if nu2[n-1] < 0.5*minw31*n - 1e-9)
print("direct check nu2 >= 0.5*minw31*n on n>=31: %d violations" % bad)

# threshold: single 0.75w violation at n=1005?
v075=[n for n in range(1005, NMAX+1) if nu2[n-1]<0.75*w(n)]
print("nu2<0.75w on n>=1005: %d violations (n=1005 alone per report)" % len(v075))

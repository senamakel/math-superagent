#!/usr/bin/env python3
"""Attack the transfer-bound decomposition: is the 0.75w violation at n=1005
an isolated dip (dip-and-rebound), and does the 0.5w bound have any near-miss
(on or below, not strictly below)?  Also test whether the composed linear
bound nu2>=0.5*minw*n is robust to the weakest w-point being removed."""
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

# isolation of n=1005 for 0.75w
print("n=1005: nu2=%d w=%d 0.75w=%.1f ratio=%.4f" % (nu2[1004], w(1005), 0.75*w(1005), nu2[1004]/w(1005)))
print("neighbors n=1003..1007 ratios (=nu2/w):")
for n in range(1003,1008):
    print("  n=%d ratio=%.4f" % (n, nu2[n-1]/w(n)))
below=[n for n in range(1000,2000) if nu2[n-1]<0.75*w(n)]
print("0.75w violations in n in [1000,2000]:", below)

# closest approach to 0.5w on n>=17 (margin of the linear transfer)
min_margin=(1e9,0)
for n in range(17,NMAX+1):
    m = nu2[n-1] - 0.5*w(n)
    if m<min_margin[0]: min_margin=(m,n)
print("min of (nu2 - w/2) over n>=17: %.3f at n=%d (0 = bare contact; positive = slack)" % (min_margin[0], min_margin[1]))

# robustness: recompute min w/n excluding the single worst n=31 to see sensitivity
tw=2
mn1=(1e9,0)
for n in range(31,NMAX+1):
    r=w(n)/n
    if r<mn1[0]: mn1=(r,n)
# remove n=31
w2_vals=[w(n)/n for n in range(31,NMAX+1) if n!=31]
mn2=min(w2_vals)
print("min w/n on n>=31 incl n=31: %.4f at n=%d ; excluding n=31: %.4f" % (mn1[0],mn1[1],mn2))

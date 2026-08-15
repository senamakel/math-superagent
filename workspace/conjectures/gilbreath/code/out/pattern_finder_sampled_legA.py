#!/usr/bin/env python3
"""Leg (a) at the 13 sampled nu2 points (from nu2_incremental_1e5.txt, already
read: n:nu2). Check nu2 >= w/2 for each large-n point."""
from lib.gilbreath import primes_up_to
samples={50:20,100:46,200:106,400:216,800:397,1600:740,3200:1573,3999:2045,
         5000:2444,10000:4992,20000:9962,50000:25173,100000:50109}
NMAX=100000
P=primes_up_to(1_500_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,b in enumerate(hbits): pref[i+1]=pref[i]+b
def w(n): return pref[n]-pref[2]
print("samples: n : nu2 : w : nu2/w : nu2>=w/2?")
allok=True
for n in sorted(samples):
    nu=samples[n]
    wn=w(n)
    ok = nu >= 0.5*wn
    allok &= ok
    print("  n=%6d nu2=%6d w=%6d nu2/w=%.3f %s" % (n,nu,wn,nu/wn,ok))
print("ALL sampled nu2>=w/2 :", allok)

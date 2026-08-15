#!/usr/bin/env python3
"""Probe the two sharp transfer points:
  - n=44  where min nu2/w over n>=17 is exactly 0.5000 (tight for 0.5w)
  - n=1005 where nu2<0.75w the only time at threshold 1005
Report the full local nu2, w, gap-bit window signature around both.
"""
from lib.gilbreath import primes_up_to
P = primes_up_to(1_000_000)
hbits = [((P[i+1]-P[i])//2) % 2 for i in range(len(P)-1)]
pref=[0]
for b in hbits: pref.append(pref[-1]+b)
def w(n): return pref[n]-pref[2]
nu2={}
for line in open("code/out/nu2_dense.txt"):
    n,v=line.split(); nu2[int(n)]=int(v)

print("Tight-0.5 window around n=44:")
for n in range(40,49):
    print(f"  n={n} nu2={nu2[n]} w={w(n)} ratio={nu2[n]/w(n):.4f} 2nu2-w={2*nu2[n]-w(n)}")
print("  bits j=2..44 (=1 iff gap==2 mod4):", ''.join(map(str,hbits[2:44])))
print("  w(44)=",w(44))

print("\nSingular 0.75 point n=1005 and neighbors:")
for n in range(1000,1011):
    print(f"  n={n} nu2={nu2[n]} w={w(n)} ratio={nu2[n]/w(n):.4f} 2nu2-n={2*nu2[n]-n}")
print("  bits j=2..1010 density:", sum(hbits[2:1010])/1008)

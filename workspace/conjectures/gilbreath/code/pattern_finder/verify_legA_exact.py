#!/usr/bin/env python3
"""Reproduce the run's EXACT nu2 and w conventions and test leg(a) nu2>=w/2.

The run's conventions (from code/gap_analysis/nu2_vs_gap_parity.py):
  gaps[i]   = P[i+1]-P[i]                      (g_{i+1}, i=0.. -> g_1,g_2,...)
  hbits[j]  = (g_{j+1}//2) % 2                  (j=0 -> gap g_1)
  w(n)      = sum(hbits[2:n])  = sum over j in [2,n-1]  -> gaps g_3..g_n
  diag(n)   = [A_k[n-k] for k in range(n)]
  tail      = diag[2:-1]                        (k=2..n-2)
  cyc       = maximal {0,2} suffix of tail
  nu2(n)    = count of 2s in cyc

Then test nu2(n) >= w(n)/2 for all n>=17 over n=1..30000, using the SAME
triangle construction (rows truncated at width 30000).
"""
import math
from lib.gilbreath import primes_up_to

def main():
    NMAX = 30000
    BOUND = 500000  # enough primes for width 30000 (~26000 primes)
    P = primes_up_to(BOUND)
    print(f"sieve {BOUND}: {len(P)} primes, need > {NMAX}")
    gaps = [P[i+1]-P[i] for i in range(len(P)-1)]
    hbits = [(g//2) % 2 for g in gaps]
    def w(n):
        return sum(hbits[2:n])     # j in [2,n-1]
    # triangle rows truncated at width NMAX+2
    rows=[P[:NMAX+2]]
    for k in range(1,NMAX):
        prev=rows[-1]
        rows.append([abs(prev[i+1]-prev[i]) for i in range(len(prev)-1)])
        if k % 5000==0:
            print(f"  row {k}")
    viol=0; first=None; min_ratio=1e9; min_n=None; equ=0; eq_list=[]
    for n in range(2,NMAX+1):
        d=[rows[k][n-k] for k in range(n)]
        tail=d[2:-1]
        i=len(tail)
        while i>0 and tail[i-1] in (0,2):
            i-=1
        cyc=tail[i:]
        nu2c=cyc.count(2)
        wv=w(n)
        ratio=nu2c/wv if wv>0 else 1e9
        if ratio<min_ratio: min_ratio=ratio; min_n=n
        if nu2c < wv/2 - 1e-12:
            viol+=1
            if first is None: first=n
            if viol<=15:
                print(f"  VIOL n={n} nu2={nu2c} w={wv} ratio={ratio:.4f}")
        if abs(nu2c - wv/2) < 1e-9:
            equ+=1
            if len(eq_list)<5: eq_list.append(n)
    print(f"leg(a) nu2>=w/2 over n in [17,{NMAX}]: viol={viol} first={first}")
    print(f"min nu2/w = {min_ratio:.4f} at n={min_n}")
    print(f"equality contacts nu2==w/2: {equ} (first {eq_list})")

if __name__=="__main__":
    main()

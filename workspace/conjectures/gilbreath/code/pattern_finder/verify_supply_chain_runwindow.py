#!/usr/bin/env python3
"""Full supply chain with the run's EXACT conventions.

nu2(n): count of 2s in the maximal {0,2} suffix of diag(n)=[A_k[n-k]], from
        the truncated triangle (verified in verify_legA_exact).
w(n)   : sum of hbits[2:n], hbits[j]=(g_{j+1}//2)%2, i.e. gaps g_3..g_n.
         window size n-2.
leg(a) nu2 >= w/2  (verified 0 viol n>=17)
leg(b) w >= (n-2)/2   (ballot: at least half of the n-2 gaps switch mod4)
compose nu2 >= (n-2)/4, clear n^0.525.

Recompute w with run's window (gaps g_3..g_n) and test everything.
"""
import math
from lib.gilbreath import primes_up_to

def main():
    NMAX=30000
    P=primes_up_to(500000)
    gaps=[P[i+1]-P[i] for i in range(len(P)-1)]
    hbits=[(g//2)%2 for g in gaps]      # hbits[j] = (g_{j+1}//2)%2 ; j=0->g_1
    # w(n) = sum(hbits[2:n])  = gaps g_3..g_n, count n-2
    # prefix of hbits
    # w_pref[k] = sum hbits[0..k-1]
    import itertools
    wpref=[0]
    for h in hbits: wpref.append(wpref[-1]+h)
    def w(n): return wpref[n]-wpref[2]  # sum hbits[2..n-1]
    # nu2 from the dense file (exact, run's construction)
    nu2={}
    with open('code/out/nu2_dense.txt') as f:
        for line in f:
            s=line.split()
            if len(s)==2: nu2[int(s[0])]=int(s[1])
    # leg(a)
    va=0; fa=None; minr=1e9; mn=None
    for n in range(17,NMAX+1):
        r=nu2[n]/(w(n) if w(n)>0 else 1)
        if r<minr: minr=r; mn=n
        if nu2[n] < w(n)/2-1e-12:
            va+=1
            if fa is None: fa=n
    print(f"[run window] leg(a) nu2>=w/2 n in [17,{NMAX}]: viol={va} first={fa} min nu2/w={minr:.4f}@{mn}")
    # leg(b) w >= (n-2)/2
    vb=0; fb=None; minex=1e9
    for n in range(2,NMAX+1):
        ex=2*w(n)-(n-2)
        if ex<0:
            vb+=1
            if fb is None: fb=n
        if ex<minex: minex=ex
    print(f"[run window] leg(b) w>=(n-2)/2 n in [2,{NMAX}]: viol={vb} first={fb} min excess={minex}")
    # composed nu2 >= (n-2)/4
    vc=0; fc=None; minm=1e9; minmn=None
    for n in range(23,NMAX+1):
        if nu2[n] < (n-2)/4-1e-12:
            vc+=1
            if fc is None: fc=n
        m=nu2[n]/n**0.525
        if m<minm: minm=m; minmn=n
    print(f"[run window] composed nu2>=(n-2)/4 n in [23,{NMAX}]: viol={vc} first={fc} min nu2/n^0.525={minm:.3f}@{minmn}")
    # also check nu2-n^0.525 margin at the min point
    print(f"  nu2({minmn})={nu2[minmn]} vs n^0.525={minmn**0.525:.1f} ratio {minm:.3f}")
    # crossover: (n-2)/4 > n^0.525
    for cand in range(2,60):
        if (cand-2)/4 > cand**0.525:
            print(f"  first n with (n-2)/4 > n^0.525: {cand}")
            break

if __name__=="__main__":
    main()

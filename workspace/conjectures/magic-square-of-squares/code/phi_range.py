#!/usr/bin/env python3
"""Examine the real-range (clip) structure of Phi that governs the additive
condition q1+q2<1.  q = f(m,n)=4mn(m^2-n^2)/(m^2+n^2)^2 in [0,?].  The MSS
additive chain needs q1,q2,q1+q2,q1-q2 all in Phi with 0<q1-q2<q1<q1+q2<1.
So the relevant set is Phi_cap = Phi intersect (0,1).  Report:
  [1] max and min of Phi_cap(M), and where the max is attained (m,n);
  [2] density: # values in each dyadic decile of (0,1);
  [3] for each q in Phi_cap(M), is q/2 in Phi? (a q1=q2=q/2 candidate would
      need 2q... actually the clip is q1+q2<1; test the strict sub-1 sum
      condition: how many pairs q1,q2 in Phi_cap(M) have q1+q2<1 AND
      q1+q2 reachable — already the no-triple search; here just report the
      size of Phi_cap(M) and its max)."""
from math import gcd
from fractions import Fraction

def f_frac(m,n):
    num=4*m*n*(m*m-n*n); den=(m*m+n*n)**2
    g=gcd(num,den)
    return Fraction(num//g, den//g)

def phi_set(M):
    return {f_frac(m,n) for m in range(2,M+1) for n in range(1,m)}

def main():
    M=400
    Phi=phi_set(M)
    cap=[q for q in Phi if 0<q<1]
    print(f"Phi({M}): |Phi|={len(Phi)}, # in (0,1): {len(cap)}")
    if cap:
        mx=max(cap); mn=min(cap)
        print(f"  min={mn}, max={mx}, max~{float(mx):.6f}")
    # deciles
    dec=[0]*10
    for q in cap:
        i=int(float(q)*10)
        if i>9: i=9
        dec[i]+=1
    print("  deciles of (0,1):", dec)
    # maximum value and its (m,n): f monotone? find argmax
    best=(None,None,None)
    for m in range(2,M+1):
        for n in range(1,m):
            q=f_frac(m,n)
            if 0<q<1 and (best[0] is None or q>best[0]):
                best=(q,m,n)
    if best[0] is not None:
        print(f"  argmax over m<=M: q={best[0]}~{float(best[0]):.6f} at (m,n)=({best[1]},{best[2]})")
    # sup over all (m,n): f(m,n) -> as m/n large.  Let t=n/m, f=4t(1-t^2)/(1+t^2)^2.
    # max over t in (0,1): compute numerically
    import math
    bestt=0; bestf=0
    for i in range(1,100000):
        t=i/100000.0
        f=4*t*(1-t*t)/((1+t*t)**2)
        if f>bestf:
            bestf=f; bestt=t
    print(f"  sup f(m,n) over all real t=n/m in (0,1): {bestf:.6f} at t={bestt:.4f} "
          f"(so f<{bestf:.3f} for all m,n; clip q1+q2<1 is automatic if both < {bestf:.3f}? no: need q1+q2<1, implied only if q1+q2 <= 2*sup)")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Quantify the two sides separately: for pairs q1>q2 in Phi(M) with
q1+q2<1, count how often 1-(q1+q2) is a rational square and how often
1+(q1+q2) is a rational square.  Hypothesis to test: 1+(q1+q2) is NEVER
a rational square, while 1-(q1+q2) frequently is.
"""
import sys, time
from math import gcd, isqrt
from lib.phi import phi_pairs

def rat_square(num, den):
    g=gcd(num,den); num//=g; den//=g
    return num>0 and den>0 and isqrt(num)**2==num and isqrt(den)**2==den

def main():
    M=int(sys.argv[1]) if len(sys.argv)>1 else 200
    budget=float(sys.argv[2]) if len(sys.argv)>2 else 500.0
    t0=time.time()
    Phi=phi_pairs(M)
    pairs=sorted(Phi,key=lambda nd: nd[0]/nd[1])
    P=len(pairs)
    n=nsqmin=nsqplus=nboth=0
    plus_examples=[]
    for i in range(P):
        A1,B1=pairs[i]
        for j in range(i):
            A2,B2=pairs[j]
            num=A1*B2+A2*B1; den=B1*B2
            if num>=den: break
            n+=1
            ok_minus=rat_square(den-num,den)
            ok_plus=rat_square(den+num,den)
            if ok_minus: nsqmin+=1
            if ok_plus:
                nsqplus+=1
                if len(plus_examples)<5: plus_examples.append(((A1,B1),(A2,B2)))
            if ok_minus and ok_plus: nboth+=1
        if time.time()-t0>budget:
            print(f"[M={M}] budget at i={i}/{P}",flush=True)
            break
    print(f"M={M} |Phi|={P} pairs sum<1: {n}")
    print(f"  1-(q1+q2) rational square: {nsqmin}")
    print(f"  1+(q1+q2) rational square: {nsqplus}  {plus_examples}")
    print(f"  both: {nboth}")

if __name__=="__main__":
    main()

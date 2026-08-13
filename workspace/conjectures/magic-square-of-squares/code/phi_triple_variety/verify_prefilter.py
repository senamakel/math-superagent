#!/usr/bin/env python3
"""INDEPENDENT verification of the prefilter-survivor claim:
For primitive m<=M, count pairs q1>q2 in Phi, q1+q2<1, such that BOTH
1-(q1+q2) and 1+(q1+q2) are rational squares.  Uses only the original
definition of Phi (via f(m,n)) and the definition of rational square —
no reliance on the closed-form square test.  Fully exact.
"""
from math import gcd, isqrt

def rat_square(num, den):
    g = gcd(num, den)
    num //= g; den //= g
    return num>0 and den>0 and isqrt(num)**2==num and isqrt(den)**2==den

def phi(M):
    out = set()
    for m in range(2, M+1):
        m2=m*m
        for n in range(1,m):
            num=4*m*n*(m2-n*n)
            den=(m2+n*n)**2
            g=gcd(num,den)
            out.add((num//g,den//g))
    return out

def main():
    M = 80
    Phi = phi(M)
    pairs = sorted(Phi, key=lambda nd: nd[0]/nd[1])
    survivors = []
    n_with_sum_lt1 = 0
    pref_both = 0
    for i,(A1,B1) in enumerate(pairs):
        for j in range(i):
            A2,B2 = pairs[j]
            num=A1*B2+A2*B1; den=B1*B2
            if num>=den: break
            n_with_sum_lt1 += 1
            ok1 = rat_square(den-num, den)
            ok2 = rat_square(den+num, den)
            if ok1 and ok2:
                survivors.append(((A1,B1),(A2,B2),ok1,ok2))
                if len(survivors)<5: print("SURVIVOR", (A1,B1),(A2,B2))
                pref_both += 1
            elif ok1 or ok2:
                # exactly one side square: also worth knowing
                if len(survivors)<5: print("one-side", (A1,B1),(A2,B2),ok1,ok2)
    print(f"M={M}: |Phi|={len(Phi)}; pairs q1>q2 with q1+q2<1: {n_with_sum_lt1}")
    print(f"  both 1+/-sum rational squares: {pref_both}")
    print(f"  so sums passing necessary Phi-condition: {len(survivors)}")

if __name__=="__main__":
    main()

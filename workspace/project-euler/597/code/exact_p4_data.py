#!/usr/bin/env python3
"""Consolidated exact p(4,L) data: L=160,240,320,400 (captured earlier) plus
800..1800 (from agent). Fit rational function in m=L/40."""
from fractions import Fraction as F
from sympy import symbols, Eq, solve

DATA = {
    160: "7/15", 240: "187/378", 320: "1951/3861", 400: "521/1020",
    800: "54559/104895", 1000: "25382/48645", 1200: "68843/131670",
    1400: "677228/1293435", 1600: "57511/109725", 1800: "166802/317985",
}

if __name__ == "__main__":
    x = symbols('x')
    pairs = [(F(L)//40, F(DATA[L])) for L in DATA]
    pairs.sort()
    print(f"{len(pairs)} points:")
    for m, p in pairs:
        print(f"  m={m:3d}  p={p} = {float(p):.8f}")
    for (nn, dn) in [(2,2),(3,3),(3,2),(4,3)]:
        a = symbols(f'a0:{nn+1}')
        b = list(symbols(f'b0:{dn}')) + [1]
        nneed = nn+1+dn
        if len(pairs) < nneed:
            print(f"deg N={nn} D={dn}: need {nneed} pts, have {len(pairs)} -> skip")
            continue
        pts = pairs[:nneed]
        eqs=[]
        for (m,p) in pts:
            num=sum(a[i]*m**i for i in range(nn+1))
            den=sum(b[i]*m**i for i in range(dn+1))
            eqs.append(Eq(p*den,num))
        sol=solve(eqs, list(a)+list(b[:dn]), dict=True)
        for s in sol:
            A=[s.get(a[i],0) for i in range(nn+1)]
            B=[s.get(b[i],0) for i in range(dn)] + [1]
            ok=all(sum(A[i]*m**i for i in range(nn+1))/sum(B[i]*m**i for i in range(dn+1))==p for (m,p) in pairs)
            print(f"deg N={nn} D={dn}: exact-on-all={ok}")
            if ok:
                print(f"   N={[str(v) for v in A]}")
                print(f"   D={[str(v) for v in B]}")
                # limit
                from sympy import limit, oo, simplify
                lim = simplify(sum(A[i]*x**i for i in range(nn+1))/sum(B[i]*x**i for i in range(dn+1)))
                print(f"   limit x->inf = {limit(lim, x, oo)}")

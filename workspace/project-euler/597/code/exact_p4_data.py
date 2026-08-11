#!/usr/bin/env python3
"""Exact p(4,L) values captured from the n=4 arrangement enumeration.
L -> p(4,L), exact rational. (From the earlier JSON snapshot, pre-overwrite.)"""
DATA = {
    160: "7/15",
    240: "187/378",
    320: "1951/3861",
    400: "521/1020",
}

if __name__ == "__main__":
    from fractions import Fraction as F
    from sympy import symbols, Eq, solve
    x = symbols('x')
    pairs = [(F(L)//40, F(DATA[L])) for L in DATA]
    pairs.sort()
    for m, p in pairs:
        print(f"  m={m:3d}  p={p} = {float(p):.8f}")
    # try fit p4(m) = N/D degree (2,2), (3,3)
    for (nn, dn) in [(2,2),(3,3),(3,2),(4,3),(4,4)]:
        a = symbols(f'a0:{nn+1}')
        b = list(symbols(f'b0:{dn}')) + [1]
        pts = pairs[:nn+1+dn]
        if len(pts) < nn+1+dn: 
            print(f"(need {nn+1+dn} pts, have {len(pairs)}): skip")
            continue
        eqs = []
        for (m,p) in pts:
            num = sum(a[i]*m**i for i in range(nn+1))
            den = sum(b[i]*m**i for i in range(dn+1))
            eqs.append(Eq(p*den, num))
        sol = solve(eqs, list(a)+list(b[:dn]), dict=True)
        for s in sol:
            A=[s.get(a[i],0) for i in range(nn+1)]
            B=[s.get(b[i],0) for i in range(dn)] + [1]
            ok=all(sum(A[i]*m**i for i in range(nn+1))/sum(B[i]*m**i for i in range(dn+1))==p for (m,p) in pairs)
            print(f"deg N={nn} D={dn}: exact-on-all={ok}; N={[str(v) for v in A]} D={[str(v) for v in B]}")

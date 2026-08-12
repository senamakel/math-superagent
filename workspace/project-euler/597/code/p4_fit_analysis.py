#!/usr/bin/env python3
"""Fit p(4,L) as a rational function of m = L/40 and analyse p(n,L) sequences.

p3 is known to be (7m^2-17m+12)/(18m^2-45m+27). Does p4(m) fit a low-degree
rational function in m? We have 22 exact p(4,L) points. Try degrees up to 5/5
and report the smallest that fits ALL points exactly.
"""
from fractions import Fraction as F
from sympy import symbols, Eq, solve

# exact p(4,L): (L, "num/den")
P4 = {
    160: "7/15", 240: "187/378", 320: "1951/3861", 400: "521/1020",
    480: "3077/5985", 560: "16033/31050", 640: "2839/5481",
    800: "54559/104895", 900: "143561/275520", 1000: "25382/48645",
    1100: "2493559/4773600", 1200: "68843/131670", 1300: "474941/907680",
    1400: "677228/1293435", 1500: "2249593/4294080", 1600: "57511/109725",
    1800: "166802/317985", 2000: "1044769/1990440", 2500: "3723481/7085760",
    3000: "2454796/4667985", 4000: "990791/1882335", 5000: "35280338/66990105",
}

pts = sorted((F(L, 40), F(val)) for L, val in P4.items())
print(f"{len(pts)} exact p(4,L) points (m=L/40, fractional p):")
for m, p in pts:
    print(f"  m={m}  p={p}  = {float(p):.8f}")

def fit_all(nn, dn):
    """Return (A,B,ok) fitting p = N/D with deg N=nn deg D=dn, D monic (B_dn=1)."""
    nneed = (nn+1) + dn
    pts_f = pts[:nneed]
    a = symbols(f'a0:{nn+1}')
    b = list(symbols(f'b0:{dn}')) + [1]
    eqs = []
    for (m, p) in pts_f:
        num = sum(a[i]*m**i for i in range(nn+1))
        den = sum(b[i]*m**i for i in range(dn+1))
        eqs.append(Eq(p*den - num, 0))
    sol = solve(eqs, list(a)+list(b[:dn]), dict=True)
    results = []
    for s in sol:
        A = [s.get(a[i], 0) for i in range(nn+1)]
        B = [s.get(b[i], 0) for i in range(dn)] + [1]
        ok_all = True
        for (m, p) in pts:
            num = sum(A[i]*m**i for i in range(nn+1))
            den = sum(B[i]*m**i for i in range(dn+1))
            if den != 0 and F(num)/F(den) != p:
                ok_all = False
                break
        results.append((ok_all, A, B))
    return results

found = None
for total_deg in range(2, 11):
    for nn in range(0, total_deg+1):
        dn = total_deg - nn
        if (nn+1) + dn > len(pts): continue
        try:
            res = fit_all(nn, dn)
        except Exception:
            continue
        for (ok, A, B) in res:
            if ok:
                print(f"\nFIT OK: deg N={nn} deg D={dn} exact on ALL {len(pts)} points")
                print("  N coeffs (m^0..):", [str(x) for x in A])
                print("  D coeffs (m^0..):", [str(x) for x in B])
                found = (nn, dn, A, B)
                break
        if found: break
    if found: break

if not found:
    print("\nNo rational fit of degree <=10 (or could not solve).")

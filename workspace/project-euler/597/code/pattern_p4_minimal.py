#!/usr/bin/env python3
"""1) Confirm degree-3/3 is MINIMAL for p(4,L) over all 31 exact points.
2) Extract the L->inf (pure-bump) limit sequence from exact rational fits:
     n=2 -> 1/2 (proven)
     n=3 -> 7/18 (verified)
     n=4 -> ratio of leading coeffs of the 3/3 fit
3) Run the exact rational-fit checker to prove 3/3 minimality over all points.
"""
from fractions import Fraction as F
from sympy import symbols, Eq, solve

P4 = {
    160: "7/15", 240: "187/378", 320: "1951/3861", 400: "521/1020",
    480: "3077/5985", 560: "16033/31050", 640: "2839/5481",
    800: "54559/104895", 900: "143561/275520", 1000: "25382/48645",
    1100: "2493559/4773600", 1200: "68843/131670", 1300: "474941/907680",
    1400: "677228/1293435", 1500: "2249593/4294080", 1600: "57511/109725",
    1800: "166802/317985", 2000: "1044769/1990440", 2100: "6490703/12362400",
    2300: "25860019/49230720", 2500: "3723481/7085760", 2700: "1575557/2997280",
    2900: "53060149/100910880", 3000: "2454796/4667985", 3400: "1203242/2287065",
    3800: "15239168/28956015", 4000: "990791/1882335", 4200: "6902786/13112415",
    4600: "3038972/5771475", 4800: "5191253/9858015", 5000: "35280338/66990105",
}
pts = sorted((F(L, 40), F(v)) for L, v in P4.items())
print(f"{len(pts)} exact p(4,L) points (m=L/40)")

def fit_all(nn, dn, pts):
    """Return list of (ok, A, B) fitting p=N/D, deg N=nn deg D=dn, D monic."""
    nneed = (nn+1) + dn
    if nneed > len(pts):
        return []
    pts_f = pts[:nneed]
    a = symbols(f'a0:{nn+1}')
    b = list(symbols(f'b0:{dn}')) + [1]
    eqs = []
    for (m, p) in pts_f:
        num = sum(a[i]*m**i for i in range(nn+1))
        den = sum(b[i]*m**i for i in range(dn+1))
        eqs.append(Eq(p*den - num, 0))
    sol = solve(eqs, list(a)+list(b[:dn]), dict=True)
    out = []
    for s in sol:
        A = [F(s.get(a[i], 0)) for i in range(nn+1)]
        B = [F(s.get(b[i], 0)) for i in range(dn)] + [F(1)]
        ok = all(sum(A[i]*m**i for i in range(nn+1)) /
                 sum(B[i]*m**i for i in range(dn+1)) == p for (m, p) in pts)
        out.append((ok, A, B))
    return out

print("\nMinimality scan over ALL 31 points (total degree up to 6):")
best = None
for total in range(2, 7):
    for nn in range(1, total+1):
        dn = total - nn
        for (ok, A, B) in fit_all(nn, dn, pts):
            if ok:
                lim = A[nn]/B[dn]
                print(f"  deg N={nn} D={dn}: EXACT on all {len(pts)} pts, limit={lim} = {float(lim):.8f}")
                if best is None or (nn+dn) < best[0]:
                    best = (nn+dn, nn, dn, lim)
if best:
    print(f"\nSmallest total degree = {best[0]} (N={best[1]}, D={best[2]}), L->inf limit = {best[3]}")

print("\nPure-bump (L->inf) limit sequence:")
print("  n=2:", float(F(1,2)))
print("  n=3:", float(F(7,18)))
print("  n=4:", float(best[3]))

"""Holonomic / gfun-style guessing for A_n and B_n (exact arithmetic).

For a sequence a_k (k=0..N-1), look for a recurrence
    sum_{j=0}^{d} P_j(k) a_{k+j} = 0,   P_j(k) = sum_{t=0}^{m} c_{j,t} k^t
with d = order, m = polynomial degree in k.  Unknowns: (m+1)(d+1).
Equations: k = 0..N-1-d  (residuals at each k).

We report, for each (d,m):
  - dimension of the exact nullspace over Q (Rational arithmetic, sympy)
  - whether the recurrence is pinned down (nullspace dim 1)
  - the predicted value of the last term from a fit on all earlier terms
    (leave-last-out), to see how many terms the fit really describes.

Only fits that use every available term are 'candidates'; a fit that also
predicts the left-out last term correctly over the FULL range of equations
is a 'verified' candidate (given the data we have).
"""
import sympy as sp
from sympy import Rational, symbols, Matrix, Poly

def terms_to_rat(ts):
    return [Rational(t) for t in ts]

def recurrence_search(name, vals, max_order=5, max_deg=4, floor_deg=0):
    N = len(vals)
    a = terms_to_rat(vals)
    k = symbols('k')
    print(f"\n===== {name}: N={N} terms, indices k=0..{N-1} =====")
    for d in range(1, max_order+1):
        if d >= N: break
        for m in range(floor_deg, max_deg+1):
            # unknowns
            c = [[symbols(f'c_{j}_{t}') for t in range(m+1)] for j in range(d+1)]
            # build equations for k = 0..N-1-d
            rows = []
            for kk in range(0, N-d):
                row = [Rational(0)]*((m+1)*(d+1))
                for j in range(d+1):
                    if kk+j >= N: continue
                    for t in range(m+1):
                        row[(j)*(m+1)+t] += Rational(kk)**t * a[kk+j] * (-1 if False else Rational(1))
                        # coefficient of c_{j,t} in eq kk: (kk)^t * a[kk+j]
                rows.append(row)
            M = Matrix(rows)
            ns = M.nullspace()
            dim = len(ns)
            # candidate: at least one nonzero sol; report those with dim==1
            tag = ""
            if dim == 0:
                tag = "no recurrence of this order/deg"
            elif dim > 1:
                tag = f"nullspace dim={dim} -> underdetermined, skip"
            if dim == 1:
                vec = ns[0]
                # normalize: make the leading nonzero coeff = 1
                idx = next(i for i,v in enumerate(vec) if v != 0)
                vec = [v/vec[idx] for v in vec]
                # print compactly
                def pol(j):
                    coeffs = [vec[j*(m+1)+t] for t in range(m+1)]
                    return Poly(coeffs, k).as_expr()
                rec = " + ".join(f"({sp.expand(pol(j))})*a_{{k+{j}}}" for j in range(d+1))
                # leave-last-out check: refit using terms k=0..N-2 (a[0..N-2])
                # equations k = 0..N-2-d  (still need a[k+j] <= a[N-2])
                rows2 = []
                for kk in range(0, N-1-d):
                    row = [Rational(0)]*((m+1)*(d+1))
                    for j in range(d+1):
                        if kk+j >= N-1: continue
                        for t in range(m+1):
                            row[(j)*(m+1)+t] += Rational(kk)**t * a[kk+j]
                    rows2.append(row)
                M2 = Matrix(rows2)
                ns2 = M2.nullspace()
                pred = None
                if len(ns2) == 1:
                    vec2 = ns2[0]
                    ii = next(i for i,v in enumerate(vec2) if v != 0)
                    vec2 = [v/vec2[ii] for v in vec2]
                    # evaluate recurrence at k = N-1-d:  sum_j P_j(N-1-d) a[N-1-d+j] = 0
                    kk = N-1-d
                    # solve for a[N-1] = a[kk+d]
                    coef_last = sum((Rational(kk)**t)*vec2[d*(m+1)+t] for t in range(m+1))
                    rest = sum(
                        sum((Rational(kk)**t)*vec2[j*(m+1)+t] for t in range(m+1)) * a[kk+j]
                        for j in range(d))
                    if coef_last != 0:
                        pred = -rest/coef_last
                tag = f"FIT (dim=1)"
                if pred is not None:
                    ok = (pred == a[N-1])
                    tag += f" | leave-last-out predict a[{N-1}]={a[N-1]} -> pred={pred} {'MATCH' if ok else 'mismatch'}"
            # only print fits and interesting cases; suppress underdetermined noise
            if dim == 1 or (dim > 1 and m == floor_deg and d <= 2):
                if dim == 1:
                    print(f"  d={d}, m={m}: {tag}")
                    if m <= 3:
                        print(f"      recurrence: {rec}")
            elif dim == 0:
                print(f"  d={d}, m={m}: {tag}")

A = [1, 10, 184, 5052, 191232, 9851040, 650626560, 54052427520, 5514150297600, 680309947699200]
B = [1, 0, -108, -3600, -208800, -12418560, -932601600, -85305830400, -9900701798400]
AB = [abs(b) for b in B]

recurrence_search("A_n (n=2..11)", A, max_order=4, max_deg=4)
recurrence_search("|B_n| (n=3..11)", AB, max_order=4, max_deg=4)
"""Clean holonomic (polynomial-coefficient) recurrence guesser.

Look for recurrences  sum_{j=0}^{d} P_j(k) a_{k+j} = 0  where k indexes the
sequence a_0..a_{N-1}, P_j polynomial in k of degree <= m with SMALL integer
coefficients.  We search coefficient space up to a small bound by solving the
linear system over the integers exactly (Hermite normal form via sympy) and
reading off a small-basis solution; then verify on all terms and, for the
strongest test, solve for the last term using only the earlier terms.

For each (d,m): build equations from ALL terms, take integer nullspace,
and if a null vector with small coefficients exists, report it and test.
"""
import itertools
from fractions import Fraction as F
import sympy as sp
from sympy import symbols, Matrix, ZZ

def small_nullspace(A, maxnorm=None, skip_zero_col=True):
    """Find a null vector of integer matrix A with small coeffs."""
    M = Matrix(A)
    # nullspace over QQ
    ns = M.nullspace()
    for v in ns:
        # clear denominators -> primitive integer vector
        dens = [x.q for x in v]
        from math import gcd
        from functools import reduce
        l = 1
        for d in dens: l = l*d//gcd(l,d)
        iv = [x*l for x in v]
        g = 0
        for x in iv: g = gcd(g, abs(int(x)))
        iv = [int(x)//g for x in iv]
        # shift so last nonzero coeff index is the k-max term? We keep as is.
        yield iv

def guess(name, vals, max_order=4, max_deg=3, coeff_bound=None):
    N = len(vals)
    a = [F(v) for v in vals]
    print(f"\n===== {name}: N={N} =====")
    for d in range(1, max_order+1):
        if d >= N: break
        for m in range(0, max_deg+1):
            ncoef = (m+1)*(d+1)
            # equations for k=0..N-1-d
            neq = N-d
            rows=[]
            for kk in range(neq):
                row=[F(0)]*ncoef
                for j in range(d+1):
                    idx=j*(m+1)
                    for t in range(m+1):
                        row[idx+t] += F(kk)**t * a[kk+j]
                rows.append(row)
            # find small integer null vectors
            found = False
            for nv in small_nullspace(rows):
                # convert nv to coeff list c[j][t]
                c = [[nv[j*(m+1)+t] for t in range(m+1)] for j in range(d+1)]
                # report only if coefficients not already covered by huge
                maxc = max(abs(x) for x in nv)
                if coeff_bound and maxc > coeff_bound:
                    continue
                found = True
                # leave-last-out: predict a[N-1] at k=N-1-d
                kk = N-1-d
                coef_last = sum(c[d][t]*kk**t for t in range(m+1))
                if coef_last != 0:
                    rest = sum(
                        (sum(c[j][t]*kk**t for t in range(m+1)))*a[kk+j]
                        for j in range(d))
                    pred = -rest/coef_last
                    ok = (pred == a[N-1])
                    tag = f"LLO predict a[{N-1}]: pred={pred} vs {a[N-1]} "+("MATCH" if ok else "mismatch")
                else:
                    tag = "last coeff zero, cannot solve"
                # print recurrence compactly
                def P(j):
                    return "+".join(f"{c[j][t]}k^{t}" if t>0 else f"{c[j][t]}" for t in range(m+1))
                rec = "  ".join(f"({P(j)})a[k+{j}]" for j in range(d+1))
                print(f"  d={d} m={m}: coeff max={maxc} | {tag}\n      rec: {rec} = 0")
            if not found:
                # detect whether ANY solution exists
                M=Matrix(rows)
                if len(M.nullspace())>0:
                    print(f"  d={d} m={m}: has rational solutions but none small (coeff_bound={coeff_bound})")

# data
A = [1,10,184,5052,191232,9851040,650626560,54052427520,5514150297600,680309947699200]
B = [1,0,-108,-3600,-208800,-12418560,-932601600,-85305830400,-9900701798400]
AB = [abs(x) for x in B]

guess("A_n (n=2..11, k=0..9)", A, max_order=3, max_deg=2, coeff_bound=10**6)
guess("|B_n| (n=3..11, k=0..8)", AB, max_order=3, max_deg=2, coeff_bound=10**6)
guess("c_n=|B|/(n-1)! n=6..11", [30,290,2464,23130,235080,2728368],
      max_order=3, max_deg=2, coeff_bound=10**4)

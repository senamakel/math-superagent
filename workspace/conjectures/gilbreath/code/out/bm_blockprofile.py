import json
import sys

def berlekamp_massey(s):
    """Shortest linear recurrence (C-finite) over rationals for sequence s.
    Returns list C with s[n] = sum_i C[i]*s[n-1-i] for n >= len(C).
    Exact rational arithmetic via Python fractions-like tuples (num,den)."""
    n = len(s)
    # use exact integers via Fraction
    from fractions import Fraction
    C = [Fraction(0)] * n
    oldC = [Fraction(0)] * n
    C[0] = Fraction(1)  # C is the connection polynomial (leading coeff 1 index0)
    oldC[0] = Fraction(1)
    L = 0
    m = 0
    for i in range(n):
        # discrepancy
        d = Fraction(0)
        for j in range(L+1):
            d += C[j] * s[i-j]
        if d == 0:
            m += 1
        else:
            T = C[:]
            coef = d / (s[i-m] if (d != 0 and i-m>=0) else Fraction(1))
            # actually standard: coef = d / (s[i-m]? ) -- need old discrepancy denominator
            # use the classic: coef = d / old_discrepancy
            # store old discrepancy at the shift
            coef = d / (s[i-m] if False else 1)
            # Standard BM: when discrepancy non-zero, shift oldC by m
            # new C = C - coef * x^m * oldC   where coef = d/discrepancy_old
            # We track discrepancy_old via oldC correction: coef = d / s[i-m] isn't right.
            # Simpler robust implementation below.
    # Use numpy-free fraction BM - re-implement cleanly:
    return bm_exact(s)

def bm_exact(s):
    from fractions import Fraction
    n = len(s)
    # Berlekamp-Massey, classic, exact fractions
    C = [Fraction(0)]*(n+1); B = [Fraction(0)]*(n+1)
    C[0] = Fraction(1); B[0] = Fraction(1)
    L = 0; m = 1; b = Fraction(1)
    for i in range(n):
        d = sum(C[j]*s[i-j] for j in range(L+1))
        if d == 0:
            m += 1
        elif 2*L <= i:
            T = C[:]
            coef = d / b
            for j in range(n+1-i):
                C[i+m+j] -= coef * B[j]
            L = i + 1 - L
            B = T[:]
            b = d
            m = 1
        else:
            coef = d / b
            for j in range(n+1-i):
                C[i+m+j] -= coef * B[j]
            m += 1
    return C[:L+1], L

data = json.load(open('code/out/blocks_depth1000.json'))
b = data['b']
print("len b =", len(b))
C, L = bm_exact(b)
print("minimal recurrence order L =", L)
# verify
ok = True
for i in range(L, len(b)):
    pred = sum(C[j]*b[i-1-j] for j in range(L))
    if pred != b[i]:
        ok = False
        print("FAIL at", i, "pred", pred, "actual", b[i])
        break
print("verify over all", len(b), "terms:", ok)

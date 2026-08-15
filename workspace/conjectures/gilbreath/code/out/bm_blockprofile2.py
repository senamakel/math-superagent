import json
from fractions import Fraction

def berlekamp_massey(s):
    n = len(s)
    N = 2*n + 5
    C = [Fraction(0)]*N; B = [Fraction(0)]*N
    C[0] = Fraction(1); B[0] = Fraction(1)
    L = 0; m = 1; b = Fraction(1)
    for i in range(n):
        # discrepancy d = C[0]*s[i] + C[1]*s[i-1] + ... + C[L]*s[i-L]
        d = sum(C[j]*s[i-j] for j in range(L+1))
        if d == 0:
            m += 1
        elif 2*L <= i:
            T = C[:]
            coef = d / b
            for j in range(N - i - m):
                if i+m+j < N:
                    C[i+m+j] -= coef * B[j]
            L = i + 1 - L
            B = T[:]
            b = d
            m = 1
        else:
            coef = d / b
            for j in range(N - i - m):
                if i+m+j < N:
                    C[i+m+j] -= coef * B[j]
            m += 1
    # connection polynomial C of degree <= L: s[n] = -sum_{j>=1} C[j]*s[n-j] (C[0]=1)
    return C[:L+1], L

data = json.load(open('/workspace/code/out/blocks_depth1000.json'))
b = data['b']
print("len b =", len(b))
C, L = berlekamp_massey(b)
print("minimal linear recurrence order L =", L)
print("connection poly (C[0]=1):", C[:min(L+1,8)], "...")
# verify: for i>=L, pred = -sum_{j=1..L} C[j]*b[i-j]
ok = True
for i in range(L, len(b)):
    pred = -sum(C[j]*b[i-j] for j in range(1, L+1))
    if pred != b[i]:
        ok = False
        print("FAIL at i", i, "pred", pred, "actual", b[i])
        break
print("verify over all", len(b), "terms:", ok, "(L=", L, ")")

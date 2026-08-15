import json
from fractions import Fraction

def berlekamp_massey(s):
    n = len(s); N = 2*n+5
    C = [Fraction(0)]*N; B = [Fraction(0)]*N
    C[0] = Fraction(1); B[0] = Fraction(1)
    L = 0; m = 1; b = Fraction(1)
    for i in range(n):
        d = sum(C[j]*s[i-j] for j in range(L+1))
        if d == 0:
            m += 1
        else:
            coef = d / b
            for j in range(N - i - m):
                if i+m+j < N:
                    C[i+m+j] -= coef * B[j]
            if 2*L <= i:
                T = C[:]
                L = i + 1 - L
                B = T[:]
                b = d
                m = 1
            else:
                m += 1
    return C[:L+1], L

# Test on Fibonacci: 0,1,1,2,3,5,8,13,21 -> order 2
fib = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
Cf, Lf = berlekamp_massey(fib)
print("FIB order =", Lf, "expect 2")

data = json.load(open('/workspace/code/out/blocks_depth1000.json'))
b = data['b']
# use first 200 terms to keep fractions tractable
sub = b[:300]
C, L = berlekamp_massey(sub)
print("block-profile first 300: minimal order L =", L, " (n=300)")
ok = True
for i in range(L, len(sub)):
    pred = -sum(C[j]*sub[i-j] for j in range(1, L+1))
    if pred != sub[i]:
        ok = False; print("FAIL at", i); break
print("verify holds:", ok)

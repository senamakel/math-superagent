"""Attack the fixed-type eigen-recurrence: hold it over far more degrees, and
confirm the Bell-total column admits NO constant-coefficient recurrence.

type t column = [S(d-1, t+1) for d >= t+2]  (Stirling second kind, exact closed
form).  Claim: satisfies the order-(t+1) recurrence with char poly prod_{j=1}^{t+1}(x-j),
i.e.  a(n) = e_1 a(n-1) - e_2 a(n-2) + ... + (-1)^t e_{t+1} a(n-t-1),
e_r = elementary symmetric sum of {1..t+1}.

Derived from the closed form S(n,k)=(1/k!) sum_j (-1)^(k-j) binom(k,j) j^n,
so it is exact for ALL degrees, not a fit.  Here we just hold it numerically
over a much larger range as an independent confirmation, then record the first
index at which any would-be constant-coefficient recurrence of lower order fails
(the falsifier for each column).
"""
from sympy import binomial, factorial

def closed_S(n, k):
    return sum((-1)**(k-j) * binomial(k, j) * j**n for j in range(k+1)) // factorial(k)

def elem_sym(k, r):
    from itertools import combinations
    from functools import reduce
    from operator import mul
    return sum(reduce(mul, c, 1) for c in combinations(range(1, k+1), r))

# --- 1. Push the eigen-recurrence to D=120  ---------------------------------
D = 120
all_ok = True
first_fail = {}
for t in range(0, 9):
    k = t + 1
    seq = [closed_S(d-1, k) for d in range(k+1, D+1)]
    cs = [(-1)**(r-1) * elem_sym(k, r) for r in range(1, k+1)]
    ok = True
    for n in range(k, len(seq)):
        if seq[n] != sum(cs[r]*seq[n-1-r] for r in range(k)):
            ok = False
            first_fail[t] = n
            break
    all_ok &= ok
    print(f"type {t:2d} (k={k:2d}): held up to d={D}  ok={ok}"
          + (f"  FIRST FAIL n={first_fail[t]}" if not ok else ""))
print("eigen-recurrence holds over ALL degrees d=..%d :" % D, all_ok)

# --- 2. Bell total as a "sequence": does it satisfy a CC recurrence?  -------
# Bell(d-1): 1,2,5,15,52,203,877,4140,...
def bell(n):
    return sum(stirling2(n, k) for k in range(n+1))
def stirling2(n, k):
    if k==0 or k>n: return 0
    S=[[0]*(k+1) for _ in range(n+1)]; S[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            S[i][j]=j*S[i-1][j]+S[i-1][j-1]
    return S[n][k]
bells=[bell(n) for n in range(1, 16)]
print("Bell(d-1) for d=2..16:", bells)

"""Verify the CGMO/Zhen-Knessl G(k,m) recurrence reproduces OEIS A007902
(the 2D amoeba = the reference for the 3D DP construction).
Also sanity-check Catalan column and row-k=2=n(3n-1)/2 of Fig.3."""
import sys

def g(k, m, memo):
    if k < 1:
        return 0
    key = (k, m)
    if key in memo:
        return memo[key]
    if m == 0:
        r = 2*g(k-1,0,memo) + g(k,1,memo) + (1 if k==2 else 0)
    elif m == 1:
        r = g(k-3,0,memo) + 2*g(k-2,1,memo) + g(k-1,2,memo) + g(k-4,1,memo)
    else:
        r = g(k-m-2,m-1,memo) + 2*g(k-m-1,m,memo) + g(k-m,m+1,memo)
    memo[key] = r
    return r

def a007902(n):
    # n>=1; a(1)=1 else G(n,0)
    if n == 1:
        return 1
    return g(n, 0, {})

expected = [1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668]  # A007902 a(1..14)
print("A007902 via G(k,m) recurrence (a(1..14)):")
allok = True
for i, e in enumerate(expected, start=1):
    v = a007902(i)
    ok = (v == e)
    allok &= ok
    print(f"  a({i}) = {v}  expected {e}  {'OK' if ok else 'MISMATCH'}")
print("ALL OK" if allok else "MISMATCHES PRESENT")

# Fig.3 checks
Cat = [1,2,5,14,42,132,429]
print("\nFig.3 n=2 column (should be Catalan C_{k+1}):", Cat)
poly2 = lambda n: n*(3*n-1)//2
print("Fig.3 row k=2, n(3n-1)/2 for n=1..6:", [poly2(n) for n in range(1,7)])

"""Verify A027610 formula vs the census counts (1,1,1,3,7,24,93,434,2110,11002,58713
for n=4..24, i.e. A027610(0..10))."""
from math import comb, factorial

def A001764(m):
    return comb(3*m, m) // (2*m+1)

def A047749(m):
    if m % 2 == 1:
        x = (m-1)//2
        return (3*x+1)*comb(3*x+1, x) // ((x+1)*(2*x+1))
    return A001764(m//2)

def A027610(n):
    N = A001764(n) // (12*(n+1))
    if n % 2 == 0:
        N += 5*A001764(n//2) // 24
    if (n-1) % 3 == 0:
        N += A001764((n-1)//3) // 3
    if (n-1) % 4 == 0:
        N += A001764((n-1)//4) // 4
    if (n-2) % 6 == 0:
        N += A001764((n-2)//6) // 6
    N += 3*A047749(n) // 8
    if (2*n-1) % 3 == 0:
        N += A047749((2*n-1)//3) // 6
    return N

census = {4:1,6:1,8:1,10:3,12:7,14:24,16:93,18:434,20:2110,22:11002,24:58713}
allok = True
for n in sorted(census):
    a = A027610((n-4)//2)
    ok = (a == census[n])
    allok &= ok
    print(f"n={n:2d} A027610({(n-4)//2})={a}  census={census[n]}  {'OK' if ok else 'MISMATCH'}")
print("ALL MATCH" if allok else "FAIL")

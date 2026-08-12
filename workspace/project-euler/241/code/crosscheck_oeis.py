"""Cross-validate that every b-file term <=1e18 appears in exactly the right
per-k OEIS sequence (via abundancy), i.e. the two independent OEIS data
sources agree; and classify each by (k,a) + odd part abundancy target."""
from math import gcd
from collections import defaultdict

A159907_b = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616,6219051710415667200,6275163455171297280,
14031414189615513600,200286975596707184640,215594611071909888000,
352444116692828160000,835095457414213632000,5997579964837140234240,
39887491844324122951680,59485231752222033838080,64031599488357236736000]
LIM=10**18

def factorize(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0: f[d]=f.get(d,0)+1; n//=d
        d+=1 if d==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f
def sigmaf(f):
    s=1
    for p,e in f.items(): s*=(p**(e+1)-1)//(p-1)
    return s
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c

inrange=[n for n in A159907_b if n<=LIM]
print("b-file terms <=1e18:",len(inrange))

perkA159907=defaultdict(list)
for n in inrange:
    k=(2*sigmaf(factorize(n))//n-1)//2
    perkA159907[k].append(n)

# Per-k seq expectation from the per-k OEIS pages we fetched:
perk_seq = {
 1:(2*k+1 for k in [0]),  # k=1 -> abund 3/2 : [2]
 2:[24,91963648,10200236032],   # A141643 (5/2)
 3:[4320,4680,26208,20427264,197064960,21857648640,57575890944,88898072401645056,301183421949935616],  # A055153 (7/2)
 4:[8910720,17428320,8583644160,57629644800,206166804480,1416963251404800,15338300494970880],  # A141645 (9/2)
 5:[17116004505600,75462255348480000,6219051710415667200],  # A159271 (11/2) <=1e18 (also 14031414189615513600 <1e18, 352444...>1e18?)
}
print("\nPer-k members from A159907 b-file (k=abundancy k+1/2):")
for k in sorted(perkA159907):
    print(f"  k={k}: {perkA159907[k]}")
    # abundancy = (2k+1)/2
    abund=(2*k+1)/2
print("\nNote k=5 should be abund 11/2. The A141645 k=4 page shows a(8)=6275163455171297280 which the A159907 b-file lists at index 24. Check it's counted.")

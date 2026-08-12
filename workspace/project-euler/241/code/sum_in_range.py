"""Sum all A159907 (hemiperfect) terms <= 10^18 from the OEIS b-file,
and validate the 2-adic reduction identity on every term in range."""
from math import gcd

# terms from research/sources/A159907_bterm.full.md
bterms = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616,6219051710415667200,6275163455171297280,
14031414189615513600,200286975596707184640,215594611071909888000,
352444116692828160000,835095457414213632000,5997579964837140234240,
39887491844324122951680,59485231752222033838080,64031599488357236736000]

LIM = 10**18

def factorize(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            f[d] = f.get(d,0)+1
            n//=d
        d += 1 if d==2 else 2
    if n>1: f[n]=f.get(n,0)+1
    return f

def sigma_from_factors(f):
    s=1
    for p,e in f.items():
        s*= (p**(e+1)-1)//(p-1)
    return s

def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c

# sorted ascending check
assert bterms == sorted(bterms), "b-file not ascending"

inrange = [n for n in bterms if n <= LIM]
print("terms <= 1e18:", len(inrange))
print(inrange)
print("sum =", sum(inrange))

# verify 2-adic identity for every in-range term
all_ok=True
for n in inrange:
    f=factorize(n); s=sigma_from_factors(f)
    k=(2*s//n-1)//2
    a=v2(n); u=n>>a
    su=sigma_from_factors(factorize(u))
    g1=gcd(su,u); num,den=su//g1,u//g1
    tnum=(2*k+1)*(1<<(a-1)); tden=(1<<(a+1))-1
    g2=gcd(tnum,tden); tnum,tden=tnum//g2,tden//g2
    ok=(num==tnum and den==tden) and (v2(su)==a-1)
    all_ok &= ok
print("2-adic identity holds for all in-range terms:", all_ok)

# which per-k do they belong to
from collections import defaultdict
perk=defaultdict(list)
for n in inrange:
    f=factorize(n); s=sigma_from_factors(f)
    k=(2*s//n-1)//2
    perk[k].append(n)
for k in sorted(perk):
    print(f"  k={k}: {len(perk[k])} terms <=1e18, sum={sum(perk[k])}")
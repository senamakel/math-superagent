"""Compute the PE241 answer set and sum: A159907 terms <= 1e18.

Also per-abundancy grouping and 2-adic data for the pattern report.
"""
from math import gcd
from collections import defaultdict

# A159907 b-file terms (from research/sources/A159907_bterm.full.md)
bterms = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616,6219051710415667200,6275163455171297280,
14031414189615513600,200286975596707184640,215594611071909888000,
352444116692828160000,835095457414213632000,5997579964837140234240,
39887491844324122951680,59485231752222033838080,64031599488357236736000]

LIM = 10**18

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

inrange=[n for n in bterms if n<=LIM]
print("num terms <=1e18:", len(inrange))
print("set:", inrange)
print("SUM =", sum(inrange))

perk=defaultdict(list)
for n in inrange:
    k=(2*sigmaf(factorize(n))//n-1)//2
    perk[k].append(n)
print("\nper-k counts:", {k:len(v) for k,v in sorted(perk.items())})
for k in sorted(perk):
    print(f"  k={k} (abund {2*k+1}/2): {perk[k]}  sum={sum(perk[k])}")

print("\nper-k partial sums:")
running=0
for k in sorted(perk):
    running+=sum(perk[k])
    print(f"  up to k={k}: {running}")

# 2-adic a=v2(n) per term
print("\nn: a=v2(n), odd part u")
for n in inrange:
    a=v2(n)
    print(f"  {n:>21} a={a}")

# per-(k,a) odd-part abundancy targets
print("\nper (k,a): odd-part target")
for k in sorted(perk):
    for n in perk[k]:
        a=v2(n); u=n>>a
        tnum=(2*k+1)*(1<<(a-1)); tden=(1<<(a+1))-1
        print(f"  k={k} a={a} n={n} u={u} target={tnum}/{tden}")

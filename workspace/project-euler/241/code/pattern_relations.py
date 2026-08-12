"""Look for multiplicative / structural regularity among the 22 hemiperfects.
The sequence itself has no constant-coefficient recurrence (checked). Here we
test the specific hypothesis: some qualifying n are products of a 'base' odd
part and powers of small primes, and consecutive/related terms share factors.

We dump:
  - ratios of consecutive sorted terms (gcmmed)
  - the odd-part abundancy target sigma(u)/u for each (k,a) group, as a
    reduced rational -> this is the sequence the DFS must hit per (k,a)
  - per-(k,a) the smallest odd u achieving each target (the seed)
"""
from math import gcd
from collections import defaultdict

B = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
     8583644160,10200236032,21857648640,57575890944,57629644800,
     206166804480,17116004505600,1416963251404800,15338300494970880,
     75462255348480000,88898072401645056,301183421949935616]

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

print("Consecutive-term ratios (gcd-reduced b/a):")
for i in range(1,len(B)):
    a,b=B[i-1],B[i]
    g=gcd(a,b)
    print(f"  {a} -> {b}:  ratio={b//g}/{a//g}  shared_gcd={g}")
    print(f"      factor to multiply = {b//a:g}" if b%a==0 else f"      b/a={b/a:.6f}")

print("\nPer (k,a): odd-part abundancy target and the odd u achieving it:")
perka=defaultdict(list)
for n in B:
    f=factorize(n); s=sigmaf(f)
    k=(2*s//n-1)//2
    a=v2(n); u=n>>a
    su=sigmaf(factorize(u))
    g=gcd(su,u); num,den=su//g,u//g
    perka[(k,a)].append((n,u,num,den))
for (k,a) in sorted(perka):
    entries=perka[(k,a)]
    t=str(entries[0][2])+'/'+str(entries[0][3])
    print(f"  k={k} a={a} target={t}: "+"; ".join(f"n={n}(u={u})" for n,u,_,_ in entries))

# the DFS odd-part targets, sorted, as a sequence of floats -> any clean growth?
print("\nAll distinct odd-part targets (reduced), with a= parameter:")
seen=set()
for n in B:
    f=factorize(n); s=sigmaf(f)
    k=(2*s//n-1)//2
    a=v2(n); u=n>>a
    su=sigmaf(factorize(u)); g=gcd(su,u)
    num,den=su//g,u//g
    if (num,den) not in seen:
        seen.add((num,den))
        print(f"  a={a} k={k}: {num}/{den}  ({num/den:.6f})")

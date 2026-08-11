import itertools, math
from fractions import Fraction
from collections import defaultdict

def order(perm):
    n=len(perm);seen=[False]*n;d=1
    for s in range(n):
        if not seen[s]:
            c=s;cnt=0
            while not seen[c]: seen[c]=True;c=perm[c];cnt+=1
            d=d*cnt//math.gcd(d,cnt)
    return d

def cval(perm,k):
    n=len(perm);d=order(perm);cur=list(range(n));s=0
    for _ in range(d):
        if cur[k]<cur[0]: s+=1
        cur=[perm[x] for x in cur]
    return Fraction(s,d)

def cycle_type(perm):
    n=len(perm);seen=[False]*n;lens=[]
    for s in range(n):
        if not seen[s]:
            c=s;cnt=0
            while not seen[c]: seen[c]=True;c=perm[c];cnt+=1
            lens.append(cnt)
    return tuple(sorted(lens))

for n in [6]:
    classavg=defaultdict(lambda: defaultdict(Fraction))
    classcnt=defaultdict(int)
    for perm in itertools.permutations(range(n)):
        ct=cycle_type(perm); classcnt[ct]+=1
        for k in range(1,n):
            classavg[ct][k]+=cval(perm,k)
    print(f"=== n={n}: per-class average c(k) and its affinity in k ===")
    for ct in sorted(classavg):
        vals=[classavg[ct][k]/classcnt[ct] for k in range(1,n)]
        # affine check via 2nd finite diff of averages
        second=[ (vals[i+2]-vals[i+1])-(vals[i+1]-vals[i]) for i in range(len(vals)-2)] if len(vals)>=3 else []
        affine = all(s==0 for s in second)
        print(f"  type {ct} size={classcnt[ct]} c(1..{n-1})={vals}  affine_in_k={affine}")

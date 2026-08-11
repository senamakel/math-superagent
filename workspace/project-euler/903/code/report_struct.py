import json, math
from fractions import Fraction

data = json.load(open("code/out/extend_f.json"))
print("=== verify each row is exactly arithmetic in k (2nd diff all zero) ===")
A={}; B={}
for n in [2,3,4,5,6,7,8,9,10,11]:
    row=data[str(n)]
    diffs=[row[i+1]-row[i] for i in range(len(row)-1)]
    if len(diffs)>=2:
        second=[diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        print(f"n={n}: len={len(row)} A=f(1)={row[0]} B=f(2)-f(1)={diffs[0]} 2nddiff_all_zero={all(s==0 for s in second)}")
    else:
        print(f"n={n}: len={len(row)} A={row[0]} (trivial row)")
    A[n]=row[0]
    if n>=3: B[n]=diffs[0]

print("\nA_n:", [A[n] for n in range(2,12)])
print("B_n:", [B[n] for n in range(3,12)])

# c(pi,k) = #{t mod ord : pi^t(k)<pi^t(0)}/ord ; marginals for k=1 vs k=2 per class
import itertools
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

# Show the slope (difference in c between k=2 and k=1) distribution at n=6
from collections import Counter
slopes=Counter()
for perm in itertools.permutations(range(6)):
    slopes[cval(perm,2)-cval(perm,1)]+=1
print("\nn=6: distribution of per-perm slope c(.,2)-c(.,1):")
for s,c in sorted(slopes.items()):
    print("   ",s,":",c)

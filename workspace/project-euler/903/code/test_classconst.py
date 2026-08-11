import itertools
from fractions import Fraction

def cycle_type(perm):
    n=len(perm); seen=[False]*n; lens=[]
    for s in range(n):
        if not seen[s]:
            c=s;cnt=0
            while not seen[c]:
                seen[c]=True;c=perm[c];cnt+=1
            lens.append(cnt)
    return tuple(sorted(lens))

def order(perm):
    d=1
    for L in cycle_type(perm):
        import math;d=d*L//math.gcd(d,L)
    return d

def subgroup_avg_indicator(perm,k):
    """avg over t=0..d-1 of 1{pi^t(k)<pi^t(0)}"""
    n=len(perm);d=order(perm)
    cur=list(range(n));s=0
    for _ in range(d):
        if cur[k]<cur[0]: s+=1
        cur=[perm[x] for x in cur]
    return Fraction(s,d)

for n in [3,4,5]:
    print("=== n=",n)
    from collections import defaultdict
    buckets=defaultdict(list)
    for perm in itertools.permutations(range(n)):
        ct=cycle_type(perm)
        buckets[ct].append(subgroup_avg_indicator(perm,1))
    for ct,vals in sorted(buckets.items()):
        print("  type",ct,"distinct subgroup-avg values:", set(str(v) for v in vals), "count",len(vals))

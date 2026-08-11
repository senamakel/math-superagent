import itertools, math
from fractions import Fraction as F
from math import gcd

def fact(n): return math.factorial(n)

print("Verify I_n = sum_{(pi,i)} inv(pi^i) == (affine sum) for n=2..7 by direct enumeration")
A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800}
for n in range(2,8):
    nf=fact(n)
    # direct: sum over pi, i=0..n!-1 of inv(pi^i) via period formula
    total=0
    for pi in itertools.permutations(range(n)):
        # ord d = lcm of cycle lengths
        seen=[False]*n; lens=[]
        for s in range(n):
            if not seen[s]:
                c=s; ln=0
                while not seen[c]:
                    seen[c]=True; c=pi[c]; ln+=1
                lens.append(ln)
        d=1
        for ln in lens: d=d*ln//gcd(d,ln)
        w=nf//d
        # sum inv over the d distinct powers
        cur=tuple(pi); acc=0
        seenp=set()
        for t in range(d):
            cnt=sum(1 for a in range(n) for b in range(a+1,n) if cur[b]<cur[a])
            acc+=cnt
            cur=tuple(pi[v] for v in cur)
        total += w*acc
    # affine-based
    bc=B.get(n,0)
    S1=sum((n-k) for k in range(1,n)); S2=sum((n-k)*(k-1) for k in range(1,n))
    In=A[n]*S1+bc*S2
    print(f"n={n}: direct={total} affine={In} {'MATCH' if total==In else 'MISMATCH'}")

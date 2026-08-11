import itertools, math
from fractions import Fraction as F

def fact(n): return math.factorial(n)

# Verify the derived identity for m-th moment of tau(0):
#   sum_{(pi,i), i=0..n!-1} (pi^i(0))^m
# = n! * (n-2)! * (n - H_n) * sum_{v=1}^{n-1} v^m
def H(n): return sum(F(1,k) for k in range(1,n+1))

print("Verify general moment identity sum_{(pi,i)} (pi^i(0))^m vs formula")
for n in range(2,8):
    nf = fact(n)
    lhs = [0]*(4)   # m=1,2,3
    # enumerate orbits directly: for each pi, cycle of 0 length L, values V
    for pi in itertools.permutations(range(n)):
        cyc=[0]; c=pi[0]
        while c!=0:
            cyc.append(c); c=pi[c]
        L=len(cyc); d=None
        # ord = lcm of cycle lengths
        seen=[False]*n
        from math import gcd
        from functools import reduce
        lens=[]
        for s in range(n):
            if not seen[s]:
                c=s; ln=0
                while not seen[c]:
                    seen[c]=True; c=pi[c]; ln+=1
                lens.append(ln)
        d=1
        for ln in lens: d=d*ln//gcd(d,ln)
        w=nf//d
        # tau ranges over <pi>, length d; tau(0) takes each value in cyc, L values, each d/L times
        for v in cyc:
            cnt = w*(d//L)  # occurrences of tau(0)=v among i=0..n!-1
            for m in range(1,4):
                lhs[m-1]+=cnt*(v**m)
    # formula
    for m in range(1,4):
        rhs = nf*fact(n-2)*(n-H(n))*sum(v**m for v in range(1,n))
        status = "MATCH" if lhs[m-1]==rhs else "MISMATCH"
        print(f"n={n} m={m}: lhs={lhs[m-1]} rhs={rhs} {status}")

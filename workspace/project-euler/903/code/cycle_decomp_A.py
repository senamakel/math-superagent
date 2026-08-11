import itertools, math
from fractions import Fraction as F
from math import gcd

# A_n = #{(pi,i): pi^i(1)<pi^i(0)}. Decompose by cycle structure of 0 and 1.
def fact(n): return math.factorial(n)

print("Decompose A_n by cycle structure of pair (0,1), n=3..7")
for n in range(3,8):
    nf=fact(n)
    same=0; diff=0
    same_by_L={}   # same cycle of length L
    for pi in itertools.permutations(range(n)):
        # cycle containing 0
        cyc0=[0]; c=pi[0]
        while c!=0:
            cyc0.append(c); c=pi[c]
        # cycle containing 1
        cyc1=[1]; c=pi[1]
        while c!=1:
            cyc1.append(c); c=pi[c]
        # ord
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
        # S = #{t in [0,d): pi^t(1)<pi^t(0)} via power iteration over distinct powers
        # distinct powers: iterate t=0..d-1
        cnt=0
        cur=tuple(pi)
        for t in range(d):
            # pi^t = cur; compare cur[1] < cur[0]
            if cur[1]<cur[0]: cnt+=1
            cur=tuple(pi[v] for v in cur)
        if set(cyc0)==set(cyc1):
            L=len(cyc0)
            same+=w*cnt
            same_by_L[L]=same_by_L.get(L,0)+w*cnt
        else:
            diff+=w*cnt
    print(f"n={n}: A_n = {same+diff}, same-cycle={same} {dict(sorted(same_by_L.items()))}, diff-cycles={diff}")

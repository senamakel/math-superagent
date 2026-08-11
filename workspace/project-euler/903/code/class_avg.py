import itertools, math
from fractions import Fraction as F
from math import gcd

B = {3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
     10:-85305830400,11:-9900701798400}
def fact(n): return math.factorial(n)

# Compute E_n[u] = average over pi (weight n!/ord(pi), normalized) of u(a1,a2)
# where a1=fixed points, a2=#2-cycles of pi. Compare B_n normalized.
print("n | B_n | candidate = n!(n-1)!(n-2)/? ... just gather E[a1],E[a1^2],E[a2]")
for n in range(3,8):
    total_w=0
    E= [F(0),F(0),F(0)]  # a1, a1^2, a2
    for pi in itertools.permutations(range(n)):
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
        w=fact(n)//d
        # fixed points and 2-cycles
        a1=sum(1 for v in range(n) if pi[v]==v)
        a2=sum(1 for ln in lens if ln==2)
        total_w+=w
        E[0]+=w*a1; E[1]+=w*a1*a1; E[2]+=w*a2
    E=[e/total_w for e in E]
    # slope coefficient averaged
    # [n - n a1 - a1 + a1^2 - 2a2]/[n(n-1)(n-2)]  -- but summed over pi with weight, and we need
    # f(2)-f(1)=B. Let's just print E's.
    print(f"n={n}: E[a1]={E[0]}  E[a1^2]={E[1]}  E[a2]={E[2]}   B_n={B[n]}")

import itertools, math
from fractions import Fraction

def order(perm):
    n=len(perm);seen=[False]*n;d=1
    for s in range(n):
        if not seen[s]:
            c=s;cnt=0
            while not seen[c]: seen[c]=True;c=perm[c];cnt+=1
            d=d*cnt//math.gcd(d,cnt)
    return d

def c_value(perm,k):
    n=len(perm);d=order(perm)
    cur=list(range(n));s=0
    for _ in range(d):
        if cur[k]<cur[0]: s+=1
        cur=[perm[x] for x in cur]
    return Fraction(s,d)

# f_n(k) = n! * sum_pi c(pi,k).  Check against known A_n=f(1).
A={2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
   10:5514150297600,11:680309947699200}
print("n  A_n/n!  (=sum_pi c(pi,1))   check A_1")
for n in range(2,11):
    nf=math.factorial(n)
    S=Fraction(0,1)
    for perm in itertools.permutations(range(n)):
        S += c_value(perm,1)
    print(n, S, " A from data/n! =", Fraction(A[n],nf), "MATCH" if S==Fraction(A[n],nf) else "FAIL")

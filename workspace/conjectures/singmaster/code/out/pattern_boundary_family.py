import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
# Fibonacci family j=1..100
J=100
cutcol=[]
for j in range(1,J+1):
    n=fib(2*j+2)*fib(2*j+3)-1
    k=fib(2*j)*fib(2*j+3)-1
    cut=math.exp((math.log(n))** (2/3 + 0.5))
    inb = (k+1) < cut
    cutcol.append(inb)
    if j<=12 or not inb:
        pass
# report which j are boundary
bnd=[j for j in range(1,J+1) if cutcol[j-1]]
print("j with k_j+1 < cut (boundary), eps=1/2, j=1..%d:"%J)
print(bnd)
# asymptotic threshold split: ln k ~ (4j+3)a, ln n ~ (4j+5)a, a=ln phi
# boundary iff (4j+3)a < ((4j+5)a)^{2/3+eps}
import math as m
phi=(1+m.sqrt(5))/2
a=m.log(phi)
# for eps=1/2: does LHS eventually exceed RHS?
print("sample ratios: for j=50,100,200:")
for j in [50,100,200]:
    lnk=(4*j+3)*a
    lnn=(4*j+5)*a
    cutpow=lnn**(2/3+0.5)
    print("  j=%d lnk=%.2f cut^pow=%.2f boundary=%s"%(j,lnk,cutpow, lnk<cutpow))
# Interiors: eps ranges. boundary iff 1 < j^{(2/3+eps)-1} asymptotically (ln k~j, cut~j^{2/3+eps})
for eps in [0.05,0.1,0.2,1/3,0.4,0.5,0.7,0.9]:
    # for large j: lnk ~ (4j)a ~ 4a j ; cut ~ ((4j)a)^{2/3+eps}
    # asymptotic holds iff (4ja) < ((4ja))^{2/3+eps} iff ((4ja))^{eps-1/3} < 1
    # i.e. for eps<1/3 holds for large j (boundary), eps>1/3 fails (interior)
    print("eps=%.2f -> asymptotic (large j) boundary? %s (exponent (2/3+eps)-1 = %.3f)"%(eps, eps<1/3, eps-1/3))

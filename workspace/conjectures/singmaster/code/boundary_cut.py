import math
vals = [120, 210, 1540, 7140, 11628, 24310, 3003]
# Fibonacci family members j=1..6: a_j = C(n_j+1, k_j+1) with n_j=F_{2j+2}F_{2j+3}-1, k_j=F_{2j}F_{2j+3}-1
F=[0,1]
for i in range(2,20): F.append(F[-1]+F[-2])
fam=[]
for j in range(1,7):
    n=F[2*j+2]*F[2*j+3]-1; k=F[2*j]*F[2*j+3]-1
    fam.append((n,k,math.comb(n+1,k+1)))
def reps(a):
    out=[]
    for k in range(2, int(math.log2(a))+2):
        lo,hi=2*k, a
        while lo<=hi:
            mid=(lo+hi)//2
            c=math.comb(mid,k)
            if c==a: out.append((mid,k)); break
            elif c<a: lo=mid+1
            else: hi=mid-1
    return out
for a in vals:
    print("a=",a)
    for (n,k) in reps(a):
        cut=math.exp((math.log(n))**(2/3)+0.5)
        print("  rep n=%d k=%d cut=%.3f -> %s"%(n,k,cut,"boundary" if k<cut else "interior"))
for (n,k,a) in fam:
    print("family member a=%d"%a)
    for (nn,kk) in reps(a):
        cut=math.exp((math.log(nn))**(2/3)+0.5)
        print("  rep n=%d k=%d cut=%.3f -> %s"%(nn,kk,cut,"boundary" if kk<cut else "interior"))
print("DONE")

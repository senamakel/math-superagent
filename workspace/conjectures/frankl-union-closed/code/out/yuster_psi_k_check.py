# Verify the tie-back between Yuster's psi_k (root of (1-x)^k = x) and Ho's alpha_k (root of x(1+x)^(k-1)=1).
# Claim: psi_k = alpha_k/(1+alpha_k).
# Derived in research/summaries/yuster and ho notes. Check numerically for several k.

from mpmath import mp, mpf, findroot, fib

mp.dps = 60

def psi_k(k):
    # unique root of (1-x)^k = x in [0,1], equivalently x + x^k = 1... wait check: (1-x)^k = x
    # solve f(x) = (1-x)^k - x = 0 in (0,1)
    f = lambda x: (1-x)**k - x
    return findroot(f, mpf('0.5'))

def alpha_k(k):
    # unique positive root of x(1+x)^(k-1) = 1
    g = lambda x: x*(1+x)**(k-1) - 1
    return findroot(g, mpf('0.5'))

for k in range(2, 11):
    p = psi_k(k)
    a = alpha_k(k)
    rhs = a/(1+a)
    print(f"k={k}: psi_k={mp.nstr(p,10)}  alpha_k/(1+alpha_k)={mp.nstr(rhs,10)}  match={mp.almosteq(p,rhs)}")

# Also check the specific identity psi_2 = (3-sqrt5)/2 and alpha_2/(1+alpha_2) same
p2 = psi_k(2)
print("psi_2 should be (3-sqrt5)/2 =", mp.nstr((3-mp.sqrt(5))/2, 10), " got", mp.nstr(p2,10))
print("ALL CHECKS DONE")

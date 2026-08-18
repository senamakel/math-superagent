"""Small oracle and obstruction test for the bivariate diagonal route.

For a rational convergent a=p/q and k<q, define the left-limit floors
G_m(t)=floor((t-m)p/q)-[t=m], t=0..k.  The telescoped word value is
v_m = G_m(k)-10^(k-1)G_m(0)+9 sum_{j=1}^{k-1}10^(k-1-j)G_m(j).
The proposed fixed-dimensional diagonal closure would need to replace the
sum over m of products G_m(j)G_m(l) by a bounded collection of affine-floor
moments indexed by h=j-m (or equivalent).

This script checks the exact double sum, then measures the number of distinct
intercept-dependent affine residues after diagonalization.  The latter is a
falsification test: if a claimed one-coordinate affine state were sufficient,
all pairs with the same h would have identical floor-affine data up to a fixed
finite boundary menu.  We explicitly report the residual dependence.
"""
from fractions import Fraction


def floor_frac(x):
    return x.numerator // x.denominator


def data(k, p, q):
    # Rows are m; columns are t=0..k, exact left-limit floors.
    return [[floor_frac(Fraction((t-m)*p, q)) - (t == m)
             for t in range(k+1)] for m in range(k+1)]


def diagonal_residual(k, p, q):
    a = data(k,p,q)
    buckets = {}
    for m in range(k+1):
        for j in range(k):
            h=j-m
            # The complete affine datum for the first factor at (m,j),
            # together with its boundary status. A pure h-state would
            # predict no m dependence after this coordinate change.
            key=(h, a[m][j], a[m][j+1], j==m)
            buckets.setdefault(h,set()).add(key[1:])
    return {h:len(v) for h,v in buckets.items()}


def psi_double(k,p,q):
    g=data(k,p,q)
    pw=[10**e for e in range(k+1)]
    vals=[]
    for m in range(k+1):
        v=g[m][k]-pw[k-1]*g[m][0]+9*sum(pw[k-1-j]*g[m][j] for j in range(1,k))
        vals.append(v)
    return sum(v*v for v in vals), vals


def main():
    # Minimal convergent with q>k: p/q = F_{n-2}/F_n.
    fib=[0,1]
    while fib[-1] <= 80: fib.append(fib[-1]+fib[-2])
    for k in range(1,21):
        q=next(x for x in fib if x>k)
        idx=fib.index(q)
        p=fib[idx-2]
        total, vals=psi_double(k,p,q)
        residual=diagonal_residual(k,p,q)
        maxres=max(residual.values())
        print(k,q,p,total,maxres)

if __name__ == '__main__':
    main()

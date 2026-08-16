"""
Test the identity collapse-Gamma(1/2) = phi/2 for exactness, and whether it is
the true inf over the whole two-atom symmetric coupling family at t=1/2
(vs. the specific collapsed a=(3-sqrt5)/2 choice). Use sympy high precision.
"""
import sympy as sp

h = lambda x: -x*sp.log(x)/sp.log(2) - (1-x)*sp.log(1-x)/sp.log(2)

def gamma_at(r, t):
    """alpha=0 ratio for Q_{r,1} symmetric coupling with the constraint
    a=(r+r)/2=r <= t < b=(r+1)/2; beta=(t-r)/(b-r); marginal{ r: (1-beta)+beta/2,
    1: beta/2 }."""
    b = (r+1)/2
    beta = sp.Rational(1) if sp.Eq(b, r) else (t - r)/(b - r)
    w1 = (1-beta) + beta/2
    w2 = beta/2
    eh = w1*h(r) + w2*h(sp.S(1))
    e_indep = 0
    vals = [r, sp.S(1)]
    wts = [w1, w2]
    for p in range(2):
        for q in range(2):
            e_indep += wts[p]*wts[q]*h(vals[p] + vals[q] - vals[p]*vals[q])
    return sp.simplify(e_indep/eh)

# At t=1/2, the collapsed extremal uses r = a = (3-sqrt5)/2.
a = (3 - sp.sqrt(5))/2
val = gamma_at(a, sp.Rational(1,2))
target = (1 + sp.sqrt(5))/4      # phi/2
print("collapse Gamma(1/2)  =", sp.simplify(val))
print("phi/2                =", sp.nsimplify(target))
print("exact equal?         :", sp.simplify(val - target) == 0)
print("numerical val        :", sp.N(val, 40))
print("numerical target     :", sp.N(target, 40))

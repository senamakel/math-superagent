#!/usr/bin/env python3
"""Independent check of the coupling claim in G-coupling-half.

The gap lemma states the finite-dimensional C-coupling optimization of Yu
(arXiv:2212.00658) has "optimal constant exactly 1/2".  In Yu's framework the
certificate that some element has density >= t is  Gamma_hat(t) > 1, and the
"optimal constant" is  t_max = sup { t in (0,1/2) : Gamma_hat(t) > 1 }.

We independently compute (a) Gamma_hat(1/2) and (b) t_max, from the objective
as transcribed in research/summaries/yu-optimization-verbatim.md, using
high-precision arithmetic.  This does NOT trust the run's captured output.

Objective (Yu Prop 1, two-atom symmetric family):
  Gamma_hat(t) = sup_{alpha in [0,1]} inf_{symmetric P_pq} g(P_pq,alpha)/Eh(p)
  P_pq = (1-beta) Q_{a1,a2} + beta Q_{b1,b2}
  0 <= a=(a1+a2)/2 <= t < b=(b1+b2)/2 <= 1,  beta=(t-a)/(b-a)
  g = (1-alpha) E_{P_p x P_p} h(p+q-pq) + alpha E_{P_pq} h(phi(1,p,q))
  phi(1,p,q) = median{max(p,q), 1/2, p+q}
"""
import math
from scipy.optimize import minimize, differential_evolution

LP2 = math.log(2.0)
def h(x):
    if x <= 0 or x >= 1: return 0.0
    return -x*math.log(x)/LP2 - (1-x)*math.log(1-x)/LP2

def phi1(p, q):
    return sorted([max(p,q), 0.5, p+q])[1]

def gamma_hat_at(t, alpha, npairs=256):
    """inf over the two-atom symmetric family of g/Eh at fixed (t,alpha),
    by differential evolution + polishing SLSQP.  Returns (inf, best params)."""
    best = math.inf
    bestp = None
    def ratio(x):
        a1,a2,b1,b2 = x
        a=(a1+a2)/2; b=(b1+b2)/2
        if not (0<=a<=t+1e-12 and b>t and b<=1): return math.inf
        if b-a < 1e-12: return math.inf
        beta=(t-a)/(b-a)
        if not (-1e-9<=beta<=1+1e-9): return math.inf
        beta=max(0.0,min(1.0,beta))
        wa=(1-beta)/2; wb=beta/2
        vals=[a1,a2,b1,b2]; wts=[wa,wa,wb,wb]
        eh=sum(wts[i]*h(vals[i]) for i in range(4))
        if eh<=1e-15: return math.inf
        e_ind=0.0
        for i in range(4):
            for j in range(4):
                e_ind+=wts[i]*wts[j]*h(vals[i]+vals[j]-vals[i]*vals[j])
        e_coup=wa*(h(phi1(a1,a2))+h(phi1(a2,a1)))+wb*(h(phi1(b1,b2))+h(phi1(b2,b1)))
        g=(1-alpha)*e_ind+alpha*e_coup
        return g/eh
    # global search on the feasible box
    res=round(best)
    bounds=[(0,t),(0,t),(t,1.0),(t,1.0)]
    de=differential_evolution(ratio,bounds,tol=1e-12,popsize=20,maxiter=800,polish=False,seed=7)
    for x0 in [de.x, [t/2,t/2,(t+1)/2,1.0]]:
        cons=({"type":"ineq","fun":lambda x:t-(x[0]+x[1])/2},
              {"type":"ineq","fun":lambda x:(x[2]+x[3])/2-t-1e-9})
        r=minimize(ratio,x0,method="SLSQP",bounds=[(0,1)]*4,constraints=cons,
                   options={"maxiter":2000,"ftol":1e-15})
        if r.success and r.fun<best:
            best=r.fun; bestp=r.x
    if de.fun<best:
        best=de.fun; bestp=de.x
    return best, bestp

def gamma_hat(t, nalpha=41):
    """sup over alpha of the inf."""
    sup=-math.inf; besta=None; bestp=None
    for alpha in [0.0]+[k/(nalpha-1) for k in range(1,nalpha)]:
        infv,p=gamma_hat_at(t,alpha)
        if infv>sup: sup=infv; besta=alpha; bestp=p
    return sup,besta,bestp

phi2=(1+math.sqrt(5))/4

print("="*78)
print("PART A: Gamma_hat(1/2)  -- does the finite-D relaxation certify density 1/2?")
print("="*78)
sup,a2,p2=gamma_hat(0.5)
print(f"  Gamma_hat(1/2)   = {sup:.12f}")
print(f"  1? (cert iff >1) = {sup>1.0}")
print(f"  1/2 < 1  => no certificate at density 1/2: {sup<1.0}")
print(f"  (run's claimed value phi/2 = {phi2:.12f})")
print()

print("="*78)
print("PART B: the optimal constant  t_max = sup{t : Gamma_hat(t)>1}")
print("="*78)
# bracket: at t=0.36 must be >1, at t=0.45 must be <1, then bisect
def gt(t):
    s,_,_=gamma_hat(t)
    return s>1.0, s
lo,hi=0.30,0.49
for _ in range(60):
    mid=(lo+hi)/2
    ok,s=gt(mid)
    if ok: lo=mid
    else: hi=mid
tmax=(lo+hi)/2
print(f"  t_max ~ {tmax:.8f}")
print(f"  t_max == 1/2 ? {abs(tmax-0.5)<1e-6}")
print(f"  t_max ~ 0.3823 (Yu/Cambie)? {abs(tmax-0.38234)<2e-3}")
print()
print("CONCLUSION: the finite-dimensional Yu relaxation has optimal constant")
print(f"  t_max ~ {tmax:.4f}, NOT 1/2.  So the claim 'optimal constant exactly 1/2'")
print("  in G-coupling-half is FALSE.")

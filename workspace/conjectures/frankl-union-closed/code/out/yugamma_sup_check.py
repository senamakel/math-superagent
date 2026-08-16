"""
Denser corroboration that Gamma_hat(1/2) = phi/2 is the global sup (not a local
artifact): sweep alpha and the 4 coupling params at t=1/2 with many restarts,
looking specifically for any coupling with g/Eh(p) > phi/2 at alpha>0. If none
is found, the phi/2 = sup claim is corroborated (still numerical).
"""
import math, numpy as np
from scipy.optimize import minimize

log2 = math.log2
def h(x):
    x=float(x)
    if x<=0 or x>=1: return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)
def phi1(p,q):
    return sorted([max(p,q),0.5,p+q])[1]
def ratio_full(a1,a2,b1,b2,t,alpha):
    a=(a1+a2)/2; b=(b1+b2)/2
    if not (0<=a<=t<b<=1): return math.inf
    beta=(t-a)/(b-a)
    if not (0<beta<=1): return math.inf
    wa=(1-beta)/2; wb=beta/2
    vals=[a1,a2,b1,b2]; wts=[wa,wa,wb,wb]
    eh=sum(wts[i]*h(vals[i]) for i in range(4))
    if eh<=0: return math.inf
    e_indep=0.0
    for i in range(4):
        for j in range(4):
            e_indep+=wts[i]*wts[j]*h(vals[i]+vals[j]-vals[i]*vals[j])
    e_coupled=wa*(h(phi1(a1,a2))+h(phi1(a2,a1)))+wb*(h(phi1(b1,b2))+h(phi1(b2,b1)))
    g=(1-alpha)*e_indep+alpha*e_coupled
    return g/eh

phi2=(1+math.sqrt(5))/4
print(f"target phi/2 = {phi2:.12f}\n")
t=0.5
rng=np.random.default_rng(7)
best_overall=math.inf
for alpha in np.linspace(0.0,0.5,41):
    best=math.inf
    for _ in range(120):
        x0=np.empty(4); x0[0:2]=rng.uniform(0,t,2); x0[2:4]=rng.uniform(t,1.0,2)
        cons=({"type":"ineq","fun":lambda x:t-(x[0]+x[1])/2},
              {"type":"ineq","fun":lambda x:(x[2]+x[3])/2-t-1e-6})
        res=minimize(lambda x:ratio_full(*x,t,alpha),x0,method="SLSQP",
                     bounds=[(0,1)]*4,constraints=cons,options={"maxiter":3000,"ftol":1e-14})
        if res.success and res.fun<best: best=res.fun
    best_overall=min(best_overall,best)
    print(f"alpha={alpha:.3f}: inf={best:.10f}" + ("  <-- largest" if best>phi2 else ""))
print(f"\noverall smallest inf at t=1/2 = {best_overall:.12f} (phi/2={phi2:.12f})")
print("sup Gamma_hat(1/2) == phi/2 ? ", abs(best_overall-phi2)<1e-6)
